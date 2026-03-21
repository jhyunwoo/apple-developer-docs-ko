---
route: /documentation/AudioUnit
source_url: https://developer.apple.com/documentation/AudioUnit
source_locale: en-US
section: docc
content_type: symbol
title: Audio Unit
original_title: Audio Unit
source_hash: 59c8436f68e351febdbcd5c97a06bfb59f8f4f519a53b9a8cd2e7f6343c9694a
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:07:37+00:00'
last_translated_at: '2026-03-14T03:28:00+09:00'
---

# Audio Unit

앱에 정교한 오디오 조작 및 처리 기능을 추가합니다.

## 개요

Audio Unit 프레임워크는 버전 2 또는 버전 3 audio unit을 호스팅하기 위한 인터페이스와, Audio Unit extension으로 알려진 버전 3 오디오 처리 plug-in을 구현하기 위한 인터페이스를 제공합니다. 버전 3 Audio Unit을 구현하는 개발자는 [AUAudioUnit](https://developer.apple.com/documentation/AudioToolbox/AUAudioUnit) 클래스를 subclass해야 합니다.

버전 3 Audio Unit extension은 host app이 iOS, tvOS, macOS에서 사용할 수 있으며 App Store를 통해 배포할 수 있습니다.

:::topic-grid
## 변수
- [AUDIO_UNIT_VERSION](https://developer.apple.com/documentation/audiounit/audio_unit_version)
:::
