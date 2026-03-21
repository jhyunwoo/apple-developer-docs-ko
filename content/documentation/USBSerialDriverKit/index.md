---
route: /documentation/USBSerialDriverKit
source_url: https://developer.apple.com/documentation/USBSerialDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: USBSerialDriverKit
original_title: USBSerialDriverKit
source_hash: 33bc289d0bc62aab3b7acfe2b902c941bd65fd114299adb89718fdbf9143aefa
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:47:39+00:00'
last_translated_at: '2026-03-13T15:35:00+09:00'
---

# USBSerialDriverKit

Mac에 연결된 직렬 USB 기기를 위한 드라이버를 개발합니다.

## 개요

USBSerialDriverKit 프레임워크를 사용하면 직렬 프로토콜을 통해 USB 기기와 통신하는 드라이버를 개발할 수 있습니다. 이 프레임워크는 기기와 데이터를 주고받는 데 필요한 버퍼와 엔드포인트를 구성함으로써 [SerialDriverKit](https://developer.apple.com/documentation/SerialDriverKit) 프레임워크의 동작을 보강합니다. 기기의 초기 구성을 처리하면, 프레임워크가 해당 기기로의 데이터 전송과 해당 기기로부터의 데이터 전송을 관리합니다.

드라이버는 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용하는 앱 안에 패키징하여 사용자의 Mac에 드라이버를 설치하고 업그레이드합니다.

:::note Note
USBSerialDriverKit은 macOS에서 사용할 수 있습니다.
:::

:::topic-grid
## 샘플
- [DriverKit sample code](https://developer.apple.com/documentation/DriverKit/driverkit-sample-code): DriverKit 계열 프레임워크로 macOS 기기 드라이버를 작성하는 방법을 보여 주는 프로젝트를 살펴봅니다.
:::

:::topic-grid
## 직렬 USB 인터페이스
- [com.apple.developer.driverkit.family.serial](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.serial): 직렬 통신 인터페이스가 있는 기기와 드라이버를 매칭할지 나타내는 Boolean 값입니다.
- [IOUserUSBSerial](https://developer.apple.com/documentation/usbserialdriverkit/iouserusbserial): USB 기기와의 직렬 연결을 관리하는 서비스입니다.
:::
