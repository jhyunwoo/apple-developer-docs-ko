---
route: /documentation/CoreAudioTypes
source_url: https://developer.apple.com/documentation/CoreAudioTypes
source_locale: en-US
section: docc
content_type: symbol
title: Core Audio Types
original_title: Core Audio Types
source_hash: 779a9759b6e6ef2dbdabdefb7106d974d17a448b0b9e12c0a729d14f90bf86e1
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:41:07+00:00'
last_translated_at: '2026-03-14T01:17:00+09:00'
---

# Core Audio Types

오디오 스트림, 복합 버퍼, 오디오비주얼 타임스탬프와 상호 작용하기 위한 특수 데이터 타입을 사용합니다.

## 개요

Core Audio Types 프레임워크는 다른 Core Audio 인터페이스가 사용하는 공통 데이터 타입과 상수를 선언합니다. 이 프레임워크에는 여러 편의 함수도 포함되어 있습니다.

오디오 데이터 조작과 관련된 특수 용어가 익숙하지 않다면 [Core Audio Glossary](https://developer.apple.com/library/archive/documentation/MusicAudio/Reference/CoreAudioGlossary/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004453)를 참고하십시오.

:::topic-grid
## 버퍼
- [AudioBuffer](https://developer.apple.com/documentation/coreaudiotypes/audiobuffer): 오디오 데이터 버퍼를 담는 구조체입니다.
- [AudioBufferList](https://developer.apple.com/documentation/coreaudiotypes/audiobufferlist): 가변 길이 오디오 버퍼 배열을 저장하는 구조체입니다.
:::

:::topic-grid
## 채널
- [AudioChannelDescription](https://developer.apple.com/documentation/coreaudiotypes/audiochanneldescription): 오디오 데이터 채널을 설명하는 구조체입니다.
- [AudioChannelLayout](https://developer.apple.com/documentation/coreaudiotypes/audiochannellayout): 파일 또는 하드웨어 안의 채널 레이아웃을 지정하는 구조체입니다.
:::

:::topic-grid
## 코덱
- [AudioClassDescription](https://developer.apple.com/documentation/coreaudiotypes/audioclassdescription): 오디오 코덱을 설명하는 구조체입니다.
:::

:::topic-grid
## 오디오 시간
- [AudioTimeStamp](https://developer.apple.com/documentation/coreaudiotypes/audiotimestamp): 타임스탬프 값을 나타내는 구조체입니다.
- [AudioTimeStampFlags](https://developer.apple.com/documentation/coreaudiotypes/audiotimestampflags): 타임스탬프용 플래그를 나타내는 구조체입니다.
:::

:::topic-grid
## SMPTE 시간
- [SMPTETime](https://developer.apple.com/documentation/coreaudiotypes/smptetime): SMPTE 시간 값을 정의하는 구조체입니다.
- [SMPTETimeFlags](https://developer.apple.com/documentation/coreaudiotypes/smptetimeflags): SMPTE 시간 플래그를 정의하는 구조체입니다.
- [SMPTETimeType](https://developer.apple.com/documentation/coreaudiotypes/smptetimetype): SMPTE 시간 유형을 정의하는 상수입니다.
:::

:::topic-grid
## 값
- [AudioValueRange](https://developer.apple.com/documentation/coreaudiotypes/audiovaluerange): 연속된 값 범위를 나타내는 구조체입니다.
- [AudioValueTranslation](https://developer.apple.com/documentation/coreaudiotypes/audiovaluetranslation): 변환 작업에 사용할 버퍼를 저장하는 구조체입니다.
:::

:::topic-grid
## 스트림
- [AudioStreamBasicDescription](https://developer.apple.com/documentation/coreaudiotypes/audiostreambasicdescription): 오디오 스트림의 형식 명세입니다.
- [AudioStreamPacketDescription](https://developer.apple.com/documentation/coreaudiotypes/audiostreampacketdescription): 오디오 데이터 버퍼 안의 packet을 설명하는 값입니다.
- [AudioFormatFlags](https://developer.apple.com/documentation/coreaudiotypes/audioformatflags): 오디오 형식 플래그의 타입 정의입니다.
- [Audio Format Flags](https://developer.apple.com/documentation/coreaudiotypes/audio-format-flags): 오디오 스트림 설명에 자주 사용하는 데이터 형식 플래그 조합입니다.
- [AudioFormatID](https://developer.apple.com/documentation/coreaudiotypes/audioformatid): 오디오 형식 식별자의 타입 정의입니다.
- [Audio Format Identifiers](https://developer.apple.com/documentation/coreaudiotypes/audio-format-identifiers): 지원되는 오디오 형식의 식별자입니다.
- [kAudioStreamAnyRate](https://developer.apple.com/documentation/coreaudiotypes/kaudiostreamanyrate): 오디오 스트림이 어떤 sample rate든 사용할 수 있음을 나타내는 값입니다.
- [MPEG4ObjectID](https://developer.apple.com/documentation/coreaudiotypes/mpeg4objectid): MPEG-4 오디오 데이터 유형을 정의하는 상수입니다.
:::

:::topic-grid
## 공통 타입
- [AVAudioInteger](https://developer.apple.com/documentation/coreaudiotypes/avaudiointeger): 오디오 작업용 정수 타입입니다.
- [AVAudioUInteger](https://developer.apple.com/documentation/coreaudiotypes/avaudiouinteger): 오디오 작업용 부호 없는 정수 타입입니다.
- [AudioSessionID](https://developer.apple.com/documentation/coreaudiotypes/audiosessionid): 오디오 세션의 고유 식별자입니다.
- [kAudioUnitSampleFractionBits](https://developer.apple.com/documentation/coreaudiotypes/kaudiounitsamplefractionbits): 고정소수점 sample의 소수 비트 수입니다.
- [COREAUDIOTYPES_VERSION](https://developer.apple.com/documentation/coreaudiotypes/coreaudiotypes_version): Core Audio Types 버전을 나타내는 값입니다.
- [AudioSampleType](https://developer.apple.com/documentation/coreaudiotypes/audiosampletype): 입력 및 출력용 표준 오디오 데이터 sample 타입입니다.
- [AudioUnitSampleType](https://developer.apple.com/documentation/coreaudiotypes/audiounitsampletype): 오디오 처리용 표준 오디오 데이터 sample 타입입니다.
- [AudioFormatListItem](https://developer.apple.com/documentation/coreaudiotypes/audioformatlistitem)
:::

:::topic-grid
## 오류
- [kAudio_ParamError](https://developer.apple.com/documentation/coreaudiotypes/kaudio_paramerror): 함수의 매개변수 목록에 오류가 있음을 나타냅니다.
- [kAudio_MemFullError](https://developer.apple.com/documentation/coreaudiotypes/kaudio_memfullerror): heap zone이 가득 찼음을 나타내는 오류입니다.
- [kAudio_FileNotFoundError](https://developer.apple.com/documentation/coreaudiotypes/kaudio_filenotfounderror): 파일을 찾지 못했음을 나타내는 오류입니다.
- [kAudio_UnimplementedError](https://developer.apple.com/documentation/coreaudiotypes/kaudio_unimplementederror): 앱이 구현되지 않은 시스템 함수를 호출했음을 나타내는 오류입니다.
:::

:::topic-grid
## 참고 자료
- [CoreAudioTypes Enumerations](https://developer.apple.com/documentation/coreaudiotypes/coreaudiotypes-enumerations)
:::

:::topic-grid
## 구조체
- [AudioStreamPacketDependencyDescription](https://developer.apple.com/documentation/coreaudiotypes/audiostreampacketdependencydescription)
:::

:::topic-grid
## 변수
- [kAudioChannelLayoutTag_Ogg_3_0](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_ogg_3_0)
- [kAudioChannelLayoutTag_Ogg_4_0](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_ogg_4_0)
- [kAudioChannelLayoutTag_Ogg_5_0](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_ogg_5_0)
- [kAudioChannelLayoutTag_Ogg_5_1](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_ogg_5_1)
- [kAudioChannelLayoutTag_Ogg_6_1](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_ogg_6_1)
- [kAudioChannelLayoutTag_Ogg_7_1](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_ogg_7_1)
- [kAudioFormatAPAC](https://developer.apple.com/documentation/coreaudiotypes/kaudioformatapac)
- [kAudio_BadFilePathError](https://developer.apple.com/documentation/coreaudiotypes/kaudio_badfilepatherror)
- [kAudio_FilePermissionError](https://developer.apple.com/documentation/coreaudiotypes/kaudio_filepermissionerror)
- [kAudio_NoError](https://developer.apple.com/documentation/coreaudiotypes/kaudio_noerror)
- [kAudio_TooManyFilesOpenError](https://developer.apple.com/documentation/coreaudiotypes/kaudio_toomanyfilesopenerror)
:::
