---
route: /documentation/SCSIControllerDriverKit
source_url: https://developer.apple.com/documentation/SCSIControllerDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: SCSIControllerDriverKit
original_title: SCSIControllerDriverKit
source_hash: ebb8dab78e55aa3906cdb440e8893644f5c402bfa0e009f9b1a184e85d8dfca2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:22:11+00:00'
last_translated_at: '2026-03-13T22:52:00+09:00'
---

# SCSIControllerDriverKit

SCSI 프로토콜 기반 장치를 위한 드라이버를 개발합니다.

## 개요

SCSIControllerDriverKit 프레임워크는 SCSI 프로토콜을 사용해 통신하는 장치를 위한 DriverKit extension(dext) 드라이버 개발을 지원합니다.

[IOUserSCSIParallelInterfaceController](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller)를 subclass하고, 프레임워크가 순수 가상 메서드로 선언한 모든 메서드를 override하여 드라이버를 개발하십시오. 그런 다음 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용해 사용자의 Mac에 드라이버를 설치하고 업그레이드하는 앱 안에 그 드라이버를 패키징하십시오.

:::note 참고
SCSIControllerDriverKit은 macOS에서 사용할 수 있습니다.
:::

:::topic-grid
## 핵심 사항
- [com.apple.developer.driverkit.family.scsicontroller](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.scsicontroller): SCSI controller가 있는 장치와 드라이버를 매칭할 수 있는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 샘플
- [DriverKit sample code](https://developer.apple.com/documentation/DriverKit/driverkit-sample-code): DriverKit 계열 프레임워크를 사용해 macOS 장치 드라이버를 작성하는 방법을 보여 주는 프로젝트를 살펴봅니다.
:::

:::topic-grid
## 드라이버 인터페이스
- [IOUserSCSIParallelInterfaceController](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller): SCSI 기반 장치와의 통신을 관리하는 DriverKit provider 객체입니다.
:::

:::topic-grid
## 매크로
- [Macros](https://developer.apple.com/documentation/scsicontrollerdriverkit/scsicontrollerdriverkit-macros)
- [kMaxBundledParallelTasks](https://developer.apple.com/documentation/scsicontrollerdriverkit/kmaxbundledparalleltasks)
:::
