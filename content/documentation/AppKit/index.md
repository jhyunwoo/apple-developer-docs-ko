---
route: /documentation/AppKit
source_url: https://developer.apple.com/documentation/AppKit
source_locale: en-US
section: docc
content_type: symbol
title: AppKit
original_title: AppKit
source_hash: faf4625f159f664ea1aa4a6e72744d8776f9af90e82b6d83ae42566ec03f784b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:17:18+00:00'
last_translated_at: '2026-03-13T22:37:00+09:00'
---

# AppKit

macOS 앱을 위한 그래픽 기반 이벤트 주도 사용자 인터페이스를 구성하고 관리합니다.

## 개요

AppKit에는 macOS 앱의 사용자 인터페이스를 빌드하는 데 필요한 객체가 들어 있습니다. window, button, panel, text field를 그리는 것에 더해, 앱과 사용자, macOS 사이의 모든 이벤트 관리와 상호 작용도 처리합니다.

![Mac에서 Mount Fuji 랜드마크를 보여 주는 Landmarks 샘플 앱 이미지입니다.](https://developer.apple.com)

상호 작용을 그리고 관리하는 것 외에도, AppKit은 printing, animation, 그리고 대용량 데이터를 가진 문서를 효율적으로 생성하는 작업도 처리합니다. 이 프레임워크에는 앱이 가능한 많은 사람에게 도달할 수 있도록 현지화와 접근성을 위한 기본 지원도 포함되어 있습니다.

AppKit은 [SwiftUI](https://developer.apple.com/documentation/SwiftUI)와도 함께 동작하므로, AppKit 앱의 일부를 SwiftUI로 구현하거나 두 프레임워크 간에 인터페이스 요소를 섞어 사용할 수 있습니다. 예를 들어 AppKit view와 view controller를 SwiftUI view 안에 배치할 수 있고 그 반대도 가능합니다.

:::note 참고
iPad 앱을 Mac으로 가져오는 방법은 [Mac Catalyst](https://developer.apple.com/documentation/UIKit/mac-catalyst)를 참고하십시오. iOS 앱을 빌드하려면 SwiftUI를 사용해 Apple의 모든 플랫폼에서 동작하는 앱을 만들거나, [UIKit](https://developer.apple.com/documentation/UIKit)을 사용해 iOS 전용 앱을 만들 수 있습니다.
:::

:::topic-grid
## 핵심 사항
- [Adopting Liquid Glass](https://developer.apple.com/documentation/TechnologyOverviews/adopting-liquid-glass): 새로운 재질을 앱에 적용하는 방법을 알아봅니다.
- [AppKit updates](https://developer.apple.com/documentation/Updates/AppKit): AppKit의 중요한 변경 사항을 알아봅니다.
- [Protecting the User’s Privacy](https://developer.apple.com/documentation/UIKit/protecting-the-user-s-privacy): 개인 데이터를 보호하고 데이터 사용 방식에 대한 사용자 선호를 존중합니다.
- [Porting your macOS apps to Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/porting-your-macos-apps-to-apple-silicon): Apple silicon과 Intel 기반 Mac 모두에서 실행되는 macOS 앱 버전을 만듭니다.
:::

:::topic-grid
## 앱 구조
- [App and Environment](https://developer.apple.com/documentation/appkit/app-and-environment): 시스템과 상호 작용할 때 사용하는 객체를 알아봅니다.
- [Documents, Data, and Pasteboard](https://developer.apple.com/documentation/appkit/documents-data-and-pasteboard): 앱의 데이터와 환경설정을 구성하고, 그 데이터를 pasteboard 또는 iCloud에서 공유합니다.
- [Cocoa Bindings](https://developer.apple.com/documentation/appkit/cocoa-bindings): Cocoa Bindings를 사용해 데이터 모델과 앱 인터페이스를 자동으로 동기화합니다.
- [Resource Management](https://developer.apple.com/documentation/appkit/resource-management): 앱 사용자 인터페이스를 담고 있는 storyboard와 nib 파일을 관리하고, resource 파일에 저장된 데이터를 불러오는 방법을 알아봅니다.
- [App Extensions](https://developer.apple.com/documentation/appkit/app-extensions): 앱의 기본 기능을 시스템의 다른 부분으로 확장합니다.
:::

:::topic-grid
## 사용자 인터페이스
- [Views and Controls](https://developer.apple.com/documentation/appkit/views-and-controls): 화면에 콘텐츠를 표시하고 사용자 입력과 이벤트를 처리합니다.
- [View Management](https://developer.apple.com/documentation/appkit/view-management): window 안의 view 크기와 위치를 포함해 사용자 인터페이스를 관리합니다.
- [View Layout](https://developer.apple.com/documentation/appkit/view-layout): stack view 또는 Auto Layout 제약을 사용해 view의 위치와 크기를 정합니다.
- [Appearance Customization](https://developer.apple.com/documentation/appkit/appearance-customization): 앱에 Dark Mode 지원을 추가하고 appearance proxy를 사용해 UI를 수정합니다.
- [Animation](https://developer.apple.com/documentation/appkit/animation): view와 기타 콘텐츠를 애니메이션하여 사용자에게 더 매력적인 경험을 만듭니다.
- [Windows, Panels, and Screens](https://developer.apple.com/documentation/appkit/windows-panels-and-screens): view 계층을 구성하고 화면에 쉽게 표시합니다.
- [Sound, Speech, and Haptics](https://developer.apple.com/documentation/appkit/sound-speech-and-haptics): 사운드와 haptic feedback을 재생하고, 인터페이스에 음성 인식과 음성 합성을 통합합니다.
- [Supporting Continuity Camera in Your Mac App](https://developer.apple.com/documentation/appkit/supporting-continuity-camera-in-your-mac-app): Continuity Camera를 사용해 사용자의 iPhone, iPad, iPod touch에서 스캔한 문서와 사진을 Mac 앱에 통합합니다.
:::

:::topic-grid
## 사용자 상호 작용
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad): 마우스, 키보드, trackpad 입력과 관련된 이벤트를 처리합니다.
- [Menus, Cursors, and the Dock](https://developer.apple.com/documentation/appkit/menus-cursors-and-the-dock): 앱과의 상호 작용을 돕기 위해 메뉴와 cursor를 구현하고, 앱의 Dock 타일을 사용해 최신 정보를 전달합니다.
- [Gestures](https://developer.apple.com/documentation/appkit/gestures): gesture recognizer 안에 앱의 이벤트 처리 로직을 캡슐화하여 앱 전체에서 재사용할 수 있게 합니다.
- [Touch Bar](https://developer.apple.com/documentation/appkit/touch-bar): Touch Bar에 상호 작용 가능한 콘텐츠와 control을 표시합니다.
- [Drag and Drop](https://developer.apple.com/documentation/appkit/drag-and-drop): drag and drop을 사용해 앱 콘텐츠를 직접 조작할 수 있도록 지원합니다.
- [Accessibility for AppKit](https://developer.apple.com/documentation/appkit/accessibility-for-appkit): macOS를 사용하는 모든 사람이 AppKit 앱을 접근 가능하게 사용할 수 있도록 만듭니다.
:::

:::topic-grid
## 그래픽, 드로잉, 색상, 프린팅
- [Images and PDF](https://developer.apple.com/documentation/appkit/images-and-pdf): bitmap, PDF, 기타 포맷의 이미지를 생성하고 관리합니다.
- [Drawing](https://developer.apple.com/documentation/appkit/drawing): 화면에 도형, 이미지, 기타 콘텐츠를 그립니다.
- [Color](https://developer.apple.com/documentation/appkit/color): 내장 형식 또는 사용자 정의 형식으로 색상을 표현하고, 사용자가 색상을 선택하고 적용할 수 있는 옵션을 제공합니다.
- [Printing](https://developer.apple.com/documentation/appkit/printing): 시스템 print panel을 표시하고 printing 과정을 관리합니다.
:::

:::topic-grid
## 텍스트
- [Text Display](https://developer.apple.com/documentation/appkit/text-display): 텍스트를 표시하고 철자를 검사합니다.
- [TextKit](https://developer.apple.com/documentation/appkit/textkit): 텍스트 저장소를 관리하고 앱의 view 안에서 텍스트 기반 콘텐츠를 사용자 정의 레이아웃으로 배치합니다.
- [Fonts](https://developer.apple.com/documentation/appkit/fonts): 텍스트 표시 때 사용하는 font를 관리합니다.
- [Writing Tools](https://developer.apple.com/documentation/appkit/writing-tools): 앱의 text view에 Writing Tools 지원을 추가합니다.
:::

:::topic-grid
## 더 이상 사용되지 않음
- [Deprecated Symbols](https://developer.apple.com/documentation/appkit/deprecated-symbols): 더 이상 지원되지 않는 symbol을 검토하고 대신 사용할 대체 항목을 찾습니다.
:::

:::topic-grid
## 참고 자료
- [Enumerations](https://developer.apple.com/documentation/appkit/enumerations): 여러 클래스와 함께 사용하는 열거형입니다.
- [Constants](https://developer.apple.com/documentation/appkit/constants): 여러 클래스와 함께 사용하는 상수입니다.
- [Data Types](https://developer.apple.com/documentation/appkit/data-types): 여러 클래스와 함께 사용하는 데이터 타입입니다.
- [Macros](https://developer.apple.com/documentation/appkit/macros): 여러 클래스와 함께 사용하는 매크로입니다.
:::

:::topic-grid
## 변수
- [NSAttachmentCharacter](https://developer.apple.com/documentation/appkit/nsattachmentcharacter)
:::
