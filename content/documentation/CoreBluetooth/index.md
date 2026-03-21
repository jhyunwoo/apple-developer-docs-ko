---
route: /documentation/CoreBluetooth
source_url: https://developer.apple.com/documentation/CoreBluetooth
source_locale: en-US
section: docc
content_type: symbol
title: Core Bluetooth
original_title: Core Bluetooth
source_hash: 9d318ee49c0eeeffd5fe1d77a0ff70474a363c85cf8fbcf58604215a76d01870
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:50+00:00'
last_translated_at: '2026-03-13T18:25:00+09:00'
---

# Core Bluetooth

Bluetooth low energy 및 BR/EDR("Classic") 기기와 통신합니다.

## 개요

Core Bluetooth 프레임워크는 앱이 Bluetooth 기능을 갖춘 low energy(LE) 및 Basic Rate / Enhanced Data Rate(BR/EDR) 무선 기술과 통신하는 데 필요한 클래스를 제공합니다.

Core Bluetooth 프레임워크의 어떤 클래스도 서브클래싱하지 마십시오. 이러한 클래스를 재정의하는 것은 지원되지 않으며 정의되지 않은 동작을 초래합니다.

macOS에서 실행되는 iPad 앱에서는 Core Bluetooth 백그라운드 실행 모드를 지원하지 않습니다.

iOS 26 이상에서는 앱이 백그라운드로 전환되기 전에 Live Activity를 시작하면 백그라운드에서도 특정 활동을 계속할 수 있습니다. 앱에 인스턴스화된 [CBManager](https://developer.apple.com/documentation/corebluetooth/cbmanager)가 있고 Live Activity를 시작하면, 포그라운드에 있을 때와 동일한 권한을 백그라운드에서도 사용할 수 있습니다. 즉 서비스 UUID를 제공하지 않는 스캔이나 중복 필터를 비활성화한 스캔 같은 활동이 백그라운드에서도 허용됩니다. Live Activity 생성에 대한 자세한 내용은 [ActivityKit](https://developer.apple.com/documentation/ActivityKit)을 참고하십시오.

:::important 중요
앱이 접근해야 하는 데이터 유형에 대한 사용 설명 키가 `Info.plist`에 포함되어 있지 않으면 앱이 충돌합니다. iOS 13 이상을 대상으로 링크된 앱에서 Core Bluetooth API에 접근하려면 [NSBluetoothAlwaysUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBluetoothAlwaysUsageDescription) 키를 포함하십시오. iOS 12 이하에서는 Bluetooth peripheral 데이터에 접근하려면 [NSBluetoothPeripheralUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBluetoothPeripheralUsageDescription)을 포함하십시오.
:::

:::topic-grid
## Central
- [CBCentral](https://developer.apple.com/documentation/corebluetooth/cbcentral): peripheral 역할을 하는 로컬 앱에 연결된 원격 기기입니다.
- [CBCentralManager](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager): peripheral을 스캔하고 발견하며 연결하고 관리하는 객체입니다.
- [CBCentralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerdelegate): peripheral 기기의 발견 및 관리에 대한 업데이트를 제공하는 프로토콜입니다.
:::

:::topic-grid
## Peripheral
- [CBPeripheral](https://developer.apple.com/documentation/corebluetooth/cbperipheral): 원격 peripheral 기기입니다.
- [CBPeripheralDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheraldelegate): peripheral의 서비스를 사용할 때의 업데이트를 제공하는 프로토콜입니다.
- [CBPeripheralManager](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager): 이 앱이 노출하는 peripheral 서비스를 관리하고 광고하는 객체입니다.
- [CBPeripheralManagerDelegate](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerdelegate): 로컬 peripheral 상태와 원격 central 기기와의 상호 작용에 대한 업데이트를 제공하는 프로토콜입니다.
- [CBAttribute](https://developer.apple.com/documentation/corebluetooth/cbattribute): peripheral이 제공하는 서비스의 공통 측면을 표현한 것입니다.
- [CBAttributePermissions](https://developer.apple.com/documentation/corebluetooth/cbattributepermissions): characteristic 값의 읽기, 쓰기, 암호화 권한을 나타내는 값입니다.
:::

:::topic-grid
## 데이터 전송
- [Transferring Data Between Bluetooth Low Energy Devices](https://developer.apple.com/documentation/corebluetooth/transferring-data-between-bluetooth-low-energy-devices): Bluetooth low energy central과 peripheral 기기를 만들고, 서로를 발견하고 데이터를 교환할 수 있게 합니다.
:::

:::topic-grid
## 서비스
- [CBService](https://developer.apple.com/documentation/corebluetooth/cbservice): 기기의 기능이나 특징을 수행하는 데이터와 관련 동작의 모음입니다.
- [CBMutableService](https://developer.apple.com/documentation/corebluetooth/cbmutableservice): 쓰기 가능한 프로퍼티 값을 가진 서비스입니다.
- [CBCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbcharacteristic): 원격 peripheral 서비스의 characteristic입니다.
- [CBMutableCharacteristic](https://developer.apple.com/documentation/corebluetooth/cbmutablecharacteristic): 로컬 peripheral 서비스의 characteristic입니다.
- [CBDescriptor](https://developer.apple.com/documentation/corebluetooth/cbdescriptor): 원격 peripheral의 characteristic에 대한 추가 정보를 제공하는 객체입니다.
- [CBMutableDescriptor](https://developer.apple.com/documentation/corebluetooth/cbmutabledescriptor): 로컬 peripheral의 characteristic에 대한 추가 정보를 제공하는 객체입니다.
:::

:::topic-grid
## 지원 타입
- [CBManager](https://developer.apple.com/documentation/corebluetooth/cbmanager): central 및 peripheral 객체를 관리하는 추상 기본 클래스입니다.
- [CBATTRequest](https://developer.apple.com/documentation/corebluetooth/cbattrequest): Attribute Protocol(ATT)을 사용하는 요청입니다.
- [CBPeer](https://developer.apple.com/documentation/corebluetooth/cbpeer): 원격 기기를 나타내는 객체입니다.
- [CBUUID](https://developer.apple.com/documentation/corebluetooth/cbuuid): Bluetooth 표준에서 정의한 전역 고유 식별자입니다.
:::

:::topic-grid
## Bluetooth Classic 지원
- [Using Core Bluetooth Classic](https://developer.apple.com/documentation/corebluetooth/using-core-bluetooth-classic): Core Bluetooth API를 사용해 Bluetooth Classic 기기를 발견하고 통신합니다.
:::

:::topic-grid
## 오류
- [CBError](https://developer.apple.com/documentation/corebluetooth/cberror-swift.struct): Bluetooth 트랜잭션 중 Core Bluetooth가 반환하는 오류입니다.
- [CBErrorDomain](https://developer.apple.com/documentation/corebluetooth/cberrordomain): Core Bluetooth 오류의 도메인입니다.
- [CBError.Code](https://developer.apple.com/documentation/corebluetooth/cberror-swift.struct/code): Bluetooth 트랜잭션 중 Core Bluetooth가 반환하는 오류 코드입니다.
- [CBATTError](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct): Attribute Protocol(ATT)을 사용하는 동안 Core Bluetooth가 반환하는 오류입니다.
- [CBATTErrorDomain](https://developer.apple.com/documentation/corebluetooth/cbatterrordomain): Core Bluetooth ATT 오류의 도메인입니다.
- [CBATTError.Code](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct/code): Bluetooth low energy ATT 트랜잭션 중 GATT 서버(원격 peripheral)가 반환할 수 있는 오류입니다.
- [CBATTError](https://developer.apple.com/documentation/corebluetooth/cbatterror-swift.struct): Attribute Protocol(ATT)을 사용하는 동안 Core Bluetooth가 반환하는 오류입니다.
:::

:::topic-grid
## 지원 중단됨
- [CBCentralManagerState](https://developer.apple.com/documentation/corebluetooth/cbcentralmanagerstate): central manager 객체의 현재 상태를 나타내는 값입니다.
- [CBPeripheralManagerState](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanagerstate): peripheral manager의 현재 상태를 나타내는 값입니다.
- [Deprecated Constants](https://developer.apple.com/documentation/corebluetooth/deprecated-constants): Core Bluetooth 프레임워크에서 찾을 수 있는 상수를 설명하는 문서입니다.
:::

:::topic-grid
## 변수
- [CBUUIDCharacteristicObservationScheduleString](https://developer.apple.com/documentation/corebluetooth/cbuuidcharacteristicobservationschedulestring)
:::
