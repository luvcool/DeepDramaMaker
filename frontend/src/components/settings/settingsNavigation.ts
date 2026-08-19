export interface NavItem {
  id: string
  label: string
  disabled?: boolean
  badge?: string
  status?: 'ONLINE' | 'DEGRADED' | 'OFFLINE' | 'DISABLED'
  children?: NavItem[]
  keywords?: string[]
}

export const settingsNavigation: NavItem[] = [
  {
    id: 'general',
    label: 'General',
    keywords: ['general', 'language', 'project', 'defaults'],
  },
  {
    id: 'ai-providers',
    label: 'AI Providers',
    keywords: ['ai', 'provider', 'llm', 'lmstudio', 'openai', 'claude'],
    children: [
      { id: 'lmstudio', label: 'LM Studio', status: 'ONLINE', keywords: ['lmstudio', 'local', 'llm'] },
      { id: 'openai', label: 'OpenAI', disabled: true, keywords: ['openai', 'gpt', 'chatgpt'] },
      { id: 'custom-llm', label: 'Custom API', disabled: true, keywords: ['custom', 'api', 'v1'] },
    ],
  },
  {
    id: 'generation',
    label: 'Generation',
    keywords: ['generation', 'image', 'tts', 'voice', 'video'],
    children: [
      { id: 'image', label: 'Image', keywords: ['image', 'sd', 'midjourney', 'flux'] },
      { id: 'tts', label: 'Voice / TTS', keywords: ['voice', 'tts', 'audio', 'elevenlabs'] },
      { id: 'video', label: 'Video', keywords: ['video', 'minimax', 'h3', 'runway', 'sora'] },
    ],
  },
  {
    id: 'mcp-servers',
    label: 'MCP Servers',
    keywords: ['mcp', 'stdio', 'tools', 'mir studio', 'comfyui'],
    children: [
      { id: 'mir-studio-mcp', label: 'Mir Studio MCP', keywords: ['mir', 'image', 'voice', 'video', 'h3', 'comfyui'] },
    ],
  },
  {
    id: 'workflow',
    label: 'Workflow',
    keywords: ['workflow', 'nodes', 'pipeline', 'graph'],
  },
  {
    id: 'queue',
    label: 'Queue & Jobs',
    keywords: ['queue', 'jobs', 'concurrency', 'retries', 'workers'],
  },
  {
    id: 'assets',
    label: 'Asset Library',
    keywords: ['assets', 'library', 'actors', 'voices', 'global'],
  },
  {
    id: 'storage',
    label: 'Storage',
    keywords: ['storage', 'paths', 'folder', 'cache', 'cleanup'],
  },
  {
    id: 'appearance',
    label: 'Appearance',
    keywords: ['appearance', 'theme', 'dark', 'neon', 'ui', 'density'],
  },
  {
    id: 'advanced',
    label: 'Advanced',
    keywords: ['advanced', 'debug', 'developer', 'logs', 'raw'],
  },
]
