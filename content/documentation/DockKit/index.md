---
route: /documentation/DockKit
source_url: https://developer.apple.com/documentation/DockKit
source_locale: en-US
section: docc
content_type: symbol
title: DockKit
original_title: DockKit
source_hash: 58fb601e833ee8ebbb8f24b367e89a7641c3fa093dcb1d4f7e7e8411dd417a89
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:51+00:00'
last_translated_at: '2026-03-13T17:35:00+09:00'
---

# DockKit

움직이는 피사체를 카메라로 추적하는 액세서리와 상호 작용합니다.

## 개요

DockKit은 DockKit 호환 전동 스탠드인 dock accessory와 연동하여 비디오 프레임에 나타나는 객체의 위치를 추적합니다. 사람 피사체의 경우 몸과 얼굴 추적을 결합해 향상된 사람 추적을 제공하면서, iPhone 카메라를 어떤 위치에 두면 객체를 가장 잘 프레이밍하고 추적할 수 있는지 판단합니다. *system tracking*이라고 하는 이 기능은 사용자가 호환되는 전동 스탠드에 iPhone을 올려놓고 Camera 앱을 실행하자마자 자동으로 시작됩니다. 예를 들어 공간 안을 움직이는 동안 카메라가 자신을 따라오길 원하는 콘텐츠 제작자나, 교실 안을 돌아다니며 화상 통화를 하는 강사에게 system tracking은 유용합니다.

[DockAccessoryManager](https://developer.apple.com/documentation/dockkit/dockaccessorymanager)와 [DockAccessory](https://developer.apple.com/documentation/dockkit/dockaccessory)를 사용해 system tracking을 비활성화하고 자체 추적 동작을 구현할 수 있습니다. 반려동물이나 작업 중인 한 쌍의 손처럼 사용자 정의 객체의 위치를 따라가려면 자체 추적 동작을 구현하십시오. DockKit 액세서리는 [AVCaptureSession](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession)과 통합되므로 카메라 권한이 있는 앱과 원활하게 함께 동작합니다.

:::topic-grid
## dock accessory 제어
- [Controlling a DockKit accessory using your camera app](https://developer.apple.com/documentation/dockkit/controlling-a-dockkit-accessory-using-your-camera-app): DockKit 액세서리에 장착한 iPhone을 사용해 실시간으로 피사체를 따라갑니다.
- [DockAccessoryManager](https://developer.apple.com/documentation/dockkit/dockaccessorymanager): dock accessory의 상태를 관찰하고 system tracking을 활성화하거나 비활성화합니다.
- [DockAccessory](https://developer.apple.com/documentation/dockkit/dockaccessory): 액세서리 정보를 얻고 추적 동작을 제어합니다.
- [DockKitError](https://developer.apple.com/documentation/dockkit/dockkiterror): DockKit이 보내는 오류 목록입니다.
:::

:::topic-grid
## 추적 동작 사용자화
- [Modify rotation and positioning programmatically](https://developer.apple.com/documentation/dockkit/modify-rotation-and-positioning-behavior-programmatically): dock accessory를 사용자 정의 방식으로 제어합니다.
- [Track custom objects in a frame](https://developer.apple.com/documentation/dockkit/track-custom-objects-in-a-frame): 기계 학습 모델을 사용해 특정 피사체에 초점을 맞춥니다.
:::
