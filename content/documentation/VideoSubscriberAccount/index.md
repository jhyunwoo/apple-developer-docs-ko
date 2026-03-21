---
route: /documentation/VideoSubscriberAccount
source_url: https://developer.apple.com/documentation/VideoSubscriberAccount
source_locale: en-US
section: docc
content_type: symbol
title: Video Subscriber Account
original_title: Video Subscriber Account
source_hash: bb2743b573247d236009376fc1396da5503f0c428ea655f4648f3c10048941aa
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:53+00:00'
last_translated_at: '2026-03-13T17:35:00+09:00'
---

# Video Subscriber Account

TV provider 및 Apple TV 앱 기능을 지원합니다.

## 개요

`VideoSubscriberAccount`는 TV provider의 인증 서비스와 안전하게 통신해야 하는 앱을 만드는 데 도움이 되는 API를 제공합니다. 이 프레임워크는 사용자가 구독을 보유하고 있는지 여부와 그 구독의 세부 사항도 Apple TV 앱에 알려 줍니다.

:::topic-grid
## 핵심 사항
- [Video Subscriber Account updates](https://developer.apple.com/documentation/Updates/VideoSubscriberAccount): Video Subscriber Account의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## TV provider 인증
- [VSAccountManager](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanager): 앱의 인증 요청을 TV provider의 인증 서비스와 조정하는 객체입니다.
:::

:::topic-grid
## TV 앱 통합
- [VSAppleSubscription](https://developer.apple.com/documentation/videosubscriberaccount/vsapplesubscription-swift.struct): Apple 스트리밍 서비스 고객과 그 고객의 구독입니다.
- [VSSubscriptionRegistrationCenter](https://developer.apple.com/documentation/videosubscriberaccount/vssubscriptionregistrationcenter): 시스템이 Apple TV 앱에 제공하는 구독 정보를 저장하는 객체입니다.
- [VSAccountApplicationProvider](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountapplicationprovider): 앱에서 앱별 provider를 표시하는 객체입니다.
:::

:::topic-grid
## 사용자 계정 관리
- [Signing people in to their media accounts automatically](https://developer.apple.com/documentation/videosubscriberaccount/signing-people-in-to-media-apps-automatically): 사용자의 Apple Account에 로그인 토큰을 관리해 미디어 스트리밍 앱의 single sign-on을 구현합니다.
- [VSUserAccountManager](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager): 앱의 사용자 계정 동작을 조정하는 객체입니다.
- [VSUserAccount](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccount-swift.struct): 사용자의 계정을 나타내는 객체입니다.
:::

:::topic-grid
## 오류
- [VSErrorDomain](https://developer.apple.com/documentation/videosubscriberaccount/vserrordomain): 프레임워크의 모든 오류에 대한 domain입니다.
- [VSErrorInfoKeySAMLResponse](https://developer.apple.com/documentation/videosubscriberaccount/vserrorinfokeysamlresponse): 구독 provider의 SAML 오류 응답입니다.
- [VSErrorInfoKeySAMLResponseStatus](https://developer.apple.com/documentation/videosubscriberaccount/vserrorinfokeysamlresponsestatus): 구독 provider의 SAML 오류 응답 상태 코드입니다.
- [VSErrorInfoKeyAccountProviderResponse](https://developer.apple.com/documentation/videosubscriberaccount/vserrorinfokeyaccountproviderresponse): 계정 provider의 오류 응답 객체입니다.
- [VSErrorInfoKeyUnsupportedProviderIdentifier](https://developer.apple.com/documentation/videosubscriberaccount/vserrorinfokeyunsupportedprovideridentifier): 지원되지 않는 구독 provider의 식별자입니다.
- [VSError](https://developer.apple.com/documentation/videosubscriberaccount/vserror): 프레임워크 오류 domain의 오류 정보입니다.
- [VSError.Code](https://developer.apple.com/documentation/videosubscriberaccount/vserror/code): 프레임워크 오류 domain의 오류 코드입니다.
:::

:::topic-grid
## 더 이상 사용되지 않음
- [VSSubscription](https://developer.apple.com/documentation/videosubscriberaccount/vssubscription): 구독자의 콘텐츠 접근을 설명하는 객체입니다.
:::
