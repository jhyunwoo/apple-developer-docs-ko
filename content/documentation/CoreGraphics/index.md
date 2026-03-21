---
route: /documentation/CoreGraphics
source_url: https://developer.apple.com/documentation/CoreGraphics
source_locale: en-US
section: docc
content_type: symbol
title: Core Graphics
original_title: Core Graphics
source_hash: 6cf00d49840213a10355388ada731ffb4e4c6e39027671687dc8acdedc1c052f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:24:08+00:00'
last_translated_at: '2026-03-13T09:10:00+00:00'
---

# Core Graphics

Quartz 기술의 강점을 활용해 고품질 출력의 경량 2D 렌더링을 수행합니다. 경로 기반 드로잉, 안티앨리어싱 렌더링, 그라디언트, 이미지, 색상 관리, PDF 문서 등을 처리할 수 있습니다.

## 개요

Core Graphics 프레임워크는 Quartz 고급 드로잉 엔진을 기반으로 합니다. 이 프레임워크는 비교할 수 없을 만큼 높은 출력 충실도의 저수준 경량 2D 렌더링을 제공합니다. 이 프레임워크를 사용해 경로 기반 드로잉, 변환, 색상 관리, 오프스크린 렌더링, 패턴, 그라디언트와 셰이딩, 이미지 데이터 관리, 이미지 생성, 이미지 마스킹뿐 아니라 PDF 문서 생성, 표시, 파싱을 처리합니다.

macOS에서는 Core Graphics에 디스플레이 하드웨어, 저수준 사용자 입력 이벤트, 윈도잉 시스템과 함께 동작하는 서비스도 포함됩니다.

:::topic-grid
## 기하 데이터 타입
- [CGFloat](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct): Core Graphics 및 관련 프레임워크에서 사용하는 부동소수점 스칼라 값의 기본 타입입니다.
- [CGPoint](https://developer.apple.com/documentation/CoreFoundation/CGPoint)
- [CGSize](https://developer.apple.com/documentation/CoreFoundation/CGSize): 너비와 높이 값을 담는 구조체입니다.
- [CGRect](https://developer.apple.com/documentation/CoreFoundation/CGRect)
- [CGVector](https://developer.apple.com/documentation/CoreFoundation/CGVector): 2차원 벡터를 담는 구조체입니다.
- [CGAffineTransform](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform)
:::

:::topic-grid
## 2D 드로잉
- [CGContext](https://developer.apple.com/documentation/coregraphics/cgcontext): Quartz 2D 드로잉 환경입니다.
- [CGImage](https://developer.apple.com/documentation/coregraphics/cgimage): 비트맵 이미지 또는 이미지 마스크입니다.
- [CGPath](https://developer.apple.com/documentation/coregraphics/cgpath): 그래픽 컨텍스트에 그릴 도형이나 선을 수학적으로 설명하는 변경 불가능한 그래픽 경로입니다.
- [CGMutablePath](https://developer.apple.com/documentation/coregraphics/cgmutablepath): 그래픽 컨텍스트에 그릴 도형이나 선을 수학적으로 설명하는 변경 가능한 그래픽 경로입니다.
- [CGLayer](https://developer.apple.com/documentation/coregraphics/cglayer): Core Graphics로 그린 콘텐츠를 재사용하기 위한 오프스크린 컨텍스트입니다.
:::

:::topic-grid
## 색상과 글꼴
- [CGColor](https://developer.apple.com/documentation/coregraphics/cgcolor): 색을 정의하는 구성 요소 집합이며, 이를 해석하는 방법은 색 공간이 지정합니다.
- [CGColorConversionInfo](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfo): 다른 시스템 서비스에서 사용할 색 공간 간 변환 방법을 설명하는 객체입니다.
- [CGColorSpace](https://developer.apple.com/documentation/coregraphics/cgcolorspace): 표시를 위해 색 값 해석 방법을 지정하는 프로파일입니다.
- [CGFont](https://developer.apple.com/documentation/coregraphics/cgfont): 텍스트를 그리기 위한 문자 glyph 집합과 레이아웃 정보입니다.
:::

:::topic-grid
## PDF 문서 다루기
- [CGPDFDocument](https://developer.apple.com/documentation/coregraphics/cgpdfdocument): PDF(Portable Document Format) 드로잉 정보를 담는 문서입니다.
:::

:::topic-grid
## 유틸리티 및 지원 클래스
- [CGDataConsumer](https://developer.apple.com/documentation/coregraphics/cgdataconsumer): 원시 메모리 버퍼를 직접 관리할 필요 없이 데이터 쓰기 작업을 수행할 수 있게 하는 추상화입니다.
- [CGDataProvider](https://developer.apple.com/documentation/coregraphics/cgdataprovider): 원시 메모리 버퍼를 직접 관리할 필요 없이 데이터 읽기 작업을 수행할 수 있게 하는 추상화입니다.
- [CGShading](https://developer.apple.com/documentation/coregraphics/cgshading): 사용자 정의 함수로 제어되는 색상 간 부드러운 전환을 정의하여 반경 방향 및 축 방향 그라디언트 채우기를 그리는 정의입니다.
- [CGGradient](https://developer.apple.com/documentation/coregraphics/cggradient): 반경 방향 및 축 방향 그라디언트 채우기를 그리기 위한 색상 간 부드러운 전환 정의입니다.
- [CGFunction](https://developer.apple.com/documentation/coregraphics/cgfunction): 콜백 함수를 정의하고 사용하는 일반적인 기능입니다.
- [CGPattern](https://developer.apple.com/documentation/coregraphics/cgpattern): 그래픽 경로를 그릴 때 사용하는 2D 패턴입니다.
:::

:::topic-grid
## 서비스
- [Quartz Display Services](https://developer.apple.com/documentation/coregraphics/quartz-display-services): 디스플레이 하드웨어를 구성하고 제어하기 위해 macOS window server 기능에 직접 접근할 수 있게 합니다.
- [Quartz Event Services](https://developer.apple.com/documentation/coregraphics/quartz-event-services): macOS에서 저수준 사용자 입력 이벤트 스트림을 관찰하고 변경하는 필터를 관리하는 기능을 제공합니다.
- [Quartz Window Services](https://developer.apple.com/documentation/coregraphics/quartz-window-services): macOS window server가 관리하는 윈도우에 대한 정보를 제공합니다.
:::

:::topic-grid
## 참고 자료
- [Core Graphics Structures](https://developer.apple.com/documentation/coregraphics/core-graphics-structures)
- [Core Graphics Enumerations](https://developer.apple.com/documentation/coregraphics/core-graphics-enumerations)
- [Core Graphics Constants](https://developer.apple.com/documentation/coregraphics/core-graphics-constants)
- [Core Graphics Functions](https://developer.apple.com/documentation/coregraphics/core-graphics-functions)
- [Core Graphics Data Types](https://developer.apple.com/documentation/coregraphics/core-graphics-data-types)
:::

:::topic-grid
## 클래스
- [CGRenderingBufferProvider](https://developer.apple.com/documentation/coregraphics/cgrenderingbufferprovider)
:::

:::topic-grid
## 구조체
- [CGBitmapParameters](https://developer.apple.com/documentation/coregraphics/cgbitmapparameters-4v8wo)
- [CGColorModel](https://developer.apple.com/documentation/coregraphics/cgcolormodel)
- [CGContentInfo](https://developer.apple.com/documentation/coregraphics/cgcontentinfo)
:::

:::topic-grid
## 열거형
- [CGBitmapLayout](https://developer.apple.com/documentation/coregraphics/cgbitmaplayout)
- [CGComponent](https://developer.apple.com/documentation/coregraphics/cgcomponent)
- [CGContentToneMappingInfo](https://developer.apple.com/documentation/coregraphics/cgcontenttonemappinginfo-swift.enum)
- [CGImageComponentInfo](https://developer.apple.com/documentation/coregraphics/cgimagecomponentinfo)
:::
