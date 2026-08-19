# Mir Studio MCP — 사용 안내서

AI 영상 제작 백엔드 세 개를 MCP 도구로 노출하는 서버다.

| 도구 | 백엔드 | 만드는 것 |
|---|---|---|
| `generate_video` | ComfyUI + MiniMax H3 | 세로 영상 클립(오디오 포함) |
| `generate_image` | ComfyUI + Qwen-Rapid-AIO | 이미지 |
| `generate_voice` | Scenema Audio | 한국어 TTS |
| `check_backends` | — | 연결 상태 확인 |

---

## 0. 먼저 알아야 할 것 (여기만은 읽어라)

이 셋을 모르면 반드시 헤맨다.

**① 파일 경로는 전부 "서버가 도는 컴퓨터" 기준이다.**
stdio 방식이라 서버는 클라이언트가 띄우는 **로컬 자식 프로세스**다. 도구는 이미지·오디오
바이트를 주고받지 않고 **경로 문자열**만 주고받는다. 넘기는 참조 파일도, 돌려받는 결과
파일도 서버 머신의 파일시스템에 있다. 클라이언트가 다른 컴퓨터에 있으면 그 경로를 읽지
못한다.

**② 오래 걸린다. 아주 오래.**

| 도구 | 1회 소요 |
|---|---|
| `generate_video` | **5~7분** |
| `generate_image` | 1~7분 |
| `generate_voice` | 10~30초 |

호출 타임아웃을 넉넉히 잡아라. 진행률 콜백은 없다 — 끝나야 돌아온다.

**③ 동시에 두 개를 돌리지 마라.**
ComfyUI 큐에서 경합해 **둘 다 느려진다**(실측: 400초짜리가 706초가 됐다).
영상·이미지를 여러 개 만들 때는 반드시 **순차**로 호출한다.

---

## 1. 설치

서버 머신에 Python 3.10+ 필요.

```bash
cd D:\Windy\mcp\mir-studio-mcp
pip install -r requirements.txt

copy config.example.json config.json
# config.json 의 voice_api_key 를 채운다

python server.py --selftest
```

`--selftest`는 백엔드 연결만 확인하고 끝난다(8초). **작업 시작 전에 반드시 통과시켜라.**
몇 시간짜리 배치를 헛돌리는 것보다 싸다.

### config.json

```json
{
  "comfy_server": "http://192.168.0.248:8188",
  "voice_server": "http://192.168.0.208:8000",
  "voice_api_key": "...",
  "output_dir": "D:/Windy/mcp/mir-studio-mcp/output",
  "voice_ref_base": ""
}
```

환경변수가 config.json을 덮어쓴다. 접두사는 `MIR_` —
`MIR_COMFY_SERVER`, `MIR_VOICE_API_KEY`, `MIR_OUTPUT_DIR` 등.

---

## 2. 클라이언트 등록

전송 방식은 **stdio**다. 클라이언트가 `python server.py`를 자식 프로세스로 띄운다.

### Claude Code / Claude Desktop / Cursor

```json
{
  "mcpServers": {
    "mir-studio": {
      "command": "python",
      "args": ["D:/Windy/mcp/mir-studio-mcp/server.py"]
    }
  }
}
```

`python`이 PATH에 없으면 전체 경로를 쓴다:
`"command": "C:/Users/<user>/AppData/Local/Programs/Python/Python312/python.exe"`

환경변수로 설정을 주고 싶으면:

```json
{
  "mcpServers": {
    "mir-studio": {
      "command": "python",
      "args": ["D:/Windy/mcp/mir-studio-mcp/server.py"],
      "env": {
        "MIR_VOICE_API_KEY": "...",
        "MIR_OUTPUT_DIR": "D:/work/out"
      }
    }
  }
}
```

### 직접 만든 프로그램 (Python)

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(
        command="python",
        args=[r"D:\Windy\mcp\mir-studio-mcp\server.py"],
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as s:
            await s.initialize()

            print([t.name for t in (await s.list_tools()).tools])

            r = await s.call_tool("generate_image", {
                "prompt": "a persimmon on a wooden table, soft window light",
                "width": 768, "height": 768,
                "out": "test.png",
            })
            print(r.content[0].text)      # JSON 문자열

asyncio.run(main())
```

> 반환값은 **JSON 문자열**로 온다. `json.loads()` 해서 쓴다.

### MCP 없이 그냥 쓰기

MCP 프로토콜이 부담스러우면 파이썬에서 직접 import해도 된다. 같은 함수다.

```python
import sys
sys.path.insert(0, r"D:\Windy\mcp\mir-studio-mcp")
import server as S

info = S.check_backends()
res  = S.generate_image(prompt="...", out="a.png", width=768, height=768)
```

---

## 3. 도구 레퍼런스

### check_backends

인자 없음. 작업 전 상태 확인용.

```json
{
  "comfy":  {"server": "...", "ok": true, "device": "cuda:0 ... RTX 4090",
             "vram_free_mb": 22815},
  "voice":  {"server": "...", "api_key_set": true, "ok": true, "body": {...}},
  "workflows": ["h3_i2v", "h3_r2v", "h3_r2v_turbo_lean", "h3_r2v_turbo_upscale",
                "qwen_aio", "qwen_aio_16x9"],
  "output_dir": "D:/Windy/mcp/mir-studio-mcp/output",
  "voice_roles": ["DOHYUN", "KUMIHO", "SEO", "SEO_K", "YURA"]
}
```

---

### generate_video

MiniMax H3로 영상 클립을 만든다. **오디오 트랙이 포함**돼 나온다(대사가 있으면 발화까지).

| 인자 | 타입 | 기본값 | 설명 |
|---|---|---|---|
| `prompt` | string | **필수** | 장면 서술. 아래 프롬프트 형식 참고 |
| `out` | string | `""` | 저장 경로. 상대경로면 `output_dir` 아래 |
| `mode` | string | `"r2v"` | `r2v`(참조 기반) 또는 `i2v`(첫 프레임 기반) |
| `ref_images` | string[] | `null` | **r2v 필수.** 배우·장소 참조 이미지 경로 |
| `ref_audios` | string[] | `null` | 음색 참조 wav, **최대 3개** |
| `image` | string | `""` | **i2v 필수.** 첫 프레임 이미지 |
| `last_image` | string | `""` | i2v 끝 프레임(선택) |
| `duration` | number | `5.5` | 초. 아래 길이 제약 반드시 참고 |
| `seed` | int | `-1` | `-1`이면 랜덤. 같은 시드+같은 해상도면 재현된다 |
| `workflow` | string | `"h3_r2v_turbo_lean"` | 아래 워크플로우 표 참고 |
| `aspect` | string | `"9:16 (Portrait Widescreen)"` | turbo 계열은 무시됨 |
| `megapixels` | number | `0.4` | turbo 계열은 무시됨 |
| `steps` | int | `20` | turbo 계열은 무시됨(4step LoRA 고정) |
| `timeout` | int | `3600` | 초 |

**반환**

```json
{
  "out": "D:\\...\\clip.mp4",
  "bytes": 4059155,
  "seconds": 312.3,
  "prompt_id": "9b18cf10-...",
  "seed": 11,
  "frames": 141,
  "actual_seconds": 5.875,
  "mode": "r2v",
  "workflow": "h3_r2v_turbo_lean.json"
}
```

#### ★ 길이 제약 — 요청한 길이대로 안 나온다

H3는 프레임 수를 **17k+5 그리드**로 스냅하고, 학습 범위가 **124~362프레임**이다.
24fps 기준 **5.17초 ~ 15.08초**만 실사용 가능하다.

| 요청 | 실제 |
|---|---|
| 4.0초 | **5.167초** (하한으로 올라감) |
| 5.2초 | 5.875초 |
| 10.0초 | 10.208초 |

**항상 반환값의 `actual_seconds`를 보고 후속 계산을 하라.** 요청값으로 타임라인을
짜면 어긋난다. 쓸 수 있는 값은 5.167 / 5.875 / 6.583 / 7.292 ... 로 이어진다.

#### 워크플로우

| 이름 | 해상도 | 비고 |
|---|---|---|
| `h3_r2v_turbo_lean` | 448×832 / 24fps | **기본 권장.** 세그당 ~300초(5~6초 클립) |
| `h3_r2v` | 가변(megapixels) | 비-turbo. steps 조정 가능 |
| `h3_i2v` | 가변 | i2v 전용 |
| `h3_r2v_turbo_upscale` | 928×1664 / 48fps | ⚠️ **아래 경고** |

> ⚠️ `h3_r2v_turbo_upscale`은 화질이 3.7배지만 **업스케일러가 얼굴을 다시 그려서
> 인물의 정체성이 바뀐다**(실측). 참조 이미지의 배우와 다른 사람이 나온다.
> 게다가 시간 이득도 없다(397초 vs 405~450초). **동일 인물이 여러 컷에 나오는
> 작업에는 쓰지 마라.** 단발 컷이고 화질이 최우선일 때만.

#### 프롬프트 형식 (r2v)

참조 이미지를 `<Subject N>` 라벨로 묶는 구조화 프롬프트를 쓴다. `ref_images` 순서가
`<Picture 1>`, `<Picture 2>` ... 에 대응한다.

```
subject_definitions:
<Subject 1> is the plain quiet woman in <Picture 1>, with long straight black hair
and thin round wire-rimmed glasses.
<Subject 2> is the location — the mansion living room in <Picture 2>: a long marble
table, a tall window wall with sheer curtains.

detailed_description:
A vertical close-up frames <Subject 1> from the chest up beside the tall window,
morning light behind her shoulder. She turns her head toward the window and her eyes
lower, then she draws one steady breath.
```

대사를 넣으려면 본문에 이렇게 쓴다:

```
<Subject 1> (S1), in a soft tired voice, says: <d>[Korean] 오늘은 좋아해 주겠지?</d>
```

`ref_audios`를 주면 그 목소리의 **음색**을 따라간다 — 신호를 복사하는 게 아니라
톤과 호흡을 참고하는 방식이다.

#### 실전 요령

- **참조 이미지는 배우 1장 + 장소 1장**이 기본. 인물이 둘이면 배우 2장 + 장소 1장
- **원거리 샷을 피하라.** 448×832에서 얼굴이 화면의 1/8보다 작아지면 뭉개져서
  참조와 다른 사람이 된다. 상체샷·클로즈업이 안전하다
- **대사 1줄당 1샷.** 한 클립에 대사를 2줄 넣으면 시간이 모자라 잘리거나 반복된다
- 실제 발화는 한국어 **약 0.19초/음절**로 잡고, 뒤에 동작 여유를 1~2초 남겨라

---

### generate_image

Qwen-Rapid-AIO로 이미지를 만든다.

| 인자 | 타입 | 기본값 | 설명 |
|---|---|---|---|
| `prompt` | string | **필수** | |
| `out` | string | `""` | 상대경로면 `output_dir` 아래 |
| `negative` | string | `""` | 네거티브 프롬프트 |
| `images` | string[] | `null` | 참조 이미지 **최대 3장**. 비우면 T2I |
| `width` / `height` | int | `1024` / `1536` | |
| `seed` | int | `-1` | |
| `workflow` | string | `"qwen_aio"` | 또는 `qwen_aio_16x9` |
| `timeout` | int | `600` | |

**반환**

```json
{"out": "...", "bytes": 553429, "seconds": 389.2, "prompt_id": "...",
 "seed": 7, "size": "768x768", "refs": 0, "workflow": "qwen_aio.json"}
```

**T2I / I2I는 `images`로 갈린다** — 비우면 텍스트만으로, 1~3장 주면 참조 편집으로
동작한다. 같은 인물의 다른 컷을 만들 때는 기존 이미지를 참조로 넣어야 얼굴이 유지된다.

---

### generate_voice

Scenema로 한국어 음성을 만든다.

| 인자 | 타입 | 기본값 | 설명 |
|---|---|---|---|
| `text` | string | **필수** | 읽을 대사 |
| `out` | string | `""` | wav 저장 경로 |
| `role` | string | `""` | 프리셋 배역. 아래 표 |
| `voice_desc` | string | `""` | 배역 대신 **자연어로 목소리 서술** |
| `gender` | string | `"female"` | `voice_desc`와 같이 쓴다 |
| `actions` | string[] | `null` | 연기 지시. 아래 설명 |
| `seed` | int | `42` | |
| `pace` | number | `1.5` | **클수록 느리다** |
| `reference_voice_url` | string | `""` | 음색 고정용 wav URL |
| `language` | string | `"ko"` | |
| `background_sfx` | boolean | `false` | |
| `timeout` | int | `900` | |

`role`과 `voice_desc` 중 **하나는 반드시** 필요하다.

**반환**

```json
{"out": "...", "duration_s": 3.49, "seconds": 12.0, "attempt": 1,
 "prompt": "<speak voice=\"...\">...</speak>"}
```

#### 배역 프리셋

| role | 목소리 |
|---|---|
| `SEO` | 30대 여성. 조용하고 지친 중저음, 감정을 눌러 담는다 |
| `SEO_K` | 30대 여성. 낮고 매끄러운 중저음에 서늘한 여유 |
| `DOHYUN` | 30대 남성. 차갑고 단정한 중저음 |
| `YURA` | 20대 여성. 밝고 달콤하지만 끝이 날카롭다 |
| `KUMIHO` | 나이 미상 여성. 낮고 울림이 깊고 느리다 |

프리셋이 안 맞으면 `voice_desc`로 즉석 캐스팅한다:

```json
{"voice_desc": "40대 한국인 남성. 굵고 거친 목소리, 말끝을 흐린다",
 "gender": "male", "text": "..."}
```

#### actions — 한 대사 안에서 감정이 바뀐다

이게 이 엔진의 핵심 기능이다. 여러 개를 주면 **문장 사이에 지시를 끼워 넣는다.**

```json
{
  "text": "어떻게... 나한테 이럴 수 있어! 내가 뭘 그렇게 잘못했는데!",
  "actions": ["울먹이며 목이 메어 시작한다", "마지막에 무너지듯 터진다"]
}
```

지시는 **한국어 연기 지시문**으로 쓴다. "angry" 같은 라벨보다
"소리치지 않는다. 목소리를 낮게 눌러 담고 떨림만 새어 나온다" 처럼 쓰면 훨씬 잘 나온다.

#### ★ 실제 길이는 추정보다 훨씬 길다

음절수 × 0.19초로 계산한 값의 **1.4~2.4배**로 나온다.

| 대사 | 추정 | 실측 |
|---|---|---|
| 여긴 아무도 안 와. | 1.33초 | 1.93초 |
| 여기서요? 누가 오면 어쩌려고. | 2.28초 | **5.41초** |

영상 슬롯에 맞출 때는 **반드시 반환값 `duration_s`를 보고** 결정하라.
추정으로 슬롯을 짜면 대사가 잘리거나 두 번 나온다.

#### ★ reference_voice_url — file:// 을 쓰지 마라

음색을 고정하려면 참조 wav의 **URL**을 준다. 업로드 엔드포인트는 없다.

```
✅ http://192.168.0.187:8899/ref_SEO.wav     ← 이걸 써라
⚠️ file://D:/path/ref.wav                    ← 동작하지만 원본을 삭제한다
❌ file:///D:/path/ref.wav  (슬래시 3개)      → 실패
❌ D:\path\ref.wav                            → "프로토콜 없음" 거절
```

> **`file://` 로 주면 서버가 참조 원본 파일을 지운다.** 1회용이라 배치에 못 쓴다.
> 여러 번 쓸 참조는 반드시 HTTP로 서빙하라. 간단히는:
> `python -m http.server 8899 --directory <참조폴더>`

`config.json`의 `voice_ref_base`를 설정해두면 `role`만 줘도 자동으로
`{base}/ref_{ROLE}.wav`를 참조로 붙인다.

---

## 4. 오류 처리

오류는 예외로 올라온다. MCP 클라이언트에서는 `isError` 응답으로 온다.

| 메시지 | 원인 | 대응 |
|---|---|---|
| `ComfyUI 실행 오류: ... CLIPTextEncode` | **간헐 오류** | 그냥 재시도하면 통과한다 |
| `타임아웃 N초` | 큐가 밀렸거나 GPU 점유 | `check_backends`로 큐 확인 |
| `실행은 끝났는데 원하는 형식의 출력이 없다` | 워크플로우가 다른 형식 저장 | 워크플로우 확인 |
| `파일 없음: ...` | 참조 경로가 **서버 머신 기준**이 아님 | 경로 확인 |
| `음성 API 키가 없다` | config 미설정 | `voice_api_key` 설정 |
| `WinError 10061 연결 거부` | 백엔드 서버가 꺼짐 | 해당 서버 기동 |

**자동 재시도는 넣지 않았다.** 5분짜리 작업을 조용히 두 번 돌리는 건 호출측이
결정할 일이라고 봤다. `generate_voice`만 예외적으로 3회 재시도한다(10~30초라 싸다).

영상은 이렇게 감싸 쓰기를 권한다:

```python
for attempt in range(3):
    try:
        res = generate_video(...)
        break
    except Exception as e:
        if "CLIPTextEncode" not in str(e) or attempt == 2:
            raise
        time.sleep(5)
```

---

## 5. 전형적인 작업 흐름

한 컷을 처음부터 만드는 순서다.

```
1) check_backends()                    상태 확인 (필수)

2) generate_image(                     배우 자산 만들기
     prompt="...", out="actor.png")

3) generate_voice(                     대사 음성 만들기
     role="SEO", text="...",
     actions=["..."], out="line.wav")
   → duration_s 를 보고 클립 길이 결정

4) generate_video(                     영상 만들기
     mode="r2v",
     ref_images=["actor.png", "loc.png"],
     ref_audios=["line.wav"],
     prompt="...<d>[Korean] 대사</d>...",
     duration=<3번에서 정한 값>,
     out="shot01.mp4")
   → actual_seconds 로 타임라인 확정

5) 여러 컷이면 4를 순차 반복 (동시 실행 금지)
```

---

## 6. 자주 겪는 문제

**"인물 얼굴이 참조와 다르다"**
원거리 샷이거나 `h3_r2v_turbo_upscale`을 썼을 가능성이 크다. 상체샷으로 바꾸고
`h3_r2v_turbo_lean`을 쓴다.

**"대사가 두 번 나온다 / 잘린다"**
클립 길이 대비 대사가 길거나 짧다. `generate_voice`의 `duration_s`로 실측한 뒤
`duration`을 다시 잡는다. 대사 뒤에 1~2초짜리 동작을 넣어 여백을 채우면 반복이 준다.

**"배경이 컷마다 바뀐다"**
장소 참조 이미지를 `ref_images`에 같이 넣고, 프롬프트에 그 장소의 구체적 요소
(창문·테이블 등)를 명시한다.

**"두 개를 동시에 돌렸더니 둘 다 느려졌다"**
정상이다. ComfyUI 큐 경합. 순차로 바꾼다.

**"결과 파일을 못 읽겠다"**
경로는 **서버 머신 기준**이다. 클라이언트가 다른 컴퓨터면 공유 폴더를 쓰거나
`output_dir`을 양쪽이 볼 수 있는 위치로 지정한다.
