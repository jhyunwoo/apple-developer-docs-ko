---
route: /documentation/WatchKit
source_url: https://developer.apple.com/documentation/WatchKit
source_locale: en-US
section: docc
content_type: symbol
title: WatchKit
original_title: WatchKit
source_hash: dd1754024a6967a969daf8583d4538e5dfc8c47a325d5b22bca2548a5f283663
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:15:08+00:00'
last_translated_at: '2026-03-14T00:54:00+09:00'
---

# WatchKit

백그라운드 작업과 extended runtime session처럼 앱 delegate가 모니터링하거나 제어하는 기능을 사용하는 watchOS 앱을 빌드합니다.

## 개요

WatchKit 프레임워크는 background task, extended runtime session, Siri intent를 관리하는 extension delegate를 포함해 watchOS 앱 생성에 필요한 기반 구조를 제공합니다. 이 프레임워크는 또한 사용자의 Apple Watch에 대한 정보 접근처럼 다른 지원 작업도 수행합니다.

![설계도를 보여 주는 일러스트입니다. 중앙에는 기어가 들어 있는 Apple Watch 도면이 있고, 시계 양옆에는 아이콘 스케치가 있습니다.](https://developer.apple.com)

WatchKit을 사용하면 storyboard에서 앱의 사용자 인터페이스를 설계하고, UI 요소를 interface controller에 연결할 수도 있습니다.

:::note 참고
SwiftUI로 앱을 빌드하면 storyboard에서 설계하는 것보다 사용자 인터페이스를 더 세밀하게 제어할 수 있습니다. 새로운 watchOS 앱을 만들 때는 [SwiftUI](https://developer.apple.com/documentation/SwiftUI) 사용을 강력히 고려하십시오. 자세한 내용은 [Building a watchOS app](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app)을 참고하십시오.
:::

watchOS 앱을 빌드하는 방법에 대한 자세한 내용은 [watchOS apps](https://developer.apple.com/documentation/watchOS-Apps)를 참고하십시오.

:::topic-grid
## 앱 구조
- [Setting up a watchOS project](https://developer.apple.com/documentation/watchOS-Apps/setting-up-a-watchos-project): 새로운 watchOS 프로젝트를 만들거나 기존 iOS 프로젝트에 watch target을 추가합니다.
- [WKApplication](https://developer.apple.com/documentation/watchkit/wkapplication): 단일 watchOS 앱 target을 가진 앱을 위한 중앙 제어 및 조정 지점입니다.
- [WKApplicationDelegate](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate): 단일 target watchOS 앱의 앱 수준 동작을 관리하는 메서드 모음입니다.
- [WKExtension](https://developer.apple.com/documentation/watchkit/wkextension): watchOS에서 실행되는 extension 기반 앱을 위한 중앙 제어 및 조정 지점입니다.
- [WKExtensionDelegate](https://developer.apple.com/documentation/watchkit/wkextensiondelegate): WatchKit extension의 앱 수준 동작을 관리하는 메서드 모음입니다.
- [WKApplicationMain(_:_:_:)](https://developer.apple.com/documentation/watchkit/wkapplicationmain(_:_:_:)): application 객체와 application delegate를 생성하고 앱의 이벤트 사이클을 설정합니다.
- [WKInterfaceDevice](https://developer.apple.com/documentation/watchkit/wkinterfacedevice): 사용자의 Apple Watch에 대한 정보를 제공하는 객체입니다.
- [WKPrefersNetworkUponForeground](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKPrefersNetworkUponForeground): 앱이 실행 시 네트워크 접근을 필요로 하는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 런타임 관리
- [Background execution](https://developer.apple.com/documentation/watchkit/background-execution): background session과 task를 관리합니다.
- [Life cycles](https://developer.apple.com/documentation/watchkit/life-cycles): life-cycle 알림을 수신하고 이에 대응합니다.
- [Using extended runtime sessions](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions): 사용자가 상호 작용을 멈춘 뒤에도 앱을 계속 실행하는 extended runtime session을 생성합니다.
- [WKExtendedRuntimeSession](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession): 사용자가 상호 작용을 멈춘 뒤에도 앱을 계속 실행하는 session입니다.
- [Interacting with Bluetooth peripherals during background app refresh](https://developer.apple.com/documentation/watchkit/interacting-with-bluetooth-peripherals-during-background-app-refresh): 앱이 background에서 실행되는 동안 Bluetooth 주변 기기에서 값을 읽어 complication을 최신 상태로 유지합니다.
:::

:::topic-grid
## 사용자 인터페이스
- [Storyboard support](https://developer.apple.com/documentation/watchkit/storyboard-support): interface controller, interface object, event handler를 사용해 코드를 storyboard 요소에 연결합니다.
- [NowPlayingView](https://developer.apple.com/documentation/watchkit/nowplayingview): 사용자가 오디오를 제어할 수 있도록 시스템의 Now Playing 인터페이스를 표시하는 view입니다.
:::

:::topic-grid
## 오류
- [WatchKitError](https://developer.apple.com/documentation/watchkit/watchkiterror): WatchKit이 보고하는 오류입니다.
:::
