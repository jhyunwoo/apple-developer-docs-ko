---
route: /documentation/tvmljs
source_url: https://developer.apple.com/documentation/tvmljs
source_locale: en-US
section: docc
content_type: symbol
title: TVMLKit JS
original_title: TVMLKit JS
source_hash: 9bc8820f675d6bff0e2e1fbfb6592a97f5b16515fe6ecb4883dae29067aa701a
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:55+00:00'
last_translated_at: '2026-03-13T18:10:00+09:00'
---

# TVMLKit JS

웹 기술을 사용해 미디어를 스트리밍하고 이벤트에 응답하는 tvOS 클라이언트-서버 앱을 생성합니다.

## 개요

TVMLKit JS 프레임워크는 Apple TV Markup Language(TVML)로 만든 클라이언트-서버 앱을 tvOS에서 표시할 수 있는 수단을 제공합니다. 이 프레임워크의 다른 클래스를 사용해 미디어를 스트리밍하고 이벤트에 응답할 수 있습니다.

TVMLKit JS 프레임워크는 다음과 같은 표준 Document Object Module 클래스를 포함하며, 이 문서에서는 이를 별도로 설명하지 않습니다. 이러한 클래스에 대한 정보는 [World Wide Web Consortium](https://www.w3.org/TR/2004/REC-DOM-Level-3-Core-20040407/core.html#Node3-textContent)을 참고하십시오.

- CharacterData
- Comment
- CustomEvent
- Document
- DocumentFragment
- DOMException
- DOMImplementation
- DOMImplementationLS
- DOMImplementationRegistry
- DOMParser
- Element
- Event
- EventException
- HTMLCollection
- LSException
- LSInput
- LSParser
- LSSerializer
- NamedNodeMap
- Node
- NodeList
- ParentNode
- ParsingElement
- Text
- XMLSerializer
- XPathEvaluator
- XPathException
- XPathExpression
- XPathResult

:::topic-grid
## 필수 항목
- [Creating a Client-Server TVML App](https://developer.apple.com/documentation/tvmljs/creating_a_client-server_tvml_app): 원격 서버에서 정보를 가져오고 파싱하여 Apple TV에서 TVML 문서를 표시하고 그 사이를 탐색합니다.
:::

:::topic-grid
## 앱 초기화
- [App](https://developer.apple.com/documentation/tvmljs/app): 앱 수명 주기 이벤트에 접근하고 응답할 수 있는 수단을 제공하는 객체입니다.
- [UserDefaults](https://developer.apple.com/documentation/tvmljs/userdefaults): 앱의 기본 환경설정을 담고 있는 객체입니다.
- [NavigationDocument](https://developer.apple.com/documentation/tvmljs/navigationdocument): 클라이언트-서버 앱을 위한 개별 TVML 문서를 담는 문서 스택입니다.
- [Responding to User Interaction](https://developer.apple.com/documentation/tvmljs/responding_to_user_interaction): Apple TV 앱에 이벤트 리스너를 추가해 화면의 정보를 업데이트합니다.
- [EventListenerObject](https://developer.apple.com/documentation/tvmljs/eventlistenerobject): 이벤트를 전달하고 다른 객체가 자신을 리스너로 추가할 수 있게 하는 객체입니다.
:::

:::topic-grid
## 기기 설정
- [Device](https://developer.apple.com/documentation/tvmljs/device): Apple TV와 그 기기에 설치된 호스트 앱에 대한 정보를 제공하는 객체입니다.
- [Settings](https://developer.apple.com/documentation/tvmljs/settings): 기기의 설정 정보에 접근할 수 있게 해 주는 객체입니다.
- [Restrictions](https://developer.apple.com/documentation/tvmljs/restrictions): 시청 등급 제한 정보를 가져오는 데 사용하는 객체입니다.
:::

:::topic-grid
## 미디어 재생
- [Playing Media in a Client-Server App](https://developer.apple.com/documentation/tvmljs/playing_media_in_a_client-server_app): TVMLKit JS의 내장 미디어 플레이어를 사용해 클라이언트-서버 앱에서 미디어 항목을 재생합니다.
- [Player](https://developer.apple.com/documentation/tvmljs/player): Apple TV 클라이언트-서버 앱에서 비디오와 오디오를 재생하는 UI를 표시하는 미디어 플레이어입니다.
- [Playlist](https://developer.apple.com/documentation/tvmljs/playlist): Apple TV 클라이언트-서버 앱에서 재생할 미디어 항목 배열입니다.
- [MediaItem](https://developer.apple.com/documentation/tvmljs/mediaitem): 단일 오디오 또는 비디오 항목입니다.
- [Slideshow](https://developer.apple.com/documentation/tvmljs/slideshow): Apple TV에서 이미지를 슬라이드쇼 형식으로 표시하는 데 사용하는 객체입니다.
- [Browser](https://developer.apple.com/documentation/tvmljs/browser): 탐색 가능한 전체 화면 보기를 구성하고 표시하는 데 사용하는 객체입니다.
:::

:::topic-grid
## 요소 접근
- [Keyboard](https://developer.apple.com/documentation/tvmljs/keyboard): 검색 필드와 텍스트 필드에서 사용자 입력을 가져오는 데 사용하는 객체입니다.
- [MenuBarDocument](https://developer.apple.com/documentation/tvmljs/menubardocument): 메뉴 항목과 연결된 문서를 설정하고 가져오는 데 사용하는 객체입니다.
:::

:::topic-grid
## 데이터 저장 및 가져오기
- [Binding JSON data to TVML documents](https://developer.apple.com/documentation/tvmljs/binding_json_data_to_tvml_documents): 단순화된 TVML 파일에서 데이터 바인딩과 쿼리를 사용해 완전한 TVML 문서를 생성합니다.
- [XMLHttpRequest](https://developer.apple.com/documentation/tvmljs/xmlhttprequest): URL에서 데이터를 가져오는 데 사용하는 객체입니다.
- [DataItem](https://developer.apple.com/documentation/tvmljs/dataitem): JSON 객체로부터 데이터 바인딩용 관찰 가능한 객체를 생성하는 데 사용하는 객체입니다.
- [Storage](https://developer.apple.com/documentation/tvmljs/storage): 키-값 쌍 정보를 저장하는 데 사용하는 객체입니다.
- [DataSource](https://developer.apple.com/documentation/tvmljs/datasource): 시스템이 데이터의 변화를 감지하고 대응할 수 있게 해 주는 인터페이스입니다.
- [LoadIndexesRequest](https://developer.apple.com/documentation/tvmljs/loadindexesrequest): 해당 이벤트가 트리거될 때 생성되는 요청입니다.
:::

:::topic-grid
## 오류
- [TVError](https://developer.apple.com/documentation/tvmljs/tverror): TVError 도메인의 오류 코드입니다.
- [NSError](https://developer.apple.com/documentation/tvmljs/nserror): 도메인, 도메인별 오류 코드, 애플리케이션별 정보를 포함하는 오류 상태 정보입니다.
:::

:::topic-grid
## 참고 자료
- [TVMLKit JS Functions](https://developer.apple.com/documentation/tvmljs/tvmlkit_js_functions): 이 레퍼런스에 포함된 함수는 앱 전역에서 사용할 수 있습니다. 특정 클래스에 속하지 않습니다.
:::

:::topic-grid
## 클래스
- [DOMException](https://developer.apple.com/documentation/tvmljs/domexception)
- [DOMImplementationLS](https://developer.apple.com/documentation/tvmljs/domimplementationls)
- [DOMImplementationRegistry](https://developer.apple.com/documentation/tvmljs/domimplementationregistry)
- [EventException](https://developer.apple.com/documentation/tvmljs/eventexception)
- [LSException](https://developer.apple.com/documentation/tvmljs/lsexception)
- [LSInput](https://developer.apple.com/documentation/tvmljs/lsinput)
- [LSParser](https://developer.apple.com/documentation/tvmljs/lsparser)
- [LSSerializer](https://developer.apple.com/documentation/tvmljs/lsserializer)
- [ParsingElement](https://developer.apple.com/documentation/tvmljs/parsingelement)
- [ViewModelLink](https://developer.apple.com/documentation/tvmljs/viewmodellink)
- [XPathException](https://developer.apple.com/documentation/tvmljs/xpathexception)
:::
