---
route: /documentation/ApplePencil
source_url: https://developer.apple.com/documentation/ApplePencil
source_locale: en-US
section: docc
content_type: article
title: Apple Pencil
original_title: Apple Pencil
source_hash: 046afa45107add97b49a09225b5ab9764940cb636286a57d5924e8856326e0a3
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:28:19+00:00'
last_translated_at: '2026-03-13T23:28:34+09:00'
---

# Apple Pencil

iPad 앱에서 그리기, 손글씨, 그리고 Apple Pencil의 다양한 기능을 지원하여 사용자 경험을 향상합니다.

## 개요

Apple Pencil은 사람들이 그리기, 스케치, 페인팅, 메모, 문서 마크업 등에 의존하는 iPad 입력 액세서리입니다. Apple Pencil은 드로잉과 손글씨뿐 아니라 포인터 및 UI 상호 작용 도구로도 사용할 수 있습니다.

![손이 Apple Pencil을 쥐고 디지털 드로잉 캔버스에 표시를 남기는 모습을 보여 주는 그림입니다.](https://developer.apple.com)

iPad용 앱을 최적화할 때는 Apple Pencil 기능으로 경험을 향상할 수 있는 방법이 많습니다. 앱의 맥락에서 가장 적절한 기능을 고르고, PencilKit, SwiftUI, UIKit API를 사용해 해당 기능을 채택하십시오.

:::term-list
**Drawing**: Apple Pencil은 손으로 그린 콘텐츠를 앱에 통합할 수 있게 해 주는 PencilKit과 자연스럽게 통합됩니다. PencilKit은 드로잉 캔버스 위에서 연필 스트로크를 만들고, 지우고, 선택하는 도구를 제공합니다. UIKit의 고정밀 터치를 사용해 직접 그리기 기능을 구현할 수도 있습니다. Apple Pencil 입력은 azimuth, altitude, roll angle, tip에 가해진 force 같은 데이터를 제공하며, 이를 사용해 풍부한 드로잉 경험을 만들 수 있습니다.
**Handwriting**: Apple Pencil을 사용하면 어떤 텍스트 필드에서든 손글씨 텍스트를 입력할 수 있고, Scribble이 이를 자동으로 타이핑된 텍스트 입력으로 변환합니다. Scribble은 여러 언어를 지원하며 기본적으로 활성화되어 있습니다. UIKit의 Scribble API를 사용하면 앱 요구에 맞게 Scribble 동작을 사용자화할 수도 있습니다.
**Double tap and squeeze**: 특정 Apple Pencil 모델에서는 사용자가 double tap이나 squeeze로 동작을 빠르게 수행할 수 있습니다. 사용자는 설정에서 double tap 또는 squeeze에 반응할 동작을 선택할 수 있고, 앱에 특화된 사용자 정의 동작을 구현할 수도 있습니다. double tap과 squeeze는 SwiftUI 또는 UIKit으로 처리합니다.
**Haptics**: Apple Pencil Pro는 햅틱 재생으로 촉각 피드백을 제공할 수 있습니다. 절제되고 일관되게 사용하면, 객체를 그리드에 스냅하는 작업처럼 Apple Pencil Pro를 활용한 경험을 더 향상할 수 있습니다. 햅틱 피드백은 SwiftUI의 sensory feedback API 또는 UIKit의 feedback generator API를 사용해 제공합니다.
**Hover**: 사용자가 지원되는 Apple Pencil 모델을 화면에 닿지 않을 정도로 가까이 가져가면, pencil은 tip이 화면에서 얼마나 떨어져 있는지에 대한 정보를 제공할 수 있습니다. 이 hover 거리를 이용해 더 표현력 있는 드로잉 및 입력 경험을 만들 수 있습니다. 이 정보는 UIKit의 hover gesture를 사용해 얻습니다.
**Pointers**: Apple Pencil은 trackpad나 마우스처럼 포인터와 비슷하게 동작할 수 있습니다. 예를 들어 사용자가 Apple Pencil을 view 위에 올려둘 때 시각적 피드백을 제공하도록 view를 구성할 수 있습니다. SwiftUI의 hover event 또는 UIKit의 pointer interaction을 사용해 hover 중 시각적 피드백을 추가합니다.
:::

Apple Pencil 기능과 호환성에 대한 자세한 내용은 [Apple Pencil](https://www.apple.com/apple-pencil/)을 참고하십시오.

#### 관련 비디오

:::topic-grid
## 핵심
- [Apple Pencil updates](https://developer.apple.com/documentation/Updates/ApplePencil): Apple Pencil의 중요한 변경 사항을 살펴봅니다.
:::

:::topic-grid
## 드로잉
- [Drawing with PencilKit](https://developer.apple.com/documentation/PencilKit/drawing-with-pencilkit): PencilKit을 사용해 표현력이 풍부하고 지연이 적은 드로잉을 앱에 추가합니다.
- [Inspecting, Modifying, and Constructing PencilKit Drawings](https://developer.apple.com/documentation/PencilKit/inspecting-modifying-and-constructing-pencilkit-drawings): PencilKit 드로잉 내부의 stroke와 point에 접근해 텍스트로 생성한 PencilKit 드로잉과의 일치 정도를 채점합니다.
- [Getting high-fidelity input with coalesced touches](https://developer.apple.com/documentation/UIKit/getting-high-fidelity-input-with-coalesced-touches): 앱에서 고정밀 터치를 지원하는 방법을 알아봅니다.
- [Implementing coalesced touch support in an app](https://developer.apple.com/documentation/UIKit/implementing-coalesced-touch-support-in-an-app): coalesced touch를 처리하는 간단한 앱을 만드는 방법을 알아봅니다.
:::

:::topic-grid
## 손글씨
- [Customizing Scribble with Interactions](https://developer.apple.com/documentation/PencilKit/customizing-scribble-with-interactions): interaction을 추가해 텍스트 입력이 아닌 view에서도 손글씨를 활성화합니다.
- [Handwriting recognition](https://developer.apple.com/documentation/UIKit/handwriting-recognition): Apple Pencil 입력을 처리하도록 텍스트 필드와 사용자 정의 view를 구성합니다.
:::

:::topic-grid
## Double tap 및 squeeze
- [Apple Pencil interactions](https://developer.apple.com/documentation/UIKit/apple-pencil-interactions): Apple Pencil의 double tap과 squeeze 같은 사용자 상호 작용을 처리합니다.
- [Handling squeezes from Apple Pencil](https://developer.apple.com/documentation/applepencil/handling-squeezes-from-apple-pencil): 사용자가 Apple Pencil Pro에서 수행하는 squeeze를 감지하고 응답합니다.
- [Handling double taps from Apple Pencil](https://developer.apple.com/documentation/applepencil/handling-double-taps-from-apple-pencil): 사용자가 Apple Pencil에서 수행하는 double tap을 감지하고 응답합니다.
:::

:::topic-grid
## 햅틱
- [Playing haptic feedback in your app](https://developer.apple.com/documentation/applepencil/playing-haptic-feedback-in-your-app): 사용자가 앱에서 특정 동작을 수행할 때 촉각 피드백을 제공합니다.
:::

:::topic-grid
## Hover
- [Adopting hover support for Apple Pencil](https://developer.apple.com/documentation/UIKit/adopting-hover-support-for-apple-pencil): Apple Pencil 입력의 hover preview로 iPadOS 앱의 사용자 피드백을 향상합니다.
:::

:::topic-grid
## 포인터
- [Input events](https://developer.apple.com/documentation/SwiftUI/Input-events): 키보드나 Touch Bar 같은 하드웨어 기기 입력에 응답합니다.
- [Pointer interactions](https://developer.apple.com/documentation/UIKit/pointer-interactions): 사용자 정의 control과 view에서 pointer interaction을 지원합니다.
- [Integrating pointer interactions into your iPad app](https://developer.apple.com/documentation/UIKit/integrating-pointer-interactions-into-your-ipad-app): view에 pointer interaction을 추가해 iPad 앱의 touch interaction을 지원합니다.
:::

:::topic-grid
## 디자인
- [Apple Pencil and Scribble](https://developer.apple.com/design/Human-Interface-Guidelines/apple-pencil-and-scribble): Apple Pencil은 그리기, 손글씨, 마크업을 자연스럽고 수월하게 만들며, 포인터 및 UI 상호 작용 도구로도 잘 동작합니다.
- [Playing haptics](https://developer.apple.com/design/Human-Interface-Guidelines/playing-haptics): 햅틱 재생은 사용자의 촉각을 자극하고 현실 세계의 익숙함을 앱이나 게임으로 가져올 수 있습니다.
:::
