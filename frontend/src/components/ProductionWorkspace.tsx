import { useEffect, useState } from 'react'
import { WandSparkles, ImagePlus, Check, RefreshCw, Save } from 'lucide-react'
import {
  approveAssetImagePrompt,
  approveProductionDesign,
  createAssetImagePromptJob,
  createProductionDesignJob,
  getAssetImagePrompts,
  getProductionDesigns,
  updateAssetImagePrompt,
  updateProductionDesign,
} from '../api'

type Design = {
  id: number
  asset_id: string
  asset_type: string
  asset_name: string
  version: number
  status: string
  design: any
  locked_attributes: string[]
  variable_attributes: string[]
  required_views: string[]
  missing_attributes: string[]
}

type Prompt = {
  id: number
  asset_id: string
  asset_type: string
  view_id: string
  version: number
  status: string
  prompt: string
  negative_prompt: string
  invariant_lock: string[]
}

export default function ProductionWorkspace({
  projectId,
}: {
  projectId: string | null
}) {
  const [tab, setTab] = useState<'design' | 'prompts'>('design')
  const [designs, setDesigns] = useState<Design[]>([])
  const [prompts, setPrompts] = useState<Prompt[]>([])
  const [busy, setBusy] = useState(false)
  const [err, setErr] = useState('')

  const load = async () => {
    if (!projectId) return
    setErr('')
    try {
      setDesigns(await getProductionDesigns(projectId))
      setPrompts(await getAssetImagePrompts(projectId))
    } catch (e) {
      setErr(String(e))
    }
  }

  useEffect(() => {
    load()
  }, [projectId])

  if (!projectId) {
    return (
      <section className="production-workspace glass">
        <div className="workspace-empty">프로젝트를 먼저 선택하세요.</div>
      </section>
    )
  }

  const runDesign = async () => {
    setBusy(true)
    try {
      await createProductionDesignJob(projectId)
      setErr(
        'Production Designer job queued. Jobs 패널에서 진행 상태를 확인하세요.'
      )
    } catch (e) {
      setErr(String(e))
    } finally {
      setBusy(false)
    }
  }

  const runPrompts = async () => {
    setBusy(true)
    try {
      await createAssetImagePromptJob(projectId)
      setErr('Asset Image Prompt Compiler job queued.')
    } catch (e) {
      setErr(String(e))
    } finally {
      setBusy(false)
    }
  }

  return (
    <section className="production-workspace glass">
      <div className="pw-head">
        <div>
          <b>Production Design + Asset Image Prompt Compiler</b>
          <small>
            승인된 Project Asset/Casting을 재사용 가능한 이미지 기준 자산 명세와 Prompt Pack으로 변환합니다.
          </small>
        </div>
        <div className="rw-tabs">
          <button
            className={tab === 'design' ? 'active' : ''}
            onClick={() => setTab('design')}
          >
            Production Design
          </button>
          <button
            className={tab === 'prompts' ? 'active' : ''}
            onClick={() => setTab('prompts')}
          >
            Image Prompts
          </button>
        </div>
        <button className="icon-btn" onClick={load}>
          <RefreshCw size={15} />
        </button>
      </div>

      {err && <div className="cw-error">{err}</div>}

      <div className="pw-actions">
        {tab === 'design' ? (
          <button className="primary-btn" disabled={busy} onClick={runDesign}>
            <WandSparkles size={14} /> Generate Designs
          </button>
        ) : (
          <button className="primary-btn" disabled={busy} onClick={runPrompts}>
            <ImagePlus size={14} /> Compile Prompt Pack
          </button>
        )}
        <span>
          {tab === 'design'
            ? `${designs.length} latest designs`
            : `${prompts.length} latest prompts`}
        </span>
      </div>

      {tab === 'design' ? (
        <div className="pw-grid">
          {designs.length === 0 ? (
            <div className="workspace-empty">
              Production Design을 아직 생성하지 않았습니다.
            </div>
          ) : (
            designs.map((d) => <DesignCard key={d.id} d={d} reload={load} />)
          )}
        </div>
      ) : (
        <div className="prompt-grid">
          {prompts.length === 0 ? (
            <div className="workspace-empty">
              승인된 Production Design 뒤 Prompt Pack을 생성하세요.
            </div>
          ) : (
            prompts.map((p) => <PromptCard key={p.id} p={p} reload={load} />)
          )}
        </div>
      )}
    </section>
  )
}

function DesignCard({ d, reload }: { d: Design; reload: () => void }) {
  const [txt, setTxt] = useState(JSON.stringify(d.design, null, 2))

  useEffect(() => {
    setTxt(JSON.stringify(d.design, null, 2))
  }, [d.design])

  const handleSave = async () => {
    try {
      const parsed = JSON.parse(txt)

      if (
        typeof parsed !== 'object' ||
        parsed === null ||
        Array.isArray(parsed)
      ) {
        throw new Error('Production Design JSON must be an object.')
      }

      const payload =
        'design' in parsed &&
        typeof parsed.design === 'object' &&
        parsed.design !== null &&
        !Array.isArray(parsed.design)
          ? parsed
          : { design: parsed }

      await updateProductionDesign(d.id, payload)
      await reload()
    } catch (e) {
      console.error(e)
      alert(String(e))
    }
  }

  const handleApprove = async () => {
    try {
      await approveProductionDesign(d.id)
      await reload()
    } catch (e) {
      console.error(e)
      alert(String(e))
    }
  }

  return (
    <div className={`design-card ${d.status === 'APPROVED' ? 'approved' : ''}`}>
      <div className="design-card-head">
        <div>
          <b>
            {d.asset_id}@v{d.version}
          </b>
          <span>
            {d.asset_name} · {d.asset_type}
          </span>
        </div>
        <code>{d.status}</code>
      </div>
      <textarea value={txt} onChange={(e) => setTxt(e.target.value)} />
      <div className="design-meta">
        <span>LOCK {d.locked_attributes.length}</span>
        <span>VIEWS {d.required_views.length}</span>
        <span>MISSING {d.missing_attributes.length}</span>
      </div>
      <div className="card-actions">
        <button className="secondary-btn tiny" onClick={handleSave}>
          <Save size={12} /> Save
        </button>
        <button
          className="primary-btn tiny"
          disabled={d.status === 'APPROVED'}
          onClick={handleApprove}
        >
          <Check size={12} /> Approve
        </button>
      </div>
    </div>
  )
}

function PromptCard({ p, reload }: { p: Prompt; reload: () => void }) {
  const [txt, setTxt] = useState(p.prompt)
  const [neg, setNeg] = useState(p.negative_prompt)

  useEffect(() => {
    setTxt(p.prompt)
    setNeg(p.negative_prompt)
  }, [p.prompt, p.negative_prompt])

  const handleSave = async () => {
    try {
      await updateAssetImagePrompt(p.id, {
        prompt: txt,
        negative_prompt: neg,
      })
      await reload()
    } catch (e) {
      console.error(e)
      alert(String(e))
    }
  }

  const handleApprove = async () => {
    try {
      await approveAssetImagePrompt(p.id)
      await reload()
    } catch (e) {
      console.error(e)
      alert(String(e))
    }
  }

  return (
    <div className={`prompt-card ${p.status === 'APPROVED' ? 'approved' : ''}`}>
      <div className="design-card-head">
        <div>
          <b>
            {p.asset_id} / {p.view_id}
          </b>
          <span>
            {p.asset_type} · Prompt v{p.version}
          </span>
        </div>
        <code>{p.status}</code>
      </div>
      <label>Prompt</label>
      <textarea value={txt} onChange={(e) => setTxt(e.target.value)} />
      <label>Negative</label>
      <textarea
        className="negative"
        value={neg}
        onChange={(e) => setNeg(e.target.value)}
      />
      <div className="design-meta">
        <span>INVARIANTS {p.invariant_lock.length}</span>
      </div>
      <div className="card-actions">
        <button className="secondary-btn tiny" onClick={handleSave}>
          <Save size={12} /> Save
        </button>
        <button
          className="primary-btn tiny"
          disabled={p.status === 'APPROVED'}
          onClick={handleApprove}
        >
          <Check size={12} /> Approve
        </button>
      </div>
    </div>
  )
}
