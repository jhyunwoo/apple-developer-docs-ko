---
route: /documentation/AppStoreServerAPI
source_url: https://developer.apple.com/documentation/AppStoreServerAPI
source_locale: en-US
section: docc
content_type: symbol
title: App Store Server API
original_title: App Store Server API
source_hash: bd93ded8139d80885a4f0138fe6ae164463364583b09b4f808d28416047521ad
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:47:52+00:00'
last_translated_at: '2026-03-14T00:13:00+09:00'
---

# App Store Server API

서버에서 고객의 App Store 거래를 관리합니다.

## 개요

App Store Server API는 서버에서 호출해 고객의 In-App Purchase에 대한 정보를 요청하고 제공하는 REST API입니다. 이 API가 반환하는 거래 및 구독 갱신 정보는 App Store가 [JSON Web Signature (JWS)](https://datatracker.ietf.org/doc/html/rfc7515) 명세를 사용해 서명합니다. 대부분의 엔드포인트는 사용자가 제공한 거래 식별자로 표시되는, 앱의 단일 고객에 대한 데이터를 반환합니다.

App Store Server API는 고객 기기에 앱이 설치되어 있는 상태와는 무관합니다. App Store 서버는 고객이 기기에 앱을 설치했는지, 제거했는지, 다시 설치했는지와 관계없이 고객의 In-App Purchase 기록을 기준으로 정보를 반환합니다.

이 API는 다음 기능을 제공합니다.

- **거래 및 자동 갱신 구독 상태.** [Get Transaction Info](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-info)를 호출해 단일 거래 정보를 얻거나, [Get Transaction History](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-history)를 사용해 고객의 전체 거래 기록을 가져옵니다. 최신 구독 상태는 [Get All Subscription Statuses](https://developer.apple.com/documentation/appstoreserverapi/get-all-subscription-statuses)를 호출합니다. 이 정보를 사용해 서버에 있는 고객의 구매 정보를 최신 상태로 유지합니다.
- **환불 정보.** [Get Refund History](https://developer.apple.com/documentation/appstoreserverapi/get-refund-history)를 호출해 고객의 환불 기록을 가져옵니다. 고객이 In-App Purchase 환불을 요청하고, 서버가 [App Store Server Notifications V2](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2)로부터 `CONSUMPTION_REQUEST` [notificationType](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType)을 수신한 뒤에는 [Send Consumption Information](https://developer.apple.com/documentation/appstoreserverapi/send-consumption-information) 엔드포인트를 사용해 App Store에 정보를 보냅니다. 이 데이터는 환불 판단에 도움이 됩니다.
- **App Store Server Notifications 기록 및 테스트.** [Get Notification History](https://developer.apple.com/documentation/appstoreserverapi/get-notification-history)를 호출해 지난 180일 동안(또는 sandbox 환경에서는 30일) 서버가 놓쳤을 수 있는 알림을 요청합니다. [Request a Test Notification](https://developer.apple.com/documentation/appstoreserverapi/request-a-test-notification)과 [Get Test Notification Status](https://developer.apple.com/documentation/appstoreserverapi/get-test-notification-status)를 호출해 서버가 [App Store Server Notifications V2](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) 엔드포인트에서 알림을 제대로 수신하는지 테스트합니다.
- **구독 갱신일 연장.** [Extend a Subscription Renewal Date](https://developer.apple.com/documentation/appstoreserverapi/extend-a-subscription-renewal-date)와 관련 엔드포인트를 호출해 일시적인 서비스 중단, 취소된 이벤트, 라이브 스트리밍 이벤트의 중단에 대해 고객에게 보상하기 위해 유료 활성 구독의 갱신일을 연장합니다. 자세한 내용은 [Extending the renewal date for auto-renewable subscriptions](https://developer.apple.com/documentation/appstoreserverapi/extending-the-renewal-date-for-auto-renewable-subscriptions)를 참고합니다.
- **주문 정보 조회.** [Look Up Order ID](https://developer.apple.com/documentation/appstoreserverapi/look-up-order-id)를 호출해 고객이 이메일로 받는 App Store 영수증에 있는 주문 ID를 기반으로 In-App Purchase 정보를 가져옵니다.
- **앱 거래 정보 및 app account token 설정.** [Get App Transaction Info](https://developer.apple.com/documentation/appstoreserverapi/get-app-transaction-info)를 호출해 앱의 원래 구매일과 버전 같은 고객의 앱 구매 세부 정보를 가져옵니다. [Set App Account Token](https://developer.apple.com/documentation/appstoreserverapi/set-app-account-token)을 사용하면 고객이 앱 외부에서 In-App Purchase를 수행할 때 app account token을 설정하거나 기존 거래의 값을 업데이트할 수 있습니다.

서버에서 App Store Server API를 사용하려면 Transport Layer Security(TLS) 프로토콜 1.2 이상을 지원해야 합니다.

이 API의 최신 변경 사항은 [App Store Server API changelog](https://developer.apple.com/documentation/appstoreserverapi/app-store-server-api-changelog)에서 확인합니다. App Store Server API 관련 비디오는 [Apple Developer website](https://developer.apple.com/videos/all-videos/?q=%22App%20Store%20Server%20API%22)에서 찾아볼 수 있습니다.

### API 호출 인증

API 호출에는 인증을 위한 JSON Web Token(JWT)이 필요합니다. 토큰 생성에 사용하는 키는 조직의 App Store Connect 계정에서 얻습니다. 키 생성은 [Creating API keys to authorize API requests](https://developer.apple.com/documentation/appstoreserverapi/creating-api-keys-to-authorize-api-requests)를 참고합니다. 키를 사용해 토큰을 생성하고 API 요청을 보내는 방법은 [Generating JSON Web Tokens for API requests](https://developer.apple.com/documentation/appstoreserverapi/generating-json-web-tokens-for-api-requests)를 참고합니다.

완전하고 서명된 토큰을 만든 뒤에는 요청의 authorization header에 bearer token으로 제공합니다. 새로운 API 요청마다 새 토큰을 생성하거나, 만료될 때까지 토큰을 재사용할 수 있습니다.

### App Store Server Library를 사용해 JWT 생성, 거래 검증 등 수행하기

App Store Server Library는 Apple이 제공하는 오픈 소스 라이브러리이며 네 가지 언어로 제공됩니다. 호출 인증용 JWT 생성 등을 포함해 App Store Server API 채택을 쉽게 해 주는 클라이언트를 제공합니다. 자세한 내용은 [Simplifying your implementation by using the App Store Server Library](https://developer.apple.com/documentation/appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library)와 WWDC23 세션 [Meet the App Store Server Library](https://developer.apple.com/videos/play/wwdc2023/10143/)를 참고합니다.

### sandbox 환경에서 테스트

모든 App Store Server API 엔드포인트는 [Look Up Order ID](https://developer.apple.com/documentation/appstoreserverapi/look-up-order-id)를 제외하고 sandbox 환경에서 테스트할 수 있습니다. sandbox 환경에 접근하려면 다음 base URL을 사용해 엔드포인트에 요청을 보냅니다.

```other
https://api.storekit-sandbox.itunes.apple.com/
```

예를 들어 sandbox 환경에서 [Get Transaction History](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-history)를 호출하려면 다음 sandbox URL로 요청을 보냅니다.

```other
https://api.storekit-sandbox.itunes.apple.com/inApps/v2/history/{transactionId}
```

경로 안의 `/inApps`는 대소문자를 구분한다는 점에 유의합니다.

[transactionId](https://developer.apple.com/documentation/appstoreserverapi/transactionid)를 매개변수로 받는 엔드포인트는 해당 거래 식별자를 생성한 동일한 환경에서 호출해야 합니다. 환경 정보는 [JWSTransactionDecodedPayload](https://developer.apple.com/documentation/appstoreserverapi/jwstransactiondecodedpayload)의 [environment](https://developer.apple.com/documentation/appstoreserverapi/environment) 속성에 포함되어 있습니다.

환경 정보가 없다면 다음 단계를 따릅니다.

1. production URL을 사용해 엔드포인트를 호출합니다. 호출이 성공하면 해당 거래 식별자는 production 환경에 속합니다.
2. `4040010` 오류 코드 [TransactionIdNotFoundError](https://developer.apple.com/documentation/appstoreserverapi/transactionidnotfounderror)를 받으면 sandbox 환경을 사용해 엔드포인트를 호출합니다.
3. 호출이 성공하면 거래 식별자는 sandbox 환경에 속합니다. 호출이 `4040010` 오류 코드로 실패하면 해당 거래 식별자는 두 환경 어디에도 존재하지 않습니다.

:::topic-grid
## 핵심 항목
- [Simplifying your implementation by using the App Store Server Library](https://developer.apple.com/documentation/appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library): Apple의 오픈 소스 라이브러리를 사용해 호출 인증용 JSON Web Token(JWT)을 생성하고, 거래를 검증하고, 영수증에서 거래 식별자를 추출하는 등 여러 작업을 수행합니다.
- [Creating API keys to authorize API requests](https://developer.apple.com/documentation/appstoreserverapi/creating-api-keys-to-authorize-api-requests): JSON Web Token에 서명하고 API 요청을 인증하는 데 사용하는 API 키를 생성합니다.
- [Generating JSON Web Tokens for API requests](https://developer.apple.com/documentation/appstoreserverapi/generating-json-web-tokens-for-api-requests): App Store Server API와 External Purchase Server API 요청을 인증하기 위해 개인 키로 서명한 JSON Web Token을 생성합니다.
- [Identifying rate limits](https://developer.apple.com/documentation/appstoreserverapi/identifying-rate-limits): App Store Server API 엔드포인트에 적용되는 rate limit를 식별하고 코드에서 처리합니다.
- [App Store Server API changelog](https://developer.apple.com/documentation/appstoreserverapi/app-store-server-api-changelog): App Store Server API의 새 기능과 업데이트를 알아봅니다.
:::

:::topic-grid
## In-App Purchase 기록
- [Get Transaction History](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-history): 앱에 대한 고객의 앱 내 구입 거래 기록을 가져옵니다.
- [HistoryResponse](https://developer.apple.com/documentation/appstoreserverapi/historyresponse): 앱에 대한 고객 거래 기록을 담는 응답입니다.
:::

:::topic-grid
## 거래 정보
- [Get Transaction Info](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-info): 앱의 단일 거래에 대한 정보를 가져옵니다.
- [TransactionInfoResponse](https://developer.apple.com/documentation/appstoreserverapi/transactioninforesponse): 단일 거래에 대한 서명된 거래 정보를 담는 응답입니다.
:::

:::topic-grid
## 앱 거래 정보
- [Get App Transaction Info](https://developer.apple.com/documentation/appstoreserverapi/get-app-transaction-info): 앱에 대한 고객의 앱 거래 정보를 가져옵니다.
- [AppTransactionInfoResponse](https://developer.apple.com/documentation/appstoreserverapi/apptransactioninforesponse): 고객에 대한 서명된 앱 거래 정보를 담는 응답입니다.
:::

:::topic-grid
## 구독 상태
- [Get All Subscription Statuses](https://developer.apple.com/documentation/appstoreserverapi/get-all-subscription-statuses): 앱 안의 고객 자동 갱신 구독 전체 상태를 가져옵니다.
- [StatusResponse](https://developer.apple.com/documentation/appstoreserverapi/statusresponse): 앱 안의 고객 자동 갱신 구독 전체에 대한 상태 정보를 담는 응답입니다.
:::

:::topic-grid
## App Account Token
- [Set App Account Token](https://developer.apple.com/documentation/appstoreserverapi/set-app-account-token): 고객이 앱 외부에서 수행한 구매에 대해 app account token 값을 설정하거나, 기존 거래에서 값을 업데이트합니다.
- [UpdateAppAccountTokenRequest](https://developer.apple.com/documentation/appstoreserverapi/updateappaccounttokenrequest): app account token 값을 담는 요청 본문입니다.
:::

:::topic-grid
## 주문 ID 조회
- [Look Up Order ID](https://developer.apple.com/documentation/appstoreserverapi/look-up-order-id): order ID를 사용해 영수증에서 고객의 앱 내 구입을 가져옵니다.
- [orderId](https://developer.apple.com/documentation/appstoreserverapi/orderid): 앱 내 구입용 App Store 영수증에 있는 고객의 주문 ID입니다.
- [OrderLookupResponse](https://developer.apple.com/documentation/appstoreserverapi/orderlookupresponse): 주문 조회 상태와 주문 안의 앱 내 구입에 대한 서명된 거래 배열을 포함하는 응답입니다.
:::

:::topic-grid
## 소비 정보
- [Send Consumption Information](https://developer.apple.com/documentation/appstoreserverapi/send-consumption-information): 서버가 consumption request 알림을 수신한 뒤 App Store에 In-App Purchase의 소비 정보를 보냅니다.
- [ConsumptionRequest](https://developer.apple.com/documentation/appstoreserverapi/consumptionrequest): In-App Purchase의 소비 정보를 담는 요청 본문입니다.
:::

:::topic-grid
## 환불 조회
- [Get Refund History](https://developer.apple.com/documentation/appstoreserverapi/get-refund-history): 앱에 대한 고객의 환불된 앱 내 구입 전체를 paginated list로 가져옵니다.
- [RefundHistoryResponse](https://developer.apple.com/documentation/appstoreserverapi/refundhistoryresponse): 서명된 JSON Web Signature(JWS) 환불 거래 배열과 페이징 정보를 담는 응답입니다.
:::

:::topic-grid
## 구독 갱신일 연장
- [Extending the renewal date for auto-renewable subscriptions](https://developer.apple.com/documentation/appstoreserverapi/extending-the-renewal-date-for-auto-renewable-subscriptions): 구독 갱신일을 연장해 적격 활성 구독자에게 서비스 중단을 보상합니다.
- [Extend a Subscription Renewal Date](https://developer.apple.com/documentation/appstoreserverapi/extend-a-subscription-renewal-date): 원래 거래 식별자를 사용해 고객 활성 구독의 갱신일을 연장합니다.
- [Extend Subscription Renewal Dates for All Active Subscribers](https://developer.apple.com/documentation/appstoreserverapi/extend-subscription-renewal-dates-for-all-active-subscribers): 구독의 제품 식별자를 사용해 적격 활성 구독자 전체의 갱신일을 연장합니다.
- [Get Status of Subscription Renewal Date Extensions](https://developer.apple.com/documentation/appstoreserverapi/get-status-of-subscription-renewal-date-extensions): 갱신일 연장 요청이 완료되었는지 확인하고, 성공 또는 실패한 연장의 최종 개수를 제공합니다.
- [ExtendRenewalDateRequest](https://developer.apple.com/documentation/appstoreserverapi/extendrenewaldaterequest): 개별 구독에 대한 구독 갱신 연장 데이터를 담는 요청 본문입니다.
- [ExtendRenewalDateResponse](https://developer.apple.com/documentation/appstoreserverapi/extendrenewaldateresponse): 개별 갱신일 연장이 성공했는지와 관련 세부 정보를 나타내는 응답입니다.
- [MassExtendRenewalDateRequest](https://developer.apple.com/documentation/appstoreserverapi/massextendrenewaldaterequest): 적격 활성 구독자 전체에 적용할 구독 갱신 연장 데이터를 담는 요청 본문입니다.
- [MassExtendRenewalDateResponse](https://developer.apple.com/documentation/appstoreserverapi/massextendrenewaldateresponse): 서버가 구독 갱신일 연장 요청을 성공적으로 받았음을 나타내는 응답입니다.
- [MassExtendRenewalDateStatusResponse](https://developer.apple.com/documentation/appstoreserverapi/massextendrenewaldatestatusresponse): 적격 구독자 전체의 구독 갱신일 연장 요청 현재 상태를 나타내는 응답입니다.
:::

:::topic-grid
## App Store Server Notifications 기록
- [Get Notification History](https://developer.apple.com/documentation/appstoreserverapi/get-notification-history): App Store 서버가 서버로 보내려고 시도한 알림 목록을 가져옵니다.
- [NotificationHistoryRequest](https://developer.apple.com/documentation/appstoreserverapi/notificationhistoryrequest): 알림 기록용 요청 본문입니다.
- [NotificationHistoryResponse](https://developer.apple.com/documentation/appstoreserverapi/notificationhistoryresponse): 앱에 대한 App Store Server Notifications 기록을 담는 응답입니다.
- [notificationHistoryResponseItem](https://developer.apple.com/documentation/appstoreserverapi/notificationhistoryresponseitem): 서명된 알림 payload와 서버의 첫 전송 시도 결과를 포함하는 App Store 서버 알림 기록입니다.
:::

:::topic-grid
## App Store Server Notifications 테스트
- [Request a Test Notification](https://developer.apple.com/documentation/appstoreserverapi/request-a-test-notification): App Store Server Notifications에 테스트 알림을 서버로 보내도록 요청합니다.
- [Get Test Notification Status](https://developer.apple.com/documentation/appstoreserverapi/get-test-notification-status): 서버로 보낸 App Store 서버 테스트 알림의 상태를 확인합니다.
- [SendTestNotificationResponse](https://developer.apple.com/documentation/appstoreserverapi/sendtestnotificationresponse): 테스트 알림 토큰을 담는 응답입니다.
- [CheckTestNotificationResponse](https://developer.apple.com/documentation/appstoreserverapi/checktestnotificationresponse): App Store 서버 테스트 알림의 내용과 서버 결과를 담는 응답입니다.
:::

:::topic-grid
## JWS 헤더 및 payload
- [JWSDecodedHeader](https://developer.apple.com/documentation/appstoreserverapi/jwsdecodedheader): 거래 또는 갱신 정보를 담는 디코딩된 JSON Web Signature(JWS) header입니다.
- [JWSAppTransaction](https://developer.apple.com/documentation/appstoreserverapi/jwsapptransaction): App Store가 서명한 앱 거래 정보로, JSON Web Signature(JWS) Compact Serialization 형식입니다.
- [JWSAppTransactionDecodedPayload](https://developer.apple.com/documentation/appstoreserverapi/jwsapptransactiondecodedpayload): 앱 거래 정보를 담는 디코딩된 payload입니다.
- [JWSTransaction](https://developer.apple.com/documentation/appstoreserverapi/jwstransaction): App Store가 서명한 거래 정보로, JSON Web Signature(JWS) Compact Serialization 형식입니다.
- [JWSTransactionDecodedPayload](https://developer.apple.com/documentation/appstoreserverapi/jwstransactiondecodedpayload): 거래 정보를 담는 디코딩된 payload입니다.
- [JWSRenewalInfo](https://developer.apple.com/documentation/appstoreserverapi/jwsrenewalinfo): App Store가 서명한 구독 갱신 정보로, JSON Web Signature(JWS) 형식입니다.
- [JWSRenewalInfoDecodedPayload](https://developer.apple.com/documentation/appstoreserverapi/jwsrenewalinfodecodedpayload): 자동 갱신 구독의 갱신 정보를 담는 디코딩된 payload입니다.
- [Data types](https://developer.apple.com/documentation/appstoreserverapi/data-types): 디코딩된 거래 및 갱신 정보 payload에 사용할 데이터 타입을 참고합니다.
:::

:::topic-grid
## 오류 정보
- [Error codes](https://developer.apple.com/documentation/appstoreserverapi/error-codes): App Store Server API 응답이 반환하는 오류 코드를 이해합니다.
:::

:::topic-grid
## 사용 중단됨
- [Get Transaction History V1](https://developer.apple.com/documentation/appstoreserverapi/get-transaction-history-v1): 완료된 소모성 앱 내 구입을 제외한 고객의 앱 내 구입 거래 기록을 가져옵니다.
- [Get Refund History V1](https://developer.apple.com/documentation/appstoreserverapi/get-refund-history-v1): 앱에 대한 고객의 환불된 앱 내 구입을 최대 50개까지 가져옵니다.
- [Send Consumption Information V1](https://developer.apple.com/documentation/appstoreserverapi/send-consumption-information-v1): 서버가 consumption request 알림을 수신한 뒤 소모성 In-App Purchase 또는 자동 갱신 구독의 소비 정보를 App Store에 보냅니다.
- [ConsumptionRequestV1](https://developer.apple.com/documentation/appstoreserverapi/consumptionrequestv1): 소비 정보를 담는 요청 본문입니다.
- [RefundLookupResponse](https://developer.apple.com/documentation/appstoreserverapi/refundlookupresponse): 서명된 JSON Web Signature(JWS) 거래 배열을 담는 응답입니다.
:::
