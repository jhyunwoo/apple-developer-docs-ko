---
route: /documentation/professional_video_applications
source_url: https://developer.apple.com/documentation/professional_video_applications
source_locale: en-US
section: docc
content_type: symbol
title: Professional Video Applications
original_title: Professional Video Applications
source_hash: c426f35b0683ac041ea5000dde52e929a88456c3c678a8c06935d0cd42592ca4
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:21+00:00'
last_translated_at: '2026-03-13T10:02:00+00:00'
---

# Professional Video Applications

Final Cut Pro와 데이터를 교환하고, Final Cut Pro와 Motion용 효과 플러그인을 생성합니다.

## 개요

Final Cut Pro XML(FCPXML)은 비디오 제작자가 앱과 Final Cut Pro 사이에서 미디어와 메타데이터 교환을 효율화할 수 있게 해 줍니다. FCPXML을 사용해 앱에서 Final Cut Pro로 미디어와 메타데이터를 보내 편집하고, Final Cut Pro에서 렌더링된 프로젝트와 그 편집 설명, 메타데이터를 다시 앱으로 받을 수 있습니다.

앱용 workflow extension을 빌드하여 Final Cut Pro 인터페이스 안에 앱의 워크플로를 통합할 수도 있습니다. Workflow extension을 사용하면 사용자가 Final Cut Pro 인터페이스를 떠나지 않고도 앱의 워크플로에 접근할 수 있어 끊김 없는 경험을 제공합니다.

FxPlug SDK는 사용자 정의 효과 플러그인을 만들기 위한 완전한 API를 제공합니다. 플러그인은 Final Cut Pro와 Motion에 완전히 통합되므로, 비디오 편집자가 후반 작업에서 쉽게 추가할 수 있습니다.

Compressor Extension SDK에는 Compressor 앱이 기본으로 제공하지 않는 출력 파일 형식을 추가할 수 있게 하는 API가 포함되어 있습니다. 이 SDK를 사용하면 사용자 정의 출력 형식을 Compressor 앱의 설정에 통합하고, 사용자가 Final Cut Pro 프로젝트를 여러분의 사용자 정의 파일 형식으로 내보낼 수 있게 할 수 있습니다.

Final Cut Pro 개념에 대한 정보는 [What are libraries](https://support.apple.com/guide/final-cut-pro/what-are-libraries-verfdd5c590e/mac)와 [Intro to metadata in Final Cut Pro](https://support.apple.com/guide/final-cut-pro/intro-to-metadata-verc392f8885/mac)를 참고하세요.

:::topic-grid
## 효과
- [FxPlug](https://developer.apple.com/documentation/professional-video-applications/fxplug): Final Cut Pro와 Motion용 사용자 정의 효과 플러그인을 생성합니다.
- [Final Cut Pro에서 사용할 효과 템플릿 만들기](https://developer.apple.com/documentation/professional-video-applications/create-an-effect-template-for-use-in-final-cut-pro): Motion을 사용해 Final Cut Pro용 사용자 정의 필터, generator, transition을 생성합니다.
:::

:::topic-grid
## XML 데이터 교환
- [Final Cut Pro와의 콘텐츠 및 메타데이터 교환](https://developer.apple.com/documentation/professional-video-applications/content-and-metadata-exchanges-with-final-cut-pro): 편집을 위해 미디어 자산과 타임라인 시퀀스를 Final Cut Pro로 보내고, 렌더링된 미디어와 편집 결과를 앱에서 받습니다.
- [Workflow Extensions](https://developer.apple.com/documentation/professional-video-applications/workflow-extensions): 데이터 교환을 효율화하기 위해 Final Cut Pro 인터페이스 안에 앱의 워크플로를 통합합니다.
- [FCPXML Reference](https://developer.apple.com/documentation/professional-video-applications/fcpxml-reference): 앱 또는 workflow extension이 Final Cut Pro와 교환하는 데이터를 설명하는 문서를 생성합니다.
:::

:::topic-grid
## Compressor 인코더 확장
- [Encoder Extensions](https://developer.apple.com/documentation/professional-video-applications/encoder-extensions): Final Cut Pro 워크플로에 사용자 정의 출력 파일 형식을 추가합니다.
:::

:::topic-grid
## 참고 자료
- [Professional Video Applications Enumerations](https://developer.apple.com/documentation/professional-video-applications/professional-video-applications-enumerations)
- [Professional Video Applications Constants](https://developer.apple.com/documentation/professional-video-applications/professional-video-applications-constants)
- [Professional Video Applications Data Types](https://developer.apple.com/documentation/professional-video-applications/professional-video-applications-data-types)
- [Professional Video Applications Protocols](https://developer.apple.com/documentation/professional-video-applications/professional-video-applications-protocols)
:::

:::topic-grid
## 변수
- [kFxPropertyKey_ChangesOutputSize](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_changesoutputsize): 필터가 입력 크기와 다른 출력 크기를 만들 수 있는지 결정하는 키입니다.
- [kFxPropertyKey_DesiredProcessingColorInfo](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_desiredprocessingcolorinfo): 플러그인이 선형 또는 감마 보정된 색 공간에서 렌더링하는지 결정하는 키입니다.
- [kFxPropertyKey_NeedsFullBuffer](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_needsfullbuffer): 플러그인이 처리에 전체 이미지를 필요로 하여 타일 렌더링을 할 수 없는지 결정하는 키입니다.
- [kFxPropertyKey_VariesWhenParamsAreStatic](https://developer.apple.com/documentation/professional_video_applications/kfxpropertykey_varieswhenparamsarestatic): 파라미터가 동일하더라도 렌더링 결과가 달라지는지 결정하는 키입니다.
:::
