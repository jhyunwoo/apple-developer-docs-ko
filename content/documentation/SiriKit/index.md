---
route: /documentation/SiriKit
source_url: https://developer.apple.com/documentation/SiriKit
source_locale: en-US
section: docc
content_type: article
title: SiriKit
original_title: SiriKit
source_hash: cc087463f0f8813a675da7b530b236b212bfeee7eaf9c3428fd233daa3a8e959
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:47:09+00:00'
last_translated_at: '2026-03-13T21:05:00+09:00'
---

# SiriKit

음성, 지능형 제안, 개인화된 워크플로를 통해 사용자가 기기와 상호 작용할 수 있도록 지원합니다.

## 개요

Intents 및 IntentsUI 프레임워크는 “Siri야…”로 시작하는 상호 작용, Shortcuts 동작, widget 구성을 구동합니다. 또한 시스템은 앱이 기증한 intent와 user activity를 Maps, Calendar, Apple Watch complication, widget, 검색 결과의 문맥 기반 제안에 통합합니다.

![MacBook Air, iPhone, Apple Watch, HomePod mini가 함께 표시되어 있고, SiriKit이 가능하게 하는 사용자 상호 작용이 나타나는 이미지입니다. MacBook Air에는 Shortcuts 앱의 All Shortcuts 섹션이 열려 있고, iPhone에는 Maps 아이콘이 있는 Siri Suggestion이 표시되며, Apple Watch에는 Siri 애니메이션과 “What can I help you with?”라는 문구가 표시됩니다.](https://developer.apple.com)

시스템이 제공하는 표준 intent를 사용하면 사용자가 이미 Siri에 요청하는 동작, 예를 들어 음악 재생이나 문자 메시지 전송 같은 작업을 지원할 수 있습니다. 또한 custom intent를 설계하여 앱의 고유한 기능을 시스템 전반에 제공할 수도 있습니다. custom intent 정의에 대한 자세한 내용은 [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](https://developer.apple.com/documentation/SiriKit/adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app)을 참고하십시오.

intent는 앱 내부에서 직접 처리할 수도 있고, Intents app extension에서 처리할 수도 있습니다. app extension을 설정하고 앱과 extension 사이에서 정보를 공유하는 방법에 대한 지침은 [Structuring Your Code to Support App Extensions](https://developer.apple.com/documentation/SiriKit/structuring-your-code-to-support-app-extensions)를 참고하십시오.

사용자 요청을 처리한 뒤 Siri와 Maps에 브랜딩이나 기타 맞춤형 콘텐츠를 표시하려면 IntentsUI app extension 안에 custom view controller를 만드십시오. 자세한 내용은 [Creating an Intents UI Extension](https://developer.apple.com/documentation/sirikit/creating-an-intents-ui-extension)을 참고하십시오.

:::important 중요
사용자의 허가가 있는 경우, [SensorKit](https://developer.apple.com/documentation/SensorKit) entitlement를 사용하는 설치된 건강 연구 앱은 SiriKit 앱이 사용 중일 때 Face Metrics 데이터를 수집할 수 있습니다. 앱이 사용 중일 때 SensorKit이 Face Metrics 데이터를 수집하지 못하게 하려면 [SRResearchDataGeneration](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SRResearchDataGeneration) 정보 property list 키를 `NO`로 설정할 수 있습니다.
:::

:::topic-grid
## 프레임워크
- [Intents](https://developer.apple.com/documentation/intents): 사용자가 자신의 기기에서 앱과의 상호 작용을 사용자화할 수 있도록 지원합니다.
- [IntentsUI](https://developer.apple.com/documentation/intentsui): Siri와 Maps 인터페이스 안의 콘텐츠를 사용자화합니다.
:::

:::topic-grid
## 샘플 코드
- [Adding Shortcuts for Wind Down](https://developer.apple.com/documentation/sirikit/adding-shortcuts-for-wind-down): 건강 앱 내부에서 앱의 shortcut을 노출합니다.
- [Booking Rides with SiriKit](https://developer.apple.com/documentation/sirikit/booking-rides-with-sirikit): Siri와 Maps를 사용한 차량 예약 요청을 처리하도록 앱에 Intents extension을 추가합니다.
- [Handling Payment Requests with SiriKit](https://developer.apple.com/documentation/sirikit/handling-payment-requests-with-sirikit): Siri를 통한 송금 요청을 처리하도록 앱에 Intent Extension을 추가합니다.
- [Handling Workout Requests with SiriKit](https://developer.apple.com/documentation/sirikit/handling-workout-requests-with-sirikit): Siri를 통한 운동 제어 요청을 처리하는 Intent Extension을 앱에 추가합니다.
- [Integrating Your App with Siri Event Suggestions](https://developer.apple.com/documentation/sirikit/integrating-your-app-with-siri-event-suggestions): 예약 정보를 기증하고 시스템 전반에서 이벤트 세부 사항에 빠르게 접근할 수 있게 합니다.
- [Managing Audio with SiriKit](https://developer.apple.com/documentation/sirikit/managing-audio-with-sirikit): SiriKit Media Intent를 사용해 오디오 재생을 제어하고 미디어 추가 요청을 처리합니다.
- [Providing Hands-Free App Control with Intents](https://developer.apple.com/documentation/sirikit/providing-hands-free-app-control-with-intents): extension 없이 intent를 resolve, confirm, handle합니다.
- [Soup Chef: Accelerating App Interactions with Shortcuts](https://developer.apple.com/documentation/sirikit/soup-chef-accelerating-app-interactions-with-shortcuts): 앱 동작에 대한 shortcut을 제공해 사용자가 Siri와 함께 앱을 더 쉽게 사용할 수 있게 합니다.
- [Soup Chef with App Intents: Migrating custom intents](https://developer.apple.com/documentation/sirikit/soup-chef-with-app-intents-migrating-custom-intents): 앱의 동작을 Siri와 Shortcuts에 제공하기 위해 App Intents를 통합합니다.
:::

:::topic-grid
## 아티클
- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](https://developer.apple.com/documentation/sirikit/adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app): 사용자가 Siri와 Shortcuts 앱을 더 빠르고 효과적으로 사용할 수 있도록 custom intent와 parameter를 추가합니다.
- [Defining Relevant Shortcuts for the Siri Watch Face](https://developer.apple.com/documentation/sirikit/defining-relevant-shortcuts-for-the-siri-watch-face): 앱의 shortcut이 사용자에게 유용할 수 있는 시점을 Siri에 알립니다.
- [Deleting Donated Shortcuts](https://developer.apple.com/documentation/sirikit/deleting-donated-shortcuts): Siri에서 기증한 shortcut을 제거합니다.
- [Dispatching intents to handlers](https://developer.apple.com/documentation/sirikit/dispatching-intents-to-handlers): 특정 intent를 처리할 수 있는 intent handler를 SiriKit에 제공합니다.
- [Improving Siri Media Interactions and App Selection](https://developer.apple.com/documentation/sirikit/improving-siri-media-interactions-and-app-selection): 앱 기능, 사용자화된 이름, 청취 습관을 시스템과 공유해 음성 제어를 세밀하게 다듬고 Siri 제안을 개선합니다.
- [Improving interactions between Siri and your messaging app](https://developer.apple.com/documentation/sirikit/improving-interactions-between-siri-and-your-messaging-app): 앱 전용 콘텐츠를 기증하고 Siri의 연락처 제안을 활용하며 최신 플랫폼 기능을 채택해 더 일관된 메시징 경험을 만듭니다.
- [Registering Custom Vocabulary with SiriKit](https://developer.apple.com/documentation/sirikit/registering-custom-vocabulary-with-sirikit): 앱의 custom 용어를 등록하고 Siri와 함께 앱을 사용하는 예시 문구를 제공합니다.
- [Confirming the Details of an Intent](https://developer.apple.com/documentation/sirikit/confirming-the-details-of-an-intent): intent parameter를 최종 검증하고 서비스가 intent를 수행할 준비가 되었는지 확인합니다.
- [Handling an Intent](https://developer.apple.com/documentation/sirikit/handling-an-intent): intent를 수행하고 수행한 작업에 대한 피드백을 SiriKit에 제공합니다.
- [Resolving the Parameters of an Intent](https://developer.apple.com/documentation/sirikit/resolving-the-parameters-of-an-intent): intent의 parameter를 검증하고 계속 진행하는 데 필요한 정보를 갖추었는지 확인합니다.
- [Generating a List of Ride Options](https://developer.apple.com/documentation/sirikit/generating-a-list-of-ride-options): Maps가 사용자에게 표시할 차량 옵션 목록을 생성합니다.
- [Handling the Ride-Booking Intents](https://developer.apple.com/documentation/sirikit/handling-the-ride-booking-intents): Shortcuts 또는 Maps로 차량을 예약할 때의 서로 다른 intent 처리 시퀀스를 지원합니다.
- [Donating Reservations](https://developer.apple.com/documentation/sirikit/donating-reservations): 앱에서 이루어진 예약 정보를 Siri에 알립니다.
- [Specifying Synonyms for Your App Name](https://developer.apple.com/documentation/sirikit/specifying-synonyms-for-your-app-name): 사용자가 더 익숙하게 느끼거나 더 쉽게 말할 수 있는 앱 이름의 대체 표현을 제공합니다.
- [Intent Phrases](https://developer.apple.com/documentation/sirikit/intent-phrases): 사용자가 Siri에서 앱과 어떻게 상호 작용하는지를 보여주기 위해 전역 vocabulary 파일에 포함하는 키입니다.
- [Localizing Your Vocabulary for Chinese Dialects](https://developer.apple.com/documentation/sirikit/localizing-your-vocabulary-for-chinese-dialects): 발음 팁에 강조 표식을 적용해 Siri가 중국어 방언을 더 잘 이해하도록 돕습니다.
- [Parameter Vocabularies](https://developer.apple.com/documentation/sirikit/parameter-vocabularies): 앱 전용 용어를 설명하기 위해 전역 vocabulary 파일에 포함하는 키입니다.
- [Offering Actions in the Shortcuts App](https://developer.apple.com/documentation/sirikit/offering-actions-in-the-shortcuts-app): 사용자가 Siri에 추가하거나 자신만의 shortcut 안에서 다른 동작과 조합하고 싶어 할 shortcut을 제안합니다.
- [Creating an Intents App Extension](https://developer.apple.com/documentation/sirikit/creating-an-intents-app-extension): Xcode 프로젝트에 Intents app extension을 추가하고 구성합니다.
- [Requesting Authorization to Use Siri](https://developer.apple.com/documentation/sirikit/requesting-authorization-to-use-siri): Siri와 Maps가 앱 또는 Intents app extension과 통신할 수 있도록 사용자 권한을 요청합니다.
- [Structuring Your Code to Support App Extensions](https://developer.apple.com/documentation/sirikit/structuring-your-code-to-support-app-extensions): 앱과 app extension이 함께 사용할 수 있도록 백엔드 서비스를 private framework로 옮깁니다.
- [Providing Live Status Updates](https://developer.apple.com/documentation/sirikit/providing-live-status-updates): 예약된 차량의 상태를 Maps에 정기적으로 업데이트합니다.
- [Donating Shortcuts](https://developer.apple.com/documentation/sirikit/donating-shortcuts): 사용자가 앱에서 수행한 동작의 shortcut을 Siri에 알립니다.
- [Configuring the View Controller for Your Custom Interface](https://developer.apple.com/documentation/sirikit/configuring-the-view-controller-for-your-custom-interface): Siri나 Maps의 기본 인터페이스를 대체하거나 보강하도록 view controller를 구성합니다.
- [Configuring Your Intents UI App Extension Target](https://developer.apple.com/documentation/sirikit/configuring-your-intents-ui-app-extension-target): Siri와 Maps 인터페이스를 사용자화할 때 사용하는 Intents UI app extension을 포함하도록 Xcode 프로젝트를 구성합니다.
:::
