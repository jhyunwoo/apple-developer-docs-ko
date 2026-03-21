---
route: /documentation/ImmersiveMediaSupport
source_url: https://developer.apple.com/documentation/ImmersiveMediaSupport
source_locale: en-US
section: docc
content_type: symbol
title: Immersive Media Support
original_title: Immersive Media Support
source_hash: c8188bd295dbe7c1860c99c411758c07c8634ade1736e35dc20479c8aee33541
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:41:40+00:00'
last_translated_at: '2026-03-13T23:51:00+09:00'
---

# Immersive Media Support

핵심 Apple Immersive Video 메타데이터를 읽고 씁니다.

## 개요

Immersive Media Support를 사용하면 Apple Immersive Video(AIV)를 처리하기 위한 사용자 정의 워크플로를 만들 수 있습니다. 이를 사용해 AIV 전용 메타데이터를 읽고 쓸 수 있으며, 편집 워크플로에서 콘텐츠 미리보기를 활성화할 수 있습니다.

:::topic-grid
## 핵심 항목
- [Authoring Apple Immersive Video](https://developer.apple.com/documentation/immersivemediasupport/authoring-apple-immersive-video): 전달을 위해 몰입형 비디오 콘텐츠를 준비하고 패키징합니다.
:::

:::topic-grid
## 카메라 메타데이터
- [VenueDescriptor](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor): Apple Immersive Media Venue Descriptor는 모든 Apple Immersive Video에 필요한 정적 메타데이터 모음입니다.
- [ImmersiveCamera](https://developer.apple.com/documentation/immersivemediasupport/immersivecamera): 몰입형 미디어 카메라가 비디오 프레임을 처리하고 렌더링하는 데 필요한 정보를 담는 구조체입니다.
- [ImmersiveCameraCalibration](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration): 몰입형 미디어 카메라 보정 데이터를 나타내는 구조체입니다.
- [ImmersiveCameraMask](https://developer.apple.com/documentation/immersivemediasupport/immersivecameramask): 카메라 마스크 타입 정보와 관련 마스크 이름을 담는 구조체입니다.
- [ImmersiveDynamicMask](https://developer.apple.com/documentation/immersivemediasupport/immersivedynamicmask): 로드 시점에 몰입형 미디어 마스크를 동적으로 생성하는 데 필요한 정보를 담는 타입입니다.
:::

:::topic-grid
## 프레젠테이션 명령
- [PresentationCommand](https://developer.apple.com/documentation/immersivemediasupport/presentationcommand): 프레젠테이션 명령의 인터페이스를 정의하는 속성 집합입니다.
- [FadeCommand](https://developer.apple.com/documentation/immersivemediasupport/fadecommand): 몰입형 미디어 재생 중 색상 페이딩을 위한 명령 타입입니다.
- [FadeEnvironmentCommand](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand): 몰입형 미디어 재생 중 환경 배경의 불투명도를 페이드하는 명령 타입입니다.
- [SetCameraCommand](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand): 재생 중 몰입형 카메라 전환을 위한 명령 타입입니다.
- [ShotFlopCommand](https://developer.apple.com/documentation/immersivemediasupport/shotflopcommand): 명령이 지속되는 동안 재생 중 비디오 프레임을 수평으로 뒤집는 명령 타입입니다.
- [PresentationDescriptor](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptor): 재생 중 또는 몰입형 비디오 파일의 메타데이터 트랙 출력 시 사용하는 동적 메타데이터를 나타내는 구조체입니다.
- [PresentationDescriptorReader](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader): 몰입형 프레젠테이션 명령을 이해하고 처리하는 데 필요한 기능을 제공하는 객체입니다.
:::

:::topic-grid
## 파라메트릭 몰입형 지원
- [ParametricImmersiveAssetInfo](https://developer.apple.com/documentation/immersivemediasupport/parametricimmersiveassetinfo): 원본 wide field of view 비디오 asset을 parametric immersive asset으로 변환하는 데 도움을 주는 객체입니다.
:::

:::topic-grid
## 몰입형 비디오 렌더링 지원
- [ImmersiveCameraViewModel](https://developer.apple.com/documentation/immersivemediasupport/immersivecameraviewmodel): 몰입형 카메라 뷰를 렌더링하는 데 필요한 모든 리소스를 담는 view model입니다.
- [ImmersiveVideoMask](https://developer.apple.com/documentation/immersivemediasupport/immersivevideomask): 비디오 렌더링 중 mesh 가장자리를 부드럽게 하기 위해 사용하는 비디오 마스크입니다.
:::

:::topic-grid
## 미리보기
- [ImmersiveMediaPreviewMessagingProtocol](https://developer.apple.com/documentation/immersivemediasupport/immersivemediapreviewmessagingprotocol): 원격 미리보기 송신자와 수신자가 통신할 때 사용하는 메시징 프로토콜을 나타내는 객체입니다.
:::

:::topic-grid
## 검증
- [AIVUValidator](https://developer.apple.com/documentation/immersivemediasupport/aivuvalidator): 기존 AIVU 파일이 AIV의 최소 요구 사항을 충족하는지 검증하는 타입입니다.
:::

:::topic-grid
## 클래스
- [ImmersiveCameraMeshCalibration](https://developer.apple.com/documentation/immersivemediasupport/immersivecamerameshcalibration): USDZ 데이터를 기반으로 한 보정 mesh geometry입니다.
- [ImmersiveImageMask](https://developer.apple.com/documentation/immersivemediasupport/immersiveimagemask): 이미지 데이터 또는 파일에서 몰입형 미디어 마스크를 로드하는 데 필요한 모든 정보를 담는 객체입니다.
- [ImmersiveMediaRemotePreviewReceiver](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewreceiver): 몰입형 미디어 원격 미리보기 sender 객체가 보낸 명령과 데이터를 앱이 수신하도록 도와주는 observable 객체입니다.
- [ImmersiveMediaRemotePreviewSender](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender): 연결된 모든 receiver 앱에 필요한 데이터를 보내 몰입형 미디어 재생의 완전한 미리보기를 가능하게 하도록 돕는 observable 객체입니다.
:::

:::topic-grid
## 구조체
- [ImmersiveCameraLensDefinition](https://developer.apple.com/documentation/immersivemediasupport/immersivecameralensdefinition): 카메라 보정 타입 인스턴스를 생성하기 위한 ILPD 렌즈 구성 매개변수를 담는 타입입니다.
- [ImmersiveVideoFrame](https://developer.apple.com/documentation/immersivemediasupport/immersivevideoframe): 몰입형 비디오 프레임을 나타내는 타입입니다. 몰입형 비디오 프레임에는 다음이 포함됩니다. - layout(SideBySide, OverUnder, Separate, Mono) - presentationTime: 프레임 표시 시간 - pixelBuffers: 프레임을 나타내는 하나 이상의 이미지 배열.
:::
