import { LayoutDashboard, Workflow, Boxes, ScrollText, ListChecks, Activity, Settings } from 'lucide-react'

const items = [
  ['Overview', LayoutDashboard],
  ['Pipeline', Workflow],
  ['Assets', Boxes],
  ['Scripts', ScrollText],
  ['Jobs', ListChecks],
  ['Monitoring', Activity],
  ['Settings', Settings],
] as const

export default function Sidebar() {
  return (
    <aside className="nav-rail">
      <div className="brand-mark">D</div>
      {items.map(([label, Icon]) => (
        <button className={`nav-item ${label === 'Pipeline' ? 'active' : ''}`} key={label}>
          <Icon size={19}/>
          <span>{label}</span>
        </button>
      ))}
      <div className="nav-version">v0.1</div>
    </aside>
  )
}
