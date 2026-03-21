---
route: /documentation/AccessoryTransportExtension
source_url: https://developer.apple.com/documentation/AccessoryTransportExtension
source_locale: en-US
section: docc
content_type: symbol
title: Accessory Transport Extension
original_title: Accessory Transport Extension
source_hash: 312e48636d057cd86aa5b70b37eb16db0009535f2e36303d44541bf28b84f89e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:17:58+00:00'
last_translated_at: '2026-03-13T23:18:11+09:00'
---

# Accessory Transport Extension

직접 개발한 연결 액세서리로 데이터를 안전하게 전송합니다.

## 개요

Accessory Transport Extension 프레임워크를 사용하면 직접 개발한 액세서리로 정보를 안전하게 전송할 수 있습니다. 먼저 [AccessorySetupKit](https://developer.apple.com/documentation/AccessorySetupKit)으로 액세서리와 연결을 설정합니다. 그런 다음 [Wi-Fi Infrastructure](https://developer.apple.com/documentation/WiFiInfrastructure)를 사용해 Wi-Fi 네트워크를 액세서리와 공유하거나, [Accessory Notifications](https://developer.apple.com/documentation/AccessoryNotifications)를 사용해 iOS 시스템 알림을 액세서리로 전달할 수 있습니다.

:::important Important
이 프레임워크는 iOS에서만 사용할 수 있습니다. Mac Catalyst로 빌드한 앱, visionOS에서 실행되는 iOS 앱, Apple silicon Mac에서 실행되는 iOS 앱에 대해서는 호출을 무시합니다.

이 프레임워크를 사용하는 앱은 어느 지역의 기기에서든 개발하고 테스트할 수 있습니다. 그러나 고객이 설치한 앱이 이 프레임워크를 사용할 수 있는 경우는 EU에 위치한 기기이면서 EU 국가 또는 지역의 Apple Account로 로그인한 경우에 한합니다.
:::

## 액세서리와 Wi-Fi 네트워크 공유

액세서리와 Wi-Fi 네트워크를 공유하려면 extension 안에서 [AccessoryTransportAppExtension](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension) protocol을 구현합니다. 시스템은 시작할 준비가 되면 extension의 [accept(sessionRequest:)](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension/accept(sessionrequest:)) 메서드를 호출합니다. session request를 수락한 뒤에는 [ASAccessorySession](https://developer.apple.com/documentation/AccessorySetupKit/ASAccessorySession)으로 액세서리에 연결하고, [WINetworkSharingProvider](https://developer.apple.com/documentation/WiFiInfrastructure/WINetworkSharingProvider)로 Wi-Fi 네트워크 데이터를 전달합니다.

## iOS 시스템 알림을 액세서리로 전달

Accessory Transport Extension 프레임워크를 [Accessory Notifications](https://developer.apple.com/documentation/AccessoryNotifications)와 함께 사용하면, 앱은 iOS 시스템 알림을 받아 직접 개발한 연결 액세서리에서 사람에게 알림을 전달할 수 있습니다. 이 워크플로는 보안과 캡슐화를 유지하기 위해 세 개의 extension을 필요로 합니다. [AccessoryDataProvider](https://developer.apple.com/documentation/accessorytransportextension/accessorydataprovider)를 구현해 특정 알림의 내용을 받아 선별합니다. 시스템은 [AccessoryTransportSecurity](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurity) extension이 제공하는 키를 사용해 알림 데이터를 암호화합니다. 그런 다음 암호화된 데이터를 액세서리로 전송하기 위해 [AccessoryTransportAppExtension](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension)에 전달합니다. transport extension은 암호화된 데이터를 액세서리에 보내지만, 알림 내용을 해독할 수는 없습니다.

:::topic-grid
## 핵심
- [com.apple.developer.accessory-transport-extension](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.accessory-transport-extension): 앱이 연결된 액세서리와 민감한 정보를 교환할 수 있는지 나타내는 Boolean 값입니다.
:::

:::topic-grid
## Wi-Fi 네트워크 공유
- [AccessoryTransportAppExtension](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension): 직접 개발한 액세서리로 데이터를 전송하는 extension을 위한 protocol입니다.
- [AccessoryTransportExtensionConfiguration](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportextensionconfiguration): extension과 시스템 사이의 통신을 구성하고 관리할 수 있게 해 주는 인터페이스입니다.
- [AccessoryTransportSession](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession): extension과 시스템 사이의 transport session을 관리하는 클래스입니다.
- [Wi-Fi Infrastructure](https://developer.apple.com/documentation/WiFiInfrastructure): 기기와 연결 액세서리 사이에서 Wi-Fi 네트워크 자격 증명을 안전하게 공유합니다.
:::

:::topic-grid
## 알림 전달
- [Receiving iOS notifications on an accessory](https://developer.apple.com/documentation/AccessoryNotifications/receiving-ios-notifications-on-an-accessory): 액세서리용 알림을 관리하는 사용자 정의 앱 extension을 만듭니다.
- [AccessoryDataProvider](https://developer.apple.com/documentation/accessorytransportextension/accessorydataprovider): iOS 시스템 알림을 받아 액세서리에 맞게 데이터를 선별하는 extension을 위한 protocol입니다.
- [AccessoryDataProviderConfiguration](https://developer.apple.com/documentation/accessorytransportextension/accessorydataproviderconfiguration): extension과 시스템 사이의 통신을 구성하고 관리하는 protocol입니다.
- [AccessoryTransportSecurity](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurity): 액세서리로 보내는 메시지의 암호화를 처리하는 extension을 위한 protocol입니다.
- [AccessoryTransportSecurityConfiguration](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurityconfiguration): 보안 extension과 시스템 사이의 통신을 구성하고 관리하는 protocol입니다.
- [Accessory Notifications](https://developer.apple.com/documentation/AccessoryNotifications): 직접 개발한 액세서리에서 전달된 iOS 시스템 알림을 수신합니다.
:::

:::topic-grid
## 데이터와 세션
- [AccessoryFeature](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeature): 액세서리 데이터 제공 extension의 capability를 정의하는 protocol입니다.
- [AccessoryFeatureSession](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesession): 특정 기능 capability의 session을 관리하는 protocol입니다.
- [AccessoryMessage](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage): 액세서리로 보낼 메시지를 나타내는 구조체입니다.
- [AccessorySecuritySession](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession): extension과 시스템 사이의 보안 session을 관리하는 클래스입니다.
- [AccessorySecurity](https://developer.apple.com/documentation/accessorytransportextension/accessorysecurity): 보안 이벤트 및 암호 연산의 타입입니다.
:::
