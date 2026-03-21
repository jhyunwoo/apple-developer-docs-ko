---
route: /documentation/ExposureNotification
source_url: https://developer.apple.com/documentation/ExposureNotification
source_locale: en-US
section: docc
content_type: symbol
title: Exposure Notification
original_title: Exposure Notification
source_hash: edeb1961db145d9a6731d1b7ab4dbdad2a805521e8fc44d9ca981a85221a5bad
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:52:39+00:00'
last_translated_at: '2026-03-13T21:30:00+09:00'
---

# Exposure Notification

사용자 개인 정보를 보호하는 COVID-19 노출 알림 시스템을 구현합니다.

## 개요

Exposure Notification 프레임워크를 사용하면 SARS-CoV-2 바이러스로 인해 발생하는 질병인 COVID-19에 잠재적으로 노출되었을 수 있음을 사람들에게 알릴 수 있습니다. 무작위로 생성되고 주기적으로 교체되는 키와 식별자를 사용해 양성 진단 정보를 전달하고, 관련 증상, 근접도, 지속 시간 같은 데이터도 함께 전달하는 알림 시스템을 구축할 수 있습니다.

### 사용자 역할 설정

ExposureNotification 프레임워크는 두 가지 사용자 역할을 정의합니다.

:::term-list
영향을 받은 사용자: 사용자가 COVID-19 확진 또는 의심 진단을 받은 경우(보건 당국 정의 기준), 프레임워크는 해당 사용자를 *affected*로 식별하고 다른 사용자에게 잠재적 노출을 경고하기 위해 그 사용자의 diagnosis key를 공유합니다.
잠재적으로 노출된 사용자: 사용자에게 *potentially exposed* 역할을 부여하려면, 프레임워크를 사용해 임시 노출 키 집합이 영향을 받은 사용자와의 근접성을 나타내는지 판별합니다. 그렇다면 앱은 프레임워크에서 날짜와 지속 시간 같은 추가 정보를 가져올 수 있습니다.
:::

:::important 중요
ExposureNotification을 사용하는 앱을 개발하려면 먼저 [com.apple.developer.exposure-notification](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.exposure-notification) entitlement가 필요합니다. 이 entitlement에 대한 자세한 내용은 [Exposure Notification APIs Addendum](https://developer.apple.com/contact/request/download/Exposure_Notification_Addendum.pdf)를 참고하십시오. 이 entitlement 사용 권한을 얻으려면 [Exposure Notification Entitlement Request](https://developer.apple.com/contact/request/exposure-notification-entitlement)를 참고하십시오.
:::

### 앱의 지역 식별

모든 EN 앱은 앱의 `Info.plist` 파일에 [ENDeveloperRegion](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ENDeveloperRegion)이라는 키를 추가하여 해당 앱이 동작하는 지역을 지정해야 합니다. `ENDeveloperRegion` 값은 앱의 지역을 나타내는 문자열입니다. 이 값은 ISO 3166-1 국가 코드(예: 캐나다는 “CA”)일 수도 있고, ISO 3166-1/3166-2 국가 코드와 하위 구역 코드(예: 캘리포니아는 “US-CA”)의 조합일 수도 있습니다.

연결된 도메인 링크를 해당 지역 코드로 명시적으로 설정하십시오. wildcard를 사용하면 시스템 동작에 영향을 줄 수 있으므로 피해야 합니다. 자세한 내용은 [Associated Domains Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.associated-domains)를 참고하십시오.

### Exposure Notification API 버전 지정

iOS 13.7은 [ENExposureConfiguration](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration)에 설명된, 사용자의 Exposure Risk Value를 계산하는 새로운 방법을 도입했습니다. 앱은 이 새 방법을 구현할 수도 있고, 이전 iOS 버전에 도입된 계산 방법을 계속 사용할 수도 있습니다. 앱이 어떤 방식을 사용할지 선택하려면 앱의 `Info.plist` 파일에 [ENAPIVersion](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ENAPIVersion) 키를 가진 항목을 추가하십시오. 새 방식을 사용하려면 값으로 `2`를 지정하고, 기존 방식을 사용하려면 값으로 `1`을 지정하십시오.

### Exposure Notification Express 지원

iOS 13.7부터 보건 당국은 전용 Exposure Notification 앱 없이도 사용자에게 COVID-19 잠재 노출을 알릴 수 있습니다. 이 기능은 Exposure Notification Express라고 하며 보건 당국이 활성화해야 합니다. 자세한 내용은 [Supporting Exposure Notifications Express](https://developer.apple.com/documentation/exposurenotification/supporting-exposure-notifications-express)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [Supporting Exposure Notifications Express](https://developer.apple.com/documentation/exposurenotification/supporting-exposure-notifications-express): 앱 없이도 사용자에게 COVID-19 잠재 노출을 알리도록 서버를 구성합니다.
- [Building an App to Notify Users of COVID-19 Exposure](https://developer.apple.com/documentation/exposurenotification/building-an-app-to-notify-users-of-covid-19-exposure): 사람들이 COVID-19에 노출되었을 가능성이 있을 때 이를 알립니다.
- [Setting Up a Key Server](https://developer.apple.com/documentation/exposurenotification/setting-up-a-key-server): 서버가 Exposure Notifications 지원 요구 사항을 충족하는지 확인합니다.
- [ENManager](https://developer.apple.com/documentation/exposurenotification/enmanager): 노출 알림을 관리하는 클래스입니다.
- [ENDeveloperRegion](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ENDeveloperRegion): 앱이 지원하는 지역을 지정하는 문자열입니다.
- [ENAPIVersion](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ENAPIVersion): 사용할 API 버전을 지정하는 숫자입니다.
- [Changing Configuration Values Using the Server‑to‑Server API](https://developer.apple.com/documentation/exposurenotification/changing-configuration-values-using-the-server-to-server-api): 공중보건 당국의 서버에서 Exposure Notifications 구성 값을 업데이트합니다.
- [Testing Exposure Notifications Apps in iOS 13.7 and Later](https://developer.apple.com/documentation/exposurenotification/testing-exposure-notifications-apps-in-ios-13-7-and-later): 구성 파일을 수동으로 불러와 기기에서 Exposure Notifications 앱의 end-to-end 검증을 수행합니다.
- [Supporting Exposure Notifications in iOS 12.5](https://developer.apple.com/documentation/exposurenotification/supporting-exposure-notifications-in-ios-12-5): 이전 iOS 버전에서도 Exposure Notifications 앱이 실행되도록 준비합니다.
:::

:::topic-grid
## 노출
- [Configuring Exposure Notifications](https://developer.apple.com/documentation/exposurenotification/configuring-exposure-notifications): 서버 기반 key-value 쌍을 할당해 특정 지역에서 Exposure Notifications가 동작하는 방식을 정의합니다.
- [ENExposureConfiguration](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration): 노출 알림 위험 점수 동작을 구성하는 매개변수를 담는 객체입니다.
- [ENExposureWindow](https://developer.apple.com/documentation/exposurenotification/enexposurewindow): 일정 시간 범위 안에서 관찰된 beacon의 scan event 집합입니다.
- [ENScanInstance](https://developer.apple.com/documentation/exposurenotification/enscaninstance): 스캔 중 수신된 beacon 감쇠값의 집계입니다.
- [Exposure Parameter Limits](https://developer.apple.com/documentation/exposurenotification/exposure-parameter-limits): 노출 위험 계산에 사용하는 매개변수의 한계값입니다.
:::

:::topic-grid
## 요약
- [ENExposureDetectionSummary](https://developer.apple.com/documentation/exposurenotification/enexposuredetectionsummary): 노출 요약입니다.
- [ENExposureDaySummary](https://developer.apple.com/documentation/exposurenotification/enexposuredaysummary): 하루 동안의 노출 정보 요약입니다.
- [ENExposureSummaryItem](https://developer.apple.com/documentation/exposurenotification/enexposuresummaryitem): 특정 기간 또는 보고 유형에 대한 노출 요약입니다.
:::

:::topic-grid
## 상태
- [ENAuthorizationStatus](https://developer.apple.com/documentation/exposurenotification/enauthorizationstatus): 앱의 권한 상태를 나타내는 케이스 집합입니다.
- [ENStatus](https://developer.apple.com/documentation/exposurenotification/enstatus): 시스템에서 노출 알림의 전체 상태를 나타내는 케이스 집합입니다.
:::

:::topic-grid
## 오류
- [ENError](https://developer.apple.com/documentation/exposurenotification/enerror): 노출 알림 프레임워크가 발생시키는 오류입니다.
- [ENError.Code](https://developer.apple.com/documentation/exposurenotification/enerror/code): 노출 알림 프레임워크가 발생시키는 오류 코드입니다.
- [ENErrorDomain](https://developer.apple.com/documentation/exposurenotification/enerrordomain): 오류의 도메인입니다.
- [ENErrorHandler](https://developer.apple.com/documentation/exposurenotification/enerrorhandler): 오류 상태를 처리하는 핸들러입니다.
:::

:::topic-grid
## 변수
- [ENRiskWeightDefaultV2](https://developer.apple.com/documentation/exposurenotification/enriskweightdefaultv2): 이 가중치는 사용되지 않습니다.
- [ENRiskWeightMaxV2](https://developer.apple.com/documentation/exposurenotification/enriskweightmaxv2): 이 가중치는 사용되지 않습니다.
- [EN_FEATURE_GENERAL](https://developer.apple.com/documentation/exposurenotification/en_feature_general)
:::

:::topic-grid
## 타입 별칭
- [ENDetectExposuresHandler](https://developer.apple.com/documentation/exposurenotification/endetectexposureshandler): 노출 요약을 반환하는 핸들러 정의입니다.
- [ENErrorOutType](https://developer.apple.com/documentation/exposurenotification/enerrorouttype): 함수에서 NSError를 반환하기 위한 타입입니다. 길고 반복적인 메서드 시그니처를 피하게 해 줍니다.
- [ENGetDiagnosisKeysHandler](https://developer.apple.com/documentation/exposurenotification/engetdiagnosiskeyshandler): diagnosis key를 반환하는 핸들러 정의입니다.
- [ENGetExposureInfoHandler](https://developer.apple.com/documentation/exposurenotification/engetexposureinfohandler): 노출 정보를 전달받는 핸들러 정의입니다.
:::

:::asset-list
- `https://developer.apple.com/contact/request/download/Exposure_Notification_Addendum.pdf` -> `https://developer.apple.com/contact/request/download/Exposure_Notification_Addendum.pdf` (pending)
:::
