---
route: /documentation/AVKit
source_url: https://developer.apple.com/documentation/AVKit
source_locale: en-US
section: docc
content_type: symbol
title: AVKit
original_title: AVKit
source_hash: 954e8e4f5b4045de1ad8b9448e7b1332e1590982e9aefb64c4f46afc935380d6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:21:33+00:00'
last_translated_at: '2026-03-13T23:21:47+09:00'
---

# AVKit

전송 제어, 챕터 탐색, picture in picture 지원, 자막 및 closed caption 표시를 포함한 미디어 재생용 사용자 인터페이스를 만듭니다.

## 개요

AVKit은 Apple 플랫폼에서 오디오 및 비디오 재생, 캡처, picture in picture, 경로 선택, 몰입형 미디어 경험을 위한 시스템 스타일 인터페이스를 제공합니다. `AVPlayerViewController`, `AVPlayerView`, `VideoPlayer` 같은 타입을 사용해 표준 재생 인터페이스를 빠르게 도입할 수 있고, tvOS와 visionOS에서는 내비게이션 마커, interstitial 콘텐츠, multiview, SharePlay 환경 동기화 같은 기능도 지원합니다.

:::topic-grid
## iOS 재생 및 캡처
- [Playing video content in a standard user interface](https://developer.apple.com/documentation/avkit/playing-video-content-in-a-standard-user-interface): player view controller를 사용해 전체 화면, 인라인, 또는 떠 있는 PiP 창에서 미디어를 재생합니다.
- [AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller): player의 콘텐츠를 표시하고 재생 제어를 위한 기본 사용자 인터페이스를 제공하는 view controller입니다.
- [AVPlayerViewControllerDelegate](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate): player view controller 이벤트에 응답하는 메서드를 정의하는 protocol입니다.
- [AVCaptureEventInteraction](https://developer.apple.com/documentation/avkit/avcaptureeventinteraction): 시스템 하드웨어 버튼에서 발생하는 캡처 이벤트에 응답할 handler를 등록하는 객체입니다.
- [AVCaptureEvent](https://developer.apple.com/documentation/avkit/avcaptureevent): 시스템 하드웨어 버튼과의 사용자 상호 작용을 설명하는 객체입니다.
- [AVCaptureEventSound](https://developer.apple.com/documentation/avkit/avcaptureeventsound): 캡처 이벤트용 사운드 객체입니다.
- [AVInputPickerInteraction](https://developer.apple.com/documentation/avkit/avinputpickerinteraction): 입력 선택기를 표시할 때 사용합니다.
:::

:::topic-grid
## tvOS 재생 및 캡처
- [Customizing the tvOS Playback Experience](https://developer.apple.com/documentation/avkit/customizing-the-tvos-playback-experience): 새롭게 디자인된 tvOS player UI의 최신 기능을 채택해 콘텐츠 시청 흐름을 간소화합니다.
- [Presenting Navigation Markers](https://developer.apple.com/documentation/avkit/presenting-navigation-markers): Chapters 패널에 navigation marker를 표시해 사용자가 콘텐츠를 빠르게 탐색할 수 있도록 합니다.
- [Working with Interstitial Content](https://developer.apple.com/documentation/avkit/working-with-interstitial-content): HTTP Live Streaming 지원을 사용해 메인 미디어와 함께 추가 콘텐츠를 표시합니다.
- [Presenting Content Proposals in tvOS](https://developer.apple.com/documentation/avkit/presenting-content-proposals-in-tvos): 현재 재생 중인 미디어가 끝날 때 다음에 볼 미디어 항목의 미리보기를 표시합니다.
- [Working with Overlays and Parental Controls in tvOS](https://developer.apple.com/documentation/avkit/working-with-overlays-and-parental-controls-in-tvos): player view controller를 사용해 대화형 overlay, parental control, 라이브스트림 채널 전환 기능을 추가합니다.
- [Supporting Continuity Camera in your tvOS app](https://developer.apple.com/documentation/avkit/supporting-continuity-camera-in-your-tvos-app): iPhone 또는 iPad를 continuity device로 연결해 Apple TV 앱에서 고품질 사진, 비디오, 오디오를 캡처합니다.
- [AVInterstitialTimeRange](https://developer.apple.com/documentation/avkit/avinterstitialtimerange): 광고나 법적 고지처럼 interstitial 지정이 있는 콘텐츠의 시청각 프레젠테이션 시간 범위입니다.
- [AVNavigationMarkersGroup](https://developer.apple.com/documentation/avkit/avnavigationmarkersgroup): 시청각 프레젠테이션 재생 탐색용 marker 집합입니다.
- [AVContentProposalViewController](https://developer.apple.com/documentation/avkit/avcontentproposalviewcontroller): 다음에 볼 콘텐츠를 제안하는 view controller입니다.
- [AVDisplayManager](https://developer.apple.com/documentation/avkit/avdisplaymanager): TV가 비디오의 원래 모드에 맞춰 모드를 전환할지 제어하는 tvOS 관리 객체입니다.
- [AVContinuityDevicePickerViewController](https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontroller): 사용자가 continuity device를 선택하고 시스템에 연결할 수 있도록 하는 인터페이스를 제공하는 view controller입니다.
- [AVContinuityDevicePickerViewControllerDelegate](https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontrollerdelegate): continuity device picker view controller의 이벤트에 응답하는 인터페이스입니다.
:::

:::topic-grid
## visionOS 재생
- [Playing immersive media with AVKit](https://developer.apple.com/documentation/avkit/playing-immersive-media-with-avkit): 몰입형 비디오 시청 경험을 제공하기 위해 시스템 재생 인터페이스를 채택합니다.
- [Creating a multiview video playback experience in visionOS](https://developer.apple.com/documentation/avkit/creating-a-multiview-video-playback-experience-in-visionos): 여러 비디오를 동시에 재생하고 서로 다른 경험 유형 간 전환을 자연스럽게 처리하는 인터페이스를 구축합니다.
- [Adopting the system player interface in visionOS](https://developer.apple.com/documentation/avkit/adopting-the-system-player-interface-in-visionos): 3D 비디오 콘텐츠를 위한 최적화된 시청 경험을 제공합니다.
- [Trimming and exporting media in visionOS](https://developer.apple.com/documentation/avkit/trimming-and-exporting-media-in-visionos): 현재 재생 중인 미디어의 타임라인을 편집할 수 있도록 앱에 표준 제어를 표시합니다.
- [AVExperienceController](https://developer.apple.com/documentation/avkit/avexperiencecontroller): 비디오 경험을 제어하는 객체입니다.
- [AVMultiviewManager](https://developer.apple.com/documentation/avkit/avmultiviewmanager): 여러 비디오를 동시에 보는 경험을 관리하는 객체입니다.
- [AVGroupExperienceCoordinator](https://developer.apple.com/documentation/avkit/avgroupexperiencecoordinator): SharePlay 세션 참가자 간 시청 환경 상태를 동기화하는 객체입니다.
:::

:::topic-grid
## macOS 재생 및 캡처
- [Implementing Trimming in a macOS Player](https://developer.apple.com/documentation/avkit/implementing-trimming-in-a-macos-player): macOS 앱에 QuickTime 스타일 미디어 트리밍 경험을 제공합니다.
- [AVPlayerView](https://developer.apple.com/documentation/avkit/avplayerview): player의 콘텐츠를 표시하고 재생 제어를 위한 기본 사용자 인터페이스를 제공하는 view입니다.
- [AVCaptureView](https://developer.apple.com/documentation/avkit/avcaptureview): 미디어 데이터 캡처를 위한 표준 사용자 인터페이스 제어를 표시하는 view입니다.
:::

:::topic-grid
## 멀티플랫폼 재생 및 캡처
- [VideoPlayer](https://developer.apple.com/documentation/avkit/videoplayer): player의 콘텐츠와 재생 제어용 기본 사용자 인터페이스를 표시하는 view입니다.
:::

:::topic-grid
## Picture in Picture
- [Adopting Picture in Picture Playback in tvOS](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-playback-in-tvos): tvOS의 picture in picture 재생으로 비디오 앱에 고급 멀티태스킹 기능을 추가합니다.
- [Adopting Picture in Picture in a Standard Player](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-in-a-standard-player): player view controller를 사용해 앱에 PiP 재생을 추가합니다.
- [Adopting Picture in Picture in a Custom Player](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-in-a-custom-player): 사용자 정의 player UI에 PiP 재생을 호출하는 제어를 추가합니다.
- [Adopting Picture in Picture for video calls](https://developer.apple.com/documentation/avkit/adopting-picture-in-picture-for-video-calls): PiP를 사용해 영상 통화 앱에 멀티태스킹 기능을 추가합니다.
- [Accessing the camera while multitasking on iPad](https://developer.apple.com/documentation/avkit/accessing-the-camera-while-multitasking-on-ipad): Split View, Slide Over, PiP, Stage Manager 모드에서 카메라를 동작시킵니다.
- [AVPictureInPictureController](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller): 떠 있고 크기 조절이 가능한 창에서 사용자 주도 PiP 비디오 재생에 응답하는 controller입니다.
:::

:::topic-grid
## 재생 경로 선택
- [AVRoutePickerView](https://developer.apple.com/documentation/avkit/avroutepickerview): 근처 미디어 수신기 목록을 표시하는 view입니다.
:::

:::topic-grid
## 메타데이터
- [AVKit Metadata Identifiers](https://developer.apple.com/documentation/avkit/avkit-metadata-identifiers): asset이 담고 있는 추가 메타데이터입니다.
:::

:::topic-grid
## 오류
- [AVKitErrorDomain](https://developer.apple.com/documentation/avkit/avkiterrordomain): 프레임워크가 생성하는 오류의 도메인입니다.
- [AVKitError](https://developer.apple.com/documentation/avkit/avkiterror-swift.struct): 프레임워크 오류를 표현하는 구조체입니다.
- [AVKitError.Code](https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/code): 프레임워크 오류 코드를 식별하는 상수입니다.
:::

:::topic-grid
## 매크로
- [Macros](https://developer.apple.com/documentation/avkit/avkit-macros)
:::

:::topic-grid
## 클래스
- [AVLegibleMediaOptionsMenuController](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller)
:::

:::topic-grid
## 구조체
- [AVLegibleMediaOptionsMenuState](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenustate)
:::
