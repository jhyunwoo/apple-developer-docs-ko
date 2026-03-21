---
route: /documentation/ExternalAccessory
source_url: https://developer.apple.com/documentation/ExternalAccessory
source_locale: en-US
section: docc
content_type: symbol
title: External Accessory
original_title: External Accessory
source_hash: 3cad77a9267644f79d5fa68253d371936fd9a4c6b0e8c02e3728efb9832057a6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:14:18+00:00'
last_translated_at: '2026-03-13T23:14:51+09:00'
---

# External Accessory

Apple Lightning 커넥터 또는 Bluetooth 무선 기술로 기기에 연결되는 액세서리와 통신합니다.

## 개요

External Accessory 프레임워크를 사용하면 iOS 앱이 지원하는 MFi 액세서리와의 연결을 설정하고 관리할 수 있습니다. 이 프레임워크는 Apple Lightning 또는 30핀 커넥터를 통해 iOS 또는 iPadOS 기기에 물리적으로 연결되는 하드웨어와, Bluetooth 기술로 무선 연결되는 하드웨어를 지원합니다. 프레임워크는 액세서리가 사용자의 기기에 연결되거나 연결 해제될 때 앱에 이를 알려 줍니다. 연결된 동안에는 기기가 지원하는 하드웨어 프로토콜을 사용해 액세서리와 직접 통신합니다.

:::note Note
Apple silicon이 탑재된 Mac에서 실행되는 iPad 및 iPhone 앱은 이 프레임워크를 사용해 외부 액세서리에 연결할 수 없습니다. 다만 앱을 이 프레임워크에 계속 링크하고 Apple silicon에서 다른 기능은 실행할 수 있습니다.
:::

MFi 액세서리 제조업체는 어떤 서드파티 앱이 해당 액세서리와 통신할 수 있는지 결정합니다. 앱을 개발하는 경우, 하드웨어와 통신하는 데 필요한 정보를 얻기 위해 제조업체와 협력하십시오. 예를 들어 액세서리가 지원하는 통신 프로토콜의 명세를 확보해야 합니다.

외부 액세서리 연결 방식에 대한 자세한 내용은 [External Accessory Programming Topics](https://developer.apple.com/library/archive/featuredarticles/ExternalAccessoryPT/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009502)를 참고하십시오.

:::topic-grid
## 핵심
- [UISupportedExternalAccessoryProtocols](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UISupportedExternalAccessoryProtocols): 앱이 외부 액세서리 하드웨어와 통신할 때 사용하는 프로토콜입니다.
- [EAAccessoryManager](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager): 연결된 액세서리를 식별하고 연결/해제 알림 전달을 시작할 때 사용하는 객체입니다.
:::

:::topic-grid
## 액세서리 통신
- [EAAccessory](https://developer.apple.com/documentation/externalaccessory/eaaccessory): 단일 연결 하드웨어 액세서리에 대한 정보를 담는 객체입니다.
- [EASession](https://developer.apple.com/documentation/externalaccessory/easession): 앱과 연결된 하드웨어 액세서리 사이의 통신을 관리할 때 사용하는 객체입니다.
:::

:::topic-grid
## Wi-Fi 액세서리 구성
- [Wireless Accessory Configuration Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.external-accessory.wireless-configuration): 앱이 MFi Wi-Fi 액세서리를 구성할 수 있는지 나타내는 Boolean 값입니다.
- [EAWiFiUnconfiguredAccessoryBrowser](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser): 무선 액세서리를 검색하고 사용자의 앱에 맞게 구성할 때 사용하는 객체입니다.
- [EAWiFiUnconfiguredAccessory](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory): 아직 구성되지 않은 MFi Wireless Accessory Configuration 액세서리에 대한 정보를 제공하는 객체입니다.
:::
