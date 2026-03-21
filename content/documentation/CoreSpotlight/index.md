---
route: /documentation/CoreSpotlight
source_url: https://developer.apple.com/documentation/CoreSpotlight
source_locale: en-US
section: docc
content_type: symbol
title: Core Spotlight
original_title: Core Spotlight
source_hash: 71d4993cbfc0c3920b3c4633a5a7692ecdf9d2c1eb8c1fa4fc424aea73883340
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:36:24+00:00'
last_translated_at: '2026-03-14T01:03:00+09:00'
---

# Core Spotlight

앱에 검색 기능을 추가하고 콘텐츠를 인덱싱해 Spotlight와 Safari에서 찾을 수 있게 합니다.

## 개요

항목에 대한 세부 정보를 Core Spotlight 인덱스에 추가해 사용자가 앱 안의 활동과 항목에 접근할 수 있도록 도와주십시오. 이 프레임워크는 콘텐츠를 인덱스에 추가하고, 그 인덱스에서 항목을 검색하는 API를 제공합니다. 어떤 콘텐츠를 인덱싱할지 여부는 개발자가 결정하지만, 일반적으로는 사용자가 앱에서 찾을 수 있는 모든 것을 인덱싱합니다. 예를 들어 사진, 연락처, 사용자가 구매한 항목, 또는 인터페이스에서 보는 데이터를 인덱싱할 수 있습니다. 그런 다음 Core Spotlight를 사용해 인덱싱된 콘텐츠를 검색하고 앱 안에 결과를 표시할 수 있습니다.

:::important Important
Spotlight File Import extension은 macOS에서 기능을 제공하지 않습니다. macOS에서 사용자 정의 파일을 Spotlight에 노출하려면 Spotlight importer plugin을 만드십시오. 자세한 내용은 [Spotlight Importer Programming Guide](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/MDImporters.html#//apple_ref/doc/uid/TP40001267)를 참고하십시오.
:::

앱은 앱 콘텐츠를 인덱싱하고 그 인덱스를 유지할 책임이 있습니다. 앱이 실행 중일 때 콘텐츠를 인덱싱할 수도 있고, 시스템이 요청할 때 콘텐츠를 인덱싱하는 app extension을 제공할 수도 있습니다. 앱이 현재 표시하고 있지 않은 파일 및 기타 콘텐츠를 포함해, 앱이 관리하는 어떤 콘텐츠든 인덱싱할 수 있습니다. Core Spotlight로 생성한 인덱스는 기기 안에만 남으며, 해당 기기 소유자에게만 비공개입니다. 기기는 인덱싱된 데이터를 Apple과 공유하지 않으며, 사용자의 다른 기기와 동기화하지도 않습니다.

콘텐츠 인덱싱 외에도 iOS는 앱 콘텐츠를 검색 가능하게 만드는 추가 전략을 제공합니다.

- [NSUserActivity](https://developer.apple.com/documentation/Foundation/NSUserActivity)의 검색 관련 속성을 사용해 항목을 온디바이스 인덱스에 추가하고, 필요하면 공용 인덱싱 대상임을 표시할 수 있습니다. [NSUserActivity](https://developer.apple.com/documentation/Foundation/NSUserActivity)에 대한 자세한 내용은 [Index Activities and Navigation Points](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/Activities.html#//apple_ref/doc/uid/TP40016308-CH6-SW1)를 참고하십시오.
- 웹 서버의 콘텐츠를 웹 마크업으로 인덱싱해 Apple의 서버 측 인덱스에 넣을 수 있으며, 그러면 해당 데이터가 모든 iOS 사용자의 Spotlight 및 Safari 검색 결과에 표시됩니다. 자세한 내용은 [App Search Programming Guide](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/index.html)의 [Mark Up Web Content](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/WebContent.html#//apple_ref/doc/uid/TP40016308-CH8-SW1)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [Adding your app’s content to Spotlight indexes](https://developer.apple.com/documentation/corespotlight/adding-your-app-s-content-to-spotlight-indexes): 앱 콘텐츠에 대한 설명을 만들고 Spotlight 인덱스에 추가해 검색 가능하게 만듭니다.
:::

:::topic-grid
## 검색 가능한 항목
- [CSSearchableItem](https://developer.apple.com/documentation/corespotlight/cssearchableitem): 사용자가 자신의 기기에서 검색할 수 있는 앱 전용 콘텐츠의 세부 정보입니다.
- [CSSearchableItemAttributeSet](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset): 검색 가능한 항목의 상세 metadata입니다.
- [CSCustomAttributeKey](https://developer.apple.com/documentation/corespotlight/cscustomattributekey): 검색 가능한 항목의 사용자 정의 attribute와 연결된 키입니다.
- [CSLocalizedString](https://developer.apple.com/documentation/corespotlight/cslocalizedstring): 앱과 관련된 검색 결과에 현지화된 텍스트를 표시하는 객체입니다.
- [CSPerson](https://developer.apple.com/documentation/corespotlight/csperson): 검색 결과의 맥락에서 사람을 나타내는 객체입니다.
:::

:::topic-grid
## 인덱스
- [Generating summary and priority data for indexed items](https://developer.apple.com/documentation/corespotlight/generating-summary-and-priority-data-for-indexed-items): Spotlight와 Apple Intelligence를 사용해 메일, 메시지, 오디오 transcript를 요약하거나 메일과 메시지의 우선순위를 평가합니다.
- [CSSearchableIndex](https://developer.apple.com/documentation/corespotlight/cssearchableindex): 앱의 검색 가능한 콘텐츠를 위한 온디바이스 인덱스입니다.
- [CSSearchableIndexDelegate](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate): delegate 객체나 app extension이 온디바이스 인덱스와의 통신을 처리할 때 사용하는 메서드를 정의하는 프로토콜입니다.
:::

:::topic-grid
## Spotlight app extension
- [Regenerating your app’s indexes on demand](https://developer.apple.com/documentation/corespotlight/regenerating-your-app-s-indexes-on-demand): 앱의 인덱스를 유지하고 필요할 때 다시 생성하는 app extension을 만듭니다.
- [CSIndexExtensionRequestHandler](https://developer.apple.com/documentation/corespotlight/csindexextensionrequesthandler): 인덱스 유지 관리 app extension을 구현하는 인터페이스입니다.
- [CSImportExtension](https://developer.apple.com/documentation/corespotlight/csimportextension): 앱이 지원하는 파일 타입에 대한 searchable attribute를 제공하는 객체입니다.
:::

:::topic-grid
## 쿼리
- [Building a search interface for your app](https://developer.apple.com/documentation/corespotlight/building-a-search-interface-for-your-app): Spotlight 쿼리를 실행하고 추천 텍스트 완성을 제공할 수 있도록 앱에 검색 인터페이스를 추가합니다.
- [Searching for information in your app](https://developer.apple.com/documentation/corespotlight/searching-for-information-in-your-app): predicate와 filter를 사용해 앱 전용 콘텐츠를 검색하고 결과를 정제합니다.
- [CSUserQuery](https://developer.apple.com/documentation/corespotlight/csuserquery): 인터페이스에서 검색을 시작하고 추천 텍스트 완성을 제공할 때 사용하는 타입입니다.
- [CSUserQueryContext](https://developer.apple.com/documentation/corespotlight/csuserquerycontext): 사용자 쿼리에 적용할 구성 세부 사항입니다.
- [CSSearchQuery](https://developer.apple.com/documentation/corespotlight/cssearchquery): 인덱싱된 앱 콘텐츠를 프로그래밍 방식으로 검색할 때 사용하는 타입입니다.
- [CSSearchQueryContext](https://developer.apple.com/documentation/corespotlight/cssearchquerycontext): 검색 쿼리에 사용할 동작 구성입니다.
- [CSSuggestion](https://developer.apple.com/documentation/corespotlight/cssuggestion): 쿼리에서 사용할 suggestion 종류입니다.
:::

:::topic-grid
## 오류
- [CSIndexError](https://developer.apple.com/documentation/corespotlight/csindexerror): Core Spotlight가 반환하는 인덱스 오류입니다.
- [CSSearchQueryError](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror): Core Spotlight가 반환하는 검색 쿼리 오류입니다.
- [CSIndex Errors](https://developer.apple.com/documentation/corespotlight/csindex-errors): 인덱스 오류 코드와 오류 도메인입니다.
- [CSSearchQuery Errors](https://developer.apple.com/documentation/corespotlight/cssearchquery-errors): 검색 쿼리 오류 코드와 오류 도메인입니다.
:::

:::topic-grid
## 버전
- [CoreSpotlightAPIVersion](https://developer.apple.com/documentation/corespotlight/corespotlightapiversion): Core Spotlight의 API 버전 번호입니다.
:::
