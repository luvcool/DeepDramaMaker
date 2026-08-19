import { useState } from 'react'

const example = `EP01 SCENE 1
늦은 밤, 서연은 자신의 아파트 거실에서 휴대폰을 들고 창밖을 바라본다.
검은 코트를 입고 있으며 어머니에게 받은 은색 목걸이를 만진다.
통화를 끝낸 뒤 현관으로 이동해 검은 세단을 타고 회사 지하주차장으로 향한다.`

export default function ScriptDrawer({onRun,busy,projectId}:{onRun:(script:string)=>void;busy:boolean;projectId:string|null}) {
  const [script,setScript] = useState(example)
  return (
    <div className="script-drawer glass">
      <div><b>Vertical Slice v0.2</b><small>Script → Extract → Edit → Approve</small></div>
      <textarea value={script} onChange={e=>setScript(e.target.value)} />
      <button className="primary-btn" disabled={busy||!projectId} onClick={()=>onRun(script)}>{busy?'Running...':projectId?'Run Extractor':'Select Project'}</button>
    </div>
  )
}
