---
route: /documentation/TabletopKit
source_url: https://developer.apple.com/documentation/TabletopKit
source_locale: en-US
section: docc
content_type: symbol
title: TabletopKit
original_title: TabletopKit
source_hash: c5d25c8b04f88201294f9cda8a08aaa2b345d998d26e92f4076240040c736cb7
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:55:51+00:00'
last_translated_at: '2026-03-13T16:05:00+09:00'
---

# TabletopKit

가상 테이블 표면 위에서 멀티플레이어 공간 게임을 만들고 FaceTime을 사용해 플레이어를 초대합니다.

## 개요

TabletopKit은 플레이어가 SharePlay를 사용해 참여하는 visionOS용 테이블 표면 기반의 공간 멀티플레이어 게임을 만드는 데 도움을 줍니다. TabletopKit은 게임 설계, 규칙 구현, 효과 렌더링, 멀티플레이어 게임 상태 동기화를 지원합니다.

![visionOS의 공간 모드에서 실행되는 테이블탑 게임 표현입니다.](https://developer.apple.com)

TabletopKit 게임을 구현하려면 다음 단계를 따르십시오.

- 테이블 위에 게임을 구성하고 플레이어가 상호 작용할 게임 말이나 장비를 만듭니다. 게임과 게임 요소를 그리는 renderer는 직접 제공합니다.
- 게임 규칙과 플레이어가 장비와 상호 작용하는 방식을 구현합니다. TabletopKit은 플레이어 제스처를 상호 작용으로 처리하고 표현합니다. 이러한 상호 작용을 관찰하고 게임 고유의 action을 추가합니다.
- 렌더링 가능한 장비의 RealityKit entity에 효과를 추가하고 상호 작용 중에 이를 트리거합니다. 예를 들어 플레이어가 말을 던질 때 음향 효과를 재생하거나 목표를 달성했을 때 애니메이션을 실행할 수 있습니다.
- SharePlay를 사용해 멀티플레이어를 설정합니다. Group Activities 세션을 시작하고 이를 TabletopKit에 제공합니다. 그런 다음 게임의 공간 경험을 사용자화합니다. 예를 들어 플레이어를 각 좌석에 배치하고 관전자를 방 안의 주변에 배치할 수 있습니다.

시작하려면 게임 인스턴스를 나타내는 [TabletopGame](https://developer.apple.com/documentation/tabletopkit/tabletopgame) 객체와 게임 레이아웃 및 장비를 나타내는 [TableSetup](https://developer.apple.com/documentation/tabletopkit/tablesetup) 객체를 만드십시오.

:::topic-grid
## 핵심 사항
- [Creating tabletop games](https://developer.apple.com/documentation/tabletopkit/creating-tabletop-games): 여러 플레이어가 테이블 위 말과 상호 작용하는 공간 보드 게임을 개발합니다.
- [Synchronizing group gameplay with TabletopKit](https://developer.apple.com/documentation/tabletopkit/synchronizing-group-gameplay-with-tabletopkit): 모든 동전을 차지하기 위해 경쟁하는 게임에서 여러 플레이어 간 게임 상태를 유지합니다.
- [TabletopGame](https://developer.apple.com/documentation/tabletopkit/tabletopgame): 테이블탑 게임의 설정과 플레이를 관리하는 객체입니다.
- [TableSetup](https://developer.apple.com/documentation/tabletopkit/tablesetup): 게임 테이블 주변의 좌석, 장비, 카운터 배치를 나타내는 객체입니다.
- [Tabletop](https://developer.apple.com/documentation/tabletopkit/tabletop): 게임의 테이블 표면을 위한 프로토콜입니다.
- [EntityTabletop](https://developer.apple.com/documentation/tabletopkit/entitytabletop): RealityKit을 사용해 렌더링할 때 게임의 테이블 표면을 위한 프로토콜입니다.
- [TabletopShape](https://developer.apple.com/documentation/tabletopkit/tabletopshape): 테이블의 물리적 속성을 나타내는 객체입니다.
:::

:::topic-grid
## 좌석
- [TableState](https://developer.apple.com/documentation/tabletopkit/tablestate): 조회하고 수정할 수 있는 테이블 상태입니다.
- [TableSeat](https://developer.apple.com/documentation/tabletopkit/tableseat): 플레이어가 차지하는 테이블 좌석을 위한 프로토콜입니다.
- [EntityTableSeat](https://developer.apple.com/documentation/tabletopkit/entitytableseat): RealityKit으로 렌더링하는 테이블 좌석을 위한 프로토콜입니다.
- [TableSeatIdentifier](https://developer.apple.com/documentation/tabletopkit/tableseatidentifier): 좌석을 위한 고유 식별자입니다.
- [TableSeatState](https://developer.apple.com/documentation/tabletopkit/tableseatstate): 플레이어가 차지한 좌석과 연관된 데이터입니다.
- [SeatState](https://developer.apple.com/documentation/tabletopkit/seatstate): TabletopKit이 플레이어 간에 동기화하는 좌석 데이터용 프로토콜입니다.
:::

:::topic-grid
## 장비
- [Implementing playing card overlap and physical characteristics](https://developer.apple.com/documentation/tabletopkit/implementing-playing-card-overlap-and-physical-characteristics): 실제처럼 쌓이고 겹치는 동작을 갖는 카드 더미에 상호 작용 가능한 카드 게임 동작을 추가합니다.
- [Equipment](https://developer.apple.com/documentation/tabletopkit/equipment): 게임에서 플레이어가 직접 상호 작용하는 장비를 위한 프로토콜입니다.
- [EquipmentCollection](https://developer.apple.com/documentation/tabletopkit/equipmentcollection): 상태를 검사하고 수정할 수 있는 장비 모음입니다.
- [EntityEquipment](https://developer.apple.com/documentation/tabletopkit/entityequipment): RealityKit을 사용해 렌더링하는 게임 장비용 프로토콜입니다.
- [EquipmentIdentifier](https://developer.apple.com/documentation/tabletopkit/equipmentidentifier): 장비를 위한 고유 식별자입니다.
- [EquipmentState](https://developer.apple.com/documentation/tabletopkit/equipmentstate): TabletopKit이 플레이어 간에 동기화하는 장비 데이터용 프로토콜입니다.
- [EquipmentStateCollection](https://developer.apple.com/documentation/tabletopkit/equipmentstatecollection): 검사하고 수정할 수 있는 장비 상태 모음입니다.
- [BaseEquipmentState](https://developer.apple.com/documentation/tabletopkit/baseequipmentstate): 장비별 데이터가 포함되지 않은 장비 상태입니다.
- [CustomEquipmentState](https://developer.apple.com/documentation/tabletopkit/customequipmentstate): TabletopKit이 플레이어 간에 동기화하는 사용자 정의 데이터를 수용할 수 있도록 하는 특수 장비 상태 프로토콜입니다.
- [MutableEquipmentState](https://developer.apple.com/documentation/tabletopkit/mutableequipmentstate): TabletopKit이 플레이어 간에 동기화하며 변경 가능한 장비 데이터용 프로토콜입니다.
- [CardState](https://developer.apple.com/documentation/tabletopkit/cardstate): 앞면과 뒷면 정보를 포함하는 카드 상태입니다.
- [DieState](https://developer.apple.com/documentation/tabletopkit/diestate): 현재 값을 포함하는 주사위 상태입니다.
- [RawValueState](https://developer.apple.com/documentation/tabletopkit/rawvaluestate): 게임 고유 값을 포함하는 장비 상태입니다.
- [ControllingSeats](https://developer.apple.com/documentation/tabletopkit/controllingseats): 장비를 조작하거나 상호 작용할 수 있는 좌석입니다.
:::

:::topic-grid
## 장비 레이아웃
- [EquipmentLayout](https://developer.apple.com/documentation/tabletopkit/equipmentlayout): 장비 레이아웃을 설명하는 객체용 프로토콜입니다.
- [DefaultEquipmentLayout](https://developer.apple.com/documentation/tabletopkit/defaultequipmentlayout): 장비 레이아웃을 위한 표준 구성을 제공하는 객체입니다.
- [EquipmentPose2D](https://developer.apple.com/documentation/tabletopkit/equipmentpose2d): XZ 평면 위 장비의 위치와 회전을 나타내는 객체입니다.
- [EquipmentPose3D](https://developer.apple.com/documentation/tabletopkit/equipmentpose3d): 테이블 위 장비의 3차원 위치와 방향을 나타내는 객체입니다.
:::

:::topic-grid
## 점수 카운터
- [ScoreCounter](https://developer.apple.com/documentation/tabletopkit/scorecounter): 테이블탑 게임의 점수를 유지하는 객체입니다.
- [CounterCollection](https://developer.apple.com/documentation/tabletopkit/countercollection): 검사하고 수정할 수 있는 점수 카운터 모음입니다.
:::

:::topic-grid
## 플레이어
- [Player](https://developer.apple.com/documentation/tabletopkit/player): 테이블탑 게임의 플레이어입니다.
- [PlayerIdentifier](https://developer.apple.com/documentation/tabletopkit/playeridentifier): 플레이어를 위한 고유 식별자입니다.
:::

:::topic-grid
## 액션
- [TabletopAction](https://developer.apple.com/documentation/tabletopkit/tabletopaction): 테이블탑 게임의 action을 설명하는 객체용 프로토콜입니다.
- [MoveEquipmentAction](https://developer.apple.com/documentation/tabletopkit/moveequipmentaction): 테이블 위 장비를 이동하거나 그룹 구성을 바꾸는 action입니다.
- [UpdateEquipmentAction](https://developer.apple.com/documentation/tabletopkit/updateequipmentaction): 테이블 위 장비의 속성을 갱신하는 action입니다.
- [SetTurnAction](https://developer.apple.com/documentation/tabletopkit/setturnaction): 현재 턴에 참여하는 좌석을 설정하는 action입니다.
- [UpdateCounterAction](https://developer.apple.com/documentation/tabletopkit/updatecounteraction): 게임 카운터를 갱신하는 action입니다.
- [CreateBookmarkAction](https://developer.apple.com/documentation/tabletopkit/createbookmarkaction): 게임의 스냅샷을 생성하는 action입니다.
- [CustomAction](https://developer.apple.com/documentation/tabletopkit/customaction): TabletopKit 외부에서 동작을 구현하는 action을 나타내는 프로토콜입니다. `CustomAction`은 `.`에 적용할 수 있는 사용자 정의 action입니다.
:::

:::topic-grid
## 상호 작용
- [Simulating dice rolls as a component for your game](https://developer.apple.com/documentation/tabletopkit/simulating-dice-rolls-as-a-component-for-your-game): 상호 작용 가능한 굴림과 점수 계산을 추가해 물리적으로 사실적인 주사위 게임을 만듭니다.
- [TabletopInteraction](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction): 플레이어가 장비와 상호 작용하는 전체 흐름을 관리하는 객체용 프로토콜입니다.
- [TossableRepresentation](https://developer.apple.com/documentation/tabletopkit/tossablerepresentation): 주사위처럼 게임플레이 중 플레이어가 던질 수 있는 기하학적 형태를 나타내는 객체입니다.
- [TableSnapshot](https://developer.apple.com/documentation/tabletopkit/tablesnapshot): 현재 테이블 상태의 스냅샷입니다.
- [TableVisualState](https://developer.apple.com/documentation/tabletopkit/tablevisualstate): 테이블 위 객체의 외형을 나타내는 구조체입니다.
- [TableCursor](https://developer.apple.com/documentation/tabletopkit/tablecursor): 현재 상호 작용이 제어 중인 하나의 장비에 대한 정보를 전달하는 커서입니다.
- [TableCursorIdentifier](https://developer.apple.com/documentation/tabletopkit/tablecursoridentifier): 커서를 위한 고유 식별자입니다.
:::

:::topic-grid
## 북마크
- [StateBookmark](https://developer.apple.com/documentation/tabletopkit/statebookmark): 특정 시점의 게임 상태 스냅샷입니다.
- [StateBookmarkIdentifier](https://developer.apple.com/documentation/tabletopkit/statebookmarkidentifier): 북마크를 위한 고유 식별자입니다.
:::

:::topic-grid
## 멀티플레이어 네트워크 세션
- [TabletopNetworkSession](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession): 멀티플레이어 게임에서 네트워크 관련 작업을 조정하는 객체입니다.
- [TabletopNetworkSessionCoordinator](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksessioncoordinator): 피어 간 네트워크 세션을 관리하는 객체용 프로토콜입니다.
- [TabletopSendMessageResult](https://developer.apple.com/documentation/tabletopkit/tabletopsendmessageresult): 네트워크 세션에서 메시지를 보낼 때 가능한 결과입니다.
:::

:::topic-grid
## 디버깅
- [DebugDrawOptions](https://developer.apple.com/documentation/tabletopkit/debugdrawoptions): 렌더링에서 디버깅하려는 항목 유형입니다.
:::
