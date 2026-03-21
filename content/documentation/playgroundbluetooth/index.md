---
route: /documentation/playgroundbluetooth
source_url: https://developer.apple.com/documentation/playgroundbluetooth
source_locale: en-US
section: docc
content_type: symbol
title: Playground Bluetooth
original_title: Playground Bluetooth
source_hash: f1a47dec4af750976e52352a6a616be5f24112067c1cb7ba094d4ef5da290cd7
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:38:51+00:00'
last_translated_at: '2026-03-13T23:42:00+09:00'
---

# Playground Bluetooth

Swift Playgrounds에서 Bluetooth 주변기기 연결을 표시하고 관리합니다.

## 개요

PlaygroundBluetooth 프레임워크는 playground 페이지 안에서 프레임워크의 central manager를 사용해 Bluetooth 주변기기 연결을 표시하고 관리할 때 사용하는 공통 인터페이스를 제공합니다.

![오른쪽 상단에 PlaygroundBluetoothConnectionView 인스턴스가 표시된 스크린샷입니다. 연결 뷰에는 세 개의 주변기기가 표시되어 있으며, 그중 하나는 연결된 상태로 표시됩니다.](https://developer.apple.com)

:::topic-grid
## 주변기기 연결
- [Connecting to Bluetooth Peripherals in Swift Playgrounds](https://developer.apple.com/documentation/playgroundbluetooth/connecting_to_bluetooth_peripherals_in_swift_playgrounds): 주변기기를 스캔하고 playground의 live view에 표시합니다.
- [PlaygroundBluetoothCentralManager](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanager): 현재 playground 페이지의 central manager를 주변 Bluetooth 주변기기에 연결하기 위한 간소화된 인터페이스입니다.
- [PlaygroundBluetoothCentralManagerDelegate](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothcentralmanagerdelegate): 주변기기 발견에 응답하고 연결 수명 주기를 관리하는 데 사용하는 delegate입니다.
:::

:::topic-grid
## 주변기기 표시
- [PlaygroundBluetoothConnectionView](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionview): 현재 페이지의 central manager에 대한 주변기기 연결 상태를 표시하고 다른 주변기기와의 연결을 관리하는 뷰입니다.
- [PlaygroundBluetoothConnectionViewDelegate](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdelegate): central manager의 connection view에서 사용자 또는 시스템이 시작한 상호 작용에 응답할 때 사용하는 delegate입니다.
- [PlaygroundBluetoothConnectionViewDataSource](https://developer.apple.com/documentation/playgroundbluetooth/playgroundbluetoothconnectionviewdatasource): playground 페이지의 connection view에 사용 가능한 주변기기를 표시하기 위해 채택하는 프로토콜입니다.
:::
