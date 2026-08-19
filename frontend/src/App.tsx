import { useCallback, useEffect, useState } from 'react'
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  MarkerType,
  type Edge,
  type Node,
} from '@xyflow/react'
import {
  Play,
  Bell,
  Settings,
  Moon,
  FolderKanban,
  Workflow as WorkflowIcon,
  TableProperties,
} from 'lucide-react'
import Sidebar from './components/Sidebar'
import AssetPanel from './components/AssetPanel'
import Inspector from './components/Inspector'
import ProviderCard from './components/ProviderCard'
import QueueMonitor from './components/QueueMonitor'
import ScriptDrawer from './components/ScriptDrawer'
import WorkflowNode from './components/WorkflowNode'
import AssetRequirementWorkspace from './components/AssetRequirementWorkspace'
import CastingWorkspace from './components/CastingWorkspace'
import ProductionWorkspace from './components/ProductionWorkspace'
import JobPanel from './components/JobPanel'
import SettingsModal from './components/settings/SettingsModal'
import {
  createExtractJob,
  createProject,
  getJobs,
  getProjects,
  probeProvider,
} from './api'
import type { Job, ProviderHealth } from './types'

const nodeTypes = { workflow: WorkflowNode }
const labels = [
  ['script', 'Script Input'],
  ['extract', 'Asset Requirement Extractor'],
  ['asset_workspace', 'Asset Requirement Workspace'],
  ['cast', 'Casting Resolver'],
  ['design', 'Production Designer'],
  ['asset_prompt', 'Asset Image Prompt Compiler'],
  ['asset_validate', 'Asset Image Validator'],
  ['approved', 'Approved Asset Library'],
  ['narrative', 'Narrative Keyframe'],
  ['motion', 'Motion Scene Compiler'],
  ['motion_validate', 'Motion Validator'],
  ['motion_keyframe', 'Motion Keyframe Prompt Compiler'],
  ['frames', 'Start / End Frames'],
  ['h3', 'H3 Prompt Compiler'],
  ['video', 'Video Output (Future)'],
] as const

const positions = [
  [70, 220],
  [260, 220],
  [465, 220],
  [680, 220],
  [880, 220],
  [1080, 220],
  [1280, 220],
  [1480, 220],
  [160, 455],
  [380, 455],
  [600, 455],
  [820, 455],
  [1050, 455],
  [1270, 455],
  [1480, 455],
]

const initialNodes: Node[] = labels.map(([id, label], i) => ({
  id,
  type: 'workflow',
  position: { x: positions[i][0], y: positions[i][1] },
  data: { label, order: i + 1 },
}))

const initialEdges: Edge[] = labels.slice(0, -1).map((_, i) => ({
  id: `e${i}`,
  source: labels[i][0],
  target: labels[i + 1][0],
  type: 'smoothstep',
  animated: i < 13,
  markerEnd: { type: MarkerType.ArrowClosed },
  style: { stroke: i === 13 ? '#64748b' : '#00e887', strokeWidth: 2.2 },
}))

export default function App() {
  const [jobs, setJobs] = useState<Job[]>([])
  const [provider, setProvider] = useState<ProviderHealth | null>(null)
  const [selected, setSelected] = useState('Asset Requirement Workspace')
  const [busy, setBusy] = useState(false)
  const [projects, setProjects] = useState<any[]>([])
  const [projectId, setProjectId] = useState<string | null>(null)
  const [mode, setMode] = useState<
    'pipeline' | 'requirements' | 'casting' | 'production'
  >('pipeline')
  const [refreshToken, setRefreshToken] = useState(0)

  const [isSettingsOpen, setIsSettingsOpen] = useState(false)
  const [settingsTab, setSettingsTab] = useState('lmstudio')

  const refreshJobs = useCallback(async () => {
    try {
      setJobs(await getJobs())
    } catch {}
  }, [])

  const refreshProjects = useCallback(async () => {
    try {
      const p = await getProjects()
      setProjects(p)
      if (!projectId && p[0]) setProjectId(p[0].id)
    } catch {}
  }, [projectId])

  const probe = useCallback(async () => {
    try {
      setProvider(await probeProvider())
    } catch (e) {
      setProvider({ state: 'OFFLINE', error: String(e) })
    }
  }, [])

  useEffect(() => {
    refreshJobs()
    refreshProjects()
    probe()

    const ws = new WebSocket(
      `${location.protocol === 'https:' ? 'wss' : 'ws'}://${location.host}/ws/events`
    )
    ws.onopen = () => ws.send('hello')
    ws.onmessage = () => {
      refreshJobs()
      setRefreshToken((x) => x + 1)
    }

    const t = setInterval(() => {
      refreshJobs()
      if (ws.readyState === 1) ws.send('ping')
    }, 5000)

    return () => {
      clearInterval(t)
      ws.close()
    }
  }, [refreshJobs, refreshProjects, probe])

  const runExtractor = async (script: string) => {
    if (!projectId) return
    setBusy(true)
    try {
      await createExtractJob(script, projectId)
      await refreshJobs()
    } finally {
      setBusy(false)
    }
  }

  const newProject = async () => {
    const name = prompt('프로젝트 이름', 'New Short Drama')
    if (!name) return
    const p = await createProject(name)
    await refreshProjects()
    setProjectId(p.id)
  }

  const openSettings = (tab: string = 'lmstudio') => {
    setSettingsTab(tab)
    setIsSettingsOpen(true)
  }

  return (
    <div className="app-shell">
      <header className="topbar">
        <div className="brand">
          <span className="brand-logo">▰</span>
          <b>DramaStudio</b>
        </div>
        <div className="project-picker">
          <FolderKanban size={15} />
          <select
            value={projectId ?? ''}
            onChange={(e) => setProjectId(e.target.value || null)}
          >
            <option value="">Select Project</option>
            {projects.map((p) => (
              <option value={p.id} key={p.id}>
                {p.name}
              </option>
            ))}
          </select>
          <button onClick={newProject}>+ New</button>
        </div>
        <div
          className={`provider-pill ${provider?.state === 'ONLINE' ? 'ok' : 'bad'}`}
          style={{ cursor: 'pointer' }}
          onClick={() => openSettings('lmstudio')}
        >
          ● LM Studio {provider?.state ?? 'UNKNOWN'}
        </div>
        <div className="top-actions">
          <Moon />
          <Bell />
          <Settings
            style={{ cursor: 'pointer' }}
            onClick={() => openSettings('lmstudio')}
          />
          <button className="run-all">
            <Play size={17} /> Run Pipeline
          </button>
        </div>
      </header>

      <Sidebar />

      <main className="workspace">
        <div className="canvas-toolbar">
          <button
            className={`view-btn ${mode === 'pipeline' ? 'active' : ''}`}
            onClick={() => setMode('pipeline')}
          >
            <WorkflowIcon size={14} /> Pipeline
          </button>
          <button
            className={`view-btn ${mode === 'requirements' ? 'active' : ''}`}
            onClick={() => setMode('requirements')}
          >
            <TableProperties size={14} /> Requirements
          </button>
          <button
            className={`view-btn ${mode === 'casting' ? 'active' : ''}`}
            onClick={() => setMode('casting')}
          >
            <FolderKanban size={14} /> Casting
          </button>
          <button
            className={`view-btn ${mode === 'production' ? 'active' : ''}`}
            onClick={() => setMode('production')}
          >
            Production
          </button>
          <span className="toolbar-spacer" />
          <span>Auto Layout</span>
          <i className="toggle on" />
          <span className="zoom-pill">100%</span>
        </div>

        {mode === 'pipeline' ? (
          <>
            <AssetPanel />
            <div className="provider-zone">
              <ProviderCard health={provider} onProbe={probe} />
              <div className="service-card glass">
                <div>
                  <b>Queue Manager</b>
                  <span className="online">● Healthy</span>
                  <small>Persistent Job / Attempt Queue</small>
                </div>
              </div>
              <div className="service-card glass">
                <div>
                  <b>Casting Resolver</b>
                  <span className="online">● v0.3</span>
                  <small>Global Actor · Voice · Pinning</small>
                </div>
              </div>
            </div>
            <div className="flow-wrap">
              <ReactFlow
                nodes={initialNodes}
                edges={initialEdges}
                nodeTypes={nodeTypes}
                fitView
                minZoom={0.35}
                maxZoom={1.5}
                onNodeClick={(_, n) => {
                  setSelected(String(n.data.label ?? 'Node'))
                  if (n.id === 'asset_workspace') setMode('requirements')
                  if (n.id === 'cast') setMode('casting')
                  if (n.id === 'design' || n.id === 'asset_prompt')
                    setMode('production')
                }}
              >
                <Background color="#22303a" gap={24} size={1} />
                <Controls />
                <MiniMap
                  pannable
                  zoomable
                  nodeColor={() => '#063a28'}
                  maskColor="rgba(3,8,12,.7)"
                />
              </ReactFlow>
            </div>
            <JobPanel
              jobs={jobs}
              onWorkspace={(pid) => {
                setProjectId(pid)
                setMode('requirements')
                setRefreshToken((x) => x + 1)
              }}
              refresh={refreshJobs}
            />
          </>
        ) : mode === 'requirements' ? (
          <AssetRequirementWorkspace
            projectId={projectId}
            refreshToken={refreshToken}
          />
        ) : mode === 'casting' ? (
          <CastingWorkspace projectId={projectId} />
        ) : (
          <ProductionWorkspace projectId={projectId} />
        )}

        <ScriptDrawer
          onRun={runExtractor}
          busy={busy}
          projectId={projectId}
        />
        <QueueMonitor jobs={jobs} />
      </main>
      <Inspector selectedLabel={selected} />

      <SettingsModal
        isOpen={isSettingsOpen}
        onClose={() => setIsSettingsOpen(false)}
        initialTab={settingsTab}
        onSaved={probe}
      />
    </div>
  )
}