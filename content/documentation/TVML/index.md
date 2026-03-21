---
route: /documentation/TVML
source_url: https://developer.apple.com/documentation/TVML
source_locale: en-US
section: docc
content_type: article
title: TVML
original_title: TVML
source_hash: 9781c4b15f8f90d3af0e1bf5f6b7810ebaf79a1056960d1187032edb2266d8a7
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:49:10+00:00'
last_translated_at: '2026-03-14T02:20:00+09:00'
---

# TVML

Apple TV Markup Language를 사용해 client-server 앱 내부의 개별 페이지를 생성합니다.

:::note Deprecated
TVML은 tvOS 18 및 이후 버전에서 deprecated되었습니다. 대신 [SwiftUI](https://developer.apple.com/documentation/SwiftUI) 또는 [UIKit](https://developer.apple.com/documentation/UIKit)으로 tvOS 앱을 개발하십시오.
:::

## 개요

client-server 앱의 모든 페이지는 Apple TV Markup Language(TVML) 템플릿 위에 구축됩니다. TVML 템플릿은 어떤 요소를 어떤 순서로 사용할 수 있는지를 정의합니다. 각 템플릿은 정보를 특정 방식으로 표시하도록 설계되어 있습니다. 예를 들어 `loadingTemplate`은 spinner와 현재 일어나고 있는 일을 간단히 설명하는 문구를 표시하고, `ratingTemplate`은 제품의 평점을 보여 줍니다. client-server 앱의 각 페이지마다 하나의 템플릿만 포함하는 새 TVML 파일을 만듭니다. 각 템플릿 페이지는 TV 화면 전체를 차지합니다.

각 템플릿 페이지는 compound 요소와 simple 요소를 사용합니다. compound 요소는 다른 요소를 포함하고, simple 요소는 한 줄짜리 TVML로 이루어집니다. 요소에는 화면에 표시되는 정보와 이미지가 들어 있습니다.

모든 템플릿에는 기본 presentation theme가 연결되어 있습니다. `info.plist` 파일에서 [UIUserInterfaceStyle](https://developer.apple.com/documentation/UIKit/UIUserInterfaceStyle)을 설정해 앱에 특정 theme를 지정할 수 있습니다. theme는 템플릿 내부에 일관된 모양을 제공합니다.

binary 앱이 호출하는 JavaScript 파일을 통해 client-server 앱의 흐름을 제어합니다. JavaScript 파일은 TVML 페이지를 로드하고 사용자 입력에 반응할 수 있어야 합니다. 사용할 수 있는 JavaScript API에 대한 자세한 내용은 [TVMLKit JS](https://developer.apple.com/documentation/tvmljs)를 참고하십시오.

:::topic-grid
## 전체 페이지 템플릿
- [alertTemplate](https://developer.apple.com/documentation/tvml/alerttemplate): 사용자에게 중요한 정보를 표시합니다.
- [catalogTemplate](https://developer.apple.com/documentation/tvml/catalogtemplate): 페이지 한쪽에는 항목 그룹을, 다른 쪽에는 해당 그룹 콘텐츠의 이미지를 표시합니다.
- [compilationTemplate](https://developer.apple.com/documentation/tvml/compilationtemplate): 단일 미디어 항목과 그 구성 요소에 대한 정보를 표시합니다.
- [descriptiveAlertTemplate](https://developer.apple.com/documentation/tvml/descriptivealerttemplate): 많은 양의 중요한 정보를 사용자에게 표시합니다.
- [divTemplate](https://developer.apple.com/documentation/tvml/divtemplate): 다른 템플릿이 정의한 레이아웃에 맞지 않는 페이지를 만들 수 있게 합니다.
- [formTemplate](https://developer.apple.com/documentation/tvml/formtemplate): 사용자에게서 정보를 수집할 수 있게 합니다.
- [listTemplate](https://developer.apple.com/documentation/tvml/listtemplate): 페이지 한쪽에는 항목 목록을, 다른 쪽에는 대응하는 이미지를 표시합니다.
- [loadingTemplate](https://developer.apple.com/documentation/tvml/loadingtemplate): 화면에 spinner와 설명을 표시합니다.
- [mainTemplate](https://developer.apple.com/documentation/tvml/maintemplate): 미디어 항목에 대한 사용자 옵션을 표시합니다.
- [menuBarTemplate](https://developer.apple.com/documentation/tvml/menubartemplate): 상단에 항목을 두고 그 아래에 관련 정보를 표시하는 페이지를 만듭니다.
- [oneupTemplate](https://developer.apple.com/documentation/tvml/oneuptemplate): 사용자가 전체 화면 이미지를 오가며 탐색할 수 있는 페이지를 만듭니다.
- [paradeTemplate](https://developer.apple.com/documentation/tvml/paradetemplate): 페이지 한쪽에는 항목 그룹을, 다른 쪽에는 스크롤되는 이미지를 표시합니다.
- [productBundleTemplate](https://developer.apple.com/documentation/tvml/productbundletemplate): 관련된 미디어 항목 그룹에 대한 정보를 표시합니다.
- [productTemplate](https://developer.apple.com/documentation/tvml/producttemplate): 단일 제품에 대한 자세한 정보를 표시합니다.
- [ratingTemplate](https://developer.apple.com/documentation/tvml/ratingtemplate): 항목의 평점을 표시합니다.
- [searchTemplate](https://developer.apple.com/documentation/tvml/searchtemplate): 사용자 입력을 기준으로 미디어 항목을 검색합니다.
- [showcaseTemplate](https://developer.apple.com/documentation/tvml/showcasetemplate): 사용자가 사이를 이동할 수 있는 이미지를 표시합니다.
- [stackTemplate](https://developer.apple.com/documentation/tvml/stacktemplate): 제품 그룹을 표시합니다.
- [Displaying a Product or Bundle in a Full-Page Template](https://developer.apple.com/documentation/tvml/displaying-a-product-or-bundle-in-a-full-page-template): 제품 페이지에서 스크롤 가능한 영역과 고정 영역을 지정합니다.
:::

:::topic-grid
## 복합 요소
- [Background Elements](https://developer.apple.com/documentation/tvml/background-elements): 배경 이미지와 배경에서 재생되는 미디어 항목을 제어합니다.
- [Banner and Header Elements](https://developer.apple.com/documentation/tvml/banner-and-header-elements): 다른 요소를 위한 초기 설명 정보를 제공합니다.
- [Information Elements](https://developer.apple.com/documentation/tvml/information-elements): 정보에 가장 적합한 형태로 콘텐츠를 그룹화하고 표시합니다.
- [Layout Elements](https://developer.apple.com/documentation/tvml/layout-elements): 여러 요소를 구조화된 레이아웃으로 배치하고 표시합니다.
- [Lockup Elements](https://developer.apple.com/documentation/tvml/lockup-elements): 여러 요소를 결합해 하나의 요소처럼 다룰 수 있게 합니다.
:::

:::topic-grid
## 단순 요소
- [Display Elements](https://developer.apple.com/documentation/tvml/display-elements): 이미지, badge, 진행 오버레이 같은 시각 요소를 표시합니다.
- [Multimedia Elements](https://developer.apple.com/documentation/tvml/multimedia-elements): 오디오를 스트리밍하고 서버에 저장된 정보를 검색할 수 있게 합니다.
- [Text Elements](https://developer.apple.com/documentation/tvml/text-elements): 화면에 텍스트를 표시합니다.
:::

:::topic-grid
## 스타일
- [Color Styles](https://developer.apple.com/documentation/tvml/color-styles): 요소의 색상을 사용자화할 수 있게 합니다.
- [Text Styles](https://developer.apple.com/documentation/tvml/text-styles): 요소의 텍스트 특성을 변경합니다.
- [Element Shaping](https://developer.apple.com/documentation/tvml/element-shaping): 요소의 크기와 모양을 수정합니다.
- [Element Alignment and Spacing](https://developer.apple.com/documentation/tvml/element-alignment-and-spacing): 요소의 정렬과 요소 사이의 간격을 수정합니다.
- [tv-placeholder](https://developer.apple.com/documentation/tvml/tv-placeholder): 요소의 기본 이미지를 설정합니다.
- [tv-rating-style](https://developer.apple.com/documentation/tvml/tv-rating-style): 제품 평점에 표시할 이미지를 설정합니다.
- [tv-transition](https://developer.apple.com/documentation/tvml/tv-transition): 요소가 화면에 나타나고 사라지는 방식을 지정합니다.
- [tv-text-highlight-style](https://developer.apple.com/documentation/tvml/tv-text-highlight-style): 요소가 포커스를 받을 때의 모양을 지정합니다.
- [tv-scrollable-bounds-inset](https://developer.apple.com/documentation/tvml/tv-scrollable-bounds-inset): stack 템플릿의 위와 아래에 지정한 크기의 비스크롤 영역을 만듭니다.
:::

:::topic-grid
## 속성
- [Image Attributes](https://developer.apple.com/documentation/tvml/image-attributes): 서버에서 이미지를 가져오고 요소 안에 어떻게 맞출지 지정합니다.
- [Text Attributes](https://developer.apple.com/documentation/tvml/text-attributes): 텍스트가 표시되고 입력되며 배치되는 방식을 수정합니다.
- [Focus Attributes](https://developer.apple.com/documentation/tvml/focus-attributes): 요소가 포커스를 받을 때 어떻게 동작하는지 정의합니다.
- [Binding and DOM Manipulation](https://developer.apple.com/documentation/tvml/binding-and-dom-manipulation): binding을 구현하고 DOM 조작 옵션을 향상합니다.
- [Inline Playback](https://developer.apple.com/documentation/tvml/inline-playback): inline playback이 언제, 어떻게 시작되는지 설정합니다.
- [Alignment, Scrolling, and Coloring](https://developer.apple.com/documentation/tvml/alignment-scrolling-and-coloring): shelf 안에서 요소를 정렬하고, 앱이 스크롤에 반응하는 방식을 설정하며, 앱의 전체 색상 구성을 설정합니다.
:::

:::topic-grid
## 쿼리
- [Media Queries](https://developer.apple.com/documentation/tvml/media-queries): 사용자의 선호에 따라 페이지의 모양과 레이아웃을 변경합니다.
- [Data Binding Queries](https://developer.apple.com/documentation/tvml/data-binding-queries): JSON 파일의 값을 다른 값과 비교합니다.
:::

:::topic-grid
## 리소스 아이콘
- [Adding Resource Icons](https://developer.apple.com/documentation/tvml/adding-resource-icons): Apple이 제공하는 아이콘을 버튼과 독립 이미지로 추가합니다.
- [Button Icons](https://developer.apple.com/documentation/tvml/button-icons): 버튼의 기능을 나타내는 아이콘입니다.
- [Movie Rating Icons (United States)](https://developer.apple.com/documentation/tvml/movie-rating-icons-united-states): 미국 영화 등급과 관련된 아이콘입니다.
- [Television Rating Icons (United States)](https://developer.apple.com/documentation/tvml/television-rating-icons-united-states): 미국 TV 등급과 관련된 아이콘입니다.
- [Rating Icons (New Zealand)](https://developer.apple.com/documentation/tvml/rating-icons-new-zealand): 뉴질랜드 영화 등급과 관련된 아이콘입니다.
- [Rating Icons (United Kingdom)](https://developer.apple.com/documentation/tvml/rating-icons-united-kingdom): 영국 영화 등급과 관련된 아이콘입니다.
- [Rating Icons (Brazil)](https://developer.apple.com/documentation/tvml/rating-icons-brazil): 브라질 영화 등급과 관련된 아이콘입니다.
- [Rotten Tomatoes Rating Icons](https://developer.apple.com/documentation/tvml/rotten-tomatoes-rating-icons): Rotten Tomatoes 평점 체계와 관련된 아이콘입니다.
- [Miscellaneous Icons](https://developer.apple.com/documentation/tvml/miscellaneous-icons): 특정 범주에 속하지 않는 기타 아이콘입니다.
:::
