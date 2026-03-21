---
route: /documentation/TVMLKit
source_url: https://developer.apple.com/documentation/TVMLKit
source_locale: en-US
section: docc
content_type: symbol
title: TVMLKit
original_title: TVMLKit
source_hash: d1b315248c39d238e165b82db09933b800e0bf6922777e93bbc2c2e1138b3575
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:15:12+00:00'
last_translated_at: '2026-03-13T19:25:00+09:00'
---

# TVMLKit

바이너리 앱에 JavaScript와 TVML 파일을 포함해 클라이언트-서버 앱을 만듭니다.

## 개요

TVMLKit 프레임워크를 사용하면 tvOS 앱 내부에서 TVMLKit JS와 TVML 파일을 평가할 수 있습니다. JavaScript 환경을 통해 TVML 요소, 스타일, view, view controller를 만들 수 있습니다.

:::topic-grid
## JavaScript 환경
- [Implementing a Hybrid TV App with TVMLKit](https://developer.apple.com/documentation/tvmlkit/implementing-a-hybrid-tv-app-with-tvmlkit): document view controller로 콘텐츠 옵션을 표시하고 TVMLKit JS로 콘텐츠를 가져와 채웁니다.
- [TVApplicationController](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontroller): JavaScript로부터 UI, navigation stack, 저장소, 이벤트 처리를 연결하는 객체입니다.
- [TVApplicationControllerContext](https://developer.apple.com/documentation/tvmlkit/tvapplicationcontrollercontext): TV application controller에 제공되는 실행 정보입니다.
:::

:::topic-grid
## View와 View Controller
- [TVViewElement](https://developer.apple.com/documentation/tvmlkit/tvviewelement): 읽기 전용 DOM 노드의 표현입니다.
- [TVInterfaceCreating](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating): view와 view controller를 만드는 데 사용하는 메서드를 정의하는 프로토콜입니다.
- [TVInterfaceFactory](https://developer.apple.com/documentation/tvmlkit/tvinterfacefactory): view와 view controller 생성을 위한 팩터리입니다.
- [TVBrowserViewController](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontroller): 탐색 가능한 전체 화면 형식으로 콘텐츠를 표시하는 view controller입니다.
- [TVDocumentViewController](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller): TVMLKit 문서를 나타내는 view controller입니다.
:::

:::topic-grid
## 사용자 정의 요소
- [TVElementFactory](https://developer.apple.com/documentation/tvmlkit/tvelementfactory): Apple TV Markup Language(TVML)를 확장하기 위해 새 요소를 등록하는 데 사용하는 객체입니다.
- [TVImageElement](https://developer.apple.com/documentation/tvmlkit/tvimageelement): 이미지 요소를 설명하는 속성을 포함한 읽기 전용 DOM 노드의 표현입니다.
- [TVTextElement](https://developer.apple.com/documentation/tvmlkit/tvtextelement): DOM 요소의 텍스트 콘텐츠입니다.
- [Creating TVML Elements](https://developer.apple.com/documentation/tvmlkit/creating-tvml-elements): 복잡하고 자주 사용하는 요소를 단순화한 사용자 정의 요소를 만들어 반복 작성하지 않도록 합니다.
:::

:::topic-grid
## 사용자 정의 스타일
- [TVViewElementStyle](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyle): view 요소에 적용되는 스타일입니다.
- [TVStyleFactory](https://developer.apple.com/documentation/tvmlkit/tvstylefactory): 사용자 정의 스타일 속성을 등록하는 데 사용하는 객체입니다.
- [TVColor](https://developer.apple.com/documentation/tvmlkit/tvcolor): 스타일에서 사용하는 색상 데이터입니다.
:::

:::topic-grid
## 사용자 정의 플레이어
- [TVMediaItem](https://developer.apple.com/documentation/tvmlkit/tvmediaitem): Apple TV JavaScript 플레이어와 연결된 단일 오디오 또는 비디오 항목입니다.
- [TVPlaylist](https://developer.apple.com/documentation/tvmlkit/tvplaylist): Apple TV JavaScript 플레이어와 연결된 미디어 항목 모음입니다.
- [TVPlayer](https://developer.apple.com/documentation/tvmlkit/tvplayer): Apple TV 클라이언트-서버 앱에서 사용하는 JavaScript 플레이어의 재생을 제어하는 사용자화 가능한 네이티브 미디어 플레이어입니다.
:::

:::topic-grid
## 오류
- [TVMLKitErrorDomain](https://developer.apple.com/documentation/tvmlkit/tvmlkiterrordomain): TVMLKit에서 오류가 발생했음을 나타냅니다.
- [TVMLKitError](https://developer.apple.com/documentation/tvmlkit/tvmlkiterror): TVMLKit 오류 도메인의 오류 코드입니다.
- [TVDocumentError](https://developer.apple.com/documentation/tvmlkit/tvdocumenterror-swift.struct)
:::

:::topic-grid
## 참고 자료
- [TVMLKit Enumerations](https://developer.apple.com/documentation/tvmlkit/tvmlkit-enumerations)
- [TVMLKit Constants](https://developer.apple.com/documentation/tvmlkit/tvmlkit-constants): 특정 클래스와 연결되지 않은 TVMLKit 프레임워크 상수를 정의하는 문서입니다.
:::
