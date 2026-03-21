---
route: /documentation/GroupActivities
source_url: https://developer.apple.com/documentation/GroupActivities
source_locale: en-US
section: docc
content_type: symbol
title: Group Activities
original_title: Group Activities
source_hash: c20087a9e3312cd7c8a7da7e52cb4bb6dd00f4c880e1b3ee6f7ccad23e557b72
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:08:27+00:00'
last_translated_at: '2026-03-13T22:06:00+09:00'
---

# Group Activities

사용자가 함께 공유하고 경험할 수 있는 앱 전용 활동을 만듭니다.

## 개요

Group Activities 프레임워크를 사용하면 앱의 콘텐츠를 SharePlay 경험에 제공할 수 있어 사용자에게 연결감과 즉시성을 전달할 수 있습니다. 예를 들어 동영상 스트리밍 앱은 참가자들이 각자의 기기에서 동시에 감상하는 영화 보기 파티 기능을 제공할 수 있습니다. 앱이 각 기기에서 재생을 처리하지만, Group Activities 프레임워크가 그 재생을 동기화하고 기기 간 통신을 돕습니다.

이 프레임워크는 FaceTime 인프라를 활용해 앱의 활동을 동기화하고 다른 참가자들이 그 활동에 참여하도록 초대합니다. 앱 UI에 공유 가능한 활동이 포함되어 있다면, 그 활동을 표현하는 객체에 [GroupActivity](https://developer.apple.com/documentation/groupactivities/groupactivity) 프로토콜을 채택하십시오. 그룹 활동이 시작되면 [GroupSession](https://developer.apple.com/documentation/groupactivities/groupsession) 객체를 사용해 앱의 동작을 다른 참가 기기와 동기화합니다.

:::note 참고
Group Activities 프레임워크는 [GroupSession](https://developer.apple.com/documentation/groupactivities/groupsession) 객체가 기기 사이에서 동기화하는 모든 세션 데이터에 종단 간 암호화를 사용합니다. Apple은 이 데이터를 복호화할 키를 갖고 있지 않습니다. Group Activities 프레임워크를 사용해도 Apple은 앱이 공유하는 콘텐츠나, 사용자가 어떤 지점에서 미디어 재생을 시작, 일시 정지, 건너뛰는지 같은 앱의 미디어 재생 관련 정보를 볼 수 없습니다. Group Activities 세션을 중개하는 Apple 서버는 앱의 정체를 알지 못합니다. 드물게 Apple이 sysdiagnose 캡처나 디버깅 프로파일 설치 같은 방식으로 문제 해결을 요청할 수 있으며, 그 과정에서 앱이 공유한 콘텐츠와 관련된 일부 정보가 부수적으로 수집될 수 있습니다.
:::

:::topic-grid
## 핵심 사항
- [com.apple.developer.group-session](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.group-session): 앱이 공유 그룹 경험을 구현할 수 있는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 활동 정의
- [Defining your app’s SharePlay activities](https://developer.apple.com/documentation/groupactivities/defining-your-apps-shareplay-activities): 앱의 SharePlay 지원을 구성하고 사람들이 앱에서 수행할 수 있는 활동을 정의합니다.
- [Supporting coordinated media playback](https://developer.apple.com/documentation/AVFoundation/supporting-coordinated-media-playback): 사용자가 기기 간에 함께 보고 들을 수 있도록 동기화된 미디어 경험을 만듭니다.
- [GroupActivity](https://developer.apple.com/documentation/groupactivities/groupactivity): 앱의 활동을 다른 참가자에게 알릴 수 있는 타입입니다.
- [GroupActivityMetadata](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata): 잠재적 참가자에게 활동을 설명하는 텍스트와 이미지 콘텐츠입니다.
- [GroupActivityActivationResult](https://developer.apple.com/documentation/groupactivities/groupactivityactivationresult): 사용자 정의 활동 시작을 준비한 결과입니다.
- [GroupActivityTransferRepresentation](https://developer.apple.com/documentation/groupactivities/groupactivitytransferrepresentation): 이미 알고 있는 문맥에서 그룹 활동을 시작할 수 있게 해 주는 타입입니다.
:::

:::topic-grid
## 인터페이스 표시
- [Presenting SharePlay activities from your app’s UI](https://developer.apple.com/documentation/groupactivities/promoting-shareplay-activities-from-your-apps-ui): 앱 UI, 시스템 share sheet, AirDrop을 통한 AirPlay에서 사람들이 활동을 쉽게 시작할 수 있도록 합니다.
- [GroupActivitySharingController](https://developer.apple.com/documentation/groupactivities/groupactivitysharingcontroller-4gtfk): 활동을 시작하기 위한 시스템 인터페이스를 표시하고, 선택적으로 해당 활동에 대한 FaceTime 통화를 시작하는 macOS view controller입니다.
- [GroupActivitySharingController](https://developer.apple.com/documentation/groupactivities/groupactivitysharingcontroller-ybcy): 활동을 시작하기 위한 시스템 인터페이스를 표시하고, 선택적으로 해당 활동에 대한 FaceTime 통화를 시작하는 iOS view controller입니다.
:::

:::topic-grid
## 세션 관리
- [Joining and managing a shared activity](https://developer.apple.com/documentation/groupactivities/joining-and-managing-a-shared-activity): SharePlay 활동이 시작될 때 세션을 구성하고, 활동 수명 주기 동안 발생하는 이벤트를 처리합니다.
- [Drawing content in a group session](https://developer.apple.com/documentation/groupactivities/drawing_content_in_a_group_session): FaceTime 통화 중 친구들과 공유 캔버스에 그림을 그리도록 초대합니다.
- [GroupSession](https://developer.apple.com/documentation/groupactivities/groupsession): 참가 기기 간 콘텐츠를 동기화하는 진행 중 활동용 세션입니다.
- [CustomMessageIdentifiable](https://developer.apple.com/documentation/groupactivities/custommessageidentifiable): 다른 기기로 보내는 메시지에 사용자 정의 ID 문자열을 할당하는 타입입니다.
- [Participant](https://developer.apple.com/documentation/groupactivities/participant): 그룹 세션의 활성 참가자입니다.
:::

:::topic-grid
## 공간 활동
- [Configure your visionOS app for sharing with people nearby](https://developer.apple.com/documentation/groupactivities/configure-your-app-for-sharing-with-people-nearby): 같은 공간에 있는 Vision Pro 사용자 및 FaceTime 참여자를 위한 공유 경험을 만듭니다.
- [Adding spatial Persona support to an activity](https://developer.apple.com/documentation/groupactivities/adding-spatial-persona-support-to-an-activity): visionOS에서 실행될 때 spatial Persona와 공유 문맥을 지원하도록 SharePlay 활동을 업데이트합니다.
- [SystemCoordinator](https://developer.apple.com/documentation/groupactivities/systemcoordinator): 활성 SharePlay 세션이 콘텐츠의 공간 배치를 지원할 때 인터페이스 동작을 조정하는 데 사용하는 타입입니다.
- [SystemCoordinator.ParticipantState](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstate): 현재 활동에 대해 참가자가 공유 시뮬레이션 공간을 지원하는지를 알려 주는 구조체입니다.
- [groupActivityAssociation(_:)](https://developer.apple.com/documentation/SwiftUI/View/groupActivityAssociation(_:)): view가 현재 SharePlay 그룹 활동과 어떻게 연관되어야 하는지를 지정합니다.
- [GroupActivityAssociationInteraction](https://developer.apple.com/documentation/groupactivities/groupactivityassociationinteraction): 현재 SharePlay 그룹 활동과 view의 연관 방식을 구성하는 interaction입니다.
- [GroupActivityAssociationKind](https://developer.apple.com/documentation/groupactivities/groupactivityassociationkind): 사용자 인터페이스 요소가 SharePlay 그룹 활동과 가질 수 있는 연관 유형입니다.
:::

:::topic-grid
## 사용자 정의 공간 템플릿
- [Building a guessing game for visionOS](https://developer.apple.com/documentation/groupactivities/building-a-guessing-game-for-visionos): Group Activities를 사용해 visionOS용 팀 기반 추측 게임을 만듭니다.
- [SpatialTemplate](https://developer.apple.com/documentation/groupactivities/spatialtemplate): 장면 안에서 spatial Persona의 사용자 정의 배치를 만드는 데 사용하는 인터페이스입니다.
- [SpatialTemplatePreference](https://developer.apple.com/documentation/groupactivities/spatialtemplatepreference): 공유 시뮬레이션 공간에서 참가자 spatial Persona의 선호 배치를 지정하는 구조체입니다.
- [SpatialTemplateSeatElement](https://developer.apple.com/documentation/groupactivities/spatialtemplateseatelement): 활동 참가자를 위한 좌석을 나타내는 공간 템플릿 요소입니다.
- [SpatialTemplateElement](https://developer.apple.com/documentation/groupactivities/spatialtemplateelement): 공간 템플릿의 요소를 정의하는 인터페이스입니다.
- [SpatialTemplateElementPosition](https://developer.apple.com/documentation/groupactivities/spatialtemplateelementposition): 공간 템플릿 요소의 위치를 정의하는 타입입니다.
- [SpatialTemplateElementDirection](https://developer.apple.com/documentation/groupactivities/spatialtemplateelementdirection): 활동이 시작될 때 참가자가 바라보는 초기 방향입니다.
- [SpatialTemplateRole](https://developer.apple.com/documentation/groupactivities/spatialtemplaterole): 그룹 활동 참가자에게 할당하는 역할을 정의하기 위한 인터페이스입니다.
:::

:::topic-grid
## 파일 및 데이터 전송
- [Creating a collaborative photo gallery with SharePlay](https://developer.apple.com/documentation/groupactivities/creating-a-collaborative-photo-gallery-with-shareplay): SharePlay를 사용해 참가자 간 이미지를 동기화하여 공유 사진 갤러리를 구축합니다.
- [Synchronizing data during a SharePlay activity](https://developer.apple.com/documentation/groupactivities/synchronizing-data-during-a-shareplay-activity): 사용자 정의 메시지와 데이터를 기기 간에 보내 활동의 콘텐츠를 동기화하고, 다른 참가자로부터 받은 메시지를 앱에 반영합니다.
- [GroupSessionMessenger](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger): 그룹 세션에 참여한 기기 간에 앱 전용 데이터를 전송하는 객체입니다.
- [GroupSessionJournal](https://developer.apple.com/documentation/groupactivities/groupsessionjournal): 그룹 세션에 참여한 참가자 간 파일 및 데이터 전송을 관리하는 객체입니다.
:::

:::topic-grid
## 시스템 상태
- [GroupStateObserver](https://developer.apple.com/documentation/groupactivities/groupstateobserver): 시스템이 SharePlay 경험을 시작할 수 있는 능력에 대한 정보를 담는 객체입니다.
:::
