---
route: /documentation/AccessorySetupKit
source_url: https://developer.apple.com/documentation/AccessorySetupKit
source_locale: en-US
section: docc
content_type: symbol
title: AccessorySetupKit
original_title: AccessorySetupKit
source_hash: 8a87ed0e8b134587ee90e8ee65b9fe9230dd07d116630ac6752bdfef777df02f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:34+00:00'
last_translated_at: '2026-03-13T17:20:00+09:00'
---

# AccessorySetupKit

개인 정보를 보호하는 방식으로 액세서리를 검색하고 구성할 수 있게 합니다.

## 개요

AccessorySetupKit을 사용하면 앱이 제공하는 이미지와 이름으로 Bluetooth 또는 Wi-Fi 액세서리를 검색하고 구성할 수 있습니다. Bluetooth, Wi-Fi, 로컬 네트워크 권한에 대해 끊김 없고 개인정보를 보호하는 사용자 동의와 제어를 제공하십시오. AccessorySetupKit 앱은 액세서리 페어링 제거와 이름 변경을 포함한 향상된 액세서리 제어에도 접근할 수 있습니다.

[Wi-Fi Aware](https://developer.apple.com/documentation/WiFiAware)와 함께 AccessorySetupKit을 사용하려면 액세서리 검색을 시작하기 전에 [ASDiscoveryDescriptor](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor)에 Wi-Fi Aware 속성을 지정하십시오.

:::important Important
AccessorySetupKit은 iOS와 iPadOS에서 사용할 수 있습니다. watchOS 26 이상에서는 누군가 iOS 앱에서 AccessorySetupKit을 사용해 액세서리를 설정하면 companion watchOS 앱도 CoreBluetooth를 사용해 새 액세서리와 다른 액세서리와 통신할 수 있습니다.
:::

:::topic-grid
## 핵심 사항
- [Setting up and authorizing a Bluetooth accessory](https://developer.apple.com/documentation/accessorysetupkit/setting-up-and-authorizing-a-bluetooth-accessory): Bluetooth 사용 권한을 요청하지 않고 특정 Bluetooth 액세서리를 검색하고 선택하고 설정합니다.
- [Discovering and configuring accessories](https://developer.apple.com/documentation/accessorysetupkit/discovering-and-configuring-accessories): 근처 액세서리를 감지하고 설정을 돕습니다.
- [ASAccessorySession](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession): 액세서리 검색을 조정하는 클래스입니다.
:::

:::topic-grid
## 액세서리 검색
- [ASAccessoryEvent](https://developer.apple.com/documentation/accessorysetupkit/asaccessoryevent): 액세서리 검색 중 발생한 이벤트의 프로퍼티입니다.
- [ASAccessoryEventType](https://developer.apple.com/documentation/accessorysetupkit/asaccessoryeventtype): 액세서리 검색 중 발생하는 이벤트 유형의 열거형입니다.
- [ASDiscoveryDescriptor](https://developer.apple.com/documentation/accessorysetupkit/asdiscoverydescriptor): 액세서리를 검색할 때 사용하는 설명 특성입니다.
:::

:::topic-grid
## 액세서리 설명
- [ASAccessory](https://developer.apple.com/documentation/accessorysetupkit/asaccessory): accessory session이 검색한 액세서리입니다.
- [ASDiscoveredAccessory](https://developer.apple.com/documentation/accessorysetupkit/asdiscoveredaccessory): 사용자화된 picker 표시 항목을 생성할 때 사용하는 검색된 액세서리입니다.
- [ASAccessory.AccessoryState](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/accessorystate): 액세서리의 가능한 권한 상태를 나타내는 열거형입니다.
:::

:::topic-grid
## picker 항목 표시
- [ASPickerDisplayItem](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplayitem): discovery picker가 표시하는 액세서리입니다.
- [ASDiscoveredDisplayItem](https://developer.apple.com/documentation/accessorysetupkit/asdiscovereddisplayitem): 검색된 액세서리를 사용자화해 만든 picker 표시 항목입니다.
- [ASMigrationDisplayItem](https://developer.apple.com/documentation/accessorysetupkit/asmigrationdisplayitem): AccessorySetupKit으로 마이그레이션할 때 사용하는, 이전에 검색된 액세서리를 나타내는 discovery picker 표시 항목입니다.
:::

:::topic-grid
## 정보 프로퍼티 리스트 키
- [NSAccessorySetupSupports](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessorySetupSupports): AccessorySetupKit이 액세서리를 검색하고 구성할 때 사용하는 무선 기술을 나타내는 문자열 배열입니다.
- [NSAccessorySetupBluetoothCompanyIdentifiers](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothCompanyIdentifiers): 앱이 구성하는 액세서리의 Bluetooth company identifier를 나타내는 문자열 배열입니다.
- [NSAccessorySetupBluetoothNames](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothNames): 앱이 구성하는 액세서리의 Bluetooth 장치 이름 또는 부분 문자열을 나타내는 문자열 배열입니다.
- [NSAccessorySetupBluetoothServices](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothServices): 앱이 구성하는 액세서리의 Bluetooth SIG 정의 서비스 또는 사용자 정의 서비스의 16진수 값을 나타내는 문자열 배열입니다.
:::

:::topic-grid
## 오류
- [ASError](https://developer.apple.com/documentation/accessorysetupkit/aserror): 액세서리 검색 중 발생한 오류입니다.
- [ASErrorDomain](https://developer.apple.com/documentation/accessorysetupkit/aserrordomain): AccessorySetupKit 오류를 위한 NSError domain입니다.
- [ASError.Code](https://developer.apple.com/documentation/accessorysetupkit/aserror/code): 액세서리 검색 중 발생한 오류를 설명하는 코드입니다.
:::
