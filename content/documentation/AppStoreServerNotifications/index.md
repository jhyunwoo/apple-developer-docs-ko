---
route: /documentation/AppStoreServerNotifications
source_url: https://developer.apple.com/documentation/AppStoreServerNotifications
source_locale: en-US
section: docc
content_type: symbol
title: App Store Server Notifications
original_title: App Store Server Notifications
source_hash: dc73932889e24f4b39edb9166d37fb7fe792218dedf1c2cf6b8b77a541d43cbb
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:54:12+00:00'
last_translated_at: '2026-03-13T19:05:00+09:00'
---

# App Store Server Notifications

App Store의 서버 알림으로 In-App Purchase 이벤트를 실시간으로 모니터링하고, 보고되지 않은 외부 구매 토큰을 파악합니다.

## 개요

App Store Server Notifications는 In-App Purchase 이벤트에 대한 실시간 알림과, 보고되지 않은 외부 구매 토큰에 대한 알림을 보내는 서버 간 서비스입니다. 알림에 포함된 데이터를 사용해 사용자 계정 데이터베이스를 업데이트하고, 앱 내 구입 환불을 모니터링하고 대응하십시오. [External Purchase](https://developer.apple.com/documentation/StoreKit/external-purchase) API 관련 알림은 [externalPurchaseToken](https://developer.apple.com/documentation/appstoreservernotifications/externalpurchasetoken)을 참고하십시오.

:::important 중요
[App Store Server Notifications V1](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v1) 엔드포인트와 version 1 알림인 [notification_type](https://developer.apple.com/documentation/appstoreservernotifications/notification_type)은 지원이 중단되었습니다. 대신 version 2 알림을 받으려면 서버에 [App Store Server Notifications V2](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v2) 엔드포인트를 구현하십시오.
:::

App Store의 서버 알림을 받으려면 App Store Connect에 서버의 HTTPS URL을 제공하십시오. 프로덕션 환경과 샌드박스 환경 알림을 모두 수신하도록 opt in하십시오. 자세한 내용은 [Enabling App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/enabling-app-store-server-notifications)를 참고하십시오.

서버는 모든 서버 간 알림 POST를 파싱하고, 해석하고, 응답할 책임이 있습니다. 자세한 내용은 [Receiving App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/receiving-app-store-server-notifications)와 [Responding to App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/responding-to-app-store-server-notifications)를 참고하십시오.

### 앱 내 구입 알림 처리

알림은 구매, 구독 갱신, 오퍼 사용, 환불 등을 포함한 앱 내 구입 수명 주기의 이벤트를 다룹니다. 알림 유형의 전체 목록은 [App Store Server Notifications V2](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v2)의 [notificationType](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)을 참고하십시오.

비즈니스 로직에 따라 notification type과 transaction 및 구독 갱신 정보를 함께 사용해 고객의 서비스를 업데이트하거나 프로모션 오퍼를 제시할 수 있습니다.

### 외부 구매 토큰 알림 처리

[notificationType](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype)이 `EXTERNAL_PURCHASE_TOKEN`이고 [subtype](https://developer.apple.com/documentation/appstoreservernotifications/subtype)이 `UNREPORTED`인 경우, Apple이 앱을 위해 외부 구매 토큰을 생성했지만 해당 토큰에 대한 보고를 아직 받지 못했음을 의미합니다. 이 알림에는 [responseBodyV2DecodedPayload](https://developer.apple.com/documentation/appstoreservernotifications/responsebodyv2decodedpayload)의 [externalPurchaseToken](https://developer.apple.com/documentation/appstoreservernotifications/externalpurchasetoken) 필드에 토큰이 포함됩니다. 시스템에서 그 토큰을 인식하지 못하는 경우를 포함해, 토큰 정보를 사용하여 Apple에 이를 보고하십시오. 관련 transaction이 있든 없든 토큰을 보고하려면 [External Purchase Server API](https://developer.apple.com/documentation/ExternalPurchaseServerAPI)의 [Send External Purchase Report](https://developer.apple.com/documentation/ExternalPurchaseServerAPI/Send-External-Purchase-Report) 엔드포인트를 호출하십시오.

토큰 보고 요구 사항에 대한 자세한 내용은 [Using alternative payment options on the App Store in the European Union](https://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu/)를 참고하십시오.

### 서버 설정 테스트

서버가 알림을 받고 있는지 확인하려면 [App Store Server API](https://developer.apple.com/documentation/AppStoreServerAPI)의 [Request a Test Notification](https://developer.apple.com/documentation/AppStoreServerAPI/Request-a-Test-Notification) 엔드포인트를 호출하여 App Store 서버가 [notificationType](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype) `TEST` 알림을 보내도록 요청하십시오. 받은 `testNotificationToken`을 사용해 [Get Test Notification Status](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Test-Notification-Status) 엔드포인트를 호출하면 서버가 테스트 알림에 어떻게 응답하는지 확인할 수 있습니다.

App Store 서버는 `TEST` 알림을 version 2 알림 형식으로 전송합니다. 하지만 App Store Connect에 version 1 또는 version 2 알림 URL 중 어느 것을 구성했는지와 상관없이 서버로 전송합니다. App Store Connect에서 URL을 구성하는 방법에 대한 자세한 내용은 [Enter a URL for App Store server notifications](https://help.apple.com/app-store-connect/#/dev0067a330b)을 참고하십시오.

:::topic-grid
## 핵심 사항
- [Enabling App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/enabling-app-store-server-notifications): 앱 내 구입 이벤트와 보고되지 않은 외부 구매 토큰에 대한 알림을 받도록 서버를 구성하고 HTTPS URL을 제공합니다.
- [Receiving App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/receiving-app-store-server-notifications): 알림 POST를 수신하고 파싱하는 서버 측 코드를 구현합니다.
- [Responding to App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications/responding-to-app-store-server-notifications): 알림 POST의 성공 여부를 나타내는 HTTP 상태 코드를 보냅니다.
- [App Store Server Notifications changelog](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-changelog): App Store Server Notifications 서비스의 변경 사항을 알아봅니다.
:::

:::topic-grid
## 서버 알림 버전 2
- [App Store Server Notifications V2](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-v2): version 2 알림을 받기 위해 App Store Connect에 보안 서버 URL을 지정합니다.
- [responseBodyV2](https://developer.apple.com/documentation/appstoreservernotifications/responsebodyv2): App Store가 version 2 서버 알림에서 보내는 응답 본문입니다.
- [responseBodyV2DecodedPayload](https://developer.apple.com/documentation/appstoreservernotifications/responsebodyv2decodedpayload): version 2 알림 데이터를 포함하는 디코드된 payload입니다.
- [notificationType](https://developer.apple.com/documentation/appstoreservernotifications/notificationtype): App Store가 version 2 알림을 보내는 In-App Purchase 또는 외부 구매 이벤트를 설명하는 타입입니다.
- [subtype](https://developer.apple.com/documentation/appstoreservernotifications/subtype): version 2의 일부 알림 유형에 대해 세부 정보를 제공하는 문자열입니다.
:::

:::topic-grid
## 지원 중단됨
- [App Store Server Notifications Version 1](https://developer.apple.com/documentation/appstoreservernotifications/app-store-server-notifications-version-1): App Store Server Notifications version 1을 수신, 파싱, 해석합니다.
:::
