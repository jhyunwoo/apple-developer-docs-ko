---
route: /documentation/ExternalPurchaseServerAPI
source_url: https://developer.apple.com/documentation/ExternalPurchaseServerAPI
source_locale: en-US
section: docc
content_type: symbol
title: External Purchase Server API
original_title: External Purchase Server API
source_hash: fc2e821e4c3503359e491c4aef068493c63135676b213e27b22d4d4c33cbd2f1
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:18+00:00'
last_translated_at: '2026-03-13T10:02:00+00:00'
---

# External Purchase Server API

앱이 디지털 상품 및 서비스에 대한 외부 구매를 제공할 때 받는 토큰에 대해 Apple로 전송하는 리포트를 보내고 관리합니다.

## 개요

서버에서 이 REST API를 호출해 외부 구매 토큰과 해당 토큰에 관련된 고객 거래를 보고합니다. 앱이 [External Purchase](https://developer.apple.com/documentation/StoreKit/external-purchase) API를 사용하고, 다음 중 하나를 이용해 디지털 상품 및 서비스에 대한 대체 결제 옵션을 제공하는 경우 이 API를 사용하세요.

- *Payment Service Providers (PSP)*: 고객이 앱 안에서 거래를 완료할 수 있게 해 주는 대체 결제 처리자입니다.
- *Linking out to purchase*: 고객을 외부 웹사이트나 선택한 배포 채널로 보내 디지털 상품 및 서비스 거래를 완료하도록 하는 방식입니다.

거래로 이어지지 않은 토큰을 포함해 모든 토큰을 보고하고, 토큰과 연결된 거래도 보고하세요. 범위와 리포트 시점 기대치를 포함한 보고 요구 사항에 대한 자세한 내용은 유럽 연합 App Store의 대체 결제 옵션 사용 관련 문서 중 [Commission, transaction reports, and payments](https://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu#commission-reports-and-payments) 섹션을 참고하세요.

### API 호출 인증하기

이 API를 호출하려면 인증용 JSON Web Token(JWT)이 필요합니다. JWT를 생성하는 데 사용할 키는 조직의 App Store Connect 계정에서 얻습니다. 키 생성 방법은 [Creating API keys to authorize API requests](https://developer.apple.com/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests)를 참고하세요. 생성한 키로 토큰을 만들고 API 요청을 보내는 방법은 [Generating JSON Web Tokens for API requests](https://developer.apple.com/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests)를 참고하세요.

### 외부 구매 토큰 및 거래 보고하기

고객이 외부 구매를 시작하면 앱이나 웹사이트는 토큰을 받습니다. 여러분은 토큰과 그 토큰에 연결된 거래를 보고해야 합니다. 토큰을 받는 방식에 대한 자세한 내용은 [Receiving and decoding external purchase tokens](https://developer.apple.com/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens)를 참고하세요. 리포트를 보내려면 각 토큰마다 [Send External Purchase Report](https://developer.apple.com/documentation/externalpurchaseserverapi/send-external-purchase-report) 엔드포인트를 호출하세요. 다음 모든 경우에 리포트를 보내야 합니다.

- 고객이 하나 이상의 거래를 완료했을 때, line item을 포함하여 토큰을 보고하는 경우
- 고객이 어떤 거래도 완료하지 않았을 때, line item 없이 토큰을 보고하는 경우
- 시스템에 기록되지 않은 토큰에 대한 App Store Server Notification을 받았을 때, 인식되지 않은 토큰을 보고하는 경우
- 중복된 `ACQUISITION` 및 `SERVICES` 토큰을 보고하는 경우

자세한 내용은 [Reporting tokens with transactions](https://developer.apple.com/documentation/externalpurchaseserverapi/reportwithtransactions)와 [Reporting unrecognized and transactionless tokens](https://developer.apple.com/documentation/externalpurchaseserverapi/reportwithouttransactions)를 참고하세요.

한 번 성공적으로 전송한 리포트가 나중에 잘못된 것으로 확인되면 제출 내용을 정정해야 합니다. 자세한 내용은 [Reporting corrections](https://developer.apple.com/documentation/externalpurchaseserverapi/reportcorrections)를 참고하세요.

### 리포트 조회하기

이전에 Apple에 보낸 리포트를 가져오려면 [Retrieve External Purchase Report](https://developer.apple.com/documentation/externalpurchaseserverapi/retrieve-external-purchase-report) 엔드포인트를 호출하세요. 어떤 리포트를 가져올지는 리포트를 전송할 때 사용한 것과 같은 `requestIdentifier` 값을 사용해 지정합니다.

### 미보고 토큰에 대한 알림 받기

App Store 서버는 다음 경우에 [App Store Server Notifications V2](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) 엔드포인트로 `EXTERNAL_PURCHASE_TOKEN` [notificationType](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType)을 보냅니다.

- `UNREPORTED` subtype을 사용해 미보고 토큰을 알리는 경우
- `ACTIVE_TOKEN_REMINDER` subtype을 사용해 활성 custom link token을 다시 알리는 경우

`EXTERNAL_PURCHASE_TOKEN` 알림을 받았다면, 알림이 지정한 토큰에 대한 리포트를 보내세요. 서버 장애처럼 알림을 놓쳤을 가능성을 확인하려면 [Get Notification History](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Notification-History) 엔드포인트에 요청을 보내 App Store Server Notifications가 서버로 전송하려고 시도한 알림 목록을 가져옵니다.

알림에 대한 자세한 내용은 [Enabling App Store Server Notifications](https://developer.apple.com/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications)를 참고하세요. 서버의 [App Store Server Notifications V2](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) 엔드포인트를 구성해 version 2 알림을 받도록 하세요.

### Sandbox 환경으로 테스트하기

Sandbox 환경에서 앱을 테스트하면 [External Purchase](https://developer.apple.com/documentation/StoreKit/external-purchase) API는 그 환경에서만 유효한 토큰을 반환합니다. 이 토큰은 `externalPurchaseId`가 “`SANDBOX`” 문자열로 시작합니다. 서버의 토큰 보고 구현을 테스트하려면 Sandbox 토큰에 대한 리포트를 [Send External Purchase Report](https://developer.apple.com/documentation/externalpurchaseserverapi/send-external-purchase-report) 엔드포인트의 Sandbox URL로 보내세요.

:::important Important
Sandbox 환경에서 생성되는 external purchase token은 테스트 전용입니다. Sandbox 토큰과 External Purchase Server API의 sandbox URL을 통해 제출하는 테스트 거래 데이터는 실제 거래가 아닙니다.
:::

:::topic-grid
## 필수 항목
- [Creating API keys to authorize API requests](https://developer.apple.com/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests): JSON Web Token에 서명하고 API 요청을 인증하는 데 사용하는 API 키를 생성합니다.
- [Generating JSON Web Tokens for API requests](https://developer.apple.com/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests): App Store Server API와 External Purchase Server API 요청을 인증하기 위해 개인 키로 서명한 JSON Web Token을 생성합니다.
- [External Purchase Server API changelog](https://developer.apple.com/documentation/externalpurchaseserverapi/changelog): External Purchase Server API의 새 기능과 업데이트를 알아봅니다.
:::

:::topic-grid
## 외부 구매 토큰
- [Receiving and decoding external purchase tokens](https://developer.apple.com/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens): 거래를 Apple에 보고하는 데 사용하는 외부 구매 토큰을 수신하고 디코딩합니다.
:::

:::topic-grid
## 외부 구매 보고
- [Send External Purchase Report](https://developer.apple.com/documentation/externalpurchaseserverapi/send-external-purchase-report): 외부 구매 토큰과 관련 거래에 대한 필수 정보를 보고합니다.
- [ExternalPurchaseReport](https://developer.apple.com/documentation/externalpurchaseserverapi/externalpurchasereport): 단일 토큰에 대한 외부 구매 리포트 내용입니다.
- [SendReportSuccessResponse](https://developer.apple.com/documentation/externalpurchaseserverapi/sendreportsuccessresponse): 요청 식별자를 포함하며 서버가 외부 구매 리포트를 성공적으로 수신했음을 나타내는 응답입니다.
- [SendReportErrorResponse](https://developer.apple.com/documentation/externalpurchaseserverapi/sendreporterrorresponse): line item의 오류 세부 정보를 포함해 외부 구매 리포트가 성공하지 않았음을 나타내는 오류 응답입니다.
:::

:::topic-grid
## 외부 구매 리포트 거래
- [Reporting tokens with transactions](https://developer.apple.com/documentation/externalpurchaseserverapi/reportwithtransactions): 일회성 청구, 구독 및 갱신, 환불을 포함하여 완료된 거래로 이어진 외부 구매 토큰에 대한 리포트를 생성합니다.
- [Reporting corrections](https://developer.apple.com/documentation/externalpurchaseserverapi/reportcorrections): 성공적으로 제출한 거래에서 오류를 발견하거나 조정 사항이 있을 경우 정정 리포트를 제출합니다.
- [OneTimeBuyLineItem](https://developer.apple.com/documentation/externalpurchaseserverapi/onetimebuylineitem): 일회성 청구 거래를 나타내는 line item입니다.
- [RefundLineItem](https://developer.apple.com/documentation/externalpurchaseserverapi/refundlineitem): 환불 거래를 나타내는 line item입니다.
- [SubscriptionBuyLineItem](https://developer.apple.com/documentation/externalpurchaseserverapi/subscriptionbuylineitem): 구독 관련 이벤트 또는 거래를 나타내는 line item입니다.
- [Line item fields](https://developer.apple.com/documentation/externalpurchaseserverapi/lineitems): 외부 구매 리포트에서 단일 거래 또는 정정을 설명하는 속성입니다.
:::

:::topic-grid
## 거래 없는 외부 구매 리포트
- [Reporting unrecognized and transactionless tokens](https://developer.apple.com/documentation/externalpurchaseserverapi/reportwithouttransactions): 완료된 거래로 이어지지 않은 외부 구매 토큰, 중복 토큰, 또는 App Store 서버 알림으로 알게 된 토큰에 대한 리포트를 생성합니다.
:::

:::topic-grid
## 외부 구매 리포트 조회
- [Retrieve External Purchase Report](https://developer.apple.com/documentation/externalpurchaseserverapi/retrieve-external-purchase-report): 요청 식별자를 제공해 외부 구매 리포트를 가져옵니다.
- [RetrieveReportSuccessResponse](https://developer.apple.com/documentation/externalpurchaseserverapi/retrievereportsuccessresponse): 성공을 나타내며 외부 구매 리포트 데이터를 포함하는 응답입니다.
:::

:::topic-grid
## 오류 처리
- [Error messages and codes](https://developer.apple.com/documentation/externalpurchaseserverapi/errorcodes): 리포트와 엔드포인트에 대한 오류 메시지와 코드입니다.
:::
