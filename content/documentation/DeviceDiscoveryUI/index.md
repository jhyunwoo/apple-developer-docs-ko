---
route: /documentation/DeviceDiscoveryUI
source_url: https://developer.apple.com/documentation/DeviceDiscoveryUI
source_locale: en-US
section: docc
content_type: symbol
title: DeviceDiscoveryUI
original_title: DeviceDiscoveryUI
source_hash: 141ed3d2c3e45ebaa5b15eb42d23268757994d73c832d2dc75195637abcb3ceb
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:51:15+00:00'
last_translated_at: '2026-03-13T18:40:00+09:00'
---

# DeviceDiscoveryUI

사용자가 로컬 네트워크를 통해 tvOS 앱을 모바일 기기와 연결할 수 있는 인터페이스를 표시합니다.

## 개요

DeviceDiscoveryUI 프레임워크는 로컬 네트워크를 사용해 tvOS 앱과 iOS, iPadOS, 또는 watchOS 앱 사이에 암호화된 연결을 제공합니다. 예를 들어 사용자는 iPad로 tvOS 게임을 조작할 수 있습니다. 또는 피트니스 tvOS 앱이 watchOS 버전과 연결되어 운동 세션을 기록하고 심박수와 칼로리 데이터를 tvOS 앱으로 다시 전달할 수 있습니다.

Apple TV에서는 [DevicePicker](https://developer.apple.com/documentation/devicediscoveryui/devicepicker) view 또는 [DDDevicePickerViewController](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller)를 먼저 표시합니다. 이 view는 로컬 네트워크에서 tvOS 앱이 연결할 수 있는 모든 기기 목록을 보여 줍니다. 사용자가 기기를 선택하면 시스템이 해당 기기에서 앱을 실행하려고 시도합니다. 앱이 이미 설치되어 있으면 시스템이 사용자가 Apple TV에 연결할지 묻습니다. 앱이 설치되어 있지 않으면 시스템이 설치를 안내합니다.

DeviceDiscoveryUI를 사용해 사용 가능한 기기 목록을 보여 주는 view를 표시한 다음, [Network](https://developer.apple.com/documentation/Network) 프레임워크를 사용해 listener를 만들고, 연결을 생성하고, 메시지를 송수신합니다.

DeviceDiscoveryUI는 [Network](https://developer.apple.com/documentation/Network) 프레임워크를 직접 사용해 연결을 만드는 것보다 여러 가지 장점을 제공합니다. 이 프레임워크는 서로 다른 로컬 기기에서 실행 중인 앱 버전 사이에 최적화된 암호화 연결을 자동으로 설정합니다. 로컬 네트워크에 있는 iOS, iPadOS, watchOS 기기에만 접근을 제공하여 사용자의 개인 정보를 보호하는 데 도움을 줍니다. 또한 시스템이 연결을 안전하게 관리하므로 사용자가 로컬 네트워크 전체 접근을 승인할 필요가 없습니다.

다음 요구 사항이 적용됩니다.

- DeviceDiscoveryUI는 Apple TV 4K에서만 지원됩니다.
- tvOS 앱은 한 번에 하나의 기기에만 연결할 수 있습니다.
- tvOS 앱은 iOS, iPadOS, watchOS에서 실행 중인 앱 자신의 다른 복사본에만 연결할 수 있습니다.
- 앱은 universal purchase로 배포해야 하며, 앱의 모든 복사본이 같은 bundle ID를 공유해야 합니다. 자세한 내용은 [Offering Universal Purchase](https://developer.apple.com/support/universal-purchase/)를 참고하십시오.

DeviceDiscoveryUI는 Apple TV의 기본 사용자의 iCloud 계정을 사용합니다. Apple TV에 사용자가 둘 이상 있는 경우 Family Sharing을 관리하는 사용자가 기본 사용자입니다. DeviceDiscoveryUI는 그 사용자의 iCloud 계정에 로그인한 기기나, 해당 사용자의 Family Sharing 그룹 계정의 기기만 표시합니다.

:::topic-grid
## 주변 기기 선택
- [Connecting a tvOS app to other devices over the local network](https://developer.apple.com/documentation/devicediscoveryui/connecting-a-tvos-app-to-other-devices-over-the-local-network): 사용자가 자신의 로컬 네트워크를 통해 연결할 수 있는 iOS, iPadOS, watchOS 기기 목록을 tvOS 앱에 표시합니다.
- [DevicePicker](https://developer.apple.com/documentation/devicediscoveryui/devicepicker): 네트워크의 다른 기기를 표시하고, 그 기기에서 실행 중인 앱 복사본과 암호화된 연결을 생성하는 SwiftUI view입니다.
- [DDDevicePickerViewController](https://developer.apple.com/documentation/devicediscoveryui/dddevicepickerviewcontroller): 네트워크의 다른 기기를 표시하고, 그 기기에서 실행 중인 앱 복사본과 암호화된 연결을 생성하는 UIKit view입니다.
- [DevicePickerSupportedAction](https://developer.apple.com/documentation/devicediscoveryui/devicepickersupportedaction): 현재 기기가 기기 검색을 지원하는지 나타내는 환경 값입니다.
- [NSApplicationServices](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSApplicationServices): 서비스 제공업체와 그들이 지원하는 기기 목록입니다.
:::

:::topic-grid
## 클래스
- [DDDevicePairingViewController](https://developer.apple.com/documentation/devicediscoveryui/dddevicepairingviewcontroller)
:::

:::topic-grid
## 구조체
- [DDDevicePairingAccess](https://developer.apple.com/documentation/devicediscoveryui/dddevicepairingaccess): 기기 검색에 대해 요청하는 접근 수준을 지정합니다.
- [DevicePairingView](https://developer.apple.com/documentation/devicediscoveryui/devicepairingview): 사용자가 검색 가능 상태가 되어 로컬 기기에 자신을 광고할 수 있게 하는 컨트롤입니다.
:::
