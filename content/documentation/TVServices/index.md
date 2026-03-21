---
route: /documentation/TVServices
source_url: https://developer.apple.com/documentation/TVServices
source_locale: en-US
section: docc
content_type: symbol
title: TV Services
original_title: TV Services
source_hash: 19c48c8d92072ba27c2604445ff867c11b209006ff215fddd6656fb250fc7ccb
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:22:17+00:00'
last_translated_at: '2026-03-13T16:55:00+09:00'
---

# TV Services

콘텐츠와 설명을 표시하고, 채널 가이드를 제공하며, Apple TV에서 여러 사용자를 지원합니다.

## 개요

TVServices 프레임워크를 사용하면 화면에 콘텐츠를 눈에 잘 띄게 표시하고 사용자 로그인을 더 빠르게 만들 수 있습니다. 앱의 미디어와 기타 정보를 *top shelf area*에 강조해 보여 줄 수 있습니다. 예를 들어 비디오 재생 앱은 사용자가 가장 최근에 본 비디오를 표시할 수 있습니다. 사용자가 tvOS 홈 화면에서 앱을 선택하면 시스템이 미디어 항목을 표시하며, 이때 앱이 실행 중일 필요는 없습니다. tvOS 앱 번들에 포함한 Top Shelf app extension을 사용해 top shelf 콘텐츠를 제공합니다.

여러 사용자 프로필을 관리하는 앱은 각 Apple TV 사용자에 대한 프로필을 유지하여 로그인 과정을 빠르게 할 수 있습니다. Apple TV는 여러 사용자 계정을 지원하며, 이 계정은 앱이 관리하는 프로필과는 별개입니다. 시스템 계정을 자체 프로필과 매핑하면 사용자가 프로필 선택 화면을 건너뛰고 바로 자신의 콘텐츠로 이동할 수 있어 더 나은 사용자 경험을 제공합니다.

:::important Important
TVServices app extension에서 메모리를 많이 사용하는 작업을 수행하지 마십시오. app extension의 메모리 한도는 앱보다 훨씬 낮기 때문에, 메모리를 과도하게 사용하면 시스템이 extension을 종료할 수 있습니다. 대신 top shelf 콘텐츠 생성과 기타 메모리 집약적인 작업은 서버에서 수행하십시오.
:::

:::topic-grid
## Top shelf app extension
- [Building a Full Screen Top Shelf Extension](https://developer.apple.com/documentation/tvservices/building-a-full-screen-top-shelf-extension): 전체 화면 Top Shelf extension을 만들어 Apple TV 앱의 콘텐츠를 강조합니다.
- [TVTopShelfContentProvider](https://developer.apple.com/documentation/tvservices/tvtopshelfcontentprovider): tvOS 홈 화면의 top shelf 영역에 콘텐츠를 제공하기 위해 사용하는 Top Shelf app extension의 주 인터페이스입니다.
- [Legacy Extension](https://developer.apple.com/documentation/tvservices/legacy-extension): top shelf 콘텐츠와 tvOS 앱 설명을 제공해 사용자가 앱을 발견하도록 돕습니다.
:::

:::topic-grid
## 캐러셀 콘텐츠
- [TVTopShelfCarouselItem](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselitem): 캐러셀 기반 인터페이스로 표시하려는 이미지, 비디오, 기타 정보를 포함하는 항목입니다.
- [TVTopShelfCarouselContent](https://developer.apple.com/documentation/tvservices/tvtopshelfcarouselcontent): top shelf에서 캐러셀 스타일 인터페이스로 표시하는 항목 집합입니다.
:::

:::topic-grid
## 섹션 및 inset 콘텐츠
- [TVTopShelfSectionedItem](https://developer.apple.com/documentation/tvservices/tvtopshelfsectioneditem): 섹션 기반 인터페이스에 표시할 항목입니다.
- [TVTopShelfItemCollection](https://developer.apple.com/documentation/tvservices/tvtopshelfitemcollection): top shelf의 섹션 기반 인터페이스에서 함께 표시하는 항목 그룹입니다.
- [TVTopShelfSectionedContent](https://developer.apple.com/documentation/tvservices/tvtopshelfsectionedcontent): top shelf에서 섹션 기반 인터페이스로 표시할 항목 집합입니다.
- [TVTopShelfInsetContent](https://developer.apple.com/documentation/tvservices/tvtopshelfinsetcontent): top shelf에서 inset 스타일 인터페이스로 표시할 항목 집합입니다.
:::

:::topic-grid
## 다중 사용자
- [Personalizing Your App for Each User on Apple TV](https://developer.apple.com/documentation/tvservices/personalizing-your-app-for-each-user-on-apple-tv): 계정별 저장소를 사용해 다중 사용자 시스템에서 데이터를 분리합니다.
- [Supporting Multiple Users in Your tvOS App](https://developer.apple.com/documentation/tvservices/supporting-multiple-users-in-your-tvos-app): 새로운 Runs as Current User capability를 사용해 사용자별 데이터를 따로 저장합니다.
- [Mapping Apple TV users to app profiles](https://developer.apple.com/documentation/tvservices/mapping-apple-tv-users-to-app-profiles): entitlement를 사용하고 로그인 흐름을 단순화해 현재 시청자에 맞게 앱 콘텐츠를 조정합니다.
- [TVUserManager](https://developer.apple.com/documentation/tvservices/tvusermanager): 공유 기기에서 여러 사람의 환경설정을 어떻게 저장할지 나타내는 객체입니다.
:::

:::topic-grid
## 채널 가이드
- [Providing Channel Navigation](https://developer.apple.com/documentation/tvservices/providing-channel-navigation): 전자 프로그램 가이드(EPG) 탐색과 특수 리모컨 버튼을 사용한 채널 변경을 지원합니다.
- [TVUserActivityTypeBrowsingChannelGuide](https://developer.apple.com/documentation/tvservices/tvuseractivitytypebrowsingchannelguide): 앱의 채널 가이드를 보기 위한 activity입니다.
:::

:::topic-grid
## 공통 타입
- [TVTopShelfItem](https://developer.apple.com/documentation/tvservices/tvtopshelfitem): top shelf에서 영화, 쇼, 기타 콘텐츠를 이미지로 표현하는 항목입니다.
- [TVTopShelfAction](https://developer.apple.com/documentation/tvservices/tvtopshelfaction): top shelf의 항목과 상호 작용할 때 수행할 동작입니다.
- [TVTopShelfContent](https://developer.apple.com/documentation/tvservices/tvtopshelfcontent): top shelf용 콘텐츠를 제공하기 위해 객체가 채택하는 프로토콜입니다.
- [TVTopShelfObject](https://developer.apple.com/documentation/tvservices/tvtopshelfobject): top shelf 항목과 항목 모음을 설명하는 추상 기본 클래스입니다.
:::

:::topic-grid
## 변수
- [TVUserActivityTypeBrowsingEntertainmentContent](https://developer.apple.com/documentation/tvservices/tvuseractivitytypebrowsingentertainmentcontent): TV Provider 앱의 메인 화면을 여는 데 사용하는 activity type입니다.
:::
