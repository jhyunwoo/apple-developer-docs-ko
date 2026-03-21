---
route: /documentation/BrowserEngineKit
source_url: https://developer.apple.com/documentation/BrowserEngineKit
source_locale: en-US
section: docc
content_type: symbol
title: BrowserEngineKit
original_title: BrowserEngineKit
source_hash: d76469626bd3ec5bd9ddd72efce31e5da33baa2eeb5d4586356cd084dda9430b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:19:43+00:00'
last_translated_at: '2026-03-13T19:40:00+09:00'
---

# BrowserEngineKit

대체 브라우저 엔진을 사용해 콘텐츠를 렌더링하는 브라우저를 만듭니다.

## 개요

웹 브라우저는 원격의, 그리고 잠재적으로 신뢰할 수 없는 서버에서 콘텐츠와 코드를 불러옵니다. 브라우저 앱은 운영 체제 리소스, 앱을 사용하는 사람의 데이터, 웹의 신뢰할 수 없는 데이터에 대한 접근을 격리하도록 설계하십시오. 브라우저 코드의 취약점이 초래하는 위험을 줄이기 위해 방어적으로 코드를 작성하십시오.

브라우저 앱에서 웹 콘텐츠를 렌더링하기 위해 [WKWebView](https://developer.apple.com/documentation/WebKit/WKWebView)를 사용하면, WebKit은 중요한 리소스와 데이터에 대한 접근을 격리하는 확장 기능들에 작업을 자동으로 분산합니다.

[WebKit](https://developer.apple.com/documentation/WebKit)을 사용하든, 직접 대체 브라우저 엔진을 작성하든, 다음이 필요합니다.

- 사용자의 기본 웹 브라우저로 동작하기 위한 entitlement를 요청합니다. 자세한 내용은 [Preparing your app to be the default web browser](https://developer.apple.com/documentation/Xcode/preparing-your-app-to-be-the-default-browser)를 참고하십시오.
- 웹사이트에서 설치하는 대체 배포 앱을 지원하기 위해 웹 콘텐츠 내의 [MarketplaceKitURIScheme](https://developer.apple.com/documentation/MarketplaceKit/MarketplaceKitURIScheme)을 감시합니다. 자세한 내용은 [Enabling alternative distribution app installation in a browser](https://developer.apple.com/documentation/appdistribution/enabling-alternative-distribution-app-installation-in-a-browser)를 참고하십시오.

### 멀티프로세스 브라우저 구축

앱에서 대체 브라우저 엔진을 사용하는 경우, 브라우저가 관리하는 확장 기능들로 서로 다른 구성 요소를 분리하는 안전한 브라우저 인프라를 설계해야 합니다. 확장 기능 전반의 작업을 조정하는 제한된 IPC(inter-process communication) 프로토콜을 설계하십시오. 대체 브라우저 엔진을 분리된 확장 기능으로 나누면 어느 한 프로세스의 보안 취약점이 미치는 영향을 제한할 수 있습니다.

브라우저 확장 기능 설계에 대한 자세한 내용은 [Designing your browser architecture](https://developer.apple.com/documentation/browserenginekit/designing-your-browser-architecture)를 참고하십시오. 브라우저에서 확장 기능을 사용하는 방법은 [Managing the browser extension life cycle](https://developer.apple.com/documentation/browserenginekit/managing-the-browser-extension-lifecycle)을 참고하십시오.

### 웹사이트 렌더링

브라우저 앱은 UIKit과 긴밀하게 통합함으로써 상당한 이점을 얻을 수 있습니다. 앱이 많은 저수준 사용자 인터페이스 이벤트를 처리하는 방식을 사용자화하고, 브라우저 앱이 CSS를 올바르게 렌더링하며, Javascript DOM을 제대로 조작하도록 보장할 수 있습니다. 브라우저 앱의 스크롤, drag interaction, context menu 처리를 위해 [BrowserEngineKit](https://developer.apple.com/documentation/BrowserEngineKit)의 view 클래스를 사용할 수 있습니다.

사용자 정의 텍스트 view를 UIKit 텍스트 시스템과 통합하는 방법은 [Integrating custom browser text views with UIKit](https://developer.apple.com/documentation/browserenginekit/integrating-custom-browser-text-views-with-uikit)을 참고하십시오.

브라우저 앱에서는 사용자가 웹 콘텐츠를 탐색할 때 확장 기능을 실행하여 네트워크 요청을 만들고, 웹 콘텐츠를 불러오며, 미디어를 렌더링합니다. 자세한 내용은 [Managing the browser extension life cycle](https://developer.apple.com/documentation/browserenginekit/managing-the-browser-extension-lifecycle)을 참고하십시오. 브라우저 앱과 확장 프로세스 간 통신에는 [XPC](https://developer.apple.com/documentation/XPC)를 사용하십시오. 자세한 내용은 [Using XPC to communicate with browser extensions](https://developer.apple.com/documentation/browserenginekit/using-xpc-to-communicate-with-browser-extensions)를 참고하십시오.

### 지역별 개발

대체 브라우저 엔진을 사용하는 앱을 배포하려면 개발자 계정에 필요한 entitlement를 요청하십시오. 앱이 웹 브라우저가 아니더라도 앱 내 브라우징을 위해 대체 브라우저 엔진을 포함한다면 entitlement를 요청해야 합니다.

대체 브라우저 엔진 지원은 지역에 따라 다릅니다.

:::term-list
European Union: EU에서 iOS 또는 iPadOS 앱용 entitlement를 요청하려면 [Using alternative browser engines in the European Union](https://developer.apple.com/support/alternative-browser-engines)를 참고하십시오.
Japan: 일본에서 iOS 앱용 entitlement를 요청하려면 [Using alternative browser engines in Japan](https://developer.apple.com/support/alternative-browser-engines-jp)을 참고하십시오. 또한 앱은 [com.apple.security.hardened-process.checked-allocations](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.checked-allocations) entitlement를 채택해야 합니다. 브라우저가 아닌 앱에서는 소유권이 있는 대체 브라우저 엔진만 포함할 수 있습니다. 자세한 내용은 [Embedded Browser Engine Association Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.embedded-web-browser-engine.engine-association)를 참고하십시오.
:::

:::topic-grid
## 핵심 사항
- [Developing a browser app that uses an alternative browser engine](https://developer.apple.com/documentation/browserenginekit/developing-a-browser-app-that-uses-an-alternative-browser-engine): 웹 브라우저 앱과 관련 확장 기능을 만듭니다.
- [Designing your browser architecture](https://developer.apple.com/documentation/browserenginekit/designing-your-browser-architecture): 운영 체제 리소스와 개인 데이터를 신뢰할 수 없는 코드로부터 격리합니다.
- [Preparing your app to be the default web browser](https://developer.apple.com/documentation/Xcode/preparing-your-app-to-be-the-default-browser): 사용자가 Safari 대신 기기의 기본 브라우저로 앱을 설정할 수 있도록 브라우저 앱을 구성합니다.
:::

:::topic-grid
## 브라우저 확장 기능
- [Creating browser extensions in Xcode](https://developer.apple.com/documentation/browserenginekit/creating-browser-extensions-in-xcode): 대체 브라우저 엔진을 지원하도록 Xcode 프로젝트를 구성합니다.
- [Extension lifecycle](https://developer.apple.com/documentation/browserenginekit/extension-lifecycle): 브라우저 확장 기능을 실행하고, 통신하고, 무효화합니다.
- [Extension resources](https://developer.apple.com/documentation/browserenginekit/extension-resources): 브라우저 확장 기능에서 파일과 메모리 접근을 제어합니다.
:::

:::topic-grid
## 웹 콘텐츠
- [View coordination](https://developer.apple.com/documentation/browserenginekit/view-coordination): 확장 기능이 렌더링한 콘텐츠를 브라우저 UI에 표시합니다.
- [Text interaction](https://developer.apple.com/documentation/browserenginekit/text-interaction): 웹 브라우저 엔진을 텍스트 시스템과 비동기적으로 통합합니다.
- [BEWebAppManifest](https://developer.apple.com/documentation/browserenginekit/bewebappmanifest): 웹 앱 manifest를 나타내는 객체입니다.
:::

:::topic-grid
## 스크롤 view 상호 작용
- [BEScrollView](https://developer.apple.com/documentation/browserenginekit/bescrollview): delegate와 함께 작동하여 중첩을 처리하고 스크롤 상호 작용을 사용자화하는 scroll view입니다.
- [BEScrollViewScrollUpdate](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate): scroll view의 스크롤 상태 변화를 나타내는 객체입니다.
- [BEScrollViewDelegate](https://developer.apple.com/documentation/browserenginekit/bescrollviewdelegate): 브라우저 scroll view delegate가 따르는 프로토콜입니다.
:::

:::topic-grid
## Drag 상호 작용
- [BEDragInteraction](https://developer.apple.com/documentation/browserenginekit/bedraginteraction): 비동기 준비와 동작을 가능하게 하는 브라우저 전용 기능을 가진 subclass입니다.
- [BEDragInteractionDelegate](https://developer.apple.com/documentation/browserenginekit/bedraginteractiondelegate): drag interaction delegate가 따르는 프로토콜입니다.
:::

:::topic-grid
## 컨텍스트 메뉴
- [BEContextMenuConfiguration](https://developer.apple.com/documentation/browserenginekit/becontextmenuconfiguration): 컨텍스트 메뉴 제스처가 처음 인식되었을 때 메뉴 표시 여부가 즉시 결정되지 않은 상황에서 컨텍스트 메뉴 표시를 지연하는 특수 객체입니다.
:::

:::topic-grid
## 접근성
- [BEAccessibilityTextMarkerSupport](https://developer.apple.com/documentation/browserenginekit/beaccessibilitytextmarkersupport): 보조 기능 지원을 위해 텍스트 오프셋 정보를 제공하는 메서드 집합입니다.
- [valueChangedNotification](https://developer.apple.com/documentation/browserenginekit/beaccessibility/valuechangednotification): 요소의 값이 변경되었을 때 게시하는 알림입니다.
- [selectionChangedNotification](https://developer.apple.com/documentation/browserenginekit/beaccessibility/selectionchangednotification): 요소 내부 선택이 변경되었을 때 게시하는 알림입니다.
- [BEAccessibilityContainerType](https://developer.apple.com/documentation/browserenginekit/beaccessibilitycontainertype): 요소가 위치한 컨테이너의 유형을 나타내는 열거형입니다.
- [BEAccessibilityPressedState](https://developer.apple.com/documentation/browserenginekit/beaccessibilitypressedstate): 요소가 눌린 상태인지를 나타내는 열거형입니다.
- [menuItem](https://developer.apple.com/documentation/browserenginekit/beaccessibility/menuitem): 접근성 요소가 메뉴 항목처럼 동작합니다.
- [popUpButton](https://developer.apple.com/documentation/browserenginekit/beaccessibility/popupbutton): 접근성 요소가 팝업 버튼처럼 동작합니다.
- [radioButton](https://developer.apple.com/documentation/browserenginekit/beaccessibility/radiobutton): 접근성 요소가 라디오 버튼처럼 동작합니다.
- [readOnly](https://developer.apple.com/documentation/browserenginekit/beaccessibility/readonly): 접근성 요소가 읽기 전용입니다.
- [visited](https://developer.apple.com/documentation/browserenginekit/beaccessibility/visited): 접근성 요소가 이전에 방문한 링크처럼 동작합니다.
:::

:::topic-grid
## Just-in-time 코드 컴파일
- [Protecting code compiled just in time](https://developer.apple.com/documentation/browserenginekit/protecting-code-compiled-just-in-time): 메모리를 쓰기 가능 상태와 실행 가능 상태 사이에서 전환합니다.
- [Improving control flow integrity with pointer authentication](https://developer.apple.com/documentation/Apple-Silicon/improving-control-flow-integrity-with-pointer-authentication): 코드가 포인터를 올바르게 사용한다는 신뢰도를 높입니다.
- [BE_JIT_WRITE_PROTECT_TAG](https://developer.apple.com/documentation/BrowserEngineCore/BE_JIT_WRITE_PROTECT_TAG): 시스템이 just-in-time 컴파일용 포인터 인증 코드를 생성할 때 사용하는 discriminator 값입니다.
:::

:::topic-grid
## 다운로드
- [Downloading files in a web browser with an alternative browser engine](https://developer.apple.com/documentation/browserenginekit/downloading-files-in-a-web-browser): 다운로드 진행 상황을 시스템에 보고해 네트워킹 확장이 계속 활성 상태를 유지하도록 합니다.
- [BEDownloadMonitor](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls): 웹 다운로드 상태를 시스템에 보고하는 객체입니다.
:::

:::topic-grid
## 클래스
- [BEAccessibilityRemoteElement](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremoteelement)
- [BEAccessibilityRemoteHostElement](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremotehostelement)
- [BEMediaEnvironment](https://developer.apple.com/documentation/browserenginekit/bemediaenvironment-15xci)
- [BEProcessCapability](https://developer.apple.com/documentation/browserenginekit/beprocesscapability-76ijx)
- [BEWebContentFilter](https://developer.apple.com/documentation/browserenginekit/bewebcontentfilter): 웹 콘텐츠 필터를 나타내는 객체입니다.
:::

:::topic-grid
## 프로토콜
- [BEExtensionProcess](https://developer.apple.com/documentation/browserenginekit/beextensionprocess)
:::

:::topic-grid
## 구조체
- [BEAccessibility](https://developer.apple.com/documentation/browserenginekit/beaccessibility)
:::

:::topic-grid
## 열거형
- [RenderingExtensionFeature](https://developer.apple.com/documentation/browserenginekit/renderingextensionfeature)
:::
