---
route: /documentation/AccessoryNotifications
source_url: https://developer.apple.com/documentation/AccessoryNotifications
source_locale: en-US
section: docc
content_type: symbol
title: Accessory Notifications
original_title: Accessory Notifications
source_hash: 528c215b6f987e2ee5bbc9302b7db71eb7afda64b17ff123198fc6679cb9c3b3
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:20:39+00:00'
last_translated_at: '2026-03-13T08:55:00+00:00'
---

# Accessory Notifications

개발한 액세서리에서 전달된 iOS 시스템 알림을 수신합니다.

## 개요

Accessory Notifications 프레임워크를 사용하면 액세서리 컴패니언 앱이 사용자에게 알림 전달을 요청하고, 확장 모델을 통해 시스템으로부터 알림 내용을 받을 수 있습니다. 사용자는 기기의 모든 앱, 어떤 앱도 아님, 또는 일부 앱의 알림만 전달하도록 선택할 수 있습니다.

:::important Important
이 프레임워크는 iPhone만 지원합니다. 이 프레임워크를 사용하는 앱은 어느 지역의 기기에서도 개발하고 테스트할 수 있습니다. 현재 이 프레임워크는 개발용 또는 Ad Hoc 테스트용으로만 빌드됩니다. App Store 제출, TestFlight, 대체 배포는 이후 시점에 지원될 예정입니다.

고객이 설치한 앱은 EU에 위치하고 EU 국가 또는 지역의 Apple 계정으로 로그인한 기기에서만 이 프레임워크를 사용할 수 있습니다.
:::

## 알림 전달 요청하기

컴패니언 앱에서 [requestForwarding(for:)](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/requestforwarding(for:))를 호출해 사용자에게 알림 전달 허용을 요청합니다. 시스템은 [AccessorySetupKit](https://developer.apple.com/documentation/AccessorySetupKit)으로부터 받은 참조를 통해 액세서리를 식별합니다. 이 메서드는 사용자의 선택을 나타내는 [ForwardingDecision](https://developer.apple.com/documentation/accessorynotifications/forwardingdecision)을 반환합니다.

## 알림 수신 및 처리

알림을 받으려면 [Accessory Transport Extension](https://developer.apple.com/documentation/AccessoryTransportExtension) 프레임워크의 [AccessoryDataProvider](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) 확장에서 [NotificationsForwarding.AccessoryNotificationsHandler](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler)를 구현하세요. 시스템은 알림 도착, 업데이트, 제거 시 handler의 메서드를 호출합니다. [AccessoryNotification](https://developer.apple.com/documentation/accessorynotifications/accessorynotification) 구조체에 들어 있는 표시용 콘텐츠, 아이콘, 관련 파일 첨부, 상호 작용 등의 정보 중에서 액세서리에 필요한 부분만 선별하세요.

선별한 데이터를 세션의 [sendMessage(_:)](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryFeatureSession/sendMessage(_:)) 메서드를 사용해 시스템에 반환합니다. 시스템은 앱의 [AccessoryTransportSecurity](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSecurity) 확장을 통해 제공한 키로 데이터를 암호화합니다. 그런 다음 시스템은 암호화된 데이터를 액세서리로 전송하기 위해 앱의 [AccessoryTransportAppExtension](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportAppExtension)에 전달합니다.

## 알림 복호화 및 표시

액세서리는 암호화된 알림 데이터를 수신한 뒤 [HPKE (RFC9180)](https://datatracker.ietf.org/doc/rfc9180/) 복호화를 구현하여 알림 세부 정보를 파싱합니다. 알림에 대해 경고를 전송할지 결정하려면 [AlertingContext](https://developer.apple.com/documentation/accessorynotifications/alertingcontext)를 사용하세요. [shouldAlert](https://developer.apple.com/documentation/accessorynotifications/alertingcontext/shouldalert) 속성은 시스템의 알림 로직과 일치하는 권장 동작을 제공합니다.

:::note Note
향후 릴리스에서는 알림 수신 확인이나 사용자 상호 작용과 같은 정보를 액세서리로부터 수신하는 기능을 지원할 예정입니다.
:::

:::topic-grid
## 필수 항목
- [액세서리에서 iOS 알림 수신하기](https://developer.apple.com/documentation/accessorynotifications/receiving-ios-notifications-on-an-accessory): 액세서리용 알림을 관리하는 사용자 정의 앱 확장을 생성합니다.
:::

:::topic-grid
## 권한 부여
- [AccessoryNotificationCenter](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter): 앱이 알림 전달 권한을 요청할 수 있게 해 주는 클래스입니다.
- [ForwardingDecision](https://developer.apple.com/documentation/accessorynotifications/forwardingdecision): 알림 전달 권한 프롬프트에 대한 가능한 결정입니다.
:::

:::topic-grid
## 알림 수신
- [NotificationsForwarding](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding): 액세서리의 데이터 제공자 확장에서 알림 전달을 처리하는 클래스입니다.
- [NotificationsForwarding.AccessoryNotificationsHandler](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/accessorynotificationshandler): 확장에서 알림 수명주기 이벤트를 처리하는 메서드를 정의하는 프로토콜입니다.
- [NotificationsForwarding.Session](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/session): 확장과 시스템 사이의 통신을 가능하게 하는 세션 객체입니다.
- [NotificationsForwarding.HandlerFactory](https://developer.apple.com/documentation/accessorynotifications/notificationsforwarding/handlerfactory): 알림 handler를 생성하는 factory용 타입 별칭입니다.
:::

:::topic-grid
## 데이터 선별 및 알림 처리
- [AccessoryNotification](https://developer.apple.com/documentation/accessorynotifications/accessorynotification): iOS가 액세서리에 제공하는 알림 세부 정보를 담는 구조체입니다.
- [AlertingContext](https://developer.apple.com/documentation/accessorynotifications/alertingcontext): 알림에 대해 어떤 방식으로 경고해야 하는지 지침을 제공하는 구조체입니다.
- [AlertCoordinating](https://developer.apple.com/documentation/accessorynotifications/alertcoordinating): 액세서리가 알림을 경고하는 과정을 완료했는지 시스템에 전달하는 프로토콜입니다.
:::

:::topic-grid
## 상호 작용 지원
- [AccessoryNotificationManaging](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationmanaging): 시스템에 알림 응답을 전달할 수 있게 해 주는 프로토콜입니다.
- [AccessoryNotificationManagerFactory](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationmanagerfactory): 시스템 알림 관리자에 접근할 수 있게 해 주는 factory 클래스입니다.
- [NotificationResponse](https://developer.apple.com/documentation/accessorynotifications/notificationresponse): 사용자의 알림 응답입니다.
:::

:::topic-grid
## 오류
- [AccessoryError](https://developer.apple.com/documentation/accessorynotifications/accessoryerror): Accessory Notifications 프레임워크가 throw할 수 있는 오류입니다.
:::
