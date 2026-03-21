---
route: /documentation/CarPlay
source_url: https://developer.apple.com/documentation/CarPlay
source_locale: en-US
section: docc
content_type: symbol
title: CarPlay
original_title: CarPlay
source_hash: 3afd4b7d044c477840362828ad4b09b518f7afd7d1b19899cc820ee98d70d12f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:11:14+00:00'
last_translated_at: '2026-03-13T22:16:00+09:00'
---

# CarPlay

오디오, 커뮤니케이션, 내비게이션, 주차, EV 충전, 음식 주문 등과 관련된 앱에 CarPlay를 통합합니다.

## 개요

CarPlay 프레임워크를 사용하면 앱을 위한 차량 내 경험을 만들 수 있습니다. 이 프레임워크는 차량 디스플레이에 표시하기 적합한 앱 인터페이스 버전을 구성할 수 있는 template를 제공합니다. 원하는 template를 앱에 추가하고 콘텐츠에 맞게 사용자화하십시오. template의 콘텐츠는 앱이 제어하지만, 터치 대상 크기, font 크기, font 색상, 하이라이트 같은 template 인터페이스 요소의 일부 측면은 프레임워크가 제어합니다.

CarPlay 기능은 현재 기기가 CarPlay를 지원하고, 그 기기가 적절히 장착된 차량에 연결되어 있을 때 실행됩니다. CarPlay는 차량 시스템 간 차이를 처리하므로, 개발자는 콘텐츠에 집중할 수 있습니다. 사용자가 차량에서 앱을 실행하면 시스템이 앱 인터페이스를 생성하고 호스팅합니다. 기기가 CarPlay를 지원하지 않으면 시스템은 앱의 CarPlay 기능에 접근하려 하지 않습니다.

앱의 CarPlay 인터페이스 일부는 다른 기술을 사용해 구동할 수도 있습니다. 메시징 앱은 [SiriKit](https://developer.apple.com/documentation/SiriKit) 지원을 포함해 메시지를 읽거나 전송할 수 있게 할 수 있습니다. VoIP 앱은 종종 SiriKit call 지원과 함께 [CallKit](https://developer.apple.com/documentation/CallKit)을 사용해 수신·발신 통화를 관리할 수 있습니다. 내비게이션 앱은 [MapKit](https://developer.apple.com/documentation/MapKit) 지원을 포함할 수 있습니다.

:::note WWDC20 관련 세션
세션 10635: [Accelerate Your App with CarPlay](https://developer.apple.com/videos/play/wwdc2020/10635/)
:::

:::topic-grid
## CarPlay 통합
- [Requesting CarPlay Entitlements](https://developer.apple.com/documentation/carplay/requesting-carplay-entitlements): 필요한 entitlement를 갖도록 CarPlay 지원 앱을 구성합니다.
- [Displaying Content in CarPlay](https://developer.apple.com/documentation/carplay/displaying-content-in-carplay): scene를 사용해 차량 내장 화면에 앱 콘텐츠를 표시합니다.
- [Supporting Previous Versions of iOS](https://developer.apple.com/documentation/carplay/supporting-previous-versions-of-ios): iOS 13 이하 같은 이전 시스템 버전과도 호환되도록 CarPlay 지원 앱을 만듭니다.
- [Using the CarPlay Simulator](https://developer.apple.com/documentation/carplay/using-the-carplay-simulator): Simulator가 CarPlay 지원 앱을 실행하고 디버깅하도록 구성합니다.
- [CPTemplateApplicationScene](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene): 앱의 사용자 인터페이스를 제어하는 CarPlay scene입니다.
- [CPTemplateApplicationSceneDelegate](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate): 앱 scene의 생명 주기 이벤트에 응답하는 메서드입니다.
- [CPSessionConfiguration](https://developer.apple.com/documentation/carplay/cpsessionconfiguration): CarPlay 환경을 위한 차량 속성과 구성을 제공하는 객체입니다.
:::

:::topic-grid
## 범용 template
- [CPListTemplate](https://developer.apple.com/documentation/carplay/cplisttemplate): 항목 목록을 표시하고 관리하는 template입니다.
- [CPGridTemplate](https://developer.apple.com/documentation/carplay/cpgridtemplate): 항목 그리드를 표시하고 관리하는 template입니다.
- [CPTabBarTemplate](https://developer.apple.com/documentation/carplay/cptabbartemplate): 다른 template를 tab으로 제시하며 표시하고 관리하는 컨테이너 template입니다.
- [CPTemplate](https://developer.apple.com/documentation/carplay/cptemplate): 인터페이스 template를 위한 추상 기본 클래스입니다.
- [CPBarButtonProviding](https://developer.apple.com/documentation/carplay/cpbarbuttonproviding): template가 navigation bar용 button을 제공할 때 사용하는 메서드입니다.
:::

:::topic-grid
## 오디오
- [Integrating CarPlay with Your Music App](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-music-app): 사용자 정의 UI를 표시해 음악 앱이 CarPlay와 함께 동작하도록 구성합니다.
- [CPNowPlayingTemplate](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate): 현재 재생 정보를 표시하는 공유 시스템 template입니다.
:::

:::topic-grid
## 계기판 클러스터
- [CPInstrumentClusterController](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontroller)
- [CPInstrumentClusterControllerDelegate](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontrollerdelegate)
- [CPTemplateApplicationInstrumentClusterScene](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscene)
- [CPTemplateApplicationInstrumentClusterSceneDelegate](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscenedelegate)
:::

:::topic-grid
## 내비게이션
- [Integrating CarPlay with Your Navigation App](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-navigation-app): 사용자 정의 지도와 길 안내를 표시해 내비게이션 앱이 CarPlay와 함께 동작하도록 구성합니다.
- [CPTemplateApplicationDashboardScene](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscene): 앱의 dashboard navigation window를 제어하는 CarPlay scene입니다.
- [CPTemplateApplicationDashboardSceneDelegate](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscenedelegate): 내비게이션 앱 dashboard scene의 생명 주기 이벤트에 응답하는 메서드입니다.
- [CPMapTemplate](https://developer.apple.com/documentation/carplay/cpmaptemplate): 앱이 지도 위에 그리는 navigation overlay를 표시하는 template입니다.
- [CPSearchTemplate](https://developer.apple.com/documentation/carplay/cpsearchtemplate): 목적지를 검색하고 검색 결과 목록을 볼 수 있는 기능을 제공하는 template입니다.
- [CPVoiceControlTemplate](https://developer.apple.com/documentation/carplay/cpvoicecontroltemplate): 오디오 입력 중 음성 제어 표시기를 보여 주는 template입니다.
:::

:::topic-grid
## 위치 및 정보
- [CPPointOfInterestTemplate](https://developer.apple.com/documentation/carplay/cppointofinteresttemplate): 선택 가능한 관심 지점이 있는 지도를 표시하는 template입니다.
- [CPInformationTemplate](https://developer.apple.com/documentation/carplay/cpinformationtemplate): 관심 지점, 음식 주문, 주차 위치, 충전 위치에 대한 정보를 제공하는 template입니다.
- [CPTextButton](https://developer.apple.com/documentation/carplay/cptextbutton): 스타일이 적용된 제목을 표시하는 button입니다.
- [Integrating CarPlay with your quick-ordering app](https://developer.apple.com/documentation/carplay/integrating-carplay-with-your-quick-ordering-app): 음식 주문 앱이 CarPlay와 함께 동작하도록 구성합니다.
:::

:::topic-grid
## 기동 지시
- [CPManeuver](https://developer.apple.com/documentation/carplay/cpmaneuver): 단일 내비게이션 지시를 설명하는 객체입니다.
- [CPManeuverState](https://developer.apple.com/documentation/carplay/cpmaneuverstate): maneuver의 상태를 설명하는 값입니다.
- [CPManeuverType](https://developer.apple.com/documentation/carplay/cpmaneuvertype): 내비게이션 maneuver 유형을 설명하는 값입니다.
:::

:::topic-grid
## 경로, 차선, 교차점
- [CPRouteInformation](https://developer.apple.com/documentation/carplay/cprouteinformation): 경로의 특성 요소를 설명하는 클래스입니다.
- [CPLane](https://developer.apple.com/documentation/carplay/cplane): 도로 위 차선의 특성을 설명하는 클래스입니다.
- [CPLaneGuidance](https://developer.apple.com/documentation/carplay/cplaneguidance): 도로의 차선 수와 내비게이션 지시 변형을 설명하는 정보를 제공하는 클래스입니다.
- [CPLaneStatus](https://developer.apple.com/documentation/carplay/cplanestatus): 차선의 상태 또는 선호도를 설명하는 값입니다.
- [CPJunctionType](https://developer.apple.com/documentation/carplay/cpjunctiontype): 도로 교차점 유형을 나타내는 값입니다.
:::

:::topic-grid
## 커뮤니케이션
- [CPContactTemplate](https://developer.apple.com/documentation/carplay/cpcontacttemplate): 사람이나 비즈니스에 대한 정보를 표시하는 template입니다.
:::

:::topic-grid
## 동작 및 경고
- [CPActionSheetTemplate](https://developer.apple.com/documentation/carplay/cpactionsheettemplate): 모달 action sheet를 표시하는 template입니다.
- [CPAlertTemplate](https://developer.apple.com/documentation/carplay/cpalerttemplate): 모달 alert를 표시하는 template입니다.
- [CPAlertAction](https://developer.apple.com/documentation/carplay/cpalertaction): 사용자가 action sheet나 alert에서 수행할 수 있는 동작을 캡슐화하는 객체입니다.
:::

:::topic-grid
## 관련 타입
- [CPButton](https://developer.apple.com/documentation/carplay/cpbutton): 이미지를 표시하고 사용자가 탭했을 때 handler를 호출하는 button입니다.
- [CPImageSet](https://developer.apple.com/documentation/carplay/cpimageset): 이미지의 라이트 및 다크 표현입니다.
- [CarPlayErrorDomain](https://developer.apple.com/documentation/carplay/carplayerrordomain): CarPlay가 제공하는 오류에 사용하는 도메인입니다.
:::

:::topic-grid
## 더 이상 사용되지 않음
- [Deprecated Symbols](https://developer.apple.com/documentation/carplay/deprecated-symbols): CarPlay 프레임워크가 더 이상 지원하지 않는 symbol입니다.
:::

:::topic-grid
## 참고 자료
- [CarPlay Enumerations](https://developer.apple.com/documentation/carplay/carplay-enumerations)
- [CarPlay Constants](https://developer.apple.com/documentation/carplay/carplay-constants)
:::

:::topic-grid
## 클래스
- [CPImageOverlay](https://developer.apple.com/documentation/carplay/cpimageoverlay): 이미지 위에 정보를 표시하는 overlay입니다.
- [CPListImageRowItemCardElement](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement)
- [CPListImageRowItemCondensedElement](https://developer.apple.com/documentation/carplay/cplistimagerowitemcondensedelement)
- [CPListImageRowItemElement](https://developer.apple.com/documentation/carplay/cplistimagerowitemelement): row item element 객체를 위한 추상 superclass입니다.
- [CPListImageRowItemGridElement](https://developer.apple.com/documentation/carplay/cplistimagerowitemgridelement)
- [CPListImageRowItemImageGridElement](https://developer.apple.com/documentation/carplay/cplistimagerowitemimagegridelement)
- [CPListImageRowItemRowElement](https://developer.apple.com/documentation/carplay/cplistimagerowitemrowelement)
- [CPListTemplateDetailsHeader](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader): action button이 포함된 풍부한 미디어 콘텐츠를 표시하는 list template용 header입니다.
- [CPMapTemplateWaypoint](https://developer.apple.com/documentation/carplay/cpmaptemplatewaypoint): 관련 이동 예상 시간과 함께 waypoint를 표현합니다.
- [CPMessageGridItemConfiguration](https://developer.apple.com/documentation/carplay/cpmessagegriditemconfiguration)
- [CPNavigationWaypoint](https://developer.apple.com/documentation/carplay/cpnavigationwaypoint): 위치 기반 정보와 안내를 제공하는 경로 상의 관심 지점을 표현합니다.
- [CPNowPlayingMode](https://developer.apple.com/documentation/carplay/cpnowplayingmode)
- [CPNowPlayingModeSports](https://developer.apple.com/documentation/carplay/cpnowplayingmodesports): sports mode는 정확히 두 팀이 등장하는 스포츠 이벤트의 라이브 스트리밍 또는 녹화 재생에 적합한 now playing 레이아웃을 나타냅니다.
- [CPNowPlayingSportsClock](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock): 시계가 증가하는 이벤트에서, 현재까지 경과한 시간을 표현합니다.
- [CPNowPlayingSportsEventStatus](https://developer.apple.com/documentation/carplay/cpnowplayingsportseventstatus): 스포츠 이벤트 상태를 표현합니다.
- [CPNowPlayingSportsTeam](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteam): 정확히 두 팀이 있는 스포츠를 위한 now playing 화면의 스포츠 팀 표현입니다.
- [CPNowPlayingSportsTeamLogo](https://developer.apple.com/documentation/carplay/cpnowplayingsportsteamlogo): 사용할 이미지가 없는 경우 팀의 약어 또는 머리글자를 대신 표시하는 로고 이미지입니다.
- [CPPlaybackConfiguration](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration)
- [CPRouteSegment](https://developer.apple.com/documentation/carplay/cproutesegment): 경로의 한 구간에 관한 정보를 설명합니다.
- [CPSportsOverlay](https://developer.apple.com/documentation/carplay/cpsportsoverlay): 왼쪽과 오른쪽 팀 정보를 표시하는 sports overlay입니다.
- [CPThumbnailImage](https://developer.apple.com/documentation/carplay/cpthumbnailimage)
:::

:::topic-grid
## 프로토콜
- [CPPlayableItem](https://developer.apple.com/documentation/carplay/cpplayableitem)
:::

:::topic-grid
## 구조체
- [CPLocationCoordinate3D](https://developer.apple.com/documentation/carplay/cplocationcoordinate3d): 위도, 경도, 고도 구성 요소를 갖는 3차원 좌표를 표현합니다.
:::

:::topic-grid
## 변수
- [CPMaximumMessageItemLeadingDetailTextImageSize](https://developer.apple.com/documentation/carplay/cpmaximummessageitemleadingdetailtextimagesize): 상세 텍스트 leading image에 대한 최대 이미지 크기입니다.
:::

:::topic-grid
## 함수
- [NSStringFromCPJunctionType(_:)](https://developer.apple.com/documentation/carplay/nsstringfromcpjunctiontype(_:))
- [NSStringFromCPLaneStatus(_:)](https://developer.apple.com/documentation/carplay/nsstringfromcplanestatus(_:))
- [NSStringFromCPManeuverType(_:)](https://developer.apple.com/documentation/carplay/nsstringfromcpmaneuvertype(_:))
- [NSStringFromCPRerouteReason(_:)](https://developer.apple.com/documentation/carplay/nsstringfromcpreroutereason(_:))
- [NSStringFromCPTrafficSide(_:)](https://developer.apple.com/documentation/carplay/nsstringfromcptrafficside(_:))
:::

:::topic-grid
## 열거형
- [CPRerouteReason](https://developer.apple.com/documentation/carplay/cpreroutereason): 내비게이션 재탐색 이유를 나타내는 값입니다.
- [CPRouteSource](https://developer.apple.com/documentation/carplay/cproutesource)
:::
