---
route: /documentation/RelevanceKit
source_url: https://developer.apple.com/documentation/RelevanceKit
source_locale: en-US
section: docc
content_type: symbol
title: RelevanceKit
original_title: RelevanceKit
source_hash: d96e7abe9efe8f9cd44b1cfdeb2007530920ed173c74ea75de5d61efe1245c98
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:11:23+00:00'
last_translated_at: '2026-03-13T23:11:40+09:00'
---

# RelevanceKit

Apple Watch에서 위젯의 노출도를 높여 주는 맥락 단서로 기기 내 지능을 제공합니다.

## 개요

Apple Watch에서는 사람의 현재 맥락에 가장 잘 맞도록 Smart Stack 안의 위젯 순서가 정해집니다. watchOS는 Smart Stack에 표시할 위젯의 순서를 정하기 위해, 앱이 시스템에 제공하는 맥락 단서를 포함한 여러 요소를 바탕으로 위젯의 관련성을 판단하려고 시도합니다.

watchOS Smart Stack에서 위젯이 더 잘 보이게 하고, 사람이 필요로 하는 순간에 나타나도록 하려면 RelevanceKit을 사용해 위젯의 관련성을 시스템에 알리는 맥락 단서를 제공하십시오. 예를 들어 위젯은 특정 위치나 시간에 가장 유용할 수도 있고, 사람이 운동을 시작할 때마다 유용할 수도 있습니다.

대화형이면서 맥락에 맞는 Smart Stack 위젯을 제공하려면 RelevanceKit을 [WidgetKit](https://developer.apple.com/documentation/WidgetKit), [App Intents](https://developer.apple.com/documentation/AppIntents)와 함께 사용해야 합니다. 여기에는 Apple Watch에 표시되는 iPhone 위젯도 포함됩니다. 코드에 App Intents용 import 구문을 추가하면 App Intents가 RelevanceKit에 대한 의존성을 암묵적으로 추가합니다. 따라서 코드에 `import RelevanceKit`을 명시적으로 추가할 필요는 없습니다.

자세한 내용은 [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks)를 참고하십시오.

:::note Note
Smart Stack은 iOS, iPadOS, watchOS에서 사용할 수 있습니다. 그러나 RelevanceKit이 제공하는 기능은 watchOS에서만 사용할 수 있습니다. 다른 플랫폼에서 API를 호출해도 아무 효과가 없습니다.
:::

:::topic-grid
## 관련성 정보 제공
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks): 위젯이 Smart Stack에서 눈에 잘 띄게 표시되도록 맥락 정보를 제공하고 intent를 시스템에 기부합니다.
- [RelevantContext](https://developer.apple.com/documentation/relevancekit/relevantcontext): 시스템이 watchOS의 Smart Stack에서 관련성 높은 위젯을 보여 줄 때 사용하는 맥락 단서입니다.
:::

:::topic-grid
## 피트니스 단서
- [fitness(_:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/fitness(_:)): 사람의 피트니스 활동 때문에 위젯이 관련성이 있음을 시스템에 알립니다.
- [RelevantContext.FitnessCondition](https://developer.apple.com/documentation/relevancekit/relevantcontext/fitnesscondition): 사람의 피트니스 활동을 나타내는 값입니다.
:::

:::topic-grid
## 하드웨어 단서
- [hardware(headphones:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/hardware(headphones:)): 사람의 헤드폰이 연결되어 있을 때 위젯이 관련성이 있음을 시스템에 알립니다.
- [RelevantContext.HeadphonesCondition](https://developer.apple.com/documentation/relevancekit/relevantcontext/headphonescondition): 사람의 헤드폰 연결 여부를 나타내는 구조체입니다.
:::

:::topic-grid
## 위치 단서
- [location(_:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/location(_:)): 특정 위치에서 위젯이 관련성이 있음을 시스템에 알립니다.
- [location(inferred:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/location(inferred:)): 추정된 위치에서 위젯이 관련성이 있음을 시스템에 알립니다.
- [RelevantContext.InferredLocation](https://developer.apple.com/documentation/relevancekit/relevantcontext/inferredlocation): 사람의 집, 직장, 학교, 통근 위치에 대한 추정값을 담는 구조체입니다.
:::

:::topic-grid
## 수면 단서
- [sleep(_:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/sleep(_:)): 사람의 수면 일정 때문에 위젯이 관련성이 있음을 시스템에 알립니다.
- [RelevantContext.SleepCondition](https://developer.apple.com/documentation/relevancekit/relevantcontext/sleepcondition): 사람이 보통 잠드는 시간이나 기상 시간을 나타내는 값입니다.
:::

:::topic-grid
## 시간 단서
- [date(_:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(_:)): 특정 날짜에 위젯이 관련성이 있음을 시스템에 알립니다.
- [date(_:kind:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(_:kind:)): 특정 날짜에 위젯이 관련성이 있음을 알리고 추가적인 맥락 힌트도 제공합니다.
- [date(interval:kind:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(interval:kind:)): 일정 시간 구간 동안 위젯이 관련성이 있음을 알리고 추가적인 맥락 힌트를 제공합니다.
- [date(range:kind:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(range:kind:)): 알려진 날짜 범위 동안 위젯이 관련성이 있음을 알리고 추가적인 맥락 힌트를 제공합니다.
- [RelevantContext.DateKind](https://developer.apple.com/documentation/relevancekit/relevantcontext/datekind): 시스템이 시간 기반 관련성 단서의 추가 맥락으로 사용하는 값입니다.
- [date(from:to:)](https://developer.apple.com/documentation/relevancekit/relevantcontext/date(from:to:)): 두 날짜 사이에 위젯이 관련성이 있음을 시스템에 알립니다.
:::
