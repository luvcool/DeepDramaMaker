# DramaStudio System Architecture & Execution Specification v0.1

**LM Studio 기반 숏폼 드라마 제작 오케스트레이터 — 구현 전 고정 설계**

Status: Implementation-ready baseline  
Scope: v0.1  
Date: 2026-08-19

> 핵심 원칙: 완전 설계가 아니라, 첫 Vertical Slice를 안전하게 구현하기 위해 아키텍처·상태·데이터 계약·버전 규칙만 먼저 고정한다.

## 1. 문서 목적과 범위
DramaStudio는 숏폼 드라마 제작 워크플로우를 노드 기반 UI에서 실행하고, 다른 PC의 LM Studio를 포함한 AI Provider를 안정적으로 호출하며, 자산·작업·검증·버전을 영속 관리하는 오케스트레이터다.

## 2. 기술 스택
- Frontend: React + TypeScript
- Node Graph: React Flow / XYFlow 계열
- Desktop wrapper: Tauri (선택)
- Backend: FastAPI
- HTTP: httpx.AsyncClient
- ORM: SQLAlchemy 2
- DB: SQLite → PostgreSQL
- Queue: DB-backed Queue 우선
- Worker: Python asyncio
- File: Filesystem + DB metadata

## 3. 핵심 아키텍처
```text
Frontend → FastAPI → Orchestrator(DAG/Queue/Retry) → Workers → Provider Adapter → LM Studio
```

## 4. 핵심 설계 규칙
- Frontend가 LM Studio를 직접 호출하지 않는다.
- 모든 Provider 호출은 Job → JobAttempt 단위로 기록한다.
- Job 상태는 CREATED / QUEUED / WAITING_DEPENDENCY / DISPATCHING / RUNNING / STREAMING / VALIDATING / COMPLETED와 RETRY_WAIT / BLOCKED / FAILED / CANCELLED / UNKNOWN / INTERRUPTED를 사용한다.
- Asset는 `ACTOR_001@v1` 형식으로 버전 pinning한다.
- 승인 AssetVersion은 immutable이다.
- 모든 결과는 Artifact로 저장하고 Validator를 통과해야 downstream에서 사용한다.
- WorkflowVersion은 Node/Prompt/Schema/Provider 설정을 snapshot으로 고정한다.

## 5. 첫 Vertical Slice
```text
Script Input
→ Asset Requirement Extractor
→ LM Studio
→ requirements.raw.json
→ Schema Validator
→ requirements.json
→ UI Result Viewer
```

필수 기반 기능: Provider health, Queue/Job persistence, async worker, timeout/retry/cancel, structured output, WebSocket, crash recovery, artifact/version history.

## 6. LM Studio 공식 근거
- https://lmstudio.ai/docs/developer/core/server/serve-on-network
- https://lmstudio.ai/docs/developer/openai-compat
- https://lmstudio.ai/docs/developer/openai-compat/structured-output
- https://lmstudio.ai/docs/developer/rest

> 상세 설계는 DOCX 본문을 기준으로 한다.
