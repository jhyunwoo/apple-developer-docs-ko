---
route: /documentation/Translation
source_url: https://developer.apple.com/documentation/Translation
source_locale: en-US
section: docc
content_type: symbol
title: Translation
original_title: Translation
source_hash: 539414e8b1a7630b71fe8d6110f936077b4b52d7ed07031e28333904bb901767
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:22:49+00:00'
last_translated_at: '2026-03-13T09:02:00+00:00'
---

# Translation

앱 안의 텍스트를 한 언어에서 다른 언어로 번역합니다.

## 개요

Translation 프레임워크를 사용해 앱 내 번역 기능을 제공하세요. 내장된 UI를 사용하면 시스템이 사용자를 대신해 번역을 제안하도록 할 수 있습니다. 또는 프레임워크를 사용해 번역 경험을 사용자화할 수 있습니다.

![번역을 보여 주는 개념 이미지입니다.](https://developer.apple.com)

내장된 시스템 번역 경험을 제공하려면 번역할 텍스트가 들어 있는 SwiftUI 뷰에 [translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)](https://developer.apple.com/documentation/SwiftUI/View/translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)) 뷰 modifier를 연결하세요. 내장 시스템 번역 UI를 표시하려는 시점에 `isPresented`를 `true`로 설정합니다. 번역할 텍스트는 `text` 매개변수로 전달합니다.

번역 경험을 사용자화하려면 [translationTask(_:action:)](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:)) 같은 translation task를 사용하세요. 이 함수들은 [TranslationSession](https://developer.apple.com/documentation/translation/translationsession)을 제공하며, 이를 이용해 텍스트 문자열을 하나씩 또는 일괄로 번역할 수 있습니다. 번역 기능을 제공하기 전에 [LanguageAvailability](https://developer.apple.com/documentation/translation/languageavailability) 클래스를 사용해 언어 지원 여부를 확인할 수 있습니다.

:::topic-grid
## 필수 항목
- [앱 내 텍스트 번역하기](https://developer.apple.com/documentation/translation/translating-text-within-your-app): 단순한 시스템 번역을 표시하고 사용자 정의 번역 경험을 만듭니다.
- [translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)](https://developer.apple.com/documentation/SwiftUI/View/translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)): 지정한 조건이 참일 때 번역 팝오버를 표시합니다.
- [translationTask(_:action:)](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:)): 이 뷰가 나타나기 전이나 번역 구성이 바뀔 때 수행할 task를 추가합니다.
- [translationTask(source:target:action:)](https://developer.apple.com/documentation/SwiftUI/View/translationTask(source:target:action:)): 이 뷰가 나타나기 전이나 지정한 원본 또는 대상 언어가 바뀔 때 수행할 task를 추가합니다.
- [TranslationSession](https://developer.apple.com/documentation/translation/translationsession): 한 쌍의 언어 사이에서 번역을 수행하는 클래스입니다.
:::

:::topic-grid
## 사용 가능 여부
- [LanguageAvailability](https://developer.apple.com/documentation/translation/languageavailability): 언어 지원 및 상태를 확인합니다.
:::

:::topic-grid
## 오류
- [TranslationError](https://developer.apple.com/documentation/translation/translationerror): 프레임워크가 번역을 수행할 수 없는 이유를 설명하는 오류 코드입니다.
:::
