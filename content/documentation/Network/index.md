---
route: /documentation/Network
source_url: https://developer.apple.com/documentation/Network
source_locale: en-US
section: docc
content_type: symbol
title: Network
original_title: Network
source_hash: d2c33979eaeddb001c57c8b55ea047ddf744d1e74ee0e0f6c14c340208529ef2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:27:46+00:00'
last_translated_at: '2026-03-13T23:24:00+09:00'
---

# Network

전송 및 보안 프로토콜을 사용해 데이터를 보내고 받기 위한 네트워크 연결을 생성합니다.

## 개요

사용자 정의 애플리케이션 프로토콜을 위해 TLS, TCP, UDP 같은 프로토콜에 직접 접근해야 할 때 이 프레임워크를 사용합니다. HTTP 및 URL 기반 리소스를 로드할 때는 이 프레임워크 위에 구축된 [URLSession](https://developer.apple.com/documentation/Foundation/URLSession)을 계속 사용합니다. 네트워킹을 어디서 시작해야 할지에 대한 심층적인 조언은 [TN3151: Choosing the right networking API](https://developer.apple.com/documentation/Technotes/tn3151-choosing-the-right-networking-api)를 참고합니다.

:::note Note
watchOS는 특정 사용 사례에서 Network 프레임워크를 지원합니다. 자세한 내용은 [TN3135: Low-level networking on watchOS](https://developer.apple.com/documentation/Technotes/tn3135-low-level-networking-on-watchOS)를 참고합니다.
:::

:::topic-grid
## 핵심 항목
- [NWEndpoint](https://developer.apple.com/documentation/network/nwendpoint): 네트워크 연결의 로컬 또는 원격 엔드포인트입니다.
- [NWParameters](https://developer.apple.com/documentation/network/nwparameters): 연결에 사용할 프로토콜, 데이터 전송 옵션, 네트워크 경로 제약 조건을 저장하는 객체입니다.
:::

:::topic-grid
## 연결 및 리스너
- [NWConnection](https://developer.apple.com/documentation/network/nwconnection): 로컬 엔드포인트와 원격 엔드포인트 사이의 양방향 데이터 연결입니다.
- [NWListener](https://developer.apple.com/documentation/network/nwlistener): 들어오는 네트워크 연결을 수신할 때 사용하는 객체입니다.
- [NWBrowser](https://developer.apple.com/documentation/network/nwbrowser): 사용 가능한 네트워크 서비스를 탐색할 때 사용하는 객체입니다.
- [NWConnectionGroup](https://developer.apple.com/documentation/network/nwconnectiongroup): 로컬 네트워크의 IP multicast group 같은 엔드포인트 그룹과 통신할 때 사용하는 객체입니다.
- [NWEthernetChannel](https://developer.apple.com/documentation/network/nwethernetchannel): 사용자 정의 Ethernet frame을 송수신할 때 사용하는 객체입니다.
:::

:::topic-grid
## 네트워크 프로토콜
- [Building a custom peer-to-peer protocol](https://developer.apple.com/documentation/network/building-a-custom-peer-to-peer-protocol): 네트워킹 프레임워크를 사용해 iOS, iPadOS, watchOS, tvOS 기기 간 게임을 위한 사용자 정의 프로토콜을 만듭니다.
- [Connecting iPadOS and visionOS apps over the local network](https://developer.apple.com/documentation/visionOS/connecting-ipados-and-visionos-apps-over-the-local-network): visionOS 앱을 제어하기 위한 iPadOS companion app을 빌드합니다.
- [NWProtocolTCP](https://developer.apple.com/documentation/network/nwprotocoltcp): Transmission Control Protocol을 사용하는 연결용 네트워크 프로토콜입니다.
- [NWProtocolTLS](https://developer.apple.com/documentation/network/nwprotocoltls): Transport Layer Security를 사용하는 연결용 네트워크 프로토콜입니다.
- [NWProtocolQUIC](https://developer.apple.com/documentation/network/nwprotocolquic): QUIC transport protocol을 사용하는 연결용 네트워크 프로토콜입니다.
- [NWProtocolUDP](https://developer.apple.com/documentation/network/nwprotocoludp): User Datagram Protocol을 사용하는 연결용 네트워크 프로토콜입니다.
- [NWProtocolIP](https://developer.apple.com/documentation/network/nwprotocolip): 연결에서 Internet Protocol을 구성하기 위한 네트워크 프로토콜입니다.
- [NWProtocolWebSocket](https://developer.apple.com/documentation/network/nwprotocolwebsocket): WebSocket을 사용하는 연결용 네트워크 프로토콜입니다.
- [NWProtocolFramer](https://developer.apple.com/documentation/network/nwprotocolframer): 애플리케이션 메시지 파서를 정의하기 위한 사용자화 가능한 네트워크 프로토콜입니다.
:::

:::topic-grid
## 네트워크 보안 및 개인 정보 보호
- [Security Options](https://developer.apple.com/documentation/network/security-options): TLS 핸드셰이크용 보안 옵션을 구성합니다.
- [Privacy Management](https://developer.apple.com/documentation/network/privacy-management): 사용자 개인 정보와 관련된 매개변수를 구성합니다.
- [Creating an Identity for Local Network TLS](https://developer.apple.com/documentation/network/creating-an-identity-for-local-network-tls): 애플리케이션에서 로컬 네트워크 TLS를 위한 디지털 신원을 생성하고 사용하는 방법을 알아봅니다.
:::

:::topic-grid
## 경로 및 인터페이스
- [NWPath](https://developer.apple.com/documentation/network/nwpath): 연결이 사용하는 네트워크 또는 앱에서 사용할 수 있는 네트워크의 속성 정보를 담는 객체입니다.
- [NWPathMonitor](https://developer.apple.com/documentation/network/nwpathmonitor): 네트워크 변화를 모니터링하고 반응할 때 사용하는 observer입니다.
- [NWInterface](https://developer.apple.com/documentation/network/nwinterface): 네트워크 연결이 데이터를 송수신하는 데 사용하는 인터페이스입니다.
:::

:::topic-grid
## 오류
- [NWError](https://developer.apple.com/documentation/network/nwerror): Network 프레임워크 객체가 반환하는 오류입니다.
:::

:::topic-grid
## 네트워크 디버깅
- [Choosing a Network Debugging Tool](https://developer.apple.com/documentation/network/choosing-a-network-debugging-tool): 네트워크 디버깅 문제에 가장 적합한 도구를 결정합니다.
- [Debugging HTTP Server-Side Errors](https://developer.apple.com/documentation/network/debugging-http-server-side-errors): HTTP 서버 측 오류와 이를 디버깅하는 방법을 이해합니다.
- [Debugging HTTPS Problems with CFNetwork Diagnostic Logging](https://developer.apple.com/documentation/network/debugging-https-problems-with-cfnetwork-diagnostic-logging): CFNetwork diagnostic logging을 사용해 HTTP 및 HTTPS 문제를 조사합니다.
- [Recording a Packet Trace](https://developer.apple.com/documentation/network/recording-a-packet-trace): 네트워크 트래픽의 저수준 추적을 기록하는 방법을 알아봅니다.
- [Taking Advantage of Third-Party Network Debugging Tools](https://developer.apple.com/documentation/network/taking-advantage-of-third-party-network-debugging-tools): 사용 가능한 서드파티 네트워크 디버깅 도구를 알아봅니다.
- [Testing and Debugging L4S in Your App](https://developer.apple.com/documentation/network/testing-and-debugging-l4s-in-your-app): 앱의 응답성을 개선하기 위해 L4S를 지원하는 호스트와 네트워크에서 앱을 검증하는 방법을 알아봅니다.
:::

:::topic-grid
## C 언어 심볼
- [C-Language Symbols](https://developer.apple.com/documentation/network/c-language-symbols)
:::

:::topic-grid
## 구조체
- [nw_interface_radio_type_t](https://developer.apple.com/documentation/network/nw_interface_radio_type_t)
- [nw_multipath_version_t](https://developer.apple.com/documentation/network/nw_multipath_version_t)
- [nw_path_unsatisfied_reason_t](https://developer.apple.com/documentation/network/nw_path_unsatisfied_reason_t)
- [nw_quic_stream_type_t](https://developer.apple.com/documentation/network/nw_quic_stream_type_t)
- [Bonjour](https://developer.apple.com/documentation/network/bonjour): Bonjour 서비스를 발견하는 browser입니다.
- [BonjourListenerProvider](https://developer.apple.com/documentation/network/bonjourlistenerprovider): Bonjour 서비스를 광고합니다.
- [Coder](https://developer.apple.com/documentation/network/coder): Codable 타입을 framing하고 인코딩/디코딩하는 프로토콜입니다.
- [DefaultProtocolStorage](https://developer.apple.com/documentation/network/defaultprotocolstorage)
- [Framer](https://developer.apple.com/documentation/network/framer): 프로토콜 스택에 로드할 Framer 프로토콜의 인스턴스입니다.
- [IP](https://developer.apple.com/documentation/network/ip): Internet Protocol(IP)의 시스템 정의입니다.
- [NWParametersBuilder](https://developer.apple.com/documentation/network/nwparametersbuilder): 매개변수화된 프로토콜 스택을 기반으로 NWParameters를 생성하고 구성하는 역할을 하는 불투명 클래스입니다.
- [NWTXTRecord](https://developer.apple.com/documentation/network/nwtxtrecord): DNS packet의 TXT record를 나타내는 dictionary입니다.
- [NetworkJSONCoder](https://developer.apple.com/documentation/network/networkjsoncoder)
- [NetworkPropertyListCoder](https://developer.apple.com/documentation/network/networkpropertylistcoder)
- [ProtocolMetadataBuilder](https://developer.apple.com/documentation/network/protocolmetadatabuilder): 선언적인 방식으로 send method의 metadata를 구성하기 위한 resultBuilder입니다.
- [ProtocolStackBuilder](https://developer.apple.com/documentation/network/protocolstackbuilder): 선언적인 방식으로 프로토콜 스택을 지정하고 구성하기 위한 resultBuilder입니다.
- [ProxyConfiguration](https://developer.apple.com/documentation/network/proxyconfiguration): Relay, Oblivious HTTP, HTTP CONNECT, SOCKSv5용 proxy 구성입니다.
- [QUIC](https://developer.apple.com/documentation/network/quic): QUIC 프로토콜의 시스템 정의입니다.
- [QUICDatagram](https://developer.apple.com/documentation/network/quicdatagram): RFC 9221을 통해 QUIC에서 비신뢰 datagram을 송수신합니다.
- [QUICStream](https://developer.apple.com/documentation/network/quicstream): QUIC connection 위에서 동작하는 QUIC stream입니다.
- [TCP](https://developer.apple.com/documentation/network/tcp): Transmission Control Protocol(TCP)의 시스템 정의입니다.
- [TLS](https://developer.apple.com/documentation/network/tls): Transport Layer Security(TLS) 프로토콜의 시스템 정의입니다.
- [TLV](https://developer.apple.com/documentation/network/tlv): Type-Length-Value(TLV) framing 프로토콜입니다.
- [TXTRecordDecoder](https://developer.apple.com/documentation/network/txtrecorddecoder)
- [UDP](https://developer.apple.com/documentation/network/udp): User Datagram Protocol(UDP)의 시스템 정의입니다.
- [UnexpectedEndpointType](https://developer.apple.com/documentation/network/unexpectedendpointtype): 예상하지 못한 endpoint type이 제공될 때 생성되는 오류입니다.
- [WebSocket](https://developer.apple.com/documentation/network/websocket): WebSocket 프로토콜의 시스템 정의입니다.
- [nw_link_quality_t](https://developer.apple.com/documentation/network/nw_link_quality_t)
:::

:::topic-grid
## 클래스
- [NWMultiplexGroup](https://developer.apple.com/documentation/network/nwmultiplexgroup)
- [NetworkBrowser](https://developer.apple.com/documentation/network/networkbrowser): 네트워크에 광고된 서비스와 기기를 발견합니다.
- [NetworkChannel](https://developer.apple.com/documentation/network/networkchannel): 임의의 네트워크 채널을 통해 데이터를 보내고 받는 기능을 지원하는 기본 클래스입니다.
- [NetworkConnection](https://developer.apple.com/documentation/network/networkconnection): 네트워크의 엔드포인트에 연결해 데이터를 송수신합니다.
- [NetworkListener](https://developer.apple.com/documentation/network/networklistener): 들어오는 네트워크 연결을 수신합니다.
:::

:::topic-grid
## 참고 자료
- [Network Constants](https://developer.apple.com/documentation/network/network-constants): C에서 사용하는 Network 프레임워크 상수에 접근합니다.
- [Network Functions](https://developer.apple.com/documentation/network/network-functions): C에서 사용하는 Network 프레임워크 함수에 접근합니다.
- [Network Data Types](https://developer.apple.com/documentation/network/network-data-types)
:::

:::topic-grid
## 프로토콜
- [BrowserProvider](https://developer.apple.com/documentation/network/browserprovider): BrowserProvider는 NetworkBrowser를 생성할 때 사용할 수 있습니다.
- [Connectable](https://developer.apple.com/documentation/network/connectable): NetworkConnection을 만들 때 사용할 수 있는 타입을 설명합니다.
- [ConnectionStorage](https://developer.apple.com/documentation/network/connectionstorage): ConnectionStorage를 준수하는 타입은 연결 내부의 추가 저장소로 사용할 수 있습니다.
- [DatagramProtocol](https://developer.apple.com/documentation/network/datagramprotocol): DatagramProtocol을 준수하는 타입은 일반적으로 고정된 최대 크기로 제한되는 최소한의 메타데이터 또는 메타데이터 없이 메시지를 송수신합니다.
- [FramerProtocol](https://developer.apple.com/documentation/network/framerprotocol): Framer 프로토콜은 연결에서 메시지의 사용자 정의 framing과 직렬화를 허용합니다.
- [ListenerProvider](https://developer.apple.com/documentation/network/listenerprovider): listener가 광고해야 할 서비스를 정의하기 위해 advertise descriptor를 구성하는 확장 가능한 지원입니다.
- [MessageProtocol](https://developer.apple.com/documentation/network/messageprotocol): MessageProtocol을 준수하는 타입은 메시지를 송수신합니다. 준수 타입은 메시지별 metadata를 지정할 책임이 있습니다.
- [MultiplexProtocol](https://developer.apple.com/documentation/network/multiplexprotocol): MultiplexProtocol을 준수하는 타입은 네트워크 프로토콜 스택의 최상위 프로토콜로서 여러 network connection 객체를 multiplexing하는 데 사용할 수 있습니다.
- [NWParametersProvider](https://developer.apple.com/documentation/network/nwparametersprovider): NWParametersProvider 프로토콜을 준수하는 타입은 NWParameters를 생성하는 데 사용할 수 있습니다.
- [NetworkCoder](https://developer.apple.com/documentation/network/networkcoder)
- [NetworkDecoder](https://developer.apple.com/documentation/network/networkdecoder): NetworkEncoder 프로토콜을 준수하는 타입은 데이터를 Encodable 객체로 디코딩할 수 있습니다.
- [NetworkEncoder](https://developer.apple.com/documentation/network/networkencoder): NetworkEncoder 프로토콜을 준수하는 타입은 Encodable 객체를 Data로 인코딩할 수 있습니다.
- [NetworkFixedWidthInteger](https://developer.apple.com/documentation/network/networkfixedwidthinteger)
- [NetworkMetadataProtocol](https://developer.apple.com/documentation/network/networkmetadataprotocol): NetworkProtocolOptions를 준수하는 타입은 프로토콜 스택을 구성할 때 사용할 수 있습니다.
- [NetworkProtocolOptions](https://developer.apple.com/documentation/network/networkprotocoloptions)
- [OneToOneProtocol](https://developer.apple.com/documentation/network/onetooneprotocol): OneToOneProtocol을 준수하는 타입은 비다중화 연결을 위한 네트워크 프로토콜 스택의 최상위 프로토콜로 사용할 수 있습니다.
- [StreamProtocol](https://developer.apple.com/documentation/network/streamprotocol): StreamProtocol 프로토콜을 준수하는 타입은 바이트 스트림을 송수신하는 메서드를 노출합니다.
:::

:::topic-grid
## 변수
- [kNWErrorDomainWiFiAware](https://developer.apple.com/documentation/network/knwerrordomainwifiaware)
- [nw_error_domain_wifi_aware](https://developer.apple.com/documentation/network/nw_error_domain_wifi_aware)
- [nw_link_quality_good](https://developer.apple.com/documentation/network/nw_link_quality_good)
- [nw_link_quality_minimal](https://developer.apple.com/documentation/network/nw_link_quality_minimal)
- [nw_link_quality_moderate](https://developer.apple.com/documentation/network/nw_link_quality_moderate)
- [nw_link_quality_unknown](https://developer.apple.com/documentation/network/nw_link_quality_unknown)
:::

:::topic-grid
## 함수
- [nw_parameters_get_allow_ultra_constrained(_:)](https://developer.apple.com/documentation/network/nw_parameters_get_allow_ultra_constrained(_:))
- [nw_parameters_set_allow_ultra_constrained(_:_:)](https://developer.apple.com/documentation/network/nw_parameters_set_allow_ultra_constrained(_:_:))
- [nw_path_get_link_quality(_:)](https://developer.apple.com/documentation/network/nw_path_get_link_quality(_:))
- [nw_path_is_ultra_constrained(_:)](https://developer.apple.com/documentation/network/nw_path_is_ultra_constrained(_:))
- [withNetworkConnection(to:using:_:)](https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-1sik8)
- [withNetworkConnection(to:using:_:)](https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-4wpc9)
- [withNetworkConnection(to:using:_:)](https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-7skhi)
- [withNetworkConnection(to:using:_:)](https://developer.apple.com/documentation/network/withnetworkconnection(to:using:_:)-887ho)
:::
