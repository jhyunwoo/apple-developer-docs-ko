---
route: /documentation/GLKit
source_url: https://developer.apple.com/documentation/GLKit
source_locale: en-US
section: docc
content_type: symbol
title: GLKit
original_title: GLKit
source_hash: e6f5eb230e7551cf47973fb5107bcfa2b87303e1f7196818339ac8da5336330c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:54:28+00:00'
last_translated_at: '2026-03-13T21:38:00+09:00'
---

# GLKit

OpenGL ES 또는 OpenGL 앱 개발을 더 빠르게 진행합니다. 수학 라이브러리, 백그라운드 텍스처 로딩, 미리 만들어진 shader effect, 표준 view 및 view controller를 사용해 렌더링 루프를 구현합니다.

## 개요

GLKit 프레임워크는 새로운 shader 기반 앱을 만들거나, 이전 OpenGL ES 또는 OpenGL 버전이 제공하던 고정 기능 vertex 또는 fragment 처리에 의존하는 기존 앱을 포팅하는 데 필요한 노력을 줄여 주는 함수와 클래스를 제공합니다.

### GLKit 기능

GLKit은 네 가지 핵심 영역의 기능을 제공합니다.

- *텍스처 로딩*을 사용하면 앱이 다양한 소스에서 텍스처를 쉽게 불러올 수 있습니다. 텍스처는 몇 줄의 코드만으로도 백그라운드에서 비동기적으로 불러올 수 있습니다. 자세한 내용은 [GLKTextureLoader](https://developer.apple.com/documentation/glkit/glktextureloader)를 참고하십시오.
- *수학 라이브러리*는 자주 사용하는 vector, quaternion, matrix 연산을 제공합니다. 이러한 구현은 뛰어난 성능을 내도록 최적화되어 있습니다.
- *effect*는 흔히 사용하는 shader effect의 표준 구현을 제공합니다. effect와 관련 vertex 데이터를 구성하면, effect가 적절한 shader를 생성하고 로드합니다. GLKit에는 세 가지 effect가 포함됩니다. [GLKBaseEffect](https://developer.apple.com/documentation/glkit/glkbaseeffect) 클래스는 OpenGL ES 1.1의 shading 및 lighting 모델의 핵심 부분을 구현하고, [GLKReflectionMapEffect](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect) 클래스는 reflection mapping 지원을 포함하도록 base effect를 확장하며, [GLKSkyboxEffect](https://developer.apple.com/documentation/glkit/glkskyboxeffect) 클래스는 skybox effect 구현을 제공합니다.
- *view와 view controller*는 OpenGL ES view와 이에 대응하는 view controller의 표준 구현을 제공합니다. 이를 통해 OpenGL ES를 사용하는 iOS 앱을 만드는 데 필요한 코드 양이 줄어듭니다. 자세한 내용은 [GLKView](https://developer.apple.com/documentation/glkit/glkview)와 [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller)를 참고하십시오.

iOS에서 GLKit은 OpenGL ES 2.0 context를 필요로 합니다. macOS에서 GLKit은 OpenGL 3.2 Core Profile을 지원하는 OpenGL context를 필요로 합니다.

:::topic-grid
## 텍스처 로딩
- [GLKTextureInfo](https://developer.apple.com/documentation/glkit/glktextureinfo): 이 클래스가 생성한 OpenGL 텍스처에 대한 정보입니다.
- [GLKTextureLoader](https://developer.apple.com/documentation/glkit/glktextureloader): 다양한 이미지 파일 포맷에서 OpenGL 또는 OpenGL ES texture data를 불러오는 일을 단순화하는 유틸리티 클래스입니다.
:::

:::topic-grid
## OpenGL ES view 렌더링
- [GLKView](https://developer.apple.com/documentation/glkit/glkview): OpenGL ES를 사용해 콘텐츠를 그리는 view의 기본 구현입니다.
- [GLKViewDelegate](https://developer.apple.com/documentation/glkit/glkviewdelegate): 객체와 함께 사용하는 drawing callback 메서드입니다.
- [GLKViewController](https://developer.apple.com/documentation/glkit/glkviewcontroller): OpenGL ES 렌더링 루프를 관리하는 view controller입니다.
- [GLKViewControllerDelegate](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate): 객체와 함께 사용하는 렌더링 루프 callback 메서드입니다.
:::

:::topic-grid
## 메시 데이터 관리
- [GLKMesh](https://developer.apple.com/documentation/glkit/glkmesh)
- [GLKMeshBuffer](https://developer.apple.com/documentation/glkit/glkmeshbuffer)
- [GLKMeshBufferAllocator](https://developer.apple.com/documentation/glkit/glkmeshbufferallocator)
- [GLKSubmesh](https://developer.apple.com/documentation/glkit/glksubmesh)
:::

:::topic-grid
## shader 기반 렌더링 effect
- [GLKNamedEffect](https://developer.apple.com/documentation/glkit/glknamedeffect): shader 기반 OpenGL 렌더링 effect를 제공하는 객체를 위한 표준 인터페이스입니다.
- [GLKBaseEffect](https://developer.apple.com/documentation/glkit/glkbaseeffect): shader 기반 OpenGL 렌더링에서 사용하는 단순한 lighting 및 shading 시스템입니다.
- [GLKReflectionMapEffect](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect): shader 기반 OpenGL 렌더링에서 reflection mapping을 지원하는 lighting 및 shading 시스템입니다.
- [GLKSkyboxEffect](https://developer.apple.com/documentation/glkit/glkskyboxeffect): shader 기반 OpenGL 렌더링에서 사용하는 단순한 skybox 시각 효과입니다.
:::

:::topic-grid
## 렌더링 effect 매개변수
- [GLKEffectProperty](https://developer.apple.com/documentation/glkit/glkeffectproperty): GLKit 렌더링 effect에 사용하는 구성 정보의 추상 superclass입니다.
- [GLKEffectPropertyFog](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog): GLKit 렌더링 effect에서 사용하는 안개 그리기 정보입니다.
- [GLKEffectPropertyLight](https://developer.apple.com/documentation/glkit/glkeffectpropertylight): GLKit 렌더링 effect에서 사용하는 조명 정보입니다.
- [GLKEffectPropertyTexture](https://developer.apple.com/documentation/glkit/glkeffectpropertytexture): GLKit 렌더링 effect에서 사용하는 텍스처 그리기 매개변수입니다.
- [GLKEffectPropertyMaterial](https://developer.apple.com/documentation/glkit/glkeffectpropertymaterial): GLKit 렌더링 effect에서 사용하는 표면 외관 속성입니다.
- [GLKEffectPropertyTransform](https://developer.apple.com/documentation/glkit/glkeffectpropertytransform): GLKit 렌더링 effect에서 사용하는 좌표 변환 정보입니다.
- [GLKit Effects Constants](https://developer.apple.com/documentation/glkit/glkit-effects-constants)
:::

:::topic-grid
## 수학 유틸리티
- [GLKMatrixStack](https://developer.apple.com/documentation/glkit/glkmatrixstack): 4 x 4 matrix의 stack을 나타내는 opaque 타입으로, 계층적 transform 모델링과 유사한 작업을 지원합니다.
- [GLKMatrix3](https://developer.apple.com/documentation/glkit/glkmatrix3-pcl)
- [GLKMatrix4](https://developer.apple.com/documentation/glkit/glkmatrix4-pce)
- [GLKVector2](https://developer.apple.com/documentation/glkit/glkvector2-pbj)
- [GLKVector3](https://developer.apple.com/documentation/glkit/glkvector3-pbt)
- [GLKVector4](https://developer.apple.com/documentation/glkit/glkvector4-pbk)
- [GLKQuaternion](https://developer.apple.com/documentation/glkit/glkquaternion-pc6)
- [GLKit Math Utilities](https://developer.apple.com/documentation/glkit/glkit-math-utilities)
:::

:::topic-grid
## 참고 자료
- [GLKit Structures](https://developer.apple.com/documentation/glkit/glkit-structures)
- [GLKit Enumerations](https://developer.apple.com/documentation/glkit/glkit-enumerations)
- [GLKit Constants](https://developer.apple.com/documentation/glkit/glkit-constants)
- [GLKit Functions](https://developer.apple.com/documentation/glkit/glkit-functions)
- [GLKit Data Types](https://developer.apple.com/documentation/glkit/glkit-data-types)
:::
