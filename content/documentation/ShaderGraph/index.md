---
route: /documentation/ShaderGraph
source_url: https://developer.apple.com/documentation/ShaderGraph
source_locale: en-US
section: docc
content_type: symbol
title: ShaderGraph
original_title: ShaderGraph
source_hash: 0c055ed82a6c1c7ac61b1d9bb63aef1a222c3ee73a886618a9ec6d3a2a73de62
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:08:27+00:00'
last_translated_at: '2026-03-13T22:06:00+09:00'
---

# ShaderGraph

Reality Composer Pro에서 3D 콘텐츠용 사용자 정의 재질과 효과를 만듭니다.

## 개요

Reality Composer Pro 안의 node 기반 재질 편집기인 Shader Graph를 사용하면 복잡한 재질과 효과를 만들 수 있습니다. 편집기는 다양한 시각 효과를 얻기 위해 node graph를 구성할 수 있는 인터페이스를 제공합니다.

Shader Graph가 재질에 대해 제공하는 제어 기능을 사용하면, 그렇지 않았다면 Metal shader를 직접 작성해야 했을지도 모르는 효과를 만들 수 있습니다. node는 값 또는 연산을 나타내며, 재질을 구성할 수 있도록 서로 연결하는 입력과 출력을 갖습니다. 이들은 Metal의 변수, 상수, 함수와 같은 역할을 합니다. 하나의 node에는 여러 버전이 있을 수 있으며, 함수 오버로드처럼 받을 수 있는 입력과 출력이 조금씩 다릅니다.

![](https://developer.apple.com)

원하는 시각적 효과와 기하 효과를 만드는 node를 사용해 재질을 구성하고, 이 재질을 Reality Composer Pro 장면 안의 entity에 적용하십시오.

## 상호 운용성

Shader Graph는 USD 파일 안에서 MaterialX를 읽고 작성할 수 있는 콘텐츠 제작 애플리케이션과의 상호 운용성을 높이기 위해 MaterialX 1.38 규약을 사용합니다.

Shader Graph에는 RealityKit 고유의 node도 여러 개 포함되어 있습니다. 이 중 일부 node는 콘텐츠 제작 워크플로에서 사용할 수 있는 표준 MaterialX 정의로도 제공됩니다. 이러한 정의를 다운로드하려면 [MaterialX definitions](https://developer.apple.com/augmented-reality/realitykit/files/MaterialX-definitions.zip)를 참고하십시오.

:::topic-grid
## 노드 카테고리
- [2D-Procedural](https://developer.apple.com/documentation/shadergraph/2d-procedural): 재질을 위해 2D 그라디언트, 노이즈, 기타 패턴을 프로그래밍 방식으로 생성합니다.
- [2D-Texture](https://developer.apple.com/documentation/shadergraph/2d-texture): 2D 텍스처 파일을 로드하고 구성합니다.
- [3D-Procedural](https://developer.apple.com/documentation/shadergraph/3d-procedural): 재질을 위해 3D 노이즈 패턴을 프로그래밍 방식으로 생성합니다.
- [3D-Texture](https://developer.apple.com/documentation/shadergraph/3d-texture): 여러 2D 이미지를 표면에 투영해 3D 텍스처를 만듭니다.
- [Adjustment](https://developer.apple.com/documentation/shadergraph/adjustment): 값이나 값의 범위를 한 형태에서 다른 형태로 수정하거나 변환합니다.
- [Application](https://developer.apple.com/documentation/shadergraph/application): 현재 시간이나 up vector의 방향 같은 시스템 값을 가져옵니다.
- [Compositing](https://developer.apple.com/documentation/shadergraph/compositing): 여러 데이터 값을 결합해 하나의 출력을 생성합니다.
- [Data](https://developer.apple.com/documentation/shadergraph/data): 데이터 값을 다른 형식으로 변환하거나 데이터 구조 안의 개별 요소를 조작합니다.
- [Geometric](https://developer.apple.com/documentation/shadergraph/geometric): 그래프가 실행되는 동안 장면 geometry에 접근합니다.
- [Logic](https://developer.apple.com/documentation/shadergraph/logic): 데이터 값에 대해 Boolean 연산과 기타 논리 비교를 수행합니다.
- [Material](https://developer.apple.com/documentation/shadergraph/material): shader graph node 집합을 하나의 모듈로 캡슐화합니다.
- [Math](https://developer.apple.com/documentation/shadergraph/math): 데이터 값에 대해 다양한 수학 연산과 변환 연산을 수행합니다.
- [Organization](https://developer.apple.com/documentation/shadergraph/organization): 값은 바꾸지 않으면서 그래프 안에서 데이터의 시각적 흐름을 수정합니다.
- [Procedural](https://developer.apple.com/documentation/shadergraph/procedural): 그래프에 상수 숫자, vector, matrix, color, string 또는 기타 값을 추가합니다.
- [RealityKit](https://developer.apple.com/documentation/shadergraph/realitykit): RealityKit 표면이나 텍스처를 재질에 추가하고 장면 geometry에 접근해 조작합니다.
- [Surface](https://developer.apple.com/documentation/shadergraph/surface): MaterialX preview surface를 생성합니다.
:::

:::asset-list
- `https://developer.apple.com/augmented-reality/realitykit/files/MaterialX-definitions.zip` -> `https://developer.apple.com/augmented-reality/realitykit/files/MaterialX-definitions.zip` (pending)
:::
