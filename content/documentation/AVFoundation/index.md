---
route: /documentation/AVFoundation
source_url: https://developer.apple.com/documentation/AVFoundation
source_locale: en-US
section: docc
content_type: symbol
title: AVFoundation
original_title: AVFoundation
source_hash: 865b8934699cfb4f800270d3ec719f64c70a491113859b4b862d0ec424a3b2f8
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:54:06+00:00'
last_translated_at: '2026-03-14T02:30:00+09:00'
---

# AVFoundation

오디오비주얼 asset로 작업하고, 기기 카메라를 제어하고, 오디오를 처리하고, 시스템 오디오 상호 작용을 구성합니다.

## 개요

AVFoundation은 Apple 플랫폼에서 오디오비주얼 미디어를 검사하고, 재생하고, 캡처하고, 처리하는 폭넓은 작업을 포괄하는 여러 주요 기술 영역을 결합합니다.

:::topic-grid
## 기초
- [AVFoundation updates](https://developer.apple.com/documentation/Updates/AVFoundation): AVFoundation의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 공통
- [Media assets](https://developer.apple.com/documentation/avfoundation/media-assets): 파일과 stream에서 media asset을 로드해 속성, track, 포함된 metadata를 검사합니다.
- [Media reading and writing](https://developer.apple.com/documentation/avfoundation/media-reading-and-writing): 비디오에서 이미지를 읽고, 대체 형식으로 내보내고, 미디어 데이터의 sample 수준 읽기 및 쓰기를 수행합니다.
- [Media types and utilities](https://developer.apple.com/documentation/avfoundation/media-types-and-utilities): AVFoundation이 지원하는 콘텐츠 유형과 파일 형식을 식별합니다.
- [Video settings](https://developer.apple.com/documentation/avfoundation/video-settings): 표준 key와 value 상수를 사용해 비디오 처리 설정을 구성합니다.
- [Audio settings](https://developer.apple.com/documentation/avfoundation/audio-settings): 표준 key와 value 상수를 사용해 오디오 처리 설정을 구성합니다.
:::

:::topic-grid
## 재생
- [Media playback](https://developer.apple.com/documentation/avfoundation/media-playback): 인터페이스에서 해당 콘텐츠를 어떻게 표시하는지와 무관하게 media asset과 interstitial content의 재생을 관리합니다.
- [Offline playback and storage](https://developer.apple.com/documentation/avfoundation/offline-playback-and-storage): stream된 콘텐츠를 디스크에 다운로드해 오프라인 재생을 가능하게 하고, 다운로드된 asset을 자동으로 제거하는 정책을 정의합니다.
- [Streaming and AirPlay](https://developer.apple.com/documentation/avfoundation/streaming-and-airplay): AirPlay를 사용해 다른 기기로 무선 스트리밍하고, FairPlay로 보호된 asset과 관련된 요청을 처리합니다.
- [Sample buffer playback](https://developer.apple.com/documentation/avfoundation/sample-buffer-playback): sample buffer stream의 재생과 타이밍 동기화를 위한 사용자 정의 controller를 생성합니다.
:::

:::topic-grid
## 캡처
- [Capture setup](https://developer.apple.com/documentation/avfoundation/capture-setup): 미디어 캡처를 위해 내장 카메라와 마이크, 외부 캡처 장치를 구성합니다.
- [Photo capture](https://developer.apple.com/documentation/avfoundation/photo-capture): 고품질 정지 이미지, Live Photo, 관련 photo 데이터를 캡처합니다.
- [Audio and video capture](https://developer.apple.com/documentation/avfoundation/audio-and-video-capture): 오디오와 비디오를 직접 media file로 캡처하거나, media sample buffer에 직접 접근할 수 있도록 media stream을 캡처합니다.
- [Additional data capture](https://developer.apple.com/documentation/avfoundation/additional-data-capture): depth와 metadata를 포함한 추가 데이터를 캡처하고, 여러 output의 캡처를 동기화합니다.
:::

:::topic-grid
## 편집
- [Composite assets](https://developer.apple.com/documentation/avfoundation/composite-assets): 여러 asset의 track과 track segment를 결합해 재생하거나 처리할 수 있는 composite asset을 만듭니다.
- [QuickTime movies](https://developer.apple.com/documentation/avfoundation/quicktime-movies): QuickTime movie 파일의 콘텐츠에 접근하고 media track의 sample 수준 편집을 수행합니다.
- [Video effects](https://developer.apple.com/documentation/avfoundation/video-effects): 표준 비디오 전환 효과를 정의하고, layer animation을 media timing과 동기화하며, 사용자 정의 video compositor를 만듭니다.
- [Audio mixing](https://developer.apple.com/documentation/avfoundation/audio-mixing): asset의 전체 duration 동안 여러 오디오 track의 오디오 레벨을 어떻게 섞을지 정의합니다.
:::

:::topic-grid
## 오디오
- [Audio playback, recording, and processing](https://developer.apple.com/documentation/avfoundation/audio-playback-recording-and-processing): 오디오를 재생, 녹음, 처리하고 앱의 시스템 오디오 동작을 구성합니다.
- [Speech synthesis](https://developer.apple.com/documentation/avfoundation/speech-synthesis): 음성이 텍스트 문자열을 읽도록 구성합니다.
:::

:::topic-grid
## 오류
- [AVFoundationErrorDomain](https://developer.apple.com/documentation/avfoundation/avfoundationerrordomain): AVFoundation 오류의 오류 도메인입니다.
- [AVError](https://developer.apple.com/documentation/avfoundation/averror-swift.struct): 프레임워크 작업이 생성할 수 있는 오류를 정의하는 구조체입니다.
:::

:::topic-grid
## 매크로
- [Macros](https://developer.apple.com/documentation/avfoundation/avfoundation-macros)
:::

:::topic-grid
## 변수
- [AVPlayerInterstitialEventMonitorScheduleRequestErrorKey](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitorschedulerequesterrorkey): `AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification`의 `userInfo` dictionary key입니다. 값은 NSError입니다. 요청이 성공하면 존재하지 않습니다.
- [AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitorschedulerequestidentifierkey): `AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification`의 `userInfo` dictionary key입니다. 값은 NSString입니다.
- [AVPlayerInterstitialEventMonitorScheduleRequestResponseKey](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitorschedulerequestresponsekey): `AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification`의 `userInfo` dictionary key입니다. 값은 NSData입니다. 요청이 실패하면 존재하지 않습니다.
:::
