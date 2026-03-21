---
route: /documentation/AppClip
source_url: https://developer.apple.com/documentation/AppClip
source_locale: en-US
section: docc
content_type: symbol
title: App Clips
original_title: App Clips
source_hash: 4f7356d59bac79b6a864ff8b6ac9a929f0f945531fc54b10279ba40211b7c6a5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:38:45+00:00'
last_translated_at: '2026-03-13T23:38:45+09:00'
---

# App Clips

즉시 사용할 수 있는 가벼운 순간형 경험 또는 앱의 데모 버전을 만듭니다.

## 개요

*App Clip*은 앱 기능의 일부에 접근할 수 있게 해 주는 가벼운 버전의 앱입니다. 예를 들어, 사용자가 App Store에서 다운로드해 설치하는 도넛 가게 앱은 도넛 주문, 즐겨찾기 저장, 리워드 적립, 특별 할인 확인 같은 기능을 제공할 수 있습니다. 반면 그 도넛 가게의 App Clip은 전체 앱을 설치하지 않아도, 예를 들어 가게 근처에서 “donuts”를 검색할 때 곧바로 사용할 수 있습니다. 빠른 실행 경험과 빠른 주문 경험을 보장하기 위해 App Clip은 도넛 주문 기능만 제공합니다.

*호출 수단으로 App Clip Code가 사용되고, 음식 트럭용 App Clip 카드와 App Clip 화면을 거쳐 결과가 제공되는 흐름을 보여 주는 그림입니다.*

일정한 제약 조건을 충족하는 App Clip은 더 큰 크기를 가질 수 있으므로, 앱의 데모 버전 역할을 하는 App Clip도 제공할 수 있습니다. 더 큰 데모 크기를 활용하면 사용자가 구매나 구독 없이도 앱의 기능을 체험할 수 있습니다. 예를 들어 게임은 첫 번째 레벨을 플레이할 수 있는 App Clip을 제공할 수 있고, 피트니스 앱은 무료 운동 세션이 포함된 App Clip을 제공할 수 있습니다. 사용자가 게임의 첫 레벨을 마치거나 무료 운동을 끝내면, App Clip은 전체 앱을 설치하라는 프롬프트를 표시합니다.

### 훌륭한 사용자 경험 제공하기

App Clip은 사용자가 현실 세계의 작업을 가능한 한 빨리 해결하거나 새로운 앱을 부담 없이 체험하도록 돕는 정제된 사용자 경험을 제공합니다. 또한 App Clip은 홈 화면에 나타나지 않으며, 사용자가 전체 앱을 관리하듯 직접 관리하지도 않습니다. 대신 시스템은 일정 기간 사용되지 않은 App Clip을 기기에서 제거하므로, 정제된 사용자 경험을 제공하는 일이 더욱 중요합니다.

디자인 지침은 [App Clips Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/app-clips/overview/)를 참고하십시오.

### App Clip 제작 검토하기

App Clip의 기능은 빠른 실행 경험을 보장하고, 사용자 개인정보를 보호하며, 순간형 경험과 앱 데모에 필요한 리소스를 보존할 수 있도록 제한해야 합니다. App Clip을 만들기 전에 다음을 검토하십시오.

1. App Clip에서 사용할 수 있는 기술과, 좋은 사용자 경험을 보장하는 제약 조건을 검토합니다.
2. 앱 기능 중 어떤 부분이 좋은 App Clip이 될 수 있는지 식별합니다.
3. 사용자가 *invocation*을 통해 App Clip을 어떻게 발견하고 실행하는지, 그리고 훌륭한 실행 경험을 제공하기 위해 App Clip 경험과 invocation URL을 어떻게 구성하는지 학습합니다.

자세한 내용은 [Choosing the right functionality for your App Clip](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip) 및 [Configuring the launch experience of your App Clip](https://developer.apple.com/documentation/appclip/configuring-the-launch-experience-of-your-app-clip)을 참고하십시오.

App Clip에 넣을 기능과 invocation 방식을 정했다면 다음 작업을 진행합니다.

- Xcode 프로젝트와 코드를 수정합니다. 예를 들어 App Clip target을 추가하고 App Clip과 전체 앱 사이에서 코드를 공유합니다.
- invocation에 응답하고 invocation URL을 처리하는 코드를 추가합니다.
- App Store Connect에서 App Clip experience를 생성합니다.
- 필요하다면 App Clip을 웹사이트와 연결해 추가 invocation과 고급 App Clip experience를 지원합니다.
- 필요하다면 사용자가 App Clip을 가장 잘 발견하고 실행할 수 있도록 App Clip Code를 만듭니다.

:::topic-grid
## 핵심
- [App Clip에 적합한 기능 선택하기](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip): App Clip에서 사용할 수 있는 프레임워크를 검토하고, 훌륭한 App Clip이 될 기능을 식별합니다.
- [App Clip 경험 구성하기](https://developer.apple.com/documentation/appclip/configuring-the-launch-experience-of-your-app-clip): invocation URL, 기본 링크, 데모 링크, 고급 App Clip experience를 통해 사용자가 App Clip을 실행하는 방식을 검토합니다.
- [App Clips 업데이트](https://developer.apple.com/documentation/Updates/AppClips): App Clips의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 생성
- [Xcode로 App Clip 만들기](https://developer.apple.com/documentation/appclip/creating-an-app-clip-with-xcode): Xcode 프로젝트에 App Clip target을 추가하고 해당 전체 앱과 코드를 공유합니다.
- [Fruta: SwiftUI로 기능이 풍부한 앱 만들기](https://developer.apple.com/documentation/appclip/fruta-building-a-feature-rich-app-with-swiftui): widget과 App Clip을 제공하는 멀티플랫폼 앱을 만들기 위해 공유 코드베이스를 구축합니다.
- [Parent Application Identifiers Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.parent-application-identifiers): 정확히 하나의 항목을 포함하는 App Clip용 parent application identifier 목록입니다.
- [com.apple.developer.associated-appclip-app-identifiers](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.associated-appclip-app-identifiers): 정확히 하나의 항목을 포함하는 앱용 App Clip identifier 목록입니다.
- [com.apple.developer.on-demand-install-capable](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.on-demand-install-capable): 번들이 App Clip을 나타내는지 여부를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 실행
- [invocation에 응답하기](https://developer.apple.com/documentation/appclip/responding-to-invocations): invocation에 응답하는 코드를 추가하고 집중된 실행 경험을 제공합니다.
- [App Clip을 웹사이트와 연결하기](https://developer.apple.com/documentation/appclip/associating-your-app-clip-with-your-website): 웹사이트와 iOS 16.3 이하 기기에서의 invocation을 지원할 수 있도록 시스템이 App Clip을 검증하게 합니다.
- [웹사이트와 Messages 앱에서의 invocation 지원하기](https://developer.apple.com/documentation/appclip/supporting-invocations-from-your-website-and-the-messages-app): 웹사이트에 Smart App Banner와 App Clip 카드를 표시해 사용자가 탭으로 App Clip을 실행하도록 하고, Messages 앱에서의 invocation도 지원합니다.
- [사용자의 실제 위치 확인하기](https://developer.apple.com/documentation/appclip/confirming-a-person-s-physical-location): 개인정보를 존중하면서 사용자의 실제 위치를 빠르게 확인하는 코드를 추가합니다.
- [앱에서 다른 앱의 App Clip 실행하기](https://developer.apple.com/documentation/appclip/launching-another-app-s-app-clip-from-your-app): App Clip link로 다른 앱의 App Clip을 앱에서 실행할 수 있게 하고, Link Presentation 프레임워크로 풍부한 미리보기를 제공합니다.
- [APActivationPayload](https://developer.apple.com/documentation/appclip/apactivationpayload): 실행 시 App Clip에 전달되는 정보입니다.
- [NSAppClip](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppClip): App Clip이 추가 기능을 얻는 데 사용하는 키 모음입니다.
:::

:::topic-grid
## App Clip Code
- [App Clip Code 만들기](https://developer.apple.com/documentation/appclip/creating-app-clip-codes): NFC 통합형 또는 스캔 전용 App Clip Code를 사용해 사용자가 App Clip을 발견하도록 돕습니다.
- [App Clip Code에 URL 인코딩하기](https://developer.apple.com/documentation/appclip/encoding-a-url-in-an-app-clip-code): 효율적으로 인코딩할 수 있는 App Clip Code용 invocation URL을 선택합니다.
- [여러 App Clip Code를 실제 배포용으로 준비하기](https://developer.apple.com/documentation/appclip/preparing-multiple-app-clip-codes-for-production): 전문 인쇄 서비스에 보낼 수 있도록 App Clip Code를 준비합니다.
- [AR에서 App Clip Code와 상호 작용하기](https://developer.apple.com/documentation/appclip/interacting-with-app-clip-codes-in-ar): AR 경험에서 App Clip Code를 활용해 콘텐츠를 표시하고 서비스를 제공합니다.
:::

:::topic-grid
## App Clip에서 전체 앱으로 전환
- [App Clip 사용자에게 앱 추천하기](https://developer.apple.com/documentation/appclip/recommending-your-app-to-app-clip-users): App Clip 위에 오버레이를 표시해 사용자에게 전체 앱을 추천합니다.
- [App Clip과 전체 앱 사이에서 데이터 공유하기](https://developer.apple.com/documentation/appclip/sharing-data-between-your-app-clip-and-your-full-app): CloudKit, Sign in with Apple, 공유 user defaults/containers, keychain을 사용해 App Clip에서 앱으로 자연스럽게 전환되도록 합니다.
:::

:::topic-grid
## 알림
- [App Clip에서 알림 활성화하기](https://developer.apple.com/documentation/appclip/enabling-notifications-in-app-clips): App Clip이 짧은 기간 또는 연장된 기간 동안 알림을 예약하고 수신할 수 있도록 합니다.
:::

:::topic-grid
## Live Activities
- [App Clip으로 Live Activities 제공하기](https://developer.apple.com/documentation/appclip/offering-live-activities-with-your-app-clip): App Clip target에 widget extension을 추가하고 ActivityKit을 사용해 잠금 화면과 Dynamic Island에 Live Activities를 표시합니다.
:::

:::topic-grid
## 테스트
- [App Clip 실행 경험 테스트하기](https://developer.apple.com/documentation/appclip/testing-the-launch-experience-of-your-app-clip): App Clip invocation을 디버깅하고, 실행 경험을 테스트하며, 배포된 App Clip 구성이 올바른지 검증합니다.
:::

:::topic-grid
## 배포
- [App Clip 배포하기](https://developer.apple.com/documentation/appclip/distributing-your-app-clip): App Clip용 전체 앱을 archive하고, App Store Connect에 업로드하며, 테스터에게 배포하거나 App Store에 게시합니다.
:::
