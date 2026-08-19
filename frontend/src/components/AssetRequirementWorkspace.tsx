import { useEffect, useMemo, useState } from 'react'
import { Check, Pencil, Save, X, Database, AlertTriangle } from 'lucide-react'
import { approveAllDrafts, approveAssetDraft, getAssetDrafts, getProjectAssets, updateAssetDraft } from '../api'

type Draft = { id:number; asset_id:string; type:string; name:string; persistence:string; importance:string; reference_required:boolean; known_attributes:Record<string,unknown>; missing_attributes:string[]; status:string; version:number }

export default function AssetRequirementWorkspace({projectId,refreshToken}:{projectId:string|null;refreshToken:number}){
  const [drafts,setDrafts]=useState<Draft[]>([])
  const [registry,setRegistry]=useState<any[]>([])
  const [editing,setEditing]=useState<number|null>(null)
  const [form,setForm]=useState<any>({})
  const [tab,setTab]=useState<'drafts'|'registry'>('drafts')

  const load=async()=>{
    if(!projectId) return;
    try {
      setDrafts(await getAssetDrafts(projectId));
      setRegistry(await getProjectAssets(projectId));
    } catch (e) {
      console.error("Failed to load workspace data:", e);
    }
  }

  useEffect(()=>{
    load();
    const interval = setInterval(load, 3000);
    return () => clearInterval(interval);
  },[projectId,refreshToken])

  const grouped=useMemo(()=>drafts.reduce((m:Record<string,Draft[]>,d)=>((m[d.type]??=[]).push(d),m),{}),[drafts])

  const startEdit=(d:Draft)=>{ setEditing(d.id); setForm({...d,knownText:JSON.stringify(d.known_attributes,null,2),missingText:d.missing_attributes.join('\n')}) }
  const save=async()=>{
    let known={}; try{ known=JSON.parse(form.knownText||'{}') }catch{ alert('known_attributes JSON이 올바르지 않습니다.'); return }
    await updateAssetDraft(editing!,{name:form.name,persistence:form.persistence,importance:form.importance,reference_required:!!form.reference_required,known_attributes:known,missing_attributes:String(form.missingText||'').split('\n').map((x:string)=>x.trim()).filter(Boolean)})
    setEditing(null); await load()
  }

  if(!projectId) return <div className="workspace-empty">먼저 프로젝트를 생성하거나 선택하세요.</div>

  return <section className="requirement-workspace glass">
    <div className="rw-head">
      <div><b>Asset Requirement Workspace</b><small>AI 추출 결과를 사람이 수정·승인한 뒤 Project Asset Registry로 확정합니다.</small></div>
      <div className="rw-tabs"><button className={tab==='drafts'?'active':''} onClick={()=>setTab('drafts')}>Drafts {drafts.length}</button><button className={tab==='registry'?'active':''} onClick={()=>setTab('registry')}>Registry {registry.length}</button></div>
      {tab==='drafts'&&<button className="primary-btn" onClick={async()=>{await approveAllDrafts(projectId);await load()}}><Check size={15}/> Approve All</button>}
    </div>
    {tab==='drafts' ? <div className="rw-body">
      {drafts.length===0 && <div className="workspace-empty">아직 자산 요구사항이 없습니다. 대본을 입력하고 Extractor를 실행하세요.</div>}
      {Object.entries(grouped).map(([type,items])=><div className="asset-group" key={type}>
        <div className="asset-group-title">{type.toUpperCase()} <span>{items.length}</span></div>
        {items.map(d=><div className={`draft-row ${d.status==='APPROVED'?'approved':''}`} key={d.id}>
          <div className="asset-id">{d.asset_id}</div>
          <div className="asset-main"><b>{d.name}</b><small>{d.persistence} · {d.importance} · ref {d.reference_required?'required':'optional'}</small></div>
          <div className="missing">{d.missing_attributes.length>0?<><AlertTriangle size={13}/>{d.missing_attributes.length} missing</>:<span className="ok-txt">complete</span>}</div>
          <div className={`status-chip ${d.status.toLowerCase()}`}>{d.status}@v{d.version}</div>
          <button className="icon-btn" onClick={()=>startEdit(d)}><Pencil size={14}/></button>
          <button className="icon-btn approve" disabled={d.status==='APPROVED'} onClick={async()=>{await approveAssetDraft(d.id);await load()}}><Check size={14}/></button>
        </div>)}
      </div>)}
    </div> : <div className="rw-body registry-grid">
      {registry.length===0?<div className="workspace-empty">아직 승인된 Project Asset이 없습니다.</div>:registry.map(a=><div className="registry-card" key={a.id}><Database size={19}/><div><b>{a.asset_id}@v{a.version}</b><span>{a.name}</span><small>{a.type} · {a.status}</small></div></div>)}
    </div>}

    {editing!==null && <div className="edit-modal-back"><div className="edit-modal glass">
      <div className="edit-head"><b>Edit Asset Requirement</b><button className="icon-btn" onClick={()=>setEditing(null)}><X size={15}/></button></div>
      <label>Name</label><input value={form.name||''} onChange={e=>setForm({...form,name:e.target.value})}/>
      <div className="edit-grid"><div><label>Persistence</label><select value={form.persistence} onChange={e=>setForm({...form,persistence:e.target.value})}><option>persistent</option><option>scene</option><option>background</option></select></div><div><label>Importance</label><select value={form.importance} onChange={e=>setForm({...form,importance:e.target.value})}><option>critical</option><option>high</option><option>medium</option><option>low</option></select></div></div>
      <label className="checkline"><input type="checkbox" checked={!!form.reference_required} onChange={e=>setForm({...form,reference_required:e.target.checked})}/> Reference required</label>
      <label>Known attributes (JSON)</label><textarea className="json-editor" value={form.knownText||''} onChange={e=>setForm({...form,knownText:e.target.value})}/>
      <label>Missing attributes (one per line)</label><textarea value={form.missingText||''} onChange={e=>setForm({...form,missingText:e.target.value})}/>
      <button className="primary-btn" onClick={save}><Save size={15}/> Save Draft</button>
    </div></div>}
  </section>
}
