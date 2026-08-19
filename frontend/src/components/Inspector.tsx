import { Code2 } from 'lucide-react'

export default function Inspector({ selectedLabel }: { selectedLabel: string }) {
  return (
    <aside className="inspector">
      <div className="inspector-header">
        <div className="square-icon"><Code2 size={22}/></div>
        <div>
          <h3>{selectedLabel || 'Asset Image Prompt Compiler'}</h3>
          <span className="online">● Active</span>
        </div>
      </div>
      <div className="tabs"><b>Properties</b><span>Inputs</span><span>Outputs</span><span>Logs</span></div>
      <label>Provider</label>
      <div className="field">LM Studio (Remote)</div>
      <label>Model</label>
      <div className="field">Auto / configured model</div>
      <label>Timeout (sec)</label>
      <div className="field">180</div>
      <label>Max Retries</label>
      <div className="field">3</div>
      <label>Output Schema</label>
      <div className="field code">asset_requirement.schema.json</div>
      <div className="section-title">Validation</div>
      {['Schema Validation','Pydantic Validation','Artifact Versioning'].map(x => (
        <div className="toggle-row" key={x}><span>{x}</span><i className="toggle on"/></div>
      ))}
      <button className="primary-btn inspector-save">Save Changes</button>
    </aside>
  )
}
