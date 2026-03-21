---
route: /documentation/CoreMIDI
source_url: https://developer.apple.com/documentation/CoreMIDI
source_locale: en-US
section: docc
content_type: symbol
title: Core MIDI
original_title: Core MIDI
source_hash: 3dd24799c690f43a6ab45eb3ce456ed5d0a620ebd700a474ca77c4178952907d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:24:06+00:00'
last_translated_at: '2026-03-14T01:12:00+09:00'
---

# Core MIDI

하드웨어 키보드와 신시사이저 같은 MIDI 장치와 통신합니다.

## 개요

Core MIDI 프레임워크는 하드웨어 키보드와 신시사이저를 포함한 MIDI(Musical Instrument Digital Interface) 장치와 통신하기 위한 API를 제공합니다. iOS 기기에서는 dock connector 또는 네트워크를 사용해 연결할 수 있습니다. Dock connector 사용에 대한 자세한 내용은 [MFi Program](https://developer.apple.com/programs/mfi/)을 참고하십시오.

:::topic-grid
## 서비스
- [MIDI Services](https://developer.apple.com/documentation/coremidi/midi-services): Universal MIDI Packet을 사용해 하드웨어와 통신합니다.
- [MIDI System Setup](https://developer.apple.com/documentation/coremidi/midi-system-setup): 전역 MIDI 시스템을 구성합니다.
- [MIDI Bluetooth](https://developer.apple.com/documentation/coremidi/midi-bluetooth): Bluetooth Low Energy MIDI 주변 장치에 연결합니다.
- [MIDI Messages](https://developer.apple.com/documentation/coremidi/midi-messages): 메시지를 만들고 구성합니다.
- [MIDI Thru Connection](https://developer.apple.com/documentation/coremidi/midi-thru-connection): source와 destination 사이의 play-through 연결을 생성합니다.
- [MIDI Networking](https://developer.apple.com/documentation/coremidi/midi-networking): 로컬 네트워크를 통해 연결된 장치를 생성하고 관리합니다.
- [MIDI Drivers](https://developer.apple.com/documentation/coremidi/midi-drivers): 드라이버 plug-in을 만듭니다.
- [MIDI Capability Inquiry](https://developer.apple.com/documentation/coremidi/midi-capability-inquiry): 장치의 양방향 검색 및 구성을 지원합니다.
:::

:::topic-grid
## 참고 자료
- [Core MIDI Structures](https://developer.apple.com/documentation/coremidi/core-midi-structures)
- [Core MIDI Enumerations](https://developer.apple.com/documentation/coremidi/core-midi-enumerations)
- [Core MIDI Constants](https://developer.apple.com/documentation/coremidi/core-midi-constants)
- [Core MIDI Functions](https://developer.apple.com/documentation/coremidi/core-midi-functions)
- [Core MIDI Data Types](https://developer.apple.com/documentation/coremidi/core-midi-data-types)
- [Core MIDI Macros](https://developer.apple.com/documentation/coremidi/coremidi-macros)
:::

:::topic-grid
## 아티클
- [Deprecated Symbols](https://developer.apple.com/documentation/coremidi/midi_system_setup-deprecated-symbols): 더 이상 지원되지 않는 symbol과 그 대체 항목을 검토합니다.
- [kMIDIObjectType_ExternalMask](https://developer.apple.com/documentation/coremidi/kmidiobjecttype_externalmask): 장치가 외부 장치임을 나타내는 비트 마스크입니다.
:::

:::topic-grid
## 클래스
- [MIDI2DeviceInfo](https://developer.apple.com/documentation/coremidi/midi2deviceinfo)
- [MIDICIDevice](https://developer.apple.com/documentation/coremidi/midicidevice)
- [MIDICIDeviceManager](https://developer.apple.com/documentation/coremidi/midicidevicemanager)
- [MIDICIDiscoveredNode](https://developer.apple.com/documentation/coremidi/midicidiscoverednode): capability inquiry에 응답하는 MIDI source와 destination을 나타내는 발견된 MIDI-CI 노드입니다.
- [MIDIUMPCIProfile](https://developer.apple.com/documentation/coremidi/midiumpciprofile)
- [MIDIUMPEndpoint](https://developer.apple.com/documentation/coremidi/midiumpendpoint)
- [MIDIUMPEndpointManager](https://developer.apple.com/documentation/coremidi/midiumpendpointmanager)
- [MIDIUMPFunctionBlock](https://developer.apple.com/documentation/coremidi/midiumpfunctionblock)
- [MIDIUMPMutableEndpoint](https://developer.apple.com/documentation/coremidi/midiumpmutableendpoint)
- [MIDIUMPMutableFunctionBlock](https://developer.apple.com/documentation/coremidi/midiumpmutablefunctionblock)
:::

:::topic-grid
## 변수
- [kMIDINoteAttributeManufacturerSpecific](https://developer.apple.com/documentation/coremidi/kmidinoteattributemanufacturerspecific)
- [kMIDINoteAttributeNone](https://developer.apple.com/documentation/coremidi/kmidinoteattributenone)
- [kMIDINoteAttributePitch](https://developer.apple.com/documentation/coremidi/kmidinoteattributepitch)
- [kMIDINoteAttributeProfileSpecific](https://developer.apple.com/documentation/coremidi/kmidinoteattributeprofilespecific)
:::
