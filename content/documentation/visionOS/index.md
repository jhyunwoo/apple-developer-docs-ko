---
route: /documentation/visionOS
source_url: https://developer.apple.com/documentation/visionOS
source_locale: en-US
section: docc
content_type: article
title: visionOS
original_title: visionOS
source_hash: 261178b6f7ea08e90f850e821677466f7eac0da04f0ce8fc4ff9c3cfbbf58f9e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:49:12+00:00'
last_translated_at: '2026-03-14T02:20:00+09:00'
---

# visionOS

Apple Vision Pro를 위한 새로운 차원의 앱과 게임을 만듭니다.

## 개요

visionOS는 Apple Vision Pro를 구동하는 운영 체제입니다. 익숙한 도구와 기술을 visionOS와 함께 사용해 공간 컴퓨팅을 위한 몰입형 앱과 게임을 구축하십시오.

![음악 앱, 창에 연결된 도구의 클로즈업, 사진 브라우저를 보여 주는 visionOS 앱의 세 장면입니다.](https://developer.apple.com)

visionOS용 개발에는 Apple silicon이 탑재된 Mac이 필요합니다. visionOS에서 제공하는 몰입도의 스펙트럼을 최대한 활용하려면 SwiftUI를 사용해 새 앱을 만드십시오. 기존 iPad 또는 iPhone 앱이 있다면 앱 target에 visionOS 대상을 추가해 표준 시스템 외관에 접근하고, 매력적인 경험을 만들기 위해 플랫폼별 기능을 더하십시오. 그동안 콘텐츠를 계속 제공하려면 visionOS에서 실행되는 호환 버전의 앱을 배포하십시오.

### 앱을 몰입형 공간으로 확장하기

### 새로운 상호 작용 방식 탐색하기

사람들은 요소를 바라본 뒤 손가락을 모아 탭하는 방식으로 요소를 선택할 수 있습니다. 또한 특정 hand gesture를 사용해 객체를 pinch, drag, zoom, rotate할 수도 있습니다. [SwiftUI](https://developer.apple.com/documentation/SwiftUI)는 이러한 표준 gesture를 기본 지원하므로 앱 입력의 대부분은 이를 활용하십시오. 표준 gesture를 넘어서는 상호 작용이 필요할 때는 [ARKit](https://developer.apple.com/documentation/ARKit)을 사용해 사용자 정의 gesture를 만드십시오.

### 주요 sample 앱 살펴보기

Hello World로 모든 visionOS 앱의 핵심 개념을 살펴보십시오. Happy Beam으로 ARKit을 사용해 사용자 정의 gesture를 감지하는 방법을 이해하십시오. Destination Video로 2D 및 입체 미디어 스트리밍을 알아보십시오. 그리고 Diorama와 Swift Splash로 RealityKit 및 Reality Composer Pro를 사용해 3D 장면을 구축하는 방법을 배워 보십시오.

:::topic-grid
## 앱 구성
- [Creating your first visionOS app](https://developer.apple.com/documentation/visionos/creating-your-first-visionos-app): SwiftUI를 사용해 새 visionOS 앱을 만들고 플랫폼별 기능을 추가합니다.
- [Adding 3D content to your app](https://developer.apple.com/documentation/visionos/adding-3d-content-to-your-app): visionOS 앱에 깊이와 차원을 더하고, 앱 콘텐츠를 사용자의 주변 환경에 통합하는 방법을 알아봅니다.
- [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionos/creating-fully-immersive-experiences): RealityKit 또는 Metal로 만든 콘텐츠와 공간을 결합해 완전한 몰입형 경험을 구축합니다.
- [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionos/drawing-sharp-layer-based-content): visionOS의 사용자 정의 Core Animation layer에서 여러 해상도의 텍스트와 벡터 이미지를 제공합니다.
- [Introductory visionOS samples](https://developer.apple.com/documentation/visionos/introductory-visionos-samples): 입문자에게 친화적인 sample code 프로젝트로 visionOS 앱 개발의 기본을 배웁니다.
- [Combining spatial support from multiple frameworks](https://developer.apple.com/documentation/visionos/combining-spatial-support-from-multiple-frameworks): 여러 프레임워크의 기능을 매끄럽게 통합해 공간 앱을 향상합니다.
- [Connecting iPadOS and visionOS apps over the local network](https://developer.apple.com/documentation/visionos/connecting-ipados-and-visionos-apps-over-the-local-network): visionOS 앱을 제어하는 iPadOS companion 앱을 구축합니다.
:::

:::topic-grid
## 디자인
- [Designing for visionOS](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-visionos): Apple Vision Pro를 착용하면 사람들은 무한한 3D 공간에 들어가 주변 환경과 연결된 상태로 앱이나 게임과 상호 작용할 수 있습니다.
- [Adopting best practices for privacy and user preferences](https://developer.apple.com/documentation/visionos/adopting-best-practices-for-privacy): 민감한 정보 사용을 최소화하고, 사용하는 정보와 사용 방법을 명확히 설명합니다.
- [Improving accessibility support in your visionOS app](https://developer.apple.com/documentation/visionos/improving-accessibility-support-in-your-app): visionOS에서 누구나 앱 콘텐츠에 접근할 수 있도록 코드를 업데이트합니다.
:::

:::topic-grid
## SwiftUI
- [Canyon Crosser: Building a volumetric hike-planning app](https://developer.apple.com/documentation/visionos/canyon-crosser-building-a-volumetric-hike-planning-app): SwiftUI와 RealityKit을 사용해 하이킹 계획 앱을 만듭니다.
- [Hello World](https://developer.apple.com/documentation/visionos/world): window, volume, immersive space를 사용해 사람들에게 지구를 소개합니다.
- [Presenting windows and spaces](https://developer.apple.com/documentation/visionos/presenting-windows-and-spaces): 앱 인터페이스를 구성하는 장면을 열고 닫습니다.
- [Positioning and sizing windows](https://developer.apple.com/documentation/visionos/positioning-and-sizing-windows): 앱이 표시하는 window의 초기 geometry에 영향을 줍니다.
- [Adopting best practices for persistent UI](https://developer.apple.com/documentation/visionos/adopting-best-practices-for-scene-restoration): scene restoration을 관리하고, window 동작을 사용자화하고, surface snapping 데이터를 활용해 지속적이고 맥락에 맞는 공간 경험을 만듭니다.
:::

:::topic-grid
## RealityKit and Reality Composer Pro
- [Reality Composer Pro](https://developer.apple.com/documentation/RealityComposerPro): RealityKit 앱용 3D 콘텐츠를 구축하고, 만들고, 설계합니다.
- [Petite Asteroids: Building a volumetric visionOS game](https://developer.apple.com/documentation/visionos/petite-asteroids-building-a-volumetric-visionos-game): 최신 RealityKit API를 사용해 visionOS용 아름다운 비디오 게임을 만듭니다.
- [BOT-anist](https://developer.apple.com/documentation/visionos/bot-anist): window, volume, animation을 사용해 로봇 식물학자의 온실을 만드는 멀티플랫폼 앱을 구축합니다.
- [Swift Splash](https://developer.apple.com/documentation/visionos/swift-splash): RealityKit을 사용해 visionOS에서 상호 작용 가능한 놀이기구를 만듭니다.
- [Diorama](https://developer.apple.com/documentation/visionos/diorama): Reality Composer Pro를 사용해 visionOS 앱의 장면을 설계합니다.
- [Building an immersive media viewing experience](https://developer.apple.com/documentation/visionos/building-an-immersive-media-viewing-experience): RealityKit과 Reality Composer Pro로 앱의 미디어 재생에 더 깊은 몰입감을 더합니다.
- [Enabling video reflections in an immersive environment](https://developer.apple.com/documentation/visionos/enabling-video-reflections-in-an-immersive-environment): 사용자 정의 환경에 비디오 반사를 추가해 더 몰입감 있는 경험을 만듭니다.
- [Combining 2D and 3D views in an immersive app](https://developer.apple.com/documentation/RealityKit/combining-2d-and-3d-views-in-an-immersive-app): attachment를 사용해 visionOS 앱의 3D 콘텐츠를 기준으로 2D 콘텐츠를 배치합니다.
- [Understanding the modular architecture of RealityKit](https://developer.apple.com/documentation/visionos/understanding-the-realitykit-modular-architecture): RealityKit의 구성 요소가 어떻게 함께 동작하는지 이해합니다.
- [Using transforms to move, scale, and rotate entities](https://developer.apple.com/documentation/visionos/understanding-transforms): RealityKit에서 Transform을 사용해 entity를 이동, 크기 조정, 회전하는 방법을 배웁니다.
- [Capturing screenshots and video from Apple Vision Pro for 2D viewing](https://developer.apple.com/documentation/visionos/capturing-screenshots-and-video-from-your-apple-vision-pro-for-2d-viewing): 앱 미리보기를 위해 visionOS 앱과 주변 환경의 스크린샷을 만들고 고품질 비디오를 녹화합니다.
- [Implementing object tracking in your visionOS app](https://developer.apple.com/documentation/visionos/implementing-object-tracking-in-your-visionos-app): 모델을 학습시켜 실제 객체를 인식하고 추적해 매력적인 상호 작용을 만듭니다.
- [Placing entities using head and device transform](https://developer.apple.com/documentation/visionos/placing-entities-using-head-and-device-transform): Apple Vision Pro의 위치와 회전 변화에 질의하고 반응합니다.
- [Manipulating entities with solid collisions](https://developer.apple.com/documentation/visionos/manipulating-entities-with-solid-collisions): entity, component, system을 사용해 조작 중에도 고체 충돌을 유지하도록 앱 기능을 확장합니다.
:::

:::topic-grid
## ARKit
- [Happy Beam](https://developer.apple.com/documentation/visionos/happybeam): Full Space를 활용해 ARKit 기반의 재미있는 게임을 만듭니다.
- [Setting up access to ARKit data](https://developer.apple.com/documentation/visionos/setting-up-access-to-arkit-data): 앱이 ARKit을 사용할 수 있는지 확인하고 사용자의 개인 정보를 존중합니다.
- [Incorporating real-world surroundings in an immersive experience](https://developer.apple.com/documentation/visionos/incorporating-real-world-surroundings-in-an-immersive-experience): 앱 콘텐츠가 세계의 실제 형태에 반응하도록 만들어 몰입형 경험을 구축합니다.
- [Placing content on detected planes](https://developer.apple.com/documentation/visionos/placing-content-on-detected-planes): 테이블과 바닥 같은 수평 표면과 벽, 문 같은 수직 평면을 감지합니다.
- [Tracking specific points in world space](https://developer.apple.com/documentation/visionos/tracking-points-in-world-space): 앱이 ARKit에 저장한 anchor의 위치와 방향을 가져옵니다.
- [Tracking preregistered images in 3D space](https://developer.apple.com/documentation/visionos/tracking-images-in-3d-space): 사용자의 주변 환경에서 알려진 이미지의 현재 위치를 바탕으로 콘텐츠를 배치합니다.
- [Exploring object tracking with ARKit](https://developer.apple.com/documentation/visionos/exploring_object_tracking_with_arkit): Create ML로 학습한 reference object를 사용해 visionOS에서 실제 객체를 찾고 추적합니다.
- [Object tracking with Reality Composer Pro experiences](https://developer.apple.com/documentation/visionos/object-tracking-with-reality-composer-pro-experiences): visionOS의 object tracking을 사용해 실제 객체에 디지털 콘텐츠를 연결하고 매력적인 경험을 만듭니다.
- [Building local experiences with room tracking](https://developer.apple.com/documentation/visionos/building-local-experiences-with-room-tracking): visionOS의 room tracking을 사용해 물리적 공간과 상호 작용하는 맞춤 경험을 제공합니다.
- [Placing entities using head and device transform](https://developer.apple.com/documentation/visionos/placing-entities-using-head-and-device-transform): Apple Vision Pro의 위치와 회전 변화에 질의하고 반응합니다.
- [Drawing in the air and on surfaces with a spatial stylus](https://developer.apple.com/documentation/visionos/drawing-in-the-air-and-on-surfaces-with-a-spatial-stylus): 공중과 표면 모두에서 지연 시간과 정확도의 균형을 맞춘 spatial stylus 드로잉 경험을 만듭니다.
:::

:::topic-grid
## SharePlay
- [Building a guessing game for visionOS](https://developer.apple.com/documentation/GroupActivities/building-a-guessing-game-for-visionos): Group Activities를 사용해 visionOS용 팀 기반 추측 게임을 만듭니다.
- [Implementing SharePlay for immersive spaces in visionOS](https://developer.apple.com/documentation/visionos/implementing-shareplay-for-immersive-spaces-in-visionos): SharePlay를 사용해 참가자 간 3D 콘텐츠를 동기화함으로써 협업적 공간 경험을 지원합니다.
- [Configure your visionOS app for sharing with people nearby](https://developer.apple.com/documentation/GroupActivities/configure-your-app-for-sharing-with-people-nearby): 같은 공간의 Vision Pro 사용자 및 FaceTime 참가자와 공유 경험을 만듭니다.
- [Adding spatial Persona support to an activity](https://developer.apple.com/documentation/GroupActivities/adding-spatial-persona-support-to-an-activity): visionOS에서 실행될 때 spatial Persona와 shared context를 지원하도록 SharePlay 활동을 업데이트합니다.
- [Synchronizing group gameplay with TabletopKit](https://developer.apple.com/documentation/TabletopKit/synchronizing-group-gameplay-with-tabletopkit): 모든 동전을 먼저 차지하기 위한 경쟁에서 여러 플레이어 간 게임 상태를 유지합니다.
:::

:::topic-grid
## 비디오 재생
- [Destination Video](https://developer.apple.com/documentation/visionos/destination-video): SwiftUI를 사용해 멀티플랫폼 앱에서 몰입형 미디어 경험을 구축합니다.
- [Displaying video from connected devices](https://developer.apple.com/documentation/visionos/displaying-video-from-connected-devices): Developer Strap으로 연결된 기기의 비디오를 visionOS 앱에 표시합니다.
- [Playing immersive media with RealityKit](https://developer.apple.com/documentation/visionos/playing-immersive-media-with-realitykit): RealityKit으로 몰입형 비디오 재생 경험을 만듭니다.
- [Rendering stereoscopic video with RealityKit](https://developer.apple.com/documentation/RealityKit/rendering-stereoscopic-video-with-realitykit): RealityKit으로 visionOS에서 입체 비디오를 렌더링합니다.
- [Creating a multiview video playback experience in visionOS](https://developer.apple.com/documentation/AVKit/creating-a-multiview-video-playback-experience-in-visionos): 여러 비디오를 동시에 재생하고 다양한 경험 유형 전환을 자연스럽게 처리하는 인터페이스를 구축합니다.
- [Configuring your app for media playback](https://developer.apple.com/documentation/AVFoundation/configuring-your-app-for-media-playback): 표준 미디어 재생 동작을 활성화하도록 앱을 구성합니다.
- [Adopting the system player interface in visionOS](https://developer.apple.com/documentation/AVKit/adopting-the-system-player-interface-in-visionos): 3D 비디오 콘텐츠를 위한 최적화된 시청 경험을 제공합니다.
- [Controlling the transport behavior of a player](https://developer.apple.com/documentation/AVFoundation/controlling-the-transport-behavior-of-a-player): 미디어 presentation을 재생, 일시 정지, 탐색합니다.
- [Monitoring playback progress in your app](https://developer.apple.com/documentation/AVFoundation/monitoring-playback-progress-in-your-app): 미디어 asset의 재생을 관찰해 앱의 사용자 인터페이스 상태를 업데이트합니다.
- [Trimming and exporting media in visionOS](https://developer.apple.com/documentation/AVKit/trimming-and-exporting-media-in-visionos): 현재 재생 중인 미디어의 타임라인을 편집할 수 있도록 앱에 표준 컨트롤을 표시합니다.
:::

:::topic-grid
## Xcode 및 시뮬레이터
- [Configuring your app icon using an asset catalog](https://developer.apple.com/documentation/Xcode/configuring-your-app-icon): App Store, 홈 화면, 설정, 검색 결과 등에서 앱을 나타내는 아이콘 변형을 asset catalog에 추가합니다.
- [Diagnosing and resolving bugs in your running app](https://developer.apple.com/documentation/Xcode/diagnosing-and-resolving-bugs-in-your-running-app): 실행 중인 앱을 검사해 버그를 분리하고, crash를 찾고, 과도한 시스템 자원 사용을 식별하고, 메모리 버그를 시각화하고, 모양 문제를 조사합니다.
- [Diagnosing issues in the appearance of a running app](https://developer.apple.com/documentation/Xcode/diagnosing-issues-in-the-appearance-of-your-running-app): 실행 중인 앱을 검사해 표시되는 콘텐츠의 모양과 배치 문제를 조사합니다.
- [Running your app in Simulator or on a device](https://developer.apple.com/documentation/Xcode/running-your-app-in-simulator-or-on-a-device): 시뮬레이터의 iOS, iPadOS, tvOS, visionOS, watchOS 기기나 Mac에 연결된 실제 기기에서 앱을 실행합니다.
- [Interacting with your app in the visionOS simulator](https://developer.apple.com/documentation/Xcode/interacting-with-your-app-in-the-visionos-simulator): Mac을 사용해 Simulator의 visionOS 앱에서 공간을 탐색하고 상호 작용을 제어합니다.
:::

:::topic-grid
## 성능
- [Creating a performance plan for your visionOS app](https://developer.apple.com/documentation/visionos/creating-a-performance-plan-for-visionos-app): 앱의 성능과 전력 목표를 식별하고 이를 측정하고 평가하기 위한 계획을 만듭니다.
- [Analyzing the performance of your visionOS app](https://developer.apple.com/documentation/visionos/analyzing-the-performance-of-your-visionos-app): Instruments의 RealityKit Trace 템플릿을 사용해 visionOS 앱의 성능을 평가하고 개선합니다.
- [Reducing the rendering cost of your UI on visionOS](https://developer.apple.com/documentation/visionos/reducing-the-rendering-cost-of-your-ui-on-visionos): visionOS에서 2D 사용자 인터페이스 렌더링을 최적화합니다.
- [Reducing the rendering cost of RealityKit content on visionOS](https://developer.apple.com/documentation/visionos/reducing-the-rendering-cost-of-realitykit-content-on-visionos): 앱의 3D 증강 현실 콘텐츠가 visionOS에서 효율적으로 렌더링되도록 최적화합니다.
- [Understanding the visionOS render pipeline](https://developer.apple.com/documentation/visionos/understanding-the-visionos-render-pipeline): visionOS가 다른 Apple 플랫폼과 다르게 이벤트를 처리하고 렌더링 루프를 관리하는 방식을 비교합니다.
:::

:::topic-grid
## iOS 마이그레이션 및 호환성
- [Determining whether to bring your app to visionOS](https://developer.apple.com/documentation/visionos/determining-whether-to-bring-your-app-to-visionos): 기존 iPadOS 또는 iOS 앱을 visionOS로 가져올지 결정합니다.
- [Bringing your existing apps to visionOS](https://developer.apple.com/documentation/visionos/bringing-your-app-to-visionos): visionOS SDK를 사용해 iPadOS 또는 iOS 앱 버전을 빌드하고 플랫폼 차이에 맞게 코드를 업데이트합니다.
- [Bringing your ARKit app to visionOS](https://developer.apple.com/documentation/visionos/bringing-your-arkit-app-to-visionos): ARKit을 사용하는 iPadOS 또는 iOS 앱을 업데이트하고 visionOS에서 동등한 경험을 제공합니다.
- [Making your existing app compatible with visionOS](https://developer.apple.com/documentation/visionos/making-your-app-compatible-with-visionos): 기존 iPadOS 또는 iOS 앱이 visionOS에서 호환 앱으로 성공적으로 실행되도록 수정합니다.
:::

:::topic-grid
## visionOS용 엔터프라이즈 API
- [Accessing the main camera](https://developer.apple.com/documentation/visionos/accessing-the-main-camera): 엔터프라이즈 앱에 카메라 기반 기능을 추가합니다.
- [Building spatial experiences for business apps with enterprise APIs for visionOS](https://developer.apple.com/documentation/visionos/building-spatial-experiences-for-business-apps-with-enterprise-apis): entitlement를 사용해 visionOS 앱에 향상된 sensor 접근과 더 큰 플랫폼 제어 권한을 부여합니다.
- [Locating and decoding barcodes in 3D space](https://developer.apple.com/documentation/visionos/locating-and-decoding-barcodes-in-3d-space): 사용자의 주변 환경에 있는 바코드를 기반으로 매력적이고 hands-free인 경험을 만듭니다.
:::
