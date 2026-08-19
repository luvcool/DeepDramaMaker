import { useEffect, useMemo, useState, type ReactNode } from 'react'
import { UserRound, Mic2, Plus, Check, Save, RefreshCw } from 'lucide-react'
import { approveCasting, approveGlobalAssetVersion, createGlobalAsset, createGlobalAssetVersion, getCastings, getGlobalAssets, getProjectCharacters, upsertCasting } from '../api'

type GVersion={version:number;status:string;metadata:any;reference_uri?:string|null}
type GAsset={asset_id:string;type:'actor'|'voice';display_name:string;versions:GVersion[]}
type Character={asset_id:string;name:string;version:number;payload:any}
type Casting={id:number;character_asset_id:string;character_name:string;actor_asset_id?:string|null;actor_version?:number|null;voice_asset_id?:string|null;voice_version?:number|null;status:string;notes:string}

export default function CastingWorkspace({projectId}:{projectId:string|null}){
 const [actors,setActors]=useState<GAsset[]>([]); const [voices,setVoices]=useState<GAsset[]>([]); const [characters,setCharacters]=useState<Character[]>([]); const [castings,setCastings]=useState<Casting[]>([]); const [tab,setTab]=useState<'casting'|'global'>('casting'); const [err,setErr]=useState('')
 const load=async()=>{setErr(''); try{setActors(await getGlobalAssets('actor'));setVoices(await getGlobalAssets('voice'));if(projectId){setCharacters(await getProjectCharacters(projectId));setCastings(await getCastings(projectId))}}catch(e){setErr(String(e))}}
 useEffect(()=>{load()},[projectId])
 const cmap=useMemo(()=>Object.fromEntries(castings.map(c=>[c.character_asset_id,c])),[castings])
 const approvedVersions=(a:GAsset)=>a.versions.filter(v=>v.status==='APPROVED')
 const saveMap=async(ch:Character,actorKey:string,voiceKey:string)=>{if(!projectId)return;const [actor_asset_id,av]=actorKey.split('@v');const [voice_asset_id,vv]=voiceKey.split('@v'); await upsertCasting(projectId,{character_asset_id:ch.asset_id,character_name:ch.name,actor_asset_id:actor_asset_id||null,actor_version:av?Number(av):null,voice_asset_id:voice_asset_id||null,voice_version:vv?Number(vv):null,notes:cmap[ch.asset_id]?.notes||''});await load()}
 const addAsset=async(type:'actor'|'voice')=>{const name=prompt(type==='actor'?'배우 자산 이름':'목소리 자산 이름',type==='actor'?'Actor ': 'Voice ');if(!name)return;const metaText=prompt('기본 metadata JSON','{}')||'{}';let metadata={};try{metadata=JSON.parse(metaText)}catch{return alert('JSON 오류')};await createGlobalAsset({asset_type:type,display_name:name,metadata});await load()}
 const addVersion=async(a:GAsset)=>{const metaText=prompt(`${a.asset_id} 새 버전 metadata JSON`,JSON.stringify(a.versions[0]?.metadata||{},null,2))||'{}';let metadata={};try{metadata=JSON.parse(metaText)}catch{return alert('JSON 오류')};await createGlobalAssetVersion(a.asset_id,{metadata});await load()}
 return <section className="casting-workspace glass">
  <div className="cw-head"><div><b>Global Actor / Voice Library + Casting Resolver</b><small>공용 배우·목소리 자산을 버전 승인하고 Project Character에 pinning합니다.</small></div><div className="rw-tabs"><button className={tab==='casting'?'active':''} onClick={()=>setTab('casting')}>Casting</button><button className={tab==='global'?'active':''} onClick={()=>setTab('global')}>Global Library</button></div><button className="icon-btn" onClick={load}><RefreshCw size={15}/></button></div>
  {err&&<div className="cw-error">{err}</div>}
  {tab==='casting'?<div className="cw-body">
    {characters.length===0?<div className="workspace-empty">Requirements에서 Character 자산을 먼저 승인하세요.</div>:characters.map(ch=>{const c=cmap[ch.asset_id];const actorVal=c?.actor_asset_id&&c.actor_version?`${c.actor_asset_id}@v${c.actor_version}`:'';const voiceVal=c?.voice_asset_id&&c.voice_version?`${c.voice_asset_id}@v${c.voice_version}`:'';return <div className={`casting-row ${c?.status==='APPROVED'?'approved':''}`} key={ch.asset_id}>
      <div className="char-badge"><UserRound size={20}/></div><div className="char-info"><b>{ch.asset_id}</b><span>{ch.name}</span><small>Project Character @v{ch.version}</small></div>
      <div><label>Actor</label><select defaultValue={actorVal} id={`actor-${ch.asset_id}`}><option value="">Unassigned</option>{actors.flatMap(a=>approvedVersions(a).map(v=><option value={`${a.asset_id}@v${v.version}`} key={`${a.asset_id}-${v.version}`}>{a.asset_id}@v{v.version} · {a.display_name}</option>))}</select></div>
      <div><label>Voice</label><select defaultValue={voiceVal} id={`voice-${ch.asset_id}`}><option value="">Unassigned</option>{voices.flatMap(a=>approvedVersions(a).map(v=><option value={`${a.asset_id}@v${v.version}`} key={`${a.asset_id}-${v.version}`}>{a.asset_id}@v{v.version} · {a.display_name}</option>))}</select></div>
      <button className="secondary-btn tiny" onClick={async()=>{const av=(document.getElementById(`actor-${ch.asset_id}`) as HTMLSelectElement).value;const vv=(document.getElementById(`voice-${ch.asset_id}`) as HTMLSelectElement).value;await saveMap(ch,av,vv)}}><Save size={13}/> Save</button>
      <button className="primary-btn tiny" disabled={!c||c.status==='APPROVED'} onClick={async()=>{try{await approveCasting(c.id);await load()}catch(e){alert(String(e))}}}><Check size={13}/> Approve</button>
      <div className={`status-chip ${(c?.status||'DRAFT').toLowerCase()}`}>{c?.status||'UNMAPPED'}</div>
    </div>})}
  </div>:<div className="cw-body global-grid">
    <GlobalColumn title="Actors" icon={<UserRound size={18}/>} items={actors} onAdd={()=>addAsset('actor')} onVersion={addVersion} onApprove={async(a,v)=>{await approveGlobalAssetVersion(a.asset_id,v);await load()}}/>
    <GlobalColumn title="Voices" icon={<Mic2 size={18}/>} items={voices} onAdd={()=>addAsset('voice')} onVersion={addVersion} onApprove={async(a,v)=>{await approveGlobalAssetVersion(a.asset_id,v);await load()}}/>
  </div>}
 </section>
}

function GlobalColumn({title,icon,items,onAdd,onVersion,onApprove}:{title:string;icon:ReactNode;items:GAsset[];onAdd:()=>void;onVersion:(a:GAsset)=>void;onApprove:(a:GAsset,v:number)=>void}){
 return <div className="global-column"><div className="global-title">{icon}<b>{title}</b><button className="secondary-btn tiny" onClick={onAdd}><Plus size={12}/> New</button></div>{items.length===0&&<div className="global-empty">No assets</div>}{items.map(a=><div className="global-card" key={a.asset_id}><div className="global-card-head"><div><b>{a.asset_id}</b><span>{a.display_name}</span></div><button className="icon-btn" onClick={()=>onVersion(a)}><Plus size={13}/></button></div><div className="version-list">{a.versions.map(v=><div className="version-row" key={v.version}><span>v{v.version}</span><code>{v.status}</code>{v.status!=='APPROVED'&&<button onClick={()=>onApprove(a,v.version)}>Approve</button>}</div>)}</div></div>)}</div>
}
