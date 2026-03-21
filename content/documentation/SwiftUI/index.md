---
route: /documentation/SwiftUI
source_url: https://developer.apple.com/documentation/SwiftUI
source_locale: en-US
section: docc
content_type: symbol
title: SwiftUI
original_title: SwiftUI
source_hash: 5cf0f8a6e6186ef617aae87cca063b0e22f7b169d65d22a3a1605a760afc1204
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:09:09+00:00'
last_translated_at: '2026-03-13T19:15:00+09:00'
---

# SwiftUI

모든 플랫폼에서 앱의 사용자 인터페이스와 동작을 선언합니다.

## 개요

SwiftUI는 앱의 사용자 인터페이스를 선언하기 위한 view, control, 레이아웃 구조를 제공합니다. 이 프레임워크는 탭, 제스처, 그 밖의 다양한 입력을 앱에 전달하는 이벤트 핸들러와, 앱의 모델에서 사용자가 보고 상호 작용하는 view와 control까지 데이터 흐름을 관리하는 도구를 제공합니다.

[App](https://developer.apple.com/documentation/swiftui/app) 프로토콜을 사용해 앱 구조를 정의하고, 앱의 사용자 인터페이스를 구성하는 view를 담은 scene들로 이를 채우십시오. [View](https://developer.apple.com/documentation/swiftui/view) 프로토콜을 따르는 사용자 정의 view를 만들고, 이를 텍스트, 이미지, 사용자 정의 도형을 표시하는 SwiftUI view와 함께 stack, list 등으로 조합하십시오. 내장 view와 자신이 만든 view에 강력한 modifier를 적용해 렌더링 방식과 상호 작용을 사용자화할 수 있습니다. 여러 플랫폼에서 문맥과 표시 방식에 적응하는 view와 control을 사용해 앱 사이에 코드를 공유할 수도 있습니다.

![Mac, iPad, iPhone에서 후지산 랜드마크를 보여 주는 Landmarks 샘플 앱 이미지입니다.](https://developer.apple.com)

[UIKit](https://developer.apple.com/documentation/UIKit), [AppKit](https://developer.apple.com/documentation/AppKit), [WatchKit](https://developer.apple.com/documentation/WatchKit) 프레임워크의 객체와 SwiftUI view를 통합하여 플랫폼별 기능을 더 활용할 수 있습니다. 또한 SwiftUI의 접근성 지원을 사용자화하고, 앱 인터페이스를 다양한 언어, 국가, 문화권에 맞게 지역화할 수도 있습니다.

:::tip 팁
SwiftUI가 처음이라면 [SwiftUI Pathway](https://developer.apple.com/swiftui/get-started/)를 방문해 보십시오. SwiftUI 시작을 돕는 튜토리얼, 글, 샘플 프로젝트 모음입니다.
:::

### 대표 샘플

:::topic-grid
## 핵심 사항
- [Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass): 앱에 새로운 머티리얼을 적용하는 방법을 알아봅니다.
- [Develop in Swift](https://developer.apple.com/tutorials/Develop-in-Swift#explore-xcode): Develop in Swift 튜토리얼은 Apple 플랫폼용 앱을 만드는 방법을 배우는 모든 사람에게 Swift와 Xcode를 이용한 앱 개발을 소개합니다.
- [SwiftUI updates](https://developer.apple.com/documentation/Updates/SwiftUI): SwiftUI의 중요한 변경 사항을 알아봅니다.
- [Landmarks: Building an app with Liquid Glass](https://developer.apple.com/documentation/swiftui/landmarks-building-an-app-with-liquid-glass): 시스템 제공 Liquid Glass와 사용자 정의 Liquid Glass로 앱 경험을 향상합니다.
:::

:::topic-grid
## 앱 구조
- [App organization](https://developer.apple.com/documentation/swiftui/app-organization): 앱의 진입점과 최상위 구조를 정의합니다.
- [Scenes](https://developer.apple.com/documentation/swiftui/scenes): 앱의 부분을 이루는 사용자 인터페이스 그룹을 선언합니다.
- [Windows](https://developer.apple.com/documentation/swiftui/windows): 사용자 인터페이스 콘텐츠를 단일 window 또는 window 모음으로 표시합니다.
- [Immersive spaces](https://developer.apple.com/documentation/swiftui/immersive-spaces): 사용자의 주변 공간에 경계 없는 콘텐츠를 표시합니다.
- [Documents](https://developer.apple.com/documentation/swiftui/documents): 사용자가 문서를 열고 관리할 수 있게 합니다.
- [Navigation](https://developer.apple.com/documentation/swiftui/navigation): 사용자가 scene 안에서 앱의 view 계층 구조의 서로 다른 부분 사이를 이동할 수 있게 합니다.
- [Modal presentations](https://developer.apple.com/documentation/swiftui/modal-presentations): 집중된 상호 작용을 제공하는 별도의 view에 콘텐츠를 표시합니다.
- [Toolbars](https://developer.apple.com/documentation/swiftui/toolbars): 자주 사용하는 명령과 control에 즉시 접근할 수 있게 합니다.
- [Search](https://developer.apple.com/documentation/swiftui/search): 사용자가 앱 내 텍스트 또는 다른 콘텐츠를 검색할 수 있게 합니다.
- [App extensions](https://developer.apple.com/documentation/swiftui/app-extensions): 위젯 추가처럼 앱의 기본 기능을 시스템의 다른 부분으로 확장합니다.
:::

:::topic-grid
## 데이터와 저장소
- [Model data](https://developer.apple.com/documentation/swiftui/model-data): 앱 인터페이스를 구동하는 데이터를 관리합니다.
- [Environment values](https://developer.apple.com/documentation/swiftui/environment-values): environment를 사용해 view 계층 전체에 데이터를 공유합니다.
- [Preferences](https://developer.apple.com/documentation/swiftui/preferences): view에서 컨테이너 view로 구성 선호 사항을 전달합니다.
- [Persistent storage](https://developer.apple.com/documentation/swiftui/persistent-storage): 앱 세션 전반에 걸쳐 사용할 데이터를 저장합니다.
:::

:::topic-grid
## View
- [View fundamentals](https://developer.apple.com/documentation/swiftui/view-fundamentals): view 계층 구조를 사용해 앱의 시각 요소를 정의합니다.
- [View configuration](https://developer.apple.com/documentation/swiftui/view-configuration): 계층 구조 안의 view 특성을 조정합니다.
- [View styles](https://developer.apple.com/documentation/swiftui/view-styles): 다양한 view 유형에 내장 또는 사용자 정의 모양과 동작을 적용합니다.
- [Animations](https://developer.apple.com/documentation/swiftui/animations): 상태 변화에 반응해 부드러운 시각적 업데이트를 만듭니다.
- [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output): 서식 있는 텍스트를 표시하고 사용자로부터 텍스트 입력을 받습니다.
- [Images](https://developer.apple.com/documentation/swiftui/images): 이미지와 심볼을 앱 사용자 인터페이스에 추가합니다.
- [Controls and indicators](https://developer.apple.com/documentation/swiftui/controls-and-indicators): 값을 표시하고 사용자 선택을 받습니다.
- [Menus and commands](https://developer.apple.com/documentation/swiftui/menus-and-commands): 공간 효율적이고 문맥 의존적인 방식으로 명령과 control에 접근하게 합니다.
- [Shapes](https://developer.apple.com/documentation/swiftui/shapes): 내장 또는 사용자 정의 도형을 색상, 그라데이션, 또는 다른 패턴으로 그리거나 채웁니다.
- [Drawing and graphics](https://developer.apple.com/documentation/swiftui/drawing-and-graphics): 그래픽 효과와 사용자 정의 드로잉으로 view를 향상합니다.
:::

:::topic-grid
## View 레이아웃
- [Layout fundamentals](https://developer.apple.com/documentation/swiftui/layout-fundamentals): stack, grid 같은 내장 레이아웃 컨테이너 안에 view를 배치합니다.
- [Layout adjustments](https://developer.apple.com/documentation/swiftui/layout-adjustments): 정렬, 간격, 패딩, 기타 레이아웃 매개변수를 세밀하게 조정합니다.
- [Custom layout](https://developer.apple.com/documentation/swiftui/custom-layout): 사용자 정의 배치에 view를 배치하고 레이아웃 유형 간 애니메이션 전환을 만듭니다.
- [Lists](https://developer.apple.com/documentation/swiftui/lists): 구조화된 스크롤 가능한 정보 열을 표시합니다.
- [Tables](https://developer.apple.com/documentation/swiftui/tables): 선택 가능하고 정렬 가능한 데이터를 행과 열로 배치해 표시합니다.
- [View groupings](https://developer.apple.com/documentation/swiftui/view-groupings): form이나 control group 같은 목적 중심 컨테이너에 view를 표시합니다.
- [Scroll views](https://developer.apple.com/documentation/swiftui/scroll-views): 현재 화면에 다 들어가지 않는 콘텐츠를 사용자가 스크롤할 수 있게 합니다.
:::

:::topic-grid
## 이벤트 처리
- [Gestures](https://developer.apple.com/documentation/swiftui/gestures): 탭, 클릭, 스와이프부터 세밀한 제스처까지 다양한 상호 작용을 정의합니다.
- [Input events](https://developer.apple.com/documentation/swiftui/input-events): 키보드나 Touch Bar 같은 하드웨어 기기의 입력에 반응합니다.
- [Clipboard](https://developer.apple.com/documentation/swiftui/clipboard): 복사 및 붙여넣기 명령을 사용해 사용자가 항목을 이동하거나 복제할 수 있게 합니다.
- [Drag and drop](https://developer.apple.com/documentation/swiftui/drag-and-drop): 사용자가 항목을 한 위치에서 다른 위치로 드래그해 이동하거나 복제할 수 있게 합니다.
- [Focus](https://developer.apple.com/documentation/swiftui/focus): 어떤 보이는 객체가 사용자 상호 작용에 반응하는지 식별하고 제어합니다.
- [System events](https://developer.apple.com/documentation/swiftui/system-events): URL 열기 같은 시스템 이벤트에 반응합니다.
:::

:::topic-grid
## 접근성
- [Accessibility fundamentals](https://developer.apple.com/documentation/swiftui/accessibility-fundamentals): 장애가 있는 사람을 포함해 모두가 SwiftUI 앱을 사용할 수 있도록 만듭니다.
- [Accessible appearance](https://developer.apple.com/documentation/swiftui/accessible-appearance): 앱 인터페이스 콘텐츠의 가독성을 향상합니다.
- [Accessible controls](https://developer.apple.com/documentation/swiftui/accessible-controls): 앱이 수행할 수 있는 동작에 더 쉽게 접근할 수 있게 합니다.
- [Accessible descriptions](https://developer.apple.com/documentation/swiftui/accessible-descriptions): 사람들이 인터페이스 요소가 무엇을 나타내는지 이해할 수 있도록 설명합니다.
- [Accessible navigation](https://developer.apple.com/documentation/swiftui/accessible-navigation): 사용자가 rotor를 사용해 특정 사용자 인터페이스 요소로 이동할 수 있게 합니다.
:::

:::topic-grid
## 프레임워크 통합
- [AppKit integration](https://developer.apple.com/documentation/swiftui/appkit-integration): AppKit view를 SwiftUI 앱에 추가하거나 SwiftUI view를 AppKit 앱에서 사용합니다.
- [UIKit integration](https://developer.apple.com/documentation/swiftui/uikit-integration): UIKit view를 SwiftUI 앱에 추가하거나 SwiftUI view를 UIKit 앱에서 사용합니다.
- [WatchKit integration](https://developer.apple.com/documentation/swiftui/watchkit-integration): WatchKit view를 SwiftUI 앱에 추가하거나 SwiftUI view를 WatchKit 앱에서 사용합니다.
- [Technology-specific views](https://developer.apple.com/documentation/swiftui/technology-specific-views): 다른 Apple 프레임워크가 제공하는 SwiftUI view를 사용합니다.
:::

:::topic-grid
## 도구 지원
- [Previews in Xcode](https://developer.apple.com/documentation/swiftui/previews-in-xcode): 사용자 정의 view의 동적이고 상호 작용 가능한 preview를 생성합니다.
- [Xcode library customization](https://developer.apple.com/documentation/swiftui/xcode-library-customization): 사용자 정의 view와 modifier를 Xcode 라이브러리에 노출합니다.
- [Performance analysis](https://developer.apple.com/documentation/swiftui/performance-analysis): 앱의 응답성을 측정하고 개선합니다.
:::
