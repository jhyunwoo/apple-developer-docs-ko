---
route: /documentation/SceneKit
source_url: https://developer.apple.com/documentation/SceneKit
source_locale: en-US
section: docc
content_type: symbol
title: SceneKit
original_title: SceneKit
source_hash: 236732d8361e85820f26430e03d3fb9cb70d441a1f3e62af1f569564acc8304d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:28:23+00:00'
last_translated_at: '2026-03-13T20:00:00+09:00'
---

# SceneKit

고수준 scene 설명을 사용해 3D 게임을 만들고 앱에 3D 콘텐츠를 추가하며, 애니메이션, 물리 시뮬레이션, 파티클 효과, 사실적인 물리 기반 렌더링을 쉽게 추가합니다.

## 개요

SceneKit은 고성능 렌더링 엔진과 3D 자산의 가져오기, 조작, 렌더링을 위한 설명적 API를 결합합니다. 장면을 표시하는 렌더링 알고리즘을 매우 정밀한 수준까지 직접 구현해야 하는 Metal이나 OpenGL 같은 저수준 API와 달리, SceneKit은 장면의 내용과 수행할 동작 또는 애니메이션에 대한 설명만 요구합니다.

:::note 참고
visionOS에서 SceneKit 콘텐츠는 2D view와 텍스처 안에서만 표시할 수 있습니다. 몰입형 3D 콘텐츠를 만드는 방법에 대한 정보는 [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionOS/creating-fully-immersive-experiences)를 참고하십시오.
:::

:::topic-grid
## 핵심 사항
- [SCNScene](https://developer.apple.com/documentation/scenekit/scnscene): 표시 가능한 3D 장면을 함께 구성하는 node 계층과 전역 속성을 담는 컨테이너입니다.
- [SCNView](https://developer.apple.com/documentation/scenekit/scnview): 3D SceneKit 콘텐츠를 표시하기 위한 view입니다.
- [SceneView](https://developer.apple.com/documentation/scenekit/sceneview): 3D SceneKit 콘텐츠를 표시하기 위한 SwiftUI view입니다.
:::

:::topic-grid
## Scene 구조
- [Organizing a Scene with Nodes](https://developer.apple.com/documentation/scenekit/organizing-a-scene-with-nodes): node를 사용해 장면의 구조를 정의합니다.
- [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode): 3D 좌표 공간의 위치와 변환을 나타내는 scene graph의 구조 요소로, geometry, light, camera 또는 다른 표시 가능한 콘텐츠를 연결할 수 있습니다.
- [SCNReferenceNode](https://developer.apple.com/documentation/scenekit/scnreferencenode): 별도의 scene 파일에서 로드할 콘텐츠의 자리표시자 역할을 하는 scene graph node입니다.
:::

:::topic-grid
## 표시와 상호 작용
- [SCNSceneRenderer](https://developer.apple.com/documentation/scenekit/scnscenerenderer): ``, ``, `` 클래스에 공통인 메서드와 프로퍼티입니다.
- [SCNSceneRendererDelegate](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate): 앱이 SceneKit의 애니메이션 루프에 참여하거나 추가 렌더링을 수행하기 위해 구현할 수 있는 메서드입니다.
- [SCNLayer](https://developer.apple.com/documentation/scenekit/scnlayer): SceneKit 장면을 자신의 콘텐츠로 렌더링하는 Core Animation layer입니다.
- [SCNRenderer](https://developer.apple.com/documentation/scenekit/scnrenderer): 기존 Metal 워크플로나 OpenGL 컨텍스트 안에서 SceneKit 장면을 표시하기 위한 renderer입니다.
- [SCNHitTestResult](https://developer.apple.com/documentation/scenekit/scnhittestresult): scene 공간 또는 view 공간에서 scene 요소를 검색한 결과에 대한 정보입니다.
:::

:::topic-grid
## 조명, 카메라, 셰이딩
- [SCNLight](https://developer.apple.com/documentation/scenekit/scnlight): 장면을 비추기 위해 node에 연결할 수 있는 광원입니다.
- [SCNCamera](https://developer.apple.com/documentation/scenekit/scncamera): 장면을 표시하기 위한 시점을 제공하기 위해 node에 연결할 수 있는 카메라 속성 집합입니다.
- [SCNMaterial](https://developer.apple.com/documentation/scenekit/scnmaterial): 렌더링될 때 geometry 표면의 외관을 정의하는 셰이딩 속성 집합입니다.
- [SCNMaterialProperty](https://developer.apple.com/documentation/scenekit/scnmaterialproperty): material의 시각 속성 중 하나에 대한 색상이나 텍스처를 담는 컨테이너입니다.
:::

:::topic-grid
## Geometry
- [SCNGeometry](https://developer.apple.com/documentation/scenekit/scngeometry): 장면에 표시할 수 있는 3차원 형태(모델 또는 mesh라고도 함)이며, 외관을 정의하는 material이 연결됩니다.
- [SCNGeometrySource](https://developer.apple.com/documentation/scenekit/scngeometrysource): 3차원 객체 또는 geometry 정의의 일부를 이루는 정점 데이터를 담는 컨테이너입니다.
- [SCNGeometryElement](https://developer.apple.com/documentation/scenekit/scngeometryelement): 정점이 어떻게 연결되어 3차원 객체 또는 geometry를 정의하는지 설명하는 인덱스 데이터를 담는 컨테이너입니다.
- [Built-in Geometry Types](https://developer.apple.com/documentation/scenekit/built-in-geometry-types): 구, 상자, 평면 같은 기본 도형과 2D 텍스트 및 Bézier 곡선으로부터 3D 객체를 생성하는 기능입니다.
:::

:::topic-grid
## 애니메이션과 제약
- [Animation](https://developer.apple.com/documentation/scenekit/animation): 장면 요소를 미리 정해진 방식으로 움직이는 선언적 애니메이션을 만들거나 외부 제작 도구에서 가져온 애니메이션을 관리합니다.
- [Constraints](https://developer.apple.com/documentation/scenekit/constraints): 지정한 규칙에 따라 node의 위치나 방향을 자동으로 조정합니다.
- [SCNSkinner](https://developer.apple.com/documentation/scenekit/scnskinner): 골격 애니메이션과 그것이 움직이는 node 및 geometry 사이의 관계를 관리하는 객체입니다.
- [SCNMorpher](https://developer.apple.com/documentation/scenekit/scnmorpher): node의 기본 geometry와 하나 이상의 대상 geometry 사이의 부드러운 전환을 관리하는 객체입니다.
:::

:::topic-grid
## 물리
- [Physics Simulation](https://developer.apple.com/documentation/scenekit/physics-simulation): 장면 요소에 동적 동작을 추가하고, 접촉과 충돌을 감지하며, 중력, 스프링, 차량 같은 사실적인 효과를 시뮬레이션합니다.
:::

:::topic-grid
## 파티클 시스템
- [SCNParticleSystem](https://developer.apple.com/documentation/scenekit/scnparticlesystem): 일반 동작만 지정하면 되는 고수준 시뮬레이션을 사용해 작은 이미지 스프라이트 시스템을 애니메이션하고 렌더링하는 객체입니다.
- [SCNParticlePropertyController](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller): 파티클 시스템이 렌더링하는 개별 파티클의 단일 속성에 대한 애니메이션입니다.
:::

:::topic-grid
## 오디오
- [SCNAudioSource](https://developer.apple.com/documentation/scenekit/scnaudiosource): 위치 기반 오디오 재생에 사용하는, 파일에서 로드한 간단하고 재사용 가능한 오디오 소스입니다.
- [SCNAudioPlayer](https://developer.apple.com/documentation/scenekit/scnaudioplayer): SceneKit 장면에서 위치 기반 오디오 소스의 재생을 제어하는 컨트롤러입니다.
:::

:::topic-grid
## Renderer 사용자화
- [SCNShadable](https://developer.apple.com/documentation/scenekit/scnshadable): Metal 또는 OpenGL 셰이더 프로그램을 사용해 geometry와 material에 대한 SceneKit 렌더링을 사용자화하는 메서드입니다.
- [SCNProgram](https://developer.apple.com/documentation/scenekit/scnprogram): geometry나 material에 대한 SceneKit 렌더링을 대체하는 완전한 Metal 또는 OpenGL 셰이더 프로그램입니다.
- [SCNBufferStream](https://developer.apple.com/documentation/scenekit/scnbufferstream): 사용자 정의 셰이더 프로그램이 사용하는 Metal buffer를 관리하는 객체입니다.
- [SCNTechnique](https://developer.apple.com/documentation/scenekit/scntechnique): 사용자 정의 Metal 또는 OpenGL 셰이더를 사용한 추가 드로잉 패스로 장면 렌더링을 보강하거나 후처리하기 위한 명세입니다.
- [SCNTechniqueSupport](https://developer.apple.com/documentation/scenekit/scntechniquesupport): `` 객체를 사용한 멀티패스 렌더링을 지원하는 SceneKit 객체의 공통 인터페이스입니다.
- [SCNNodeRendererDelegate](https://developer.apple.com/documentation/scenekit/scnnoderendererdelegate): node 콘텐츠를 렌더링하기 위해 자신의 Metal 또는 OpenGL 드로잉 코드를 사용할 때 구현할 수 있는 메서드입니다.
- [Postprocessing a Scene With Custom Symbols](https://developer.apple.com/documentation/scenekit/postprocessing-a-scene-with-custom-symbols): 사용자 정의 심볼이 있는 렌더링 기법을 정의하여 장면에 시각 효과를 만듭니다.
:::

:::topic-grid
## Scene 자산 가져오기
- [SCNSceneSource](https://developer.apple.com/documentation/scenekit/scnscenesource): 파일이나 데이터에서 scene 내용을 로드하는 데 관련된 데이터 읽기 작업을 관리하는 객체입니다.
:::

:::topic-grid
## JavaScript
- [SCNExportJavaScriptModule(_:)](https://developer.apple.com/documentation/scenekit/scnexportjavascriptmodule(_:)): SceneKit 클래스와 전역 상수를 지정한 JavaScript 컨텍스트에서 사용할 수 있게 합니다.
:::

:::topic-grid
## SceneKit 데이터 타입
- [SceneKit 3D Data Types](https://developer.apple.com/documentation/scenekit/scenekit-3d-data-types): SceneKit 전용 벡터, 행렬, 그리고 관련 함수 및 연산입니다.
:::

:::topic-grid
## 매크로
- [Macros](https://developer.apple.com/documentation/scenekit/scenekit-macros)
:::

:::topic-grid
## 참고 자료
- [SceneKit Enumerations](https://developer.apple.com/documentation/scenekit/scenekit-enumerations)
- [SceneKit Constants](https://developer.apple.com/documentation/scenekit/scenekit-constants): SceneKit 프레임워크 전반에서 사용하는 상수입니다.
:::
