---
route: /documentation/ReplayKit
source_url: https://developer.apple.com/documentation/ReplayKit
source_locale: en-US
section: docc
content_type: symbol
title: ReplayKit
original_title: ReplayKit
source_hash: ae24a16b4409bc67255a2cfc9ce635ac7093d0b2db98569354ad43d0a43c0f67
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:14:55+00:00'
last_translated_at: '2026-03-13T16:45:00+09:00'
---

# ReplayKit

화면의 비디오와 앱 및 마이크의 오디오를 녹화하거나 스트리밍합니다.

## 개요

ReplayKit 프레임워크를 사용하면 사용자가 화면의 비디오와 앱 및 마이크의 오디오를 녹화할 수 있습니다. 그런 다음 이메일, 메시지, 소셜 미디어를 통해 해당 녹화본을 다른 사용자와 공유할 수 있습니다. 콘텐츠를 공유 서비스로 라이브 방송하기 위한 app extension도 만들 수 있습니다. ReplayKit은 [AVPlayer](https://developer.apple.com/documentation/AVFoundation/AVPlayer) 콘텐츠와 호환되지 않습니다.

:::topic-grid
## Replay 공유
- [Recording and Streaming Your macOS App](https://developer.apple.com/documentation/replaykit/recording-and-streaming-your-macos-app): macOS 앱과 게임에 ReplayKit을 추가해 화면 녹화를 공유하거나 앱의 오디오와 비디오를 라이브 방송합니다.
- [RPScreenRecorder](https://developer.apple.com/documentation/replaykit/rpscreenrecorder): 앱의 오디오와 비디오를 녹화하는 기능을 제공하는 공유 recorder 객체입니다.
- [RPPreviewViewController](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller): ReplayKit으로 만든 화면 녹화를 사용자가 미리 보고 편집하는 사용자 인터페이스를 표시하는 객체입니다.
:::

:::topic-grid
## 미디어 클립 처리
- [RPBroadcastController](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller): 방송을 시작하고 제어하는 메서드를 포함하는 객체입니다.
- [RPBroadcastHandler](https://developer.apple.com/documentation/replaykit/rpbroadcasthandler): 방송 앱에 메시지를 보내는 객체입니다.
- [RPBroadcastSampleHandler](https://developer.apple.com/documentation/replaykit/rpbroadcastsamplehandler): ReplayKit에서 전달받은 buffer 객체를 처리하는 객체입니다.
- [RPBroadcastMP4ClipHandler](https://developer.apple.com/documentation/replaykit/rpbroadcastmp4cliphandler): ReplayKit의 MP4 동영상 클립을 처리하는 객체입니다.
:::

:::topic-grid
## 라이브 방송 구현
- [RPBroadcastActivityViewController](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller): 사용자가 방송 서비스를 선택하는 사용자 인터페이스를 표시하는 view controller입니다.
- [RPSystemBroadcastPickerView](https://developer.apple.com/documentation/replaykit/rpsystembroadcastpickerview): 탭하면 방송 picker를 표시하는 방송 버튼을 보여 주는 view입니다.
- [RPBroadcastActivityController](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontroller): macOS 방송 picker를 표시하는 controller 객체입니다.
- [RPBroadcastActivityControllerDelegate](https://developer.apple.com/documentation/replaykit/rpbroadcastactivitycontrollerdelegate): broadcast activity controller의 선택 이벤트에 응답하기 위해 구현하는 메서드를 정의하는 프로토콜입니다.
- [RPBroadcastConfiguration](https://developer.apple.com/documentation/replaykit/rpbroadcastconfiguration): 라이브 방송 중 생성되는 동영상 클립을 구성하는 객체입니다.
:::

:::topic-grid
## 오류
- [RPRecordingErrorCode](https://developer.apple.com/documentation/replaykit/rprecordingerrorcode): ReplayKit 오류 도메인 코드입니다.
- [RPRecordingErrorDomain](https://developer.apple.com/documentation/replaykit/rprecordingerrordomain): ReplayKit 오류 도메인입니다.
- [SCStreamErrorDomain](https://developer.apple.com/documentation/replaykit/scstreamerrordomain)
:::
