import { Box, RefreshCw } from 'lucide-react'
import type { ProviderHealth } from '../types'

export default function ProviderCard({health, onProbe}:{health:ProviderHealth|null, onProbe:()=>void}) {
  const online = health?.state === 'ONLINE'
  return (
    <div className="service-card glass">
      <div className="service-icon"><Box size={21}/></div>
      <div className="service-main">
        <b>LM Studio Provider</b>
        <span className={online ? 'online' : 'offline'}>● {health?.state ?? 'UNKNOWN'}</span>
        <small>{health?.configured_model || health?.models?.[0] || 'No model selected'}</small>
      </div>
      <button className="icon-btn" onClick={onProbe} title="Probe Provider"><RefreshCw size={15}/></button>
    </div>
  )
}
