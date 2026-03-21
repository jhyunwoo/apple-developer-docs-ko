---
route: /documentation/CompositorServices
source_url: https://developer.apple.com/documentation/CompositorServices
source_locale: en-US
section: docc
content_type: symbol
title: Compositor Services
original_title: Compositor Services
source_hash: 7f89bcc8587f80f0fc684327dc1488dd5313d3e9a2696e1543e6fbe35dec98a6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:41:40+00:00'
last_translated_at: '2026-03-13T23:51:00+09:00'
---

# Compositor Services

드로잉 환경을 직접 제어하고 Metal을 사용해 자체 콘텐츠를 렌더링합니다.

## 개요

Compositor Services를 사용하면 Metal과 자체 렌더링 엔진을 사용해 기기의 디스플레이에 직접 그릴 수 있습니다. 이 프레임워크를 사용하면 사용자의 주변 환경과 통합할 필요가 없는 완전 몰입형 장면을 앱에서 만들 수 있습니다.

앱에서 [CompositorLayer](https://developer.apple.com/documentation/compositorservices/compositorlayer) 콘텐츠로 immersive space를 표시하면, Metal 드로잉 환경을 설정하는 데 필요한 정보를 담은 [LayerRenderer](https://developer.apple.com/documentation/compositorservices/layerrenderer)를 받습니다. 이 layer를 사용해 렌더링 루프를 시작하고 연속적인 콘텐츠 프레임을 전달합니다. layer는 디스플레이의 새로 고침 속도에 맞춰 프레임을 전달하는 데 필요한 타이밍 정보를 제공합니다. 또한 기기 디스플레이에 콘텐츠를 그리는 데 필요한 Metal texture와 기타 정보도 제공합니다.

Metal을 사용해 앱 콘텐츠를 그리는 방법에 대한 자세한 내용은 [Metal](https://developer.apple.com/documentation/Metal)을 참고합니다.

:::topic-grid
## 앱 통합
- [Drawing fully immersive content using Metal](https://developer.apple.com/documentation/compositorservices/drawing-fully-immersive-content-using-metal): 사용자 정의 Metal 기반 렌더링 엔진을 사용해 visionOS에서 완전 몰입형 경험을 만듭니다.
- [Interacting with virtual content blended with passthrough](https://developer.apple.com/documentation/compositorservices/interacting-with-virtual-content-blended-with-passthrough): 사용자의 주변 환경에 콘텐츠를 그리기 위한 mixed immersion style 공간을 표시하고, 렌더링된 콘텐츠에 대해 상지 표현 방식을 선택합니다.
- [Rendering hover effects in Metal immersive apps](https://developer.apple.com/documentation/compositorservices/rendering_hover_effects_in_metal_immersive_apps): 플레이어가 바라볼 때 렌더링된 화면 요소의 외형을 변경합니다.
- [CompositorLayer](https://developer.apple.com/documentation/compositorservices/compositorlayer): immersive space와 함께 사용해 Metal로 완전 몰입형 콘텐츠를 표시하는 타입입니다.
- [CompositorLayerConfiguration](https://developer.apple.com/documentation/compositorservices/compositorlayerconfiguration): Metal 렌더링 엔진과 함께 사용할 texture 구성과 렌더링 동작을 지정하는 인터페이스입니다.
- [DefaultCompositorLayerConfiguration](https://developer.apple.com/documentation/compositorservices/defaultcompositorlayerconfiguration): 현재 기기의 기본 texture 구성과 렌더링 동작으로 layer를 구성하는 타입입니다.
:::

:::topic-grid
## 렌더 루프 설정
- [LayerRenderer](https://developer.apple.com/documentation/compositorservices/layerrenderer): 콘텐츠를 그리는 데 필요한 Metal 타입과 타이밍 정보를 제공하는 타입입니다.
- [LayerRenderer.Frame](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame): 단일 콘텐츠 프레임을 렌더링하는 데 필요한 타이밍 정보와 데이터 타입에 접근할 수 있게 하는 타입입니다.
:::

:::topic-grid
## 드로잉 환경
- [LayerRenderer.Drawable](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable): 콘텐츠 프레임을 그리는 데 필요한 texture와 정보를 제공하는 타입입니다.
- [LayerRenderer.Drawable.View](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/view): 프레임의 texture에 콘텐츠를 어떻게 렌더링할지에 대한 정보를 제공하는 타입입니다.
:::

:::topic-grid
## 오류
- [LayerRendererConfigurationError](https://developer.apple.com/documentation/compositorservices/layerrendererconfigurationerror): layer를 구성할 때 발생할 수 있는 오류입니다.
:::

:::topic-grid
## 문서
- [CompositorServices Functions](https://developer.apple.com/documentation/compositorservices/compositorservices-functions)
- [Controlling Metal rendering immersion level](https://developer.apple.com/documentation/compositorservices/controlling-metal-rendering-immersion-level): Metal 콘텐츠를 렌더링할 때 progressive immersion을 지원해 유연한 몰입형 렌더링을 활성화합니다.
:::

:::topic-grid
## 구조체
- [TextureTopology](https://developer.apple.com/documentation/compositorservices/texturetopology): drawable의 texture 중 하나가 어떻게 구성되는지를 지정하는 타입입니다.
:::

:::topic-grid
## 타입 별칭
- [cp_drawable_array_t](https://developer.apple.com/documentation/compositorservices/cp_drawable_array_t): 렌더 파이프라인을 설정하는 데 필요한 drawable 타입과 기타 정보를 담는 불투명 타입입니다.
- [cp_hover_effect_t](https://developer.apple.com/documentation/compositorservices/cp_hover_effect_t): tracking area의 hover effect를 설명하는 불투명 타입입니다.
:::
