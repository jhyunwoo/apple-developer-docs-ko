---
route: /documentation/XCUIAutomation
source_url: https://developer.apple.com/documentation/XCUIAutomation
source_locale: en-US
section: docc
content_type: symbol
title: XCUIAutomation
original_title: XCUIAutomation
source_hash: 8cf1d5f0f148927505231d9261c4559e48dfa455d97ea283acb1814af886a901
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:29:46+00:00'
last_translated_at: '2026-03-13T20:10:00+09:00'
---

# XCUIAutomation

상호 작용 시퀀스를 재현하고 앱의 사용자 인터페이스가 의도한 대로 동작하는지 확인합니다.

## 개요

UI 테스트를 사용하면 앱의 데이터 모델 일부를 변경했을 때 앱의 view controller, view, control이 적절하게 반응하는지 검증할 수 있습니다. 또한 사람이 인터페이스와 상호 작용하는 것처럼 앱의 view와 control을 조작하는 테스트 케이스를 만들 수도 있습니다. XCUIAutomation 프레임워크를 사용해 앱의 사용자 인터페이스를 제어하고 상태를 검사하십시오. [XCTest](https://developer.apple.com/documentation/XCTest)를 사용해 XCUIAutomation으로 앱을 제어하는 테스트를 작성하고, 앱의 상태가 기대와 일치하는지 확인하십시오.

:::note 참고
UI 테스트는 visionOS SDK로 빌드한 앱에서는 사용할 수 없습니다. 하지만 iOS SDK로 빌드하고 visionOS에서 실행하는 호환 iPad 및 iPhone 앱을 테스트하는 데는 여전히 사용할 수 있습니다.
:::

:::topic-grid
## 핵심 사항
- [Recording UI automation for testing](https://developer.apple.com/documentation/xcuiautomation/recording-ui-automation-for-testing): 상호 작용 시퀀스를 캡처하고 재생하여 앱 동작을 검증합니다.
:::

:::topic-grid
## UI 요소 쿼리
- [XCUIElementQuery](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery): 테스트가 UI 요소를 식별하기 위해 사용하는 검색 기준을 정의하는 객체입니다.
- [XCUIElementTypeQueryProvider](https://developer.apple.com/documentation/xcuiautomation/xcuielementtypequeryprovider): 하위 UI 요소를 찾기 위한 미리 준비된 쿼리를 제공하는 타입입니다.
:::

:::topic-grid
## UI 요소
- [XCUIElement](https://developer.apple.com/documentation/xcuiautomation/xcuielement): 애플리케이션 안의 UI 요소입니다.
- [XCUIElementAttributes](https://developer.apple.com/documentation/xcuiautomation/xcuielementattributes): UI 요소가 노출하는 속성입니다.
- [XCUIElementSnapshot](https://developer.apple.com/documentation/xcuiautomation/xcuielementsnapshot): 요소 속성과 하위 사용자 인터페이스 계층 구조의 스냅샷을 표현하는 속성 집합입니다.
- [XCUIElementSnapshotProviding](https://developer.apple.com/documentation/xcuiautomation/xcuielementsnapshotproviding): 요소 속성과 하위 사용자 인터페이스 계층 구조의 스냅샷을 캡처하는 메서드입니다.
- [XCUICoordinate](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate): UI 요소를 기준으로 한 화면상의 위치입니다.
:::

:::topic-grid
## 애플리케이션 수명 주기
- [XCUIApplication](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication): 테스트 대상 애플리케이션을 실행하고, 모니터링하고, 종료할 수 있는 프록시입니다.
:::

:::topic-grid
## 스크린샷
- [XCUIScreen](https://developer.apple.com/documentation/xcuiautomation/xcuiscreen): 기기에 연결된 물리적 화면입니다.
- [XCUIScreenshot](https://developer.apple.com/documentation/xcuiautomation/xcuiscreenshot): 화면, 앱 또는 UI 요소 상태를 캡처한 이미지입니다.
- [XCUIScreenshotProviding](https://developer.apple.com/documentation/xcuiautomation/xcuiscreenshotproviding): 현재 UI 상태의 스크린샷을 제공할 수 있는 타입입니다.
:::

:::topic-grid
## 기기 시뮬레이션
- [XCUIDevice](https://developer.apple.com/documentation/xcuiautomation/xcuidevice): iOS, watchOS, tvOS 기기에 대해 물리 버튼, 기기 방향, Siri 상호 작용을 시뮬레이션할 수 있는 프록시입니다.
- [XCUISystem](https://developer.apple.com/documentation/xcuiautomation/xcuisystem): OS별 속성과 동작에 대한 인터페이스를 제공하는 프록시입니다.
- [XCUISiriService](https://developer.apple.com/documentation/xcuiautomation/xcuisiriservice): 기기의 Siri 인터페이스를 시뮬레이션하는 프록시입니다.
:::

:::topic-grid
## 리모컨 시뮬레이션
- [XCUIRemote](https://developer.apple.com/documentation/xcuiautomation/xcuiremote): 물리 리모컨과의 상호 작용을 시뮬레이션하는 클래스입니다.
:::

:::topic-grid
## UI 테스트 가용성
- [XCUI_UI_TESTING_AVAILABLE](https://developer.apple.com/documentation/xcuiautomation/xcui_ui_testing_available): 현재 환경이 UI 테스트를 지원하는지 나타냅니다.
:::
