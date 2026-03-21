---
route: /documentation/BlockStorageDeviceDriverKit
source_url: https://developer.apple.com/documentation/BlockStorageDeviceDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: BlockStorageDeviceDriverKit
original_title: BlockStorageDeviceDriverKit
source_hash: a65386d83103bf72b476b22bfeb097a541a3eefdfa4fa8def570e328fe9521c6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:14:52+00:00'
last_translated_at: '2026-03-13T16:45:00+09:00'
---

# BlockStorageDeviceDriverKit

사용자 정의 프로토콜로 드라이버와 통신하는 맞춤형 저장 장치를 위한 드라이버를 개발합니다.

## 개요

`BlockStorageDeviceDriverKit`을 [PCIDriverKit](https://developer.apple.com/documentation/PCIDriverKit) 같은 프레임워크와 함께 사용하면 사용자 정의 저장 장치 인터커넥트 프로토콜을 통해 하드웨어와 통신할 수 있는 드라이버를 만들 수 있습니다.

[IOUserBlockStorageDevice](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice)를 서브클래싱하고 프레임워크가 C++ pure virtual로 선언한 모든 메서드를 재정의해 드라이버를 개발하십시오. 그런 다음 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용하는 앱 안에 드라이버를 패키징해 사용자의 Mac에 드라이버를 설치하고 업그레이드합니다.

:::note Note
BlockStorageDeviceDriverKit은 macOS에서 사용할 수 있습니다.
:::

:::topic-grid
## 핵심 사항
- [com.apple.developer.driverkit.family.block-storage-device](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.block-storage-device): 사용자 정의 드라이버를 사용하는 블록 저장 장치와 드라이버를 매칭할지 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 드라이버 인터페이스
- [IOUserBlockStorageDevice](https://developer.apple.com/documentation/blockstoragedevicedriverkit/iouserblockstoragedevice): 블록 저장 장치와의 통신을 관리하는 DriverKit provider 객체입니다.
:::

:::topic-grid
## 매크로
- [kMaxDeviceStringLength](https://developer.apple.com/documentation/blockstoragedevicedriverkit/kmaxdevicestringlength)
:::
