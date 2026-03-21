---
route: /documentation/AppIntents
source_url: https://developer.apple.com/documentation/AppIntents
source_locale: en-US
section: docc
content_type: symbol
title: App Intents
original_title: App Intents
source_hash: a23f7b38298a467b3d1fba14c7edf530d97aab14b78051a42c9ab98e9b7fd5a0
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:54:44+00:00'
last_translated_at: '2026-03-14T00:13:00+09:00'
---

# App Intents

Spotlight, 위젯, 단축어 앱 같은 시스템 경험에서 앱의 콘텐츠와 동작을 발견할 수 있게 만듭니다.

## 개요

App Intents 프레임워크는 Siri, Spotlight, 위젯, 컨트롤 등 플랫폼 전반의 시스템 경험과 앱의 동작 및 콘텐츠를 깊이 통합할 수 있는 기능을 제공합니다. Apple Intelligence와 App Intents의 향상 덕분에 Siri는 사용자가 앱의 기능을 발견하도록 앱의 동작을 제안할 수 있고, 앱 안팎에서 동작을 수행하는 능력도 얻게 됩니다.

![App Intents 프레임워크 아이콘을 보여 주는 대표 이미지입니다.](https://developer.apple.com)

App Intents 프레임워크를 채택하면 사용자는 다음과 같은 방식으로 앱 기능을 즉시 사용해 자신의 기기를 더 개인화할 수 있습니다.

- Apple Intelligence의 개인 맥락 인식과 동작 기능을 활용하는 상호 작용을 포함한 Siri와의 상호 작용
- Spotlight 제안 및 검색
- 단축어 앱의 동작과 자동화
- Action 버튼이나 Apple Pencil의 squeeze 제스처처럼 앱 동작을 시작하는 하드웨어 상호 작용
- 주의를 분산시키는 요소를 줄일 수 있도록 돕는 Focus

:::note 참고
Siri의 개인 맥락 이해, 화면 인식, 앱 내 동작은 현재 개발 중이며 향후 소프트웨어 업데이트에서 제공될 예정입니다.
:::

예를 들어 App Intents를 사용하면 App Shortcut을 제공해 앱의 동작을 표현할 수 있습니다. 그러면 사용자는 앱 안에 있든 시스템의 다른 위치에 있든 Siri에게 해당 동작을 대신 수행해 달라고 요청할 수 있습니다. 또한 App Entities를 사용해 앱의 콘텐츠를 Spotlight와 Apple Intelligence의 시맨틱 인덱싱에 노출할 수 있습니다. 그러면 예를 들어 여행 앱의 항공편 정보를 Siri에게 불러오게 한 뒤 사랑하는 사람과 공유하도록 요청하는 식으로, 앱의 정보를 Siri가 가져오도록 할 수 있습니다.

이 구성 요소들은 다른 기술과 함께 재사용할 수 있어 앱과 그 기능을 더욱 쉽게 발견하고 더 널리 사용할 수 있는 추가 기능과 경험을 제공할 수 있습니다. 예를 들어 모듈식 App Intents 코드를 [WidgetKit](https://developer.apple.com/documentation/WidgetKit)과 함께 재사용해 다음을 제공할 수 있습니다.

- 상호 작용형 위젯
- 컨트롤
- Live Activities

App Intents 프레임워크가 가능하게 하는 기능과 프레임워크를 가장 잘 채택하는 방법을 자세히 알아보려면 [Making actions and content discoverable and widely available](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-and-widely-available)를 참고하십시오.

디자인 가이드는 [Human Interface Guidelines > App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts), [Human Interface Guidelines > Siri](https://developer.apple.com/design/human-interface-guidelines/siri), [Human Interface Guidelines > Action Button](https://developer.apple.com/design/human-interface-guidelines/action-button)을 참고하십시오.

:::topic-grid
## 핵심 사항
- [App Intents updates](https://developer.apple.com/documentation/Updates/AppIntents): App Intents의 중요한 변경 사항을 알아봅니다.
- [Making actions and content discoverable and widely available](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-and-widely-available): Spotlight, 컨트롤, 위젯, Action 버튼에서 앱을 발견할 수 있도록 App Intents를 채택합니다.
:::

:::topic-grid
## 시스템 경험
- [Adopting App Intents to support system experiences](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences): Spotlight, visual intelligence, 단축어 같은 시스템 경험에 통합할 app intents와 entities를 만듭니다.
- [Making app entities available in Spotlight](https://developer.apple.com/documentation/appintents/making-app-entities-available-in-spotlight): Spotlight 인덱싱을 지원하도록 앱 entity 타입에 annotation을 추가하고, entity를 donation하여 검색에서 찾을 수 있게 합니다.
- [Launching your voice-based conversational app from the side button of iPhone](https://developer.apple.com/documentation/appintents/launching-your-voice-based-conversational-app-from-the-side-button-of-iphone): 일본의 사용자가 iPhone의 측면 버튼을 구성해 음성 기반 대화형 앱을 실행할 수 있게 합니다.
- [Siri](https://developer.apple.com/documentation/appintents/siri): 앱을 Siri 및 Apple Intelligence와 통합해 음성 명령, 검색, 기타 시스템 경험으로 작업을 수행하게 합니다.
- [Visual intelligence](https://developer.apple.com/documentation/appintents/visual-intelligence): 앱을 visual intelligence와 통합하고 앱의 콘텐츠를 검색 결과에 포함합니다.
- [App Shortcuts](https://developer.apple.com/documentation/appintents/app-shortcuts): 지원되는 iPhone 및 Apple Watch 모델에서 앱의 intents와 entities를 단축어 앱, Siri, Spotlight, Action 버튼과 통합합니다.
- [Widgets, Live Activities, and controls](https://developer.apple.com/documentation/appintents/widgets-and-live-activities): app intents를 사용해 위젯과 Live Activities를 상호 작용형으로 만들고, 컨트롤을 제공하며, Smart Stack에서 위젯을 제안합니다.
- [Action button on iPhone and Apple Watch](https://developer.apple.com/documentation/appintents/actionbutton): iPhone의 Action 버튼으로 App Shortcuts를 실행하거나 Apple Watch의 Action 버튼으로 앱의 운동 또는 다이브 세션을 시작할 수 있게 합니다.
- [Focus](https://developer.apple.com/documentation/appintents/focus): 현재 Focus가 바뀔 때 앱의 동작을 조정하고 들어오는 알림을 필터링합니다.
:::

:::topic-grid
## 동작
- [Accelerating app interactions with App Intents](https://developer.apple.com/documentation/appintents/acceleratingappinteractionswithappintents): Siri, Spotlight, 단축어를 통해 사용자가 앱 기능을 빠르게 사용할 수 있게 합니다.
- [Creating your first app intent](https://developer.apple.com/documentation/appintents/creating-your-first-app-intent): Spotlight나 단축어 앱 같은 시스템 경험에서 앱을 사용할 수 있게 만드는 첫 app intent를 만듭니다.
- [App intents](https://developer.apple.com/documentation/appintents/app-intents): 특화된 intents를 사용해 시스템에 노출할 사용자 정의 동작을 정의합니다.
- [App intent domains](https://developer.apple.com/documentation/appintents/app-intent-domains): assistant schema를 사용해 앱의 동작과 콘텐츠를 Siri 및 Apple Intelligence에서 사용할 수 있게 합니다.
- [Intent infrastructure](https://developer.apple.com/documentation/appintents/intent-infrastructure): intent에 보조 문맥을 제공하고, 여러 앱에서 app intents를 재사용할 수 있는 기반 구조를 만듭니다.
:::

:::topic-grid
## 매개변수 및 데이터 타입
- [Adding parameters to an app intent](https://developer.apple.com/documentation/appintents/adding-parameters-to-an-app-intent): 사용자가 사용자 정의 입력 값으로 app intent를 구성할 수 있게 합니다.
- [Parameter resolution](https://developer.apple.com/documentation/appintents/parameter-resolution): app intent에 필요한 매개변수를 정의하고 런타임에 그 매개변수를 해석하는 방법을 지정합니다.
- [Resolvers](https://developer.apple.com/documentation/appintents/resolvers): app intent의 매개변수를 해석하고, 표준 해석 타입을 앱의 사용자 정의 타입까지 확장합니다.
- [Common data types](https://developer.apple.com/documentation/appintents/common-data-types): 통화, 파일, 연락처를 포함해 앱이 지원하는 공통 타입을 지정합니다.
- [App entities](https://developer.apple.com/documentation/appintents/app-entities): 핵심 타입이나 개념을 app entities로 선언해 시스템이 발견할 수 있게 만듭니다.
- [Static parameter types](https://developer.apple.com/documentation/appintents/app-enums): 정적인 매개변수 값 목록을 나타내는 타입입니다.
- [Entity queries](https://developer.apple.com/documentation/appintents/entity-queries): 시스템이 앱이 정의한 entities를 찾고, 이를 사용해 매개변수를 해석하도록 돕습니다.
- [Property comparators](https://developer.apple.com/documentation/appintents/property-comparators): 프로퍼티 일치 쿼리 중 수행할 비교 유형을 지정합니다.
:::

:::topic-grid
## 결과
- [Displaying static and interactive snippets](https://developer.apple.com/documentation/appintents/displaying-static-and-interactive-snippets): 사용자가 app intent의 결과를 보고 즉시 후속 동작을 수행할 수 있게 합니다.
- [IntentDialog](https://developer.apple.com/documentation/appintents/intentdialog): 값을 요청하거나, 후보를 구분하거나, 동작을 확인할 때 시스템이 표시하거나 읽어 줄 텍스트입니다.
- [IntentResult](https://developer.apple.com/documentation/appintents/intentresult): 동작 수행 결과를 담고, 호출자에게 돌려보낼 선택적 정보를 포함하는 타입입니다.
- [IntentResultContainer](https://developer.apple.com/documentation/appintents/intentresultcontainer): 완료된 intent의 출력을 나타내는 객체입니다.
- [OpensIntent](https://developer.apple.com/documentation/appintents/opensintent): 동작 수행 결과로 action의 호출자에게 app intent를 전달합니다.
- [ProvidesDialog](https://developer.apple.com/documentation/appintents/providesdialog): 동작 수행 결과로 action의 호출자에게 대화문을 전달합니다.
- [ReturnsValue](https://developer.apple.com/documentation/appintents/returnsvalue): 동작 수행 결과로 호출자에게 값을 전달합니다.
- [ShowsSnippetIntent](https://developer.apple.com/documentation/appintents/showssnippetintent): 규약을 준수하는 타입이 생성한 snippet을 표시하는 동작 수행 결과입니다.
- [ShowsSnippetView](https://developer.apple.com/documentation/appintents/showssnippetview): 동작 수행 결과로 action의 호출자에게 view를 전달합니다.
- [ResultsCollection](https://developer.apple.com/documentation/appintents/resultscollection): 섹션 구분을 지원하는 반환 항목 컬렉션을 나타내는 프로토콜입니다.
:::

:::topic-grid
## 선택 및 확인
- [IntentChoiceOption](https://developer.apple.com/documentation/appintents/intentchoiceoption): app intent가 다시 동작을 이어 가기 전에 사용자가 고를 수 있는 옵션 목록의 항목을 나타내는 구조체입니다.
- [ConfirmationConditions](https://developer.apple.com/documentation/appintents/confirmationconditions): 확인 요청에 대한 조건입니다.
:::

:::topic-grid
## 탐색 및 앱 실행
- [AppIntentSceneDelegate](https://developer.apple.com/documentation/appintents/appintentscenedelegate): 특정 scene을 대상으로 하는 AppIntent 호출을 처리하려면 이 프로토콜을 `UIScene` delegate에 구현합니다.
- [IntentModes](https://developer.apple.com/documentation/appintents/intentmodes): app intent의 동작을 설명하는 옵션 집합입니다.
- [CustomURLRepresentationParameterConvertible](https://developer.apple.com/documentation/appintents/customurlrepresentationparameterconvertible)
:::

:::topic-grid
## SiriKit 마이그레이션
- [Soup Chef with App Intents: Migrating custom intents](https://developer.apple.com/documentation/SiriKit/soup-chef-with-app-intents-migrating-custom-intents): App Intents를 통합해 앱의 동작을 Siri와 단축어에 제공합니다.
- [CustomIntentMigratedAppIntent](https://developer.apple.com/documentation/appintents/customintentmigratedappintent): 기존 SiriKit 사용자 정의 intent를 대체해, 이미 존재하는 shortcut과 donation이 계속 작동하도록 하는 인터페이스입니다.
:::

:::topic-grid
## 오류
- [AppIntentError](https://developer.apple.com/documentation/appintents/appintenterror): intent 처리 코드가 app intent를 해석하거나 실행하는 동안 문제를 나타내기 위해 반환할 수 있는 오류입니다.
:::

:::topic-grid
## 프로토콜
- [UndoableIntent](https://developer.apple.com/documentation/appintents/undoableintent)
:::

:::topic-grid
## 열거형
- [VideoCategory](https://developer.apple.com/documentation/appintents/videocategory)
:::
