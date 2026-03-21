---
route: /documentation/UserNotifications
source_url: https://developer.apple.com/documentation/UserNotifications
source_locale: en-US
section: docc
content_type: symbol
title: User Notifications
original_title: User Notifications
source_hash: abfe17bb8b4e5444563e4aa5d824f9e3ccc451f11068c7c9a22f170610ba8073
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:15:00+00:00'
last_translated_at: '2026-03-13T16:45:00+09:00'
---

# User Notifications

서버에서 사용자의 기기로 사용자 대상 알림을 푸시하거나, 앱에서 로컬로 생성합니다.

## 개요

사용자 대상 알림은 앱이 사용자의 기기에서 실행 중인지 여부와 관계없이 앱 사용자에게 중요한 정보를 전달합니다. 예를 들어 스포츠 앱은 사용자가 좋아하는 팀이 득점했을 때 이를 알려 줄 수 있습니다. 알림은 앱에 정보를 다운로드하고 인터페이스를 업데이트하라고 지시할 수도 있습니다. 알림은 경고를 표시하고, 사운드를 재생하고, 앱 아이콘에 배지를 표시할 수 있습니다.

![iOS 기기의 잠금 화면과 홈 화면에 표시된 알림 인터페이스입니다.](https://developer.apple.com)

알림은 앱에서 로컬로 생성하거나, 직접 관리하는 서버에서 원격으로 생성할 수 있습니다. *로컬 알림*의 경우 앱이 알림 콘텐츠를 만들고, 알림 전달을 트리거할 시간이나 위치 같은 조건을 지정합니다. *원격 알림*의 경우 회사의 서버가 push notification을 생성하고 Apple Push Notification service(APNs)가 이를 사용자 기기로 전달합니다.

이 프레임워크를 사용해 다음을 수행하십시오.

- 앱이 지원하는 알림 유형을 정의합니다.
- 알림 유형과 연결된 사용자 정의 action을 정의합니다.
- 로컬 알림 전달을 예약합니다.
- 이미 전달된 알림을 처리합니다.
- 사용자가 선택한 action에 응답합니다.

시스템은 로컬 및 원격 알림을 적시에 전달하기 위해 최선을 다하지만 전달이 보장되지는 않습니다. PushKit 프레임워크는 VoIP 및 watchOS complication처럼 특정 유형의 알림에 대해 더 신속한 전달 메커니즘을 제공합니다. 자세한 내용은 [PushKit](https://developer.apple.com/documentation/PushKit)을 참고하십시오.

Safari 16.0 이상 웹 페이지의 경우, Safari와 다른 브라우저에서 동작하는 [Push API](https://www.w3.org/TR/push-api/) 코드를 사용해 직접 관리하는 서버에서 원격 알림을 생성하십시오.

:::note Note
Siri는 알림 API를 통해 앱이 제공한 온디바이스 정보를 사용해 검색, News, Safari 및 기타 앱에서 사용자에게 제안을 제공할 수 있습니다. 사용자는 언제든지 앱에 대한 Siri 및 검색 설정에서 이 기능을 허용하도록 변경할 수 있습니다.
:::

디자인 가이드는 [Human Interface Guidelines > Notifications](https://developer.apple.com/design/human-interface-guidelines/ios/system-capabilities/notifications/)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [User Notifications updates](https://developer.apple.com/documentation/Updates/UserNotifications): User Notifications의 중요한 변경 사항을 알아봅니다.
- [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications): 알림에 응답해 경고를 표시하고 사운드를 재생하고 앱 아이콘에 배지를 표시할 권한을 요청합니다.
:::

:::topic-grid
## 알림 관리
- [UNUserNotificationCenter](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter): 앱이나 app extension의 알림 관련 활동을 관리하는 중심 객체입니다.
- [UNUserNotificationCenterDelegate](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate): 들어오는 알림을 처리하고 알림 action에 응답하는 인터페이스입니다.
- [UNNotificationSettings](https://developer.apple.com/documentation/usernotifications/unnotificationsettings): 알림 관련 설정과 앱의 권한 부여 상태를 관리하는 객체입니다.
:::

:::topic-grid
## 원격 알림
- [Setting up a remote notification server](https://developer.apple.com/documentation/usernotifications/setting-up-a-remote-notification-server): 알림을 생성해 사용자 기기로 푸시합니다.
- [Sending push notifications using command-line tools](https://developer.apple.com/documentation/usernotifications/sending-push-notifications-using-command-line-tools): 기본 macOS 명령줄 도구를 사용해 Apple Push Notification service(APNs)로 push notification을 보냅니다.
- [Testing notifications using the Push Notification Console](https://developer.apple.com/documentation/usernotifications/testing-notifications-using-the-push-notification-console): 테스트 알림을 보내고 전달 로그에 접근해 Apple Push Notification service(APNs) 통합을 테스트합니다.
:::

:::topic-grid
## 알림 요청
- [Scheduling a notification locally from your app](https://developer.apple.com/documentation/usernotifications/scheduling-a-notification-locally-from-your-app): 사용자의 주의를 끌고 싶을 때 앱에서 알림을 생성하고 예약합니다.
- [UNNotificationRequest](https://developer.apple.com/documentation/usernotifications/unnotificationrequest): 알림 콘텐츠와 전달 트리거 조건을 포함하는 로컬 알림 예약 요청입니다.
- [UNNotification](https://developer.apple.com/documentation/usernotifications/unnotification): 시스템이 앱에 전달하는 로컬 또는 원격 알림 데이터입니다.
:::

:::topic-grid
## Safari의 push notification
- [Sending web push notifications in web apps and browsers](https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers): 브라우저 간 표준을 따라 Safari, 다른 브라우저, 웹 앱에서 동작하는 push notification을 보낼 수 있도록 웹 서버와 웹사이트를 업데이트합니다.
:::

:::topic-grid
## 알림 콘텐츠
- [Implementing communication notifications](https://developer.apple.com/documentation/usernotifications/implementing-communication-notifications): intent를 사용해 앱의 communication notification을 구성하고 표시합니다.
- [UNNotificationContentProviding](https://developer.apple.com/documentation/usernotifications/unnotificationcontentproviding): 시스템이 사용자 알림과 관련된 컨텍스트를 제공할 때 사용하는 프로토콜입니다.
- [UNNotificationActionIcon](https://developer.apple.com/documentation/usernotifications/unnotificationactionicon): action과 연결된 아이콘입니다.
- [UNMutableNotificationContent](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent): 편집 가능한 알림 콘텐츠입니다.
- [UNNotificationContent](https://developer.apple.com/documentation/usernotifications/unnotificationcontent): 편집할 수 없는 알림 콘텐츠입니다.
- [UNNotificationAttachment](https://developer.apple.com/documentation/usernotifications/unnotificationattachment): 알림과 연결된 미디어 파일입니다.
- [UNNotificationSound](https://developer.apple.com/documentation/usernotifications/unnotificationsound): 알림 전달 시 재생되는 사운드입니다.
- [UNNotificationSoundName](https://developer.apple.com/documentation/usernotifications/unnotificationsoundname): 사운드 파일 이름을 제공하는 문자열입니다.
:::

:::topic-grid
## 트리거
- [UNCalendarNotificationTrigger](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger): 시스템이 특정 날짜와 시간에 알림을 전달하게 하는 트리거 조건입니다.
- [UNTimeIntervalNotificationTrigger](https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger): 지정한 시간이 지난 후 시스템이 알림을 전달하게 하는 트리거 조건입니다.
- [UNLocationNotificationTrigger](https://developer.apple.com/documentation/usernotifications/unlocationnotificationtrigger): 사용자의 기기가 지정한 지리적 영역에 들어가거나 나갈 때 시스템이 알림을 전달하게 하는 트리거 조건입니다.
- [UNPushNotificationTrigger](https://developer.apple.com/documentation/usernotifications/unpushnotificationtrigger): Apple Push Notification Service(APNs)가 알림을 보냈음을 나타내는 트리거 조건입니다.
- [UNNotificationTrigger](https://developer.apple.com/documentation/usernotifications/unnotificationtrigger): 로컬 또는 원격 알림 전달을 트리거하는 하위 클래스들의 공통 동작입니다.
:::

:::topic-grid
## 알림 카테고리와 사용자 action
- [Declaring your actionable notification types](https://developer.apple.com/documentation/usernotifications/declaring-your-actionable-notification-types): 알림을 구분하고 알림 인터페이스에 action 버튼을 추가합니다.
- [UNNotificationCategory](https://developer.apple.com/documentation/usernotifications/unnotificationcategory): 앱이 지원하는 알림 유형과 시스템이 표시하는 사용자 정의 action입니다.
- [UNNotificationAction](https://developer.apple.com/documentation/usernotifications/unnotificationaction): 시스템이 전달한 알림에 응답해 앱이 수행하는 작업입니다.
- [UNTextInputNotificationAction](https://developer.apple.com/documentation/usernotifications/untextinputnotificationaction): 사용자가 직접 입력한 텍스트를 받는 action입니다.
:::

:::topic-grid
## 알림 응답
- [Handling notifications and notification-related actions](https://developer.apple.com/documentation/usernotifications/handling-notifications-and-notification-related-actions): 앱의 사용자 정의 action 처리를 포함해 시스템 알림 인터페이스에서의 사용자 상호 작용에 응답합니다.
- [UNNotificationResponse](https://developer.apple.com/documentation/usernotifications/unnotificationresponse): 사용자의 actionable notification 응답입니다.
- [UNTextInputNotificationResponse](https://developer.apple.com/documentation/usernotifications/untextinputnotificationresponse): 사용자가 입력하거나 받아쓴 사용자 정의 텍스트를 포함하는 actionable notification 응답입니다.
:::

:::topic-grid
## 알림 서비스 app extension
- [Modifying content in newly delivered notifications](https://developer.apple.com/documentation/usernotifications/modifying-content-in-newly-delivered-notifications): 원격 알림이 사용자의 iOS 기기에 표시되기 전에 payload를 수정합니다.
- [UNNotificationServiceExtension](https://developer.apple.com/documentation/usernotifications/unnotificationserviceextension): 원격 알림이 사용자에게 전달되기 전에 콘텐츠를 수정하는 객체입니다.
:::

:::topic-grid
## entitlement
- [APS Environment Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/aps-environment): push notification용 환경입니다.
- [APS Environment (macOS) Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.aps-environment): macOS 앱의 push notification용 환경입니다.
:::

:::topic-grid
## 샘플 코드
- [Handling Communication Notifications and Focus Status Updates](https://developer.apple.com/documentation/usernotifications/handling-communication-notifications-and-focus-status-updates): communication notification과 Focus status update를 구현해 앱의 통화 및 메시징 경험을 더 풍부하게 만듭니다.
- [Implementing Alert Push Notifications](https://developer.apple.com/documentation/usernotifications/implementing-alert-push-notifications): UserNotifications 프레임워크를 사용해 앱에 표시형 경고 알림을 추가합니다.
- [Implementing Background Push Notifications](https://developer.apple.com/documentation/usernotifications/implementing-background-push-notifications): UserNotifications 프레임워크를 사용해 앱에 background notification을 추가합니다.
:::

:::topic-grid
## 클래스
- [UNNotificationAttributedMessageContext](https://developer.apple.com/documentation/usernotifications/unnotificationattributedmessagecontext)
:::
