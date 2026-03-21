---
route: /documentation/ModelIO
source_url: https://developer.apple.com/documentation/ModelIO
source_locale: en-US
section: docc
content_type: symbol
title: Model I/O
original_title: Model I/O
source_hash: b8078a4a44cdf2899592e36f912de7abff1990f6ea6d3d01430f97f0f9716bbb
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:17+00:00'
last_translated_at: '2026-03-13T09:10:00+00:00'
---

# Model I/O

MetalKit, GLKit, SceneKit과 통합되는 공통 인프라를 사용해 3D 모델을 가져오고, 내보내고, 조작합니다.

## 개요

Model I/O 프레임워크는 3D 모델 자산과 관련 리소스를 시스템 수준에서 이해할 수 있게 해 줍니다. 이 프레임워크를 사용하면 널리 쓰이는 저작 도구와 게임 엔진이 지원하는 다양한 업계 표준 파일 포맷으로부터 자산을 가져오거나, 그 포맷으로 자산을 내보낼 수 있습니다. 또한 Model I/O를 사용해 모델 및 텍스처 데이터를 생성하거나 처리할 수도 있습니다. 예를 들어 subdivision surface를 만들거나, ambient occlusion 텍스처를 베이크하거나, light probe를 생성할 수 있습니다. Model I/O는 MetalKit, GLKit, SceneKit 프레임워크와 데이터 버퍼를 공유하여 3D 자산을 효율적으로 로드, 처리, 렌더링할 수 있게 도와줍니다.

### Model I/O 기능

- 3D 자산 가져오기 및 내보내기. [MDLAsset](https://developer.apple.com/documentation/modelio/mdlasset) 객체는 3D 장면의 요소를 설명하는 [MDLMesh](https://developer.apple.com/documentation/modelio/mdlmesh), [MDLLight](https://developer.apple.com/documentation/modelio/mdllight), [MDLCamera](https://developer.apple.com/documentation/modelio/mdlcamera) 객체 모음을 나타냅니다. [MDLAsset](https://developer.apple.com/documentation/modelio/mdlasset) 클래스를 사용해 파일에서 이러한 객체를 로드하거나, 파일로 내보내기 위한 3D 객체 컬렉션을 만들 수 있습니다.
- 3D 모델 데이터 다루기. [MDLVertexDescriptor](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor) 클래스를 사용해 메시의 vertex 및 index 데이터 포맷을 검사하거나 재배치할 수 있습니다. [MDLMeshBuffer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer) 및 [MDLMeshBufferAllocator](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator) 프로토콜을 채택한 클래스를 사용하면, 메시의 vertex 및 index 데이터가 GPU 로딩, 처리, 렌더링 사이에서 복사되고 변환되는 횟수를 최소화할 수 있습니다. MetalKit과 GLKit 프레임워크는 이러한 클래스를 제공합니다. 자세한 내용은 [MetalKit](https://developer.apple.com/documentation/MetalKit)과 [GLKit](https://developer.apple.com/documentation/GLKit)을 참고하세요.
- 자산 데이터 처리 및 생성. [MDLMesh](https://developer.apple.com/documentation/modelio/mdlmesh) 메서드(예: [addNormals(withAttributeNamed:creaseThreshold:)](https://developer.apple.com/documentation/modelio/mdlmesh/addnormals(withattributenamed:creasethreshold:)) 메서드)를 사용해 모델을 처리하고, 렌더링에 사용할 표면 노멀, 탄젠트 기저 벡터, ambient occlusion, light map 같은 추가 데이터를 생성할 수 있습니다. [MDLTexture](https://developer.apple.com/documentation/modelio/mdltexture) 클래스와 그 하위 클래스를 사용하면 noise, normal map, 현실적인 sky box 같은 절차적 텍스처를 생성할 수 있습니다. [MDLLightProbe](https://developer.apple.com/documentation/modelio/mdllightprobe) 클래스를 사용하면 장면 내용에 기반한 조명을 생성할 수 있습니다. [MDLVoxelArray](https://developer.apple.com/documentation/modelio/mdlvoxelarray) 클래스를 사용하면 모델의 체적 설명을 다룰 수 있습니다.
- 현실적인 렌더링 매개변수 설명. [MDLMaterial](https://developer.apple.com/documentation/modelio/mdlmaterial) 객체의 표면 외형을 설명하는 여러 방식 중 하나인 [MDLPhysicallyPlausibleScatteringFunction](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblescatteringfunction) 클래스는 인기 장편 영화와 고급 게임 엔진에서 볼 수 있는 것과 같은 물리 기반 셰이딩 시스템을 사용해 표면의 의도된 렌더링을 정의합니다. [MDLPhotometricLight](https://developer.apple.com/documentation/modelio/mdlphotometriclight)와 [MDLPhysicallyPlausibleLight](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight) 클래스는 렌더링에 사용할 현실적인 조명 속성을 설명하며, [MDLCamera](https://developer.apple.com/documentation/modelio/mdlcamera) 클래스도 물리 기반 렌더링 매개변수를 지원합니다.

:::topic-grid
## 3D 자산 기본 요소
- [MDLAsset](https://developer.apple.com/documentation/modelio/mdlasset): transform 계층, 메시, 카메라, 조명 같은 관련 정보를 포함하는 3D 객체용 인덱스 기반 컨테이너입니다.
- [MDLObject](https://developer.apple.com/documentation/modelio/mdlobject): 메시, 카메라, 조명 등 3D 자산의 일부인 객체를 위한 기반 클래스입니다.
- [MDLTransform](https://developer.apple.com/documentation/modelio/mdltransform): 3D 객체의 로컬 좌표 공간 변환을 설명합니다.
- [MDLMesh](https://developer.apple.com/documentation/modelio/mdlmesh): 3D 객체를 렌더링하는 데 사용할 vertex buffer 데이터를 담는 컨테이너입니다.
- [MDLSubmesh](https://developer.apple.com/documentation/modelio/mdlsubmesh): 3D 객체 전체 또는 일부를 렌더링하는 데 사용할 index buffer 데이터와 material 정보를 담는 컨테이너입니다.
- [MDLSubmeshTopology](https://developer.apple.com/documentation/modelio/mdlsubmeshtopology): submesh의 index buffer 데이터가 어떻게 배열되어 있으며, 그 배열을 submesh의 의도된 3D 형태를 만들기 위해 어떻게 사용해야 하는지 설명합니다.
- [MDLNamed](https://developer.apple.com/documentation/modelio/mdlnamed): 사람이 읽을 수 있는 이름을 노출하는 Model I/O 객체를 위한 공통 인터페이스입니다.
:::

:::topic-grid
## 메시 데이터 관리
- [MDLMeshBuffer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer): 메시를 로드, 처리, 렌더링할 때 사용하는 vertex 및 index 데이터 저장소를 관리하는 일반 인터페이스입니다.
- [MDLMeshBufferAllocator](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator): 메시를 로드, 처리, 렌더링할 때 사용할 데이터 버퍼 할당을 관리하는 일반 인터페이스입니다.
- [MDLMeshBufferData](https://developer.apple.com/documentation/modelio/mdlmeshbufferdata): Model I/O 메시의 vertex 또는 index 데이터를 저장하는 메모리 버퍼입니다.
- [MDLMeshBufferDataAllocator](https://developer.apple.com/documentation/modelio/mdlmeshbufferdataallocator): 데이터 객체를 사용해 주 메모리에서 할당하는 기본 allocator 구현입니다.
- [MDLMeshBufferMap](https://developer.apple.com/documentation/modelio/mdlmeshbuffermap): Model I/O 메시의 데이터 저장에 사용하는 메모리 버퍼에 대한 접근을 관리하는 객체입니다.
- [MDLMeshBufferZone](https://developer.apple.com/documentation/modelio/mdlmeshbufferzone): 관련된 메시 데이터 버퍼를 할당할 때 사용하는 논리적 메모리 풀을 위한 일반 인터페이스입니다.
- [MDLMeshBufferZoneDefault](https://developer.apple.com/documentation/modelio/mdlmeshbufferzonedefault): 해당 프로토콜의 표준 구현입니다.
- [MDLVertexAttribute](https://developer.apple.com/documentation/modelio/mdlvertexattribute): 메시 객체의 단일 vertex attribute에 대한 per-vertex 데이터 포맷 설명입니다.
- [MDLVertexAttributeData](https://developer.apple.com/documentation/modelio/mdlvertexattributedata): 메시의 특정 vertex attribute에 대한 vertex 데이터에 편리하게 접근할 수 있게 해 주는 객체입니다.
- [MDLVertexBufferLayout](https://developer.apple.com/documentation/modelio/mdlvertexbufferlayout): 객체 안의 vertex buffer에 대한 레이아웃 정보를 설명하는 객체입니다. vertex layer 객체, vertex attribute 객체, 추가 정보를 모아 만든 객체는 메시의 vertex buffer 레이아웃을 완전히 설명합니다.
- [MDLVertexDescriptor](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor): 메시와 연결된 vertex 데이터 버퍼의 구조, 포맷, 레이아웃 설명입니다.
:::

:::topic-grid
## 재질
- [MDLMaterial](https://developer.apple.com/documentation/modelio/mdlmaterial): 3D 객체 렌더링 시 의도된 표면 외형을 함께 설명하는 material property 모음입니다.
- [MDLMaterialProperty](https://developer.apple.com/documentation/modelio/mdlmaterialproperty): 재질의 렌더링 매개변수 중 한 특정 측면에 대한 정의입니다.
- [MDLMaterialPropertyConnection](https://developer.apple.com/documentation/modelio/mdlmaterialpropertyconnection)
- [MDLMaterialPropertyGraph](https://developer.apple.com/documentation/modelio/mdlmaterialpropertygraph)
- [MDLMaterialPropertyNode](https://developer.apple.com/documentation/modelio/mdlmaterialpropertynode)
- [MDLScatteringFunction](https://developer.apple.com/documentation/modelio/mdlscatteringfunction): 재질을 위한 기본 셰이딩 모델을 설명하는 material property 집합이며, 더 복잡한 셰이딩 모델의 상위 클래스입니다.
- [MDLPhysicallyPlausibleScatteringFunction](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblescatteringfunction): 재질을 위한 물리적으로 현실적인 셰이딩 모델을 설명하는 material property 집합입니다.
:::

:::topic-grid
## 텍스처
- [MDLTexture](https://developer.apple.com/documentation/modelio/mdltexture): 재질 표면 외형을 렌더링하는 데 사용하는 texel 데이터의 소스입니다.
- [MDLCheckerboardTexture](https://developer.apple.com/documentation/modelio/mdlcheckerboardtexture): 지정한 두 색으로 checkerboard 패턴을 생성하는 texel 데이터 생성기입니다.
- [MDLColorSwatchTexture](https://developer.apple.com/documentation/modelio/mdlcolorswatchtexture): 지정한 두 색 사이의 그라디언트를 생성하는 texel 데이터 생성기입니다.
- [MDLNoiseTexture](https://developer.apple.com/documentation/modelio/mdlnoisetexture): 무작위 noise 필드를 생성하는 texel 데이터 생성기입니다.
- [MDLNormalMapTexture](https://developer.apple.com/documentation/modelio/mdlnormalmaptexture): 제공된 텍스처로부터 normal map을 계산하는 texel 데이터 생성기입니다.
- [MDLSkyCubeTexture](https://developer.apple.com/documentation/modelio/mdlskycubetexture): 햇빛이 비치는 하늘을 물리적으로 사실적으로 시뮬레이션하여 cube texture를 생성하는 texel 데이터 생성기입니다.
- [MDLURLTexture](https://developer.apple.com/documentation/modelio/mdlurltexture): 텍스처 데이터를 로드할 URL을 가리키는 가벼운 참조입니다.
- [MDLTextureFilter](https://developer.apple.com/documentation/modelio/mdltexturefilter): 렌더러가 텍스처를 샘플링할 때 사용할 필터링 모드를 설명합니다.
- [MDLTextureSampler](https://developer.apple.com/documentation/modelio/mdltexturesampler): 텍스처 렌더링에 사용할 샘플링 매개변수와 텍스처 데이터 소스를 짝지은 객체입니다.
:::

:::topic-grid
## 조명
- [MDLLight](https://developer.apple.com/documentation/modelio/mdllight): 장면의 광원을 설명하는 객체들의 추상 상위 클래스입니다.
- [MDLAreaLight](https://developer.apple.com/documentation/modelio/mdlarealight): 특정한 모양의 면적에서 3D 장면을 비추는 광원입니다.
- [MDLLightProbe](https://developer.apple.com/documentation/modelio/mdllightprobe): 모든 방향에서의 조명 색과 강도 변화를 기준으로 설명되는 광원입니다.
- [MDLLightProbeIrradianceDataSource](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource): 장면 주위에 light probe를 자동 배치할 때 사용할 정보를 제공하려면 이 프로토콜을 채택합니다.
- [MDLPhotometricLight](https://developer.apple.com/documentation/modelio/mdlphotometriclight): 광도의 모양, 방향, 조명 강도가 photometric profile로 결정되는 광원입니다.
- [MDLPhysicallyPlausibleLight](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight): 현실 세계 물리학을 기반으로 한 셰이딩 모델에서 사용하는 광원입니다.
:::

:::topic-grid
## 카메라
- [MDLCamera](https://developer.apple.com/documentation/modelio/mdlcamera): 3D 장면을 렌더링하기 위한 시점과, 의도한 렌더링 외형을 설명하는 매개변수 집합입니다.
- [MDLStereoscopicCamera](https://developer.apple.com/documentation/modelio/mdlstereoscopiccamera): 3D 장면을 입체적으로 표시하기 위한 시점입니다.
:::

:::topic-grid
## 확장 가능한 자산 포맷 지원
- [MDLComponent](https://developer.apple.com/documentation/modelio/mdlcomponent): Model I/O의 확장 가능한 파일 포맷 지원을 위한 기반 프로토콜입니다.
- [MDLObjectContainer](https://developer.apple.com/documentation/modelio/mdlobjectcontainer): 3D 자산의 객체 계층 관계를 다루기 위한 기본 구현입니다.
- [MDLObjectContainerComponent](https://developer.apple.com/documentation/modelio/mdlobjectcontainercomponent): 객체 계층에서 컨테이너 역할을 할 수 있는 클래스들을 위한 일반 인터페이스입니다.
- [MDLTransformComponent](https://developer.apple.com/documentation/modelio/mdltransformcomponent): 3D 객체의 로컬 좌표 공간 변환을 관리하는 클래스들을 위한 일반 인터페이스입니다.
:::

:::topic-grid
## 체적 표현
- [MDLVoxelArray](https://developer.apple.com/documentation/modelio/mdlvoxelarray): 3D 객체의 고체 부피를 voxel, 즉 정육면체 단위들의 모음으로 표현한 모델입니다.
:::

:::topic-grid
## 참고 자료
- [Model I/O Data Types](https://developer.apple.com/documentation/modelio/model-i-o-data-types)
- [Model I/O Structures](https://developer.apple.com/documentation/modelio/model-i-o-structures)
- [Model I/O Enumerations](https://developer.apple.com/documentation/modelio/model-i-o-enumerations)
- [Model I/O Constants](https://developer.apple.com/documentation/modelio/model-i-o-constants)
:::

:::topic-grid
## 클래스
- [MDLAnimatedMatrix4x4](https://developer.apple.com/documentation/modelio/mdlanimatedmatrix4x4)
- [MDLAnimatedQuaternion](https://developer.apple.com/documentation/modelio/mdlanimatedquaternion)
- [MDLAnimatedQuaternionArray](https://developer.apple.com/documentation/modelio/mdlanimatedquaternionarray)
- [MDLAnimatedScalar](https://developer.apple.com/documentation/modelio/mdlanimatedscalar)
- [MDLAnimatedScalarArray](https://developer.apple.com/documentation/modelio/mdlanimatedscalararray)
- [MDLAnimatedValue](https://developer.apple.com/documentation/modelio/mdlanimatedvalue)
- [MDLAnimatedVector2](https://developer.apple.com/documentation/modelio/mdlanimatedvector2)
- [MDLAnimatedVector3](https://developer.apple.com/documentation/modelio/mdlanimatedvector3)
- [MDLAnimatedVector3Array](https://developer.apple.com/documentation/modelio/mdlanimatedvector3array)
- [MDLAnimatedVector4](https://developer.apple.com/documentation/modelio/mdlanimatedvector4)
- [MDLAnimationBindComponent](https://developer.apple.com/documentation/modelio/mdlanimationbindcomponent)
- [MDLBundleAssetResolver](https://developer.apple.com/documentation/modelio/mdlbundleassetresolver)
- [MDLMatrix4x4Array](https://developer.apple.com/documentation/modelio/mdlmatrix4x4array)
- [MDLPackedJointAnimation](https://developer.apple.com/documentation/modelio/mdlpackedjointanimation)
- [MDLPathAssetResolver](https://developer.apple.com/documentation/modelio/mdlpathassetresolver)
- [MDLRelativeAssetResolver](https://developer.apple.com/documentation/modelio/mdlrelativeassetresolver)
- [MDLSkeleton](https://developer.apple.com/documentation/modelio/mdlskeleton)
- [MDLTransformMatrixOp](https://developer.apple.com/documentation/modelio/mdltransformmatrixop)
- [MDLTransformOrientOp](https://developer.apple.com/documentation/modelio/mdltransformorientop)
- [MDLTransformRotateOp](https://developer.apple.com/documentation/modelio/mdltransformrotateop)
- [MDLTransformRotateXOp](https://developer.apple.com/documentation/modelio/mdltransformrotatexop)
- [MDLTransformRotateYOp](https://developer.apple.com/documentation/modelio/mdltransformrotateyop)
- [MDLTransformRotateZOp](https://developer.apple.com/documentation/modelio/mdltransformrotatezop)
- [MDLTransformScaleOp](https://developer.apple.com/documentation/modelio/mdltransformscaleop)
- [MDLTransformStack](https://developer.apple.com/documentation/modelio/mdltransformstack)
- [MDLTransformTranslateOp](https://developer.apple.com/documentation/modelio/mdltransformtranslateop)
- [MDLUtility](https://developer.apple.com/documentation/modelio/mdlutility)
:::

:::topic-grid
## 프로토콜
- [MDLAssetResolver](https://developer.apple.com/documentation/modelio/mdlassetresolver)
- [MDLJointAnimation](https://developer.apple.com/documentation/modelio/mdljointanimation)
- [MDLTransformOp](https://developer.apple.com/documentation/modelio/mdltransformop)
:::
