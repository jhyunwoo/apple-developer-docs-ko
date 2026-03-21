---
route: /documentation/DeveloperToolsSupport
source_url: https://developer.apple.com/documentation/DeveloperToolsSupport
source_locale: en-US
section: docc
content_type: symbol
title: DeveloperToolsSupport
original_title: DeveloperToolsSupport
source_hash: 78f1255309692db50f6a0b18eb31e47a92636e0b1dc421cef8acc21e5a984671
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:03:24+00:00'
last_translated_at: '2026-03-13T16:25:00+09:00'
---

# DeveloperToolsSupport

Xcode 라이브러리에 사용자 정의 view와 modifier를 노출합니다.

## 개요

DeveloperToolsSupport 프레임워크를 사용하면 Xcode에 사용자 정의 SwiftUI view와 view modifier를 알려줄 수 있습니다. 뷰와 modifier를 추가하면, Xcode는 툴바의 Library 버튼(`+`)을 클릭했을 때 이들을 사용할 수 있게 합니다. 시스템이 제공하는 항목과 마찬가지로, 사용자 정의 라이브러리 항목을 선택해 코드로 드래그할 수 있습니다.

라이브러리에 항목을 추가하려면 [LibraryContentProvider](https://developer.apple.com/documentation/developertoolssupport/librarycontentprovider) 프로토콜을 준수하는 구조체를 만들고, 추가하려는 항목을 [LibraryItem](https://developer.apple.com/documentation/developertoolssupport/libraryitem) 인스턴스로 캡슐화합니다. view를 포함하는 라이브러리 항목을 추가하려면 [views](https://developer.apple.com/documentation/developertoolssupport/librarycontentprovider/views) 계산 프로퍼티를 구현합니다. view modifier를 포함하는 항목을 추가하려면 [modifiers(base:)](https://developer.apple.com/documentation/developertoolssupport/librarycontentprovider/modifiers(base:)) 메서드를 구현합니다. Xcode는 작업 중 프로젝트의 모든 library content provider에서 항목을 수집하여 라이브러리에서 사용할 수 있게 만듭니다.

:::topic-grid
## 라이브러리 사용자화
- [LibraryContentProvider](https://developer.apple.com/documentation/developertoolssupport/librarycontentprovider): Xcode 라이브러리와 코드 완성 콘텐츠의 소스입니다.
- [LibraryItem](https://developer.apple.com/documentation/developertoolssupport/libraryitem): Xcode 라이브러리에 추가할 단일 항목입니다.
:::

:::topic-grid
## 프리뷰 등록
- [PreviewRegistry](https://developer.apple.com/documentation/developertoolssupport/previewregistry): 시스템이 런타임에 preview를 찾을 때 사용하는 프로토콜입니다.
- [Preview](https://developer.apple.com/documentation/developertoolssupport/preview): preview 매크로가 preview를 생성할 때 사용하는 기본 타입입니다.
- [PreviewLayout](https://developer.apple.com/documentation/developertoolssupport/previewlayout): preview를 위한 크기 제약입니다.
- [PreviewTrait](https://developer.apple.com/documentation/developertoolssupport/previewtrait): preview에 적용할 수 있는 사용자화 항목입니다.
:::

:::topic-grid
## 리소스 정의
- [ColorResource](https://developer.apple.com/documentation/developertoolssupport/colorresource): 색상 리소스입니다.
- [ImageResource](https://developer.apple.com/documentation/developertoolssupport/imageresource): 이미지 리소스입니다.
:::

:::topic-grid
## 카메라 관리
- [PreviewCamera](https://developer.apple.com/documentation/developertoolssupport/previewcamera): preview에서 시점을 정의하는 카메라입니다.
- [PreviewCameraBuilder](https://developer.apple.com/documentation/developertoolssupport/previewcamerabuilder): 3D 장면에서 view를 미리 보기 위해 카메라 컬렉션을 조합하는 builder 타입입니다.
:::

:::topic-grid
## 구조체
- [PreviewBodyBuilder](https://developer.apple.com/documentation/developertoolssupport/previewbodybuilder): 매크로 내부의 preview body 콘텐츠를 위한 builder입니다.
- [PreviewMacroBodyBuilder](https://developer.apple.com/documentation/developertoolssupport/previewmacrobodybuilder): 매크로 내부의 preview body 콘텐츠를 위한 builder입니다.
- [PreviewUnavailable](https://developer.apple.com/documentation/developertoolssupport/previewunavailable): 런타임에 preview를 사용할 수 없을 때 시스템이 던지는 오류입니다.
:::
