---
route: /design/human-interface-guidelines/app-shortcuts
source_url: https://developer.apple.com/design/human-interface-guidelines/app-shortcuts
source_locale: ko-KR
section: hig
content_type: article
title: 앱 단축어
original_title: App Shortcuts
source_hash: 26144ac3ebda50156c6f2dc463e50c287103210db9c7c00af5c8d6e55c986f83
canonical_source: official-ko
last_crawled_at: '2026-03-13T15:12:49+00:00'
last_translated_at: '2026-03-14T00:12:46+09:00'
---

# 앱 단축어

앱 단축어를 통해 시스템 전반에서 앱의 주요 기능 또는 콘텐츠에 접근할 수 있습니다.

![새로운 메모를 생성하고 두 개의 다른 최근 메모를 열기 위한 앱 단축어와 함께 Spotlight의 가장 연관성 높은 항목 영역의 결과로 나타나는 스타일화된 메모 앱의 모양이 표시되어 있음. 여섯 가지 색상으로 된 기존 Apple 로고의 빨간색을 은은하게 반영하는 빨간색 색조가 이미지에 적용됨.](https://developer.apple.com)

앱 단축어는 [Siri](https://developer.apple.com/kr/design/human-interface-guidelines/siri), Spotlight, 단축어 앱과 같은 기능을 사용하거나, iPhone 또는 Apple Watch의 [동작 버튼](https://developer.apple.com/kr/design/human-interface-guidelines/action-button)과 같은 하드웨어 기능을 사용하거나, Apple Pencil을 [Apple Pencil 및 손글씨 입력](https://developer.apple.com/kr/design/human-interface-guidelines/apple-pencil-and-scribble#Squeeze)하여 실행할 수 있습니다.

앱 단축어는 앱의 일부이기 때문에 설치가 완료되자마자 사용할 수 있습니다. 예를 들어, 일기 쓰기 앱의 경우 앱을 처음 열기 전에 새로운 일기 입력 항목을 작성하는 앱 단축어를 제공할 수 있습니다. 앱을 사용하기 시작한 후에는 FaceTime에서 최근 연락처에 전화하는 것과 같이 앱 단축어에서 사람들의 선택 사항을 반영할 수 있습니다.

![FaceTime의 앱 단축어가 격자 보기로 나열되어 있는 iPhone 단축어 앱의 부분적 스크린샷. 앱 단축어는 레이블이 ‘최근 통화 대상에게 전화’인 그룹에 있으며, 각각의 제목은 최근 FaceTime 연락처의 이름임.](https://developer.apple.com)

앱 단축어는 [App Intents](https://developer.apple.com/documentation/AppIntents)를 사용하여 앱 내의 동작을 정의하고 시스템에서 사용할 수 있도록 만듭니다. 각각의 앱 단축어는 사람들이 작업을 완료하기 위해 수행하고자 하는 단계의 세트로 구성된 하나 이상의 동작을 포함합니다. 예를 들어, 홈 보안 앱은 취침 시 전등을 끄고 바깥 문을 잠그는 두 가지 일반적인 동작을 하나의 앱 단축어로 결합할 수 있습니다. 각각의 앱은 최대 10개의 앱 단축어를 포함할 수 있습니다.

:::note 참고
앱에서 제공하는 앱 단축어뿐만 아니라 App Intent를 사용하여 앱의 동작을 시스템에서 사용할 수 있도록 하는 경우, 사람들이 단축어 앱에서 동작을 결합하여 자신만의 사용자 설정 단축어를 만들 수도 있습니다. 사용자 설정 단축어를 통해 동작을 유연하게 구성하고, 여러 앱에 걸쳐 작업을 실행하는 작업흐름을 구현할 수 있습니다. 추가 지침을 보려면 [Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios)의 내용을 참조하십시오.
:::

## 모범 사례

**앱에서 가장 일반적이고 중요한 작업을 수행하는 앱 단축어를 제공하십시오.** 사람들이 현재 상태를 벗어나지 않고 완료할 수 있는 직접적인 작업이 가장 좋지만, 여러 단계의 작업을 더 쉽게 완료하는 데 도움이 된다면 앱을 열어도 괜찮습니다.

**옵션 세트를 선택할 수 있도록 하여 유연성을 높이십시오.** 적합한 경우 앱 단축어는 하나의 옵션 값, 즉 매개변수를 포함할 수 있습니다. 예를 들어, 명상 앱의 경우 특정 유형의 명상을 시작하는 “[아침, 일일, 수면] 명상 시작”과 같은 앱 단축어를 제공할 수 있습니다. 참고할 수 있는 목록이 앞에 표시되지 않기 때문에 예측 가능하고 친숙한 값을 옵션으로 포함하십시오. 개발자 지침을 보려면 [Adding parameters to an app intent](https://developer.apple.com/documentation/AppIntents/Adding-parameters-to-an-app-intent)의 내용을 참조하십시오.

![커피 앱에서 음료를 주문하는 단축어의 활성화 문구가 표시된 다이어그램. 활성화 문구에는 음료의 이름이 옵션 값으로 포함되어 있으며, 밑줄이 그어져 있고 단축어의 매개변수로 설명되어 있음.](https://developer.apple.com)

**옵션 정보가 누락된 요청의 경우 확인을 요청하십시오.** 예를 들어, 유형(아침, 일일, 수면)을 지정하지 않고 “명상 시작”이라고 말할 수 있습니다. 이 경우, 가장 최근에 사용한 항목 또는 현재 시간을 기반으로 이어서 제안할 수 있습니다. 가능성이 높은 한 가지 옵션이 있을 경우 이를 기본값으로 표시하는 것을 고려하십시오. 그리고 기본 선택이 마음에 들지 않을 경우에 대비하여 선택 가능한 대체 항목을 짧은 목록으로 제공하십시오.

**음성 상호작용을 간결하게 유지하십시오.** 문구를 소리 내어 말할 때 너무 복잡하게 느껴지는 경우, 문구를 기억하거나 올바로 말하기 어려울 수 있습니다. 예를 들어, ‘자연의 소리로 [수면] 명상 시작’은 명상 유형과 사운드가 두 개의 가능한 매개변수인 것처럼 보입니다. 추가 정보가 꼭 필요한 경우, 후속 단계에서 이를 요청하십시오. 음성 상호작용에 대한 대화 텍스트를 작성하는 것과 관련된 추가 지침을 보려면 [Siri](https://developer.apple.com/kr/design/human-interface-guidelines/siri)의 내용을 참조하십시오.

**앱에서 앱 단축어를 발견할 수 있도록 하십시오.** 단축어가 있다는 사실을 알게 되면 사람들은 자주 수행하는 작업에 대한 앱 단축어를 기억하고 사용할 것입니다. 앱 단축어가 있다는 것을 알 수 있도록 사람들이 일반적인 동작을 수행할 때 가끔씩 앱에 팁을 표시하는 것을 고려하십시오. 개발자 지침을 보려면 [SiriTipUIView](https://developer.apple.com/documentation/AppIntents/SiriTipUIView)의 내용을 참조하십시오.

### 앱 단축어에 응답하기

사람들이 앱 단축어를 사용할 때 앱은 Siri가 소리 내어 말하는 대화와 스니펫 및 실시간 현황과 같은 사용자 설정 시각 항목 등 다양한 방식으로 응답할 수 있습니다.

- 스니펫은 현재 위치의 날씨를 보거나 주문을 확인하는 등 정적인 정보 또는 대화 옵션을 표시하는 사용자 설정 보기에 적합합니다. 개발자 지침을 보려면 [ShowsSnippetView](https://developer.apple.com/documentation/AppIntents/ShowsSnippetView)의 내용을 참조하십시오.
- [실시간 현황](https://developer.apple.com/kr/design/human-interface-guidelines/live-activities)은 연관성이 유지되고 시간이 지나면서 값이 변할 가능성이 있는 정보에 대한 지속적인 접근을 제공하며, 이벤트가 완료될 때까지 표시되는 타이머 및 카운트다운에 적합합니다. 개발자 지침을 보려면 [LiveActivityIntent](https://developer.apple.com/documentation/AppIntents/LiveActivityIntent)의 내용을 참조하십시오.

**오디오 전용 기기에서의 상호작용을 위해 충분한 세부사항을 제공하십시오.** 사람들은 AirPods 및 HomePod과 같은 오디오 전용 기기에서 응답을 받을 수 있으며, 화면상의 콘텐츠를 보지 못할 수도 있습니다. 앱 단축어의 전체 대화 텍스트에 중요 정보를 모두 포함하십시오. 개발자 지침을 보려면 [init(full:supporting:systemImageName:)](https://developer.apple.com/documentation/AppIntents/IntentDialog/init(full:supporting:systemImageName:))의 내용을 참조하십시오.

## 편집 지침

**간결하고 기억하기 쉬운 활성화 문구 및 자연스러운 다른 표현을 제공하십시오.** 앱 단축어 문구(또는 정의한 다른 표현)는 Siri로 앱 단축어를 실행하기 위해 사람들이 말하는 내용이므로 간결하고 기억하기 쉽게 만드는 것이 중요합니다. 앱 이름을 포함해야 하지만 창의적으로 표현할 수 있습니다. 예를 들어, Keynote는 “Keynote 생성” 및 “Keynote에서 새 프레젠테이션 추가”를 모두 새 문서를 생성하는 앱 단축어 문구로 이해합니다. 개발자 지침을 보려면 [AppShortcutPhrase](https://developer.apple.com/documentation/AppIntents/AppShortcutPhrase)의 내용을 참조하십시오.

**앱 단축어(App Shortcuts) 또는 단축어(Shortcuts) 앱을 언급하는 경우, 항상 제목식 대문자 표기법을 사용하고 영문 표기 시에는 *복수형(Shortcuts)*을 사용하십시오.** 예를 들어, ‘*MyApp은 단축어(Shortcuts)와 통합되어 Siri에게 요청하거나 탭 한 번만으로 작업을 빠르게 완료할 수 있는 방법을 제공하며, 동작 버튼에 지정할 수 있는 앱 단축어(App Shortcuts)를 제공합니다.*’와 같이 표현하십시오.

**앱 단축어(App Shortcuts) 또는 단축어(Shortcuts) 앱이 아닌 개별 단축어(shortcut)를 언급할 때는 소문자를 사용하십시오.** 예를 들어, ‘*Siri에게 요청하거나 잠금 화면에서 제안을 탭하여 단축어(shortcut)를 실행하십시오*.’와 같이 표현하십시오.

## 플랫폼 고려 사항

*visionOS 또는 watchOS에 대한 추가 고려 사항은 없습니다. tvOS에서는 지원되지 않습니다.*

### iOS, iPadOS

앱 단축어는 사람들이 앱을 검색할 때 Spotlight의 가장 연관성 높은 항목 영역 또는 아래에 있는 단축어 영역에 나타날 수 있습니다. 각각의 앱 단축어에는 기능을 나타내도록 선택한 [SF Symbols](https://developer.apple.com/kr/design/human-interface-guidelines/sf-symbols)의 기호가 포함되어 있거나, 단축어가 직접 연결되는 항목의 미리보기 이미지가 포함되어 있습니다.

![iPhone의 Spotlight 검색 결과가 표시된 부분적 스크린샷. 화면 상단에 가장 연관성 높은 항목 영역이 있고 아래에 제안 영역이 있음. 메모 앱이 가장 연관성 높은 항목으로 나타나고 앱 아이콘 오른쪽에 앱 단축어가 연달아 나타남. 하나는 제목이 ‘새로운 메모’이고 정사각형 위에 연필이 대각선으로 있는 기호이고, 다른 하나는 제목이 ‘빠른 메모’이고 캔버스 위에 손으로 그린 선이 있는 기호이며, 나머지 하나는 포함된 이미지 썸네일과 함께 제목이 ‘자연’인 최근 메모가 나타난 모습임. 제안 영역에는 ‘메모’에 대한 웹 검색 링크가 포함되어 있고 ‘메모장’, ‘메모리’가 자동 완성 단어로 제안됨.](https://developer.apple.com)

**중요도에 따라 단축어를 정렬하십시오.** 지정된 단축어 순서는 Spotlight 및 단축어 앱에서 앱 단축어가 처음 나타나는 방식을 결정하므로 일반적으로 가장 유용한 항목을 먼저 포함하는 것이 도움이 됩니다. 사람들이 앱 단축어를 사용하기 시작하면 가장 자주 사용되는 항목이 우선적으로 표시되도록 시스템이 정보를 업데이트합니다.

**실시간 현황을 시작하는 앱 단축어를 제공하십시오.** 실시간 현황을 통해 사람들은 자신의 여러 기기에 걸쳐 한눈에 확인할 수 있는 위치에서 이벤트 또는 작업의 진행 상태를 추적할 수 있습니다. 예를 들어, 요리 앱은 요리를 오븐에서 꺼낼 준비가 될 때까지 남은 시간을 표시하는 실시간 현황을 제공할 수 있습니다. 사람들이 손쉽게 요리 타이머를 시작할 수 있도록 앱은 동작 버튼에 지정할 수 있는 앱 단축어를 제공합니다. 실시간 현황에 대한 자세한 정보는 [실시간 현황](https://developer.apple.com/kr/design/human-interface-guidelines/live-activities)의 내용을 참조하십시오.

### macOS

앱 단축어는 macOS에서 지원되지 않습니다. 하지만 App Intent를 사용하여 앱용으로 생성한 동작은 지원되며, 사람들은 Mac에서 단축어 앱으로 해당 동작을 사용하여 사용자 설정 단축어를 만들 수 있습니다.

## 리소스

#### 관련 콘텐츠

[Siri](https://developer.apple.com/kr/design/human-interface-guidelines/siri)

[Siri Style Guide](https://developer.apple.com/siri/style-guide/)

[Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios)

#### Developer 문서

[App Intents](https://developer.apple.com/documentation/AppIntents)

[SiriKit](https://developer.apple.com/documentation/SiriKit)

[Making actions and content discoverable and widely available](https://developer.apple.com/documentation/AppIntents/Making-actions-and-content-discoverable-and-widely-available) — App Intents

[Integrating custom data types into your intents](https://developer.apple.com/documentation/AppIntents/Integrating-custom-types-into-your-intents) — App Intents

#### 비디오

## 변경 기록

| 날짜 | 변경 사항 |
| --- | --- |
| 2025년 1월 17일 | 지침이 업데이트되고 간소화됨. |
| 2023년 6월 5일 | 새로운 페이지. |
