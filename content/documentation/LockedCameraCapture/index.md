---
route: /documentation/LockedCameraCapture
source_url: https://developer.apple.com/documentation/LockedCameraCapture
source_locale: en-US
section: docc
content_type: symbol
title: LockedCameraCapture
original_title: LockedCameraCapture
source_hash: ab2d9c93b272d5a751fb4d81b12e6b1c5124c87feb3c5699ccc50a1a2eda49dc
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:52+00:00'
last_translated_at: '2026-03-13T17:35:00+09:00'
---

# LockedCameraCapture

기기가 잠겨 있을 때도 앱의 카메라 경험으로 콘텐츠를 캡처합니다.

## 개요

LockedCameraCapture 프레임워크를 사용하면 기기가 잠겨 있을 때도 사용자가 앱의 카메라 경험을 실행해 빠르게 콘텐츠를 캡처할 수 있는 extension을 만들 수 있습니다. 이 extension은 Control Center, Lock Screen, Action 버튼에서 카메라 경험에 접근할 수 있게 해 줍니다.

![iPhone의 잠금 화면, iPhone의 제어 센터, iPhone 15 Pro의 Action 버튼에서 카메라 아이콘이 있는 컨트롤을 보여 주는 개념 이미지입니다.](https://developer.apple.com)

:::topic-grid
## 핵심 사항
- [Creating a camera experience for the Lock Screen](https://developer.apple.com/documentation/lockedcameracapture/creating-a-camera-experience-for-the-lock-screen): Control Center, Lock Screen, Action 버튼에서 잠긴 기기용 앱의 카메라 경험을 제공합니다.
:::

:::topic-grid
## 캡처와 실행
- [LockedCameraCaptureUIScene](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracaptureuiscene): 잠금 상태 카메라 캡처 extension에 표시할 session 객체와 UI를 담는 구조체입니다.
- [LockedCameraCaptureSession](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturesession): extension을 포함한 앱을 열도록 요청할 수 있고 session 구성 업데이트를 수신하는 객체입니다.
:::

:::topic-grid
## 앱 통합
- [LockedCameraCaptureManager](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracapturemanager): 캡처한 콘텐츠 처리와 extension의 포함 앱으로 전환하는 기능을 제공하는 객체입니다.
- [NSUserActivityTypeLockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture/nsuseractivitytypelockedcameracapture): 캡처 extension에서 앱을 열 때 사용하는 타입입니다.
:::

:::topic-grid
## extension
- [LockedCameraCaptureExtension](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracaptureextension): 잠금 상태 카메라 캡처 extension을 생성하는 프로토콜입니다.
- [LockedCameraCaptureExtensionScene](https://developer.apple.com/documentation/lockedcameracapture/lockedcameracaptureextensionscene): 잠금 상태 카메라 캡처 extension의 UI를 제공하는 프로토콜입니다.
:::
