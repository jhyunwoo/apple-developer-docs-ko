---
route: /documentation/WiFiAware
source_url: https://developer.apple.com/documentation/WiFiAware
source_locale: en-US
section: docc
content_type: symbol
title: Wi-Fi Aware
original_title: Wi-Fi Aware
source_hash: aee28ce9b0e22fb3b2937fb51da4c91099d4df8851b210134261175492de17ed
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:21:29+00:00'
last_translated_at: '2026-03-14T01:05:00+09:00'
---

# Wi-Fi Aware

피어 투 피어 Wi-Fi를 통해 외부 장치와 안전하게 페어링하고 연결합니다.

## 개요

Wi-Fi Aware(TM)(Neighbor Awareness Networking 또는 NAN이라고도 함)는 인터넷 연결이나 액세스 포인트 없이도 주변 장치를 안전하게 발견하고, 페어링하고, 통신할 수 있게 하는 Wi-Fi Alliance(TM) 표준 규격입니다. 앱은 Wi-Fi Aware 프레임워크를 사용해 Wi-Fi Aware 인증 액세서리에 연결할 수 있습니다. 이 프레임워크는 Wi-Fi 장치 간 피어 투 피어(P2P) 연결을 설정하는 안전하고 표준화된 방법을 제공하며, 다음과 같은 네트워킹 기능을 제공합니다.

- 고대역폭, 저지연 데이터 전송
- Wi-Fi 계층에서 인증 및 암호화된 페어링 장치와의 연결
- 여러 Wi-Fi Aware 장치와의 동시 연결
- Wi-Fi Aware 장치와 Wi-Fi 인프라 네트워크의 동시 사용
- 다른 피어와의 연결을 끊지 않고도 피어가 자유롭게 드나들 수 있는 완전한 피어 투 피어 토폴로지

Wi-Fi Aware 기술은 Wi-Fi 인프라 네트워크, 셀룰러 링크, 인터넷 연결, 클라우드 서버 없이도 동작합니다. 앱은 [AccessorySetupKit](https://developer.apple.com/documentation/accessorysetupkit/) 또는 [DeviceDiscoveryUI](https://developer.apple.com/documentation/devicediscoveryui)로 Wi-Fi Aware 장치를 페어링할 수 있습니다. 페어링이 완료되면 앱은 Wi-Fi Aware 프레임워크와 [Network](https://developer.apple.com/documentation/Network) 프레임워크를 사용해 페어링된 장치 간에 필요 시 안전하고 인증되며 암호화된 피어 투 피어 연결을 만들 수 있습니다.

앱은 foreground와 background 상태 모두에서 실행 중인 동안 언제든지 페어링된 Wi-Fi Aware 장치에 연결할 수 있습니다. 앱은 [BackgroundTasks](https://developer.apple.com/documentation/backgroundtasks) API처럼 플랫폼의 기존 메커니즘을 사용해 런타임을 확보할 수 있습니다.

Wi-Fi Aware를 사용하는 하드웨어 장치나 액세서리를 빌드하는 경우, Apple 기기와 잘 동작하기 위한 요구 사항은 [Accessory Guide](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf)의 Wi-Fi Aware 장을 참고하십시오.

:::important 중요
다음 Apple 기기에서 Wi-Fi Aware 프레임워크를 지원합니다.

- iPhone 12 및 이후 모델
- iPad(10세대) 및 이후 모델
- iPad Air(4세대) 및 이후 모델
- iPad Pro 11형(3세대) 및 이후 모델
- iPad Pro 12.9형(5세대) 및 이후 모델
- iPad mini(6세대) 및 이후 모델
:::

:::topic-grid
## 핵심 사항
- [Building peer-to-peer apps](https://developer.apple.com/documentation/wifiaware/building-peer-to-peer-apps): Wi-Fi Aware를 사용해 안전하고 고처리량, 저지연 연결로 주변 장치와 통신합니다.
- [Connecting devices for peer-to-peer Wi-Fi](https://developer.apple.com/documentation/wifiaware/connecting-paired-devices): 페어링된 장치와 안전한 outgoing 연결을 만들고 incoming 연결을 수락합니다.
- [Adopting Wi-Fi Aware](https://developer.apple.com/documentation/wifiaware/adopting-wi-fi-aware): entitlement를 추가하고 앱의 서비스를 선언합니다.
- [com.apple.developer.wifi-aware](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.wifi-aware): 앱이 Wi-Fi Aware 프레임워크를 사용하기 위해 시스템이 요구하는 entitlement입니다.
- [WiFiAwareServices](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WiFiAwareServices): 앱이 publish하거나 subscribe할 수 있는 Wi-Fi Aware 서비스 dictionary입니다.
:::

:::topic-grid
## 호스트 기능
- [WACapabilities](https://developer.apple.com/documentation/wifiaware/wacapabilities): 호스트 기기의 지원 기능과 capability를 확인하는 구조체입니다.
- [WACapabilities.Feature](https://developer.apple.com/documentation/wifiaware/wacapabilities/feature): 앱의 현재 호스트 기기가 지원할 수 있는 기능입니다.
:::

:::topic-grid
## 검색할 서비스
- [WAService](https://developer.apple.com/documentation/wifiaware/waservice): 장치가 publish하거나 subscribe할 수 있는 서비스를 정의하는 프로토콜입니다.
- [WASubscribableService](https://developer.apple.com/documentation/wifiaware/wasubscribableservice): 앱이 원격 장치에서 발견하고 연결할 수 있는 서비스입니다.
- [WAPublishableService](https://developer.apple.com/documentation/wifiaware/wapublishableservice): 앱이 호스팅하며, 원격 장치가 연결할 수 있는 서비스입니다.
:::

:::topic-grid
## 페어링된 장치
- [WAPairedDevice](https://developer.apple.com/documentation/wifiaware/wapaireddevice): 앱이 연결할 수 있는 알려진 Wi-Fi Aware 장치입니다.
- [WAPairedDevice.Devices](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devices): 현재 페어링되어 있고 앱이 접근할 수 있으며 알고 있는 장치의 스냅샷을 담는 dictionary입니다.
- [WAPairedDevice.DevicesSequence](https://developer.apple.com/documentation/wifiaware/wapaireddevice/devicessequence): 장치 목록이 바뀔 때 paired device 목록의 업데이트를 제공하는 sequence입니다.
- [WAPairedDevice.PairingInfo](https://developer.apple.com/documentation/wifiaware/wapaireddevice/pairinginfo-swift.struct): 장치가 처음 페어링되기 전에 시스템이 수신하는 인증되지 않은 정보 모음입니다.
:::

:::topic-grid
## Subscriber
- [WASubscriberBrowser](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser): Wi-Fi Aware 서비스에 subscribe하고 페어링된 장치로 outgoing 연결을 만들도록 network browser를 구성하는 구조체입니다.
- [WASubscriberBrowser.Action](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/action): network browser가 수행할 Wi-Fi Aware subscriber 동작을 구성하는 구조체입니다.
- [WASubscriberBrowser.Devices](https://developer.apple.com/documentation/wifiaware/wasubscriberbrowser/devices): 연결할 장치를 결정하는 구조체입니다.
:::

:::topic-grid
## Publisher
- [WAPublisherListener](https://developer.apple.com/documentation/wifiaware/wapublisherlistener): Wi-Fi Aware를 통해 서비스를 publish하고, 페어링된 장치에서 들어오는 연결을 수락하도록 network listener를 구성합니다.
- [WAPublisherListener.Action](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/action): network listener가 수행할 Wi-Fi Aware publisher 동작을 구성하는 구조체입니다.
- [WAPublisherListener.Devices](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/devices): 연결할 장치를 결정하는 구조체입니다.
- [WAPublisherListener.DatapathParameters](https://developer.apple.com/documentation/wifiaware/wapublisherlistener/datapathparameters): 연결된 장치에 대해 초기 Wi-Fi Aware data path 구성을 설정하는 매개변수입니다.
:::

:::topic-grid
## 매개변수
- [NWParameters](https://developer.apple.com/documentation/Network/NWParameters): 연결에 사용할 프로토콜, 데이터 전송 옵션, 네트워크 경로 제약 조건을 저장하는 객체입니다.
- [NWParametersBuilder](https://developer.apple.com/documentation/Network/NWParametersBuilder): 매개변수화된 프로토콜 스택을 기반으로 `NWParameters`를 생성하고 구성하는 불투명 클래스입니다.
- [WAParameters](https://developer.apple.com/documentation/wifiaware/waparameters): Wi-Fi Aware data path 연결을 구성하는 매개변수입니다.
:::

:::topic-grid
## 연결
- [WAEndpoint](https://developer.apple.com/documentation/wifiaware/waendpoint): Wi-Fi Aware 연결의 endpoint입니다.
- [WAConnection](https://developer.apple.com/documentation/wifiaware/waconnection): 주어진 연결의 기반이 되는 Wi-Fi Aware 전용 구성과 정보에 접근할 수 있게 합니다.
:::

:::topic-grid
## 보안
- [WASharedSecret](https://developer.apple.com/documentation/wifiaware/washaredsecret): 이 네트워크 연결에 고유한 고엔트로피 shared secret입니다.
:::

:::topic-grid
## 연결 성능
- [NWPath](https://developer.apple.com/documentation/Network/NWPath): 연결이 사용하는 네트워크의 속성 또는 앱이 사용할 수 있는 속성 정보를 담는 객체입니다.
- [WAPath](https://developer.apple.com/documentation/wifiaware/wapath): 현재 Wi-Fi Aware 경로의 표현입니다.
- [WAPerformanceMode](https://developer.apple.com/documentation/wifiaware/waperformancemode): 어떤 성능 기준을 우선할지 나타내는 성능 모드입니다.
- [WAAccessCategory](https://developer.apple.com/documentation/wifiaware/waaccesscategory): Wi-Fi 계층이 연결의 데이터 패킷을 공중으로 전송할 때 사용하는 기반 품질 서비스(QoS)입니다.
- [WAPerformanceReport](https://developer.apple.com/documentation/wifiaware/waperformancereport): data path의 현재 성능 상태입니다.
:::

:::topic-grid
## 오류
- [NWError](https://developer.apple.com/documentation/Network/NWError): Network 프레임워크의 객체가 반환하는 오류입니다.
- [WAError](https://developer.apple.com/documentation/wifiaware/waerror): Wi-Fi Aware의 오류입니다.
:::

:::asset-list
- `https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf` -> `https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf` (pending)
:::
