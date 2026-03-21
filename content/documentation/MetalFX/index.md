---
route: /documentation/MetalFX
source_url: https://developer.apple.com/documentation/MetalFX
source_locale: en-US
section: docc
content_type: symbol
title: MetalFX
original_title: MetalFX
source_hash: 3eeb436669b2bd79c5a636dfc8711680747e618fc7e24519ea2c84431741c2c2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:36:25+00:00'
last_translated_at: '2026-03-14T01:03:00+09:00'
---

# MetalFX

낮은 해상도의 콘텐츠를 업스케일해 GPU 시간을 절약함으로써 Metal 앱의 성능을 높입니다.

## 개요

`MetalFX` 프레임워크는 [Metal](https://developer.apple.com/documentation/Metal)과 통합되어, 비교적 낮은 해상도의 이미지를 출력 해상도에 직접 렌더링하는 것보다 더 짧은 시간에 더 높은 해상도로 업스케일합니다.

![전통적인 렌더링 시간과 MetalFX 업스케일링 시간을 비교하는 타임라인 다이어그램입니다. 낮은 해상도로 렌더링한 뒤 MetalFX로 최종 해상도로 업스케일하는 MetalFX 방식은, 더 높은 최종 해상도로 직접 렌더링하는 전통적인 방식보다 대략 절반 정도의 시간이 걸립니다.](https://developer.apple.com)

절약한 GPU 시간을 활용해 앱이나 게임 경험을 더 향상시킬 수 있습니다. 예를 들어 더 많은 효과나 장면 디테일을 추가할 수 있습니다.

`MetalFX`는 입력 렌더링을 업스케일하는 두 가지 방식을 제공합니다.

- 시간 기반 안티앨리어싱 업스케일링
- 공간 업스케일링

픽셀 색상, 깊이, 모션 정보를 제공할 수 있다면 render pipeline에 [MTLFXTemporalScaler](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler) 인스턴스를 추가하십시오. 그렇지 않다면 픽셀 색상 입력 texture만 필요로 하는 [MTLFXSpatialScaler](https://developer.apple.com/documentation/metalfx/mtlfxspatialscaler) 인스턴스를 추가하십시오.

스케일링 효과는 초기화에 시간이 걸리므로, 앱 실행 시점이나 디스플레이 해상도가 변경될 때 두 효과 중 하나의 인스턴스를 만들어 두십시오. 효과 인스턴스를 만든 뒤에는 반복해서 사용할 수 있으며, 일반적으로는 프레임마다 한 번씩 사용합니다.

:::topic-grid
## Temporal scaling
- [Applying temporal antialiasing and upscaling using MetalFX](https://developer.apple.com/documentation/metalfx/applying-temporal-antialiasing-and-upscaling-using-metalfx): MetalFX를 사용해 렌더링 workload를 줄이면서 이미지 디테일을 높입니다.
- [MTLFXTemporalScaler](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler): 시간에 따라 여러 입력 texture를 분석해 render pass 안에서 더 높은 해상도 texture를 생성하는 업스케일링 효과입니다.
- [MTLFXTemporalScalerDescriptor](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor): temporal scaling 효과를 구성하는 속성 집합과, 그 효과를 생성하는 factory method입니다.
:::

:::topic-grid
## Spatial scaling
- [MTLFXSpatialScaler](https://developer.apple.com/documentation/metalfx/mtlfxspatialscaler): 입력 texture를 공간적으로 분석해 render pass 안에서 더 높은 해상도 texture를 생성하는 업스케일링 효과입니다.
- [MTLFXSpatialScalerDescriptor](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerdescriptor): spatial scaling 효과를 구성하는 속성 집합과, 그 효과를 생성하는 factory method입니다.
- [MTLFXSpatialScalerColorProcessingMode](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalercolorprocessingmode): spatial scaling 효과 인스턴스와 함께 사용하는 입력 및 출력 texture의 색 공간 모드입니다.
:::

:::topic-grid
## 클래스
- [MTLFXFrameInterpolatorDescriptor](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor): frame interpolator를 구성하는 속성 집합과, 그 효과를 생성하는 factory method입니다.
- [MTLFXTemporalDenoisedScalerDescriptor](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor)
:::

:::topic-grid
## 프로토콜
- [MTL4FXFrameInterpolator](https://developer.apple.com/documentation/metalfx/mtl4fxframeinterpolator)
- [MTL4FXSpatialScaler](https://developer.apple.com/documentation/metalfx/mtl4fxspatialscaler): 입력 texture를 공간적으로 분석해 render pass 안에서 더 높은 해상도 texture를 생성하는 업스케일링 효과입니다.
- [MTL4FXTemporalDenoisedScaler](https://developer.apple.com/documentation/metalfx/mtl4fxtemporaldenoisedscaler)
- [MTL4FXTemporalScaler](https://developer.apple.com/documentation/metalfx/mtl4fxtemporalscaler)
- [MTLFXFrameInterpolatableScaler](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatablescaler)
- [MTLFXFrameInterpolator](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolator)
- [MTLFXFrameInterpolatorBase](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase)
- [MTLFXSpatialScalerBase](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerbase): 입력 texture를 공간적으로 분석해 render pass 안에서 더 높은 해상도 texture를 생성하는 업스케일링 효과입니다.
- [MTLFXTemporalDenoisedScaler](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscaler)
- [MTLFXTemporalDenoisedScalerBase](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerbase)
- [MTLFXTemporalScalerBase](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase): 시간에 따라 여러 입력 texture를 분석해 render pass 안에서 더 높은 해상도 texture를 생성하는 업스케일링 효과입니다.
:::
