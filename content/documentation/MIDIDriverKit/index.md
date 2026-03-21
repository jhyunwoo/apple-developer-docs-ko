---
route: /documentation/MIDIDriverKit
source_url: https://developer.apple.com/documentation/MIDIDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: MIDIDriverKit
original_title: MIDIDriverKit
source_hash: 7c01306403fcc89fd80ca52a5a8fc7736c987a61623b632c4dfa1d1b795475c2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T05:21:16+00:00'
last_translated_at: '2026-03-13T05:21:16+00:00'
---

# MIDIDriverKit

MIDI 기기용 드라이버를 개발합니다.

## 개요

MIDIDriverKit 프레임워크를 사용해 Core MIDI와 통신하는 MIDI 드라이버 확장을 구현하세요. 이 프레임워크는 드라이버 확장과 Core MIDI 서버 사이의 모든 사용자 클라이언트 통신을 처리하므로 MIDI 드라이버 플러그인을 구현할 필요가 없습니다. 구현 시 [USBDriverKit](https://developer.apple.com/documentation/USBDriverKit) 같은 다른 전송 기반 드라이버 확장 프레임워크도 활용할 수 있습니다.

:::topic-grid
## 핵심
- [Creating a MIDI device driver](https://developer.apple.com/documentation/mididriverkit/creating-a-midi-device-driver): macOS와 iPadOS의 사용자 공간에서 실행되는 구성 가능한 가상 MIDI 드라이버를 드라이버 확장으로 구현합니다.
- [com.apple.developer.driverkit.family.midi](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.midi): 드라이버를 MIDI를 지원하는 기기와 매칭할지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 클래스
- [IOUserMIDIDestination](https://developer.apple.com/documentation/mididriverkit/iousermididestination)
- [IOUserMIDIDevice](https://developer.apple.com/documentation/mididriverkit/iousermididevice)
- [IOUserMIDIDriver](https://developer.apple.com/documentation/mididriverkit/iousermididriver)
- [IOUserMIDIEndpoint](https://developer.apple.com/documentation/mididriverkit/iousermidiendpoint)
- [IOUserMIDIEntity](https://developer.apple.com/documentation/mididriverkit/iousermidientity)
- [IOUserMIDIObject](https://developer.apple.com/documentation/mididriverkit/iousermidiobject)
- [IOUserMIDISource](https://developer.apple.com/documentation/mididriverkit/iousermidisource)
:::

:::topic-grid
## 레퍼런스
- [MIDIDriverKit Constants](https://developer.apple.com/documentation/mididriverkit/mididriverkit-constants)
- [MIDIDriverKit Data Types](https://developer.apple.com/documentation/mididriverkit/mididriverkit-data-types)
:::

:::topic-grid
## 네임스페이스
- [MIDIDriverKit](https://developer.apple.com/documentation/mididriverkit/mididriverkit)
:::

:::topic-grid
## 매크로
- [kIOUserMIDIDriverUserClientType](https://developer.apple.com/documentation/mididriverkit/kiousermididriveruserclienttype)
:::
