---
route: /documentation/SerialDriverKit
source_url: https://developer.apple.com/documentation/SerialDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: SerialDriverKit
original_title: SerialDriverKit
source_hash: 7fe59be79d6616fc6f7bb3baff064dd1726d0ca29718b1892c19d6ce22a655e0
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:43:00+00:00'
last_translated_at: '2026-03-13T17:35:00+09:00'
---

# SerialDriverKit

Mac에 연결된 직렬 I/O 장치용 드라이버를 개발합니다.

## 개요

SerialDriverKit 프레임워크는 직렬 인터페이스를 사용해 통신하는 장치용 드라이버 개발을 지원합니다. 이 프레임워크를 사용하면 모뎀 하드웨어 또는 UART(universal asynchronous receiver/transmitter)를 지원하는 드라이버를 만들 수 있습니다. USB 장치와 직렬 방식으로 통신하는 드라이버를 만들려면 대신 [USBSerialDriverKit](https://developer.apple.com/documentation/USBSerialDriverKit) 프레임워크를 사용하십시오.

드라이버는 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용하는 앱 안에 패키징하여 사용자의 Mac에 드라이버를 설치하고 업그레이드합니다.

:::note Note
SerialDriverKit은 macOS에서 사용할 수 있습니다.
:::

:::topic-grid
## 샘플
- [DriverKit sample code](https://developer.apple.com/documentation/DriverKit/driverkit-sample-code): DriverKit 계열 프레임워크로 macOS 장치 드라이버를 작성하는 방법을 보여 주는 프로젝트를 살펴봅니다.
:::

:::topic-grid
## 직렬 인터페이스
- [com.apple.developer.driverkit.family.serial](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.serial): 직렬 통신 인터페이스를 가진 장치와 드라이버를 매칭할지 나타내는 Boolean 값입니다.
- [IOUserSerial](https://developer.apple.com/documentation/serialdriverkit/iouserserial): 직렬 연결을 사용해 통신하는 서비스를 빌드하는 클래스입니다.
:::

:::topic-grid
## 레퍼런스
- [SerialDriverKit Enumerations](https://developer.apple.com/documentation/serialdriverkit/serialdriverkit-enumerations)
- [SerialDriverKit Data Types](https://developer.apple.com/documentation/serialdriverkit/serialdriverkit-data-types)
:::

:::topic-grid
## 네임스페이스
- [driverkit](https://developer.apple.com/documentation/serialdriverkit/driverkit)
:::

:::topic-grid
## 매크로
- [PD_RS232_S_LE](https://developer.apple.com/documentation/serialdriverkit/pd_rs232_s_le)
- [PD_RS232_S_RNG](https://developer.apple.com/documentation/serialdriverkit/pd_rs232_s_rng)
- [kIOTTYBaseNameKey](https://developer.apple.com/documentation/serialdriverkit/kiottybasenamekey)
- [kIOTTYSuffixKey](https://developer.apple.com/documentation/serialdriverkit/kiottysuffixkey)
:::

:::topic-grid
## 열거형 케이스
- [kIOSerialMemoryArena](https://developer.apple.com/documentation/serialdriverkit/kioserialmemoryarena)
- [kIOSerialMemoryRxBuf](https://developer.apple.com/documentation/serialdriverkit/kioserialmemoryrxbuf)
- [kIOSerialMemoryTxBuf](https://developer.apple.com/documentation/serialdriverkit/kioserialmemorytxbuf)
- [kIOSerialPTYMaster](https://developer.apple.com/documentation/serialdriverkit/kioserialptymaster)
- [kIOSerialUserClient](https://developer.apple.com/documentation/serialdriverkit/kioserialuserclient)
- [kIOSerialUserClientIoctl](https://developer.apple.com/documentation/serialdriverkit/kioserialuserclientioctl)
- [kIOSerialUserClientOpen](https://developer.apple.com/documentation/serialdriverkit/kioserialuserclientopen)
- [kIOSerialUserClientPoll](https://developer.apple.com/documentation/serialdriverkit/kioserialuserclientpoll)
:::
