import type { Job, ProviderHealth } from './types'

export async function getJobs(): Promise<Job[]> { const r=await fetch('/api/jobs'); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function createProject(name:string){ const r=await fetch('/api/projects',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({name})}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function getProjects(){ const r=await fetch('/api/projects'); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function createExtractJob(script:string,project_id?:string){ const r=await fetch('/api/jobs',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({script,priority:10,project_id})}); if(!r.ok) throw new Error(await r.text()); return r.json() as Promise<{job_id:string}> }
export async function getJob(id:string){ const r=await fetch(`/api/jobs/${id}`); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function retryJob(id:string){ await fetch(`/api/jobs/${id}/retry`,{method:'POST'}) }
export async function cancelJob(id:string){ await fetch(`/api/jobs/${id}/cancel`,{method:'POST'}) }
export async function probeProvider():Promise<ProviderHealth>{ const r=await fetch('/api/providers/lmstudio/probe'); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function materializeWorkspace(jobId:string){ const r=await fetch(`/api/jobs/${jobId}/workspace`,{method:'POST'}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function getAssetDrafts(projectId:string){ const r=await fetch(`/api/projects/${projectId}/asset-drafts`); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function updateAssetDraft(id:number,payload:any){ const r=await fetch(`/api/asset-drafts/${id}`,{method:'PATCH',headers:{'content-type':'application/json'},body:JSON.stringify(payload)}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function approveAssetDraft(id:number){ const r=await fetch(`/api/asset-drafts/${id}/approve`,{method:'POST'}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function approveAllDrafts(projectId:string){ const r=await fetch(`/api/projects/${projectId}/asset-drafts/approve-all`,{method:'POST'}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function getProjectAssets(projectId:string){ const r=await fetch(`/api/projects/${projectId}/assets`); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function getGlobalAssets(type?:'actor'|'voice'){ const q=type?`?asset_type=${type}`:''; const r=await fetch(`/api/global-assets${q}`); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function createGlobalAsset(payload:{asset_type:'actor'|'voice';display_name:string;metadata?:any;reference_uri?:string|null}){ const r=await fetch('/api/global-assets',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(payload)}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function createGlobalAssetVersion(assetId:string,payload:{metadata?:any;reference_uri?:string|null}){ const r=await fetch(`/api/global-assets/${assetId}/versions`,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(payload)}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function approveGlobalAssetVersion(assetId:string,version:number){ const r=await fetch(`/api/global-assets/${assetId}/versions/${version}/approve`,{method:'POST'}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function getProjectCharacters(projectId:string){ const r=await fetch(`/api/projects/${projectId}/characters`); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function getCastings(projectId:string){ const r=await fetch(`/api/projects/${projectId}/castings`); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function upsertCasting(projectId:string,payload:any){ const r=await fetch(`/api/projects/${projectId}/castings`,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(payload)}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function updateCasting(id:number,payload:any){ const r=await fetch(`/api/castings/${id}`,{method:'PATCH',headers:{'content-type':'application/json'},body:JSON.stringify(payload)}); if(!r.ok) throw new Error(await r.text()); return r.json() }
export async function approveCasting(id:number){ const r=await fetch(`/api/castings/${id}/approve`,{method:'POST'}); if(!r.ok) throw new Error(await r.text()); return r.json() }

export async function createProductionDesignJob(projectId:string){const r=await fetch(`/api/projects/${projectId}/production-design/jobs`,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({priority:12})});if(!r.ok)throw new Error(await r.text());return r.json()}
export async function getProductionDesigns(projectId:string){const r=await fetch(`/api/projects/${projectId}/production-designs`);if(!r.ok)throw new Error(await r.text());return r.json()}
export async function updateProductionDesign(id:number,payload:any){const r=await fetch(`/api/production-designs/${id}`,{method:'PATCH',headers:{'content-type':'application/json'},body:JSON.stringify(payload)});if(!r.ok)throw new Error(await r.text());return r.json()}
export async function approveProductionDesign(id:number){const r=await fetch(`/api/production-designs/${id}/approve`,{method:'POST'});if(!r.ok)throw new Error(await r.text());return r.json()}
export async function createAssetImagePromptJob(projectId:string){const r=await fetch(`/api/projects/${projectId}/asset-image-prompts/jobs`,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({priority:14})});if(!r.ok)throw new Error(await r.text());return r.json()}
export async function getAssetImagePrompts(projectId:string){const r=await fetch(`/api/projects/${projectId}/asset-image-prompts`);if(!r.ok)throw new Error(await r.text());return r.json()}
export async function updateAssetImagePrompt(id:number,payload:any){const r=await fetch(`/api/asset-image-prompts/${id}`,{method:'PATCH',headers:{'content-type':'application/json'},body:JSON.stringify(payload)});if(!r.ok)throw new Error(await r.text());return r.json()}
export async function approveAssetImagePrompt(id:number){const r=await fetch(`/api/asset-image-prompts/${id}/approve`,{method:'POST'});if(!r.ok)throw new Error(await r.text());return r.json()}

export async function getProviders(): Promise<any[]> {
  const r = await fetch('/api/providers')
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function getProvider(id: string): Promise<any> {
  const r = await fetch(`/api/providers/${id}`)
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function updateProvider(id: string, payload: any): Promise<any> {
  const r = await fetch(`/api/providers/${id}`, {
    method: 'PUT',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(payload),
  })
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function testProvider(id: string, payload?: any): Promise<any> {
  const r = await fetch(`/api/providers/${id}/test`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(payload || {}),
  })
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function refreshProviderModels(id: string, baseUrl?: string): Promise<any> {
  const r = await fetch(`/api/providers/${id}/models/refresh`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ base_url: baseUrl }),
  })
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function getMcpServers(): Promise<any[]> {
  const r = await fetch('/api/mcp/servers')
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function getMcpServer(id: string): Promise<any> {
  const r = await fetch(`/api/mcp/servers/${id}`)
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function updateMcpServer(id: string, payload: any): Promise<any> {
  const r = await fetch(`/api/mcp/servers/${id}`, {
    method: 'PUT',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(payload),
  })
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function testMcpServer(id: string): Promise<any> {
  const r = await fetch(`/api/mcp/servers/${id}/test`, { method: 'POST' })
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function checkMcpBackends(id: string): Promise<any> {
  const r = await fetch(`/api/mcp/servers/${id}/check-backends`, { method: 'POST' })
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

export async function createMcpJob(payload: {
  server_id: string
  tool_name: string
  arguments?: Record<string, unknown>
  project_id?: string | null
  priority?: number
}) {
  const r = await fetch('/api/mcp/jobs', {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify(payload),
  })
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}
