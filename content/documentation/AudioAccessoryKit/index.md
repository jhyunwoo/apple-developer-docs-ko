---
route: /documentation/AudioAccessoryKit
source_url: https://developer.apple.com/documentation/AudioAccessoryKit
source_locale: en-US
section: docc
content_type: symbol
title: AudioAccessoryKit
original_title: AudioAccessoryKit
source_hash: 5c7d6f3f8687d91cf3e23ed5acd3be7bde55aa3a4b007f91ccc528fac5f5aaf6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:11:24+00:00'
last_translated_at: '2026-03-13T23:11:40+09:00'
---

# AudioAccessoryKit

자동 오디오 전환 같은 오디오 기능을 지원합니다.

## 개요

AudioAccessoryKit을 사용하면 서드파티 오디오 액세서리 제조업체가 헤드폰 정보를 시스템에 제공하여 자동 오디오 전환을 지원할 수 있습니다. 예를 들어 사람이 이어버드를 귀에서 빼면 iPhone은 오디오를 스피커로 라우팅할 수 있습니다. 액세서리의 companion 앱은 이어버드의 착용 상태를 [AccessoryControlDevice.Placement.inEar](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/placement/inear)에서 [AccessoryControlDevice.Placement.offHead](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/placement/offhead)로 업데이트합니다. 그러면 iOS는 멀리 있는 액세서리에서 계속 재생하지 않고, 상황에 맞게 오디오 경로를 지능적으로 다시 설정합니다.

companion 앱은 [AccessorySetupKit](https://developer.apple.com/documentation/AccessorySetupKit)으로 액세서리를 페어링한 다음, AudioAccessoryKit을 사용해 [placement](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/capabilities/placement) 같은 액세서리 기능을 등록합니다. 액세서리는 착용 상태 정보뿐 아니라 연결된 오디오 소스도 함께 전달합니다. 자동 오디오 전환에 참여하려면 액세서리 상태가 바뀔 때마다 시스템 정보를 최신 상태로 유지하십시오.

:::important Important
이 프레임워크는 iPhone과 iPad만 지원합니다. 이 프레임워크를 사용하는 앱은 어느 지역의 기기에서든 개발하고 테스트할 수 있습니다. 현재 이 프레임워크는 개발용 빌드 또는 Ad Hoc 테스트용 빌드에 대해서만 동작합니다. App Store 제출, TestFlight, 대체 배포 지원은 추후 제공될 예정입니다.

고객이 설치한 앱에서 이 프레임워크를 사용할 수 있는 경우는, EU에 위치한 기기이면서 EU 국가 또는 지역의 Apple Account로 로그인한 경우에 한합니다.
:::

:::topic-grid
## 핵심
- [Supporting automatic audio switching for third-party accessories](https://developer.apple.com/documentation/audioaccessorykit/supporting-automatic-audio-switching): 연결된 기기 사이에서 오디오가 끊김 없이 라우팅되도록 오디오 액세서리를 구성합니다.
:::

:::topic-grid
## 오디오 구성
- [AccessoryControlDevice](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice): 오디오 액세서리의 기능과 상태를 관리하는 구성 객체입니다.
:::

:::topic-grid
## 기기 특성
- [AccessoryControlDevice.Placement](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/placement): 오디오 액세서리의 물리적 착용 또는 배치 상태입니다.
- [AccessoryControlDevice.Capabilities](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/capabilities): 오디오 액세서리가 지원하는 기능 집합입니다.
- [AccessoryControlDevice.Configuration](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/configuration-swift.struct): 액세서리의 구성 정보입니다.
:::

:::topic-grid
## 오류
- [AccessoryControlDevice.Error](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/error): 오디오 액세서리 구성 작업 중 발생하는 오류입니다.
:::
