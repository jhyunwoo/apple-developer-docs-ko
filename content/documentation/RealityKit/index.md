---
route: /documentation/RealityKit
source_url: https://developer.apple.com/documentation/RealityKit
source_locale: en-US
section: docc
content_type: symbol
title: RealityKit
original_title: RealityKit
source_hash: 280816677f41f009c8bc47e3b1df89021d68fcc8c43d3817d6cd3afb5971e1ee
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:07:36+00:00'
last_translated_at: '2026-03-14T03:28:00+09:00'
---

# RealityKit

증강 현실 앱에서 사용할 3D 콘텐츠를 시뮬레이션하고 렌더링합니다.

## 개요

RealityKit은 iOS, iPadOS, macOS, tvOS, visionOS용 3D 또는 증강 현실(AR) 앱을 만들 때 사용할 수 있는 고성능 3D 시뮬레이션 및 렌더링 기능을 제공합니다. RealityKit은 [ARKit](https://developer.apple.com/documentation/ARKit)을 활용해 가상 객체를 현실 세계에 자연스럽게 통합하는 AR 우선 3D 프레임워크입니다.

![극장처럼 구성된 가상 창고 환경을 보여 주는 스크린샷입니다. 큰 떠 있는 화면에는 바퀴 달린 로봇이 야외 환경을 이동하는 영화가 재생되고 있습니다.](https://developer.apple.com)

RealityKit의 풍부한 기능을 사용해 매력적인 증강 현실 경험을 만드십시오.

- visionOS용 Reality Composer Pro를 사용해 모델, 애니메이션, Spatial Audio가 포함된 전체 RealityKit scene을 생성하고 가져오기
- 코드에서 3D 모델, 도형 primitive, 사운드를 추가해 런타임에 scene을 빌드하거나 수정하기
- 가상 객체가 현실 세계의 객체와 상호 작용하게 하기
- 수동 또는 physics simulation으로 객체를 애니메이션하기
- 사용자 입력과 주변 환경 변화에 반응하기
- 기기 간 동기화 및 SharePlay를 사용해 그룹 AR 경험 지원하기

:::topic-grid
## 기초
- [Understanding the modular architecture of RealityKit](https://developer.apple.com/documentation/visionOS/understanding-the-realitykit-modular-architecture): RealityKit의 구성 요소가 어떻게 맞물리는지 이해합니다.
- [Building an immersive experience with RealityKit](https://developer.apple.com/documentation/realitykit/building-an-immersive-experience-with-realitykit): system과 postprocessing effect를 사용해 사실적인 수중 장면을 만듭니다.
- [Entity](https://developer.apple.com/documentation/realitykit/entity): 외형과 동작 특성을 제공하는 component를 붙이는 RealityKit scene의 요소입니다.
- [Component](https://developer.apple.com/documentation/realitykit/component): entity에 적용하는 geometry 또는 behavior의 표현입니다.
:::

:::topic-grid
## 표시
- [Views and attachments](https://developer.apple.com/documentation/realitykit/presentation-views-and-attachments): view와 renderer를 사용해 앱으로 RealityKit 콘텐츠를 가져옵니다.
- [Presentation UI](https://developer.apple.com/documentation/realitykit/presentation-user-interface): 앱 콘텐츠와 사용자의 상호 작용 방식을 제어합니다.
:::

:::topic-grid
## scene 관리 및 로직
- [Scenes](https://developer.apple.com/documentation/realitykit/ecs-scenes): 모든 RealityKit entity를 담는 문맥입니다.
- [Systems](https://developer.apple.com/documentation/realitykit/ecs-systems): RealityKit scene 안의 entity에 behavior와 물리 효과를 적용합니다.
- [Events](https://developer.apple.com/documentation/realitykit/ecs-events): 특정 event type을 구독해 RealityKit scene에서 일어나는 일에 반응합니다.
- [Entity actions](https://developer.apple.com/documentation/realitykit/ecs-entity-actions): 앱 상태나 RealityKit scene을 바꾸거나 entity를 애니메이션할 수 있는 단순하고 재사용 가능한 action을 만듭니다.
:::

:::topic-grid
## asset 생성
- [Reality Composer Pro](https://developer.apple.com/documentation/RealityComposerPro): RealityKit 앱용 3D 콘텐츠를 구축하고, 만들고, 설계합니다.
- [Swift Splash](https://developer.apple.com/documentation/visionOS/swift-splash): RealityKit을 사용해 visionOS에서 상호 작용 가능한 놀이기구를 만듭니다.
- [Diorama](https://developer.apple.com/documentation/visionOS/diorama): Reality Composer Pro를 사용해 visionOS 앱의 장면을 설계합니다.
- [Presenting an artist’s scene](https://developer.apple.com/documentation/realitykit/presenting-an-artists-scene): visionOS에서 Reality Composer Pro의 장면을 표시합니다.
- [Object capture](https://developer.apple.com/documentation/realitykit/realitykit-object-capture): photogrammetry를 사용해 일련의 사진에서 3D 객체를 만듭니다.
- [USD](https://developer.apple.com/documentation/USD): 3D 장면을 표현하기 위한 효율적이고 확장 가능한 방법입니다.
- [Composing interactive 3D content with RealityKit and Reality Composer Pro](https://developer.apple.com/documentation/realitykit/composing-interactive-3d-content-with-realitykit-and-reality-composer-pro): 애니메이션 timeline을 사용해 상호 작용하는 장면을 구축합니다.
:::

:::topic-grid
## scene 콘텐츠
- [Hello World](https://developer.apple.com/documentation/visionOS/World): window, volume, immersive space를 사용해 사람들에게 지구를 소개합니다.
- [Enabling video reflections in an immersive environment](https://developer.apple.com/documentation/visionOS/enabling-video-reflections-in-an-immersive-environment): 사용자 정의 환경에 비디오 반사를 추가해 더 몰입감 있는 경험을 만듭니다.
- [Creating a spatial drawing app with RealityKit](https://developer.apple.com/documentation/realitykit/creating-a-spatial-drawing-app-with-realitykit): 저수준 mesh 및 texture API를 사용해 RealityKit을 ARKit 및 SwiftUI와 통합함으로써 사용자의 brush stroke를 빠르게 업데이트합니다.
- [Generating interactive geometry with RealityKit](https://developer.apple.com/documentation/realitykit/generating-interactive-geometry-with-realitykit): 저수준 mesh와 저수준 texture로 상호 작용 가능한 mesh를 만듭니다.
- [Combining 2D and 3D views in an immersive app](https://developer.apple.com/documentation/realitykit/combining-2d-and-3d-views-in-an-immersive-app): attachment를 사용해 visionOS 앱에서 3D 콘텐츠를 기준으로 2D 콘텐츠를 배치합니다.
- [Transforming RealityKit entities using gestures](https://developer.apple.com/documentation/realitykit/transforming-realitykit-entities-with-gestures): 어떤 entity에서든 표준 visionOS gesture를 지원하는 RealityKit component를 구축합니다.
- [Responding to gestures on an entity](https://developer.apple.com/documentation/realitykit/responding-to-gestures-on-an-entity): input target 및 collision component를 사용해 RealityKit entity에 수행된 gesture에 반응합니다.
- [Models and meshes](https://developer.apple.com/documentation/realitykit/scene-content-models-and-meshes): mesh 기반 모델로 scene에 가상 객체를 표시합니다.
- [Materials, textures, and shaders](https://developer.apple.com/documentation/realitykit/scene-content-materials-and-shaders): scene의 3D 객체 표면에 texture를 적용해 각 객체에 고유한 외형을 부여합니다.
- [Anchors](https://developer.apple.com/documentation/realitykit/scene-content-anchors): 가상 콘텐츠를 현실 세계에 고정합니다.
- [Lights and cameras](https://developer.apple.com/documentation/realitykit/scene-content-lights-and-cameras): scene의 조명과 시점을 제어합니다.
- [Content synchronization](https://developer.apple.com/documentation/realitykit/scene-content-content-synchronization): entity 콘텐츠를 로컬 또는 네트워크 전반에서 동기화합니다.
- [Audio](https://developer.apple.com/documentation/realitykit/scene-content-audio): 개인화되고 현실적인 공간 오디오 경험을 만듭니다.
- [Videos](https://developer.apple.com/documentation/realitykit/scene-content-videos): RealityKit 경험에서 비디오를 표시합니다.
- [Images](https://developer.apple.com/documentation/realitykit/scene-content-images): RealityKit 경험에서 이미지와 공간 장면을 표시합니다.
:::

:::topic-grid
## 게임 개발
- [Gaming sample code projects](https://developer.apple.com/documentation/realitykit/game-development-sample-code): 게임 개발과 관련된 프로젝트 모음을 살펴봅니다.
- [Entity animations](https://developer.apple.com/documentation/realitykit/game-development-entity-animations): 런타임에 entity를 동적으로 이동, 회전, 크기 조정합니다.
- [Character control, skeletons, and inverse kinematics](https://developer.apple.com/documentation/realitykit/game-development-character-skeletons): 모델의 움직임과 애니메이션을 지시합니다.
:::

:::topic-grid
## 물리 시뮬레이션
- [Collision detection](https://developer.apple.com/documentation/realitykit/physics-collision-detection): entity가 서로 또는 환경과 충돌하는 시점을 판단합니다.
- [Simulations and motion](https://developer.apple.com/documentation/realitykit/physics-simulations-and-motion): entity 또는 system 간 물리 상호 작용을 시뮬레이션합니다.
- [Force effects](https://developer.apple.com/documentation/realitykit/physics-force-effects): 힘을 사용해 가상 객체의 움직임을 제어합니다.
- [Physics joints and pins](https://developer.apple.com/documentation/realitykit/physics-joints-and-pins): 가상 객체를 연결하는 joint physics를 시뮬레이션합니다.
:::

:::topic-grid
## 성능 향상
- [Improving the Performance of a RealityKit App](https://developer.apple.com/documentation/realitykit/improving-the-performance-of-a-realitykit-app): CPU와 GPU 사용량을 측정해 앱 성능을 개선할 방법을 찾습니다.
- [Reducing GPU Utilization in Your RealityKit App](https://developer.apple.com/documentation/realitykit/reducing-gpu-utilization-in-your-realitykit-app): 렌더링 복잡도를 줄여 GPU가 앱의 frame rate를 제한하지 않도록 합니다.
- [Reducing CPU Utilization in Your RealityKit App](https://developer.apple.com/documentation/realitykit/reducing-cpu-utilization-in-your-realitykit-app): 앱과 콘텐츠를 조정해 특정 CPU metric을 목표로 최적화합니다.
- [Construct an immersive environment for visionOS](https://developer.apple.com/documentation/realitykit/construct-an-immersive-environment-for-visionos): 앱을 위한 효율적인 사용자 정의 world를 구축합니다.
- [Passing Metal command objects around your application](https://developer.apple.com/documentation/realitykit/passing-metal-command-objects-around-your-application): Metal compute shader를 dispatch하는 entity에 Metal command object를 생성해 전달하는 system을 구축합니다.
:::

:::topic-grid
## 아티클
- [Rendering stereoscopic video with RealityKit](https://developer.apple.com/documentation/realitykit/rendering-stereoscopic-video-with-realitykit): RealityKit으로 visionOS에서 입체 비디오를 렌더링합니다.
:::
