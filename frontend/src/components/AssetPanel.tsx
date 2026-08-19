import { Search, Users, Map, Package, Shirt, Car, Mic } from 'lucide-react'

const rows = [
  ['Actors', 12, Users],
  ['Voices', 9, Mic],
  ['Locations', 28, Map],
  ['Wardrobe', 41, Shirt],
  ['Vehicles', 8, Car],
  ['Props', 73, Package],
] as const

export default function AssetPanel() {
  return (
    <section className="asset-panel glass">
      <div className="panel-title">Asset Library</div>
      <div className="asset-search"><Search size={15}/><span>Search assets...</span></div>
      <div className="asset-list">
        {rows.map(([name, count, Icon]) => (
          <div className="asset-row" key={name}>
            <div className="asset-icon"><Icon size={18}/></div>
            <span>{name}</span>
            <b>{count}</b>
          </div>
        ))}
      </div>
      <button className="secondary-btn">Open Asset Library</button>
    </section>
  )
}
