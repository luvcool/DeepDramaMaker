# Motion Keyframe Prompt Package Schema v0.1

권장 Markdown 블록:

```text
## MKF-EP01-S01-SH01
STATUS: READY | DRAFT | BLOCKED
DURATION: 2.0s
SOURCE: 09_motion/ep01-motion.json / SHOT-...

APPROVED_REFERENCES:
- ACTOR-001@v1 / FACE-FRONT45
- WARD-...
- LOC-... / VIEW-...
- PROP-... / STATE-...

INVARIANT_LOCK:
- ...

DELTA_ALLOWED:
- ...

START_STATE:
- ...

START_PROMPT_KO:
...

START_PROMPT_EN:
...

END_STATE:
- ...

END_PROMPT_KO:
...

END_PROMPT_EN:
...

NEGATIVE_DO_NOT_CHANGE:
- ...

QA_CHECKS:
- SAME_IDENTITY: PASS
- SAME_CAMERA: PASS
- CONTACT_TOPOLOGY: PASS
- VISIBILITY: PASS
- DELTA_ONLY: PASS
```

## ID

`MKF-EP{NN}-S{NN}-SH{NN}`

하나의 Motion Shot당 한 쌍을 기본으로 한다. Start-only 또는 End-only 모델 사용이 필요한 경우에도 패키지 내부에서는 두 상태를 유지하고 실제 생성 큐에서 사용 여부를 표시한다.

## generation-queue.md

최소 필드:

- MKF ID
- priority
- start status
- end status
- approved references
- generator/model slot
- generated file slot
- validation status
- notes

실제 파일 경로는 존재하는 생성 결과가 제공된 뒤에만 기록한다.
