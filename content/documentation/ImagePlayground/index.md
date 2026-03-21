---
route: /documentation/ImagePlayground
source_url: https://developer.apple.com/documentation/ImagePlayground
source_locale: en-US
section: docc
content_type: symbol
title: Image Playground
original_title: Image Playground
source_hash: abb3fc676dd2cc2ca54864872c95fb02061e07324096c23f412dc49f9c1ffbb5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:02:15+00:00'
last_translated_at: '2026-03-13T21:47:00+09:00'
---

# Image Playground

설명 정보를 바탕으로 이미지를 생성하는 시스템 인터페이스를 제공합니다.

## 개요

`ImagePlayground` 프레임워크를 사용하면 시스템이 지원하는 스타일을 활용해 사용자 정의 이미지를 생성할 수 있습니다. 이미지를 생성하려면 원하는 내용을 설명하는 텍스트, 선택적 이미지, 그리고 이미지가 따르길 원하는 스타일을 지정합니다. 이 정보를 사용해 SwiftUI view에서 시스템 sheet를 표시하거나, UIKit 또는 AppKit 인터페이스에서 시스템 view controller를 표시합니다. 시스템 인터페이스는 사용자와의 모든 상호 작용을 관리하고, 성공하면 콘텐츠에 포함할 수 있는 이미지를 전달합니다. 상호 작용 없이 이미지를 생성하는 프로그래밍 방식 인터페이스도 사용할 수 있습니다.

:::topic-grid
## SwiftUI 표시
- [imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)](https://developer.apple.com/documentation/SwiftUI/View/imagePlaygroundSheet(isPresented:concept:sourceImage:onCompletion:onCancellation:)): 지정한 입력으로 이미지를 생성하는 시스템 sheet를 표시합니다.
- [imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)](https://developer.apple.com/documentation/SwiftUI/View/imagePlaygroundSheet(isPresented:concepts:sourceImage:onCompletion:onCancellation:)): 지정한 입력으로 이미지를 생성하는 시스템 sheet를 표시합니다.
- [imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)](https://developer.apple.com/documentation/SwiftUI/View/imagePlaygroundSheet(isPresented:concepts:sourceImageURL:onCompletion:onCancellation:)): 지정한 입력으로 이미지를 생성하는 시스템 sheet를 표시합니다.
:::

:::topic-grid
## UIKit 및 AppKit 표시
- [ImagePlaygroundViewController](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller): 제공된 입력으로 이미지를 생성하는 표준 시스템 인터페이스를 표시합니다.
:::

:::topic-grid
## 프로그래밍 방식 생성
- [ImageCreator](https://developer.apple.com/documentation/imageplayground/imagecreator): 지정한 설명과 스타일 정보를 바탕으로 프로그래밍 방식으로 이미지를 생성합니다.
:::

:::topic-grid
## 플랫폼 지원
- [ImagePlaygroundConcept](https://developer.apple.com/documentation/imageplayground/imageplaygroundconcept): 이미지에 포함할 콘텐츠를 지정하는 텍스트 요소입니다.
- [ImagePlaygroundStyle](https://developer.apple.com/documentation/imageplayground/imageplaygroundstyle): 생성된 이미지의 외관을 결정하는 스타일 옵션입니다.
:::

:::topic-grid
## 구조체
- [ImagePlaygroundOptions](https://developer.apple.com/documentation/imageplayground/imageplaygroundoptions): 이미지 생성에 영향을 미치는 옵션 집합을 저장하는 구조체입니다.
:::
