import { useState, useEffect } from 'react'
import { X, SlidersHorizontal, AlertCircle } from 'lucide-react'
import SettingsNavigator from './SettingsNavigator'
import SettingsPage from './SettingsPage'
import { settingsNavigation } from './settingsNavigation'
import { getProviders } from '../../api'

interface SettingsModalProps {
  isOpen: boolean
  onClose: () => void
  initialTab?: string
  onSaved?: () => void
}

export default function SettingsModal({
  isOpen,
  onClose,
  initialTab = 'lmstudio',
  onSaved,
}: SettingsModalProps) {
  const [activeTab, setActiveTab] = useState(initialTab)
  const [searchQuery, setSearchQuery] = useState('')
  const [isDirty, setIsDirty] = useState(false)
  const [providerStatuses, setProviderStatuses] = useState<
    Record<string, 'ONLINE' | 'DEGRADED' | 'OFFLINE' | 'DISABLED'>
  >({})

  useEffect(() => {
    if (isOpen) {
      setActiveTab(initialTab)
      setIsDirty(false)
      loadProviderStatuses()
    }
  }, [isOpen, initialTab])

  const loadProviderStatuses = async () => {
    try {
      const providers = await getProviders()
      const statuses: Record<string, any> = {}
      for (const p of providers) {
        if (p.type === 'lmstudio' || p.id === 'LMSTUDIO_01') {
          statuses['lmstudio'] = p.status || 'OFFLINE'
        } else if (p.type === 'openai') {
          statuses['openai'] = p.status || 'DISABLED'
        } else if (p.type === 'custom-openai') {
          statuses['custom-llm'] = p.status || 'DISABLED'
        }
      }
      setProviderStatuses(statuses)
    } catch {
      // fallback
    }
  }

  if (!isOpen) return null

  const handleSelectTab = (tabId: string) => {
    if (isDirty) {
      const confirmDiscard = window.confirm(
        '저장되지 않은 변경 사항이 있습니다. 취소하고 이동하시겠습니까?'
      )
      if (!confirmDiscard) return
    }
    setActiveTab(tabId)
    setIsDirty(false)
  }

  const handleClose = () => {
    if (isDirty) {
      const confirmDiscard = window.confirm(
        '저장되지 않은 변경 사항이 있습니다. 정말 닫으시겠습니까?'
      )
      if (!confirmDiscard) return
    }
    setIsDirty(false)
    onClose()
  }

  const handleSaveSuccess = () => {
    setIsDirty(false)
    loadProviderStatuses()
    if (onSaved) {
      onSaved()
    }
  }

  return (
    <div className="settings-modal-backdrop" onClick={handleClose}>
      <div
        className="settings-modal-panel glass"
        onClick={(e) => e.stopPropagation()}
      >
        <header className="settings-modal-header">
          <div className="settings-modal-title">
            <SlidersHorizontal size={18} className="icon-neon" />
            <b>Settings Center</b>
          </div>
          <button className="icon-btn close-btn" onClick={handleClose}>
            <X size={18} />
          </button>
        </header>

        <div className="settings-modal-body">
          <SettingsNavigator
            items={settingsNavigation}
            activeId={activeTab}
            onSelect={handleSelectTab}
            searchQuery={searchQuery}
            onSearchChange={setSearchQuery}
            providerStatuses={providerStatuses}
          />
          <div className="settings-content-area">
            <SettingsPage
              activeId={activeTab}
              onDirtyChange={setIsDirty}
              onSaveSuccess={handleSaveSuccess}
            />
          </div>
        </div>

        <footer className="settings-modal-footer">
          <div className="settings-footer-status">
            {isDirty && (
              <span className="dirty-indicator">
                <AlertCircle size={14} /> Unsaved changes
              </span>
            )}
          </div>
          <div className="settings-footer-actions">
            <button className="secondary-btn" onClick={handleClose}>
              Cancel
            </button>
            <button className="primary-btn" onClick={handleClose}>
              Done
            </button>
          </div>
        </footer>
      </div>
    </div>
  )
}
