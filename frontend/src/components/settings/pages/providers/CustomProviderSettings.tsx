export default function CustomProviderSettings() {
  return (
    <div className="settings-page">
      <div className="settings-header">
        <div>
          <h2>Custom API</h2>
          <p className="settings-subtext">OpenAI 호환 커스텀 API 엔드포인트 연동 설정입니다.</p>
        </div>
      </div>
      <div className="coming-soon-card">
        <div className="coming-soon-badge">Disabled / Coming Soon</div>
        <h3>Custom OpenAI-compatible API</h3>
        <p>Ollama, vLLM, LocalAI 등 사용자 정의 엔드포인트 연동 기능이 준비 중입니다.</p>
      </div>
    </div>
  )
}
