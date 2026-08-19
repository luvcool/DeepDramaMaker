import { Search } from 'lucide-react'
import type { NavItem } from './settingsNavigation'

interface SettingsNavigatorProps {
  items: NavItem[]
  activeId: string
  onSelect: (id: string) => void
  searchQuery: string
  onSearchChange: (query: string) => void
  providerStatuses?: Record<string, 'ONLINE' | 'DEGRADED' | 'OFFLINE' | 'DISABLED'>
}

export default function SettingsNavigator({
  items,
  activeId,
  onSelect,
  searchQuery,
  onSearchChange,
  providerStatuses = {},
}: SettingsNavigatorProps) {
  const query = searchQuery.toLowerCase().trim()

  const filterItem = (item: NavItem): boolean => {
    if (!query) return true
    const labelMatch = item.label.toLowerCase().includes(query)
    const keywordMatch = item.keywords?.some((k) => k.toLowerCase().includes(query))
    const childrenMatch = item.children?.some((c) => filterItem(c))
    return Boolean(labelMatch || keywordMatch || childrenMatch)
  }

  const filteredItems = items.filter((item) => filterItem(item))

  return (
    <div className="settings-nav">
      <div className="settings-nav-search">
        <Search size={14} />
        <input
          type="text"
          placeholder="Search settings..."
          value={searchQuery}
          onChange={(e) => onSearchChange(e.target.value)}
        />
      </div>

      <div className="settings-nav-list">
        {filteredItems.map((item) => {
          if (item.children && item.children.length > 0) {
            const childItems = query
              ? item.children.filter((c) => filterItem(c))
              : item.children

            return (
              <div key={item.id} className="settings-nav-group">
                <div className="settings-nav-group-title">{item.label}</div>
                <div className="settings-nav-group-children">
                  {childItems.map((child) => {
                    const isActive = activeId === child.id
                    const status = providerStatuses[child.id] || child.status

                    return (
                      <button
                        key={child.id}
                        type="button"
                        disabled={child.disabled}
                        className={`settings-nav-item child ${isActive ? 'active' : ''} ${
                          child.disabled ? 'disabled' : ''
                        }`}
                        onClick={() => !child.disabled && onSelect(child.id)}
                      >
                        <span>{child.label}</span>
                        {status && (
                          <span className={`status-dot ${status.toLowerCase()}`}>●</span>
                        )}
                        {child.badge && <span className="nav-badge">{child.badge}</span>}
                      </button>
                    )
                  })}
                </div>
              </div>
            )
          }

          const isActive = activeId === item.id

          return (
            <button
              key={item.id}
              type="button"
              disabled={item.disabled}
              className={`settings-nav-item ${isActive ? 'active' : ''} ${
                item.disabled ? 'disabled' : ''
              }`}
              onClick={() => !item.disabled && onSelect(item.id)}
            >
              <span>{item.label}</span>
              {item.badge && <span className="nav-badge">{item.badge}</span>}
            </button>
          )
        })}
      </div>
    </div>
  )
}
