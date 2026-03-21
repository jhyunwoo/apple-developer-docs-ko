---
route: /documentation/TelephonyMessagingKit
source_url: https://developer.apple.com/documentation/TelephonyMessagingKit
source_locale: en-US
section: docc
content_type: symbol
title: TelephonyMessagingKit
original_title: TelephonyMessagingKit
source_hash: 74b99062fc6234103e5e5a76c2a893761f394e3e363902e9e813b099cba9d54f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:56:51+00:00'
last_translated_at: '2026-03-14T02:40:00+09:00'
---

# TelephonyMessagingKit

셀룰러 네트워크를 통해 표준 기반 메시지를 보내고 받습니다.

## 개요

TelephonyMessagingKit을 사용하려면 [TelephonyMessagingSession](https://developer.apple.com/documentation/telephonymessagingkit/telephonymessagingsession)의 공유 인스턴스를 앱이 프레임워크와 상호 작용하는 주된 진입점으로 사용하십시오. session을 사용하면 앱은 현재 기기에서 사용할 수 있는 서비스를 검사할 수 있습니다. 이 프레임워크는 Short Message Service(SMS), Multimedia Messaging Service(MMS), Rich Communication Services(RCS)를 지원합니다.

각 서비스는 앱이 처리할 수 있는 수신 메시지 알림용 비동기 sequence를 제공합니다. 새 메시지를 보내려면 메시지 내용을 구성한 다음 해당 서비스에 맞는 `send` 메서드를 호출합니다. RCS 서비스가 존재한다면 일대일 메시징을 넘어서 group chat과 chatbot을 포함한 기능도 제공합니다.

:::note Note
TelephonyMessagingKit은 iPhone 기기에서만 SMS, MMS, RCS 메시징을 지원합니다. 이 프레임워크는 iPadOS나 visionOS에서 실행되는 iOS 앱, Apple silicon 기반 macOS에서 실행되는 iOS 앱에서는 기능이 없습니다. Mac Catalyst로 빌드한 Mac 앱의 호출은 프레임워크가 무시합니다.
:::

### 기본 통신사 메시징 앱

TelephonyMessageKit API에 접근하려면 앱에 [Default Carrier Messaging App](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.carrier-messaging-app) entitlement를 추가해야 합니다. 사용자가 앱을 기본 통신사 메시징 앱으로 선택했을 때만 이 기능이 앱에서 활성화됩니다.

:::important Important
TelephonyMessagingKit 앱은 Apple이 제공하는 provisioning profile을 사용해 모든 지역의 기기에서 개발하고 테스트할 수 있습니다. 하지만 앱 사용자는 유럽 연합(EU)에 등록된 계정을 가지고 있어야 하며, 해당 기기도 EU 내에 있어야 합니다.
:::

:::topic-grid
## 기초
- [Creating a carrier messaging app](https://developer.apple.com/documentation/telephonymessagingkit/creating-a-carrier-messaging-app): TelephonyMessagingKit을 사용해 SMS, MMS, RCS 메시지를 보내고 받습니다.
- [TelephonyMessagingSession](https://developer.apple.com/documentation/telephonymessagingkit/telephonymessagingsession): TelephonyMessagingKit 프레임워크와의 상호 작용을 조정하는 객체입니다.
- [Default Carrier Messaging App](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.carrier-messaging-app): 앱이 TelephonyMessagingKit 프레임워크를 사용해 기본 통신사 메시징 앱 역할을 할 수 있는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 지원 타입
- [RCSFileTransferMetadata](https://developer.apple.com/documentation/telephonymessagingkit/rcsfiletransfermetadata): RCS 파일 전송에 대한 metadata를 담는 구조체입니다.
- [RCSGroupContext](https://developer.apple.com/documentation/telephonymessagingkit/rcsgroupcontext): 메시지의 그룹에 대한 정보를 담는 구조체입니다.
:::
