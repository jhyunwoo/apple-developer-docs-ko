---
route: /design/human-interface-guidelines/web-views
source_url: https://developer.apple.com/design/human-interface-guidelines/web-views
source_locale: ko-KR
section: hig
content_type: article
title: 웹 뷰
original_title: Web views
source_hash: 35fc7f292cc6740af7aa5af7ad43e6b97dbd5e70e226db1200f06e398fdc918f
canonical_source: official-ko
last_crawled_at: '2026-03-13T15:01:18+00:00'
last_translated_at: '2026-03-14T00:01:12+09:00'
---

# 웹 뷰

웹 뷰는 내장 HTML 및 웹사이트와 같은 풍부한 웹 콘텐츠를 앱에 직접 로드하고 표시합니다.

![스타일화된 나침반 아이콘 모양이 표시되어 있음. 여섯 가지 색상으로 된 기존 Apple 로고의 빨간색을 은은하게 반영하는 빨간색 색조가 이미지에 적용됨.](https://developer.apple.com)

예를 들어, Mail은 웹 뷰를 사용하여 메시지의 HTML 콘텐츠를 표시합니다.

## 모범 사례

**적합할 경우, 이전 및 다음 페이지 탐색을 지원하십시오.** 웹 뷰는 이전 및 다음 페이지 탐색을 지원하지만, 이 동작은 기본적으로 사용되지 않습니다. 사람들이 웹 뷰를 사용하여 여러 페이지에 방문할 가능성이 있는 경우, 이전 및 다음 페이지 탐색을 허용하고 이 기능을 실행할 해당 제어기를 제공하십시오.

**웹 뷰를 사용하여 웹 브라우저를 빌드하지 마십시오.** 웹 뷰를 사용하여 사람들이 앱의 맥락을 벗어나지 않고 웹사이트에 잠시 접근하도록 하는 것은 좋지만, 사람들이 웹을 브라우징하는 기본적인 방식은 Safari입니다. 앱에서 Safari의 기능을 복제하려는 시도는 불필요하며 권장되지 않습니다.

## 플랫폼 고려 사항

*iOS, iPadOS, macOS 또는 visionOS에 대한 추가 고려 사항은 없습니다. tvOS 또는 watchOS에서는 지원되지 않습니다.*

## 리소스

#### 관련 콘텐츠

[Webkit.org](https://webkit.org/)

#### Developer 문서

[WKWebView](https://developer.apple.com/documentation/WebKit/WKWebView) — WebKit

#### 비디오
