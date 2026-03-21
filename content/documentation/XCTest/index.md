---
route: /documentation/XCTest
source_url: https://developer.apple.com/documentation/XCTest
source_locale: en-US
section: docc
content_type: symbol
title: XCTest
original_title: XCTest
source_hash: a27e3ae3f076a6ffd61c8364277238ba11e6c2c54f3327199181db10e19a947b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:18:00+00:00'
last_translated_at: '2026-03-13T23:18:11+09:00'
---

# XCTest

Xcode 프로젝트를 위한 단위 테스트, 성능 테스트, UI 테스트를 만들고 실행합니다.

## 개요

XCTest 프레임워크를 사용하면 Xcode의 테스트 워크플로와 자연스럽게 통합되는 단위 테스트를 작성할 수 있습니다.

테스트는 코드 실행 중 특정 조건이 만족되는지 검증하고, 그 조건이 만족되지 않으면 테스트 실패를 기록합니다. 필요하다면 메시지도 함께 기록할 수 있습니다. 테스트는 코드 블록의 성능을 측정해 성능 회귀 여부를 확인할 수도 있습니다. XCTest를 [XCUIAutomation](https://developer.apple.com/documentation/XCUIAutomation)과 함께 사용하면 앱의 UI와 상호 작용하면서 사용자 상호 작용 흐름을 검증할 수 있습니다. 자세한 내용은 [Recording UI automation for testing](https://developer.apple.com/documentation/XCUIAutomation/recording-ui-automation-for-testing)을 참고하십시오.

:::tip Tip
Xcode 16 이상에는 Swift 프로그래밍 언어의 강력한 기능을 활용하는 단위 테스트 프레임워크인 Swift Testing이 포함되어 있습니다. 새로운 단위 테스트는 Swift Testing 사용을 고려하고, 기존 테스트는 [Migrating a test from XCTest](https://developer.apple.com/documentation/Testing/MigratingFromXCTest)에서 설명하는 방식으로 마이그레이션할 수 있습니다. 하나의 테스트 target 안에는 Swift Testing과 XCTest를 모두 포함할 수 있지만, 같은 테스트 안에서 두 프레임워크의 API를 섞어 사용하지는 마십시오. 사용자 인터페이스 테스트와 [Performance Tests](https://developer.apple.com/documentation/xctest/performance-tests)는 계속 XCTest를 사용하십시오.
:::

:::topic-grid
## 테스트 케이스와 테스트 메서드
- [Defining Test Cases and Test Methods](https://developer.apple.com/documentation/xctest/defining-test-cases-and-test-methods): 코드가 기대한 대로 동작하는지 확인하기 위해 테스트 케이스와 테스트 메서드를 test target에 추가합니다.
- [XCTestCase](https://developer.apple.com/documentation/xctest/xctestcase): 테스트 케이스, 테스트 메서드, 성능 테스트를 정의하는 기본 클래스입니다.
- [XCTest](https://developer.apple.com/documentation/xctest/xctest): 테스트를 생성, 관리, 실행하는 추상 기반 클래스입니다.
:::

:::topic-grid
## 테스트 단언
- [Boolean Assertions](https://developer.apple.com/documentation/xctest/boolean-assertions): true 또는 false 결과를 생성하는 조건을 테스트합니다.
- [Nil and Non-Nil Assertions](https://developer.apple.com/documentation/xctest/nil-and-non-nil-assertions): 테스트 조건이 값을 가지는지 또는 가지지 않는지 확인합니다.
- [Equality and Inequality Assertions](https://developer.apple.com/documentation/xctest/equality-and-inequality-assertions): 두 값이 같은지 또는 다른지 검사합니다.
- [Comparable Value Assertions](https://developer.apple.com/documentation/xctest/comparable-value-assertions): 두 값을 비교해 어느 쪽이 더 큰지 또는 더 작은지 판단합니다.
- [Error Assertions](https://developer.apple.com/documentation/xctest/error-assertions): 함수 호출이 오류를 던지는지 또는 던지지 않는지 확인합니다.
- [NSException Assertions](https://developer.apple.com/documentation/xctest/nsexception-assertions): 함수 호출이 예외를 던지는지 또는 던지지 않는지 확인합니다.
- [Unconditional Test Failures](https://developer.apple.com/documentation/xctest/unconditional-test-failures): 즉시 그리고 무조건적으로 실패를 생성합니다.
- [Expected Failures](https://developer.apple.com/documentation/xctest/expected-failures): 알려진 테스트 실패를 예상해 워크플로에 영향을 주지 않도록 합니다.
- [Methods for Skipping Tests](https://developer.apple.com/documentation/xctest/methods-for-skipping-tests): 지정한 조건을 만족할 때 테스트를 건너뜁니다.
:::

:::topic-grid
## 비동기 테스트
- [Asynchronous Tests and Expectations](https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations): 비동기 코드가 기대한 대로 동작하는지 검증합니다.
:::

:::topic-grid
## UI 테스트
- [XCUIAutomation](https://developer.apple.com/documentation/XCUIAutomation): 상호 작용 시퀀스를 재현하고 앱의 사용자 인터페이스가 의도대로 동작하는지 확인합니다.
:::

:::topic-grid
## 성능 테스트
- [Performance Tests](https://developer.apple.com/documentation/xctest/performance-tests): 코드 실행 중 metric을 수집하고, 그 metric이 기준값보다 유의미하게 나빠지면 실패를 보고합니다.
:::

:::topic-grid
## 활동 및 첨부 자료
- [Activities and Attachments](https://developer.apple.com/documentation/xctest/activities-and-attachments): 긴 테스트를 activity로 세분화하고 파일과 스크린샷 같은 출력 데이터를 첨부합니다.
:::

:::topic-grid
## 테스트 실행
- [Test Execution and Observation](https://developer.apple.com/documentation/xctest/test-execution-and-observation): 테스트 실행 흐름을 관찰하고, 내부를 들여다보고, 사용자화합니다.
:::

:::topic-grid
## 지원 중단
- [Deprecated Symbols](https://developer.apple.com/documentation/xctest/deprecated-symbols): 더 이상 권장되지 않는 지원 중단 심볼입니다.
:::

:::topic-grid
## 변수
- [XCT_UI_TESTING_AVAILABLE](https://developer.apple.com/documentation/xctest/xct_ui_testing_available)
:::

:::topic-grid
## 함수
- [XCTAssertNoThrow(_:_:file:line:)](https://developer.apple.com/documentation/xctest/xctassertnothrow(_:_:file:line:)): 표현식이 오류를 던지지 않는다고 단언합니다.
:::
