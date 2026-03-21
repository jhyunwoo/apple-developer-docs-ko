---
route: /documentation/ScreenCaptureKit
source_url: https://developer.apple.com/documentation/ScreenCaptureKit
source_locale: en-US
section: docc
content_type: symbol
title: ScreenCaptureKit
original_title: ScreenCaptureKit
source_hash: 28f5320bb23fa526409eabb7a411c5d8af363bdd89083b5e4d1b489c8cefe77e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:25:16+00:00'
last_translated_at: '2026-03-13T23:12:00+09:00'
---

# ScreenCaptureKit

화면 콘텐츠를 필터링하고 선택해 앱으로 스트리밍합니다.

## 개요

ScreenCaptureKit 프레임워크를 사용하면 Mac 앱에 화면 및 오디오 콘텐츠의 고성능 프레임 캡처 지원을 추가할 수 있습니다. 이 프레임워크는 캡처하려는 콘텐츠만 선택하고 스트리밍할 수 있도록 세밀한 제어를 제공합니다. 스트림이 새 비디오 프레임과 오디오 샘플을 캡처하면, 미디어 데이터와 관련 메타데이터를 담은 [CMSampleBuffer](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) 객체로 이를 앱에 전달합니다. ScreenCaptureKit은 스트리밍 선택과 관리를 위한 macOS 통합 피커인 [SCContentSharingPicker](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker)도 제공합니다.

:::note Related Sessions from WWDC22 and WWDC23
세션 10156: [Meet ScreenCaptureKit](https://developer.apple.com/wwdc22/10156)

세션 10155: [Take ScreenCaptureKit to the next level](https://developer.apple.com/wwdc22/10155)

세션 10136: [What’s new in ScreenCaptureKit](https://developer.apple.com/videos/play/wwdc2023/10136/)
:::

:::topic-grid
## 핵심 항목
- [ScreenCaptureKit updates](https://developer.apple.com/documentation/Updates/ScreenCaptureKit): ScreenCaptureKit의 중요한 변경 사항을 알아봅니다.
- [Persistent Content Capture](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.persistent-content-capture): VNC(Virtual Network Computing) 앱이 화면 캡처에 지속적으로 접근해야 하는지를 나타내는 Boolean 값입니다.
- [Capturing screen content in macOS](https://developer.apple.com/documentation/screencapturekit/capturing-screen-content-in-macos): 앱에 화면 캡처를 채택해 디스플레이, 앱, 윈도우 같은 데스크톱 콘텐츠를 스트리밍합니다.
:::

:::topic-grid
## 공유 가능한 콘텐츠
- [SCShareableContent](https://developer.apple.com/documentation/screencapturekit/scshareablecontent): 앱이 캡처할 수 있는 디스플레이, 앱, 윈도우 집합을 나타내는 인스턴스입니다.
- [SCShareableContentInfo](https://developer.apple.com/documentation/screencapturekit/scshareablecontentinfo): 지정된 스트림의 콘텐츠에 대한 정보를 제공하는 인스턴스입니다.
- [SCShareableContentStyle](https://developer.apple.com/documentation/screencapturekit/scshareablecontentstyle): 스트림에 표시되는 콘텐츠의 스타일입니다.
- [SCDisplay](https://developer.apple.com/documentation/screencapturekit/scdisplay): 디스플레이 장치를 나타내는 인스턴스입니다.
- [SCRunningApplication](https://developer.apple.com/documentation/screencapturekit/scrunningapplication): 기기에서 실행 중인 앱을 나타내는 인스턴스입니다.
- [SCWindow](https://developer.apple.com/documentation/screencapturekit/scwindow): 화면에 표시된 윈도우를 나타내는 인스턴스입니다.
:::

:::topic-grid
## 콘텐츠 캡처
- [SCStream](https://developer.apple.com/documentation/screencapturekit/scstream): 공유 가능한 콘텐츠의 스트림을 나타내는 인스턴스입니다.
- [SCStreamConfiguration](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration): 스트림의 출력 구성을 제공하는 인스턴스입니다.
- [SCContentFilter](https://developer.apple.com/documentation/screencapturekit/sccontentfilter): 스트림이 캡처하는 콘텐츠를 필터링하는 인스턴스입니다.
- [SCStreamDelegate](https://developer.apple.com/documentation/screencapturekit/scstreamdelegate): 앱이 구현해 스트림 이벤트에 응답하는 delegate 프로토콜입니다.
- [SCScreenshotManager](https://developer.apple.com/documentation/screencapturekit/scscreenshotmanager): 스트림에서 단일 프레임을 캡처하기 위한 인스턴스입니다.
- [SCScreenshotConfiguration](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration): 출력 너비, 높이, 이미지 품질 사양 같은 스크린샷 속성을 담는 객체입니다.
- [SCScreenshotOutput](https://developer.apple.com/documentation/screencapturekit/scscreenshotoutput): 클라이언트가 요청한 모든 이미지를 담는 객체입니다.
:::

:::topic-grid
## 출력 처리
- [SCStreamOutput](https://developer.apple.com/documentation/screencapturekit/scstreamoutput): 앱이 구현해 캡처 스트림 출력 이벤트를 수신하는 delegate 프로토콜입니다.
- [SCStreamOutputType](https://developer.apple.com/documentation/screencapturekit/scstreamoutputtype): 스트림 프레임의 출력 타입을 나타내는 상수입니다.
- [SCStreamFrameInfo](https://developer.apple.com/documentation/screencapturekit/scstreamframeinfo): 스트림 프레임의 메타데이터 키를 정의하는 인스턴스입니다.
- [SCFrameStatus](https://developer.apple.com/documentation/screencapturekit/scframestatus): 스트림에서 받은 프레임의 상태 값입니다.
:::

:::topic-grid
## 시스템 콘텐츠 공유 피커
- [SCContentSharingPicker](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker): 프레임 캡처 스트림을 관리하기 위해 운영체제가 제공하는 피커 인스턴스입니다.
- [SCContentSharingPickerConfiguration](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerconfiguration-swift.struct): 시스템 콘텐츠 공유 피커를 구성하기 위한 인스턴스입니다.
- [SCContentSharingPickerMode](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickermode): 운영체제가 제공하는 피커에서 스트리밍 콘텐츠를 선택할 때 사용할 수 있는 모드입니다.
- [SCContentSharingPickerObserver](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerobserver): 운영체제의 콘텐츠 피커로부터 메시지를 수신하기 위해 앱이 구현하는 observer 프로토콜입니다.
:::

:::topic-grid
## 스트림 오류
- [SCStreamErrorDomain](https://developer.apple.com/documentation/screencapturekit/scstreamerrordomain): 오류 도메인의 문자열 표현입니다.
- [SCStreamError](https://developer.apple.com/documentation/screencapturekit/scstreamerror): ScreenCaptureKit 프레임워크 오류를 나타내는 인스턴스입니다.
:::
