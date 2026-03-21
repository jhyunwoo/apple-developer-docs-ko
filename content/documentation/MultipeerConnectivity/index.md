---
route: /documentation/MultipeerConnectivity
source_url: https://developer.apple.com/documentation/MultipeerConnectivity
source_locale: en-US
section: docc
content_type: symbol
title: Multipeer Connectivity
original_title: Multipeer Connectivity
source_hash: ccb2d3c861edb4719c5e4c773cf7b5b010723ac5c36760e62e029b35c5c2145e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:54:44+00:00'
last_translated_at: '2026-03-14T00:13:00+09:00'
---

# Multipeer Connectivity

피어 투 피어 연결과 주변 기기 검색을 지원합니다.

## 개요

Multipeer Connectivity 프레임워크는 주변 기기가 제공하는 서비스를 검색하고, 메시지 기반 데이터, 스트리밍 데이터, 리소스(예: 파일)를 통해 해당 서비스와 통신할 수 있게 해 줍니다. iOS에서는 인프라 Wi-Fi 네트워크, 피어 투 피어 Wi-Fi, Bluetooth 개인 영역 네트워크를 기반 전송 계층으로 사용합니다. macOS와 tvOS에서는 인프라 Wi-Fi, 피어 투 피어 Wi-Fi, Ethernet을 사용합니다.

:::important 중요
로컬 네트워크를 사용하는 앱은 `Info.plist`에 [NSLocalNetworkUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription) 키와 함께 사용 목적 문자열을 제공해야 합니다. Bonjour를 사용하는 앱은 [NSBonjourServices](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) 키를 사용해 탐색할 서비스를 함께 선언해야 합니다.
:::

### 아키텍처

Multipeer Connectivity 프레임워크를 사용할 때 앱은 여러 종류의 객체와 상호 작용해야 합니다.

- Session 객체([MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession))는 연결된 피어 기기 사이의 통신을 지원합니다. 앱은 피어가 연결 초대를 수락하면 session을 만들고 피어를 추가하며, 다른 피어로부터 연결 초대를 받았을 때도 session을 생성합니다. Session 객체는 session에 연결된 피어를 나타내는 peer ID 객체 집합을 유지합니다.
- Advertiser 객체([MCNearbyServiceAdvertiser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser))는 앱이 지정한 유형의 session에 참여할 의사가 있음을 주변 피어에게 알립니다. Advertiser 객체는 단일 로컬 peer 객체를 사용해 기기와 사용자 정보를 주변 다른 기기에 식별 정보로 제공합니다.
- Advertiser assistant 객체([MCAdvertiserAssistant](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant))는 advertiser 객체와 같은 기능을 제공하면서, 사용자가 초대를 수락할 수 있는 표준 사용자 인터페이스도 제공합니다. 자체 사용자 인터페이스를 제공하거나 표시할 초대를 프로그래밍 방식으로 더 세밀하게 제어하려면 advertiser 객체를 직접 사용하십시오.
- Browser 객체([MCNearbyServiceBrowser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser))는 앱이 특정 유형의 session을 지원하는 주변 기기를 프로그래밍 방식으로 검색하게 해 줍니다.
- Browser view controller 객체([MCBrowserViewController](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller))는 사용자가 session에 추가할 주변 피어를 선택할 수 있는 표준 사용자 인터페이스를 제공합니다.
- Peer ID([MCPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid))는 기기에서 실행 중인 앱을 주변 피어에게 고유하게 식별합니다.

### 검색 단계와 세션 단계

이 프레임워크는 검색 단계와 세션 단계, 두 단계로 사용합니다.

검색 단계에서 앱은 [MCNearbyServiceBrowser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser) 객체를 사용해 주변 피어를 탐색하며, 필요하면 [MCBrowserViewController](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller) 객체를 사용해 사용자 인터페이스를 표시합니다.

앱은 또한 [MCNearbyServiceAdvertiser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser) 객체나 [MCAdvertiserAssistant](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant) 객체를 사용해 자신이 사용 가능하다는 사실을 주변 피어에게 알립니다. 그러면 주변 다른 기기의 앱이 현재 앱을 session에 초대할 수 있습니다.

검색 단계 동안 앱은 다른 피어와 제한된 범위에서만 통신하고 그들에 대해 제한된 정보만 알 수 있습니다. 이 단계에서는 다른 주변 클라이언트가 제공하는 `discoveryInfo` 데이터와, session 참여 초대 시 다른 피어가 제공하는 context 데이터에 접근할 수 있습니다.

사용자가 session에 추가할 피어를 선택하면 앱은 해당 피어들을 session에 초대합니다. 주변 기기에서 실행 중인 앱은 이 초대를 수락하거나 거부할 수 있으며, 필요한 경우 사용자에게 허가를 요청할 수 있습니다.

피어가 초대를 수락하면 browser가 advertiser와 연결을 설정하고 세션 단계가 시작됩니다. 이 단계에서 앱은 session 안의 하나 이상의 피어와 직접 통신할 수 있습니다. 프레임워크는 delegate callback을 통해 피어가 session에 참여하거나 session을 떠날 때 앱에 알려 줍니다.

앱이 background로 이동하면 프레임워크는 advertising과 browsing을 중지하고 열려 있는 session을 모두 끊습니다. foreground로 돌아오면 프레임워크는 advertising과 browsing을 자동으로 다시 시작하지만, 닫힌 session은 개발자가 다시 설정해야 합니다.

:::topic-grid
## 클래스
- [MCAdvertiserAssistant](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant): advertising을 처리하고, 들어오는 초대를 사용자에게 표시하며, 사용자의 응답을 처리하는 편의 클래스입니다. 초대 처리에 대한 프로그래밍 제어가 필요하지 않을 때 사용자 인터페이스를 제공하려면 이 클래스를 사용합니다.
- [MCBrowserViewController](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller): 주변 기기를 사용자에게 표시하고, 사용자가 주변 기기를 session에 초대할 수 있게 하는 클래스입니다. iOS나 tvOS에서는 기반 view controller의 표시 및 해제 메서드를 사용하고, macOS에서는 이에 대응하는 메서드를 사용합니다.
- [MCNearbyServiceAdvertiser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser): Multipeer Connectivity 프레임워크를 통해 앱이 제공하는 특정 서비스에 대한 advertisement를 게시하고, 주변 피어의 초대에 대해 delegate에 알리는 클래스입니다.
- [MCNearbyServiceBrowser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser): 인프라 Wi-Fi, 피어 투 피어 Wi-Fi, Bluetooth(iOS) 또는 Ethernet(macOS 및 tvOS)을 사용해 주변 기기가 제공하는 서비스를 서비스 유형별로 검색하고, 해당 기기들을 Multipeer Connectivity session에 쉽게 초대할 수 있게 합니다.
- [MCPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid): 멀티피어 session의 피어를 나타내는 객체입니다.
- [MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession): Multipeer Connectivity session에 속한 모든 피어 간의 통신을 가능하게 하고 관리하는 객체입니다.
:::

:::topic-grid
## 프로토콜
- [MCAdvertiserAssistantDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate): 인스턴스의 delegate 객체가 advertising 관련 이벤트를 처리하기 위해 구현할 수 있는 메서드를 설명하는 프로토콜입니다.
- [MCBrowserViewControllerDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate): delegate 객체가 클래스와 관련된 이벤트를 처리하기 위해 구현할 수 있는 메서드를 정의하는 프로토콜입니다.
- [MCNearbyServiceAdvertiserDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate): 인스턴스의 delegate 객체가 클래스에서 전달되는 이벤트를 처리하기 위해 구현할 수 있는 메서드를 설명하는 프로토콜입니다.
- [MCNearbyServiceBrowserDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate): 객체의 delegate가 browser 관련 이벤트를 처리하기 위해 구현할 수 있는 메서드를 정의하는 프로토콜입니다.
- [MCSessionDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate): class의 delegate가 session 관련 이벤트를 처리하기 위해 구현할 수 있는 메서드를 정의하는 프로토콜입니다.
:::

:::topic-grid
## 구조체
- [MCError](https://developer.apple.com/documentation/multipeerconnectivity/mcerror)
:::

:::topic-grid
## 참고 자료
- [MultipeerConnectivity Enumerations](https://developer.apple.com/documentation/multipeerconnectivity/multipeerconnectivity_enumerations)
- [MultipeerConnectivity Constants](https://developer.apple.com/documentation/multipeerconnectivity/multipeerconnectivity_constants)
:::
