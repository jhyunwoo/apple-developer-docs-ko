---
route: /documentation/Dispatch
source_url: https://developer.apple.com/documentation/Dispatch
source_locale: en-US
section: docc
content_type: symbol
title: Dispatch
original_title: Dispatch
source_hash: c6b782fcbba5a125f51fdf70939c6659958ad18361ab5fe284ba5d442321e911
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:55:50+00:00'
last_translated_at: '2026-03-13T16:05:00+09:00'
---

# Dispatch

시스템이 관리하는 dispatch queue에 작업을 제출하여 멀티코어 하드웨어에서 코드를 동시에 실행합니다.

## 개요

Grand Central Dispatch(GCD)라고도 하는 Dispatch는 macOS, iOS, watchOS, tvOS의 멀티코어 하드웨어에서 동시 코드 실행 지원을 시스템 차원에서 포괄적으로 개선하는 언어 기능, 런타임 라이브러리, 시스템 향상을 포함합니다.

BSD 서브시스템, Core Foundation, Cocoa API는 모두 이러한 향상을 사용하도록 확장되어 시스템과 앱이 더 빠르고 효율적으로, 그리고 더 뛰어난 응답성으로 동작하도록 돕습니다. 하나의 앱이 여러 코어를 효과적으로 활용하는 것조차 어렵고, 하물며 코어 수가 서로 다른 다양한 컴퓨터나 여러 앱이 같은 코어를 두고 경쟁하는 환경에서 이를 수행하는 일은 더욱 어렵습니다. 시스템 수준에서 동작하는 GCD는 실행 중인 모든 앱의 요구 사항을 더 잘 수용하고, 이를 사용 가능한 시스템 리소스에 균형 있게 맞출 수 있습니다.

### Dispatch 객체와 ARC

Objective-C 컴파일러를 사용해 앱을 빌드하면 모든 dispatch 객체는 Objective-C 객체가 됩니다. 따라서 automatic reference counting(ARC)이 활성화되어 있으면 dispatch 객체는 다른 Objective-C 객체와 마찬가지로 자동으로 retain 및 release 됩니다. ARC가 활성화되어 있지 않다면 [dispatch_retain](https://developer.apple.com/documentation/dispatch/dispatch_retain) 및 [dispatch_release](https://developer.apple.com/documentation/dispatch/dispatch_release) 함수(또는 Objective-C 의미 체계)를 사용해 dispatch 객체를 retain 및 release 하십시오. Core Foundation retain 및 release 함수는 사용할 수 없습니다.

이전 배포 대상과의 호환성을 유지하기 위해 ARC가 활성화된 앱에서 retain 및 release 의미 체계를 사용해야 한다면, 컴파일러 플래그에 `-DOS_OBJECT_USE_OBJC=0`을 추가해 Objective-C 기반 dispatch 객체를 비활성화할 수 있습니다.

:::topic-grid
## 큐와 작업
- [DispatchQueue](https://developer.apple.com/documentation/dispatch/dispatchqueue): 앱의 메인 스레드 또는 백그라운드 스레드에서 작업을 직렬 또는 동시 방식으로 실행하도록 관리하는 객체입니다.
- [DispatchWorkItem](https://developer.apple.com/documentation/dispatch/dispatchworkitem): 완료 핸들이나 실행 의존성을 연결할 수 있도록 캡슐화한 작업 단위입니다.
- [DispatchGroup](https://developer.apple.com/documentation/dispatch/dispatchgroup): 하나의 단위로 모니터링하는 작업 그룹입니다.
- [Dispatch Queue](https://developer.apple.com/documentation/dispatch/dispatch-queue): 앱의 메인 스레드 또는 백그라운드 스레드에서 작업을 직렬 또는 동시 방식으로 실행하도록 관리하는 객체입니다.
- [Dispatch Work Item](https://developer.apple.com/documentation/dispatch/dispatch-work-item): 완료 핸들이나 실행 의존성을 연결할 수 있도록 캡슐화한 작업 단위입니다.
- [Dispatch Group](https://developer.apple.com/documentation/dispatch/dispatch-group): 하나의 단위로 모니터링하는 작업 그룹입니다.
- [Workloop](https://developer.apple.com/documentation/dispatch/workloop): quality-of-service(QoS) 수준에 따라 작업 실행 우선순위를 정하는 dispatch 객체입니다.
:::

:::topic-grid
## 스레드 스케줄링
- [DispatchQoS](https://developer.apple.com/documentation/dispatch/dispatchqos): 작업에 적용하는 서비스 품질, 즉 실행 우선순위입니다.
:::

:::topic-grid
## 시스템 이벤트 모니터링
- [DispatchSource](https://developer.apple.com/documentation/dispatch/dispatchsource): 파일 시스템 이벤트, 타이머, UNIX 신호 같은 특정 저수준 시스템 이벤트 처리를 조정하는 객체입니다.
- [Dispatch Source](https://developer.apple.com/documentation/dispatch/dispatch-source): 파일 시스템 이벤트, 타이머, UNIX 신호 같은 특정 저수준 시스템 이벤트 처리를 조정하는 객체입니다.
- [DispatchIO](https://developer.apple.com/documentation/dispatch/dispatchio): 스트림 기반 또는 임의 접근 의미 체계로 파일 디스크립터 작업을 관리하는 객체입니다.
- [DispatchData](https://developer.apple.com/documentation/dispatch/dispatchdata): 메모리 기반 데이터 버퍼를 관리하고 이를 연속된 메모리 블록으로 노출하는 객체입니다.
- [DispatchDataIterator](https://developer.apple.com/documentation/dispatch/dispatchdataiterator): dispatch data 객체의 내용을 바이트 단위로 순회하는 반복자입니다.
- [Dispatch I/O](https://developer.apple.com/documentation/dispatch/dispatch-i-o): 스트림 기반 또는 임의 접근 의미 체계로 파일 디스크립터 작업을 관리하는 객체입니다.
- [Dispatch Data](https://developer.apple.com/documentation/dispatch/dispatch-data): 메모리 기반 데이터 버퍼를 관리하고 이를 연속된 메모리 블록으로 노출하는 객체입니다.
- [DispatchSourceProtocol](https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol): 모든 dispatch source 타입이 공유하는 공통 속성과 메서드 집합을 정의합니다.
:::

:::topic-grid
## 작업 동기화
- [DispatchSemaphore](https://developer.apple.com/documentation/dispatch/dispatchsemaphore): 전통적인 카운팅 세마포어를 사용해 여러 실행 컨텍스트에서 리소스 접근을 제어하는 객체입니다.
- [Dispatch Semaphore](https://developer.apple.com/documentation/dispatch/dispatch-semaphore): 전통적인 카운팅 세마포어를 사용해 여러 실행 컨텍스트에서 리소스 접근을 제어하는 객체입니다.
- [Dispatch Barrier](https://developer.apple.com/documentation/dispatch/dispatch-barrier): 동시 dispatch queue에서 실행되는 작업을 위한 동기화 지점입니다.
:::

:::topic-grid
## 시간 구성 요소
- [DispatchTime](https://developer.apple.com/documentation/dispatch/dispatchtime): 기본 시계를 기준으로 한 시점으로, 나노초 정밀도를 가집니다.
- [DispatchWallTime](https://developer.apple.com/documentation/dispatch/dispatchwalltime): wall clock 기준의 절대 시점으로, 마이크로초 정밀도를 가집니다.
- [DispatchTimeInterval](https://developer.apple.com/documentation/dispatch/dispatchtimeinterval): 초, 밀리초, 마이크로초 또는 나노초 수를 나타냅니다.
- [DispatchTimeoutResult](https://developer.apple.com/documentation/dispatch/dispatchtimeoutresult): dispatch 작업이 지정된 시간 전에 끝났는지 여부를 나타내는 결과 값입니다.
- [dispatch_time_t](https://developer.apple.com/documentation/dispatch/dispatch_time_t): 추상적인 시간 표현입니다.
- [DISPATCH_WALLTIME_NOW](https://developer.apple.com/documentation/dispatch/dispatch_walltime_now): 현재 시각입니다.
- [Wall Time Constants](https://developer.apple.com/documentation/dispatch/2963138-wall-time-constants): wall time 값에 대한 상수입니다.
:::

:::topic-grid
## Dispatch 객체
- [DispatchObject](https://developer.apple.com/documentation/dispatch/dispatchobject): 대부분의 dispatch 타입의 기본 클래스입니다.
- [DispatchPredicate](https://developer.apple.com/documentation/dispatch/dispatchpredicate): 주어진 실행 컨텍스트 안에서 평가할 논리 조건입니다.
- [dispatchPrecondition(condition:)](https://developer.apple.com/documentation/dispatch/dispatchprecondition(condition:)): 이후 실행에 필요한 dispatch 조건을 검사합니다.
- [Dispatch Objects](https://developer.apple.com/documentation/dispatch/dispatch-objects): 모든 dispatch 타입이 지원하는 기본 동작입니다.
:::

:::topic-grid
## 사용 중단
- [Deprecated Symbols](https://developer.apple.com/documentation/dispatch/deprecated-symbols)
:::

:::topic-grid
## 클래스
- [DispatchWorkloop](https://developer.apple.com/documentation/dispatch/dispatchworkloop)
:::

:::topic-grid
## 레퍼런스
- [Dispatch Constants](https://developer.apple.com/documentation/dispatch/dispatch-constants)
- [Dispatch Data Types](https://developer.apple.com/documentation/dispatch/dispatch-data-types)
- [Dispatch Functions](https://developer.apple.com/documentation/dispatch/dispatch-functions)
:::
