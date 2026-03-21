---
route: /documentation/playgroundsupport
source_url: https://developer.apple.com/documentation/playgroundsupport
source_locale: en-US
section: docc
content_type: symbol
title: Playground Support
original_title: Playground Support
source_hash: 249fd33379e46aa46e2c4c8eba33951b3c3c3375fb3c5fdbf6d04c1789b809ed
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:12:36+00:00'
last_translated_at: '2026-03-14T00:45:00+09:00'
---

# Playground Support

playground 데이터를 공유하고, live view를 관리하며, playground의 실행을 제어합니다.

## 개요

Playground 안에서 Playground Support를 사용해 다음을 수행합니다.

- playground 페이지에 접근하고 그 실행을 관리합니다.
- 영속 데이터를 접근하고 공유합니다.
- 학습자의 진행 상황을 평가하고, 힌트를 업데이트하며, 성공 메시지를 표시합니다.

또한 Playground Support를 사용해 *live view*를 표시하고 닫을 수 있습니다. live view는 playground에서 코드를 실행한 결과를 보여 줍니다. 많은 기존 타입에서 제공하는 내장 live view 표현을 활용하면 사용자 정의 타입에 대해서도 live view를 만들 수 있습니다.

기존 live view는 Xcode의 playground와 Swift Playgrounds 모두에서 사용할 수 있습니다. 이들은 playground 코드와 같은 프로세스에서 실행되므로 평소처럼 해당 프로퍼티와 메서드에 접근할 수 있지만, playground를 실행할 때마다 초기화됩니다. Swift Playgrounds에서 페이지에 `LiveView.swift`를 추가하면 활성화되는 always-on live view는 자체 프로세스에서 실행되므로, 연속 실행 사이에도 정보와 시각 요소를 유지할 수 있습니다. Always-on live view는 페이지를 떠날 때까지 초기화되지 않습니다.

:::topic-grid
## Playground 페이지
- [PlaygroundPage](https://developer.apple.com/documentation/playgroundsupport/playgroundpage): playground 페이지의 상태와 live view를 구성할 때 사용하는 객체입니다.
:::

:::topic-grid
## Live view
- [PlaygroundLiveViewable](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewable): 인스턴스를 playground의 live view로 표시하는 프로토콜입니다.
- [PlaygroundLiveViewRepresentation](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewrepresentation): playground의 live view에 표시할 수 있도록 지원되는 타입입니다.
- [PlaygroundLiveViewSafeAreaContainer](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewsafeareacontainer): Swift Playgrounds 사용자 인터페이스 안에서 view가 가려지지 않고 맞도록 보장하는 프로토콜입니다.
:::

:::topic-grid
## 페이지와 view 간 통신
- [Messaging Between a Playground Page and the Always-On Live View](https://developer.apple.com/documentation/playgroundsupport/messaging_between_a_playground_page_and_the_always-on_live_view): playground 페이지 코드의 실행 결과를 영속적인 live view에 표시합니다.
- [PlaygroundRemoteLiveViewProxy](https://developer.apple.com/documentation/playgroundsupport/playgroundremoteliveviewproxy): always-on live view와 해당 playground 페이지 사이의 메시지 전달을 돕는 프록시입니다.
- [PlaygroundRemoteLiveViewProxyDelegate](https://developer.apple.com/documentation/playgroundsupport/playgroundremoteliveviewproxydelegate): always-on live view로부터 메시지를 수신할 때 사용하는 delegate입니다.
- [PlaygroundLiveViewMessageHandler](https://developer.apple.com/documentation/playgroundsupport/playgroundliveviewmessagehandler): always-on live view와 해당 playground 페이지 사이에서 메시지를 주고받을 때 사용하는 handler입니다.
:::

:::topic-grid
## 데이터 영속성
- [PlaygroundKeyValueStore](https://developer.apple.com/documentation/playgroundsupport/playgroundkeyvaluestore): 여러 세션에 걸쳐 정보를 유지할 때 사용하는 데이터 저장 컨테이너입니다.
- [PlaygroundValue](https://developer.apple.com/documentation/playgroundsupport/playgroundvalue): key-value 저장소에 저장하거나 live view에 보내는 메시지에 사용할 수 있는 타입입니다.
- [playgroundSharedDataDirectory](https://developer.apple.com/documentation/playgroundsupport/playgroundshareddatadirectory): Xcode의 모든 playground 사이에서 공유되는 데이터가 들어 있는 디렉터리 경로입니다.
:::
