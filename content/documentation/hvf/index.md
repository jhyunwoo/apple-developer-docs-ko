---
route: /documentation/hvf
source_url: https://developer.apple.com/documentation/hvf
source_locale: en-US
section: docc
content_type: symbol
title: hvf
original_title: hvf
source_hash: fb5e48986c475252c778ead8f382918a667c97a67125706eb70dc2bd55edd8c1
canonical_source: manual-translation
last_crawled_at: '2026-03-13T05:20:38+00:00'
last_translated_at: '2026-03-13T05:20:38+00:00'
---

# hvf

Hierarchical Variation Font(HVF) 글리프 외곽선을 렌더링하고, 폰트 편집기 및 관련 도구를 지원합니다.

## 개요

`hvf` 라이브러리는 C 및 Swift 인터페이스를 제공합니다. C 인터페이스는 기존 폰트에서 `hvgl` 및 `hvpm` 테이블의 렌더링을 지원합니다.

Swift 인터페이스는 다음에 대한 지원을 추가합니다:

- 폰트 편집기의 데이터베이스처럼 다른 소스에서 HVF 글리프를 렌더링하기 위한 사용자 정의 로더를 작성합니다.
- 사용자 정의 로더와 동일한 코드를 사용해 `hvgl` 테이블을 빌드하는 데 필요한 데이터를 생성합니다.
- 폰트 편집기에서처럼 파트 모양과 데이터를 대화형으로 수정합니다.

:::topic-grid
## 클래스
- [HVGLPartLoader](https://developer.apple.com/documentation/hvf/hvglpartloader): 메모리에 있는 HVGL 테이블을 위한 특수 로더 객체입니다. 반드시 Double 정렬되어 있어야 하며, 일반적으로 메모리 매핑된 폰트에서 가져옵니다.
- [PartRenderer](https://developer.apple.com/documentation/hvf/partrenderer): 파트 렌더링 매개변수를 설정하고, 파트를 렌더링하고, 렌더링 결과를 진단하는 데 사용할 수 있는 객체입니다.
:::

:::topic-grid
## 프로토콜
- [CompositeWriter](https://developer.apple.com/documentation/hvf/compositewriter): 렌더링용 Composite 파트를 만들거나 HVGL 테이블을 빌드하기 위한 프로토콜입니다.
- [PartGenerator](https://developer.apple.com/documentation/hvf/partgenerator): Shape 또는 Composite 데이터를 생성하기 위한 writer 객체를 반환하는 프로토콜입니다.
- [ShapeWriter](https://developer.apple.com/documentation/hvf/shapewriter): 렌더링용 Shape 파트를 만들거나 HVGL 테이블을 빌드하기 위한 프로토콜입니다.
:::

:::topic-grid
## 구조체
- [CompositeExtremumIndex](https://developer.apple.com/documentation/hvf/compositeextremumindex): Composite 파트에서 extremum 회전 또는 이동의 인덱스입니다.
- [CompositeSubpart](https://developer.apple.com/documentation/hvf/compositesubpart): Composite 파트 안의 하위 파트입니다.
- [CompositeSubpartTranslation](https://developer.apple.com/documentation/hvf/compositesubparttranslation): Composite 파트 안의 하위 파트 이동입니다.
:::

:::topic-grid
## 변수
- [hvfLibraryVersion](https://developer.apple.com/documentation/hvf/hvflibraryversion-swift.var): HVF 라이브러리의 버전을 반환합니다.
:::

:::topic-grid
## 타입 별칭
- [CustomPartLoader](https://developer.apple.com/documentation/hvf/custompartloader): 임의의 소스에서 파트를 로드하는 클로저입니다. 첫 번째 매개변수는 파트를 고유하게 식별하는 part index이며, 이는 로더가 할당합니다. 두 번째 매개변수는 요청된 파트를 생성하기 위해 ShapeWriter 또는 CompositeWriter를 얻는 데 로더가 사용하는 PartGenerator입니다. 결과는 생성된 파트이며 PartResult로 반환됩니다.
:::

:::topic-grid
## 열거형
- [AxisExtremum](https://developer.apple.com/documentation/hvf/axisextremum): 축 안에서 어떤 extremum인지 나타냅니다.
- [PartResult](https://developer.apple.com/documentation/hvf/partresult): part loader에서 반환되는 결과입니다.
- [PointCoordinate](https://developer.apple.com/documentation/hvf/pointcoordinate): 점 안에서 어떤 좌표인지를 나타냅니다.
- [SegmentBlendType](https://developer.apple.com/documentation/hvf/segmentblendtype): 경로 세그먼트의 blend 유형입니다.
- [SegmentPoint](https://developer.apple.com/documentation/hvf/segmentpoint): 세그먼트 안에서 어떤 점인지를 나타냅니다.
:::
