---
route: /documentation/watchOS-Apps
source_url: https://developer.apple.com/documentation/watchOS-Apps
source_locale: en-US
section: docc
content_type: article
title: watchOS apps
original_title: watchOS apps
source_hash: ffacb77bb97732ecb6cdc560764a3ec1c035b297d28b51e951de25124bbdb5e9
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:41:09+00:00'
last_translated_at: '2026-03-14T01:17:00+09:00'
---

# watchOS apps

complication, 알림, Siri를 결합해 Apple Watch에서 개인화된 경험을 만드는 watchOS 앱을 빌드합니다.

## 개요

Apple Watch는 손목 위에서 중요한 정보에 쉽게 접근할 수 있게 해 줍니다. watchOS 경험은 짧고 구분된 상호 작용을 통해 유용한 작업을 수행하는 빠른 action에 초점을 둡니다.

![사용자 인터페이스 만들기, 백그라운드 오디오 재생, 사용자 정의 알림 표시 등을 나타내는 아이콘들에 둘러싸인 Apple Watch를 보여 주는 일러스트입니다.](https://developer.apple.com)

Apple Watch에서는 상호 작용을 가능한 한 짧게 유지하십시오. 중요한 정보를 한눈에 보여 주고, 착용자가 몇 번의 탭만으로 반응한 뒤 손목을 내리고 다음 일로 넘어가도록 유도하십시오. 사용자는 action이 성공했는지 기다릴 필요가 없습니다. 대신 watchOS 앱이 중요한 업데이트가 있으면 자동으로 알립니다.

watchOS에서는 실제 코드 작성보다 앱 경험을 계획하고, 설계하고, 다듬는 데 더 많은 시간을 쓰게 될 것이라고 예상하십시오. 디자인 가이드는 [Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/platforms/designing-for-watchos/)를 참고하십시오.

watchOS 앱을 설계할 때는 더 풍부한 경험을 만들기 위해 다음 기술을 조합해 사용하십시오.

## watchOS 앱

메인 앱은 watchOS 앱 경험의 기반 역할을 합니다. 누구나 앱을 직접 실행하고 상호 작용할 수 있습니다. 하지만 앱 인터페이스가 반드시 사람들이 앱과 상호 작용하는 주요 방식인 것은 아닙니다. 많은 사용자는 complication이나 알림을 통해 상호 작용하는 것을 선호할 수 있으며, 앱을 명시적으로 실행하지 않을 수도 있습니다.

![네 개의 watchOS 앱 아이콘이 표시된 watch face 일러스트입니다.](https://developer.apple.com)

## Complication

Complication은 watch face에서 앱 데이터의 작은 일부를 직접 보여 줍니다. 대부분의 watch face에 complication을 추가할 수 있지만 공간은 제한적입니다. complication은 시의적절하고, 최신이며, 유용한 정보를 보여 주도록 설계하십시오. 사용자는 complication을 탭해 watchOS 앱을 빠르고 쉽게 실행할 수도 있습니다.

![코너 complication을 나타내기 위해 모서리가 강조된 watch face 일러스트입니다.](https://developer.apple.com)

## 알림

중요한 이벤트를 알리기 위해 알림을 사용하십시오. 또한 사용자가 앱을 열지 않고도 즉시 응답할 수 있도록 action을 제공할 수 있습니다. 앱이 실행 중이 아니더라도 로컬 알림과 원격 알림 중 어느 쪽이든 사용해 소통할 수 있습니다.

![알림 아이콘과 알림 텍스트를 나타내는 두 개의 막대가 보이는 watch face 일러스트입니다.](https://developer.apple.com)

## Siri

SiriKit과 App intents를 사용해 사용자가 앱과 상호 작용하는 방식을 확장하십시오. 앱이 메시징이나 미디어 같은 도메인을 사용한다면 [SiriKit](https://developer.apple.com/documentation/SiriKit)을 사용해 앱에 Siri 지원을 추가하십시오. 그 밖의 기능에는 [App Intents](https://developer.apple.com/documentation/AppIntents)를 사용해 앱 기능을 Siri와 Shortcuts 앱 같은 시스템 서비스에 노출하십시오.

![Siri 아이콘과 `What can I help you with?` 텍스트가 보이는 watch face 일러스트입니다.](https://developer.apple.com)

:::topic-grid
## 핵심 사항
- [Creating an intuitive and effective UI in watchOS 10](https://developer.apple.com/documentation/watchos-apps/creating-an-intuitive-and-effective-ui-in-watchos-10): 새로운 디자인 기능으로 더 간결하고, 일관되고, 한눈에 들어오는 사용자 경험을 제공합니다.
- [Updating your app and widgets for watchOS 10](https://developer.apple.com/documentation/watchos-apps/updating-your-app-and-widgets-for-watchos-10): SwiftUI 요소와 watch 전용 기능을 통합하고 Smart Stack용 widget을 빌드합니다.
- [Building a watchOS app](https://developer.apple.com/documentation/watchos-apps/building_a_watchos_app): 앱의 life cycle을 설정하고 SwiftUI로 사용자 인터페이스를 만듭니다.
- [watchOS updates](https://developer.apple.com/documentation/Updates/watchos): watchOS의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 앱 경험
- [Setting up a watchOS project](https://developer.apple.com/documentation/watchos-apps/setting-up-a-watchos-project): 새 watchOS 프로젝트를 만들거나 기존 iOS 프로젝트에 watch target을 추가합니다.
- [Creating independent watchOS apps](https://developer.apple.com/documentation/watchos-apps/creating-independent-watchos-apps): companion iOS 앱 없이 설치 및 실행되는 watchOS 앱을 설정합니다.
- [Keeping your watchOS content up to date](https://developer.apple.com/documentation/watchos-apps/keeping-your-watchos-app-s-content-up-to-date): 앱 콘텐츠가 관련성 있고 최신 상태를 유지하도록 합니다.
- [Updating watchOS apps with timelines](https://developer.apple.com/documentation/watchos-apps/updating-watchos-apps-with-timelines): 비활성 상태에서도 사용자 인터페이스 업데이트를 매끄럽게 예약합니다.
- [Authenticating users on Apple Watch](https://developer.apple.com/documentation/watchos-apps/authenticating-users-on-apple-watch): 앱용 계정 가입 및 로그인 전략을 만듭니다.
- [Responding to the Action button on Apple Watch Ultra](https://developer.apple.com/documentation/AppIntents/ActionButtonArticle): App Intents를 사용해 앱의 action을 등록합니다.
- [Enabling the double-tap gesture on Apple Watch](https://developer.apple.com/documentation/watchos-apps/enabling-double-tap): Apple Watch의 double-tap gesture에 대한 앱 반응을 사용자화합니다.
:::

:::topic-grid
## 손쉬운 사용
- [Create accessible experiences for watchOS](https://developer.apple.com/documentation/watchos-apps/create-accessible-experiences-for-watchos): watchOS 앱을 더 접근 가능하게 만드는 방법을 배웁니다.
:::

:::topic-grid
## 사용자 인터페이스
- [Building a productivity app for Apple Watch](https://developer.apple.com/documentation/watchos-apps/building-a-productivity-app-for-apple-watch): 작업 목록을 관리하고 공유하며 차트로 상태를 시각화하는 watch 앱을 만듭니다.
- [Supporting multiple watch sizes](https://developer.apple.com/documentation/watchos-apps/supporting-multiple-watch-sizes): 모든 Apple Watch 크기를 지원하도록 사용자 인터페이스 레이아웃을 맞춤화합니다.
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state): 지속 표시를 위해 watchOS 앱의 사용자 인터페이스를 맞춤화합니다.
- [Setting the app’s accent color](https://developer.apple.com/documentation/watchos-apps/setting-the-app-s-accent-color): 앱의 accent color를 설정합니다.
:::

:::topic-grid
## Complication
- [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications): 잠금 화면과 Apple Watch의 complication으로 표시되는 accessory widget을 지원합니다.
- [Migrating ClockKit complications to WidgetKit](https://developer.apple.com/documentation/WidgetKit/Converting-A-ClockKit-App): WidgetKit API를 활용해 SwiftUI로 watchOS complication을 만듭니다.
- [Creating a widget extension](https://developer.apple.com/documentation/WidgetKit/Creating-a-Widget-Extension): 다양한 기기에서 앱 콘텐츠를 편리하고 유익한 widget으로 표시합니다.
- [Keeping a widget up to date](https://developer.apple.com/documentation/WidgetKit/Keeping-a-Widget-Up-To-Date): 동적 view를 사용해 적절하고 관련성 있는 정보를 보여 주도록 widget timeline을 계획하고, 변경이 있을 때 timeline을 업데이트합니다.
- [Increasing the visibility of widgets in Smart Stacks](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks): 맥락 정보를 제공하고 intent를 donate해 widget이 Smart Stack에서 눈에 띄게 표시되도록 합니다.
:::

:::topic-grid
## 알림
- [Notifications](https://developer.apple.com/documentation/watchos-apps/notifications): 앱이 실행 중이 아닐 때도 사용자와 소통합니다.
:::

:::topic-grid
## Siri
- [Making actions and content discoverable and widely available](https://developer.apple.com/documentation/AppIntents/Making-actions-and-content-discoverable-and-widely-available): Spotlight, control, widget, Action button에서 앱을 발견할 수 있도록 App Intents를 채택합니다.
- [Creating an Intents App Extension](https://developer.apple.com/documentation/SiriKit/creating-an-intents-app-extension): Xcode 프로젝트에 Intents app extension을 추가하고 구성합니다.
:::

:::topic-grid
## 건강 및 피트니스
- [Setting up HealthKit](https://developer.apple.com/documentation/HealthKit/setting-up-healthkit): HealthKit store를 설정하고 구성합니다.
- [Authorizing access to health data](https://developer.apple.com/documentation/HealthKit/authorizing-access-to-health-data): 앱에서 데이터를 읽고 공유할 권한을 요청합니다.
- [Saving data to HealthKit](https://developer.apple.com/documentation/HealthKit/saving-data-to-healthkit): HealthKit sample을 생성하고 공유합니다.
- [Reading data from HealthKit](https://developer.apple.com/documentation/HealthKit/reading-data-from-healthkit): query를 사용해 HealthKit에서 sample 데이터를 요청합니다.
- [Build a workout app for Apple Watch](https://developer.apple.com/documentation/HealthKit/build-a-workout-app-for-apple-watch): HealthKit과 SwiftUI를 사용해 빠르고 쉽게 자신만의 workout 앱을 만듭니다.
:::

:::topic-grid
## 런타임 관리
- [Background execution](https://developer.apple.com/documentation/WatchKit/background-execution): 백그라운드 세션과 작업을 관리합니다.
- [Life cycles](https://developer.apple.com/documentation/WatchKit/life-cycles): life-cycle 알림을 수신하고 응답합니다.
- [Using extended runtime sessions](https://developer.apple.com/documentation/WatchKit/using-extended-runtime-sessions): 사용자가 상호 작용을 멈춘 뒤에도 앱이 계속 실행되도록 extended runtime session을 만듭니다.
- [Interacting with Bluetooth peripherals during background app refresh](https://developer.apple.com/documentation/WatchKit/interacting-with-bluetooth-peripherals-during-background-app-refresh): 앱이 백그라운드에서 실행되는 동안 Bluetooth peripheral의 값을 읽어 complication을 최신 상태로 유지합니다.
:::

:::topic-grid
## 네트워크 요청
- [Making default and ephemeral requests](https://developer.apple.com/documentation/watchos-apps/making-default-and-ephemeral-requests): 앱이 foreground에서 실행 중일 때 요청을 보냅니다.
- [Making background requests](https://developer.apple.com/documentation/watchos-apps/making-background-requests): 앱이 background에서 실행 중일 때 요청을 보냅니다.
:::

:::topic-grid
## 단위 테스트
- [Setting up tests for your watchOS app](https://developer.apple.com/documentation/watchos-apps/setting-up-tests-for-your-watchos-app): watch 전용 프로젝트에 단위 테스트와 사용자 인터페이스 테스트를 구성합니다.
:::
