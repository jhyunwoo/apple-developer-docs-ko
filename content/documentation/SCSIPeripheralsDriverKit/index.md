---
route: /documentation/SCSIPeripheralsDriverKit
source_url: https://developer.apple.com/documentation/SCSIPeripheralsDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: SCSIPeripheralsDriverKit
original_title: SCSIPeripheralsDriverKit
source_hash: f27729011363a17840ca1e258a3f7d84a28521fc082aa8c09e03751ceadaa818
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:58+00:00'
last_translated_at: '2026-03-13T17:35:00+09:00'
---

# SCSIPeripheralsDriverKit

SCSI Block Command 및 Multimedia Command 프로토콜을 사용하는 주변 장치용 드라이버를 개발합니다.

## 개요

SCSIPeripheralsDriverKit 프레임워크는 SCSI 프로토콜을 사용해 통신하는 외부 장치용 드라이버 개발을 지원합니다. 이 프레임워크는 논리 장치 수준에서 동작합니다. 블록 수준 드라이버 개발에는 [BlockStorageDeviceDriverKit](https://developer.apple.com/documentation/BlockStorageDeviceDriverKit)을 사용하십시오. 프로토콜 수준 드라이버 개발에는 [SCSIControllerDriverKit](https://developer.apple.com/documentation/SCSIControllerDriverKit)을 사용하십시오.

장치가 각각 SCSI Block Commands(SBC) 또는 SCSI Multimedia Commands(SMC)를 사용하는지에 따라 [IOUserSCSIPeripheralDeviceType00](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00) 또는 [IOUserSCSIPeripheralDeviceType05](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05)를 서브클래싱하여 드라이버를 개발하십시오. 서브클래스에서 프레임워크가 순수 가상 함수로 선언한 모든 메서드를 재정의합니다. 그런 다음 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용하는 앱 안에 드라이버를 패키징하여 사용자의 Mac에 드라이버를 설치하고 업그레이드합니다.

:::note Note
SCSIPeripheralsDriverKit은 macOS에서 사용할 수 있습니다.
:::

:::topic-grid
## 드라이버 인터페이스
- [IOUserSCSIPeripheralDeviceType00](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype00): SCSI Block Commands(SBC)를 사용하는 type 00 장치와 동작하는 DriverKit provider 객체입니다.
- [IOUserSCSIPeripheralDeviceType05](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype05): SCSI Multimedia Commands(SMC)를 사용하는 type 05 장치와 동작하는 DriverKit provider 객체입니다.
:::

:::topic-grid
## 장치 명령
- [SCSI commands](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsi-commands): framework의 free function을 호출해 주변 장치로 보낼 Command Descriptor Block(CDB)을 채웁니다.
:::

:::topic-grid
## 클래스
- [IOUserSCSIPeripheralDeviceType07](https://developer.apple.com/documentation/scsiperipheralsdriverkit/iouserscsiperipheraldevicetype07)
:::

:::topic-grid
## 레퍼런스
- [SCSIPeripheralsDriverKit Enumerations](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsiperipheralsdriverkit-enumerations)
- [SCSIPeripheralsDriverKit Data Types](https://developer.apple.com/documentation/scsiperipheralsdriverkit/scsiperipheralsdriverkit-data-types)
:::
