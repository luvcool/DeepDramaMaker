import { useEffect, useState } from 'react'
import { RefreshCw, Zap, CheckCircle2, XCircle, ShieldCheck } from 'lucide-react'
import { getProvider, updateProvider, refreshProviderModels, testProvider } from '../../../../api'

interface LMStudioSettingsProps {
  onDirtyChange?: (isDirty: boolean) => void
  onSaveSuccess?: () => void
}

export default function LMStudioSettings({
  onDirtyChange,
  onSaveSuccess,
}: LMStudioSettingsProps) {
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [refreshing, setRefreshing] = useState(false)
  const [testing, setTesting] = useState(false)

  const [enabled, setEnabled] = useState(true)
  const [baseUrl, setBaseUrl] = useState('http://127.0.0.1:1234/v1')
  const [model, setModel] = useState('')
  const [timeoutSeconds, setTimeoutSeconds] = useState(180)
  const [maxRetries, setMaxRetries] = useState(3)
  const [temperature, setTemperature] = useState(0.1)
  const [autoSelectModel, setAutoSelectModel] = useState(true)
  const [structuredOutput, setStructuredOutput] = useState(true)
  const [apiToken, setApiToken] = useState('')

  const [availableModels, setAvailableModels] = useState<string[]>([])
  const [status, setStatus] = useState<'ONLINE' | 'OFFLINE' | 'DISABLED'>('OFFLINE')
  const [refreshMsg, setRefreshMsg] = useState<{ type: 'ok' | 'err'; text: string } | null>(null)
  const [testResult, setTestResult] = useState<any | null>(null)

  const [initialState, setInitialState] = useState<string>('')

  const loadData = async () => {
    setLoading(true)
    try {
      const data = await getProvider('LMSTUDIO_01')
      if (data) {
        setEnabled(data.enabled ?? true)
        setBaseUrl(data.base_url || 'http://127.0.0.1:1234/v1')
        setModel(data.model || '')
        setTimeoutSeconds(data.timeout_seconds ?? 180)
        setMaxRetries(data.max_retries ?? 3)
        setTemperature(data.temperature ?? 0.1)
        setAutoSelectModel(data.auto_select_model ?? true)
        setStructuredOutput(data.structured_output ?? true)
        setApiToken(data.api_token || '')
        setStatus(data.status || 'OFFLINE')
        if (data.available_models) {
          setAvailableModels(data.available_models)
        }

        const stateStr = JSON.stringify({
          enabled: data.enabled ?? true,
          baseUrl: data.base_url || 'http://127.0.0.1:1234/v1',
          model: data.model || '',
          timeoutSeconds: data.timeout_seconds ?? 180,
          maxRetries: data.max_retries ?? 3,
          temperature: data.temperature ?? 0.1,
          autoSelectModel: data.auto_select_model ?? true,
          structuredOutput: data.structured_output ?? true,
          apiToken: data.api_token || '',
        })
        setInitialState(stateStr)
      }
    } catch (e) {
      console.error(e)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    loadData()
  }, [])

  useEffect(() => {
    if (!initialState) return
    const currentStateStr = JSON.stringify({
      enabled,
      baseUrl,
      model,
      timeoutSeconds,
      maxRetries,
      temperature,
      autoSelectModel,
      structuredOutput,
      apiToken,
    })
    const dirty = currentStateStr !== initialState
    if (onDirtyChange) {
      onDirtyChange(dirty)
    }
  }, [
    enabled,
    baseUrl,
    model,
    timeoutSeconds,
    maxRetries,
    temperature,
    autoSelectModel,
    structuredOutput,
    apiToken,
    initialState,
    onDirtyChange,
  ])

  const handleRefreshModels = async () => {
    setRefreshing(true)
    setRefreshMsg({ type: 'ok', text: 'Refreshing models...' })
    try {
      const res = await refreshProviderModels('LMSTUDIO_01', baseUrl)
      if (res.success) {
        setAvailableModels(res.models || [])
        if (res.selected_model) {
          setModel(res.selected_model)
        }
        setRefreshMsg({ type: 'ok', text: res.message || `${(res.models || []).length} models found` })
        setStatus('ONLINE')
      } else {
        setRefreshMsg({ type: 'err', text: res.error || 'Failed to refresh models' })
      }
    } catch (e) {
      setRefreshMsg({ type: 'err', text: `Failed to refresh models: ${String(e)}` })
    } finally {
      setRefreshing(false)
    }
  }

  const handleTestConnection = async () => {
    setTesting(true)
    setTestResult(null)
    try {
      const res = await testProvider('LMSTUDIO_01', {
        base_url: baseUrl,
        model,
        api_token: apiToken,
      })
      setTestResult(res)
      if (res.status === 'ONLINE') {
        setStatus('ONLINE')
        if (res.models) {
          setAvailableModels(res.models)
        }
      } else {
        setStatus('OFFLINE')
      }
    } catch (e) {
      setTestResult({
        status: 'OFFLINE',
        endpoint: baseUrl.replace('http://', '').replace('https://', '').replace('/v1', ''),
        model,
        models_count: 0,
        response_time_ms: 0,
        error: String(e),
      })
      setStatus('OFFLINE')
    } finally {
      setTesting(false)
    }
  }

  const handleSave = async () => {
    setSaving(true)
    try {
      const payload = {
        enabled,
        base_url: baseUrl,
        model,
        timeout_seconds: timeoutSeconds,
        max_retries: maxRetries,
        temperature,
        auto_select_model: autoSelectModel,
        structured_output: structuredOutput,
        api_token: apiToken,
      }
      await updateProvider('LMSTUDIO_01', payload)

      const stateStr = JSON.stringify({
        enabled,
        baseUrl,
        model,
        timeoutSeconds,
        maxRetries,
        temperature,
        autoSelectModel,
        structuredOutput,
        apiToken,
      })
      setInitialState(stateStr)
      if (onDirtyChange) onDirtyChange(false)
      if (onSaveSuccess) onSaveSuccess()
    } catch (e) {
      alert(`Save failed: ${String(e)}`)
    } finally {
      setSaving(false)
    }
  }

  if (loading) {
    return <div className="settings-page-loading">LM Studio 설정 로드 중...</div>
  }

  const endpointDisplay = baseUrl.replace('http://', '').replace('https://', '').replace('/v1', '')

  return (
    <div className="settings-page">
      <div className="settings-header">
        <div>
          <h2>LM Studio</h2>
          <p className="settings-subtext">
            로컬 또는 원격 LM Studio LLM 추론 서버 연동 설정입니다.
          </p>
        </div>
        <div className={`status-badge-hero ${status === 'ONLINE' ? 'online' : 'offline'}`}>
          <span className="dot">●</span>
          <div>
            <b>{status === 'ONLINE' ? 'Online' : 'Offline'}</b>
            <small>{endpointDisplay || 'Remote Provider'}</small>
          </div>
        </div>
      </div>

      <div className="settings-section">
        <div className="setting-row toggle-row">
          <div>
            <label className="setting-label">Provider Enabled</label>
            <span className="setting-desc">LM Studio 서비스 활성화 여부</span>
          </div>
          <button
            type="button"
            className={`toggle ${enabled ? 'on' : ''}`}
            onClick={() => setEnabled(!enabled)}
          />
        </div>

        <div className="setting-field-group">
          <label className="setting-label">Base URL</label>
          <input
            type="text"
            className="setting-input"
            value={baseUrl}
            onChange={(e) => setBaseUrl(e.target.value)}
            placeholder="http://127.0.0.1:1234/v1"
          />
        </div>

        <div className="setting-field-group">
          <label className="setting-label">Model</label>
          <div className="input-with-button">
            <select
              className="setting-select"
              value={model}
              onChange={(e) => setModel(e.target.value)}
            >
              <option value="">Select a model</option>
              {availableModels.map((m) => (
                <option key={m} value={m}>
                  {m}
                </option>
              ))}
              {model && !availableModels.includes(model) && (
                <option value={model}>{model} (Current)</option>
              )}
            </select>
            <button
              type="button"
              className="secondary-btn tiny"
              disabled={refreshing}
              onClick={handleRefreshModels}
            >
              <RefreshCw size={13} className={refreshing ? 'spin' : ''} />
              {refreshing ? 'Refreshing...' : 'Refresh Models'}
            </button>
          </div>
          {refreshMsg && (
            <div className={`msg-banner ${refreshMsg.type}`}>
              {refreshMsg.text}
            </div>
          )}
        </div>

        <div className="setting-grid-2">
          <div className="setting-field-group">
            <label className="setting-label">Timeout (seconds)</label>
            <input
              type="number"
              className="setting-input"
              value={timeoutSeconds}
              onChange={(e) => setTimeoutSeconds(Number(e.target.value))}
            />
          </div>
          <div className="setting-field-group">
            <label className="setting-label">Max Retries</label>
            <input
              type="number"
              className="setting-input"
              value={maxRetries}
              onChange={(e) => setMaxRetries(Number(e.target.value))}
            />
          </div>
        </div>

        <div className="setting-field-group">
          <label className="setting-label">Temperature: {temperature}</label>
          <input
            type="range"
            min="0"
            max="1"
            step="0.05"
            className="setting-slider"
            value={temperature}
            onChange={(e) => setTemperature(Number(e.target.value))}
          />
        </div>

        <div className="setting-row toggle-row">
          <div>
            <label className="setting-label">Auto Select First Loaded Model</label>
            <span className="setting-desc">
              선택한 모델이 없거나 변경된 경우 목록의 첫 번째 모델을 자동으로 선택합니다.
            </span>
          </div>
          <button
            type="button"
            className={`toggle ${autoSelectModel ? 'on' : ''}`}
            onClick={() => setAutoSelectModel(!autoSelectModel)}
          />
        </div>

        <div className="setting-row toggle-row">
          <div>
            <label className="setting-label">Structured Output (JSON Schema)</label>
            <span className="setting-desc">
              JSON Schema 규격을 강제하여 정형화된 응답을 보장합니다.
            </span>
          </div>
          <button
            type="button"
            className={`toggle ${structuredOutput ? 'on' : ''}`}
            onClick={() => setStructuredOutput(!structuredOutput)}
          />
        </div>

        <div className="setting-field-group">
          <label className="setting-label">API Token (Optional)</label>
          <input
            type="password"
            className="setting-input"
            value={apiToken}
            onChange={(e) => setApiToken(e.target.value)}
            placeholder="lm-studio-token-xyz (Optional)"
          />
        </div>
      </div>

      <div className="settings-actions-zone">
        <button
          type="button"
          className="secondary-btn"
          disabled={testing}
          onClick={handleTestConnection}
        >
          <Zap size={14} />
          {testing ? 'Testing Connection...' : 'Test Connection'}
        </button>

        <button
          type="button"
          className="primary-btn"
          disabled={saving}
          onClick={handleSave}
        >
          <ShieldCheck size={14} />
          {saving ? 'Saving...' : 'Save LM Studio Settings'}
        </button>
      </div>

      {testResult && (
        <div className={`test-result-card ${testResult.status === 'ONLINE' ? 'success' : 'failed'}`}>
          <div className="test-result-header">
            {testResult.status === 'ONLINE' ? (
              <CheckCircle2 size={18} className="text-green" />
            ) : (
              <XCircle size={18} className="text-red" />
            )}
            <b>{testResult.status === 'ONLINE' ? 'Connected' : 'Connection Failed'}</b>
          </div>
          <div className="test-result-grid">
            <div>
              <span>Endpoint:</span>
              <b>{testResult.endpoint || 'N/A'}</b>
            </div>
            <div>
              <span>Selected Model:</span>
              <b>{testResult.model || 'None'}</b>
            </div>
            <div>
              <span>Models Available:</span>
              <b>{testResult.models_count ?? 0}</b>
            </div>
            <div>
              <span>Response Time:</span>
              <b>{testResult.response_time_ms} ms</b>
            </div>
          </div>
          {testResult.error && (
            <div className="test-result-error">
              <code>{testResult.error}</code>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
