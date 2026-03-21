---
route: /documentation/AdvancedCommerceAPI
source_url: https://developer.apple.com/documentation/AdvancedCommerceAPI
source_locale: en-US
section: docc
content_type: symbol
title: Advanced Commerce API
original_title: Advanced Commerce API
source_hash: 68fd396978d255cd88fd44b1ba0b3f7a66c979e7f5742fbea197270e5053a5f5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:41:40+00:00'
last_translated_at: '2026-03-13T23:51:00+09:00'
---

# Advanced Commerce API

예외적으로 큰 카탈로그의 사용자 정의 일회성 구매, 구독, 선택적 추가 항목이 있는 구독에 대해 App Store를 통한 In-App Purchase를 지원합니다.

## 개요

이 프레임워크를 사용하면 App Store 상거래 시스템을 사용하면서도 예외적으로 큰 일회성 구매, 구독, 선택적 추가 항목이 있는 구독 카탈로그를 제공할 수 있습니다. 이 API를 사용하는 앱은 자체 In-App Purchase 카탈로그, 즉 SKU를 호스팅하고 관리합니다. App Store 상거래 시스템은 종단 간 결제 처리, 글로벌 배포, 세금 지원, 고객 서비스를 담당합니다.

같은 앱에서 Advanced Commerce API와 StoreKit [In-App Purchase](https://developer.apple.com/documentation/StoreKit/in-app-purchase) API를 함께 사용할 수 있습니다. 두 API는 동일한 서명된 JWS 트랜잭션과 JWS 갱신 정보를 포함해 App Store 상거래 시스템을 사용합니다. In-App Purchase API로 제공하는 제품의 경우 App Store Connect에서 제품 식별자를 설정합니다. Advanced Commerce API로 제공하는 제품의 경우 자체 SKU 카탈로그를 호스팅하고 관리하며 런타임에 제품 세부 정보를 동적으로 추가합니다. 전체 설정 정보는 [Setting up your project for Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi/setting-up-your-project-for-advanced-commerce)를 참고합니다.

Advanced Commerce API 기능은 앱에서 StoreKit을 사용해 보내는 요청과 서버에서 보내는 엔드포인트 요청을 통해 사용할 수 있습니다. 이러한 요청을 인증하려면 JSON Web Token(JWT)을 생성합니다. App Store Server Library는 호출 인증용 JWT 생성 작업을 더 쉽게 해 주는 클라이언트를 제공합니다. 이 라이브러리에 대한 자세한 내용은 [Simplifying your implementation by using the App Store Server Library](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library)를 참고합니다. 호출 인증에 대한 자세한 내용은 [Authorizing API requests from your server](https://developer.apple.com/documentation/advancedcommerceapi/authorizing-server-calls)를 참고합니다.

서버에서 Advanced Commerce API를 호출하려면 Transport Layer Security(TLS) 프로토콜 1.2 이상을 지원해야 합니다.

:::important Important
Advanced Commerce API의 자격 요건과 액세스 신청 방법에 대한 자세한 내용은 [Advanced Commerce API](https://developer.apple.com/in-app-purchase/advanced-commerce-api/)를 참고합니다. Mini Apps Partner Program의 자격 요건과 액세스 신청 방법에 대한 자세한 내용은 [Mini Apps Partner Program](https://developer.apple.com/programs/mini-apps-partner/)을 참고합니다.
:::

:::topic-grid
## 핵심 항목
- [Setting up your project for Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi/setting-up-your-project-for-advanced-commerce): App Store Connect에서 앱을 구성하고, 서버를 설정하고, SKU를 준비합니다.
- [Setting up a link to manage subscriptions](https://developer.apple.com/documentation/advancedcommerceapi/setupmanagesubscriptions): 앱의 구독 관리 페이지로 이동하는 deep link를 생성합니다.
- [Advanced Commerce API changelog](https://developer.apple.com/documentation/advancedcommerceapi/changelog): Advanced Commerce API의 새 기능과 업데이트를 알아봅니다.
:::

:::topic-grid
## API 인증 및 rate limit
- [Authorizing API requests from your server](https://developer.apple.com/documentation/advancedcommerceapi/authorizing-server-calls): 서버에서 보내는 Advanced Commerce 요청을 인증하기 위한 JSON Web Token(JWT)을 생성합니다.
- [Identifying rate limits for Advanced Commerce APIs](https://developer.apple.com/documentation/advancedcommerceapi/ratelimits): Advanced Commerce API 엔드포인트에 적용되는 rate limit를 파악하고 처리합니다.
:::

:::topic-grid
## 일반 제품 ID 및 SKU
- [Setting up generic product identifiers](https://developer.apple.com/documentation/advancedcommerceapi/setting-up-generic-product-identifiers): Advanced Commerce API에 필요한 일반 제품 ID를 App Store Connect에서 구성합니다.
- [Creating SKUs for your In-App Purchases](https://developer.apple.com/documentation/advancedcommerceapi/creating-your-purchases): 앱 안에서 일회성 청구, 구독, 번들 구독을 정의하고 관리합니다.
- [Creating SKUs for the Mini Apps Partner Program](https://developer.apple.com/documentation/advancedcommerceapi/creating-skus-for-the-mini-app-partner-program): Mini Apps Partner Program의 일회성 청구 및 구독을 위한 표시 이름과 SKU를 정의합니다.
:::

:::topic-grid
## 세금 코드 및 가격
- [Specifying prices for Advanced Commerce SKUs](https://developer.apple.com/documentation/advancedcommerceapi/prices): 지원되는 소수 자릿수와 통화 milliunit 단위로 SKU 가격을 제공합니다.
- [Choosing tax codes for your SKUs](https://developer.apple.com/documentation/advancedcommerceapi/taxcodes): 앱이 앱 내 구입으로 제공하는 제품을 나타내는 SKU마다 세금 코드를 선택합니다.
- [Handling subscription price changes](https://developer.apple.com/documentation/advancedcommerceapi/handling-subscription-price-changes): 가격 변경을 시작하고 App Store를 통해 구독자와의 커뮤니케이션을 관리합니다.
:::

:::topic-grid
## 앱 내 API 요청
- [Sending Advanced Commerce API requests from your app](https://developer.apple.com/documentation/StoreKit/sending-advanced-commerce-api-requests-from-your-app): 서버에서 생성한 JSON Web Signature(JWS)로 인증되는 Advanced Commerce API 요청을 앱에서 보냅니다.
- [Generating JWS to sign App Store requests](https://developer.apple.com/documentation/StoreKit/generating-jws-to-sign-app-store-requests): 앱의 API 요청을 인증하기 위해 서버에서 서명된 JSON Web Signature(JWS) 문자열을 생성합니다.
:::

:::topic-grid
## 앱에서의 일회성 청구 생성
- [OneTimeChargeCreateRequest](https://developer.apple.com/documentation/advancedcommerceapi/onetimechargecreaterequest): 고객이 일회성 청구 제품을 구매할 때 앱이 제공하는 요청 데이터입니다.
- [OneTimeChargeItem](https://developer.apple.com/documentation/advancedcommerceapi/onetimechargeitem): 표시 이름, 가격, SKU, 메타데이터를 포함한 일회성 청구 제품의 세부 정보입니다.
:::

:::topic-grid
## 앱에서의 구독 생성
- [SubscriptionCreateRequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreaterequest): 고객이 자동 갱신 구독을 구매할 때 앱이 제공하는 요청 데이터입니다.
- [SubscriptionCreateItem](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreateitem): 구독 항목을 설명하는 데이터입니다.
:::

:::topic-grid
## 앱에서의 구독 수정
- [SubscriptionModifyInAppRequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyinapprequest): 자동 갱신 구독을 변경하기 위해 앱이 제공하는 요청 데이터입니다.
- [SubscriptionModifyAddItem](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyadditem): 자동 갱신 구독을 변경할 때 항목을 추가하기 위해 앱이 제공하는 데이터입니다.
- [SubscriptionModifyChangeItem](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifychangeitem): 자동 갱신 구독의 항목을 변경하기 위해 앱이 제공하는 데이터입니다.
- [SubscriptionModifyRemoveItem](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyremoveitem): 자동 갱신 구독에서 항목을 제거하기 위해 앱이 제공하는 데이터입니다.
- [SubscriptionModifyPeriodChange](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyperiodchange): 자동 갱신 구독의 기간을 변경하기 위해 앱이 제공하는 데이터입니다.
:::

:::topic-grid
## 앱에서의 구독 재활성화
- [SubscriptionReactivateInAppRequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest): 자동 갱신이 꺼진 구독을 다시 활성화하기 위해 앱이 제공하는 요청입니다.
- [SubscriptionReactivateItem](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateitem): 재활성화할 구독 내 항목입니다.
:::

:::topic-grid
## 서버에서의 구독 가격 변경
- [Change Subscription Price](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-price): 다음 갱신 시 자동 갱신 구독, 번들, 또는 구독 내 개별 항목의 가격을 인상하거나 인하합니다.
- [SubscriptionPriceChangeRequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangerequest): 자동 갱신 구독 가격을 변경하기 위해 사용하는 요청 본문입니다.
- [SubscriptionPriceChangeResponse](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionpricechangeresponse): 구독 가격 변경 요청 후 서명된 JWS 갱신 정보와 JWS 거래 정보를 담는 응답입니다.
:::

:::topic-grid
## 서버에서의 구독 취소
- [Cancel a Subscription](https://developer.apple.com/documentation/advancedcommerceapi/cancel-a-subscription): 자동 갱신을 꺼서 고객의 자동 갱신 구독을 취소합니다.
- [SubscriptionCancelRequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncancelrequest): 구독의 자동 갱신을 끄기 위한 요청 본문입니다.
- [SubscriptionCancelResponse](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncancelresponse): 성공적인 구독 취소에 대한 응답 본문입니다.
:::

:::topic-grid
## 서버에서의 구독 철회
- [Revoke Subscription](https://developer.apple.com/documentation/advancedcommerceapi/revoke-subscription): 고객의 구독과 구독에 포함된 모든 항목을 즉시 취소하고, 전액 또는 비례 환불을 요청합니다.
- [SubscriptionRevokeRequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionrevokerequest): 구독과 그 모든 항목을 즉시 종료하기 위해 제공하는 요청 본문입니다.
- [SubscriptionRevokeResponse](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionrevokeresponse): 성공적인 revoke-subscription 요청에 대한 응답 본문입니다.
:::

:::topic-grid
## 서버에서의 환불 요청
- [Request Transaction Refund](https://developer.apple.com/documentation/advancedcommerceapi/request-transaction-refund): 일회성 청구 또는 구독 거래에 대한 환불을 요청합니다.
- [RequestRefundRequest](https://developer.apple.com/documentation/advancedcommerceapi/requestrefundrequest): 거래에 대한 환불을 요청하기 위한 요청 본문입니다.
- [RequestRefundResponse](https://developer.apple.com/documentation/advancedcommerceapi/requestrefundresponse): 거래 환불 요청에 대한 응답 본문입니다.
- [RequestRefundItem](https://developer.apple.com/documentation/advancedcommerceapi/requestrefunditem): SKU, 환불 금액, 사유, 유형과 같은 항목 환불 요청 정보를 담습니다.
:::

:::topic-grid
## 서버에서의 구독 메타데이터 변경
- [Change Subscription Metadata](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-metadata): 구독의 청구나 서비스에 영향을 주지 않고, 구독과 연결된 SKU, 표시 이름, 설명을 업데이트합니다.
- [SubscriptionChangeMetadataRequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadatarequest): 구독 메타데이터를 변경하기 위해 제공하는 요청 본문입니다.
- [SubscriptionChangeMetadataResponse](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadataresponse): 성공적인 구독 메타데이터 변경에 대한 응답 본문입니다.
- [SubscriptionChangeMetadataDescriptors](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadatadescriptors): 변경할 구독 메타데이터, 즉 설명과 표시 이름입니다.
- [SubscriptionChangeMetadataItem](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadataitem): 변경할 항목의 메타데이터, 즉 SKU, 설명, 표시 이름입니다.
:::

:::topic-grid
## 서버에서의 마이그레이션
- [Migrate a Subscription to Advanced Commerce API](https://developer.apple.com/documentation/advancedcommerceapi/migrate-subscription-to-advanced-commerce-api): In-App Purchase로 구매한 구독을 Advanced Commerce API로 관리하는 구독으로 마이그레이션합니다.
- [SubscriptionMigrateRequest](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmigraterequest): descriptor, 항목, storefront 등 In-App Purchase에서 Advanced Commerce API로 구독을 마이그레이션하기 위해 제공하는 구독 세부 정보입니다.
- [SubscriptionMigrateResponse](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmigrateresponse): 구독이 Advanced Commerce API로 성공적으로 마이그레이션된 후 서명된 갱신 정보와 거래 정보를 담는 응답입니다.
- [SubscriptionMigrateItem](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmigrateitem): 마이그레이션된 구독 항목에 사용할 SKU, 설명, 표시 이름입니다.
- [SubscriptionMigrateRenewalItem](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmigraterenewalitem): 구독이 갱신될 때 마이그레이션된 구독 항목을 대체하는 항목 정보입니다.
- [SubscriptionMigrateDescriptors](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmigratedescriptors): 사용자가 관리하는 대상으로 마이그레이션할 구독의 설명과 표시 이름입니다.
:::

:::topic-grid
## 객체 및 타입
- [Data types](https://developer.apple.com/documentation/advancedcommerceapi/datatypes): Advanced Commerce API를 위한 객체와 데이터 타입입니다.
:::

:::topic-grid
## 서명된 거래 정보
- [JWSRenewalInfo](https://developer.apple.com/documentation/advancedcommerceapi/jwsrenewalinfo): App Store가 서명한 구독 갱신 정보로, JSON Web Signature(JWS) 형식입니다.
- [JWSTransaction](https://developer.apple.com/documentation/advancedcommerceapi/jwstransaction): App Store가 서명한 거래 정보로, JSON Web Signature(JWS) Compact Serialization 형식입니다.
:::

:::topic-grid
## 오류 처리
- [Error messages and codes](https://developer.apple.com/documentation/advancedcommerceapi/errorcodes): Advanced Commerce API의 오류 메시지와 코드입니다.
:::
