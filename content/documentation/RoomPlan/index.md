---
route: /documentation/RoomPlan
source_url: https://developer.apple.com/documentation/RoomPlan
source_locale: en-US
section: docc
content_type: symbol
title: RoomPlan
original_title: RoomPlan
source_hash: bad2dad3fae9785ead326447c1384a30528daa22c3701a218c9520e7e0064df6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:19+00:00'
last_translated_at: '2026-03-13T10:02:00+00:00'
---

# RoomPlan

기기의 카메라를 사용해 실제 환경을 스캔하도록 사용자를 대화형으로 안내하여 방의 3D 모델을 생성합니다.

## 개요

RoomPlan을 사용해 실내 방의 3D 모델을 생성합니다. 이 프레임워크는 기기의 센서, 학습된 ML 모델, RealityKit의 렌더링 기능을 사용해 실내 방의 물리적 주변 환경을 캡처합니다. 예를 들어 프레임워크는 기기의 카메라 피드와 LiDAR 판독값을 조사해 벽, 창문, 개구부, 문을 식별합니다. RoomPlan은 벽난로, 침대, 냉장고 같은 방의 특징, 가구, 가전도 인식하고 그 정보를 앱에 제공합니다.

캡처를 시작하면 앱은 사용자가 AR로 자신의 방을 보는 [RoomCaptureView](https://developer.apple.com/documentation/roomplan/roomcaptureview)를 표시합니다. 사용자가 방 안을 움직이는 동안 이 뷰는 가상 신호를 표시합니다.

- 실시간 그래픽 오버레이가 방의 물리적 구조 위에 표시되어 스캔 진행 상황을 전달합니다.
- 캡처를 완료하려면 특정한 기기 움직임이나 시점이 필요할 경우, UI가 기기를 어떻게 위치시켜야 하는지 설명하는 안내를 표시합니다.

![세로 모드로 iPhone을 들고 있는 손과 주방을 보여 주는 일러스트입니다. 기기 화면에는 창문과 싱크대 같은 물리적 구조 주위에 강조 표시가 있는 주방 카메라 피드가 보입니다. 화면 상단 배너에는 Move device to start라고 적혀 있고, 오른쪽에는 Instructional text라는 callout이 있습니다. 또 다른 callout은 Structural highlights라고 표시되며 창문 주위의 강조 표시를 가리킵니다.](https://developer.apple.com)

앱이 현재 스캔이 완료되었다고 판단하면, 사용자가 승인할 수 있도록 스캔된 방의 축소 버전을 표시합니다.

대신 앱이 [RoomCaptureSession](https://developer.apple.com/documentation/roomplan/roomcapturesession) 스캔 세션 객체를 직접 만들고 사용하여 스캔 과정 동안 사용자 정의 그래픽을 표시할 수도 있습니다.

### 캡처 결과 접근하기

이 프레임워크는 스캔 결과를 *parametric* 데이터로 출력하므로, 앱이 스캔한 방의 개별 구성 요소를 쉽게 수정할 수 있습니다. RoomPlan은 또한 여러 가지 Universal Scene Description(USD) 형식으로 결과를 제공합니다. 이러한 자산을 사용하면 앱은 다음과 같은 사용자 정의 기능을 구현할 수 있습니다.

- 방의 특정 영역 크기를 추정합니다.
- 카탈로그에 있는 가상 가구를 다양한 스타일과 위치로 미리 봅니다.
- 스캔한 방이나 구조물의 버전을 3D 게임에 통합합니다.

![스캔된 방과 그 데이터 표현을 보여 주는 일러스트입니다. 왼쪽에는 스캔된 방의 축소된 3D 버전이 있고, 오른쪽으로 향하는 세 개의 화살표가 있습니다. 위 화살표는 집 아이콘과 바닥 평면도 2D 이미지 네 개를 가리키며, 평면도에는 물체를 측정하는 자가 있습니다. 가운데 화살표는 장바구니 아이콘과 세로 모드의 iPhone을 가리키며, 화면에는 테이블, 램프, 의자가 있는 가구 카탈로그가 보입니다. 그 옆에는 카탈로그의 가상 테이블이 강조된 스캔 방의 축소 3D 버전이 있습니다. 아래 화살표는 게임 컨트롤러 아이콘과 가로 모드 iPhone을 가리키며, 화면에는 스캔된 방의 3D 게임 버전이 표시됩니다.](https://developer.apple.com)

### Mac Catalyst로 macOS에서 스캔 결과 처리하기

Mac Catalyst로 빌드한 Mac 앱은 [CapturedRoom](https://developer.apple.com/documentation/roomplan/capturedroom)과 [CapturedStructure](https://developer.apple.com/documentation/roomplan/capturedstructure)에 접근할 수 있고, 인코딩, 디코딩, 내보내기를 수행할 수 있습니다. 환경 스캔은 iOS 및 iPadOS 기기에서 증강 현실을 지원하는 카메라, LiDAR, 기타 센서에 의존합니다. 하지만 Mac Catalyst로 빌드한 macOS 앱은 그런 기기에서 수행한 방 캡처 세션 결과를 처리할 수 있습니다. RoomPlan은 Mac Catalyst로 빌드한 macOS 앱에서 캡처 세션 관련 호출을 모두 무시합니다.

:::topic-grid
## 필수 항목
- [AR 경험을 통해 사용자를 안내하여 실내 방의 3D 모델 만들기](https://developer.apple.com/documentation/roomplan/create-a-3d-model-of-an-interior-room-by-guiding-the-user-through-an-ar-experience): 프레임워크가 제공하는 뷰를 사용해 물리적 구조를 강조 표시하고, 사용자가 자신의 실제 환경 형태를 스캔하도록 안내하는 텍스트를 표시합니다.
:::

:::topic-grid
## 사용자 인터페이스
- [RoomCaptureView](https://developer.apple.com/documentation/roomplan/roomcaptureview): 사용자가 기기의 카메라로 방을 스캔할 수 있게 하는 뷰입니다.
- [RoomCaptureViewDelegate](https://developer.apple.com/documentation/roomplan/roomcaptureviewdelegate): 스캔 결과를 후처리하기 위한 명세입니다.
:::

:::topic-grid
## 스캔 프로토콜
- [RoomCaptureSession](https://developer.apple.com/documentation/roomplan/roomcapturesession): 방 스캔 프로세스를 관리하는 객체입니다.
- [RoomCaptureSessionDelegate](https://developer.apple.com/documentation/roomplan/roomcapturesessiondelegate): 방 스캔 프로세스의 중요한 이벤트를 정의하는 명세입니다.
:::

:::topic-grid
## 캡처된 데이터
- [여러 스캔을 하나의 구조로 병합하기](https://developer.apple.com/documentation/roomplan/merging-multiple-scans-into-a-single-structure): 같은 물리적 주변에서 캡처한 여러 방으로 구성된 3D 모델을 내보냅니다.
- [하나의 구조물에 있는 여러 방 스캔하기](https://developer.apple.com/documentation/roomplan/scanning-the-rooms-of-a-single-structure): 사람들이 여러 방이 있는 건물을 스캔할 수 있게 하는 AR 경험을 만듭니다.
- [CapturedRoom](https://developer.apple.com/documentation/roomplan/capturedroom): 스캔된 방의 핵심 세부 정보를 제공하는 구조체입니다.
- [CapturedStructure](https://developer.apple.com/documentation/roomplan/capturedstructure): 여러 캡처 세션 병합 결과를 담는 객체입니다.
- [CapturedRoomData](https://developer.apple.com/documentation/roomplan/capturedroomdata): 스캔의 원시 결과를 담는 opaque 객체입니다.
- [Captured Object Attributes](https://developer.apple.com/documentation/roomplan/captured-object-attributes): 프레임워크가 스캔에서 식별한 물체와 표면의 세부 정보를 파악합니다.
:::

:::topic-grid
## 3D 자산 출력
- [캡처된 방 및 구조물 내보내기에 사용자 정의 모델 제공하기](https://developer.apple.com/documentation/roomplan/providing-custom-models-for-captured-rooms-and-structure-exports): 객체 경계 상자를 상세한 3D 렌더링으로 대체하여 내보낸 3D 모델의 외형을 향상합니다.
- [RoomBuilder](https://developer.apple.com/documentation/roomplan/roombuilder): 방 캡처 데이터로부터 3D 자산을 생성하는 객체입니다.
- [StructureBuilder](https://developer.apple.com/documentation/roomplan/structurebuilder): 여러 스캔 세션을 하나의 캡처 결과로 결합하는 객체입니다.
- [CapturedRoom.USDExportOptions](https://developer.apple.com/documentation/roomplan/capturedroom/usdexportoptions): 스캔 내보내기의 기반 데이터 형식을 결정하는 옵션입니다.
:::
