import { useState } from 'react'
import { Clipboard, FolderOpen, RotateCcw, XCircle } from 'lucide-react'
import { cancelJob, getJob, materializeWorkspace, retryJob } from '../api'
import type { Job } from '../types'

export default function JobPanel({
  jobs,
  onWorkspace,
  refresh,
}: {
  jobs: Job[]
  onWorkspace: (projectId: string) => void
  refresh: () => void
}) {
  const [detail, setDetail] = useState<any | null>(null)
  const open = async (id: string) => setDetail(await getJob(id))

  const copyDiagnostics = async () => {
    if (!detail) return
    const text = JSON.stringify(
      {
        id: detail.id,
        node_type: detail.node_type,
        state: detail.state,
        progress_message: detail.progress_message,
        diagnostics: detail.diagnostics,
        attempts: detail.attempts,
      },
      null,
      2
    )
    await navigator.clipboard.writeText(text)
  }

  return (
    <section className="jobs-panel glass">
      <div className="panel-title">Jobs / Queue</div>
      <div className="jobs-list">
        {jobs.slice(0, 8).map((j) => (
          <button
            key={j.id}
            className={`job-row ${j.state.toLowerCase()}`}
            onClick={() => open(j.id)}
          >
            <span>{j.id.slice(-6)}</span>
            <b>{j.state}</b>
            <small>{j.progress_message}</small>
            {j.error && <em className="job-error-preview">{formatErrorPreview(j.error)}</em>}
          </button>
        ))}
      </div>

      {detail && (
        <div className="job-detail">
          <div className="job-detail-title">
            <div>
              <b>{detail.id}</b>
              <small>{detail.node_type}</small>
            </div>
            <button className="icon-btn" onClick={() => setDetail(null)}>
              <XCircle size={14} />
            </button>
          </div>

          <div className={`job-state-banner ${detail.state.toLowerCase()}`}>
            <b>{detail.state}</b>
            <span>{detail.progress_message}</span>
          </div>

          {detail.diagnostics && (
            <div className="diagnostics-card">
              <div className="diagnostics-head">
                <b>Diagnostics</b>
                <button className="secondary-btn tiny" onClick={copyDiagnostics}>
                  <Clipboard size={12} /> Copy
                </button>
              </div>
              <div className="diag-grid">
                <span>Stage</span><code>{detail.diagnostics.stage ?? '-'}</code>
                <span>Exception</span><code>{detail.diagnostics.exception_type ?? '-'}</code>
                <span>Message</span><code>{detail.diagnostics.message ?? '-'}</code>
              </div>
              {detail.diagnostics.context && (
                <details open>
                  <summary>Context</summary>
                  <pre>{JSON.stringify(detail.diagnostics.context, null, 2)}</pre>
                </details>
              )}
              {detail.diagnostics.traceback && (
                <details>
                  <summary>Python traceback</summary>
                  <pre>{detail.diagnostics.traceback}</pre>
                </details>
              )}
            </div>
          )}

          {detail.attempts?.length > 0 && (
            <details className="attempts-block" open>
              <summary>Attempts ({detail.attempts.length})</summary>
              {detail.attempts.map((a: any) => (
                <div className="attempt-row" key={a.attempt_no}>
                  <b>#{a.attempt_no} · {a.state}</b>
                  <span>{a.provider} / {a.model || '-'}</span>
                  <small>{a.started_at} → {a.finished_at ?? 'running'}</small>
                </div>
              ))}
            </details>
          )}

          <div className="job-actions">
            {detail.state === 'COMPLETED' && detail.project_id && detail.node_type === 'asset_requirement_extractor' && (
              <button
                className="primary-btn"
                onClick={async () => {
                  await materializeWorkspace(detail.id)
                  onWorkspace(detail.project_id)
                  refresh()
                  setDetail(null)
                }}
              >
                <FolderOpen size={14} /> Open Workspace
              </button>
            )}
            <button
              className="secondary-btn tiny"
              onClick={async () => {
                await retryJob(detail.id)
                refresh()
              }}
            >
              <RotateCcw size={13} /> Retry
            </button>
            <button
              className="secondary-btn tiny"
              onClick={async () => {
                await cancelJob(detail.id)
                refresh()
              }}
            >
              Cancel
            </button>
          </div>
        </div>
      )}
    </section>
  )
}

function formatErrorPreview(error: string) {
  try {
    const d = JSON.parse(error)
    return `${d.exception_type ?? 'Error'}: ${d.message ?? ''}`.slice(0, 160)
  } catch {
    return error.slice(0, 160)
  }
}
