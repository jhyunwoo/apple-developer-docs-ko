---
route: /documentation/ImageCaptureCore
source_url: https://developer.apple.com/documentation/ImageCaptureCore
source_locale: en-US
section: docc
content_type: symbol
title: ImageCaptureCore
original_title: ImageCaptureCore
source_hash: afa8ebba5aad36fb839ae339bb86b800e37399075dba81d7fcc24de01a87ed73
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:13:40+00:00'
last_translated_at: '2026-03-13T22:24:00+09:00'
---

# ImageCaptureCore

미디어 장치를 탐색하고 앱에서 프로그래밍 방식으로 제어합니다.

## 개요

ImageCaptureCore를 사용하면 앱에서 다음 작업을 수행할 수 있습니다.

- 연결된 카메라와 스캐너를 검색합니다.
- 연결된 카메라의 폴더, 파일, metadata를 보고 수정합니다.
- tethered capture를 사용해 연결된 카메라에서 직접 사진을 촬영합니다.
- 연결된 스캐너에서 개요 스캔과 일반 스캔을 수행합니다.

![케이블로 카메라와 스캐너에 연결된 macOS 기기와, 케이블로 카메라에 연결된 iPadOS 기기를 보여 주는 다이어그램입니다.](https://developer.apple.com)

### tethered capture와 사진 가져오기 구성

macOS 앱에서 사진을 가져오고 tether 기능을 사용하려면 먼저 Xcode에서 Hardened Runtime capability를 활성화한 다음 [Photos Library Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.personal-information.photos-library)을 추가해야 합니다.

iOS 앱에서 tether 기능을 사용하려면, 먼저 앱이 외부 카메라 접근을 요청하는 이유를 사용자에게 알려야 합니다. 앱의 `Info.plist` 파일에 [NSCameraUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription) 키를 추가하고 사용 목적을 설명하십시오.

:::important 중요
macOS 14 이상에서는 sandboxed 앱이 USB 장치와 상호 작용할 수 있도록 [com.apple.security.device.usb](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.device.usb) entitlement 키를 사용하십시오.
:::

:::topic-grid
## 핵심 사항
- [ICDeviceBrowser](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser): 디지털 카메라와 스캐너를 찾기 위한 객체입니다.
- [Photos Library Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.personal-information.photos-library): 앱이 사용자의 Photos 라이브러리에 읽기/쓰기 접근 권한을 가지는지를 나타내는 Boolean 값입니다.
- [NSCameraUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription): 앱이 기기의 카메라 접근을 요청하는 이유를 사용자에게 알려 주는 메시지입니다.
:::

:::topic-grid
## 카메라
- [ICCameraDevice](https://developer.apple.com/documentation/imagecapturecore/iccameradevice): 카메라를 나타내는 객체입니다.
- [ICCameraDeviceDelegate](https://developer.apple.com/documentation/imagecapturecore/iccameradevicedelegate): 카메라 감지, metadata와 thumbnail 가져오기, 접근 및 capability 변경 처리, 연결된 카메라에서 다른 동작 수행을 위한 메서드입니다.
- [ICCameraItem](https://developer.apple.com/documentation/imagecapturecore/iccameraitem): 카메라 항목을 나타내는 추상 클래스입니다.
- [ICCameraFile](https://developer.apple.com/documentation/imagecapturecore/iccamerafile): 카메라에 있는 파일을 나타내는 객체입니다.
- [ICCameraFolder](https://developer.apple.com/documentation/imagecapturecore/iccamerafolder): 카메라에 있는 폴더를 나타내는 객체입니다.
:::

:::topic-grid
## 스캐너
- [ICScannerDevice](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice): 스캐너를 나타내는 객체입니다.
- [ICScannerDeviceDelegate](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate): 사용 가능 여부 확인, 기능 단위 선택, 연결된 스캐너에서 스캔 수행을 위한 메서드입니다.
- [Scanner Configuration](https://developer.apple.com/documentation/imagecapturecore/scanner-configuration): 스캐너의 기능 단위와 특징을 살펴봅니다.
:::

:::topic-grid
## 오류
- [ICReturn](https://developer.apple.com/documentation/imagecapturecore/icreturn)
- [ICLegacyReturn](https://developer.apple.com/documentation/imagecapturecore/iclegacyreturn)
- [ICReturnConnectionError](https://developer.apple.com/documentation/imagecapturecore/icreturnconnectionerror): ImageCaptureCore가 반환하는 연결 오류입니다.
- [ICReturnDownloadError](https://developer.apple.com/documentation/imagecapturecore/icreturndownloaderror): ImageCaptureCore가 반환하는 다운로드 오류입니다.
- [ICReturnMetadataError](https://developer.apple.com/documentation/imagecapturecore/icreturnmetadataerror): ImageCaptureCore가 반환하는 metadata 오류입니다.
- [ICReturnObjectError](https://developer.apple.com/documentation/imagecapturecore/icreturnobjecterror): ImageCaptureCore가 반환하는 객체 오류입니다.
- [ICReturnPTPDeviceError](https://developer.apple.com/documentation/imagecapturecore/icreturnptpdeviceerror): ImageCaptureCore가 반환하는 PTP 장치 오류입니다.
- [ICReturnThumbnailError](https://developer.apple.com/documentation/imagecapturecore/icreturnthumbnailerror): ImageCaptureCore가 반환하는 thumbnail 오류입니다.
:::

:::topic-grid
## 레거시 symbol
- [ICRunLoopMode](https://developer.apple.com/documentation/imagecapturecore/icrunloopmode)
:::

:::topic-grid
## 아티클
- [ImageCaptureCore Constants](https://developer.apple.com/documentation/imagecapturecore/imagecapturecore-constants)
- [ImageCaptureCore Data Types](https://developer.apple.com/documentation/imagecapturecore/imagecapturecore-data-types)
- [ImageCaptureCore Enumerations](https://developer.apple.com/documentation/imagecapturecore/imagecapturecore-enumerations)
- [ImageCaptureCore Macros](https://developer.apple.com/documentation/imagecapturecore/imagecapturecore-macros)
:::
