---
route: /documentation/ActivityKit
source_url: https://developer.apple.com/documentation/ActivityKit
source_locale: en-US
section: docc
content_type: symbol
title: ActivityKit
original_title: ActivityKit
source_hash: 8a6bf87db33c0641efa8d879d7b351e2d411ee88a8112de48d6528031b372c71
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:25:16+00:00'
last_translated_at: '2026-03-13T23:12:00+09:00'
---

# ActivityKit

iPhone, iPad, Apple Watch, Mac에서 앱의 라이브 업데이트를 Live Activities로 공유합니다.

## 개요

ActivityKit 프레임워크를 사용하면 앱의 라이브 업데이트를 공유하기 위해 Live Activity를 시작할 수 있습니다. Live Activities는 몇 시간에 걸쳐 진행되는 이벤트나 활동을 사람들이 추적할 수 있도록 풍부하고 인터랙티브하며 한눈에 파악하기 쉬운 방식을 제공합니다. 특히 업데이트된 정보를 제공하기 위해 알림 한계를 밀어붙이는 앱에 적합합니다. 예를 들어 스포츠 앱은 경기 동안 라이브 정보를 한눈에 볼 수 있게 하는 Live Activity를 시작할 수 있습니다.

Live Activity는 눈에 잘 띄는 다음과 같은 맥락에 표시됩니다.

- iPad와 iPhone에서는 Lock Screen, Dynamic Island, Home Screen에 표시됩니다.
- Apple Watch에서는 Smart Stack에 표시됩니다.
- Mac에서는 메뉴 막대에 표시됩니다.
- CarPlay에서는 Home Screen에 표시됩니다.

실시간 정보를 보는 것 외에도, 사람들은 Live Activity 레이아웃에 포함된 버튼이나 토글을 사용해 앱을 실행하지 않고도 필수 기능을 수행할 수 있고, Live Activity를 탭해 해당 활동의 콘텐츠와 일치하는 장면으로 앱을 실행할 수도 있습니다.

![배달 앱의 Live Activity를 보여 주는 iPhone 스크린샷 3장입니다. Lock Screen, Dynamic Island의 leading 및 trailing 표시, 그리고 확장 표시에서 Live Activity가 보입니다.](https://developer.apple.com)

앱에서는 ActivityKit을 사용해 Live Activity를 구성하고, 시작하고, 업데이트하고, 종료합니다. 그리고 widget extension, [WidgetKit](https://developer.apple.com/documentation/WidgetKit), [SwiftUI](https://developer.apple.com/documentation/SwiftUI)를 사용해 Live Activity의 사용자 인터페이스를 만듭니다. SwiftUI와 WidgetKit을 사용하면 위젯과 Live Activity 사이에서 코드를 공유하거나 두 기능을 함께 개발할 수 있습니다.

하지만 Live Activities는 업데이트를 받는 방식이 위젯과 다릅니다. 타임라인 메커니즘을 사용하는 대신, Live Activities는 ActivityKit을 통해 앱으로부터 업데이트된 데이터를 받고, ActivityKit 푸시 알림을 통해 서버로부터도 업데이트를 받습니다. 또한 ActivityKit 푸시 알림으로 Live Activity를 시작할 수도 있습니다.

:::note Note
visionOS는 Live Activities를 지원하지 않습니다. 호환되는 iPad 또는 iPhone 앱에서 Live Activity 시작을 요청하면 실패합니다.
:::

:::topic-grid
## 핵심 항목
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/WidgetKit/Developing-a-WidgetKit-strategy): 위젯, 컨트롤, watch complication, Live Activities를 구현하기 위한 계획을 세울 때 기능, 작업, 관련 프레임워크, 제약 사항을 살펴봅니다.
- [ActivityKit updates](https://developer.apple.com/documentation/Updates/ActivityKit): ActivityKit의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## Live Activity 시작
- [Displaying live data with Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities): Dynamic Island, Lock Screen, CarPlay, 그리고 페어링된 Mac 또는 Apple Watch에서 최신 데이터를 표시하고 빠른 상호 작용을 제공합니다.
- [Starting and updating Live Activities with ActivityKit push notifications](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications): ActivityKit을 사용해 푸시 토큰을 받고, ActivityKit 알림으로 Live Activity를 원격 시작, 업데이트, 종료합니다.
- [Activity](https://developer.apple.com/documentation/activitykit/activity): Live Activity를 시작하고, 업데이트하고, 종료하는 데 사용하는 객체입니다.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](https://developer.apple.com/documentation/WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations): Live Activities와 컨트롤을 제공하고, 데이터 업데이트를 애니메이션으로 처리하며, 위젯에 상호 작용 기능을 추가합니다.
- [NSSupportsLiveActivities](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSupportsLiveActivities): 앱이 Live Activities를 지원하는지를 나타내는 Boolean 값입니다.
- [NSSupportsLiveActivitiesFrequentUpdates](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSSupportsLiveActivitiesFrequentUpdates): 앱이 Live Activities를 자주 업데이트할 수 있는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 사용자 인터페이스
- [Creating custom views for Live Activities](https://developer.apple.com/documentation/activitykit/creating-custom-views-for-live-activities): 각 Live Activity 표시를 지원하는 재사용 가능한 사용자 정의 뷰와 레이아웃을 만듭니다.
- [Adding accessible descriptions to widgets and Live Activities](https://developer.apple.com/documentation/activitykit/adding-accessible-descriptions-to-widgets-and-live-activities): 사람들이 의미를 이해할 수 있도록 위젯과 Live Activity의 인터페이스 요소를 설명합니다.
- [Launching your app from a Live Activity](https://developer.apple.com/documentation/activitykit/launching-your-app-from-a-live-activity): deep link를 사용해 Live Activity 데이터와 일치하는 장면으로 앱을 열 수 있게 합니다.
:::

:::topic-grid
## 위젯 생태계
- [Creating a widget extension](https://developer.apple.com/documentation/WidgetKit/Creating-a-Widget-Extension): 다양한 기기에서 앱 콘텐츠를 편리하고 유익한 위젯으로 표시합니다.
- [Animating data updates in widgets and Live Activities](https://developer.apple.com/documentation/WidgetKit/Animating-data-updates-in-widgets-and-live-activities): SwiftUI 애니메이션을 사용해 위젯과 Live Activity의 데이터 업데이트를 나타냅니다.
- [Creating views for widgets, Live Activities, and watch complications](https://developer.apple.com/documentation/WidgetKit/Creating-views-for-widgets-Live-Activities-and-watch-complications): WidgetKit과 SwiftUI로 한눈에 파악할 수 있는 뷰를 구현합니다.
- [Linking to specific app scenes from your widget or Live Activity](https://developer.apple.com/documentation/WidgetKit/Linking-to-specific-app-scenes-from-your-widget-or-Live-Activity): 위젯과 Live Activity에 deep link를 추가해 앱의 특정 장면을 열 수 있게 합니다.
- [WidgetKit](https://developer.apple.com/documentation/WidgetKit): 위젯, watch complication, Live Activities, 컨트롤을 만들어 앱의 도달 범위를 확장합니다.
:::
