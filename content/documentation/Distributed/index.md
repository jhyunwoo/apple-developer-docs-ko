---
route: /documentation/Distributed
source_url: https://developer.apple.com/documentation/Distributed
source_locale: en-US
section: docc
content_type: symbol
title: Distributed
original_title: Distributed
source_hash: 72e3ee8ed4715afba50cda2f3a0276e10566ce9de94c0e1c59c1b0057335ee36
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:24:08+00:00'
last_translated_at: '2026-03-14T01:12:00+09:00'
---

# Distributed

여러 프로세스와 기기에 걸쳐 분산 코드를 실행하는 시스템을 빌드합니다.

## 개요

Distributed actor는 Swift actor와 많은 특성을 공유하며, 분산 환경에서 위치 투명성과 안전성을 보장하기 위한 추가 격리 검사를 포함합니다. Actor가 단일 컴퓨터에서 안전하고 올바르게 실행되는 동시성 코드를 더 쉽게 작성하게 해 주는 것과 비슷하게, distributed actor는 여러 컴퓨터에 걸쳐 실행되는 코드를 더 쉽게 작성하게 해 줍니다.

![두 개의 actor 열을 보여 주는 다이어그램입니다. 왼쪽 열에는 remote actor reference가 있고, 오른쪽 열에는 local distributed actor가 있습니다. 화살표는 remote actor reference가 자신이 가리키는 local distributed actor를 향하고 있습니다.](https://developer.apple.com)

Distributed actor로 코드를 작성할 때는 세 가지 주요 요소를 사용합니다.

- Actor와 distributed actor를 위한 Swift 언어 지원입니다. 자세한 내용은 [The Swift Programming Language](https://docs.swift.org/swift-book/)의 [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html)를 참고하십시오.
- Distributed module입니다. 이 모듈에는 distributed actor를 선언하고 사용하는 데 필요한 타입과 프로토콜이 포함되어 있습니다. 예를 들어 distributed actor와 distributed actor system이 준수하는 프로토콜, 그리고 distributed actor 호출 정보를 캡슐화하는 구조체가 포함됩니다.
- *distributed actor system*(cluster runtime이라고도 함)입니다. 이는 [DistributedActorSystem](https://developer.apple.com/documentation/distributed/distributedactorsystem) 프로토콜의 구현을 제공하고 클러스터 노드 간 조정을 담당합니다. Distributed actor는 항상 어떤 distributed actor system의 일부이며, 그 system이 원격 메서드 호출에 필요한 직렬화와 네트워킹을 처리합니다. 로컬 테스트에는 [LocalTestingDistributedActorSystem](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystem)을 사용할 수 있습니다. 프로덕션에서는 [Swift Distributed Actors](https://github.com/apple/swift-distributed-actors/) 라이브러리의 distributed actor system을 사용하거나, 다른 라이브러리를 사용하거나, 직접 distributed actor system을 작성할 수 있습니다.

:::topic-grid
## 핵심 사항
- [TicTacFish: Implementing a game using distributed actors](https://developer.apple.com/documentation/swift/tictacfish_implementing_a_game_using_distributed_actors): Distributed actor를 사용해 Swift 동시성과 actor 기반 앱을 단일 프로세스 너머로 확장합니다.
:::

:::topic-grid
## Distributed actor
- [DistributedActor](https://developer.apple.com/documentation/distributed/distributedactor): 모든 distributed actor가 암묵적으로 준수하는 공통 프로토콜입니다.
- [DistributedActorSystem](https://developer.apple.com/documentation/distributed/distributedactorsystem): distributed actor의 모든 기능을 뒷받침하고 구현하는 distributed actor system입니다.
- [Resolvable()](https://developer.apple.com/documentation/distributed/resolvable()): 부착된 프로토콜을 원격 distributed actor reference로 resolve할 수 있게 합니다.
- [buildDefaultDistributedRemoteActorExecutor(_:)](https://developer.apple.com/documentation/distributed/builddefaultdistributedremoteactorexecutor(_:)): 원격 distributed actor reference가 사용하는 unowned executor를 얻습니다. 이 executor는 모든 원격 기본 executor distributed actor 사이에서 공유되며, 여기에 작업이 enqueue되면 crash가 발생합니다.
:::

:::topic-grid
## 원격 호출
- [RemoteCallTarget](https://developer.apple.com/documentation/distributed/remotecalltarget): 메서드나 계산 프로퍼티처럼 distributed call의 '대상'을 나타냅니다. 식별 방식은 시스템마다 다를 수 있으며, 향후 변경될 수 있습니다.
- [RemoteCallArgument](https://developer.apple.com/documentation/distributed/remotecallargument): distributed call target에 전달되는 인자를 나타냅니다.
- [DistributedTargetInvocationEncoder](https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder): distributed target(메서드 또는 계산 프로퍼티)의 호출을 인코딩할 때 사용합니다.
- [DistributedTargetInvocationDecoder](https://developer.apple.com/documentation/distributed/distributedtargetinvocationdecoder): Swift runtime이 호출 인자를 디코딩할 때 사용하는 decoder입니다.
- [DistributedTargetInvocationResultHandler](https://developer.apple.com/documentation/distributed/distributedtargetinvocationresulthandler): distributed invocation 실행 결과 처리기가 준수하는 프로토콜입니다.
:::

:::topic-grid
## 로컬 테스트
- [LocalTestingDistributedActorSystem](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystem): 로컬 전용 테스트를 위해 설계된 시스템입니다.
- [LocalTestingActorID](https://developer.apple.com/documentation/distributed/localtestingactorid)
- [LocalTestingActorAddress](https://developer.apple.com/documentation/distributed/localtestingactoraddress)
- [LocalTestingInvocationEncoder](https://developer.apple.com/documentation/distributed/localtestinginvocationencoder)
- [LocalTestingInvocationDecoder](https://developer.apple.com/documentation/distributed/localtestinginvocationdecoder)
- [LocalTestingInvocationResultHandler](https://developer.apple.com/documentation/distributed/localtestinginvocationresulthandler)
:::

:::topic-grid
## 오류
- [DistributedActorCodingError](https://developer.apple.com/documentation/distributed/distributedactorcodingerror): distributed actor system이 인코딩/디코딩 문제를 만났을 때 발생시키는 오류입니다.
- [DistributedActorSystemError](https://developer.apple.com/documentation/distributed/distributedactorsystemerror): 모든 distributed actor system이 발생시키는 오류가 준수해야 하는 오류 프로토콜입니다.
- [ExecuteDistributedTargetError](https://developer.apple.com/documentation/distributed/executedistributedtargeterror): distributed target 실행 중 발생하는 오류입니다.
- [LocalTestingDistributedActorSystemError](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystemerror)
:::
