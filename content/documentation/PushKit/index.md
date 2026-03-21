---
route: /documentation/PushKit
source_url: https://developer.apple.com/documentation/PushKit
source_locale: en-US
section: docc
content_type: symbol
title: PushKit
original_title: PushKit
source_hash: be1a9cdf76b45e5f51af0ef1bbfc9c7375f77920a269e582aaa5b356d05373f7
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:39:24+00:00'
last_translated_at: '2026-03-14T01:09:00+09:00'
---

# PushKit

앱의 complication, file provider, VoIP 서비스와 관련된 push notification에 응답합니다.

## 개요

PushKit 프레임워크는 watchOS complication 업데이트, file provider 변경 대응, 수신 Voice-over-IP(VoIP) 통화 수신을 위한 특화된 알림을 지원합니다. PushKit 알림은 [User Notifications](https://developer.apple.com/documentation/UserNotifications) 프레임워크로 처리하는 알림과 다릅니다. 경고를 표시하거나, 앱 아이콘에 배지를 붙이거나, 소리를 재생하는 대신, PushKit 알림은 앱을 깨우거나 실행하고 응답할 시간을 제공합니다. PushKit과 User Notifications는 모두 Apple Push Notification service(APNs)를 사용해 사용자 기기에 push notification을 전달합니다.

PushKit 알림을 받으려면 앱이 [PKPushRegistry](https://developer.apple.com/documentation/pushkit/pkpushregistry) 객체를 만들고 이를 사용해 지원하는 알림 유형을 구성해야 합니다. 등록에 성공하면 PushKit은 현재 기기의 식별자와 push type을 담은 고유한 data token을 앱에 전달합니다. 이 token을 서버로 전달하고, 사용자에게 보내는 모든 알림에 이를 포함하십시오. APNs는 이 token을 사용해 올바른 유형의 알림을 사용자의 기기에 전달합니다.

서버를 APNs와 함께 동작하도록 구성하는 방법은 [Setting up a remote notification server](https://developer.apple.com/documentation/UserNotifications/setting-up-a-remote-notification-server)를 참고하십시오.

:::note Note
PushKit은 Apple Push Notification service(APNs)에 접근할 수 없는 일부 특수 사용 사례를 지원하지 않습니다. 이러한 사례를 지원해야 할 수 있는 시점에 대한 자세한 내용은 [iOS 10 and the Legacy VoIP Architecture](https://developer.apple.com/library/archive/qa/qa1938/_index.html#//apple_ref/doc/uid/DTS40017564)를 참고하십시오.
:::

:::topic-grid
## 등록
- [Supporting PushKit Notifications in Your App](https://developer.apple.com/documentation/pushkit/supporting-pushkit-notifications-in-your-app): 앱이 지원하는 PushKit 알림 유형을 선언하고, 이에 응답할 객체를 구성합니다.
- [PKPushRegistry](https://developer.apple.com/documentation/pushkit/pkpushregistry): PushKit 알림의 전달을 요청하고 수신을 처리하는 객체입니다.
- [PKPushRegistryDelegate](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate): 수신 PushKit 알림과 등록 이벤트를 처리할 때 사용하는 메서드입니다.
- [PKPushCredentials](https://developer.apple.com/documentation/pushkit/pkpushcredentials): 앱에 push notification을 전달할 때 사용하는 device token을 캡슐화하는 객체입니다.
:::

:::topic-grid
## Push 유형
- [Responding to VoIP Notifications from PushKit](https://developer.apple.com/documentation/pushkit/responding-to-voip-notifications-from-pushkit): 수신 Voice-over-IP(VoIP) push notification을 받고, 이를 사용해 사용자에게 시스템 통화 인터페이스를 표시합니다.
- [PKPushType](https://developer.apple.com/documentation/pushkit/pkpushtype): 지원하려는 push 유형을 반영하는 상수입니다.
:::

:::topic-grid
## Payload
- [PKPushPayload](https://developer.apple.com/documentation/pushkit/pkpushpayload): 수신한 PushKit 알림에 대한 정보를 담는 객체입니다.
:::

:::topic-grid
## 데이터 내보내기
- [Exporting delivery metrics logs](https://developer.apple.com/documentation/pushkit/exporting-delivery-metrics-logs): push notification metric을 다운로드하고 분석합니다.
- [Exporting broadcast push notification metrics](https://developer.apple.com/documentation/pushkit/exporting-broadcast-push-notification-metrics): 얼마나 많은 사용자가 broadcast 채널을 구독하는지, 그리고 얼마나 많은 메시지를 받는지 확인합니다.
:::

:::topic-grid
## 클래스
- [PKVoIPPushMetadata](https://developer.apple.com/documentation/pushkit/pkvoippushmetadata): 수신한 PushKit VoIP 알림에 대한 metadata를 담는 객체입니다.
:::
