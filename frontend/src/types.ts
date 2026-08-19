export type Job = {
  id: string
  project_id?: string | null
  node_type: string
  state: string
  priority: number
  progress_message: string
  error?: string | null
  created_at?: string
}

export type ProviderHealth = {
  state: string
  base_url?: string
  configured_model?: string
  models?: string[]
  error?: string
}
