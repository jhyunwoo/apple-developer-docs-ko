---
route: /documentation/Charts
source_url: https://developer.apple.com/documentation/Charts
source_locale: en-US
section: docc
content_type: symbol
title: Swift Charts
original_title: Swift Charts
source_hash: 484c278ff34c33fae856251968b10db3e80385971fa6caf63fd9687277198170
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:23+00:00'
last_translated_at: '2026-03-13T09:10:00+00:00'
---

# Swift Charts

모든 Apple 플랫폼에서 차트를 구성하고 사용자화합니다.

## 개요

Swift Charts는 데이터를 유익한 시각화로 바꾸는 데 사용할 수 있는 강력하고 간결한 SwiftUI 프레임워크입니다. Swift Charts를 사용하면 적은 코드로도 효과적이고 사용자화 가능한 차트를 만들 수 있습니다. 이 프레임워크는 다양한 데이터 기반 차트를 개발할 수 있도록 mark, scale, axis, legend를 조합 가능한 구성 요소로 제공합니다.

![Swift Charts로 만든 세 가지 차트인 line chart, bar chart, scatter plot을 보여 주는 그래픽입니다.](https://developer.apple.com)

Swift Charts를 사용하면 데이터의 패턴이나 추세를 전달하는 여러 방법을 활용할 수 있습니다. 위와 같이 line chart, bar chart, scatter plot을 포함한 다양한 차트를 만들 수 있습니다. 이 프레임워크로 차트를 생성하면 데이터에 맞는 scale과 axis가 자동으로 생성됩니다.

Swift Charts는 현지화와 접근성 기능을 지원합니다. chart modifier를 사용해 기본 동작을 재정의하여 차트를 사용자화할 수도 있습니다. 예를 들어 차트에 애니메이션을 추가해 동적인 경험을 만들 수 있습니다.

:::topic-grid
## 필수 항목
- [Swift Charts 업데이트](https://developer.apple.com/documentation/Updates/SwiftCharts): Swift Charts의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 차트
- [Swift Charts로 차트 생성하기](https://developer.apple.com/documentation/charts/creating-a-chart-using-swift-charts): SwiftUI에서 차트 구성 요소를 조합해 차트를 만듭니다.
- [앱의 데이터 시각화하기](https://developer.apple.com/documentation/charts/visualizing-your-app-s-data): Swift Charts를 사용해 복잡하고 상호작용 가능한 차트를 구축합니다.
- [Chart](https://developer.apple.com/documentation/charts/chart): 차트를 표시하는 SwiftUI 뷰입니다.
- [ChartContent](https://developer.apple.com/documentation/charts/chartcontent): 차트에 그리는 콘텐츠를 나타내는 타입입니다.
- [ChartContentBuilder](https://developer.apple.com/documentation/charts/chartcontentbuilder): 차트의 콘텐츠를 구성할 때 사용하는 result builder입니다.
- [Plot](https://developer.apple.com/documentation/charts/plot): 차트 콘텐츠를 하나의 엔터티로 그룹화하는 메커니즘입니다.
:::

:::topic-grid
## 3D 차트
- [Chart3D](https://developer.apple.com/documentation/charts/chart3d): 상호작용 가능한 3D 차트와 시각화를 표시하는 SwiftUI 뷰입니다.
- [Chart3DContent](https://developer.apple.com/documentation/charts/chart3dcontent): 차트에 그리는 3차원 콘텐츠를 나타내는 타입입니다.
- [Chart3DContentBuilder](https://developer.apple.com/documentation/charts/chart3dcontentbuilder): 차트의 3차원 콘텐츠를 구성할 때 사용하는 result builder입니다.
- [SurfacePlot](https://developer.apple.com/documentation/charts/surfaceplot): 두 변수의 수학 함수를 3D 표면으로 나타내는 chart content입니다.
:::

:::topic-grid
## Marks
- [AreaMark](https://developer.apple.com/documentation/charts/areamark): 하나 이상의 영역 넓이를 사용해 데이터를 표현하는 chart content입니다.
- [LineMark](https://developer.apple.com/documentation/charts/linemark): 연결된 선분 시퀀스를 사용해 데이터를 표현하는 chart content입니다.
- [PointMark](https://developer.apple.com/documentation/charts/pointmark): 점을 사용해 데이터를 표현하는 chart content입니다.
- [RectangleMark](https://developer.apple.com/documentation/charts/rectanglemark): 사각형을 사용해 데이터를 표현하는 chart content입니다.
- [RuleMark](https://developer.apple.com/documentation/charts/rulemark): 하나의 수평 또는 수직 기준선을 사용해 데이터를 표현하는 chart content입니다.
- [BarMark](https://developer.apple.com/documentation/charts/barmark): 막대를 사용해 데이터를 표현하는 chart content입니다.
- [SectorMark](https://developer.apple.com/documentation/charts/sectormark): 개별 카테고리가 의미 있는 전체를 어떻게 구성하는지 보여 주는 파이 또는 도넛 차트의 sector입니다.
:::

:::topic-grid
## 벡터화된 plot
- [Swift Charts로 데이터 시각화 대시보드 만들기](https://developer.apple.com/documentation/charts/creating-a-data-visualization-dashboard-with-swift-charts): Swift Charts에서 단일 벡터화 plot을 생성하여 전체 데이터 컬렉션을 효율적으로 시각화합니다.
- [AreaPlot](https://developer.apple.com/documentation/charts/areaplot): 함수 또는 데이터 컬렉션을 하나 이상의 영역 넓이로 표현하는 chart content입니다.
- [LinePlot](https://developer.apple.com/documentation/charts/lineplot): 함수 또는 데이터 컬렉션을 연결된 선분 시퀀스로 표현하는 chart content입니다.
- [PointPlot](https://developer.apple.com/documentation/charts/pointplot): 데이터 컬렉션을 점으로 표현하는 chart content입니다.
- [RectanglePlot](https://developer.apple.com/documentation/charts/rectangleplot): 데이터 컬렉션을 사각형으로 표현하는 chart content입니다.
- [RulePlot](https://developer.apple.com/documentation/charts/ruleplot): 데이터 컬렉션을 하나의 수평 또는 수직 기준선으로 표현하는 chart content입니다.
- [BarPlot](https://developer.apple.com/documentation/charts/barplot): 데이터 컬렉션을 막대로 표현하는 chart content입니다.
- [SectorPlot](https://developer.apple.com/documentation/charts/sectorplot): 개별 카테고리가 의미 있는 전체를 어떻게 구성하는지 보여 주는 파이 또는 도넛 차트의 sector로 데이터 컬렉션을 표현하는 chart content입니다.
- [VectorizedChartContent](https://developer.apple.com/documentation/charts/vectorizedchartcontent): 차트를 통해 전달되는 콘텐츠를 나타내는 제네릭 타입입니다.
:::

:::topic-grid
## Mark 구성
- [MarkStackingMethod](https://developer.apple.com/documentation/charts/markstackingmethod): 차트에서 mark를 쌓는 방식입니다.
- [MarkDimension](https://developer.apple.com/documentation/charts/markdimension): mark의 너비 또는 높이를 나타내는 개별 차원입니다.
- [InterpolationMethod](https://developer.apple.com/documentation/charts/interpolationmethod): line mark 또는 area mark가 데이터를 보간하는 방식입니다.
- [BasicChartSymbolShape](https://developer.apple.com/documentation/charts/basicchartsymbolshape): 기본 차트 심볼 모양입니다.
- [ChartSymbolShape](https://developer.apple.com/documentation/charts/chartsymbolshape): 차트에 추가하는 mark의 모양으로 동작할 수 있는 타입입니다.
- [AnyChartSymbolShape](https://developer.apple.com/documentation/charts/anychartsymbolshape): 타입이 소거된 plotting shape입니다.
:::

:::topic-grid
## 라벨이 있는 데이터
- [PlottableValue](https://developer.apple.com/documentation/charts/plottablevalue): mark를 사용해 차트에 표시하는 라벨이 붙은 데이터입니다.
- [Plottable](https://developer.apple.com/documentation/charts/plottable): 차트에 표시할 데이터로 사용할 수 있는 타입입니다.
:::

:::topic-grid
## Scale
- [ScaleRange](https://developer.apple.com/documentation/charts/scalerange): 차트의 범위를 구성할 때 사용할 수 있는 타입입니다.
- [PositionScaleRange](https://developer.apple.com/documentation/charts/positionscalerange): x축과 y축 값을 구성하는 타입입니다.
- [PlotDimensionScaleRange](https://developer.apple.com/documentation/charts/plotdimensionscalerange): plot 영역의 너비 또는 높이를 나타내는 범위입니다.
- [ScaleDomain](https://developer.apple.com/documentation/charts/scaledomain): 차트의 도메인을 구성할 때 사용할 수 있는 타입입니다.
- [AutomaticScaleDomain](https://developer.apple.com/documentation/charts/automaticscaledomain): 차트가 데이터로부터 추론하는 도메인입니다.
- [ScaleType](https://developer.apple.com/documentation/charts/scaletype): plot의 도메인 또는 범위를 스케일링하는 방식입니다.
:::

:::topic-grid
## 축
- [Swift Charts에서 축 사용자화하기](https://developer.apple.com/documentation/charts/customizing-axes-in-swift-charts): 축의 외형을 구성해 차트의 명확성을 높입니다.
- [ChartAxisContent](https://developer.apple.com/documentation/charts/chartaxiscontent): 차트의 축을 나타내는 뷰입니다.
- [AxisContent](https://developer.apple.com/documentation/charts/axiscontent): 차트의 축을 빌드하는 데 사용하는 요소를 나타내는 타입입니다.
- [AxisMarks](https://developer.apple.com/documentation/charts/axismarks): 차트 축의 구성을 나타내기 위해 차트가 그리는 시각적 mark 그룹입니다.
- [AnyAxisContent](https://developer.apple.com/documentation/charts/anyaxiscontent): 타입이 소거된 차트 축 요소입니다.
- [AxisContentBuilder](https://developer.apple.com/documentation/charts/axiscontentbuilder): axis content를 구성하는 result builder입니다.
:::

:::topic-grid
## 축 mark
- [AxisMark](https://developer.apple.com/documentation/charts/axismark): 축 요소의 기본 구성 요소 역할을 하는 타입입니다.
- [AxisTick](https://developer.apple.com/documentation/charts/axistick): 축을 따라 기준점을 나타내기 위해 차트가 축에 그리는 mark입니다.
- [AxisGridLine](https://developer.apple.com/documentation/charts/axisgridline): 특정 축을 따라 기준점을 나타내기 위해 차트가 plot 영역 전체에 그리는 선입니다.
- [AxisValueLabel](https://developer.apple.com/documentation/charts/axisvaluelabel): 축 mark의 값을 설명하는 라벨입니다.
- [AxisValue](https://developer.apple.com/documentation/charts/axisvalue): 축 mark를 위한 값입니다.
- [AnyAxisMark](https://developer.apple.com/documentation/charts/anyaxismark): 타입이 소거된 axis mark입니다.
- [AxisMarkBuilder](https://developer.apple.com/documentation/charts/axismarkbuilder): axis mark를 구성하고 기본 mark를 재정의하는 result builder입니다.
:::

:::topic-grid
## 주석
- [AnnotationContext](https://developer.apple.com/documentation/charts/annotationcontext): 주석을 추가하는 항목에 대한 정보입니다.
- [AnnotationPosition](https://developer.apple.com/documentation/charts/annotationposition): 주석의 위치입니다.
- [AnnotationOverflowResolution](https://developer.apple.com/documentation/charts/annotationoverflowresolution)
:::

:::topic-grid
## 데이터 bin
- [NumberBins](https://developer.apple.com/documentation/charts/numberbins): 숫자 기준으로 데이터를 표시하는 차트용 bin 컬렉션입니다.
- [DateBins](https://developer.apple.com/documentation/charts/datebins): 날짜 기준으로 데이터를 표시하는 차트용 bin 컬렉션입니다.
- [ChartBinRange](https://developer.apple.com/documentation/charts/chartbinrange): 차트의 단일 bin이 나타내는 데이터 범위입니다.
:::

:::topic-grid
## 차트 관리
- [ChartPlotContent](https://developer.apple.com/documentation/charts/chartplotcontent): 차트의 plot 영역을 나타내는 뷰입니다.
- [ChartProxy](https://developer.apple.com/documentation/charts/chartproxy): 차트의 scale과 plot 영역에 접근하는 데 사용하는 proxy입니다.
:::

:::topic-grid
## 스크롤링
- [ChartScrollTargetBehavior](https://developer.apple.com/documentation/charts/chartscrolltargetbehavior): 차트의 스크롤 동작을 구성하는 타입입니다.
- [ChartScrollTargetBehaviorContext](https://developer.apple.com/documentation/charts/chartscrolltargetbehaviorcontext): 차트의 스크롤 방식을 어떻게 조정하는 것이 가장 좋은지 결정할 때 사용할 수 있는 문맥 정보입니다.
:::

:::topic-grid
## 구조체
- [Chart3DRenderingStyle](https://developer.apple.com/documentation/charts/chart3drenderingstyle)
:::
