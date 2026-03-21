---
route: /documentation/AppStoreReceipts
source_url: https://developer.apple.com/documentation/AppStoreReceipts
source_locale: en-US
section: docc
content_type: symbol
title: App Store Receipts
original_title: App Store Receipts
source_hash: 6d608fb64a6847b1ebcd827f7ace443dc5b65c59ff56bab321f89270c57f7fd6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:31+00:00'
last_translated_at: '2026-03-13T17:10:00+09:00'
---

# App Store Receipts

App Store에서 앱 및 In-App Purchase 영수증을 검증합니다.

## 개요

:::important Important
[verifyReceipt](https://developer.apple.com/documentation/appstorereceipts/verify-receipt) 엔드포인트는 더 이상 사용되지 않습니다. 서버에서 영수증을 검증하려면 [Validating receipts on the device](https://developer.apple.com/documentation/appstorereceipts/validating-receipts-on-the-device)의 단계를 서버에서 따르십시오.
:::

서버는 [verifyReceipt](https://developer.apple.com/documentation/appstorereceipts/verify-receipt) 엔드포인트에 접근해 앱 및 앱 내 거래 영수증을 검증할 수 있습니다. [shared secret](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-a-shared-secret-to-verify-receipts)와 함께 영수증을 App Store에 제출하면 앱 정보와 앱 내 구입 세부 사항을 영수증을 구성하는 필드에 담아 JSON 응답으로 돌려받습니다. 각 필드 또는 필드 조합은 사용자가 받을 서비스와 콘텐츠를 정의하는 데 활용할 수 있는 정보를 제공합니다.

앱이 [finishTransaction(_:)](https://developer.apple.com/documentation/StoreKit/SKPaymentQueue/finishTransaction(_:)) 또는 [finish()](https://developer.apple.com/documentation/StoreKit/Transaction/finish())를 사용해 완료로 표시하지 않은 앱 내 거래는 App Store 영수증에 남아 있습니다. 자동 갱신 구독, 비갱신 구독, 비소모성 항목은 영수증에 무기한 남아 있으며, [Get Transaction History V1](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Transaction-History-V1) 엔드포인트를 호출하면 고객 거래 기록에 표시됩니다.

자동 갱신 구독용 [responseBody.Latest_receipt_info](https://developer.apple.com/documentation/appstorereceipts/responsebody/latest_receipt_info-data.dictionary) 객체는 갱신 거래가 영수증에 무기한 남기 때문에 시간이 지날수록 커질 수 있습니다. 성능 최적화를 위해 App Store는 샌드박스 환경에서 오래된 거래를 제거하도록 영수증을 잘라낼 수 있습니다.

샌드박스 환경에서 영수증 검증을 테스트할 수 있습니다. 자세한 내용은 [Testing In-App Purchases with sandbox](https://developer.apple.com/documentation/StoreKit/testing-in-app-purchases-with-sandbox)와 [Test in-app purchases](https://developer.apple.com/help/app-store-connect/test-in-app-purchases-main/test-in-app-purchases)를 참고하십시오.

App Store의 영수증은 서버 측 영수증 검증 또는 온디바이스 검증으로 검증할 수 있습니다. 영수증 검증 옵션에 대한 자세한 내용은 [Choosing a receipt validation technique](https://developer.apple.com/documentation/StoreKit/choosing-a-receipt-validation-technique)을 참고하십시오.

:::note Related sessions from WWDC22
Session 110404: [Implement proactive in-app purchase restore](https://developer.apple.com/videos/play/wwdc2022/110404/).
:::

:::topic-grid
## 영수증 데이터
- [App Store receipt data types](https://developer.apple.com/documentation/appstorereceipts/app-store-receipt-data-types): 영수증에 반환되는 객체의 데이터 타입입니다.
:::

:::topic-grid
## 로컬 영수증 검증
- [Validating receipts on the device](https://developer.apple.com/documentation/appstorereceipts/validating-receipts-on-the-device): 기기에서 영수증을 디코드하고 파싱해 앱 영수증의 내용을 검증합니다.
:::

:::topic-grid
## 더 이상 사용되지 않음
- [verifyReceipt](https://developer.apple.com/documentation/appstorereceipts/verify-receipt): 검증을 위해 영수증을 App Store로 보냅니다.
- [requestBody](https://developer.apple.com/documentation/appstorereceipts/requestbody): App Store에 대한 요청과 함께 제출하는 JSON 내용입니다.
- [responseBody](https://developer.apple.com/documentation/appstorereceipts/responsebody): App Store 응답에서 반환되는 JSON 데이터입니다.
- [error](https://developer.apple.com/documentation/appstorereceipts/error): 요청이 성공하지 않았을 때 응답 본문에 반환되는 오류 정보입니다.
:::
