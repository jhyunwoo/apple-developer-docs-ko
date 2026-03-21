---
route: /documentation/NetworkExtension
source_url: https://developer.apple.com/documentation/NetworkExtension
source_locale: en-US
section: docc
content_type: symbol
title: Network Extension
original_title: Network Extension
source_hash: d030d83e8e0db803306b8cb7f5663dae92485a5d715ad4c1d6cde72361dfbbbb
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:04:57+00:00'
last_translated_at: '2026-03-13T07:05:46+00:00'
---

# Network Extension

핵심 네트워킹 기능을 사용자화하고 확장합니다.

## 개요

NetworkExtension 프레임워크를 사용하면 시스템의 핵심 네트워킹 기능을 사용자화하고 확장할 수 있습니다. 구체적으로는 다음을 수행할 수 있습니다.

- 시스템의 Wi-Fi 구성을 변경합니다.
- 앱을 핫스팟 네트워크 하위 시스템(Hotspot Helper)과 통합합니다.
- 내장 VPN 프로토콜(Personal VPN) 또는 사용자 정의 VPN 프로토콜을 사용해 VPN 구성을 생성하고 관리합니다.
- 네트워크 릴레이 구성을 생성하고 관리합니다.
- 기기 내 콘텐츠 필터를 구현합니다.
- 내장 DNS 프로토콜 또는 사용자 정의 기기 내 DNS 프록시를 사용해 시스템 전반의 DNS 구성을 생성하고 관리합니다.

NetworkExtension 프레임워크는 macOS, iOS, tvOS, visionOS에서 사용할 수 있지만, 모든 기능이 모든 플랫폼에서 제공되는 것은 아니며 일부 기능에는 특정 제한이 있습니다. 예를 들어 일부 기능은 관리형 iOS 기기에서만 동작합니다. 각 기능의 문서에 이러한 제한 사항이 설명되어 있습니다.

### VPN 구현 옵션

NetworkExtension 프레임워크는 가상 사설망(VPN)을 폭넓게 지원합니다. VPN은 네트워크 터널의 한 형태로, VPN 클라이언트가 공용 인터넷을 사용해 VPN 서버에 연결한 뒤 그 연결을 통해 사설 네트워크 트래픽을 전달합니다.

VPN은 매우 다양한 용도로 사용됩니다. 예를 들어 기업은 원격 직원이 공용 인터넷에서는 접근할 수 없는 사내 네트워크 리소스에 접근할 수 있도록 VPN을 구성할 수 있습니다. 또는 공항의 무료 Wi-Fi처럼 신뢰할 수 없는 네트워크에서 인터넷에 접속하려는 일반 사용자가 자신의 트래픽을 보호하기 위해 VPN을 설정할 수도 있습니다.

지원되는 운영 체제에는 프로토콜 지원 방식에 따라 구분되는 여러 VPN API가 포함되어 있습니다.

- [Personal VPN](https://developer.apple.com/documentation/networkextension/personal-vpn)을 사용하면 내장 VPN 프로토콜(IPsec 또는 IKEv2)을 사용하는 VPN 구성을 생성하고 관리할 수 있습니다.
- [Packet tunnel provider](https://developer.apple.com/documentation/networkextension/packet-tunnel-provider)를 생성하면 패킷 지향 사용자 정의 VPN 프로토콜용 VPN 클라이언트를 구현할 수 있습니다.
- [App proxy provider](https://developer.apple.com/documentation/networkextension/app-proxy-provider)를 생성하면 흐름 지향 사용자 정의 VPN 프로토콜용 VPN 클라이언트를 구현할 수 있습니다.

### Always-on VPN 정보

iOS는 모든 IP 트래픽이 조직으로 다시 터널링되도록 보장하는 Always-on VPN을 지원합니다. Always-on VPN 구성 방법은 [iOS Deployment Reference](https://support.apple.com/guide/deployment-reference-ios/always-on-vpn-iore8b083096/1/web/1)를 참고하세요.

:::topic-grid
## Wi-Fi 관리
- [Wi-Fi 구성](https://developer.apple.com/documentation/networkextension/wi-fi-configuration): 지속적인 Wi-Fi 구성을 추가하거나, 기기를 특정 Wi-Fi 네트워크로 일시적으로 이동합니다.
- [Wi-Fi 액세서리가 네트워크에 참여하도록 구성하기](https://developer.apple.com/documentation/networkextension/configuring-a-wi-fi-accessory-to-join-a-network): 네트워크 구성 정보를 전달하기 위해 iOS 기기를 액세서리의 네트워크와 연결합니다.
- [Hotspot helper](https://developer.apple.com/documentation/networkextension/hotspot-helper): 앱을 iOS 핫스팟 네트워크 하위 시스템과 통합합니다.
:::

:::topic-grid
## 가상 사설망
- [VPN 네트워크 트래픽 라우팅하기](https://developer.apple.com/documentation/networkextension/routing-your-vpn-network-traffic): 일부 네트워크 트래픽을 포함하거나 제외하도록 VPN을 구성합니다.
- [Personal VPN](https://developer.apple.com/documentation/networkextension/personal-vpn): 내장 VPN 프로토콜(IPsec 또는 IKEv2)을 사용하는 VPN 구성을 생성하고 관리합니다.
- [Packet tunnel provider](https://developer.apple.com/documentation/networkextension/packet-tunnel-provider): 패킷 지향 사용자 정의 VPN 프로토콜용 VPN 클라이언트를 구현합니다.
- [App proxy provider](https://developer.apple.com/documentation/networkextension/app-proxy-provider): 흐름 지향 사용자 정의 VPN 프로토콜용 VPN 클라이언트를 구현합니다.
:::

:::topic-grid
## 네트워크 릴레이
- [Relays](https://developer.apple.com/documentation/networkextension/relays): HTTP/3 및 HTTP/2를 통한 TCP와 UDP 트래픽의 내장 프록시 기능을 사용하는 시스템 전반 네트워크 릴레이 구성을 생성하고 관리합니다.
:::

:::topic-grid
## 콘텐츠 필터
- [Content filter providers](https://developer.apple.com/documentation/networkextension/content-filter-providers): 기기 내 네트워크 콘텐츠 필터를 생성합니다.
- [네트워크 트래픽 필터링](https://developer.apple.com/documentation/networkextension/filtering-network-traffic): Network Extension 프레임워크를 사용해 네트워크 연결을 허용하거나 거부합니다.
:::

:::topic-grid
## URL 필터
- [URL filters](https://developer.apple.com/documentation/networkextension/url-filters): 개인정보를 보호하면서 전체 URL을 분석하는 필터를 생성합니다.
:::

:::topic-grid
## DNS 구성
- [DNS settings](https://developer.apple.com/documentation/networkextension/dns-settings): 내장 암호화 DNS 프로토콜을 사용하는 시스템 전반 DNS 구성을 생성하고 관리합니다.
- [DNS proxy provider](https://developer.apple.com/documentation/networkextension/dns-proxy-provider): 사용자 정의 프로토콜을 사용하는 기기 내 DNS 프록시를 생성합니다.
:::

:::topic-grid
## 로컬 네트워킹
- [Local push connectivity](https://developer.apple.com/documentation/networkextension/local-push-connectivity): 더 넓은 인터넷에 접근할 수 없을 때 Apple Push Notification Service와 유사한 기능을 제공합니다.
:::

:::topic-grid
## 앱 확장
- [NEAppExtensionConfiguration](https://developer.apple.com/documentation/networkextension/neappextensionconfiguration): NetworkExtension 앱 확장에서 사용할 구성 옵션을 정의하는 클래스입니다.
:::

:::topic-grid
## 프로토콜
- [NEAppProxyUDPFlowHandling](https://developer.apple.com/documentation/networkextension/neappproxyudpflowhandling)
:::

:::topic-grid
## 구조체
- [NETunnelProviderError](https://developer.apple.com/documentation/networkextension/netunnelprovidererror-swift.struct): 터널 제공자가 마주친 오류입니다.
- [NEVPNError](https://developer.apple.com/documentation/networkextension/nevpnerror-swift.struct): VPN을 구성하거나 사용하는 동안 발생한 오류에 대한 정보입니다.
:::

:::topic-grid
## 변수
- [NERelayClientErrorDomain](https://developer.apple.com/documentation/networkextension/nerelayclienterrordomain)
:::

:::topic-grid
## 열거형
- [NERelayManagerClientError](https://developer.apple.com/documentation/networkextension/nerelaymanagerclienterror)
:::
