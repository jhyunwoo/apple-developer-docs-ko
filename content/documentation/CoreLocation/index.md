---
route: /documentation/CoreLocation
source_url: https://developer.apple.com/documentation/CoreLocation
source_locale: en-US
section: docc
content_type: symbol
title: Core Location
original_title: Core Location
source_hash: 57b12ee5f989d122faccf70e3318f15cc840b1f18426729fccf9cd9eb41d4424
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:28:20+00:00'
last_translated_at: '2026-03-13T23:28:34+09:00'
---

# Core Location

기기의 지리적 위치와 방향을 얻습니다.

## 개요

Core Location은 기기의 지리적 위치, 고도, 방향 또는 근처 iBeacon 기기에 대한 상대적 위치를 결정하는 서비스를 제공합니다. 이 프레임워크는 Wi‑Fi, GPS, Bluetooth, magnetometer, barometer, cellular 하드웨어를 포함한 기기의 모든 사용 가능한 구성 요소를 사용해 데이터를 수집합니다.

[CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) 클래스의 인스턴스를 사용해 Core Location 서비스를 구성하고 시작하고 중지합니다. location manager 객체는 다음과 같은 위치 관련 활동을 지원합니다.

:::term-list
Standard and significant location updates: 구성 가능한 정확도로 사용자의 현재 위치가 크게 또는 작게 바뀌는 것을 추적합니다.
Region monitoring: 관심 있는 특정 영역을 모니터링하고 사용자가 그 영역에 들어가거나 나갈 때 위치 이벤트를 생성합니다.
Beacon ranging: 근처 beacon을 감지하고 위치를 파악합니다.
Compass headings: 기기에 탑재된 나침반의 heading 변화를 보고합니다.
:::

위치 서비스를 사용하려면 [liveUpdates(_:)](https://developer.apple.com/documentation/corelocation/cllocationupdate/liveupdates(_:))를 호출해 update stream을 얻고, 그 stream을 비동기적으로 순회하면서 위치 update를 수신하고 처리하며, 위치 update가 도착하지 않는 이유를 이해하기 위한 진단 속성도 함께 받습니다.

필요하다면 시스템이 사용자에게 요청을 허용하거나 거부할지 묻습니다. 아래 예시는 초기 권한 요청입니다.

![iPhone 화면에 “Park Finder” 앱이 위치 접근 권한을 요청하는 프롬프트가 표시되어 있고, 옵션은 “OK”와 “Not now”입니다.](https://developer.apple.com)

iOS 기기에서 사용자는 Settings 앱에서 언제든지 위치 서비스 설정을 변경할 수 있으며, 이는 개별 앱이나 기기 전체에 영향을 줄 수 있습니다. 앱은 [CLLocationUpdate](https://developer.apple.com/documentation/corelocation/cllocationupdate)와 [CLMonitor](https://developer.apple.com/documentation/corelocation/clmonitor-6ynwz)의 비동기 시퀀스를 관찰해 권한 변경을 포함한 이벤트를 수신합니다.

:::topic-grid
## 핵심
- [Configuring your app to use location services](https://developer.apple.com/documentation/corelocation/configuring-your-app-to-use-location-services): 위치 데이터 수집을 시작할 수 있도록 앱을 준비합니다.
- [Supporting live updates in SwiftUI and Mac Catalyst apps](https://developer.apple.com/documentation/corelocation/supporting-live-updates-in-swiftui-and-mac-catalyst-apps): lifecycle event 지원을 추가해 백그라운드 이벤트를 활성화합니다.
- [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager): 앱에 위치 관련 이벤트 전달을 시작하고 중지할 때 사용하는 객체입니다.
- [CLBackgroundActivitySession](https://developer.apple.com/documentation/corelocation/clbackgroundactivitysession-3mzv3): 앱이 백그라운드에서 계속 사용 중으로 간주되도록 시각적 indicator를 관리해 update나 event를 받을 수 있게 하는 객체입니다.
- [CLLocationUpdate](https://developer.apple.com/documentation/corelocation/cllocationupdate): 프레임워크가 각 update와 함께 전달하는 위치 정보를 담는 구조체입니다.
- [Adopting live updates in Core Location](https://developer.apple.com/documentation/corelocation/adopting-live-updates-in-core-location): Swift의 비동기 이벤트를 사용해 위치 전달을 단순화합니다.
- [Monitoring location changes with Core Location](https://developer.apple.com/documentation/corelocation/monitoring-location-changes-with-core-location): 경계를 정의하고 사용자 위치 update에 반응합니다.
:::

:::topic-grid
## 권한 부여
- [Requesting authorization to use location services](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services): 위치 서비스 사용 권한을 얻고 앱의 권한 상태 변화를 관리합니다.
- [Suspending authorization requests](https://developer.apple.com/documentation/corelocation/suspending-authorization-requests): 앱이 준비될 때까지 시스템의 권한 요청 대화상자를 미룹니다.
- [CLAuthorizationStatus](https://developer.apple.com/documentation/corelocation/clauthorizationstatus): 앱의 위치 서비스 사용 권한을 나타내는 상수입니다.
- [CLAccuracyAuthorization](https://developer.apple.com/documentation/corelocation/claccuracyauthorization): 앱이 사용할 수 있도록 허가된 위치 정확도 수준을 나타내는 상수입니다.
- [NSLocationAlwaysAndWhenInUseUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysAndWhenInUseUsageDescription): 앱이 항상 위치 정보 접근을 요청하는 이유를 사용자에게 설명하는 메시지입니다.
- [NSLocationWhenInUseUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationWhenInUseUsageDescription): 앱이 포그라운드 실행 중 위치 정보 접근을 요청하는 이유를 설명하는 메시지입니다.
- [NSLocationUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationUsageDescription): 앱이 위치 정보 접근을 요청하는 이유를 설명하는 메시지입니다.
- [NSLocationDefaultAccuracyReduced](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationDefaultAccuracyReduced): 앱이 기본적으로 축소된 위치 정확도를 요청하는지 나타내는 Boolean 값입니다.
- [NSLocationAlwaysUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocationAlwaysUsageDescription): 앱이 항상 위치 접근을 요청하는 이유를 설명하는 메시지입니다.
:::

:::topic-grid
## 모니터링
- [CLMonitor](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v): 추가한 조건을 모니터링하는 객체입니다.
:::

:::topic-grid
## 위치 업데이트
- [Getting the current location of a device](https://developer.apple.com/documentation/corelocation/getting-the-current-location-of-a-device): 위치 서비스를 시작하고 전력 사용 최적화를 위해 시스템에 필요한 정보를 제공합니다.
- [Handling location updates in the background](https://developer.apple.com/documentation/corelocation/handling-location-updates-in-the-background): 앱이 포그라운드에 없을 때도 위치 update를 받을 수 있도록 구성합니다.
- [Creating a location push service extension](https://developer.apple.com/documentation/corelocation/creating-a-location-push-service-extension): 다른 사람의 요청에 응답해 위치 공유 앱이 사람의 위치에 접근할 수 있도록 extension을 추가하고 구성합니다.
- [CLLocation](https://developer.apple.com/documentation/corelocation/cllocation): 시스템이 보고하는 위도, 경도, 진행 방향 정보입니다.
- [CLLocationCoordinate2D](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2d): WGS 84 기준 좌표계로 지정한 위치의 위도와 경도입니다.
- [CLFloor](https://developer.apple.com/documentation/corelocation/clfloor): 사용자의 기기가 위치한 건물의 층입니다.
- [CLVisit](https://developer.apple.com/documentation/corelocation/clvisit): 특정 기간 동안 사용자의 위치에 대한 정보입니다.
- [CLLocationSourceInformation](https://developer.apple.com/documentation/corelocation/cllocationsourceinformation): 위치를 제공하는 source에 대한 정보입니다.
- [CLServiceSession](https://developer.apple.com/documentation/corelocation/clservicesession-pt7n): 앱의 위치 서비스 사용 권한에 대한 진단을 제공하는 객체입니다.
:::

:::topic-grid
## 영역 모니터링
- [Monitoring the user’s proximity to geographic regions](https://developer.apple.com/documentation/corelocation/monitoring-the-user-s-proximity-to-geographic-regions): 조건 모니터링을 사용해 사용자가 지리적 영역에 들어가거나 나가는 시점을 판단합니다.
- [CLRegion](https://developer.apple.com/documentation/corelocation/clregion): 모니터링할 수 있는 영역을 나타내는 기반 클래스입니다.
:::

:::topic-grid
## iBeacon
- [Ranging for Beacons](https://developer.apple.com/documentation/corelocation/ranging-for-beacons): 기기를 beacon처럼 동작하도록 구성하고 주변 beacon을 감지합니다.
- [Determining the proximity to an iBeacon device](https://developer.apple.com/documentation/corelocation/determining-the-proximity-to-an-ibeacon-device): beacon을 감지하고 기기와의 상대 거리를 판단합니다.
- [Turning an iOS device into an iBeacon device](https://developer.apple.com/documentation/corelocation/turning-an-ios-device-into-an-ibeacon-device): iOS 기기에서 iBeacon 신호를 브로드캐스트합니다.
- [CLBeacon](https://developer.apple.com/documentation/corelocation/clbeacon): 관찰한 iBeacon 기기와 사람의 기기 사이 상대 거리에 대한 정보입니다.
- [CLCondition](https://developer.apple.com/documentation/corelocation/clcondition-swift.protocol): 다른 모든 monitor condition의 추상 기반 클래스입니다.
:::

:::topic-grid
## 나침반 heading
- [Getting heading and course information](https://developer.apple.com/documentation/corelocation/getting-heading-and-course-information): 기기의 방향 및 진행 방향 정보를 탐색에 사용합니다.
- [CLHeading](https://developer.apple.com/documentation/corelocation/clheading): 진북 또는 자북을 기준으로 한 사용자의 기기 방향입니다.
:::

:::topic-grid
## 지오코딩
- [Converting between coordinates and user-friendly place names](https://developer.apple.com/documentation/corelocation/converting-between-coordinates-and-user-friendly-place-names): 위도·경도 쌍과 더 친숙한 장소 설명 사이를 변환합니다.
- [Converting a user’s location to a descriptive placemark](https://developer.apple.com/documentation/corelocation/converting-a-user-s-location-to-a-descriptive-placemark): 지도에 표시된 사용자의 위치를 역지오코딩해 설명적인 텍스트로 변환합니다.
- [CLGeocoder](https://developer.apple.com/documentation/corelocation/clgeocoder): 지리 좌표와 장소 이름 사이를 변환하는 인터페이스입니다.
- [CLPlacemark](https://developer.apple.com/documentation/corelocation/clplacemark): 종종 장소 이름, 주소, 기타 관련 정보를 포함하는 사용자 친화적인 지리 좌표 설명입니다.
:::

:::topic-grid
## 위치 push service extension
- [Location Push Service Extension](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.location.push): 위치 공유 앱이 push notification에 응답해 누군가의 위치를 조회할 수 있게 하는 entitlement입니다.
- [CLLocationPushServiceExtension](https://developer.apple.com/documentation/corelocation/cllocationpushserviceextension): Location Push Service Extension의 주요 진입점 역할을 하는 타입이 채택하는 인터페이스입니다.
- [CLLocationPushServiceError](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct): 위치 push notification 모니터링 시작이 실패할 때 location manager가 반환하는 오류 코드입니다.
- [CLLocationPushServiceErrorDomain](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerrordomain): Location Push Service Extension 오류의 도메인입니다.
- [CLLocationPushServiceError.Code](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code): 위치 push notification 모니터링 시작이 실패할 때 location manager가 반환하는 오류 코드입니다.
:::

:::topic-grid
## 오류
- [CLError](https://developer.apple.com/documentation/corelocation/clerror-swift.struct): Core Location 오류입니다.
- [kCLErrorDomain](https://developer.apple.com/documentation/corelocation/kclerrordomain): Core Location 오류의 도메인입니다.
- [kCLErrorUserInfoAlternateRegionKey](https://developer.apple.com/documentation/corelocation/kclerroruserinfoalternateregionkey): 지연된 영역 모니터링 응답과 관련된 오류의 사용자 정보 dictionary에 들어가는 키입니다.
:::

:::topic-grid
## 지원 중단
- [Deprecated](https://developer.apple.com/documentation/corelocation/deprecated)
:::

:::topic-grid
## 참고 자료
- [Core Location Constants](https://developer.apple.com/documentation/corelocation/core-location-constants): Core Location 프레임워크의 상수를 설명합니다.
- [Core Location Functions](https://developer.apple.com/documentation/corelocation/core-location-functions): 좌표 값을 다루는 데 도움이 되는 함수를 제공합니다.
:::
