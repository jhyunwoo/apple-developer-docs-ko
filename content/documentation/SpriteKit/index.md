---
route: /documentation/SpriteKit
source_url: https://developer.apple.com/documentation/SpriteKit
source_locale: en-US
section: docc
content_type: symbol
title: SpriteKit
original_title: SpriteKit
source_hash: 830370890f90ef03d1fc834ccdfb3cdf8ebf5e38c55bbea41ea698a3f7723814
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:42:57+00:00'
last_translated_at: '2026-03-13T23:42:57+09:00'
---

# SpriteKit

부드러운 애니메이션이 포함된 고성능 2D 콘텐츠를 앱에 추가하거나, 고수준 2D 게임 도구 모음을 사용해 게임을 만듭니다.

## 개요

SpriteKit은 2차원에서 도형, 파티클, 텍스트, 이미지, 비디오를 그리기 위한 범용 프레임워크입니다. Metal을 활용해 고성능 렌더링을 구현하면서도 간단한 프로그래밍 인터페이스를 제공하므로, 게임과 그래픽 집약적 앱을 쉽게 만들 수 있습니다. 풍부한 애니메이션과 물리 동작 세트를 사용해 시각 요소에 빠르게 생동감을 더하고 화면 전환도 자연스럽게 구성할 수 있습니다.

SpriteKit은 iOS, macOS, tvOS, watchOS에서 지원되며 GameplayKit, SceneKit 같은 프레임워크와도 잘 통합됩니다. visionOS에서 실행되는 호환 iPhone 또는 iPad 앱 안에서는 SpriteKit을 사용할 수 있지만, visionOS 전용 앱을 만들 때는 사용하지 마십시오.

:::topic-grid
## 핵심
- [뷰 안에 SpriteKit 콘텐츠 그리기](https://developer.apple.com/documentation/spritekit/drawing-spritekit-content-in-a-view): SpriteKit을 사용해 시각 콘텐츠를 표시합니다.
- [SKScene](https://developer.apple.com/documentation/spritekit/skscene): 활성화된 모든 SpriteKit 콘텐츠를 구성하는 객체입니다.
- [Nodes for Scene Building](https://developer.apple.com/documentation/spritekit/nodes-for-scene-building): 장면 콘텐츠의 모양과 배치를 정의합니다.
:::

:::topic-grid
## 장면 렌더러
- [SpriteKit Scene Renderer 선택하기](https://developer.apple.com/documentation/spritekit/choosing-a-spritekit-scene-renderer): SpriteKit 장면을 표시하는 여러 방법을 비교합니다.
- [SKView](https://developer.apple.com/documentation/spritekit/skview): SpriteKit 장면을 렌더링하는 view 하위 클래스입니다.
- [SKRenderer](https://developer.apple.com/documentation/spritekit/skrenderer): 장면을 사용자화한 Metal 렌더링 파이프라인에 렌더링하고 장면 update cycle을 구동하는 객체입니다.
- [WKInterfaceSKScene](https://developer.apple.com/documentation/WatchKit/WKInterfaceSKScene): SpriteKit 장면을 표시하는 시각적 WatchKit 요소입니다.
:::

:::topic-grid
## 텍스처
- [Texture 성능 극대화하기](https://developer.apple.com/documentation/spritekit/maximizing-texture-performance): 이미지 표시 속도를 높이고 한 번에 더 많은 이미지를 표시할 수 있게 합니다.
- [SKTexture](https://developer.apple.com/documentation/spritekit/sktexture): GPU에서 디코딩되어 다양한 SpriteKit 객체를 렌더링하는 데 사용할 수 있는 이미지입니다.
- [SKTextureAtlas](https://developer.apple.com/documentation/spritekit/sktextureatlas): 저장 및 드로잉 성능에 최적화된 texture 모음입니다.
- [SKMutableTexture](https://developer.apple.com/documentation/spritekit/skmutabletexture): 내용을 동적으로 갱신할 수 있는 texture입니다.
:::

:::topic-grid
## 애니메이션
- [Action 시작하기](https://developer.apple.com/documentation/spritekit/getting-started-with-actions): SpriteKit에서 action을 만들고 구성하고 실행합니다.
- [SKAction](https://developer.apple.com/documentation/spritekit/skaction): 노드가 자신의 구조나 콘텐츠를 변경하기 위해 실행하는 객체입니다.
:::

:::topic-grid
## 제약 조건
- [SKConstraint](https://developer.apple.com/documentation/spritekit/skconstraint): 노드의 위치나 회전을 제한하기 위한 사양입니다.
- [SKReachConstraints](https://developer.apple.com/documentation/spritekit/skreachconstraints): inverse kinematics를 풀 때 자유도를 정의하는 사양입니다.
:::

:::topic-grid
## 수학 도구
- [SKKeyframeSequence](https://developer.apple.com/documentation/spritekit/skkeyframesequence): 서로 다른 시점에 지정된 값들(keyframe) 사이를 보간하는 객체입니다.
- [SKRange](https://developer.apple.com/documentation/spritekit/skrange): 부동소수점 값 범위를 정의합니다.
- [SKRegion](https://developer.apple.com/documentation/spritekit/skregion): 임의 영역의 정의입니다.
:::

:::topic-grid
## 물리 시뮬레이션
- [물리 기능 시작하기](https://developer.apple.com/documentation/spritekit/getting-started-with-physics): 중력, 가속도, 충돌 감지, joint를 시뮬레이션합니다.
- [SKPhysicsWorld](https://developer.apple.com/documentation/spritekit/skphysicsworld): 장면의 physics engine을 구동하며, 물리 시스템을 구성하고 조회할 수 있게 하는 객체입니다.
- [SKPhysicsBody](https://developer.apple.com/documentation/spritekit/skphysicsbody): 노드에 물리 시뮬레이션을 추가하는 객체입니다.
- [SKPhysicsContact](https://developer.apple.com/documentation/spritekit/skphysicscontact): 두 physics body 간 접촉을 설명합니다.
- [SKPhysicsContactDelegate](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate): physics body가 접촉했을 때 앱이 응답할 수 있도록 구현하는 메서드입니다.
- [SKFieldNode](https://developer.apple.com/documentation/spritekit/skfieldnode): 주변 노드에 물리 효과를 적용하는 노드입니다.
:::

:::topic-grid
## 물리 joint
- [Inverse Kinematics 다루기](https://developer.apple.com/documentation/spritekit/working-with-inverse-kinematics): joint로 연결된 객체를 더 정밀하게 제어합니다.
- [SKPhysicsJoint](https://developer.apple.com/documentation/spritekit/skphysicsjoint): physics body를 연결하는 객체의 추상 상위 클래스입니다.
- [SKPhysicsJointFixed](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed): 기준점에서 두 physics body를 고정 결합하는 joint입니다.
- [SKPhysicsJointLimit](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit): 두 physics body 사이의 최대 거리를 제한하는 joint로, 마치 밧줄로 연결된 것처럼 동작합니다.
- [SKPhysicsJointPin](https://developer.apple.com/documentation/spritekit/skphysicsjointpin): 독립적인 회전을 허용하면서 두 physics body를 고정하는 joint입니다.
- [SKPhysicsJointSliding](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding): 두 physics body가 특정 축을 따라 미끄러질 수 있게 하는 joint입니다.
- [SKPhysicsJointSpring](https://developer.apple.com/documentation/spritekit/skphysicsjointspring): 두 physics body를 잇는 스프링을 시뮬레이션하는 joint입니다.
:::

:::topic-grid
## 타일링
- [SKTileMapNode](https://developer.apple.com/documentation/spritekit/sktilemapnode): 2차원 이미지 배열입니다.
- [SKTileDefinition](https://developer.apple.com/documentation/spritekit/sktiledefinition): tile map 안에서 반복할 수 있는 단일 타일입니다.
- [SKTileGroup](https://developer.apple.com/documentation/spritekit/sktilegroup): 하나의 지형 유형을 함께 정의하는 타일 집합입니다.
- [SKTileGroupRule](https://developer.apple.com/documentation/spritekit/sktilegrouprule): 지도의 여러 타일을 어떻게 배치할지 설명하는 규칙입니다.
- [SKTileSet](https://developer.apple.com/documentation/spritekit/sktileset): 관련 tile group의 컨테이너입니다.
:::

:::topic-grid
## 셰이더
- [SKShader](https://developer.apple.com/documentation/spritekit/skshader): 사용자화 fragment shader를 적용할 수 있게 하는 객체입니다.
- [SKAttribute](https://developer.apple.com/documentation/spritekit/skattribute): 사용자화 shader와 함께 사용하는 동적 per-node 데이터의 사양입니다.
- [SKAttributeValue](https://developer.apple.com/documentation/spritekit/skattributevalue): 노드와 연결된 동적 shader 데이터의 컨테이너입니다.
- [SKUniform](https://developer.apple.com/documentation/spritekit/skuniform): uniform shader 데이터의 컨테이너입니다.
:::

:::topic-grid
## 워핑
- [SKWarpGeometry](https://developer.apple.com/documentation/spritekit/skwarpgeometry): 워프 가능한 노드의 변형 정의입니다.
- [SKWarpGeometryGrid](https://developer.apple.com/documentation/spritekit/skwarpgeometrygrid): 워프 가능한 노드의 격자 기반 변형 정의입니다.
- [SKWarpable](https://developer.apple.com/documentation/spritekit/skwarpable): `SKWarpGeometry`로 워프 및 애니메이션할 수 있는 객체용 프로토콜입니다.
:::

:::topic-grid
## 참고 자료
- [SpriteKit Enumerations](https://developer.apple.com/documentation/spritekit/spritekit-enumerations): SpriteKit 전반에서 사용하는 열거형입니다.
- [SpriteKit Data Types](https://developer.apple.com/documentation/spritekit/spritekit-data-types): SpriteKit 전반에서 사용하는 데이터 타입입니다.
- [SpriteKit Constants](https://developer.apple.com/documentation/spritekit/spritekit-constants): SpriteKit 전반에서 사용하는 상수입니다.
- [SpriteKit Type Aliases](https://developer.apple.com/documentation/spritekit/spritekit-type-aliases): SpriteKit 전반에서 사용하는 type alias입니다.
- [SpriteKit Variables](https://developer.apple.com/documentation/spritekit/spritekit-variables): SpriteKit 전반에서 사용하는 전역 변수와 매크로입니다.
:::

:::topic-grid
## 구조체
- [SpriteView](https://developer.apple.com/documentation/spritekit/spriteview): SpriteKit 장면을 렌더링하는 SwiftUI view입니다.
:::
