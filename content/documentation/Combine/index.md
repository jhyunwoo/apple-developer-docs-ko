---
route: /documentation/Combine
source_url: https://developer.apple.com/documentation/Combine
source_locale: en-US
section: docc
content_type: symbol
title: Combine
original_title: Combine
source_hash: df66382ec7107143c972daf72cde6cfb37354cadfc8990c2240007ac3ecf0bcd
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:04:37+00:00'
last_translated_at: '2026-03-14T03:18:00+09:00'
---

# Combine

이벤트 처리 연산자를 조합해 비동기 이벤트 처리를 사용자화합니다.

## 개요

Combine 프레임워크는 시간에 따라 변하는 값을 처리하기 위한 선언형 Swift API를 제공합니다. 이러한 값은 다양한 종류의 비동기 이벤트를 나타낼 수 있습니다. Combine은 시간이 지나며 바뀔 수 있는 값을 노출하기 위한 *publisher*와, publisher로부터 그 값을 받는 *subscriber*를 선언합니다.

- [Publisher](https://developer.apple.com/documentation/combine/publisher) protocol은 시간이 지남에 따라 값의 시퀀스를 전달할 수 있는 타입을 선언합니다. publisher는 upstream publisher에서 받은 값에 작용하고 다시 게시하는 *operator*를 가집니다.
- publisher 체인의 끝에서 [Subscriber](https://developer.apple.com/documentation/combine/subscriber)는 요소를 받는 즉시 그 요소에 대해 동작합니다. publisher는 subscriber가 명시적으로 요청할 때만 값을 방출합니다. 이로써 subscriber 코드는 자신이 연결된 publisher로부터 이벤트를 얼마나 빠르게 받을지 제어할 수 있습니다.

[Timer](https://developer.apple.com/documentation/Foundation/Timer), [NotificationCenter](https://developer.apple.com/documentation/Foundation/NotificationCenter), [URLSession](https://developer.apple.com/documentation/Foundation/URLSession)을 포함한 여러 Foundation 타입이 publisher를 통해 기능을 노출합니다. Combine은 또한 Key-Value Observing을 준수하는 모든 property를 위한 내장 publisher도 제공합니다.

여러 publisher의 출력을 결합하고 그 상호 작용을 조정할 수 있습니다. 예를 들어 텍스트 필드의 publisher 업데이트를 구독하고, 그 텍스트를 사용해 URL 요청을 수행할 수 있습니다. 그런 다음 또 다른 publisher를 사용해 응답을 처리하고 그 결과로 앱을 업데이트할 수 있습니다.

Combine을 채택하면 이벤트 처리 코드를 중앙화하고 중첩 closure나 관례 기반 callback 같은 까다로운 기법을 제거하여 코드를 더 읽기 쉽고 유지 보수하기 쉽게 만들 수 있습니다.

:::topic-grid
## 기초
- [Receiving and Handling Events with Combine](https://developer.apple.com/documentation/combine/receiving-and-handling-events-with-combine): 비동기 소스에서 오는 이벤트를 사용자화하고 수신합니다.
:::

:::topic-grid
## Publisher
- [Publisher](https://developer.apple.com/documentation/combine/publisher): 타입이 시간에 따라 값의 시퀀스를 전송할 수 있음을 선언합니다.
- [Publishers](https://developer.apple.com/documentation/combine/publishers): publisher 역할을 하는 타입을 위한 namespace입니다.
- [AnyPublisher](https://developer.apple.com/documentation/combine/anypublisher): 다른 publisher를 감싸 타입 소거를 수행하는 publisher입니다.
- [Published](https://developer.apple.com/documentation/combine/published): attribute가 표시된 property를 게시하는 타입입니다.
- [Cancellable](https://developer.apple.com/documentation/combine/cancellable): 활동 또는 작업이 취소를 지원함을 나타내는 protocol입니다.
- [AnyCancellable](https://developer.apple.com/documentation/combine/anycancellable): 취소 시 제공된 closure를 실행하는 type-erasing cancellable 객체입니다.
:::

:::topic-grid
## 편의 Publisher
- [Future](https://developer.apple.com/documentation/combine/future): 결국 하나의 값을 생성한 뒤 완료하거나 실패하는 publisher입니다.
- [Just](https://developer.apple.com/documentation/combine/just): 각 subscriber에게 단 한 번 output을 방출하고 완료하는 publisher입니다.
- [Deferred](https://developer.apple.com/documentation/combine/deferred): 새 subscriber를 위한 publisher를 생성하기 위해 제공된 closure를 실행하기 전에 구독을 기다리는 publisher입니다.
- [Empty](https://developer.apple.com/documentation/combine/empty): 값을 전혀 게시하지 않고 필요하면 즉시 완료하는 publisher입니다.
- [Fail](https://developer.apple.com/documentation/combine/fail): 지정한 오류로 즉시 종료하는 publisher입니다.
- [Record](https://developer.apple.com/documentation/combine/record): 나중에 각 subscriber에게 재생할 수 있도록 입력 시리즈와 completion을 기록하게 해 주는 publisher입니다.
:::

:::topic-grid
## Connectable Publisher
- [Controlling Publishing with Connectable Publishers](https://developer.apple.com/documentation/combine/controlling-publishing-with-connectable-publishers): publisher가 subscriber에게 요소 전송을 시작하는 시점을 조정합니다.
- [ConnectablePublisher](https://developer.apple.com/documentation/combine/connectablepublisher): publication을 연결하고 취소하는 명시적 수단을 제공하는 publisher입니다.
:::

:::topic-grid
## Subscriber
- [Processing Published Elements with Subscribers](https://developer.apple.com/documentation/combine/processing-published-elements-with-subscribers): publisher가 요소를 생성하는 시점을 정밀하게 제어하기 위해 back pressure를 적용합니다.
- [Subscriber](https://developer.apple.com/documentation/combine/subscriber): publisher로부터 입력을 받을 수 있는 타입을 선언하는 protocol입니다.
- [Subscribers](https://developer.apple.com/documentation/combine/subscribers): subscriber 역할을 하는 타입을 위한 namespace입니다.
- [AnySubscriber](https://developer.apple.com/documentation/combine/anysubscriber): type-erasing subscriber입니다.
- [Subscription](https://developer.apple.com/documentation/combine/subscription): subscriber와 publisher 사이의 연결을 나타내는 protocol입니다.
- [Subscriptions](https://developer.apple.com/documentation/combine/subscriptions): subscription과 관련된 symbol을 위한 namespace입니다.
:::

:::topic-grid
## Subject
- [Subject](https://developer.apple.com/documentation/combine/subject): 외부 호출자가 요소를 게시할 수 있는 메서드를 노출하는 publisher입니다.
- [CurrentValueSubject](https://developer.apple.com/documentation/combine/currentvaluesubject): 단일 값을 감싸며 그 값이 변할 때마다 새 요소를 게시하는 subject입니다.
- [PassthroughSubject](https://developer.apple.com/documentation/combine/passthroughsubject): downstream subscriber에게 요소를 방송하는 subject입니다.
:::

:::topic-grid
## Scheduler
- [Scheduler](https://developer.apple.com/documentation/combine/scheduler): closure를 언제, 어떻게 실행할지 정의하는 protocol입니다.
- [ImmediateScheduler](https://developer.apple.com/documentation/combine/immediatescheduler): 동기 작업을 수행하기 위한 scheduler입니다.
- [SchedulerTimeIntervalConvertible](https://developer.apple.com/documentation/combine/schedulertimeintervalconvertible): scheduler에 상대 시간을 위한 표현을 제공하는 protocol입니다.
:::

:::topic-grid
## Combine 마이그레이션
- [Routing Notifications to Combine Subscribers](https://developer.apple.com/documentation/combine/routing-notifications-to-combine-subscribers): notification center의 publisher를 사용해 notification을 subscriber에게 전달합니다.
- [Replacing Foundation Timers with Timer Publishers](https://developer.apple.com/documentation/combine/replacing-foundation-timers-with-timer-publishers): timer를 사용해 주기적으로 요소를 게시합니다.
- [Performing Key-Value Observing with Combine](https://developer.apple.com/documentation/combine/performing-key-value-observing-with-combine): Combine publisher로 KVO 변경을 노출합니다.
- [Using Combine for Your App’s Asynchronous Code](https://developer.apple.com/documentation/combine/using-combine-for-your-app-s-asynchronous-code): closure 기반 이벤트 처리 코드를 마이그레이션하기 위한 공통 패턴을 적용합니다.
:::

:::topic-grid
## Observable Object
- [ObservableObject](https://developer.apple.com/documentation/combine/observableobject): 객체가 변경되기 전에 방출하는 publisher를 가진 객체 타입입니다.
- [ObservableObjectPublisher](https://developer.apple.com/documentation/combine/observableobjectpublisher): observable object의 변경 사항을 게시하는 publisher입니다.
:::

:::topic-grid
## 비동기 Publisher
- [AsyncPublisher](https://developer.apple.com/documentation/combine/asyncpublisher): 요소를 비동기 시퀀스로 노출하는 publisher입니다.
- [AsyncThrowingPublisher](https://developer.apple.com/documentation/combine/asyncthrowingpublisher): 요소를 throwing 비동기 시퀀스로 노출하는 publisher입니다.
:::

:::topic-grid
## Encoder와 Decoder
- [TopLevelEncoder](https://developer.apple.com/documentation/combine/toplevelencoder): 인코딩용 메서드를 정의하는 타입입니다.
- [TopLevelDecoder](https://developer.apple.com/documentation/combine/topleveldecoder): 디코딩용 메서드를 정의하는 타입입니다.
:::

:::topic-grid
## 디버깅 식별자
- [CustomCombineIdentifierConvertible](https://developer.apple.com/documentation/combine/customcombineidentifierconvertible): publisher stream을 고유하게 식별하기 위한 protocol입니다.
- [CombineIdentifier](https://developer.apple.com/documentation/combine/combineidentifier): publisher stream을 식별하기 위한 고유 식별자입니다.
:::
