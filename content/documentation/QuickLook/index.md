---
route: /documentation/QuickLook
source_url: https://developer.apple.com/documentation/QuickLook
source_locale: en-US
section: docc
content_type: symbol
title: Quick Look
original_title: Quick Look
source_hash: a5cd61967909d7315c9521635111ce552aa679028b8756b7f2b8e86a75e093bd
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:19:44+00:00'
last_translated_at: '2026-03-13T19:40:00+09:00'
---

# Quick Look

앱 안에서 사용할 파일 미리보기를 만들거나, 미리보기에서 간단한 편집을 수행합니다.

## 개요

앱에서 파일을 표시할 때 파일과 그 콘텐츠를 빠르게 미리볼 수 있게 하면 사용자에게 도움이 됩니다. 예를 들어 사용자가 사진을 확대하거나 오디오 파일을 재생하도록 허용하고 싶을 수 있습니다. Quick Look 프레임워크를 사용하면 기본 상호 작용을 허용하는 일반적인 파일 타입의 미리보기를 앱에서 표시할 수 있습니다. Quick Look은 다음을 포함한 일반적인 파일 타입의 미리보기를 생성할 수 있습니다.

- iWork 및 Microsoft Office 문서
- 이미지
- Live Photo
- 텍스트 파일
- PDF
- 오디오 및 비디오 파일
- USDZ 파일 포맷을 사용하는 증강 현실 객체(iOS 및 iPadOS 전용)

iOS 기기에서 Quick Look 프레임워크는 일반적인 파일 타입의 미리보기에서 간단한 편집을 수행하는 기능도 제공합니다. 예를 들어 사용자가 이미지에 마크업을 추가할 수 있습니다. 파일에 대해 더 고급 편집을 수행하거나, 고급 재생 기능을 제공하거나, 파일 콘텐츠를 텍스트 옆에 표시하거나, 미리보기 위에 view를 추가하려면 더 저수준 API를 사용하십시오. 예를 들어 고급 비디오 재생 기능을 제공하려면 [AVPlayer](https://developer.apple.com/documentation/AVFoundation/AVPlayer)를 사용합니다.

자신의 데이터 타입에 대해서는 직접 view controller로 view를 렌더링하거나, PDF나 HTML 같은 지원되는 미리보기 포맷을 반환하여 미리보기를 제공할 수 있습니다.

:::note 참고
지원되는 일반 파일 타입 목록은 운영 체제 릴리스마다 달라질 수 있습니다.
:::

### 자신의 데이터 타입에 Quick Look 미리보기 제공

자신의 파일 타입에 대한 Quick Look 미리보기를 제공하려면 view controller 기반 또는 데이터 기반 미리보기 중 하나를 사용하는 Quick Look preview extension을 만드십시오. 두 경우 모두 확장의 `Info.plist` 파일에 있는 `QLSupportedContentTypes` 배열에 지원하는 콘텐츠 타입을 추가하십시오.

view controller 기반 preview extension을 제공하려면 [QLPreviewingController](https://developer.apple.com/documentation/QuickLookUI/QLPreviewingController)를 따르는 [UIViewController](https://developer.apple.com/documentation/UIKit/UIViewController)를 설정하십시오. [preparePreviewOfFile(at:completionHandler:)](https://developer.apple.com/documentation/QuickLookUI/QLPreviewingController/preparePreviewOfFile(at:completionHandler:)) 메서드 안에서 view를 준비하고 표시합니다.

데이터 기반 preview extension을 제공하려면 시스템이 제공하는 [QLFilePreviewRequest](https://developer.apple.com/documentation/QuickLookUI/QLFilePreviewRequest)를 바탕으로 [QLPreviewReply](https://developer.apple.com/documentation/QuickLookUI/QLPreviewReply)를 제공하도록 [QLPreviewProvider](https://developer.apple.com/documentation/QuickLookUI/QLPreviewProvider)의 subclass를 구현하십시오.

:::topic-grid
## 미리보기
- [QLPreviewController](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller): 항목 미리보기를 위한 특수 view controller입니다.
- [QLPreviewItem](https://developer.apple.com/documentation/QuickLookUI/QLPreviewItem): 애플리케이션 콘텐츠의 미리보기를 만들기 위해 구현하는 프로퍼티 집합을 정의하는 프로토콜입니다.
- [QLPreviewSceneActivationConfiguration](https://developer.apple.com/documentation/quicklook/qlpreviewsceneactivationconfiguration): 지정된 URL의 항목을 미리보기 위한 scene 구성입니다.
- [Previews or thumbnail images for macOS 10.14 or earlier](https://developer.apple.com/documentation/quicklook/previews-or-thumbnail-images-for-macos-10-14-or-earlier): 이전 macOS 버전에서 일반 파일과 사용자 정의 파일 타입의 썸네일 이미지나 미리보기를 만듭니다.
:::

:::topic-grid
## 미리보기 확장 기능
- [QLPreviewingController](https://developer.apple.com/documentation/QuickLookUI/QLPreviewingController): 파일 미리보기를 생성하는 사용자 정의 컨트롤러를 구현하기 위한 프로토콜입니다.
:::

:::topic-grid
## 데이터 기반 미리보기 확장 기능
- [QLPreviewProvider](https://developer.apple.com/documentation/QuickLookUI/QLPreviewProvider): 데이터 기반 Quick Look preview extension을 제공하기 위해 subclass하는 클래스입니다.
- [QLFilePreviewRequest](https://developer.apple.com/documentation/QuickLookUI/QLFilePreviewRequest): 미리볼 콘텐츠를 나타내는 Quick Look 미리보기 요청입니다.
- [QLPreviewReply](https://developer.apple.com/documentation/QuickLookUI/QLPreviewReply): 데이터 기반 Quick Look preview extension을 제공할 때 생성하는 클래스입니다.
- [QLPreviewReplyAttachment](https://developer.apple.com/documentation/QuickLookUI/QLPreviewReplyAttachment): 시스템이 미리보기를 표시할 때 추가 콘텐츠를 제공하는 Quick Look preview reply의 첨부 항목입니다.
:::

:::topic-grid
## 클래스
- [ARQuickLookPreviewItem](https://developer.apple.com/documentation/quicklook/arquicklookpreviewitem)
- [PreviewApplication](https://developer.apple.com/documentation/quicklook/previewapplication): 플랫폼 Quick Look 애플리케이션을 구성하고 실행하는 데 사용하는 클래스입니다.
:::

:::topic-grid
## 구조체
- [PreviewItem](https://developer.apple.com/documentation/quicklook/previewitem): preview application에서 미리볼 항목입니다.
- [PreviewSession](https://developer.apple.com/documentation/quicklook/previewsession): 기존 세션을 제어하고 현재 preview application의 이벤트를 받는 구조체입니다.
:::

:::topic-grid
## 타입 별칭
- [EditingMode](https://developer.apple.com/documentation/quicklook/editingmode)
:::
