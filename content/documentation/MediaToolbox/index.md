---
route: /documentation/MediaToolbox
source_url: https://developer.apple.com/documentation/MediaToolbox
source_locale: en-US
section: docc
content_type: symbol
title: Media Toolbox
original_title: Media Toolbox
source_hash: cbcfd6516064aeb0c8d384f2f7df2036d34c085d1136e2f7b0c77186bdaca36f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:44:05+00:00'
last_translated_at: '2026-03-13T20:45:00+09:00'
---

# Media Toolbox

미디어 포맷 리더 지원을 활성화하고, 오디오 믹스에서 오디오를 탭해 처리합니다.

## 개요

사용자 정의 [MediaExtension](https://developer.apple.com/documentation/MediaExtension) 포맷 리더를 사용할 수 있게 하려면 [MTRegisterProfessionalVideoWorkflowFormatReaders()](https://developer.apple.com/documentation/mediatoolbox/mtregisterprofessionalvideoworkflowformatreaders()) 함수를 호출하십시오.

[AVPlayer](https://developer.apple.com/documentation/AVFoundation/AVPlayer)에서 오디오를 탭하려면 [MTAudioProcessingTap](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtap)을 사용하십시오.

:::topic-grid
## 전문 비디오 워크플로
- [MTRegisterProfessionalVideoWorkflowFormatReaders()](https://developer.apple.com/documentation/mediatoolbox/mtregisterprofessionalvideoworkflowformatreaders()): 전문 비디오 워크플로를 지원하는 미디어 포맷 리더 사용을 활성화합니다.
:::

:::topic-grid
## 오디오 탭
- [MTAudioProcessingTapCreate(_:_:_:_:)](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcreate(_:_:_:_:)): 새 오디오 처리 탭을 생성합니다.
- [MTAudioProcessingTapGetSourceAudio(_:_:_:_:_:_:)](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapgetsourceaudio(_:_:_:_:_:_:)): 오디오 처리 탭의 소스 오디오를 가져옵니다.
- [MTAudioProcessingTapGetStorage(_:)](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapgetstorage(_:)): 오디오 처리 탭에 대한 사용자 정의 저장소 포인터를 가져옵니다.
- [MTAudioProcessingTapGetTypeID()](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapgettypeid()): 이 오디오 처리 탭의 타입 식별자를 가져옵니다.
- [MTAudioProcessingTapFlags](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapflags): 오디오를 어디에서 탭할지 나타내는 플래그입니다.
- [MTAudioProcessingTap](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtap): 오디오 처리 탭 객체입니다.
:::

:::topic-grid
## 유틸리티
- [MTCopyLocalizedNameForMediaType(_:)](https://developer.apple.com/documentation/mediatoolbox/mtcopylocalizednameformediatype(_:)): 지정한 미디어 타입의 지역화된 이름을 반환합니다.
- [MTCopyLocalizedNameForMediaSubType(_:_:)](https://developer.apple.com/documentation/mediatoolbox/mtcopylocalizednameformediasubtype(_:_:)): 지정한 미디어 타입과 subtype의 지역화된 이름을 반환합니다.
:::

:::topic-grid
## 열거형
- [Anonymous Enumerations](https://developer.apple.com/documentation/mediatoolbox/anonymous-enums)
:::
