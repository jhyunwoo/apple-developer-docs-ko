---
route: /documentation/XPC
source_url: https://developer.apple.com/documentation/XPC
source_locale: en-US
section: docc
content_type: symbol
title: XPC
original_title: XPC
source_hash: 69728299d503abffed58d48739d7818ab399ba0fab6d1dc77b2dcf75a2a7d80a
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:46:58+00:00'
last_translated_at: '2026-03-14T01:23:00+09:00'
---

# XPC

하위 수준 프로세스 간 통신 메커니즘에 접근합니다.

## 개요

XPC는 기본적인 프로세스 간 통신을 위한 경량 메커니즘을 제공합니다. 이를 사용하면 앱을 대신해 작업을 수행하는 경량 helper tool, 즉 *XPC service*를 만들 수 있습니다. `launchd` 시스템 daemon은 이러한 서비스를 관리하며, 필요할 때 실행하고, 유휴 상태가 되면 종료하며, 충돌 시 다시 시작합니다. XPC service의 장점은 다음과 같습니다.

- 여러 프로세스의 작업을 중앙집중화하거나 공유 리소스에 대한 접근을 중재합니다.
- 클라이언트의 life cycle을 넘어 계속되어야 하는 작업을 위임합니다.
- 권한 격리를 통해 기능별 접근 범위를 좁힙니다.

이러한 서비스를 사용하는 클라이언트는 프로세스 경계를 넘어 통신하기 위해 peer-to-peer XPC 연결에 의존합니다. 각 연결에는 두 측면이 있습니다. 한쪽은 *listener* 또는 서버로, 들어오는 연결 요청에 응답하고 작업을 수행합니다. 다른 한쪽은 클라이언트로, listener와 *session*을 생성해 XPC service에 연결을 시작합니다. 클라이언트가 listener와 연결을 맺으면 서비스에 메시지를 보내고 응답을 받습니다.

어떤 유형의 XPC service를 빌드할지는 서비스가 수행하는 작업 요구 사항에 따라 달라집니다. 다음 표는 사용 가능한 서비스 유형과 동작 방식의 차이 일부를 요약한 것입니다.

| Service Type | Process Environment |
| --- | --- |
| Launch Agent | 로그인한 사용자마다 하나의 프로세스가 있으며, 해당 사용자 권한으로 실행됩니다. 빠른 사용자 전환으로 여러 사용자가 로그인한 경우 각 사용자는 자신의 실행 중인 프로세스를 가집니다. |
| Launch Daemon | 더 높은 권한 수준에서 `root` 사용자로 실행되는 시스템 전역 프로세스 하나입니다. LaunchDaemon은 사용자 프로세스에 대한 연결을 시작할 수 없지만, 그들로부터의 요청에는 응답할 수 있습니다. |
| XPC Service | 서비스의 클라이언트마다 하나의 프로세스가 있으며, 클라이언트의 수명과 연결됩니다. 클라이언트 프로세스가 서비스에 연결하면 `launchd`가 XPC service용 프로세스를 시작합니다. 클라이언트 프로세스가 종료되면 XPC service도 함께 종료됩니다. 이 유형의 서비스는 앱이나 프레임워크 내부에 번들로 포함합니다. |

:::note Note
LaunchAgent와 LaunchDaemon 유형은 특별한 설치와 구성이 필요합니다. macOS 13 이전에는 앱이 일반적으로 설치 스크립트를 사용해 이러한 서비스 유형을 구성했습니다. macOS 13 이후에는 [Service Management](https://developer.apple.com/documentation/ServiceManagement) 프레임워크가 이러한 서비스 유형을 패키징하고 설치하는 새로운 구조를 제공합니다.
:::

XPC service는 C, Swift, Objective-C로 빌드할 수 있습니다. XPC 사용에는 고수준 API와 저수준 API가 모두 있습니다. 프로젝트가 Foundation 프레임워크를 사용한다면 [NSXPCConnection](https://developer.apple.com/documentation/Foundation/NSXPCConnection)이 프로세스 간 투명한 원격 메서드 디스패치 메커니즘을 제공하는 고수준 객체 지향 API를 제공합니다. Foundation 프레임워크의 [NSXPCConnection](https://developer.apple.com/documentation/Foundation/NSXPCConnection)을 사용하면 클라이언트가 사용할 명확하게 정의된 프로토콜을 설계할 수 있습니다. 프로젝트가 Foundation에 연결하지 않거나 연결할 수 없다면 XPC 프레임워크의 저수준 `libSystem` API를 사용하십시오.

:::topic-grid
## 핵심 사항
- [XPC updates](https://developer.apple.com/documentation/Updates/XPC): XPC의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 프로세스 간 통신
- [Creating XPC services](https://developer.apple.com/documentation/xpc/creating-xpc-services): listener를 구성하고, 클라이언트 session을 설정하며, 프로세스 간 메시지를 교환합니다.
- [XPCListener](https://developer.apple.com/documentation/xpc/xpclistener): 프로세스 경계를 넘어 클라이언트를 위해 작업을 수행하는 타입입니다.
- [XPCSession](https://developer.apple.com/documentation/xpc/xpcsession): 서버 프로세스로 메시지를 보내는 타입입니다.
- [XPCReceivedMessage](https://developer.apple.com/documentation/xpc/xpcreceivedmessage): session과 listener 사이에 전달된 메시지를 나타내는 타입입니다.
- [xpc_listener_t](https://developer.apple.com/documentation/xpc/xpc_listener_t): 프로세스 경계를 넘어 클라이언트를 위해 작업을 수행하는 C 타입입니다.
- [xpc_session_t](https://developer.apple.com/documentation/xpc/xpc_session_t-10if0): 서버 프로세스로 메시지를 보내는 C 타입입니다.
:::

:::topic-grid
## 작업
- [XPC activities](https://developer.apple.com/documentation/xpc/xpc-activities): 시스템이 실행할 백그라운드 활동을 예약합니다.
:::

:::topic-grid
## 이벤트
- [XPC events](https://developer.apple.com/documentation/xpc/xpc-events): IOKit 이벤트와 알림에 필요 시 응답합니다.
:::

:::topic-grid
## 추가 타입
- [XPC objects](https://developer.apple.com/documentation/xpc/xpc-objects): 기본 타입, 컬렉션 등을 나타내는 객체 안에 데이터를 캡슐화합니다.
- [Utilities](https://developer.apple.com/documentation/xpc/utilities): XPC API와 함께 사용할 디버깅 유틸리티와 상수를 살펴봅니다.
- [XPC connections](https://developer.apple.com/documentation/xpc/xpc-connections): 연결 기반 API를 사용해 서비스 연결을 생성하고 관리합니다.
:::

:::topic-grid
## 클래스
- [OS_xpc_session](https://developer.apple.com/documentation/xpc/os_xpc_session-swift.class)
:::

:::topic-grid
## 구조체
- [XPCEndpoint](https://developer.apple.com/documentation/xpc/xpcendpoint): 직렬화된 형태의 연결입니다.
- [XPCPeerRequirement](https://developer.apple.com/documentation/xpc/xpcpeerrequirement)
:::

:::topic-grid
## 타입 별칭
- [xpc_peer_requirement_t](https://developer.apple.com/documentation/xpc/xpc_peer_requirement_t)
:::
