---
route: /documentation/PHASE
source_url: https://developer.apple.com/documentation/PHASE
source_locale: en-US
section: docc
content_type: symbol
title: PHASE
original_title: PHASE
source_hash: eb368f55bb250b318cf2704824f89e4610f587e14ae25166a83614dd7da97253
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:04:39+00:00'
last_translated_at: '2026-03-14T03:18:00+09:00'
---

# PHASE

환경의 이벤트와 신호에 반응하는 동적인 오디오 경험을 게임이나 앱에서 만듭니다.

## 개요

게임과 앱에 복잡하고 동적인 오디오 경험을 제공하려면 PHASE(Physical Audio Spatialization Engine)를 사용하십시오. PHASE를 사용하면 사운드 layer를 제어하고 오디오 매개변수를 실시간으로 조정할 수 있습니다. 앱을 개발할 때 시각 장면과의 동적 통합을 통해 오디오는 논리와 시각적 변화에 자동으로 반응합니다. 이 프레임워크는 다양한 오디오 하드웨어를 지원하므로, 앱은 헤드폰과 스피커 같은 출력 장치를 포함해 여러 플랫폼에서 일관된 공간 오디오 경험을 제공할 수 있습니다.

![PHASE 기능을 보여 주는 게임 장면 일러스트입니다. 왼쪽에서는 다각형 안의 dragon에서 hero를 향해 sound wave가 방출되고, volumetric sound source와 sound event hierarchy callout이 표시됩니다. 오른쪽에서는 dragon의 fireball이 rock과 충돌하고, rock 뒤 영역을 제외한 방향으로 sound wave가 퍼지며 geometric sound occlusion callout이 표시됩니다.](https://developer.apple.com)

:::note Note
게임이나 앱의 오디오가 환경 이벤트나 신호를 포함하지 않는다면 [AVFoundation](https://developer.apple.com/documentation/AVFoundation) 또는 [Core Audio](https://developer.apple.com/documentation/CoreAudio)를 사용할 수 있습니다.
:::

### 시각 시뮬레이션과 오디오 통합하기

세밀한 환경을 모델링하는 앱과 게임은 개발 중에 많은 수정이 일어납니다. PHASE에 앱 장면에 대한 기본 이해를 제공하면 오디오는 그 장면의 특성에 맞춰 재생됩니다. 게임 레벨을 추가하는 것처럼 장면을 수정하면 오디오도 장면의 시각적 형태와 속성에 맞춰 따라갑니다. PHASE는 소리와 시각 요소를 결합하고 앱의 오디오 유지 보수 부담을 줄여 줍니다.

- 장면 geometry를 받아서, 소리를 내는 장면 객체가 가려질 때 볼륨을 줄입니다. 예를 들어 플레이어가 벽 뒤에 숨으면 날아오는 fireball의 볼륨을 낮춥니다.
- 앱의 런타임 상태에 반응해 재생되는 복잡한 sound event를 제공합니다.
- 형태에서 퍼져 나오는 sound effect를 추가합니다. 장면 객체의 형태를 PHASE에 제공하면, 소리의 볼륨은 플레이어와 그 형태 사이의 거리와 방향에 따라 조절됩니다.
- reverberation과 시간 지연 오디오 반사를 추가해 환경 효과를 만들고 실내 장면을 시뮬레이션합니다.

:::topic-grid
## 기초
- [Playing sound from a location in a 3D scene](https://developer.apple.com/documentation/phase/playing-sound-from-a-location-in-a-3d-scene): 특정 방향의 위치에서 소리를 배치하고 환경에 따라 볼륨을 자동으로 높이거나 낮춥니다.
- [Personalizing spatial audio in your app](https://developer.apple.com/documentation/phase/personalizing-spatial-audio-in-your-app): 사용자의 머리 움직임을 추적하고 개인 공간 오디오 프로필을 반영해 공간 오디오 출력의 현실감을 향상합니다.
- [PHASE updates](https://developer.apple.com/documentation/Updates/PHASE): PHASE의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 설정
- [PHASEEngine](https://developer.apple.com/documentation/phase/phaseengine): 오디오 asset를 관리하고, 재생을 제어하고, 환경 효과를 구성하는 객체입니다.
- [PHASEEngine.UpdateMode](https://developer.apple.com/documentation/phase/phaseengine/updatemode): 프레임워크가 API 호출을 소비하고 내부 상태를 업데이트하는 시점을 결정하는 mode입니다.
- [PHASEEngine.RenderingMode](https://developer.apple.com/documentation/phase/phaseengine/renderingmode): 시스템이 오디오를 프로세스 내부 또는 외부에서 렌더링할지를 결정하는 mode입니다.
- [PHASEAssetRegistry](https://developer.apple.com/documentation/phase/phaseassetregistry): 오디오 asset의 중앙 저장소입니다.
- [PHASENormalizationMode](https://developer.apple.com/documentation/phase/phasenormalizationmode): 프레임워크가 사용자의 출력 장치에 맞게 sound asset의 loudness를 조정할지를 결정하는 옵션입니다.
- [PHASESpatializationMode](https://developer.apple.com/documentation/phase/phasespatializationmode): PHASE가 공간 오디오를 출력하는 방식입니다.
- [PHASEReverbPreset](https://developer.apple.com/documentation/phase/phasereverbpreset): PHASE가 공명음을 확산하는 방식입니다.
- [PHASEMedium](https://developer.apple.com/documentation/phase/phasemedium): 소리가 전달되는 방식에 영향을 주는 환경의 속성 또는 품질입니다.
:::

:::topic-grid
## 사운드스케이프 생성
- [PHASESource](https://developer.apple.com/documentation/phase/phasesource): 장면 안의 3D 위치와 방향에서 오디오를 재생하는 객체입니다.
- [PHASEListener](https://developer.apple.com/documentation/phase/phaselistener): 사용자가 가장 잘 들을 수 있는 장면 안의 위치를 정의하는 기준점입니다.
- [PHASEOccluder](https://developer.apple.com/documentation/phase/phaseoccluder): listener에게 오디오가 도달하는 것을 막는 형태와 위치를 가진 객체입니다.
- [PHASEObject](https://developer.apple.com/documentation/phase/phaseobject): 장면 안의 객체입니다.
- [PHASEShape](https://developer.apple.com/documentation/phase/phaseshape): 연결되어 3D volume을 형성하는 점들의 집합입니다.
- [PHASEShape.Element](https://developer.apple.com/documentation/phase/phaseshape/element): 물리 표면의 특성을 설명하는 객체입니다.
- [PHASEMaterial](https://developer.apple.com/documentation/phase/phasematerial): 객체의 음향 특성을 결정하는 표면 특성입니다.
- [PHASEMaterialPreset](https://developer.apple.com/documentation/phase/phasematerialpreset): 각각 앱 오디오에 고유한 음향 특성을 더하는 물리 표면의 모음입니다.
- [PHASEMixerParameters](https://developer.apple.com/documentation/phase/phasemixerparameters): sound event용 mixer를 지정하고 이를 3D 공간에 배치하는 객체입니다.
:::

:::topic-grid
## 오디오 선택 및 재생
- [PHASESoundAsset](https://developer.apple.com/documentation/phase/phasesoundasset): asset registry에 저장된 사운드 리소스입니다.
- [PHASESoundEvent](https://developer.apple.com/documentation/phase/phasesoundevent): 어떤 오디오를 재생할지 결정하는 객체입니다.
- [PHASESoundEvent.RenderingState](https://developer.apple.com/documentation/phase/phasesoundevent/renderingstate-swift.enum): 오디오의 재생 상태입니다.
- [PHASESoundEventNodeDefinition](https://developer.apple.com/documentation/phase/phasesoundeventnodedefinition): 연결되어 node 계층 구조를 형성하는 sound event node의 기본 클래스입니다.
- [PHASESoundEventNodeAsset](https://developer.apple.com/documentation/phase/phasesoundeventnodeasset): 환경 상태에 반응해 재생될 수 있는 사운드를 위한 템플릿 객체입니다.
- [PHASEAsset](https://developer.apple.com/documentation/phase/phaseasset): 프레임워크 asset에 이름을 더하는 기본 클래스입니다.
- [Sound Event Nodes](https://developer.apple.com/documentation/phase/sound-event-nodes): 오디오 작업의 계층 트리를 형성하도록 연결되는 객체입니다.
:::

:::topic-grid
## 오디오 레이어링 및 효과
- [PHASEChannelMixerDefinition](https://developer.apple.com/documentation/phase/phasechannelmixerdefinition): 소리를 장치 출력으로 직접 보내는 오디오 레이어링 객체입니다.
- [PHASEAmbientMixerDefinition](https://developer.apple.com/documentation/phase/phaseambientmixerdefinition): 3D 공간의 특정 방향으로 소리를 출력하는 오디오 레이어링 객체입니다.
- [PHASEMixerDefinition](https://developer.apple.com/documentation/phase/phasemixerdefinition): 주어진 구성으로 mixer를 초기화하는 객체입니다.
- [PHASEMixer](https://developer.apple.com/documentation/phase/phasemixer): 여러 오디오 신호를 하나의 신호로 결합하는 객체입니다.
- [PHASEDefinition](https://developer.apple.com/documentation/phase/phasedefinition): 프레임워크 definition에 이름을 더하는 기본 클래스입니다.
- [Spatial Mixing](https://developer.apple.com/documentation/phase/spatial-mixing): 앱의 3D soundscape에서 소리가 재생되는 방식을 결정하는 환경 특성을 정의합니다.
:::

:::topic-grid
## 동적 사운드 제어
- [PHASEEnvelope](https://developer.apple.com/documentation/phase/phaseenvelope): 선형 입력에 대해 복잡한 곡선을 그래프로 그리도록 연결되는 segment 모음입니다.
- [PHASEEnvelopeSegment](https://developer.apple.com/documentation/phase/phaseenvelopesegment): envelope의 곡선 구간입니다.
- [PHASECurveType](https://developer.apple.com/documentation/phase/phasecurvetype): 입력 값에 수학 함수를 적용하는 옵션입니다.
- [PHASENumericPair](https://developer.apple.com/documentation/phase/phasenumericpair): envelope의 bounding box를 정의하는 순서쌍입니다.
- [Playback Parameterization](https://developer.apple.com/documentation/phase/playback-parameterization): 런타임에 속성을 조정해 재생 중인 오디오의 특성을 바꿉니다.
:::

:::topic-grid
## 사운드 그룹화 및 관리
- [PHASEGroup](https://developer.apple.com/documentation/phase/phasegroup): 사운드 모음과 오디오 매개변수를 공유하는 container입니다.
- [PHASEGroupPreset](https://developer.apple.com/documentation/phase/phasegrouppreset): group용 설정 모음입니다.
- [PHASEGroupPresetSetting](https://developer.apple.com/documentation/phase/phasegrouppresetsetting): group preset의 설정입니다.
- [PHASEDucker](https://developer.apple.com/documentation/phase/phaseducker): 경쟁하는 사운드를 관리하는 객체입니다.
:::

:::topic-grid
## 오류
- [PHASE Errors](https://developer.apple.com/documentation/phase/phase-errors): PHASE 프레임워크가 보고하는 오류입니다.
:::

:::topic-grid
## 클래스
- [PHASEPullStreamNode](https://developer.apple.com/documentation/phase/phasepullstreamnode)
- [PHASEPullStreamNodeDefinition](https://developer.apple.com/documentation/phase/phasepullstreamnodedefinition)
- [PHASEStreamNode](https://developer.apple.com/documentation/phase/phasestreamnode)
:::

:::topic-grid
## 구조체
- [PHASEAutomaticHeadTrackingFlags](https://developer.apple.com/documentation/phase/phaseautomaticheadtrackingflags)
:::

:::topic-grid
## 타입 별칭
- [PHASEPullStreamRenderHandler](https://developer.apple.com/documentation/phase/phasepullstreamrenderhandler)
:::
