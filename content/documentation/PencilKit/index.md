---
route: /documentation/PencilKit
source_url: https://developer.apple.com/documentation/PencilKit
source_locale: en-US
section: docc
content_type: symbol
title: PencilKit
original_title: PencilKit
source_hash: ca389d9430a5720fd1ef65c7f8d0948e54b7a16896a2b6a4a62a889905f0d22f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:38:51+00:00'
last_translated_at: '2026-03-13T23:42:00+09:00'
---

# PencilKit

터치와 Apple Pencil 입력을 드로잉으로 캡처하고, 앱에서 그 콘텐츠를 표시합니다.

## 개요

PencilKit을 사용하면 손으로 그린 콘텐츠를 iPadOS 또는 macOS 앱에 쉽게 통합할 수 있습니다. PencilKit은 Apple Pencil 또는 사용자의 손가락 입력을 받아 iPadOS, iOS, macOS에서 표시할 이미지로 바꾸는 드로잉 환경을 iOS 앱에 제공합니다. 이 환경에는 선을 만들고, 지우고, 선택하는 도구가 함께 제공됩니다.

기존 뷰 계층에 통합하는 [PKCanvasView](https://developer.apple.com/documentation/pencilkit/pkcanvasview) 객체를 사용해 iPad 앱에서 콘텐츠를 캡처합니다. 이 객체는 Apple Pencil이나 손가락에서 발생한 터치를 지연 없이 캡처하는 기능을 지원합니다. canvas 객체는 최종 결과를 [PKDrawing](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct) 객체로 보내며, 그 내용은 앱의 콘텐츠와 함께 저장할 수 있습니다. 그린 콘텐츠를 이미지로 변환해 iOS 또는 macOS 앱에 표시할 수도 있습니다.

UIKit 앱에서 Apple Pencil의 사용자 상호 작용을 처리하는 방법은 [Apple Pencil interactions](https://developer.apple.com/documentation/UIKit/apple-pencil-interactions)를 참고합니다.

:::topic-grid
## Canvas
- [Drawing with PencilKit](https://developer.apple.com/documentation/pencilkit/drawing-with-pencilkit): PencilKit을 사용해 표현력이 풍부하고 지연이 적은 드로잉을 앱에 추가합니다.
- [Customizing Scribble with Interactions](https://developer.apple.com/documentation/pencilkit/customizing-scribble-with-interactions): interaction을 추가해 텍스트 입력 뷰가 아닌 곳에서도 쓰기를 가능하게 합니다.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](https://developer.apple.com/documentation/pencilkit/inspecting-modifying-and-constructing-pencilkit-drawings): PencilKit drawing 내부의 stroke와 point에 접근해, 텍스트로 생성된 PencilKit drawing과 사용자의 매칭 능력을 점수화합니다.
- [PKCanvasView](https://developer.apple.com/documentation/pencilkit/pkcanvasview): Apple Pencil 입력을 캡처하고 렌더링된 결과를 iOS 앱에 표시하는 뷰입니다.
- [PKDrawing](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct): canvas view가 캡처한 드로잉 정보를 나타내는 구조체입니다.
- [PKStroke](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct): canvas에 그린 stroke의 경로, 경계, 기타 속성을 나타내는 구조체입니다.
- [PKStrokePath](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct): stroke를 구성하는 요소를 캡처하고 stroke 경로를 따라 점을 찾고 보간하는 메서드를 제공하는 구조체입니다.
- [PKStrokePoint](https://developer.apple.com/documentation/pencilkit/pkstrokepoint-swift.struct): stroke 경로를 따라 있는 특정 지점의 속성을 나타내는 구조체입니다.
- [PKInk](https://developer.apple.com/documentation/pencilkit/pkink-swift.struct): 타입, 색상, 너비를 지정하는 잉크를 나타내는 구조체입니다.
:::

:::topic-grid
## 도구
- [Configuring the PencilKit tool picker](https://developer.apple.com/documentation/pencilkit/configuring-the-pencilkit-tool-picker): 다양한 시스템 도구와 사용자 정의 도구를 갖춘 PencilKit tool picker를 드로잉 앱에 통합합니다.
- [PKToolPicker](https://developer.apple.com/documentation/pencilkit/pktoolpicker): 사용자가 선택할 수 있는 드로잉 도구와 색상 모음을 표시하는 도구 팔레트입니다.
- [PKInkingTool](https://developer.apple.com/documentation/pencilkit/pkinkingtool-swift.struct): canvas view에 선을 그릴 때 사용할 드로잉 특성(너비, 색상, 펜 스타일)을 정의하는 구조체입니다.
- [PKEraserTool](https://developer.apple.com/documentation/pencilkit/pkerasertool-swift.struct): canvas view에서 이전에 그린 콘텐츠를 지우는 도구입니다.
- [PKLassoTool](https://developer.apple.com/documentation/pencilkit/pklassotool-swift.struct): canvas view에서 stroke 선과 도형을 선택하는 도구입니다.
- [PKTool](https://developer.apple.com/documentation/pencilkit/pktool-swift.protocol): canvas view에서 사용하는 드로잉 및 쓰기 도구가 채택하는 인터페이스입니다.
:::

:::topic-grid
## 하위 호환성
- [Supporting backward compatibility for ink types](https://developer.apple.com/documentation/pencilkit/supporting-backward-compatibility-for-ink-types): 최신 PencilKit 기능을 활용하면서도 이를 지원하지 않는 이전 OS 버전에서 좋은 사용자 경험을 제공합니다.
- [PKContentVersion](https://developer.apple.com/documentation/pencilkit/pkcontentversion): 하위 호환성을 위한 PencilKit 버전을 나타내는 상수입니다.
:::

:::topic-grid
## 클래스
- [PKResponderState](https://developer.apple.com/documentation/pencilkit/pkresponderstate): 와 관련된 PencilKit 동작의 상태입니다.
:::

:::topic-grid
## 열거형
- [PKToolPickerVisibility](https://developer.apple.com/documentation/pencilkit/pktoolpickervisibility): tool picker의 가시성 상태입니다.
:::
