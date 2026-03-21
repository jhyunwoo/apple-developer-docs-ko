---
route: /documentation/PaperKit
source_url: https://developer.apple.com/documentation/PaperKit
source_locale: en-US
section: docc
content_type: symbol
title: PaperKit
original_title: PaperKit
source_hash: 0b4f40f58e593c0257584b4852a2cb9562689162387fd2b5bee9d143ffce2e9d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:57+00:00'
last_translated_at: '2026-03-13T18:25:00+09:00'
---

# PaperKit

드로잉, 도형, 일관된 마크업 경험을 앱에 추가합니다.

## 개요

PaperKit은 [PencilKit](https://developer.apple.com/documentation/PencilKit) 위에 구축되어 포괄적인 마크업 경험을 제공합니다. 도형, 이미지, 텍스트 상자 등을 포함한 요소 레이어를 추가하여 드로잉과 주석 작성을 모두 지원하는 통합 캔버스를 만들 수 있게 도와줍니다. PaperKit은 모든 Apple 플랫폼에서 마크업 경험을 구동하며, 어떤 앱에도 풍부한 마크업 기능을 쉽게 추가할 수 있는 방법을 제공합니다.

PaperKit은 완전한 마크업 경험을 제공하기 위해 함께 동작하는 세 가지 주요 구성 요소로 이루어집니다. [PaperMarkupViewController](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller)는 PencilKit 콘텐츠와 함께 PaperKit 요소를 대화형으로 생성하고 표시하는 기본 마크업 컨트롤러 역할을 합니다. [PaperMarkup](https://developer.apple.com/documentation/paperkit/papermarkup)은 마크업 요소와 PencilKit 드로잉 데이터를 모두 저장, 로드, 렌더링하는 데이터 모델 컨테이너 역할을 합니다. [MarkupEditViewController](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller)(iOS, iPadOS, visionOS)와 [MarkupToolbarViewController](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller)(macOS)는 마크업 요소를 추가하기 위한 플랫폼별 삽입 메뉴를 제공합니다.

[FeatureSet](https://developer.apple.com/documentation/paperkit/featureset)을 제공하여 어떤 마크업 도구와 기능을 사용할 수 있을지 제어하면 앱의 구체적인 요구 사항에 맞게 PaperKit을 구성할 수 있습니다. HDR 지원을 활성화해 시각적으로 뛰어난 콘텐츠를 만들고, 사용자 정의 배경 view를 설정하며, 마크업 경험을 앱의 디자인과 기능에 완벽하게 맞도록 세밀하게 조정할 수 있습니다.

:::topic-grid
## 핵심 사항
- [Integrating PaperKit into your app](https://developer.apple.com/documentation/paperkit/getting-started-with-paperkit): view controller를 설정하고, 마크업 편집 도구를 추가하며, 데이터 영속성을 구현해 첫 번째 마크업 경험을 만듭니다.
:::

:::topic-grid
## View controller
- [PaperMarkupViewController](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller): 대화형으로 마크업을 생성하고 표시하는 view controller입니다.
- [MarkupEditViewController](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller): 캔버스에 콘텐츠를 삽입하는 인터페이스를 관리하는 view controller입니다.
- [MarkupToolbarViewController](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller)
:::

:::topic-grid
## 구성
- [FeatureSet](https://developer.apple.com/documentation/paperkit/featureset): PaperKit UI 및 데이터 모델이 지원하는 기능입니다.
- [ShapeConfiguration](https://developer.apple.com/documentation/paperkit/shapeconfiguration): 도형의 모양을 지정하는 구성입니다.
- [RenderingOptions](https://developer.apple.com/documentation/paperkit/renderingoptions): 종이 데이터 모델을 그릴 때의 렌더링 옵션입니다.
:::

:::topic-grid
## 데이터 모델
- [PaperMarkup](https://developer.apple.com/documentation/paperkit/papermarkup): 에서 생성한 마크업 데이터를 저장하기 위한 데이터 모델 객체입니다.
:::

:::topic-grid
## 오류 처리
- [MarkupError](https://developer.apple.com/documentation/paperkit/markuperror): 데이터 모델을 인코딩하거나 디코딩할 때 발생하는 오류입니다.
:::
