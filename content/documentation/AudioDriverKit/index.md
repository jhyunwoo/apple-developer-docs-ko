---
route: /documentation/AudioDriverKit
source_url: https://developer.apple.com/documentation/AudioDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: AudioDriverKit
original_title: AudioDriverKit
source_hash: f11e287b09e706481c7c7a785f2e135c43ed8dd1da8366f6da0e9dfbd766eda5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:24:09+00:00'
last_translated_at: '2026-03-13T09:10:00+00:00'
---

# AudioDriverKit

오디오 기기용 드라이버를 개발합니다.

## 개요

AudioDriverKit 프레임워크는 CoreAudio HAL과 통신하는 [DriverKit](https://developer.apple.com/documentation/DriverKit) 기반 오디오 확장의 개발을 지원합니다. AudioDriverKit는 CoreAudio HAL과 드라이버 확장 사이에 필요한 모든 user client 통신을 처리하므로, 오디오 서버 플러그인을 직접 구현할 필요가 없습니다. 또한 [PCIDriverKit](https://developer.apple.com/documentation/PCIDriverKit) 같은 transport 기반 드라이버 확장 프레임워크와 통합할 수도 있습니다.

[IOUserAudioDriver](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver)를 서브클래싱하여 드라이버를 개발하세요. macOS에서는 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용해 드라이버를 설치하고 업그레이드합니다. iPadOS에서는 시스템이 호스트 앱과 함께 드라이버를 자동으로 검색하고 업그레이드합니다.

:::note Note
AudioDriverKit는 Intel 및 Apple Silicon 기기의 macOS에서, 그리고 M 시리즈 프로세서를 탑재한 기기의 iPadOS에서 사용할 수 있습니다.
:::

:::topic-grid
## 필수 항목
- [IOUserAudioObject](https://developer.apple.com/documentation/audiodriverkit/iouseraudioobject): 프레임워크 대부분의 클래스에 대한 기반 클래스입니다.
- [IOUserAudioDriver](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodriver): 오디오 기기와의 통신을 관리하는 DriverKit provider 객체입니다.
- [DriverKit Audio Family](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.audio): 기기가 오디오 기능을 지원하는지 나타내는 불리언 값입니다.
- [오디오 기기 드라이버 만들기](https://developer.apple.com/documentation/audiodriverkit/creating-an-audio-device-driver): macOS와 iPadOS의 사용자 공간에서 실행되는 드라이버 확장으로 구성 가능한 오디오 입력 소스를 구현합니다.
:::

:::topic-grid
## 오디오 기기 다루기
- [IOUserAudioClockDevice](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice): 동기화와 I/O 수행에 사용하는 오디오 클록 기기 객체입니다.
- [IOUserAudioDevice](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice): I/O 실행을 위한 구성을 처리하는 오디오 클록 기기 객체입니다.
:::

:::topic-grid
## 오디오 객체 컨테이너
- [IOUserAudioBox](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox): 다른 오디오 객체, 일반적으로 오디오 기기와 오디오 클록 기기를 담는 컨테이너입니다.
:::

:::topic-grid
## 오디오 스트림 다루기
- [IOUserAudioStream](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream): 오디오 기기에 대한 I/O를 수행하는 오디오 객체입니다.
:::

:::topic-grid
## 오디오 컨트롤 사용하기
- [IOUserAudioControl](https://developer.apple.com/documentation/audiodriverkit/iouseraudiocontrol): 오디오 컨트롤 객체의 기반 클래스입니다.
- [IOUserAudioBooleanControl](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobooleancontrol): 불리언 값을 설정할 수 있는 컨트롤 객체입니다.
- [IOUserAudioStereoPanControl](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostereopancontrol): 스테레오 채널 사이에서 pan을 설정할 수 있는 컨트롤 객체입니다.
- [IOUserAudioSliderControl](https://developer.apple.com/documentation/audiodriverkit/iouseraudioslidercontrol): 32비트 정수 값을 설정할 수 있는 컨트롤 객체입니다.
- [IOUserAudioSelectorControl](https://developer.apple.com/documentation/audiodriverkit/iouseraudioselectorcontrol): 값 집합 중 하나를 선택할 수 있는 컨트롤 객체입니다.
- [IOUserAudioLevelControl](https://developer.apple.com/documentation/audiodriverkit/iouseraudiolevelcontrol): 스칼라 값 또는 데시벨 값으로 오디오 레벨을 설정할 수 있는 컨트롤 객체입니다.
:::

:::topic-grid
## 지원 타입
- [IOUserAudioReservedConfigChangeAction](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioreservedconfigchangeaction): 구성 변경이 필요한 객체 상태 변경에 대한 식별자입니다.
:::

:::topic-grid
## 네임스페이스
- [AudioDriverKit](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit)
:::

:::topic-grid
## 매크로
- [DebugMsg](https://developer.apple.com/documentation/audiodriverkit/debugmsg)
- [FailIf](https://developer.apple.com/documentation/audiodriverkit/failif)
- [FailIfError](https://developer.apple.com/documentation/audiodriverkit/failiferror)
- [FailIfNULL](https://developer.apple.com/documentation/audiodriverkit/failifnull)
- [kIOUserAudioDriverUserClientType](https://developer.apple.com/documentation/audiodriverkit/kiouseraudiodriveruserclienttype)
:::
