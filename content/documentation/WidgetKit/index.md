---
route: /documentation/WidgetKit
source_url: https://developer.apple.com/documentation/WidgetKit
source_locale: en-US
section: docc
content_type: symbol
title: WidgetKit
original_title: WidgetKit
source_hash: abc800538531f561686cad55591fd88d31df34f07fbbe648404cd70a807d85a3
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:04:40+00:00'
last_translated_at: '2026-03-14T03:18:00+09:00'
---

# WidgetKit

widget, watch complication, Live Activity, control을 만들어 앱의 도달 범위를 확장합니다.

## 개요

WidgetKit을 사용하면 앱 외부의 문맥에서도 앱 콘텐츠를 사용할 수 있게 하고, 한눈에 확인할 수 있으며 항상 최신 상태인 경험의 생태계를 구축해 앱의 도달 범위를 확장할 수 있습니다.

![iPhone의 작은 widget, Apple Watch의 직사각형 widget, Mac 데스크톱의 작은 widget을 보여 주는 개념 이미지입니다.](https://developer.apple.com)

WidgetKit이 가능하게 하는 생태계는 다음으로 구성됩니다.

:::term-list
**Widgets**: widget은 앱의 작고 시의적절하며 개인적으로 관련 있는 정보를 끌어올려 사용자가 한눈에 볼 수 있는 곳에 표시하고, 앱을 실행하지 않고도 특정 앱 기능을 제공합니다. iPhone과 iPad에서는 Today View, 홈 화면, 잠금 화면에 widget을 배치합니다. Mac에서는 네이티브 Mac 앱 widget을 데스크톱과 Notification Center에 배치합니다. 또한 Mac 데스크톱과 Notification Center, 또는 CarPlay 같은 위치에 iPhone widget을 배치할 수 있습니다. Apple Watch에서는 widget이 Smart Stack에 나타나고, Apple Vision Pro에서는 widget이 사용자가 수평 및 수직 표면에 고정할 수 있는 3차원 객체가 됩니다.
**Smart Stacks**: iPhone과 iPad에서는 사용자가 홈 화면에 widget을 쌓아 Smart Rotate를 사용하는 Smart Stack을 만들고, 가장 문맥에 맞는 widget을 표시합니다. Apple Watch에서는 시스템이 개인의 문맥과 가장 관련 있는 widget을 지능적으로 표시합니다. 또한 사용자는 특정 widget이 항상 Smart Stack에 나타나도록 구성하거나 고정 위치에 pin할 수 있습니다.
**Watch complications**: 사용자는 Apple Watch face에 watch complication을 배치해 손목을 들었을 때 시의적절하고 관련 있는 정보를 봅니다. 또한 Apple Watch의 Smart Stack은 최대 세 개의 complication을 위한 공간을 제공합니다.
**Live Activities**: Live Activity는 이벤트와 작업 정보 같은 앱의 최신 콘텐츠를 잠금 화면이나 Dynamic Island에 표시합니다. Live Activity는 업데이트를 위해 [ActivityKit](https://developer.apple.com/documentation/ActivityKit)을 사용하고, 필요하면 Apple Push Notification service(APNs)를 통해 ActivityKit push notification을 전송합니다. 자세한 내용은 [ActivityKit](https://developer.apple.com/documentation/ActivityKit)을 참고하십시오.
**Controls**: control은 [App Intents](https://developer.apple.com/documentation/AppIntents) 프레임워크로 설명하는 동작을 Control Center, 잠금 화면, Action button에서 수행할 수 있게 하는 button 또는 toggle로 동작합니다. button control은 앱의 동작을 시작하거나 앱의 특정 view를 열 수 있고, toggle은 조명을 켜고 끄거나 차고 문을 열고 닫을 수 있습니다. control은 Control Center 또는 메뉴 막대 항목으로 표시되며 Apple Watch의 Control Center에도 표시됩니다.
:::

### 한눈에 보이는 기능을 반복적으로 개발하기

WidgetKit은 iPad, iPhone, Mac, Apple Watch, Apple Vision Pro 전반에서 기능을 가능하게 하지만, 사람의 기기와 개인적 필요에 가장 잘 맞는 방식으로만 제공합니다. 예를 들어 WidgetKit은 모든 플랫폼에서 여러 크기의 widget을 지원합니다. 반면 Live Activity와 control은 Apple Vision Pro에서는 제공되지 않습니다.

WidgetKit이 제공하는 모든 기능이 모든 플랫폼이나 기기에서 사용 가능한 것은 아니지만, widget, Live Activity, control, watch complication은 기술적, 디자인적 유사성을 공유합니다. 따라서 이 기능들을 함께 개발하고 문맥 전반으로 사용 범위를 넓히기 쉽습니다.

반복적인 접근 방식을 사용해 한 가지 기능이나 일부 widget 크기부터 지원을 시작하십시오. 예를 들어 [Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension)에 설명된 작은 widget부터 시작하되, 처음부터 플랫폼 전반의 추가 크기와 기능을 계획하고 설계하십시오. 그런 다음 가능한 한 많은 문맥에서 사용자가 콘텐츠를 볼 수 있게 하십시오.

자세한 내용은 [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy)를 참고하십시오.

### 상호 작용과 개인화 이해하기

WidgetKit 생태계는 사용자가 새로운 문맥에서 앱 콘텐츠를 보고, 필요할 때 필요한 위치에서 앱과 특정 상호 작용을 수행할 수 있게 합니다.

- 사용자는 widget, watch complication, Live Activity를 탭해 대응하는 앱 또는 그 정보나 기능에 맞는 장면을 실행합니다. 예를 들어 Emoji Ranger widget 또는 watch complication을 탭하면 표시된 hero에 맞는 앱 장면이 실행됩니다. 자세한 내용은 [Linking to specific app scenes from your widget or Live Activity](https://developer.apple.com/documentation/widgetkit/linking-to-specific-app-scenes-from-your-widget-or-live-activity)를 참고하십시오.
- 사용자는 widget, control, Live Activity 안의 button과 toggle을 사용해 앱을 실행하지 않고도 앱과 상호 작용합니다. 예를 들어 [Emoji Rangers: Supporting Live Activities, interactivity, and animations](https://developer.apple.com/documentation/widgetkit/emoji-rangers-supporting-live-activities-interactivity-and-animations) 샘플 프로젝트의 large widget에는 사용자가 탭해 hero의 치유 능력을 일시적으로 강화하는 button이 포함됩니다.

관련 정보와 즉각적인 상호 작용을 제공하는 것 외에도, 사용자는 widget, watch complication, Live Activity, control을 사용해 기기를 개인화합니다.

- 사용자는 자신의 필요에 맞는 세부 정보를 표시하도록 widget과 watch complication을 구성합니다. 예를 들어 [Emoji Rangers: Supporting Live Activities, interactivity, and animations](https://developer.apple.com/documentation/widgetkit/emoji-rangers-supporting-live-activities-interactivity-and-animations) 샘플 프로젝트의 widget은 사용자가 widget에 나타나는 hero를 구성할 수 있게 합니다.
- 사용자는 자신에게 가장 잘 맞는 방식으로 widget과 watch complication을 배치합니다. iPhone 또는 iPad에서 widget을 쌓고 Smart Rotate를 활성화하면 WidgetKit은 가장 관련 있는 widget을 자동으로 위로 회전시켜 사용자가 적절한 시점에 가장 중요한 정보를 보게 합니다. Apple Watch에서는 Smart Stack이 문맥 관련성을 기준으로 widget을 표시하고, 사용자는 즐겨 쓰는 widget을 Smart Stack의 고정 위치에 pin합니다.

### timeline과 push notification으로 콘텐츠 업데이트하기

widget과 watch complication은 콘텐츠를 업데이트하기 위한 특별한 메커니즘을 사용합니다. 데이터 업데이트 timeline을 만들고 이를 WidgetKit에 전달하면 WidgetKit이 에너지 효율적인 방식으로 widget이나 complication의 콘텐츠를 업데이트합니다. timeline에 대한 자세한 내용은 [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date)를 참고하십시오. 또한 widget은 Apple Push Notification service(APNs)와 원격 push notification을 사용해 업데이트를 받을 수 있습니다.

Live Activity는 timeline을 사용하지 않습니다. 대신 [ActivityKit](https://developer.apple.com/documentation/ActivityKit)과 APNs로 보내는 ActivityKit push notification을 사용합니다. 자세한 내용은 [ActivityKit](https://developer.apple.com/documentation/ActivityKit)을 참고하십시오.

control도 timeline을 사용하지 않습니다. 대신 사용자가 control을 사용할 때, 앱이 이를 다시 로드할 때, 또는 시스템이 APNs의 원격 push notification을 받을 때 콘텐츠를 업데이트합니다.

### 집중되고 한눈에 들어오는 디자인 만들기

widget, watch complication, Live Activity, control은 크기가 작기 때문에 집중된 한눈에 들어오는 디자인이 필요합니다. 디자인 가이드는 [Human Interface Guidelines > Widgets](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets), [Human Interface Guidelines > Complications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications), [Human Interface Guidelines > Live Activities](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/live-activities), [Human Interface Guidelines > Controls](https://developer.apple.com/design/human-interface-guidelines/controls)를 참고하십시오.

:::topic-grid
## 기초
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy): widget, control, watch complication, Live Activity 구현 계획을 세우면서 기능, 작업, 관련 프레임워크, 제약 사항을 살펴봅니다.
- [WidgetKit updates](https://developer.apple.com/documentation/Updates/WidgetKit): WidgetKit의 중요한 변경 사항을 알아봅니다.
- [Creating a widget extension](https://developer.apple.com/documentation/widgetkit/creating-a-widget-extension): 여러 기기에서 앱 콘텐츠를 편리하고 유익한 widget으로 표시합니다.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](https://developer.apple.com/documentation/widgetkit/emoji-rangers-supporting-live-activities-interactivity-and-animations): Live Activity와 control을 제공하고, 데이터 업데이트를 애니메이션하며, widget에 상호 작용을 추가합니다.
- [WidgetBundle](https://developer.apple.com/documentation/SwiftUI/WidgetBundle): 하나의 widget extension에서 여러 widget을 노출하는 데 사용하는 container입니다.
:::

:::topic-grid
## 시스템 경험
- [Widgets and watch complications](https://developer.apple.com/documentation/widgetkit/widgets-and-complications-collection): 사용자가 기기를 개인화하고, 관련 정보를 보고, widget과 watch complication으로 상호 작용할 수 있게 합니다.
- [Live Activities](https://developer.apple.com/documentation/widgetkit/liveactivities-collection): 사용자가 Live Activity로 앱의 업데이트를 추적할 수 있게 합니다.
- [Controls](https://developer.apple.com/documentation/widgetkit/controls-collection): 사용자가 Control Center, 잠금 화면, Action button에 배치해 앱의 동작을 빠르게 수행할 수 있는 control을 제공합니다.
:::

:::topic-grid
## 표시
- [Creating views for widgets, Live Activities, and watch complications](https://developer.apple.com/documentation/widgetkit/creating-views-for-widgets-live-activities-and-watch-complications): WidgetKit과 SwiftUI로 한눈에 보이는 view를 구현합니다.
- [SwiftUI views for widgets](https://developer.apple.com/documentation/widgetkit/swiftui-views): SwiftUI view로 widget 안에 앱 콘텐츠를 표시합니다.
:::

:::topic-grid
## 상호 작용
- [Adding interactivity to widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/adding-interactivity-to-widgets-and-live-activities): widget 또는 Live Activity에 button이나 toggle을 포함해 앱을 실행하지 않고도 앱 기능을 제공합니다.
- [Animating data updates in widgets and Live Activities](https://developer.apple.com/documentation/widgetkit/animating-data-updates-in-widgets-and-live-activities): SwiftUI 애니메이션을 사용해 widget과 Live Activity의 데이터 업데이트를 나타냅니다.
- [Linking to specific app scenes from your widget or Live Activity](https://developer.apple.com/documentation/widgetkit/linking-to-specific-app-scenes-from-your-widget-or-live-activity): 사용자가 앱의 특정 장면을 열 수 있게 하는 deep link를 widget과 Live Activity에 추가합니다.
:::

:::topic-grid
## 접근성
- [Adding accessible descriptions to widgets and Live Activities](https://developer.apple.com/documentation/ActivityKit/adding-accessible-descriptions-to-widgets-and-live-activities): 사용자가 widget과 Live Activity의 인터페이스 요소가 무엇을 나타내는지 이해할 수 있도록 설명합니다.
:::

:::topic-grid
## preview 및 디버깅
- [Previewing widgets and Live Activities in Xcode](https://developer.apple.com/documentation/widgetkit/previewing-widgets-and-live-activities-in-xcode): Xcode preview를 사용해 widget과 Live Activity를 반복적으로 개발하고 미세 조정하며 문제를 해결합니다.
- [WidgetPreviewContext](https://developer.apple.com/documentation/widgetkit/widgetpreviewcontext): widget preview 문맥에 대한 specification입니다.
- [Preview macros](https://developer.apple.com/documentation/widgetkit/preview-macros): Swift macro를 사용해 Xcode에서 widget preview를 생성합니다.
:::
