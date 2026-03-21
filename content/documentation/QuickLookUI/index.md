---
route: /documentation/QuickLookUI
source_url: https://developer.apple.com/documentation/QuickLookUI
source_locale: en-US
section: docc
content_type: symbol
title: Quick Look UI
original_title: Quick Look UI
source_hash: f97a8d03fcb633ed152623a9b32296353e9638f82737ff05ccbfda8c5991fa22
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:17:43+00:00'
last_translated_at: '2026-03-13T08:34:00+00:00'
---

# Quick Look UI

macOS 앱 안에서 사용할 파일 미리보기를 생성합니다.

## 개요

앱에서 파일을 보여 줄 때 파일과 그 내용을 빠르게 미리 볼 수 있는 기능을 함께 제공하면 사용자에게 도움이 됩니다. 예를 들어 사용자가 사진을 확대하거나 오디오 파일을 재생하도록 허용하고 싶을 수 있습니다. Quick Look 프레임워크를 사용하면 기본적인 상호 작용이 가능한 일반 파일 형식의 미리보기를 macOS 앱에서 보여 줄 수 있습니다. Quick Look은 다음과 같은 일반 파일 형식의 미리보기를 생성할 수 있습니다.

- iWork 및 Microsoft Office 문서
- 이미지
- Live Photos
- 텍스트 파일
- PDF
- 오디오 및 비디오 파일

자체 데이터 타입의 미리보기도 제공할 수 있습니다. 사용자 자신의 뷰 컨트롤러로 뷰를 렌더링하거나, PDF나 HTML처럼 지원되는 미리보기 형식을 반환하는 방법을 사용할 수 있습니다.

### 데이터 타입용 Quick Look 미리보기 제공하기

자체 파일 형식에 대한 Quick Look 미리보기를 제공하려면, 뷰 컨트롤러 기반 또는 데이터 기반 미리보기를 사용하는 Quick Look Preview Extension을 만드세요. 어느 방식이든 확장 프로그램의 `Info.plist` 파일에 있는 `QLSupportedContentTypes` 배열에 지원하는 콘텐츠 타입을 추가해야 합니다.

뷰 컨트롤러 기반 미리보기 확장을 제공하려면 [QLPreviewingController](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller)를 준수하는 [NSViewController](https://developer.apple.com/documentation/AppKit/NSViewController)를 설정하세요. [preparePreviewOfFile(at:completionHandler:)](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller/preparepreviewoffile(at:completionhandler:)) 메서드 안에서 뷰를 준비하고 표시합니다.

데이터 기반 미리보기 확장을 제공하려면 [QLPreviewProvider](https://developer.apple.com/documentation/quicklookui/qlpreviewprovider)의 하위 클래스를 구현하여, 시스템이 제공하는 [QLFilePreviewRequest](https://developer.apple.com/documentation/quicklookui/qlfilepreviewrequest)를 바탕으로 [QLPreviewReply](https://developer.apple.com/documentation/quicklookui/qlpreviewreply)를 제공하세요.

:::topic-grid
## 미리보기
- [QLPreviewPanel](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel): 항목 목록의 미리보기를 표시하는 Quick Look 미리보기 패널을 구현하는 클래스입니다.
- [QLPreviewView](https://developer.apple.com/documentation/quicklookui/qlpreviewview): 뷰 계층에 임베드할 수 있는 항목의 Quick Look 미리보기입니다.
- [QLPreviewItem](https://developer.apple.com/documentation/quicklookui/qlpreviewitem): 애플리케이션 콘텐츠의 미리보기를 만들기 위해 구현하는 속성 집합을 정의하는 프로토콜입니다.
- [QLPreviewPanelDataSource](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldatasource): Quick Look 미리보기 패널이 데이터 소스 객체의 내용에 접근할 때 사용하는 프로토콜입니다.
- [QLPreviewPanelDelegate](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldelegate): Quick Look 미리보기 패널의 delegate를 위한 프로토콜입니다.
- [QLPreviewItemLoadingBlock](https://developer.apple.com/documentation/quicklookui/qlpreviewitemloadingblock): Quick Look 미리보기 항목을 로드할 때 사용하는 블록을 정의하는 타입입니다.
:::

:::topic-grid
## 미리보기 확장
- [QLPreviewingController](https://developer.apple.com/documentation/quicklookui/qlpreviewingcontroller): 파일 미리보기를 생성하는 사용자 정의 컨트롤러를 구현하기 위한 프로토콜입니다.
:::

:::topic-grid
## 데이터 기반 미리보기 확장
- [QLPreviewProvider](https://developer.apple.com/documentation/quicklookui/qlpreviewprovider): 데이터 기반 Quick Look 미리보기 확장을 제공하기 위해 하위 클래스로 구현하는 클래스입니다.
- [QLFilePreviewRequest](https://developer.apple.com/documentation/quicklookui/qlfilepreviewrequest): 미리 볼 콘텐츠를 나타내는 Quick Look 미리보기 요청입니다.
- [QLPreviewReply](https://developer.apple.com/documentation/quicklookui/qlpreviewreply): 데이터 기반 Quick Look 미리보기 확장을 제공할 때 생성하는 클래스입니다.
- [QLPreviewReplyAttachment](https://developer.apple.com/documentation/quicklookui/qlpreviewreplyattachment): 시스템이 미리보기를 표시할 수 있도록 추가 콘텐츠를 제공하는 Quick Look 미리보기 응답용 첨부 항목입니다.
:::
