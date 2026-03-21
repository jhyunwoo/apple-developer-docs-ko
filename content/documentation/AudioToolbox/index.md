---
route: /documentation/AudioToolbox
source_url: https://developer.apple.com/documentation/AudioToolbox
source_locale: en-US
section: docc
content_type: symbol
title: Audio Toolbox
original_title: Audio Toolbox
source_hash: e49443cb61e2e5d1c024423a03ad3e22b822a9d62df456bcdb5b94210ecb1d93
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:17:58+00:00'
last_translated_at: '2026-03-13T23:18:11+09:00'
---

# Audio Toolbox

오디오를 녹음하거나 재생하고, 포맷을 변환하고, 오디오 스트림을 파싱하고, 오디오 세션을 구성합니다.

## 개요

AudioToolbox 프레임워크는 녹음, 재생, 스트림 파싱을 위한 인터페이스를 제공합니다. iOS에서는 오디오 세션을 관리하는 추가 인터페이스도 제공합니다.

:::topic-grid
## 핵심
- [Porting your audio code to Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/porting-your-audio-code-to-apple-silicon): Apple silicon Mac에서 실행할 때 오디오 관련 코드의 문제를 제거합니다.
:::

:::topic-grid
## Audio Unit
- [Generating spatial audio from a multichannel audio stream](https://developer.apple.com/documentation/audiotoolbox/generating-spatial-audio-from-a-multichannel-audio-stream): spatial mixer audio unit을 사용해 8채널 오디오를 2채널 spatial audio로 변환합니다.
- [Audio Unit v3 Plug-Ins](https://developer.apple.com/documentation/audiotoolbox/audio-unit-v3-plug-ins): Audio Unit v3 앱 extension을 사용해 사용자 정의 오디오 효과, 악기, 기타 오디오 동작을 제공합니다.
- [Audio Components](https://developer.apple.com/documentation/audiotoolbox/audio-components): Audio Unit 및 오디오 codec 같은 오디오 구성 요소를 찾고, 불러오고, 구성합니다.
- [Audio Unit v2 (C) API](https://developer.apple.com/documentation/audiotoolbox/audio-unit-v2-c-api): Audio Unit을 구성하고 오디오 렌더링을 준비합니다.
- [Audio Unit Properties](https://developer.apple.com/documentation/audiotoolbox/audio-unit-properties): 내장 mixer, equalizer, filter, effect 및 기타 Audio Unit 앱 extension에 대한 정보를 가져옵니다.
- [Audio Unit Voice I/O](https://developer.apple.com/documentation/audiotoolbox/audio-unit-voice-i-o): 시스템 음성 처리를 구성하고 음성 이벤트에 대응합니다.
:::

:::topic-grid
## 재생 및 녹음
- [Audio Queue Services](https://developer.apple.com/documentation/audiotoolbox/audio-queue-services): 오디오 하드웨어에 연결하고 녹음 또는 재생 과정을 관리합니다.
- [Audio Services](https://developer.apple.com/documentation/audiotoolbox/audio-services): 적절한 하드웨어를 갖춘 iOS 기기에서 짧은 소리를 재생하거나 진동 효과를 트리거합니다.
- [Music Player](https://developer.apple.com/documentation/audiotoolbox/music-player): 트랙 시퀀스를 만들고 재생하며, 표준 이벤트에 따라 재생 관련 측면을 관리합니다.
- [Anchoring sound to a window or volume](https://developer.apple.com/documentation/audiotoolbox/spatializing-sound-from-a-uiscene): 3D 공간의 window와 volume에 소리를 부착해 고유한 앱 경험을 제공합니다.
:::

:::topic-grid
## 오디오 파일 및 포맷
- [Audio Format Services](https://developer.apple.com/documentation/audiotoolbox/audio-format-services): 오디오 포맷과 codec에 대한 정보에 접근합니다.
- [Audio File Services](https://developer.apple.com/documentation/audiotoolbox/audio-file-services): 다양한 오디오 데이터를 디스크 또는 메모리 buffer에서 읽고 씁니다.
- [Extended Audio File Services](https://developer.apple.com/documentation/audiotoolbox/extended-audio-file-services): 단순화된 인터페이스로 압축 파일과 linear PCM 오디오 파일을 읽고 씁니다.
- [Audio File Stream Services](https://developer.apple.com/documentation/audiotoolbox/audio-file-stream-services): 사용자의 컴퓨터에 데이터가 도착하는 대로 스트리밍 오디오 파일을 파싱합니다.
- [Audio File Components](https://developer.apple.com/documentation/audiotoolbox/audio-file-components): 오디오 파일 포맷과 오디오 데이터를 포함한 파일에 대한 정보를 가져옵니다.
- [Core Audio File Format](https://developer.apple.com/documentation/audiotoolbox/core-audio-file-format): Core Audio 파일 구조를 파싱합니다.
:::

:::topic-grid
## 유틸리티
- [Analyzing audio performance with Instruments](https://developer.apple.com/documentation/audiotoolbox/analyzing-audio-performance-with-instruments): Audio System Trace를 사용해 앱에서 부드럽고 몰입감 있는 오디오 경험을 보장합니다.
- [Audio Converter Services](https://developer.apple.com/documentation/audiotoolbox/audio-converter-services): linear PCM 오디오 포맷 사이와 linear PCM 및 압축 포맷 사이를 변환합니다.
- [Audio Session Support](https://developer.apple.com/documentation/audiotoolbox/audio-session-support): 오디오 세션과 오디오 경로에 연결하는 속성을 설명합니다.
- [Audio Toolbox Debugging](https://developer.apple.com/documentation/audiotoolbox/audio-toolbox-debugging): 코드 개발 및 디버깅 중 Core Audio 객체의 내부 상태를 얻습니다.
- [Workgroup Management](https://developer.apple.com/documentation/audiotoolbox/workgroup-management): 사용자 정의 실시간 오디오 스레드 활동을 시스템 및 다른 프로세스와 조정합니다.
- [Audio Codec](https://developer.apple.com/documentation/audiotoolbox/audio-codec): 오디오 데이터를 한 포맷에서 다른 포맷으로 변환합니다.
- [Clock Utilities](https://developer.apple.com/documentation/audiotoolbox/clock-utilities): 오디오 재생과 관련된 시간 정보를 관리합니다.
:::

:::topic-grid
## 지원 중단
- [Deprecated Symbols](https://developer.apple.com/documentation/audiotoolbox/deprecated-symbols): 더 이상 지원하지 않는 심볼과 대체 항목을 검토합니다.
:::

:::topic-grid
## 참고 자료
- [AudioToolbox Structures](https://developer.apple.com/documentation/audiotoolbox/audiotoolbox-structures)
- [AudioToolbox Enumerations](https://developer.apple.com/documentation/audiotoolbox/audiotoolbox-enumerations)
- [AudioToolbox Constants](https://developer.apple.com/documentation/audiotoolbox/audiotoolbox-constants)
- [AudioToolbox Functions](https://developer.apple.com/documentation/audiotoolbox/audiotoolbox-functions)
- [AudioToolbox Data Types](https://developer.apple.com/documentation/audiotoolbox/audiotoolbox-data-types)
:::

:::topic-grid
## 매크로
- [Macros](https://developer.apple.com/documentation/audiotoolbox/audiotoolbox-macros)
:::

:::topic-grid
## 프로토콜
- [SpatialAudioExperience](https://developer.apple.com/documentation/audiotoolbox/spatialaudioexperience): spatial computing을 위해 오디오 스트림을 구성합니다.
:::

:::topic-grid
## 구조체
- [AutomaticSpatialAudio](https://developer.apple.com/documentation/audiotoolbox/automaticspatialaudio): 시스템이 결정하는 spatial audio 경험입니다.
- [BypassedSpatialAudio](https://developer.apple.com/documentation/audiotoolbox/bypassedspatialaudio): 시스템이 오디오 스트림에 공간 처리를 적용하지 않는 경험입니다.
- [FixedSpatialAudio](https://developer.apple.com/documentation/audiotoolbox/fixedspatialaudio): 사용자 움직임을 고려하지 않는 공간 경험입니다.
- [HeadTrackedSpatialAudio](https://developer.apple.com/documentation/audiotoolbox/headtrackedspatialaudio): 사용자 움직임을 고려하는 공간 경험입니다.
:::

:::topic-grid
## 변수
- [kAUAudioMixParameter_RemixAmount](https://developer.apple.com/documentation/audiotoolbox/kauaudiomixparameter_remixamount)
- [kAUAudioMixParameter_Style](https://developer.apple.com/documentation/audiotoolbox/kauaudiomixparameter_style)
- [kAUAudioMixProperty_EnableSpatialization](https://developer.apple.com/documentation/audiotoolbox/kauaudiomixproperty_enablespatialization)
- [kAUAudioMixProperty_SpatialAudioMixMetadata](https://developer.apple.com/documentation/audiotoolbox/kauaudiomixproperty_spatialaudiomixmetadata)
- [kAudioCodecContentSource_AV_Spatial_Live](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_av_spatial_live)
- [kAudioCodecContentSource_AV_Spatial_Offline](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_av_spatial_offline)
- [kAudioCodecContentSource_AV_Traditional_Live](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_av_traditional_live)
- [kAudioCodecContentSource_AV_Traditional_Offline](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_av_traditional_offline)
- [kAudioCodecContentSource_AppleAV_Spatial_Live](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_appleav_spatial_live)
- [kAudioCodecContentSource_AppleAV_Spatial_Offline](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_appleav_spatial_offline)
- [kAudioCodecContentSource_AppleAV_Traditional_Live](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_appleav_traditional_live)
- [kAudioCodecContentSource_AppleAV_Traditional_Offline](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_appleav_traditional_offline)
- [kAudioCodecContentSource_AppleCapture_Spatial](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_applecapture_spatial)
- [kAudioCodecContentSource_AppleCapture_Spatial_Enhanced](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_applecapture_spatial_enhanced)
- [kAudioCodecContentSource_AppleCapture_Traditional](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_applecapture_traditional)
- [kAudioCodecContentSource_AppleMusic_Spatial](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_applemusic_spatial)
- [kAudioCodecContentSource_AppleMusic_Traditional](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_applemusic_traditional)
- [kAudioCodecContentSource_ApplePassthrough](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_applepassthrough)
- [kAudioCodecContentSource_Capture_Spatial](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_capture_spatial)
- [kAudioCodecContentSource_Capture_Spatial_Enhanced](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_capture_spatial_enhanced)
- [kAudioCodecContentSource_Capture_Traditional](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_capture_traditional)
- [kAudioCodecContentSource_Music_Spatial](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_music_spatial)
- [kAudioCodecContentSource_Music_Traditional](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_music_traditional)
- [kAudioCodecContentSource_Passthrough](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_passthrough)
- [kAudioCodecContentSource_Reserved](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_reserved)
- [kAudioCodecContentSource_Unspecified](https://developer.apple.com/documentation/audiotoolbox/kaudiocodeccontentsource_unspecified)
- [kAudioCodecDynamicRangeControlConfiguration_Capture](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecdynamicrangecontrolconfiguration_capture)
- [kAudioCodecDynamicRangeControlConfiguration_Movie](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecdynamicrangecontrolconfiguration_movie)
- [kAudioCodecDynamicRangeControlConfiguration_Music](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecdynamicrangecontrolconfiguration_music)
- [kAudioCodecDynamicRangeControlConfiguration_None](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecdynamicrangecontrolconfiguration_none)
- [kAudioCodecDynamicRangeControlConfiguration_Speech](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecdynamicrangecontrolconfiguration_speech)
- [kAudioCodecPropertyASPFrequency](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecpropertyaspfrequency)
- [kAudioCodecPropertyContentSource](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecpropertycontentsource)
- [kAudioCodecPropertyDynamicRangeControlConfiguration](https://developer.apple.com/documentation/audiotoolbox/kaudiocodecpropertydynamicrangecontrolconfiguration)
- [kAudioConverterPropertyChannelMixMap](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertychannelmixmap)
- [kAudioConverterPropertyPerformDownmix](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterpropertyperformdownmix)
- [kAudioUnitErr_MultipleVoiceProcessors](https://developer.apple.com/documentation/audiotoolbox/kaudiouniterr_multiplevoiceprocessors)
- [kAudioUnitSubType_AUAudioMix](https://developer.apple.com/documentation/audiotoolbox/kaudiounitsubtype_auaudiomix)
:::

:::topic-grid
## 함수
- [AudioConverterFillComplexBufferRealtimeSafe(_:_:_:_:_:_:)](https://developer.apple.com/documentation/audiotoolbox/audioconverterfillcomplexbufferrealtimesafe(_:_:_:_:_:_:))
- [AudioConverterFillComplexBufferWithPacketDependencies(_:_:_:_:_:_:_:)](https://developer.apple.com/documentation/audiotoolbox/audioconverterfillcomplexbufferwithpacketdependencies(_:_:_:_:_:_:_:))
- [AudioFileWritePacketsWithDependencies(_:_:_:_:_:_:_:_:)](https://developer.apple.com/documentation/audiotoolbox/audiofilewritepacketswithdependencies(_:_:_:_:_:_:_:_:))
- [AudioServicesPlayAlertSound(_:spatialExperience:)](https://developer.apple.com/documentation/audiotoolbox/audioservicesplayalertsound(_:spatialexperience:)): 제공한 spatial audio 경험으로 경고음을 재생합니다.
- [AudioServicesPlaySystemSound(_:spatialExperience:)](https://developer.apple.com/documentation/audiotoolbox/audioservicesplaysystemsound(_:spatialexperience:)): 제공한 spatial audio 경험으로 시스템 사운드를 재생합니다.
:::

:::topic-grid
## 타입 별칭
- [AudioConverterComplexInputDataProcRealtimeSafe](https://developer.apple.com/documentation/audiotoolbox/audioconvertercomplexinputdataprocrealtimesafe)
:::

:::topic-grid
## 열거형
- [AUAudioMixRenderingStyle](https://developer.apple.com/documentation/audiotoolbox/auaudiomixrenderingstyle)
- [SpatialAudioExperiences](https://developer.apple.com/documentation/audiotoolbox/spatialaudioexperiences)
:::
