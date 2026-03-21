---
route: /documentation/GameplayKit
source_url: https://developer.apple.com/documentation/GameplayKit
source_locale: en-US
section: docc
content_type: symbol
title: GameplayKit
original_title: GameplayKit
source_hash: b860e174ca5f7a3ef708fcb4bc17d374c9aa3f650e09945daf2af14b22c71488
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:13:40+00:00'
last_translated_at: '2026-03-13T22:24:00+09:00'
---

# GameplayKit

게임 로직을 설계하고 구성합니다. 난수 생성, 인공 지능, 경로 탐색, agent 동작 같은 일반적인 게임플레이 동작을 통합합니다.

## 개요

GameplayKit은 게임을 구축하기 위한 기초 도구와 기술을 제공하는 객체 지향 프레임워크입니다. GameplayKit에는 기능적이고 재사용 가능한 아키텍처로 게임을 설계하기 위한 도구와, 캐릭터 이동 및 상대 동작 같은 게임플레이 기능을 구축하고 향상하기 위한 기술이 포함되어 있습니다.

### GameplayKit 시작하기

GameplayKit은 게임 설계와 개발의 많은 측면을 다룹니다. GameplayKit으로 활용할 수 있는 게임 설계 패턴에 대한 더 깊은 논의와, GameplayKit 기능으로 게임을 만드는 과정을 보여 주는 튜토리얼은 [GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172)를 참고하십시오.

### 관련 샘플 코드

실제로 동작하는 GameplayKit을 실험해 보려면 다음 샘플 코드 프로젝트를 참고하십시오.

- [Boxes: GameplayKit Entity-Component Basics](https://developer.apple.com/library/archive/samplecode/Boxes_GamePlayKit/Introduction/Intro.html#//apple_ref/doc/uid/TP40016459)
- [Dispenser: GameplayKit State Machine Basics](https://developer.apple.com/library/archive/samplecode/Dispenser_GameplayKit/Introduction/Intro.html#//apple_ref/doc/uid/TP40016460)
- [Pathfinder: GameplayKit Pathfinding Basics](https://developer.apple.com/library/archive/samplecode/Pathfinder_GameplayKit/Introduction/Intro.html#//apple_ref/doc/uid/TP40016461)
- [AgentsCatalog: Using the Agents System in GameplayKit](https://developer.apple.com/library/archive/samplecode/AgentsCatalog/Introduction/Intro.html#//apple_ref/doc/uid/TP40016141)
- [FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI](https://developer.apple.com/library/archive/samplecode/FourInARow/Introduction/Intro.html#//apple_ref/doc/uid/TP40016142)
- [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](https://developer.apple.com/library/archive/samplecode/DemoBots/Introduction/Intro.html#//apple_ref/doc/uid/TP40015179)

:::topic-grid
## 엔티티와 컴포넌트
- [GKEntity](https://developer.apple.com/documentation/gameplaykit/gkentity): 기능이 전적으로 component 객체 모음으로 제공되는, 게임플레이와 관련된 객체입니다.
- [GKComponent](https://developer.apple.com/documentation/gameplaykit/gkcomponent): 엔티티에 특정 게임플레이 기능을 추가하는 객체를 만들기 위한 추상 superclass입니다.
- [GKComponentSystem](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem): 지정된 클래스의 모든 component 객체에 대한 주기적 update 메시지를 관리합니다.
:::

:::topic-grid
## 상태 머신
- [GKState](https://developer.apple.com/documentation/gameplaykit/gkstate): 상태 머신의 일부로 상태별 로직을 정의하기 위한 추상 superclass입니다.
- [GKStateMachine](https://developer.apple.com/documentation/gameplaykit/gkstatemachine): 유한 상태 머신으로, 게임플레이의 특정 상태에 대한 로직과 상태 전이 규칙을 각각 정의하는 상태 객체 모음입니다.
:::

:::topic-grid
## 공간 분할
- [GKQuadtree](https://developer.apple.com/documentation/gameplaykit/gkquadtree): 2차원 공간 안의 위치를 기준으로 객체를 조직하는 데이터 구조입니다.
- [GKQuadtreeNode](https://developer.apple.com/documentation/gameplaykit/gkquadtreenode): quadtree 안에 배치한 객체를 관리하는 보조 클래스입니다.
- [GKOctree](https://developer.apple.com/documentation/gameplaykit/gkoctree): 3차원 공간 안의 위치를 기준으로 객체를 조직하는 데이터 구조입니다.
- [GKOctreeNode](https://developer.apple.com/documentation/gameplaykit/gkoctreenode): octree 안에 배치한 객체를 관리하는 보조 클래스입니다.
- [GKRTree](https://developer.apple.com/documentation/gameplaykit/gkrtree): 2차원 공간 안의 위치에 따라 적응적으로 객체를 조직하는 데이터 구조입니다.
:::

:::topic-grid
## strategist
- [GKStrategist](https://developer.apple.com/documentation/gameplaykit/gkstrategist): 턴 기반 게임과 유사한 게임에서 사용할 인공 지능을 제공하는 객체를 위한 일반 인터페이스입니다.
- [GKMinmaxStrategist](https://developer.apple.com/documentation/gameplaykit/gkminmaxstrategist): 전략을 사용해 턴 기반 게임에서 수를 선택하는 AI입니다.
- [GKMonteCarloStrategist](https://developer.apple.com/documentation/gameplaykit/gkmontecarlostrategist): 전략을 사용해 턴 기반 게임에서 수를 선택하는 AI입니다.
- [GKGameModel](https://developer.apple.com/documentation/gameplaykit/gkgamemodel): strategist 객체가 게임 수를 계획할 수 있도록 게임플레이 모델을 설명하기 위해 이 프로토콜을 구현합니다.
- [GKGameModelPlayer](https://developer.apple.com/documentation/gameplaykit/gkgamemodelplayer): strategist 객체가 게임 수를 계획할 수 있도록 턴 기반 게임의 플레이어를 설명하기 위해 이 프로토콜을 구현합니다.
- [GKGameModelUpdate](https://developer.apple.com/documentation/gameplaykit/gkgamemodelupdate): strategist 객체가 게임 수를 계획할 수 있도록 턴 기반 게임의 이동을 설명하기 위해 이 프로토콜을 구현합니다.
:::

:::topic-grid
## 의사 결정 트리
- [GKDecisionTree](https://developer.apple.com/documentation/gameplaykit/gkdecisiontree): 특정 질문 집합, 가능한 답변, 그리고 일련의 답변 뒤에 따르는 동작을 모델링하는 데이터 구조입니다.
- [GKDecisionNode](https://developer.apple.com/documentation/gameplaykit/gkdecisionnode): 의사 결정 트리를 수동으로 만들 때 사용하는 node로, 특정 질문과 가능한 답변 또는 다른 질문들에 대한 답변 뒤에 이어지는 동작을 표현합니다.
:::

:::topic-grid
## 경로 탐색
- [GKGraph](https://developer.apple.com/documentation/gameplaykit/gkgraph): 게임 세계의 이동 가능성을 설명하고 그 공간 안의 경로를 검색하는 메서드를 제공하는 node 모음입니다.
- [GKObstacleGraph](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph): 장애물 주위의 정밀한 pathfinding을 위해 최소 네트워크를 생성하는 2D 게임 세계용 navigation graph입니다.
- [GKMeshGraph](https://developer.apple.com/documentation/gameplaykit/gkmeshgraph): 장애물 주위의 부드러운 pathfinding을 위해 공간을 채우는 네트워크를 생성하는 2D 게임 세계용 navigation graph입니다.
- [GKGridGraph](https://developer.apple.com/documentation/gameplaykit/gkgridgraph): 이동이 정수 격자로 제한되는 2D 게임 세계용 navigation graph입니다.
- [GKGraphNode](https://developer.apple.com/documentation/gameplaykit/gkgraphnode): pathfinding에 사용하는 navigation graph의 단일 node입니다.
- [GKGraphNode2D](https://developer.apple.com/documentation/gameplaykit/gkgraphnode2d): 연속적인 2D 공간의 한 점과 연관된 navigation graph의 node입니다.
- [GKGraphNode3D](https://developer.apple.com/documentation/gameplaykit/gkgraphnode3d): 연속적인 3D 공간의 한 점과 연관된 navigation graph의 node입니다.
- [GKGridGraphNode](https://developer.apple.com/documentation/gameplaykit/gkgridgraphnode): 이산적인 2차원 격자 위의 위치와 연관된 navigation graph의 node입니다.
:::

:::topic-grid
## agent, goal, behavior
- [GKAgent](https://developer.apple.com/documentation/gameplaykit/gkagent): 목표 집합과 현실적인 제약에 따라 게임 엔티티를 이동시키는 component입니다.
- [GKAgent2D](https://developer.apple.com/documentation/gameplaykit/gkagent2d): 2차원 공간에서 동작하는 agent입니다.
- [GKAgent3D](https://developer.apple.com/documentation/gameplaykit/gkagent3d): 3차원 공간에서 동작하는 agent입니다.
- [GKGoal](https://developer.apple.com/documentation/gameplaykit/gkgoal): 하나 이상의 agent 이동을 유도하는 영향입니다.
- [GKBehavior](https://developer.apple.com/documentation/gameplaykit/gkbehavior): 함께 agent의 이동에 영향을 주는 목표 집합입니다.
- [GKCompositeBehavior](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior): 각각 목표 집합인 여러 behavior의 집합으로, 함께 agent의 이동에 영향을 줍니다.
- [GKPath](https://developer.apple.com/documentation/gameplaykit/gkpath): agent가 따라갈 수 있는 polygonal path입니다.
- [GKAgentDelegate](https://developer.apple.com/documentation/gameplaykit/gkagentdelegate): 게임 안에서 agent의 상태를 시각적 표현과 동기화하기 위해 이 프로토콜을 구현합니다.
:::

:::topic-grid
## 장애물
- [GKObstacle](https://developer.apple.com/documentation/gameplaykit/gkobstacle): 게임 세계에서 통과할 수 없는 영역을 표현하는 객체를 위한 추상 기본 클래스입니다.
- [GKCircleObstacle](https://developer.apple.com/documentation/gameplaykit/gkcircleobstacle): agent가 피해야 하는 원형 통과 불가 영역입니다.
- [GKSphereObstacle](https://developer.apple.com/documentation/gameplaykit/gksphereobstacle): agent가 피해야 하는 구형 통과 불가 체적입니다.
- [GKPolygonObstacle](https://developer.apple.com/documentation/gameplaykit/gkpolygonobstacle): 2D 게임 세계의 다각형 모양 통과 불가 영역입니다.
:::

:::topic-grid
## 절차적 노이즈
- [GKNoiseSource](https://developer.apple.com/documentation/gameplaykit/gknoisesource): 절차적 노이즈 생성기의 추상 superclass입니다.
- [GKNoise](https://developer.apple.com/documentation/gameplaykit/gknoise): 노이즈 소스로 생성된 절차적 노이즈를 표현하며, 노이즈를 처리, 변환, 결합하는 데 사용할 수 있습니다.
- [GKNoiseMap](https://developer.apple.com/documentation/gameplaykit/gknoisemap): 절차적 노이즈 데이터의 샘플로, 여기서 직접 노이즈 값을 읽거나 노이즈 텍스처를 만들 수 있습니다.
- [GKCoherentNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkcoherentnoisesource): 일관된 노이즈를 생성하는 절차적 노이즈 생성기의 추상 superclass입니다.
- [GKBillowNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkbillownoisesource): 출력이 부드러운 특징을 가진 fractal coherent noise 유형인 절차적 노이즈 생성기입니다.
- [GKPerlinNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkperlinnoisesource): 출력이 구름과 지형 같은 자연 현상을 닮은 fractal coherent noise 유형인 절차적 노이즈 생성기입니다.
- [GKRidgedNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkridgednoisesource): 출력이 날카롭게 정의된 특징을 가진 multifractal coherent noise 유형인 절차적 노이즈 생성기입니다.
- [GKVoronoiNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkvoronoinoisesource): 출력(워र्ल리 노이즈 또는 cellular noise라고도 함)이 임의의 seed point 주변에 불연속적인 cell을 나누는 절차적 노이즈 생성기입니다.
- [GKCylindersNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkcylindersnoisesource): 출력이 동심 원통 껍질의 3D 필드인 절차적 노이즈 생성기입니다.
- [GKSpheresNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkspheresnoisesource): 출력이 동심 구형 껍질의 3D 필드인 절차적 노이즈 생성기입니다.
- [GKCheckerboardNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkcheckerboardnoisesource): 출력이 번갈아 나타나는 정사각형 패턴인 절차적 노이즈 생성기입니다.
- [GKConstantNoiseSource](https://developer.apple.com/documentation/gameplaykit/gkconstantnoisesource): 하나의 상수 값 필드를 출력하는 절차적 노이즈 생성기입니다.
:::

:::topic-grid
## 무작위화
- [GKRandom](https://developer.apple.com/documentation/gameplaykit/gkrandom): GameplayKit 안의, 또는 GameplayKit과 함께 사용할 수 있는 모든 무작위화 클래스의 공통 인터페이스입니다.
- [GKRandomSource](https://developer.apple.com/documentation/gameplaykit/gkrandomsource): GameplayKit의 모든 기본 무작위화 클래스의 superclass입니다.
- [GKARC4RandomSource](https://developer.apple.com/documentation/gameplaykit/gkarc4randomsource): ARC4 알고리즘을 구현한 기본 난수 생성기로, 대부분의 게임플레이 메커니즘에 적합합니다.
- [GKLinearCongruentialRandomSource](https://developer.apple.com/documentation/gameplaykit/gklinearcongruentialrandomsource): 선형 합동 생성기 알고리즘을 구현한 기본 난수 생성기로, 기본 random source보다 빠르지만 무작위성은 낮습니다.
- [GKMersenneTwisterRandomSource](https://developer.apple.com/documentation/gameplaykit/gkmersennetwisterrandomsource): Mersenne Twister 알고리즘을 구현한 기본 난수 생성기로, 기본 random source보다 더 무작위적이지만 더 느립니다.
- [GKRandomDistribution](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution): 특정 범위 안에 있으며 여러 번 샘플링했을 때 특정 분포를 보이는 난수를 생성하는 생성기입니다.
- [GKGaussianDistribution](https://developer.apple.com/documentation/gameplaykit/gkgaussiandistribution): 여러 번 샘플링했을 때 정규 분포(가우시안 분포라고도 함)를 따르는 난수를 생성하는 생성기입니다.
- [GKShuffledDistribution](https://developer.apple.com/documentation/gameplaykit/gkshuffleddistribution): 여러 번 샘플링했을 때는 균등 분포를 보이지만, 짧은 구간에서 비슷한 값이 연속으로 나올 가능성은 낮은 난수 생성기입니다.
:::

:::topic-grid
## 규칙 시스템
- [GKRule](https://developer.apple.com/documentation/gameplaykit/gkrule): 규칙 시스템 문맥에서 사용되는 규칙으로, 테스트할 predicate와 테스트가 성공했을 때 실행할 action을 가집니다.
- [GKNSPredicateRule](https://developer.apple.com/documentation/gameplaykit/gknspredicaterule): 자신을 평가하기 위해 Foundation 객체를 사용하는 규칙 시스템용 규칙입니다.
- [GKRuleSystem](https://developer.apple.com/documentation/gameplaykit/gkrulesystem): 규칙 목록과, 그것들을 평가하고 결과를 해석하는 문맥을 함께 제공하여 데이터 기반 로직이나 퍼지 로직 시스템을 구성하는 데 사용하는 시스템입니다.
:::

:::topic-grid
## Xcode 및 SpriteKit 통합
- [GKScene](https://developer.apple.com/documentation/gameplaykit/gkscene): GameplayKit 객체를 SpriteKit scene과 연관시키는 컨테이너입니다.
- [GKSceneRootNodeType](https://developer.apple.com/documentation/gameplaykit/gkscenerootnodetype): 내장된 GameplayKit 정보를 지원하는 다른 프레임워크의 scene 클래스를 식별합니다.
- [GKSKNodeComponent](https://developer.apple.com/documentation/gameplaykit/gksknodecomponent): SpriteKit node를 관리하는 component입니다.
:::

:::topic-grid
## 참고 자료
- [GameplayKit Constants](https://developer.apple.com/documentation/gameplaykit/gameplaykit-constants)
- [GameplayKit Structures](https://developer.apple.com/documentation/gameplaykit/gameplaykit-structures)
- [GameplayKit Enumerations](https://developer.apple.com/documentation/gameplaykit/gameplaykit-enumerations)
:::

:::topic-grid
## 클래스
- [GKSCNNodeComponent](https://developer.apple.com/documentation/gameplaykit/gkscnnodecomponent)
:::
