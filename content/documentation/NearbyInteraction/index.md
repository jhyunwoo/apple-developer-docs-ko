---
route: /documentation/NearbyInteraction
source_url: https://developer.apple.com/documentation/NearbyInteraction
source_locale: en-US
section: docc
content_type: symbol
title: Nearby Interaction
original_title: Nearby Interaction
source_hash: 003f9a76ee4d0070eafcff7b3bc3de332f83c95e062eb696563bfcd5b52e5a29
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:22:16+00:00'
last_translated_at: '2026-03-13T18:55:00+09:00'
---

# Nearby Interaction

식별자, 거리, 방향을 사용해 근처 기기를 찾고 상호 작용합니다.

## 개요

앱에서 Nearby Interaction을 사용하면 iPhone 11 이상, Apple Watch, 서드파티 액세서리처럼 Ultra Wideband(UWB) 칩을 탑재한 기기의 위치를 얻을 수 있습니다. 상호 작용에 참여하려면 물리적으로 가까이 있는 기기들이 앱을 실행하고, 서로를 고유하게 식별하는 위치 및 기기 토큰을 공유합니다. 앱이 포그라운드에서 실행 중이면 Nearby Interaction은 상대 기기의 방향과 미터 단위 거리를 보고하여 상호 작용 세션에 상대의 위치를 알려 줍니다.

Apple 기기는 UWB 칩의 고주파 기능을 사용해 실제 환경에서 자신의 위치를 공유하고 유연한 대화형 세션을 가능하게 합니다. 예를 들면 다음과 같습니다.

- 참가자들의 손에 가상의 물풍선을 배치하는 다중 사용자 AR 경험
- 상대 사용자의 방향을 실시간으로 활용해 운전자와 고객의 상대 위치를 파악하는 택시 또는 라이드셰어 앱
- 아래 그림처럼 사용자가 자신의 기기로 패들을 조작하고, 상대 사용자 화면에서 움직이는 공에 반응할 수 있게 하는 게임 앱

![각자 iPhone을 들고 있는 두 손의 일러스트입니다. 사용자들의 실제 움직임을 나타내는 화살표가 휴대폰에서 뻗어 나옵니다. 화면에는 공과 패들 게임이 표시되며, 첫 번째 사용자의 움직임은 아래쪽 패들을 좌우로 움직이고, 상대의 움직임은 위쪽 패들을 좌우로 움직입니다. 화면 중앙에서는 움직임 선이 있는 공이 첫 번째 사용자의 패들에 맞고 화면 오른쪽 위 모서리 쪽으로 향하는 모습이 보이는데, 그 구역은 상대 패들이 막고 있지 않습니다.](https://developer.apple.com)

Nearby Interaction 설계 지침은 [Human Interface Guidelines > Nearby interactions](https://developer.apple.com/design/human-interface-guidelines/nearby-interactions)를 참고하십시오.

### Apple Watch와 상호 작용하기

watchOS 8이 실행되는 UWB 칩 지원 Apple Watch는 Nearby Interaction 세션을 지원합니다. 앱은 사용자 정의 서버, [Core Bluetooth](https://developer.apple.com/documentation/CoreBluetooth), LAN(TCP/UDP), 또는 [Watch Connectivity](https://developer.apple.com/documentation/WatchConnectivity)를 사용해 discovery token을 공유하여 watchOS에서 상호 작용 세션을 시작합니다.

iOS의 Nearby Interaction은 상대 기기의 거리와 방향을 제공하는 반면, watchOS의 Nearby Interaction은 상대 기기의 거리만 제공합니다.

### 서드파티 기기와 상호 작용하기

iOS 15 이상과 watchOS 8 이상에서는 UWB 지원 기기가 [Nearby Interaction Accessory Protocol Specification](https://developer.apple.com/nearby-interaction/specification)을 사용해 직접 개발했거나 협력하여 만든 서드파티 액세서리와 상호 작용할 수 있습니다. 서드파티 액세서리와 상호 작용 세션을 시작하려면 액세서리와 데이터 링크를 설정하고, 해당 구성 데이터를 수신한 뒤, [NINearbyAccessoryConfiguration](https://developer.apple.com/documentation/nearbyinteraction/ninearbyaccessoryconfiguration)을 생성하십시오. 프레임워크는 [session(_:didGenerateShareableConfigurationData:for:)](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate/session(_:didgenerateshareableconfigurationdata:for:))를 통해 기기의 구성 데이터를 제공하며, 앱은 이 데이터를 액세서리에 보내 액세서리의 범위 감지를 시작합니다. 액세서리 상호 작용에 대한 자세한 내용은 [NINearbyAccessoryConfiguration](https://developer.apple.com/documentation/nearbyinteraction/ninearbyaccessoryconfiguration)을 참고하십시오.

:::note 참고
[supportsPreciseDistanceMeasurement](https://developer.apple.com/documentation/nearbyinteraction/nidevicecapability/supportsprecisedistancemeasurement) 함수는 Mac Catalyst로 빌드한 Mac 앱에서 [false](https://developer.apple.com/documentation/Swift/false)를 반환합니다. visionOS에서 실행되는 호환 iPad 또는 iPhone 앱에서는 프레임워크 기능을 사용할 수 없으며, 프레임워크 API를 호출해도 아무런 효과가 없습니다.
:::

### 백그라운드에서 Nearby Interaction 사용하기

앱이 포그라운드에 있을 때는 UWB 기기들 사이의 ranging에 Nearby Interaction을 자유롭게 사용할 수 있습니다. 앱이 백그라운드로 이동하면 Bluetooth Low Energy(LE)로 페어링되고 연결된 기기하고만 UWB ranging을 수행할 수 있습니다.

iOS 18.4 이상에서는 앱이 백그라운드로 이동할 때 Live Activity를 시작하면, 앱이 지원되는 어떤 기기와도 백그라운드에서 ranging을 계속할 수 있습니다. Live Activity 생성에 대한 자세한 내용은 [ActivityKit](https://developer.apple.com/documentation/ActivityKit)을 참고하십시오.

:::note 참고
이 두 가지 백그라운드 활동 형태 모두 Xcode에서 적절한 capability를 활성화해야 합니다. 대상의 Signing & Capabilities 탭에서 "Background Modes" capability를 추가한 다음, "Uses Nearby Interaction"을 선택하십시오.
:::

:::topic-grid
## 설정
- [Initiating and maintaining a session](https://developer.apple.com/documentation/nearbyinteraction/initiating-and-maintaining-a-session): 근처 기기의 상대 위치를 측정하고 사용자가 상호 작용을 지속할 수 있도록 안내합니다.
- [NISession](https://developer.apple.com/documentation/nearbyinteraction/nisession): 두 상대 기기 사이의 고유한 연결을 식별하는 객체입니다.
:::

:::topic-grid
## 권한 부여
- [NSNearbyInteractionUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSNearbyInteractionUsageDescription): 근처 기기와 상호 작용 세션을 시작하기 위한 사용자 권한 요청입니다.
:::

:::topic-grid
## 전화기 상호 작용
- [Implementing interactions between users in close proximity](https://developer.apple.com/documentation/nearbyinteraction/implementing-interactions-between-users-in-close-proximity): 기기가 상대 위치 정보에 접근할 수 있도록 합니다.
- [Discovering peers with Multipeer Connectivity](https://developer.apple.com/documentation/nearbyinteraction/discovering-peers-with-multipeer-connectivity): 로컬 네트워크를 통해 discovery token을 교환합니다.
- [Extending advanced direction finding and ranging](https://developer.apple.com/documentation/nearbyinteraction/extending-advanced-direction-finding-and-ranging): Ultra Wideband 기기의 데이터를 사용해 앱의 방향 탐지 기능을 확장합니다.
- [NINearbyPeerConfiguration](https://developer.apple.com/documentation/nearbyinteraction/ninearbypeerconfiguration): iPhone 또는 Apple Watch 기기 간 상호 작용을 가능하게 하는 구성입니다.
:::

:::topic-grid
## Watch 상호 작용
- [Implementing proximity-based interactions between a phone and watch](https://developer.apple.com/documentation/nearbyinteraction/implementing-proximity-based-interactions-between-a-phone-and-watch): 페어링된 iPhone까지의 거리를 측정해 근처 Apple Watch와 상호 작용합니다.
:::

:::topic-grid
## 서드파티 액세서리
- [Implementing spatial interactions with third-party accessories](https://developer.apple.com/documentation/nearbyinteraction/implementing-spatial-interactions-with-third-party-accessories): 근처 액세서리와 연결을 설정해 사용자와의 거리 측정값을 주기적으로 수신합니다.
- [NINearbyAccessoryConfiguration](https://developer.apple.com/documentation/nearbyinteraction/ninearbyaccessoryconfiguration): iPhone과 서드파티 액세서리 간 상호 작용을 가능하게 하는 구성입니다.
:::

:::topic-grid
## 주기적 업데이트
- [NINearbyObject](https://developer.apple.com/documentation/nearbyinteraction/ninearbyobject): 상호 작용 세션에서 상대 기기의 위치 정보입니다.
- [NISessionDelegate](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate): 세션 업데이트를 모니터링하고 반응하는 객체입니다.
:::

:::topic-grid
## 카메라 지원
- [Finding devices with precision](https://developer.apple.com/documentation/nearbyinteraction/finding-devices-with-precision): 앱에서 ARKit과 Apple Ultra Wideband Chip의 공간 인식을 활용해 사용자를 근처 기기로 안내합니다.
- [NIAlgorithmConvergence](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergence): 사용자 코칭 권장 사항의 상태와 이유를 제공하는 객체입니다.
- [NIAlgorithmConvergenceStatus](https://developer.apple.com/documentation/nearbyinteraction/nialgorithmconvergencestatus-2fnve): Camera Assistance의 가능한 상태입니다.
- [Algorithm Convergence Status](https://developer.apple.com/documentation/nearbyinteraction/algorithm-convergence-status): Camera Assistance의 가능한 Objective-C 상태입니다.
:::

:::topic-grid
## DL-TDoA ranging
- [Downlink time difference of arrival ranging](https://developer.apple.com/documentation/nearbyinteraction/dl-tdoa-ranging): anchor 기기를 사용해 실내 위치 추적의 정확도를 향상합니다.
:::

:::topic-grid
## 오류
- [NIError](https://developer.apple.com/documentation/nearbyinteraction/nierror): Nearby Interaction이 보고하는 오류입니다.
- [NIError.Code](https://developer.apple.com/documentation/nearbyinteraction/nierror/code): Nearby Interaction의 오류를 식별하는 코드입니다.
- [NIErrorDomain](https://developer.apple.com/documentation/nearbyinteraction/nierrordomain): Nearby Interaction을 위한 고유한 오류 도메인입니다.
:::

:::topic-grid
## 지원 중단됨
- [NSNearbyInteractionAllowOnceUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSNearbyInteractionAllowOnceUsageDescription): 근처 기기와 상호 작용 세션을 시작하기 위한 일회성 사용자 권한 요청입니다.
:::
