import { useEffect, useState } from 'react'
import { Activity, RefreshCw, Save, Wrench } from 'lucide-react'
import { checkMcpBackends, getMcpServer, testMcpServer, updateMcpServer } from '../../../../api'

export default function MirStudioMcpSettings({
  onDirtyChange,
  onSaveSuccess,
}: {
  onDirtyChange?: (v: boolean) => void
  onSaveSuccess?: () => void
}) {
  const [cfg, setCfg] = useState<any | null>(null)
  const [saved, setSaved] = useState<any | null>(null)
  const [result, setResult] = useState<any | null>(null)
  const [busy, setBusy] = useState('')
  const serverId = 'MIR_STUDIO'

  useEffect(() => {
    void load()
  }, [])

  useEffect(() => {
    if (!cfg || !saved) return
    onDirtyChange?.(JSON.stringify(cfg) !== JSON.stringify(saved))
  }, [cfg, saved, onDirtyChange])

  const load = async () => {
    try {
      const x = await getMcpServer(serverId)
      setCfg(x)
      setSaved(x)
    } catch (e) {
      setResult({ ok: false, error: String(e) })
    }
  }

  const save = async () => {
    if (!cfg) return
    setBusy('save')
    try {
      const r = await updateMcpServer(serverId, cfg)
      setCfg(r.server)
      setSaved(r.server)
      setResult({ ok: true, message: 'MCP settings saved.' })
      onSaveSuccess?.()
    } catch (e) {
      setResult({ ok: false, error: String(e) })
    } finally {
      setBusy('')
    }
  }

  const test = async () => {
    setBusy('test')
    setResult(null)
    try {
      if (cfg) await updateMcpServer(serverId, cfg)
      setResult(await testMcpServer(serverId))
    } catch (e) {
      setResult({ ok: false, error: String(e) })
    } finally {
      setBusy('')
    }
  }

  const check = async () => {
    setBusy('check')
    setResult(null)
    try {
      if (cfg) await updateMcpServer(serverId, cfg)
      setResult(await checkMcpBackends(serverId))
    } catch (e) {
      setResult({ ok: false, error: String(e) })
    } finally {
      setBusy('')
    }
  }

  if (!cfg) return <div className="settings-page">Loading MCP settings...</div>

  const set = (key: string, value: any) => setCfg((x: any) => ({ ...x, [key]: value }))

  return (
    <div className="settings-page">
      <div className="settings-header">
        <div>
          <h2>Mir Studio MCP</h2>
          <p className="settings-subtext">stdio MCP · Image / Voice / MiniMax H3 Video</p>
        </div>
        <span className={`provider-status-badge ${cfg.enabled ? 'online' : 'disabled'}`}>● {cfg.enabled ? 'Enabled' : 'Disabled'}</span>
      </div>

      <div className="settings-warning">
        MCP의 파일 경로는 <b>server.py가 실행되는 PC 기준</b>입니다. generate_image / generate_video는 오래 걸리며 진행률 callback이 없으므로 DramaStudio Job Queue를 통해 순차 실행하세요.
      </div>

      <div className="settings-form-grid">
        <label className="settings-field wide">
          <span>Enabled</span>
          <input type="checkbox" checked={Boolean(cfg.enabled)} onChange={(e) => set('enabled', e.target.checked)} />
        </label>
        <label className="settings-field wide">
          <span>Python / Command</span>
          <input value={cfg.command ?? 'python'} onChange={(e) => set('command', e.target.value)} />
        </label>
        <label className="settings-field wide">
          <span>server.py path (first argument)</span>
          <input
            value={(cfg.args ?? [])[0] ?? ''}
            onChange={(e) => set('args', [e.target.value, ...(cfg.args ?? []).slice(1)])}
            placeholder="D:/Windy/mcp/mir-studio-mcp/server.py"
          />
        </label>
        <label className="settings-field wide">
          <span>Working directory (optional)</span>
          <input value={cfg.working_directory ?? ''} onChange={(e) => set('working_directory', e.target.value)} />
        </label>
        <label className="settings-field">
          <span>Timeout (sec)</span>
          <input type="number" value={cfg.timeout_seconds ?? 3600} onChange={(e) => set('timeout_seconds', Number(e.target.value))} />
        </label>
        <label className="settings-field">
          <span>Serialize Calls</span>
          <input type="checkbox" checked={Boolean(cfg.serialize_calls)} onChange={(e) => set('serialize_calls', e.target.checked)} />
        </label>
      </div>

      <div className="mcp-actions">
        <button className="secondary-btn" disabled={Boolean(busy)} onClick={test}><Wrench size={14}/>{busy === 'test' ? ' Testing...' : ' Test / List Tools'}</button>
        <button className="secondary-btn" disabled={Boolean(busy)} onClick={check}><Activity size={14}/>{busy === 'check' ? ' Checking...' : ' check_backends'}</button>
        <button className="primary-btn" disabled={Boolean(busy)} onClick={save}><Save size={14}/>{busy === 'save' ? ' Saving...' : ' Save'}</button>
      </div>

      {result && (
        <div className={`mcp-result ${result.ok ? 'ok' : 'bad'}`}>
          <div><b>{result.ok ? 'SUCCESS' : 'FAILED'}</b></div>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}

      <div className="settings-note-card">
        <RefreshCw size={15}/>
        <div>
          <b>Queue recommendation</b>
          <p>Mir Studio 문서 기준 generate_video는 5~7분, generate_image는 1~7분, generate_voice는 10~30초가 걸릴 수 있습니다. 영상/이미지 동시 실행은 피하고 Queue에서 순차 실행하는 것이 안전합니다.</p>
        </div>
      </div>
    </div>
  )
}
