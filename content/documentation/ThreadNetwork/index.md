---
route: /documentation/ThreadNetwork
source_url: https://developer.apple.com/documentation/ThreadNetwork
source_locale: en-US
section: docc
content_type: symbol
title: ThreadNetwork
original_title: ThreadNetwork
source_hash: 61eb0f8e82b7ed88e6c8d6950f8d4d4aea04b6a04044750bddab701a4ca7f96e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:26:18+00:00'
last_translated_at: '2026-03-13T23:26:32+09:00'
---

# ThreadNetwork

Thread Border Router를 사용해 견고한 스마트 기기 네트워크를 만듭니다.

## 개요

[Thread](https://www.threadgroup.org) 표준은 표준 인터넷 프로토콜 위에서 동작하는 저전력 무선 메시 네트워킹 프로토콜로, Apple Home 호환 기기 같은 스마트 홈 기기가 서로 통신할 수 있게 합니다. 메시 네트워크는 중앙에 단일 라우터가 없는 peer-to-peer 네트워크이므로 단일 장애 지점의 위험이 없습니다. 또한 공유 자격 증명을 가진 주변 peer 기기를 찾아 스스로 동적으로 재구성할 수 있습니다. 그 결과 일부 기기가 오프라인이 되더라도 통신을 유지할 수 있습니다.

![2층짜리 집의 단면도입니다. 아래층 거실에는 선풍기, HomePod mini, 전구, 리모컨이 Thread로 무선 연결되어 있습니다. 위층 방에는 천장 선풍기, HomePod, 여러 전구, 벽면 플러그가 Thread로 연결되어 있습니다. 1층 주방에는 오븐과 전구가 Thread에 무선 연결되어 있습니다. 앞마당에는 나무 아래의 조경등이 Thread에 무선 연결되어 있습니다.](https://developer.apple.com)

Thread의 견고함은 구성원 기기가 이웃에게 패킷을 전달하는 데서 나옵니다. 이 과정으로 메시가 형성되며, 사람들이 더 많은 기기를 추가할수록 네트워크는 더 강해지고 신뢰성이 높아집니다. 또한 메시지 경로가 더 많아지므로, 특히 큰 네트워크에서는 더 빠른 통신도 제공할 수 있습니다.

Thread Border Router 하드웨어 기기는 Thread 네트워크의 핵심 요소입니다. 이 기기는 Thread와 Wi‑Fi 또는 Ethernet 네트워크 사이에서 IP 트래픽을 라우팅하고, iOS 기기가 Thread 기기와 통신할 수 있게 해 줍니다. HomePod와 HomePod mini는 Border Router의 예입니다.

자신만의 Thread Border Router를 만들려면 ThreadNetwork 프레임워크를 사용해 라우터를 구성하고 관리하십시오. ThreadNetwork 프레임워크는 인증된 Thread Border Router에 적합한 Thread 네트워크를 선택하는 데 도움을 줍니다.

## Thread 네트워크 기기 역할 알아보기

Thread 네트워크에는 여러 유형의 기기가 포함될 수 있으며, 사람은 이를 다양한 조합으로 배치할 수 있습니다.

:::term-list
Thread Border Router: Thread 네트워크와 기존 Wi‑Fi 또는 Ethernet 네트워크 사이의 연결을 제공하는 기기입니다. 이러한 기기는 라우터 역할만 수행하는 독립형일 수도 있고, 추가 기능을 지원할 수도 있습니다. 예를 들어 HomePod(2세대), HomePod mini, Apple TV 4K는 모두 Thread Border Router의 예입니다.
Thread Leader: Thread 네트워크에서 라우터를 관리하는 기기입니다. Thread 네트워크에는 어느 시점이든 Thread Leader가 하나만 존재할 수 있으며, 구성원 기기는 성능을 최적화하기 위해 네트워크의 여러 라우팅 특성을 바탕으로 Thread Leader를 선택합니다.
End device: Thread 네트워크 끝단에 위치한 Thread 기기입니다. 다른 Thread 기기와 직접 통신할 수 있지만, 다른 기기를 대신해 패킷을 전달하는 라우터 역할은 하지 않습니다.
Sleepy End device: 저전력 모드로 동작하며 대체로 배터리로 구동되는 end device입니다. 전력을 절약하기 위해 가끔씩만 깨어나 자신이 수집한 데이터를 보고하므로 “sleepy”라고 부릅니다. 배터리식 온도 센서나 공기 질 모니터가 대표적인 예입니다.
:::

다음 이미지는 Border Router, end device, sleepy end device 사이의 연결을 보여 줍니다.

![Thread Border Router가 두 개의 end device와 무선으로 연결되어 있습니다. 하나는 조명 스위치를 나타내는 end device 아이콘이고, 다른 하나는 무선 배터리식 센서를 나타내는 sleepy end device 아이콘입니다.](https://developer.apple.com)

Thread에 대해 더 알아보려면 [OpenThread Guides](https://openthread.io/guides)와 [What is Thread?](https://www.threadgroup.org/What-is-Thread/Overview)를 참고하십시오.

:::note Note
Thread 표준은 Thread Group이 개발하며, Border Router를 설명하기 위해 “Thread”라는 용어를 사용하는 것은 Thread Group의 상표 및 인증 정책의 적용을 받습니다.
:::

ThreadNetwork 개발 과정에 대해 더 알아보려면 [Getting started with ThreadNetwork](https://developer.apple.com/documentation/threadnetwork/getting-started-with-threadnetwork)를 참고하십시오.

:::topic-grid
## Thread Border Router 설정
- [Getting started with ThreadNetwork](https://developer.apple.com/documentation/threadnetwork/getting-started-with-threadnetwork): Thread Border Router 앱을 빌드, 테스트, 배포하기 위한 계획을 세웁니다.
- [Configuring a Border Router](https://developer.apple.com/documentation/threadnetwork/configuring-a-border-router): Thread 네트워크에서 Border Router를 설정하거나 추가합니다.
- [Managing Thread network credentials](https://developer.apple.com/documentation/threadnetwork/managing-thread-network-credentials): Apple 기기에서 Thread 네트워크 자격 증명을 저장, 조회, 업데이트, 삭제합니다.
:::

:::topic-grid
## 클라이언트 관리 및 자격 증명 공유
- [com.apple.developer.networking.manage-thread-network-credentials](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.manage-thread-network-credentials): 앱이 ThreadNetwork를 사용할 수 있는지 나타내는 Boolean 값입니다.
- [THClient](https://developer.apple.com/documentation/threadnetwork/thclient): 여러 클라이언트 사이에서 Thread 자격 증명을 안전하게 공유할 수 있게 해 주는 클래스입니다.
- [THCredentials](https://developer.apple.com/documentation/threadnetwork/thcredentials): Thread 네트워크의 자격 증명을 담는 클래스입니다.
:::
