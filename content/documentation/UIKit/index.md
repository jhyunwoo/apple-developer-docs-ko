---
route: /documentation/UIKit
source_url: https://developer.apple.com/documentation/UIKit
source_locale: en-US
section: docc
content_type: symbol
title: UIKit
original_title: UIKit
source_hash: 9c2d1b7aa46d0058107c1c3211212e05840c65fb79e7616056d9748f0f3cae85
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:11:05+00:00'
last_translated_at: '2026-03-13T22:16:00+09:00'
---

# UIKit

iOS, iPadOS, tvOS 앱을 위한 그래픽 기반 이벤트 주도 사용자 인터페이스를 구성하고 관리합니다.

## 개요

UIKit은 앱을 빌드하기 위한 다양한 기능을 제공하며, iOS, iPadOS, tvOS 앱의 핵심 인프라를 구성하는 데 사용할 수 있는 컴포넌트도 포함합니다. 이 프레임워크는 UI를 구현하기 위한 window 및 view 아키텍처, Multi-Touch와 기타 입력을 앱으로 전달하는 이벤트 처리 인프라, 사용자·시스템·앱 간 상호 작용을 관리하는 메인 run loop를 제공합니다.

![iPad와 iPhone에서 Mount Fuji 랜드마크를 보여주는 Landmarks 샘플 앱 이미지입니다.](https://developer.apple.com)

UIKit에는 애니메이션, 문서, 드로잉 및 프린팅, 텍스트 관리 및 표시, 검색, app extension, 리소스 관리, 현재 기기 정보 획득을 위한 지원도 포함되어 있습니다. 또한 접근성 지원을 사용자화하고, 서로 다른 언어, 국가, 문화권에 맞게 앱 인터페이스를 현지화할 수 있습니다.

UIKit은 [SwiftUI](https://developer.apple.com/documentation/SwiftUI) 프레임워크와 자연스럽게 함께 동작하므로, UIKit 앱의 일부를 SwiftUI로 구현하거나 두 프레임워크의 인터페이스 요소를 섞어 사용할 수 있습니다. 예를 들어 UIKit view와 view controller를 SwiftUI view 안에 배치할 수 있고, 반대로도 가능합니다.

macOS 앱을 빌드하려면 [SwiftUI](https://developer.apple.com/documentation/SwiftUI)를 사용해 Apple의 모든 플랫폼에서 동작하는 앱을 만들거나, [AppKit](https://developer.apple.com/documentation/AppKit)을 사용해 Mac 전용 앱을 만들 수 있습니다. 또는 [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst)를 사용해 UIKit 기반 iPad 앱을 Mac으로 가져올 수도 있습니다.

:::important 중요
특정 클래스 문서에서 별도로 명시하지 않는 한 UIKit 클래스는 앱의 main thread 또는 main dispatch queue에서만 사용하십시오. 이 제한은 특히 [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)를 상속하는 클래스나, 어떤 형태로든 앱의 사용자 인터페이스를 조작하는 클래스에 적용됩니다.
:::

:::topic-grid
## 핵심 사항
- [Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass): 새로운 재질을 앱에 적용하는 방법을 알아봅니다.
- [UIKit updates](https://developer.apple.com/documentation/Updates/UIKit): UIKit의 중요한 변경 사항을 알아봅니다.
- [About app development with UIKit](https://developer.apple.com/documentation/uikit/about-app-development-with-uikit): UIKit과 Xcode가 iOS 및 tvOS 앱에 제공하는 기본 지원을 알아봅니다.
- [Protecting the User’s Privacy](https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy): 개인 데이터를 보호하고 데이터 사용 방식에 대한 사용자 선호를 존중합니다.
:::

:::topic-grid
## 앱 구조
- [App and environment](https://developer.apple.com/documentation/uikit/app-and-environment): 생명 주기 이벤트와 앱의 UI scene을 관리하고, 앱이 실행되는 환경과 trait에 대한 정보를 가져옵니다.
- [Documents, data, and pasteboard](https://developer.apple.com/documentation/uikit/documents-data-and-pasteboard): 앱의 데이터를 구성하고 그 데이터를 pasteboard에서 공유합니다.
- [Resource management](https://developer.apple.com/documentation/uikit/resource-management): 앱 인터페이스 구현에 사용하는 이미지, 문자열, storyboard, nib 파일을 관리합니다.
- [App extensions](https://developer.apple.com/documentation/uikit/app-extensions): 앱의 기본 기능을 시스템의 다른 부분으로 확장합니다.
- [Interprocess communication](https://developer.apple.com/documentation/uikit/interprocess-communication): 사용자에게 activity 기반 서비스를 표시합니다.
- [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst): 사용자가 Mac 기기에서 실행할 수 있는 iPad 앱 버전을 만듭니다.
:::

:::topic-grid
## 사용자 인터페이스
- [Views and controls](https://developer.apple.com/documentation/uikit/views-and-controls): 화면에 콘텐츠를 표시하고 그 콘텐츠에 허용할 상호 작용을 정의합니다.
- [View controllers](https://developer.apple.com/documentation/uikit/view-controllers): view controller를 사용해 인터페이스를 관리하고 앱 콘텐츠 사이의 탐색을 쉽게 만듭니다.
- [View layout](https://developer.apple.com/documentation/uikit/view-layout): stack view를 사용해 인터페이스의 view를 자동으로 배치합니다. view를 정확히 배치해야 할 때는 Auto Layout을 사용합니다.
- [Appearance customization](https://developer.apple.com/documentation/uikit/appearance-customization): view에 Liquid Glass를 적용하고, 앱에서 Dark Mode를 지원하며, bar의 외관을 사용자화하고, appearance proxy를 사용해 UI를 수정합니다.
- [Animation and haptics](https://developer.apple.com/documentation/uikit/animation-and-haptics): view 기반 애니메이션과 haptic을 사용해 사용자에게 피드백을 제공합니다.
- [Windows and screens](https://developer.apple.com/documentation/uikit/windows-and-screens): view 계층과 기타 콘텐츠를 담는 컨테이너를 제공합니다.
:::

:::topic-grid
## 사용자 상호 작용
- [Touches, presses, and gestures](https://developer.apple.com/documentation/uikit/touches-presses-and-gestures): gesture recognizer 안에 앱의 이벤트 처리 로직을 캡슐화하여 앱 전체에서 재사용할 수 있게 합니다.
- [Menus and shortcuts](https://developer.apple.com/documentation/uikit/menus-and-shortcuts): 메뉴 시스템, 문맥 메뉴, 홈 화면 빠른 동작, 키보드 shortcut을 사용해 앱과의 상호 작용을 단순화합니다.
- [Drag and drop](https://developer.apple.com/documentation/uikit/drag-and-drop): view와 함께 interaction API를 사용해 앱에 drag and drop을 도입합니다.
- [Pointer interactions](https://developer.apple.com/documentation/uikit/pointer-interactions): 사용자 정의 control 및 view에서 pointer 상호 작용을 지원합니다.
- [Apple Pencil interactions](https://developer.apple.com/documentation/uikit/apple-pencil-interactions): Apple Pencil에서 double tap과 squeeze 같은 사용자 상호 작용을 처리합니다.
- [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based-navigation): remote, game controller, keyboard를 사용해 UIKit 앱 인터페이스를 탐색합니다.
- [Accessibility for UIKit](https://developer.apple.com/documentation/uikit/accessibility-for-uikit): iOS와 tvOS를 사용하는 모든 사람이 UIKit 앱을 접근 가능하게 사용할 수 있도록 만듭니다.
:::

:::topic-grid
## 그래픽, 드로잉, 프린팅
- [Images and PDF](https://developer.apple.com/documentation/uikit/images-and-pdf): bitmap 및 PDF 포맷을 사용하는 이미지를 포함해 이미지를 생성하고 관리합니다.
- [Drawing](https://developer.apple.com/documentation/uikit/drawing): 색상, renderer, draw path, 문자열, 그림자를 사용해 앱의 drawing 환경을 구성합니다.
- [Printing](https://developer.apple.com/documentation/uikit/printing): 시스템 print panel을 표시하고 printing 과정을 관리합니다.
:::

:::topic-grid
## 텍스트
- [Text display and fonts](https://developer.apple.com/documentation/uikit/text-display-and-fonts): 텍스트를 표시하고, font를 관리하고, 철자를 검사합니다.
- [TextKit](https://developer.apple.com/documentation/uikit/textkit): 텍스트 저장소를 관리하고 앱의 view 안에서 텍스트 기반 콘텐츠를 사용자 정의 레이아웃으로 배치합니다.
- [Keyboards and input](https://developer.apple.com/documentation/uikit/keyboards-and-input): 시스템 keyboard를 구성하고, 입력을 처리하는 사용자 정의 keyboard를 만들거나, 실제 keyboard의 키 입력을 감지합니다.
- [Writing Tools](https://developer.apple.com/documentation/uikit/writing-tools): 앱의 text view에 Writing Tools 지원을 추가합니다.
- [Handwriting recognition](https://developer.apple.com/documentation/uikit/handwriting-recognition): 텍스트를 받는 text field와 사용자 정의 view가 Apple Pencil 입력을 처리하도록 구성합니다.
:::

:::topic-grid
## 더 이상 사용되지 않음
- [Deprecated symbols](https://developer.apple.com/documentation/uikit/deprecated-symbols): 지원되지 않는 symbol과 대체 항목을 검토합니다.
:::

:::topic-grid
## 참고 자료
- [UIKit Enumerations](https://developer.apple.com/documentation/uikit/uikit-enumerations)
- [UIKit Constants](https://developer.apple.com/documentation/uikit/uikit-constants): 이 문서는 UIKit 프레임워크 전반에서 사용되는 상수를 설명합니다.
- [UIKit Data Types](https://developer.apple.com/documentation/uikit/uikit-data-types): UIKit 프레임워크는 프레임워크 여러 곳에서 사용하는 데이터 타입을 정의합니다.
- [UIKit Functions](https://developer.apple.com/documentation/uikit/uikit-functions): UIKit 프레임워크는 많은 함수를 정의하며, 그중 다수는 그래픽과 드로잉 연산에 사용됩니다.
:::

:::topic-grid
## 클래스
- [UIColorEffect](https://developer.apple.com/documentation/uikit/uicoloreffect): 단색 배경을 적용하는 시각 효과입니다.
:::
