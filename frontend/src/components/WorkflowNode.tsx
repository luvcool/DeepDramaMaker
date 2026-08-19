import { Handle, Position, type NodeProps } from '@xyflow/react'
import {
  FileText, Search, Users, Code2, ShieldCheck, FolderCheck,
  Image, Clapperboard, Film, BrainCircuit, Video, Mic
} from 'lucide-react'

const icons: Record<string, React.ComponentType<{size?: number}>> = {
  script: FileText,
  extract: Search,
  cast: Users,
  asset_prompt: Code2,
  asset_validate: ShieldCheck,
  approved: FolderCheck,
  narrative: Image,
  motion: Clapperboard,
  motion_validate: ShieldCheck,
  motion_keyframe: Code2,
  frames: Film,
  h3: BrainCircuit,
  video: Video,
  voice: Mic,
}

export default function WorkflowNode({ id, data, selected }: NodeProps) {
  const Icon = icons[id] ?? Code2
  const future = id === 'video'
  return (
    <div className={`workflow-node ${selected ? 'selected' : ''} ${future ? 'future' : ''}`}>
      <Handle type="target" position={Position.Left} />
      <div className="node-index">{String(data.order ?? '')}</div>
      <Icon size={23}/>
      <div className="node-label">{String(data.label ?? '')}</div>
      <div className="node-state">{future ? 'FUTURE' : 'READY'}</div>
      <Handle type="source" position={Position.Right} />
    </div>
  )
}
