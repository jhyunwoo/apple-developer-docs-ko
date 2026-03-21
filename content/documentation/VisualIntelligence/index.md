---
route: /documentation/VisualIntelligence
source_url: https://developer.apple.com/documentation/VisualIntelligence
source_locale: en-US
section: docc
content_type: symbol
title: Visual Intelligence
original_title: Visual Intelligence
source_hash: 8851b8b12b2c7f0b6d62c14ff2ba5d5c7716f12199f73aac5a4340b96bee3030
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:21:34+00:00'
last_translated_at: '2026-03-13T23:21:47+09:00'
---

# Visual Intelligence

visual intelligence가 제공하는 검색 결과에 앱의 콘텐츠를 포함합니다.

## 개요

![다채로운 배경 앞에 있는 visual intelligence 아이콘입니다.](https://developer.apple.com)

사람들은 visual intelligence를 사용해 주변 장소와 물체, 그리고 화면 위의 대상을 더 잘 이해합니다. visual intelligence 카메라를 주변 환경에 비추고 검색 버튼을 탭하거나, 스크린샷 속 대상을 선택하면, visual intelligence와 통합된 앱 안의 일치하는 콘텐츠를 검색할 수 있습니다. 일치 항목은 visual intelligence 경험 안에 표시되며, 사용자는 항목을 보고 열거나, 해당 앱에서 더 많은 검색 결과를 확인할 수 있습니다. 예를 들어 랜드마크 정보를 제공하는 앱은 visual intelligence와 통합하여 사용자가 랜드마크 정보를 보거나 더 많은 정보를 위해 앱을 열 수 있게 할 수 있습니다.

앱을 visual intelligence와 통합하고 앱 콘텐츠를 검색 결과에 포함하려면 Visual Intelligence 프레임워크와 [App Intents](https://developer.apple.com/documentation/AppIntents)를 사용하십시오. Visual Intelligence 프레임워크는 visual intelligence가 캡처한 정보를 앱에 제공하고, 앱은 App Intents 프레임워크를 사용해 이 정보를 받아 시스템과 visual intelligence에 일치하는 콘텐츠를 반환합니다.

:::topic-grid
## 핵심
- [Integrating your app with visual intelligence](https://developer.apple.com/documentation/visualintelligence/integrating-your-app-with-visual-intelligence): visual intelligence를 사용해 주변 환경이나 화면 속 대상과 일치하는 앱 콘텐츠를 사람들이 찾을 수 있게 합니다.
- [Adopting App Intents to support system experiences](https://developer.apple.com/documentation/AppIntents/adopting-app-intents-to-support-system-experiences): Spotlight, visual intelligence, Shortcuts 같은 시스템 경험에 앱을 통합하기 위해 app intent와 entity를 만듭니다.
- [SemanticContentDescriptor](https://developer.apple.com/documentation/visualintelligence/semanticcontentdescriptor): 스크린샷, 사진, 사진 및 비디오 스트림처럼 visual intelligence가 캡처하는 장면을 나타내는 타입입니다.
:::

:::topic-grid
## App Intents 핵심
- [Making actions and content discoverable and widely available](https://developer.apple.com/documentation/AppIntents/Making-actions-and-content-discoverable-and-widely-available): Spotlight, control, widget, Action button으로 앱을 더 쉽게 발견할 수 있도록 App Intents를 채택합니다.
- [Creating your first app intent](https://developer.apple.com/documentation/AppIntents/Creating-your-first-app-intent): Spotlight나 Shortcuts 앱 같은 시스템 경험에 앱을 노출하는 첫 번째 app intent를 만듭니다.
:::
