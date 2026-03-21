---
route: /documentation/StoreKit
source_url: https://developer.apple.com/documentation/StoreKit
source_locale: en-US
section: docc
content_type: symbol
title: StoreKit
original_title: StoreKit
source_hash: 42734af7a24ebe4201b8f99875779ebb882090cf2ddfcd059e44f41410d6b842
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:12:34+00:00'
last_translated_at: '2026-03-14T00:45:00+09:00'
---

# StoreKit

앱 내 구입과 App Store와의 상호 작용을 지원합니다.

## 개요

StoreKit 프레임워크를 사용하면 앱과 앱 내 구입에 대해 다음 기능과 서비스를 제공할 수 있습니다.

:::term-list
앱 내 구입: 콘텐츠와 서비스를 위한 앱 내 구입을 제공하고 홍보합니다.
앱 트랜잭션: App Store가 서명한 트랜잭션으로 고객의 앱 구매를 검증합니다.
메시지: 앱 안에서 App Store 메시지의 표시를 제어합니다.
리뷰: 고객에게 App Store 리뷰와 평점을 요청합니다.
추천: 고객이 App Store에서 구매할 수 있는 타사 콘텐츠를 추천합니다.
광고 네트워크 어트리뷰션: 광고가 유도한 앱 설치를 검증합니다. App Store 및 대체 마켓플레이스의 앱 광고 캠페인은 [AdAttributionKit](https://developer.apple.com/documentation/AdAttributionKit)을 참고하십시오.
:::

StoreKit 프레임워크는 또한 [External Purchase](https://developer.apple.com/documentation/storekit/external-purchase), [External link account](https://developer.apple.com/documentation/storekit/external-link-account), [PaymentMethodBinding](https://developer.apple.com/documentation/storekit/paymentmethodbinding), [StoreDownloaderExtension](https://developer.apple.com/documentation/storekit/storedownloaderextension)을 위한 기능도 제공합니다.

:::topic-grid
## 앱 내 구입
- [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase): Swift 기반 인터페이스를 사용해 Apple 플랫폼 전반에서 앱 안의 콘텐츠와 서비스를 제공합니다.
- [Understanding StoreKit workflows](https://developer.apple.com/documentation/storekit/understanding-storekit-workflows): StoreKit view를 사용해 여러 제품 유형이 있는 앱 내 상점을 구현합니다.
- [Getting started with In-App Purchase using StoreKit views](https://developer.apple.com/documentation/storekit/getting-started-with-in-app-purchases-using-storekit-views): SwiftUI와 StoreKit view를 사용해 앱 내 상점을 설정합니다.
:::

:::topic-grid
## 앱 트랜잭션
- [Supporting business model changes by using the app transaction](https://developer.apple.com/documentation/storekit/supporting-business-model-changes-by-using-the-app-transaction): 앱 트랜잭션에 접근해 고객이 언제 앱을 구매했는지와 어떤 기능에 대한 자격이 있는지를 판단합니다.
- [AppTransaction](https://developer.apple.com/documentation/storekit/apptransaction): 고객의 앱 구매를 나타내는 정보로, App Store가 암호학적으로 서명합니다.
:::

:::topic-grid
## 메시지
- [Message](https://developer.apple.com/documentation/storekit/message): 앱 안에서 App Store 메시지를 수신하고 표시하기 위한 인스턴스입니다.
- [Message.Reason](https://developer.apple.com/documentation/storekit/message/reason-swift.struct): App Store 메시지가 표시되는 이유입니다.
- [DisplayMessageAction](https://developer.apple.com/documentation/storekit/displaymessageaction): 적절한 경우 StoreKit에 App Store 메시지를 표시하도록 요청하는 인스턴스입니다.
:::

:::topic-grid
## 리뷰
- [Requesting App Store reviews](https://developer.apple.com/documentation/storekit/requesting-app-store-reviews): 사용자가 App Store에서 앱을 리뷰하도록 요청하는 모범 사례를 구현합니다.
- [RequestReviewAction](https://developer.apple.com/documentation/storekit/requestreviewaction): 적절한 경우 StoreKit에 App Store 평점 또는 리뷰를 요청하도록 지시하는 인스턴스입니다.
- [SKStoreReviewController](https://developer.apple.com/documentation/storekit/skstorereviewcontroller): 고객에게 App Store 평점과 리뷰를 요청하는 과정을 제어하는 객체입니다.
:::

:::topic-grid
## 추천
- [Offering media for sale in your app](https://developer.apple.com/documentation/storekit/offering-media-for-sale-in-your-app): 앱 안에서 사용자가 App Store의 미디어를 구매할 수 있게 합니다.
- [SKStoreProductViewController](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller): 고객이 App Store에서 미디어를 구매할 수 있는 페이지를 제공하는 view controller입니다.
- [SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay): 다른 앱이나 App Clip에 대응하는 전체 앱을 추천하는 데 사용할 수 있는 overlay를 표시하는 클래스입니다.
:::

:::topic-grid
## 백그라운드 자산 extension
- [StoreDownloaderExtension](https://developer.apple.com/documentation/storekit/storedownloaderextension): 시스템 구현을 사용해 Apple 호스팅 asset-pack 다운로드를 자동으로 예약하는 app extension입니다.
:::

:::topic-grid
## 결제 수단 바인딩
- [PaymentMethodBinding](https://developer.apple.com/documentation/storekit/paymentmethodbinding): Apple Account용 앱에서 결제 수단을 사용할 수 있게 하는 바인딩입니다.
:::

:::topic-grid
## 광고 네트워크 어트리뷰션
- [Ad network attribution](https://developer.apple.com/documentation/storekit/ad-network-attribution): 광고가 유도한 앱 설치를 검증합니다.
:::

:::topic-grid
## External Purchase
- [External Purchase](https://developer.apple.com/documentation/storekit/external-purchase): 자격을 갖춘 앱이 외부 구매를 제공할 수 있게 합니다.
:::

:::topic-grid
## External link account
- [External link account](https://developer.apple.com/documentation/storekit/external-link-account): 자격을 갖춘 앱이 계정 생성 또는 관리를 위해 외부 웹사이트로 연결할 수 있게 합니다.
:::

:::topic-grid
## Deprecated
- [SKCloudServiceSetupViewController](https://developer.apple.com/documentation/storekit/skcloudservicesetupviewcontroller): Apple Music 구독 같은 cloud service 설정을 수행하도록 돕는 view controller입니다.
- [SKCloudServiceController](https://developer.apple.com/documentation/storekit/skcloudservicecontroller): 사용자의 Music 보관함이 현재 어떤 기능을 사용할 수 있는지 판단하는 객체입니다.
:::

:::topic-grid
## 아티클
- [Supporting subscription offer codes in your app](https://developer.apple.com/documentation/storekit/supporting-subscription-offer-codes-in-your-app): App Store 또는 앱 내부에서 offer code를 사용하는 고객에게 구독 서비스를 제공합니다.
:::
