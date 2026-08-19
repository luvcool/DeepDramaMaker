export default function QueueSettings() {
  return (
    <div className="settings-page">
      <div className="settings-header">
        <div>
          <h2>Queue & Jobs</h2>
          <p className="settings-subtext">작업 큐 동시성, 재시도 및 보관 정책 설정입니다.</p>
        </div>
      </div>
      <div className="coming-soon-card">
        <div className="coming-soon-badge">Coming Soon</div>
        <h3>Queue & Concurrent Workers</h3>
        <p>Default Max Retries, Concurrent Workers, Priority Policy 설정이 준비 중입니다.</p>
      </div>
    </div>
  )
}
