---
route: /documentation/Synchronization
source_url: https://developer.apple.com/documentation/Synchronization
source_locale: en-US
section: docc
content_type: symbol
title: Synchronization
original_title: Synchronization
source_hash: b39e6efeddcaff45083a275cf43a39f44c73228bbfb50f86f469197efeac22d4
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:55:52+00:00'
last_translated_at: '2026-03-13T16:05:00+09:00'
---

# Synchronization

저수준의 원시 연산을 사용해 동기화 구성 요소를 만듭니다.

:::topic-grid
## 원자적 값
- [Atomic](https://developer.apple.com/documentation/synchronization/atomic): 원자적 값입니다.
- [AtomicLazyReference](https://developer.apple.com/documentation/synchronization/atomiclazyreference): 지연 초기화 가능한 원자적 strong reference입니다.
- [WordPair](https://developer.apple.com/documentation/synchronization/wordpair): word 크기 두 개로 이루어진 쌍입니다.
- [AtomicRepresentable](https://developer.apple.com/documentation/synchronization/atomicrepresentable): 별도의 원자적 저장 표현을 통해 원자적 연산을 지원하는 타입입니다.
- [AtomicOptionalRepresentable](https://developer.apple.com/documentation/synchronization/atomicoptionalrepresentable): `Optional`로 감쌌을 때도 원자적 연산을 지원하는 원자적 값입니다. atomic optional representable 타입은 optional로 감싼 변형에 대해 독립적인 원자적 표현을 제공합니다.
:::

:::topic-grid
## 메모리 순서 의미 체계
- [AtomicLoadOrdering](https://developer.apple.com/documentation/synchronization/atomicloadordering): 원자적 load 연산의 메모리 순서 의미 체계를 지정합니다.
- [AtomicStoreOrdering](https://developer.apple.com/documentation/synchronization/atomicstoreordering): 원자적 store 연산의 메모리 순서 의미 체계를 지정합니다.
- [AtomicUpdateOrdering](https://developer.apple.com/documentation/synchronization/atomicupdateordering): 원자적 read-modify-write 연산의 메모리 순서 의미 체계를 지정합니다.
- [atomicMemoryFence(ordering:)](https://developer.apple.com/documentation/synchronization/atomicmemoryfence(ordering:)): 특정 원자적 연산과 연결하지 않고 메모리 순서를 설정합니다.
:::

:::topic-grid
## 구조체
- [Mutex](https://developer.apple.com/documentation/synchronization/mutex): 상호 배제를 통해 공유 가능한 가변 상태를 보호하는 동기화 원시 구성 요소입니다.
:::
