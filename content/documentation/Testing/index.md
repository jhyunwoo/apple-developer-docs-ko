---
route: /documentation/Testing
source_url: https://developer.apple.com/documentation/Testing
source_locale: en-US
section: docc
content_type: symbol
title: Swift Testing
original_title: Swift Testing
source_hash: 4791463828972ac44aaccea783b25e7749944d69ca3db1be5996cdde20a606bd
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:42:57+00:00'
last_translated_at: '2026-03-13T23:42:57+09:00'
---

# Swift Testing

Swift package와 Xcode 프로젝트를 위한 테스트를 만들고 실행합니다.

## 개요

Swift Testing을 사용하면 Swift 프로그래밍 언어의 강력하고 표현력 있는 기능을 활용해 더 큰 자신감으로, 더 적은 코드로 테스트를 개발할 수 있습니다. 이 라이브러리는 Swift Package Manager의 테스트 워크플로와 자연스럽게 통합되며, 유연한 테스트 구성, 사용자화 가능한 메타데이터, 확장 가능한 테스트 실행을 지원합니다.

- 단 하나의 attribute만으로 거의 어디서나 테스트 함수를 정의할 수 있습니다.
- Swift의 타입 시스템을 사용해 관련 테스트를 계층 구조로 묶을 수 있습니다.
- Swift concurrency와 자연스럽게 통합됩니다.
- 폭넓은 입력 범위에 걸쳐 테스트 함수를 parameterize할 수 있습니다.
- 런타임 조건에 따라 테스트를 동적으로 활성화할 수 있습니다.
- 프로세스 내부에서 테스트를 병렬화할 수 있습니다.
- tag를 사용해 테스트를 분류할 수 있습니다.
- 수정 사항을 검증하거나 문제를 재현하는 테스트에 bug를 직접 연결할 수 있습니다.

#### 관련 비디오

- [Meet Swift Testing](https://developer.apple.com/videos/play/wwdc2024/10179)
- [Go further with Swift Testing](https://developer.apple.com/videos/play/wwdc2024/10195)

:::topic-grid
## 핵심
- [테스트 함수 정의하기](https://developer.apple.com/documentation/testing/definingtests): 코드가 올바르게 동작하는지 검증하는 테스트 함수를 정의합니다.
- [suite 타입으로 테스트 함수 구성하기](https://developer.apple.com/documentation/testing/organizingtests): 테스트를 test suite로 구성합니다.
- [XCTest에서 테스트 마이그레이션하기](https://developer.apple.com/documentation/testing/migratingfromxctest): XCTest로 작성한 기존 테스트 메서드나 테스트 클래스를 마이그레이션합니다.
- [Test(_:_:)](https://developer.apple.com/documentation/testing/test(_:_:)): 테스트를 선언합니다.
- [Test](https://developer.apple.com/documentation/testing/test): 테스트 또는 suite를 나타내는 타입입니다.
- [Suite(_:_:)](https://developer.apple.com/documentation/testing/suite(_:_:)): test suite를 선언합니다.
:::

:::topic-grid
## 테스트 parameterization
- [parameterized test 구현하기](https://developer.apple.com/documentation/testing/parameterizedtesting): 서로 다른 입력 매개변수를 지정해 하나의 테스트 함수에서 여러 test case를 생성합니다.
- [Test(_:_:arguments:)](https://developer.apple.com/documentation/testing/test(_:_:arguments:)-8kn7a): 값 컬렉션 하나에 대해 parameterized된 테스트를 선언합니다.
- [Test(_:_:arguments:_:) ](https://developer.apple.com/documentation/testing/test(_:_:arguments:_:)): 값 컬렉션 두 개에 대해 parameterized된 테스트를 선언합니다.
- [Test(_:_:arguments:)](https://developer.apple.com/documentation/testing/test(_:_:arguments:)-3rzok): 두 컬렉션을 zip한 값에 대해 parameterized된 테스트를 선언합니다.
- [CustomTestArgumentEncodable](https://developer.apple.com/documentation/testing/customtestargumentencodable): parameterized test에 전달된 인수를 어떻게 인코딩할지 사용자화하는 프로토콜입니다. 특정 인수만 실행할 때의 매칭에도 사용됩니다.
- [Test.Case](https://developer.apple.com/documentation/testing/test/case): parameterized된 `Test`에서 생성된 단일 test case입니다.
:::

:::topic-grid
## 동작 검증
- [Expectation과 confirmation](https://developer.apple.com/documentation/testing/expectations): 예상 값, 결과, 비동기 이벤트를 테스트 안에서 확인합니다.
- [Known issues](https://developer.apple.com/documentation/testing/known-issues): 테스트 실행 시 문제를 알려진 이슈로 표시합니다.
:::

:::topic-grid
## 테스트 사용자화
- [Traits](https://developer.apple.com/documentation/testing/traits): 테스트 함수와 suite에 annotation을 추가하고 동작을 사용자화합니다.
:::

:::topic-grid
## 데이터 수집
- [Attachments](https://developer.apple.com/documentation/testing/attachments): 문제 진단과 피드백 수집을 돕도록 테스트에 값을 첨부합니다.
:::
