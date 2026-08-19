import LMStudioSettings from './pages/providers/LMStudioSettings'
import OpenAISettings from './pages/providers/OpenAISettings'
import CustomProviderSettings from './pages/providers/CustomProviderSettings'
import ImageGenerationSettings from './pages/generation/ImageGenerationSettings'
import TTSSettings from './pages/generation/TTSSettings'
import VideoGenerationSettings from './pages/generation/VideoGenerationSettings'
import GeneralSettings from './pages/GeneralSettings'
import WorkflowSettings from './pages/WorkflowSettings'
import QueueSettings from './pages/QueueSettings'
import AssetSettings from './pages/AssetSettings'
import StorageSettings from './pages/StorageSettings'
import AppearanceSettings from './pages/AppearanceSettings'
import AdvancedSettings from './pages/AdvancedSettings'
import MirStudioMcpSettings from './pages/mcp/MirStudioMcpSettings'

interface SettingsPageProps {
  activeId: string
  onDirtyChange?: (isDirty: boolean) => void
  onSaveSuccess?: () => void
}

export default function SettingsPage({
  activeId,
  onDirtyChange,
  onSaveSuccess,
}: SettingsPageProps) {
  switch (activeId) {
    case 'lmstudio':
      return (
        <LMStudioSettings
          onDirtyChange={onDirtyChange}
          onSaveSuccess={onSaveSuccess}
        />
      )
    case 'openai':
      return <OpenAISettings />
    case 'custom-llm':
      return <CustomProviderSettings />
    case 'image':
      return <ImageGenerationSettings />
    case 'tts':
      return <TTSSettings />
    case 'video':
      return <VideoGenerationSettings />
    case 'mir-studio-mcp':
      return <MirStudioMcpSettings onDirtyChange={onDirtyChange} onSaveSuccess={onSaveSuccess} />
    case 'general':
      return <GeneralSettings />
    case 'workflow':
      return <WorkflowSettings />
    case 'queue':
      return <QueueSettings />
    case 'assets':
      return <AssetSettings />
    case 'storage':
      return <StorageSettings />
    case 'appearance':
      return <AppearanceSettings />
    case 'advanced':
      return <AdvancedSettings />
    default:
      return (
        <LMStudioSettings
          onDirtyChange={onDirtyChange}
          onSaveSuccess={onSaveSuccess}
        />
      )
  }
}
