---
route: /documentation/safari-developer-tools
source_url: https://developer.apple.com/documentation/safari-developer-tools
source_locale: en-US
section: docc
content_type: symbol
title: Safari Developer Features
original_title: Safari Developer Features
source_hash: e0f1121253a6a0b56248db5a3d9c94d87cee3ee6dfbd7352900107823a682c2f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:49:12+00:00'
last_translated_at: '2026-03-14T02:20:00+09:00'
---

# Safari Developer Features

Safari, 다른 앱, 그리고 iPhone과 iPad를 포함한 다른 기기에서 웹 콘텐츠를 검사하고 디버그하며 테스트합니다.

## 개요

Safari에는 Safari 안의 웹 콘텐츠, 다른 앱 안의 웹 콘텐츠, 그리고 iPhone, iPad, Apple Vision Pro 같은 다른 기기에서의 웹 콘텐츠를 검사, 디버그, 테스트하는 데 도움이 되는 기능과 도구가 포함되어 있습니다. 또한 JavaScript와 TVML을 검사하기 위해 Apple TV도 지원합니다.

![Mac, iPhone, iPad에 developer.apple.com이 보입니다. Mac에서는 페이지 로딩 타임라인을 보여 주는 Web Inspector도 함께 표시됩니다.](https://developer.apple.com)

macOS용 Safari의 [Web Inspector](https://developer.apple.com/documentation/safari-developer-tools/web-inspector) 같은 기능을 사용하면 스타일 변경을 시험해 보고, `grid`와 `flex` 컨테이너 레이아웃을 시각화하고, 사용자 정의 variation axis를 포함한 타이포그래피를 조정하고, 색상 구성표나 reduced motion 같은 사용자 선호를 에뮬레이션해 모든 사용자에게 콘텐츠가 훌륭하게 보이도록 할 수 있습니다. 또한 Web Inspector를 사용해 JavaScript에 breakpoint를 설정하고, 대화식으로 디버그하고, 디버깅 중인 페이지의 상태를 검사할 수 있습니다. Timelines 같은 도구는 스크립트와 레이아웃이 성능과 메모리 사용량에 미치는 영향을 시각화하고, 긴 frame time의 원인을 파악하는 데도 도움이 됩니다.

또한 [WebDriver](https://developer.apple.com/documentation/safari-developer-tools/webdriver)를 사용해 Safari에서 웹페이지 테스트를 자동화할 수 있습니다. 웹은 계속 진화하므로 웹페이지가 의도한 대로 동작하는지 지속적으로 테스트하는 것이 중요합니다. WebDriver는 플랫폼 전반의 모든 주요 브라우저가 지원하는 웹 콘텐츠 테스트 자동화용 cross-browser API이며, 브라우저별 코드를 요구하지 않습니다.

:::topic-grid
## 기초
- [Enabling features for web developers](https://developer.apple.com/documentation/safari-developer-tools/enabling-developer-features): Safari에서 웹 개발자를 위한 기능과 설정을 활성화합니다.
:::

:::topic-grid
## 도구
- [Develop menu](https://developer.apple.com/documentation/safari-developer-tools/develop-menu): Safari 안의 웹페이지 디버깅 도구와 다른 앱 및 다른 기기의 웹 콘텐츠 디버깅 도구에 접근합니다.
- [Web Inspector](https://developer.apple.com/documentation/safari-developer-tools/web-inspector): Web Inspector를 사용해 HTML, CSS, JavaScript를 검사하고 디버그합니다.
- [Responsive Design Mode](https://developer.apple.com/documentation/safari-developer-tools/responsive-design-mode): query와 기타 동적 스타일을 테스트해 어떤 화면에서도 웹페이지가 잘 보이도록 합니다.
- [Inspect Apps and Devices](https://developer.apple.com/documentation/safari-developer-tools/inspect-apps-and-devices): Mac과 연결된 기기에서 Safari 및 다른 앱의 검사 가능한 모든 웹 콘텐츠를 찾습니다.
- [WebDriver](https://developer.apple.com/documentation/safari-developer-tools/webdriver): WebDriver를 사용해 강건하고 포괄적인 테스트를 작성하고, Safari를 포함해 WebDriver 호환 드라이버가 있는 모든 브라우저에서 실행합니다.
:::

:::topic-grid
## 콘텐츠 검사
- [Inspecting Safari on macOS](https://developer.apple.com/documentation/safari-developer-tools/inspecting-safari-macos): macOS용 Safari에서 웹페이지, service worker, extension을 검사합니다.
- [Inspecting iOS and iPadOS](https://developer.apple.com/documentation/safari-developer-tools/inspecting-ios): 연결된 Mac에서 iOS 및 iPadOS 기기와 시뮬레이터의 웹페이지, service worker, 홈 화면 웹 앱, extension, 앱 내부 콘텐츠를 검사합니다.
- [Inspecting visionOS](https://developer.apple.com/documentation/safari-developer-tools/inspecting-visionos): 같은 네트워크에 있는 Mac에서 visionOS의 웹페이지, service worker, extension, 앱 내부 콘텐츠를 검사합니다.
- [Inspecting tvOS](https://developer.apple.com/documentation/safari-developer-tools/inspecting-tvos): 같은 네트워크에 있는 Mac에서 tvOS의 JavaScript 및 TVML 콘텐츠를 검사합니다.
- [Enabling inspecting content in your apps](https://developer.apple.com/documentation/safari-developer-tools/enabling-inspecting-content-in-your-apps): 연결된 Mac에서 검사할 때 개발 중인 앱의 웹페이지와 JavaScript를 검사할 수 있도록 설정합니다.
:::

:::topic-grid
## 시뮬레이터
- [Installing Xcode and Simulators](https://developer.apple.com/documentation/safari-developer-tools/installing-xcode-and-simulators): 웹 개발에 사용할 시뮬레이터를 설치합니다.
- [Adding additional simulators](https://developer.apple.com/documentation/safari-developer-tools/adding-additional-simulators): 웹 개발에 사용할 서로 다른 기기와 iOS 버전용 시뮬레이터를 추가합니다.
:::

:::topic-grid
## 설정
- [Changing Developer settings in Safari on macOS](https://developer.apple.com/documentation/safari-developer-tools/developer-settings): Safari의 동작을 바꾸는 개발자 중심 설정을 변경합니다.
- [Changing Feature Flag settings in Safari on macOS](https://developer.apple.com/documentation/safari-developer-tools/feature-flag-settings): Safari에 출시되기 전에 새로운 웹 플랫폼 기능을 테스트합니다.
:::

:::topic-grid
## AutoFill
- [Improving AutoFill experiences for your forms](https://developer.apple.com/documentation/safari-developer-tools/autofill): 잘 구조화된 표준 마크업을 사용해 웹사이트 폼에서 더 신뢰할 수 있는 AutoFill 경험을 제공합니다.
:::
