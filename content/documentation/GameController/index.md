---
route: /documentation/GameController
source_url: https://developer.apple.com/documentation/GameController
source_locale: en-US
section: docc
content_type: symbol
title: Game Controller
original_title: Game Controller
source_hash: 6a2e0bda5e2f6c8a8bf9d5c7d0f762d9641ab249057f480f7849250048f44b5a
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:28:18+00:00'
last_translated_at: '2026-03-13T23:28:34+09:00'
---

# Game Controller

게임에서 하드웨어 게임 컨트롤러를 지원합니다.

## 개요

Game Controller를 사용하면 실제 또는 가상 게임 컨트롤러로 앱과 상호 작용하는 사용자를 지원할 수 있습니다. 게임 컨트롤러에는 DualShock 4, DualSense, Xbox 같은 서드파티 제품뿐 아니라 마우스, 키보드, Siri Remote, 레이싱 휠도 포함됩니다.

![도로를 달리는 자동차가 시골 풍경 쪽으로 향하는 게임을 노트북에 표시한 그림입니다. 왼쪽에는 스티어링 휠 컨트롤러 오버레이가 있습니다.](https://developer.apple.com)

게임 컨트롤러를 지원하려면 프로젝트에 Game Controller capability([GCSupportsControllerUserInteraction](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportsControllerUserInteraction) 속성)를 추가하면 Xcode가 Game Controller 프레임워크를 자동으로 추가합니다. 그런 다음 Signing & Capabilities 패널의 Game Controllers capability 아래에서 앱이 지원하는 컨트롤러 유형([GCSupportedGameControllers](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportedGameControllers) 속성)을 선택하십시오.

레이싱 휠을 제외한 컨트롤러 입력을 앱에서 처리하려면 다음 단계를 따르십시오.

- 사용자가 게임 컨트롤러를 연결하거나 연결 해제할 때 특정 알림을 등록해 실제 게임 컨트롤러 객체를 가져옵니다. 또는 사용자가 상호 작용할 수 있는 가상 컨트롤러를 표시할 수도 있습니다.
- 그런 다음 실제 또는 가상 컨트롤러에서 profile 객체를 가져와 버튼, 트리거, thumbstick, 방향 패드 같은 입력 요소에 접근합니다. profile은 앱에서 보이는 컨트롤러 입력 요소의 하드웨어 세부 사항과 레이아웃을 캡슐화합니다.
- 입력을 처리하려면 요소에서 값을 직접 읽거나 사용자가 값을 바꿀 때 호출되는 callback을 등록합니다. visionOS에서 실행되는 앱은 사용자가 앱 창을 보고 있을 때만 입력 이벤트를 받습니다.
- 햅틱을 지원하는 컨트롤러의 경우, 컨트롤러 actuator를 조작하는 엔진을 만들어 사용자에게 피드백을 제공할 수 있습니다.

사용자는 설정과 환경설정에서 게임 컨트롤러 요소를 다시 매핑할 수 있으므로, 인터페이스에는 올바른 입력 요소를 표시해야 합니다. [hasRemappedElements](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/hasremappedelements) 속성이 [true](https://developer.apple.com/documentation/Swift/true)이면 사용자가 요소를 다시 매핑한 것이며, [mappedElementAlias(forPhysicalInputName:)](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/mappedelementalias(forphysicalinputname:)) 및 [mappedPhysicalInputNames(forElementAlias:)](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputprofile/mappedphysicalinputnames(forelementalias:)) 메서드를 사용해 실제 요소와 별칭 요소 사이의 매핑을 얻을 수 있습니다.

macOS 앱에서 레이싱 휠 기기를 지원하려면 [Racing wheel device support](https://developer.apple.com/documentation/gamecontroller/racing-wheel-device-support)를 참고하십시오.

:::topic-grid
## 핵심
- [Game Controller updates](https://developer.apple.com/documentation/Updates/GameController): Game Controller의 중요한 변경 사항을 살펴봅니다.
- [Discovering game controllers](https://developer.apple.com/documentation/gamecontroller/discovering-game-controllers): 플레이어에게 자연스러운 실제 컨트롤러 지원을 제공하기 위해 연결 및 입력 처리를 구현합니다.
- [Handling input events](https://developer.apple.com/documentation/gamecontroller/handling-input-events): polling 또는 callback을 사용해 컨트롤러 입력을 받습니다.
:::

:::topic-grid
## 구성
- [GCSupportsControllerUserInteraction](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportsControllerUserInteraction): 앱이 게임 컨트롤러를 지원하는지 나타내는 Boolean 값입니다.
- [GCSupportedGameControllers](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportedGameControllers): 앱이 지원하거나 필요로 하는 게임 컨트롤러 profile 유형입니다.
- [GCSupportsMultipleMicroGamepads](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportsMultipleMicroGamepads): 실제 Apple TV Remote와 Apple TV Remote 앱이 별도 게임 컨트롤러로 동작하는지 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 뷰 컨트롤러
- [GCEventViewController](https://developer.apple.com/documentation/gamecontroller/gceventviewcontroller): responder chain에서 view로, 또는 게임 컨트롤러에서 profile로 입력을 전달하는 view controller입니다.
:::

:::topic-grid
## 게임 컨트롤러
- [Supporting Game Controllers](https://developer.apple.com/documentation/gamecontroller/supporting-game-controllers): 햅틱, 조명, 모션 감지를 통해 실제 컨트롤러를 지원하거나 가상 컨트롤러를 추가해 게임 상호 작용을 향상합니다.
- [Letting players use their second-generation Siri Remote as a game controller](https://developer.apple.com/documentation/gamecontroller/letting-players-use-their-second-generation-siri-remote-as-a-game-controller): Apple TV 게임에서 2세대 Siri Remote를 게임 컨트롤러로 지원합니다.
- [Discovering and tracking spatial game controllers and styli](https://developer.apple.com/documentation/gamecontroller/discovering-and-tracking-spatial-game-controllers-and-styli): 증강 현실 앱 콘텐츠와 상호 작용하기 위한 컨트롤러 및 stylus 입력을 받습니다.
- [GCDevice](https://developer.apple.com/documentation/gamecontroller/gcdevice): 게임 입력 기기의 공통 인터페이스를 정의하는 protocol입니다.
- [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller): 실제 게임 컨트롤러, 가상 컨트롤러, 또는 컨트롤러 snapshot의 표현입니다.
- [GCRacingWheel](https://developer.apple.com/documentation/gamecontroller/gcracingwheel): 기기에 연결된 실제 레이싱 휠 컨트롤러를 나타내는 객체입니다.
- [GCKeyboard](https://developer.apple.com/documentation/gamecontroller/gckeyboard): 기기에 연결된 실제 키보드를 나타내는 객체입니다.
- [GCMouse](https://developer.apple.com/documentation/gamecontroller/gcmouse): 기기에 연결된 실제 마우스를 나타내는 객체입니다.
- [GCStylus](https://developer.apple.com/documentation/gamecontroller/gcstylus): 기기에 연결된 실제 stylus를 나타내는 객체입니다.
:::

:::topic-grid
## 게임 컨트롤러 프로필
- [Input](https://developer.apple.com/documentation/gamecontroller/input): 게임 또는 게임 엔진 흐름에 가장 잘 맞는 방식으로 컨트롤러 입력을 받습니다.
- [GCMotion](https://developer.apple.com/documentation/gamecontroller/gcmotion): 방향과 동작을 지원하는 컨트롤러 profile입니다.
- [GCDeviceBattery](https://developer.apple.com/documentation/gamecontroller/gcdevicebattery): 기기 배터리의 충전량과 상태입니다.
- [GCDeviceHaptics](https://developer.apple.com/documentation/gamecontroller/gcdevicehaptics): 게임 컨트롤러의 햅틱 actuator 위치입니다.
- [GCDeviceLight](https://developer.apple.com/documentation/gamecontroller/gcdevicelight): 기기의 색상 조명입니다.
:::

:::topic-grid
## 가상 컨트롤러
- [Adding virtual controls to games that support game controllers in iOS](https://developer.apple.com/documentation/gamecontroller/adding-virtual-controls-to-games-that-support-game-controllers-in-ios): 터치 입력과 가상 컨트롤러를 사용해 컨트롤러가 없는 플레이어도 게임을 이용할 수 있게 합니다.
- [GCVirtualController](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller): 게임에 맞게 특별히 구성하는 실제 컨트롤러의 소프트웨어 에뮬레이션입니다.
:::

:::topic-grid
## 버튼 요소와 이름
- [GCTouchedStateInput](https://developer.apple.com/documentation/gamecontroller/gctouchedstateinput): 터치 상태 입력을 가진 요소의 공통 속성입니다.
- [GCPressedStateInput](https://developer.apple.com/documentation/gamecontroller/gcpressedstateinput): 버튼 입력처럼 누름 상태 입력을 가진 요소의 공통 속성입니다.
:::

:::topic-grid
## 레이싱 휠
- [Racing wheel device support](https://developer.apple.com/documentation/gamecontroller/racing-wheel-device-support): macOS에서 레이싱 휠 기기 지원을 추가합니다.
:::

:::topic-grid
## IOKit에서 Game Controller 프레임워크로의 마이그레이션
- [Understanding game controller backward compatibility](https://developer.apple.com/documentation/gamecontroller/understanding-game-controller-backward-compatibility): Game Controller 프레임워크 도입 이전의 소프트웨어에 최신 게임 컨트롤러 지원을 macOS가 어떻게 제공하는지 알아봅니다.
- [kIOHIDGCSyntheticDeviceKey](https://developer.apple.com/documentation/gamecontroller/kiohidgcsyntheticdevicekey): 기기가 게임 컨트롤러 synthetic HID 기기인지 지정하는 키입니다.
:::

:::topic-grid
## 하위 호환 별칭
- [GCDeviceElement](https://developer.apple.com/documentation/gamecontroller/gcdeviceelement): 이전 SDK 버전과의 하위 호환성을 위한 심볼 이름 별칭입니다.
- [GCDeviceAxisInput](https://developer.apple.com/documentation/gamecontroller/gcdeviceaxisinput): 이전 SDK 버전과의 하위 호환성을 위한 심볼 이름 별칭입니다.
- [GCDeviceButtonInput](https://developer.apple.com/documentation/gamecontroller/gcdevicebuttoninput): 이전 SDK 버전과의 하위 호환성을 위한 심볼 이름 별칭입니다.
- [GCDeviceTouchpad](https://developer.apple.com/documentation/gamecontroller/gcdevicetouchpad): 이전 SDK 버전과의 하위 호환성을 위한 심볼 이름 별칭입니다.
- [GCDeviceDirectionPad](https://developer.apple.com/documentation/gamecontroller/gcdevicedirectionpad): 이전 SDK 버전과의 하위 호환성을 위한 심볼 이름 별칭입니다.
:::

:::topic-grid
## 지원 중단 심볼
- [Deprecated symbols](https://developer.apple.com/documentation/gamecontroller/deprecated-symbols)
:::

:::topic-grid
## 프로토콜
- [GCPhysicalInputExtents](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputextents): 물리적 extents는 정규화된 값을 물리 단위로 확장합니다.
:::
