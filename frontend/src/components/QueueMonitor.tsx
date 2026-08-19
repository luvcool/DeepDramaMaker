import type { Job } from '../types'
import { Layers3, PlayCircle, Ban } from 'lucide-react'

export default function QueueMonitor({jobs}:{jobs:Job[]}) {
  const queued = jobs.filter(j => ['CREATED','QUEUED','WAITING_DEPENDENCY','RETRY_WAIT'].includes(j.state)).length
  const running = jobs.filter(j => ['DISPATCHING','RUNNING','STREAMING','VALIDATING'].includes(j.state)).length
  const blocked = jobs.filter(j => ['BLOCKED','FAILED','UNKNOWN','INTERRUPTED'].includes(j.state)).length
  return (
    <div className="bottom-monitor">
      <Stat icon={<Layers3 size={18}/>} label="Queued Jobs" value={queued} accent="purple"/>
      <Stat icon={<PlayCircle size={18}/>} label="Running Jobs" value={running} accent="cyan"/>
      <Stat icon={<Ban size={18}/>} label="Blocked / Failed" value={blocked} accent="red"/>
      <div className="monitor-detail">
        <b>Recent activity</b>
        <span>{jobs[0]?.id ?? 'No jobs yet'}</span>
        <small>{jobs[0]?.progress_message ?? 'Create an extractor job to begin.'}</small>{jobs[0]?.error && <em className="recent-error">{formatError(jobs[0].error)}</em>}
      </div>
    </div>
  )
}

function Stat({icon,label,value,accent}:{icon:React.ReactNode,label:string,value:number,accent:string}) {
  return (
    <div className={`monitor-stat ${accent}`}>
      <div className="stat-head">{icon}<span>{label}</span></div>
      <strong>{value}</strong>
    </div>
  )
}

function formatError(error:string){
  try{const d=JSON.parse(error);return `${d.exception_type ?? 'Error'}: ${d.message ?? ''}`.slice(0,180)}catch{return error.slice(0,180)}
}
