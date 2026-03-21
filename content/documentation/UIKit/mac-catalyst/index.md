---
route: /documentation/UIKit/mac-catalyst
source_url: https://developer.apple.com/documentation/UIKit/mac-catalyst
source_locale: en-US
section: docc
content_type: article
title: Mac Catalyst
original_title: Mac Catalyst
source_hash: 1b43ac7bc538e02d30da065c3db0ed02bdfb8262d056e1d6d1503821ead28853
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:17:41+00:00'
last_translated_at: '2026-03-13T08:36:00+00:00'
---

# Mac Catalyst

사용자가 Mac 기기에서 실행할 수 있는 iPad 앱 버전을 만듭니다.

## 개요

Mac Catalyst를 사용하면 iPad 앱의 Mac 버전을 만들 수 있습니다. iPad 앱의 프로젝트 설정에서 Mac 체크상자를 클릭하면 프로젝트가 앱의 Mac 버전과 iPad 버전을 모두 빌드하도록 구성됩니다. 두 앱은 같은 프로젝트와 소스 코드를 공유하므로 한 곳에서 코드를 변경하기 쉽습니다.

![iPad와 Mac 노트북 사진입니다. iPad에서 Mac으로 향하는 화살표가 있으며, iPad 화면에는 샘플 레시피 앱이 보이고 노트북에는 그 앱의 Mac 버전이 표시됩니다.](https://developer.apple.com)

iPad 앱의 Mac 버전을 설계하는 방법에 대한 정보는 Human Interface Guidelines의 [Mac Catalyst](https://developer.apple.com/design/human-interface-guidelines/ios/overview/mac-catalyst/)를 참고하세요.

:::important Important
Mac Catalyst로 빌드한 Mac 앱은 [NSToolbar](https://developer.apple.com/documentation/AppKit/NSToolbar), [NSTouchBar](https://developer.apple.com/documentation/AppKit/NSTouchBar)처럼 Mac Catalyst에서 사용 가능하다고 표시된 [AppKit](https://developer.apple.com/documentation/AppKit) API만 사용할 수 있습니다. Mac Catalyst는 사용할 수 없는 AppKit API에 접근하는 것을 지원하지 않습니다.
:::

:::topic-grid
## 필수 항목
- [iPad 앱의 Mac 버전 만들기](https://developer.apple.com/documentation/uikit/creating-a-mac-version-of-your-ipad-app): Mac Catalyst로 iPad 앱을 macOS로 가져옵니다.
:::

:::topic-grid
## 앱 지원
- [Mac Catalyst로 iPad 앱을 Mac으로 가져오기](https://developer.apple.com/tutorials/Mac-Catalyst): iPad 앱과 같은 코드베이스로 네이티브 Mac 앱을 빌드합니다.
- [Mac 앱의 사용자 인터페이스 관용구 선택하기](https://developer.apple.com/documentation/uikit/choosing-a-user-interface-idiom-for-your-mac-app): Mac Catalyst로 빌드한 Mac 앱에서 iPad 또는 Mac 사용자 인터페이스 관용구를 선택합니다.
- [Mac을 위해 iPad 앱 최적화하기](https://developer.apple.com/documentation/uikit/optimizing-your-ipad-app-for-mac): macOS의 시스템 기능을 활용해 iPad 앱을 더 Mac 앱처럼 만듭니다.
- [LSMinimumSystemVersion](https://developer.apple.com/documentation/BundleResources/Information-Property-List/LSMinimumSystemVersion): 앱이 macOS에서 실행되기 위해 필요한 최소 운영체제 버전입니다.
- [UIApplicationSupportsTabbedSceneCollection](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSceneManifest/UIApplicationSupportsTabbedSceneCollection): Mac Catalyst로 빌드한 앱이 자동 탭 모드를 지원하는지 나타내는 불리언 값입니다.
:::

:::topic-grid
## 사용자 인터페이스
- [UIKit Catalog: 뷰와 컨트롤 생성 및 사용자화](https://developer.apple.com/documentation/uikit/uikit-catalog-creating-and-customizing-views-and-controls): 뷰와 컨트롤로 앱의 사용자 인터페이스를 사용자화합니다.
- [Mac Catalyst로 앱 빌드 및 개선하기](https://developer.apple.com/documentation/uikit/building-and-improving-your-app-with-mac-catalyst): 네이티브 컨트롤, 다중 윈도우, 공유, 인쇄, 메뉴, 키보드 단축키를 지원해 iPadOS 앱을 개선합니다.
- [Mac Catalyst로 빌드한 Mac 앱에서 체크상자 표시하기](https://developer.apple.com/documentation/uikit/displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst): 앱이 Mac 사용자 인터페이스 관용구로 실행될 때 스위치 컨트롤을 Mac 스타일 체크상자로 표시합니다.
- [Mac Catalyst로 빌드한 Mac 앱에서 제목 막대 제거하기](https://developer.apple.com/documentation/uikit/removing-the-title-bar-in-your-mac-app-built-with-mac-catalyst): 제목 막대를 제거해 창의 전체 높이를 채우는 콘텐츠를 표시합니다.
- [Toolbar](https://developer.apple.com/documentation/uikit/toolbar): 창의 제목 막대 아래와 사용자 정의 콘텐츠 위에 컨트롤을 배치할 공간을 제공합니다.
- [Touch Bar](https://developer.apple.com/documentation/AppKit/touch-bar): Touch Bar에 상호 작용 가능한 콘텐츠와 컨트롤을 표시합니다.
:::

:::topic-grid
## 사용자 상호 작용
- [키보드로 앱의 사용자 인터페이스 탐색하기](https://developer.apple.com/documentation/uikit/navigating-an-app-s-user-interface-using-a-keyboard): iPad 앱과 Mac Catalyst로 빌드한 앱에서 키보드와 포커스 가능한 UI 요소를 사용해 인터페이스 요소 사이를 이동합니다.
- [메뉴 막대와 사용자 인터페이스에 메뉴 및 단축키 추가하기](https://developer.apple.com/documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface): Mac Catalyst로 빌드한 Mac 앱에 메뉴와 키보드 단축키를 추가해 유용한 동작에 빠르게 접근할 수 있게 합니다.
- [물리 키보드에서 발생한 키 입력 처리하기](https://developer.apple.com/documentation/uikit/handling-key-presses-made-on-a-physical-keyboard): 물리 키보드에서 키를 누르고 놓는 시점을 감지합니다.
- [UIHoverGestureRecognizer](https://developer.apple.com/documentation/uikit/uihovergesturerecognizer): 뷰 위에서 포인터가 움직이는 동작을 해석하는 연속 제스처 인식기입니다.
:::

:::topic-grid
## 사용자 환경설정
- [설정 창 표시하기](https://developer.apple.com/documentation/uikit/displaying-a-settings-window): Mac Catalyst로 빌드한 Mac 앱에 Settings 번들에 정의된 앱 설정을 관리할 수 있는 설정 창을 제공합니다.
- [환경설정 창의 변경 감지하기](https://developer.apple.com/documentation/uikit/detecting-changes-in-the-preferences-window): Combine을 사용해 Mac Catalyst로 빌드한 Mac 앱에서 사용자의 환경설정 변경을 감지하고 대응합니다.
:::

:::topic-grid
## 툴팁
- [툴팁 상호 작용을 사용해 뷰와 컨트롤에 도움말 태그 표시하기](https://developer.apple.com/documentation/uikit/showing-help-tags-for-views-and-controls-using-tooltip-interactions): 사용자가 포인터를 요소 위에 올렸을 때 툴팁을 표시해 인터페이스 요소의 목적을 설명합니다.
- [UIToolTipInteraction](https://developer.apple.com/documentation/uikit/uitooltipinteraction): 뷰나 컨트롤 위에 포인터를 올렸을 때 툴팁을 표시할 수 있게 해 주는 상호 작용 객체입니다.
- [UIToolTipInteractionDelegate](https://developer.apple.com/documentation/uikit/uitooltipinteractiondelegate): 상호 작용에 툴팁 설정을 제공하는 인터페이스입니다.
:::
