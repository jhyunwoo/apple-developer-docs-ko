---
route: /documentation/NetworkingDriverKit
source_url: https://developer.apple.com/documentation/NetworkingDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: NetworkingDriverKit
original_title: NetworkingDriverKit
source_hash: 7cddd4a73c8ed53e6bb206c579e2120d67ee3fe41bd9c72e6114665f88918503
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:20:37+00:00'
last_translated_at: '2026-03-13T08:55:00+00:00'
---

# NetworkingDriverKit

Ethernet 네트워킹 기기용 드라이버를 개발합니다.

## 개요

NetworkingDriverKit를 사용하면 USB Ethernet 어댑터용 드라이버를 개발할 수 있습니다. 이 프레임워크는 [DriverKit](https://developer.apple.com/documentation/DriverKit)의 API를 확장하여 네트워킹 드라이버를 관리하는 서비스 클래스를 제공합니다. 또한 패킷을 저장하는 데 사용하는 메모리를 관리하고, 기기와 네트워킹 스택 사이에서 패킷을 전송하며, Ethernet 링크 상태를 검사하는 기능도 제공합니다.

현재 NetworkingDriverKit가 지원하는 네트워킹 인터페이스는 Ethernet뿐이라는 점에 유의하세요.

DriverKit와 NetworkingDriverKit로 드라이버를 개발하세요. 하드웨어 기기와의 연결은 USBDriverKit를 사용해 관리합니다. 드라이버를 macOS 앱 안에 포함시키고 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용해 사용자의 Mac에 드라이버를 설치하고 업그레이드합니다.

:::note Note
NetworkingDriverKit는 macOS에서 사용할 수 있습니다.
:::

:::topic-grid
## 필수 항목
- [com.apple.developer.driverkit.family.networking](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.networking): 드라이버를 네트워킹 프로토콜로 통신하는 기기와 매칭할지 나타내는 불리언 값입니다.
:::

:::topic-grid
## 샘플
- [네트워크 드라이버 연결하기](https://developer.apple.com/documentation/PCIDriverKit/connecting-a-network-driver): 시스템의 네트워크 프로토콜 스택과 인터페이스하는 Ethernet 드라이버를 생성합니다.
- [DriverKit 샘플 코드](https://developer.apple.com/documentation/DriverKit/driverkit-sample-code): DriverKit 프레임워크 계열로 macOS 기기 드라이버를 작성하는 방법을 보여 주는 프로젝트를 살펴봅니다.
:::

:::topic-grid
## 네트워크 서비스
- [IOUserNetworkEthernet](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet): 네트워킹 드라이버의 설정, 구성, 종료를 관리하는 데 사용하는 객체입니다.
:::

:::topic-grid
## 패킷 관리
- [IOUserNetworkPacketBufferPool](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketbufferpool): 드라이버로 들어오고 나가는 패킷의 저장 공간을 관리하는 객체입니다.
- [IOUserNetworkPacket](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacket): 드라이버가 처리할 데이터를 담고 있는 네트워크 패킷입니다.
- [IOUserNetworkPacketDirection](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketdirection): 기기를 기준으로 패킷이 이동하는 방향입니다.
:::

:::topic-grid
## 패킷 큐
- [IOUserNetworkRxSubmissionQueue](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxsubmissionqueue): 기기로부터 패킷을 받는 큐입니다.
- [IOUserNetworkRxCompletionQueue](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxcompletionqueue): 네트워킹 스택으로 성공적으로 전달한 패킷을 저장하는 데 사용하는 큐입니다.
- [IOUserNetworkTxSubmissionQueue](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueue): 네트워킹 스택으로부터 패킷을 받는 큐입니다.
- [IOUserNetworkTxCompletionQueue](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxcompletionqueue): 기기로 성공적으로 전달한 패킷을 저장하는 데 사용하는 큐입니다.
- [IOUserNetworkPacketQueue](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue): 기기와 주고받는 패킷을 관리하는 큐들의 기반 클래스입니다.
:::

:::topic-grid
## 참고 자료
- [NetworkingDriverKit Structures](https://developer.apple.com/documentation/networkingdriverkit/networkingdriverkit-structures)
- [NetworkingDriverKit Data Types](https://developer.apple.com/documentation/networkingdriverkit/networkingdriverkit-data-types)
- [NetworkingDriverKit Constants](https://developer.apple.com/documentation/networkingdriverkit/networkingdriverkit-constants)
:::

:::topic-grid
## 클래스
- [IOUserNetworkPacketPoller](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketpoller)
- [IOUserNetworkPacketQueueCompat](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueuecompat)
- [IOUserNetworkRxCompletionQueueCompat](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxcompletionqueuecompat)
- [IOUserNetworkRxSubmissionQueueCompat](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxsubmissionqueuecompat)
- [IOUserNetworkTxCompletionQueueCompat](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxcompletionqueuecompat)
- [IOUserNetworkTxSubmissionQueueCompat](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueuecompat)
:::

:::topic-grid
## 구조체
- [IOUserNetworkEthernet_IVars](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet_ivars)
- [IOUserNetworkPacketQueueCompat_IVars](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueuecompat_ivars)
- [IOUserNetworkRxCompletionQueueCompat_IVars](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxcompletionqueuecompat_ivars)
- [IOUserNetworkRxSubmissionQueueCompat_IVars](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkrxsubmissionqueuecompat_ivars)
- [IOUserNetworkTxCompletionQueueCompat_IVars](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxcompletionqueuecompat_ivars)
- [IOUserNetworkTxSubmissionQueueCompat_IVars](https://developer.apple.com/documentation/networkingdriverkit/iousernetworktxsubmissionqueuecompat_ivars)
:::

:::topic-grid
## 매크로
- [NDK_25](https://developer.apple.com/documentation/networkingdriverkit/ndk_25)
:::

:::topic-grid
## 열거형 케이스
- [kIOUserNetworkHWAssistLRONumSeg](https://developer.apple.com/documentation/networkingdriverkit/kiousernetworkhwassistlronumseg)
:::

:::topic-grid
## 타입 별칭
- [DequeueActionCompat](https://developer.apple.com/documentation/networkingdriverkit/dequeueactioncompat)
- [EnqueueActionCompat](https://developer.apple.com/documentation/networkingdriverkit/enqueueactioncompat)
- [IOUserNetworkPacketQueueCompatId](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueuecompatid)
- [QueryFreeSpaceActionCompat](https://developer.apple.com/documentation/networkingdriverkit/queryfreespaceactioncompat)
:::
