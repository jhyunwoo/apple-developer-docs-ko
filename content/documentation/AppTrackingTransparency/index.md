---
route: /documentation/AppTrackingTransparency
source_url: https://developer.apple.com/documentation/AppTrackingTransparency
source_locale: en-US
section: docc
content_type: symbol
title: App Tracking Transparency
original_title: App Tracking Transparency
source_hash: ccb6a40af4f448492a3d98ff17d950cd8421fc271066ffc0f93602e24981e030
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:04:19+00:00'
last_translated_at: '2026-03-13T21:56:00+09:00'
---

# App Tracking Transparency

사용자나 기기를 추적하기 위해 앱 관련 데이터에 접근하려면 사용자 권한을 요청합니다.

## 개요

앱이 최종 사용자에 대한 데이터를 수집하고, 여러 앱과 웹 사이트를 가로질러 사용자를 추적하는 목적으로 그 데이터를 다른 회사와 공유한다면 AppTrackingTransparency 프레임워크를 반드시 사용해야 합니다. AppTrackingTransparency 프레임워크는 사용자에게 앱 추적 권한 요청을 표시하고 추적 권한 상태를 제공합니다.

AppTrackingTransparency 프레임워크를 사용하려면 다음을 수행하십시오.

1. 최종 사용자 기기에 설치된 앱에 대해 시스템 권한 요청 경고를 표시할 수 있도록 [NSUserTrackingUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserTrackingUsageDescription)을 설정합니다.
2. [requestTrackingAuthorization(completionHandler:)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:))를 호출해 최종 사용자에게 앱 추적 권한 요청을 표시합니다.
3. [trackingAuthorizationStatus](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/trackingauthorizationstatus)를 사용해 앱 추적 권한 상태를 확인합니다. 상태 열거형은 [ATTrackingManager.AuthorizationStatus](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus)를 참고하십시오.

앱 추적과 개인 정보 보호에 대한 자세한 내용은 [User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)와 [App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [NSUserTrackingUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserTrackingUsageDescription): 앱이 사용자나 기기를 추적하기 위해 데이터를 사용하려는 이유를 사용자에게 알려 주는 메시지입니다.
:::

:::topic-grid
## 클래스 및 구성 요소
- [ATTrackingManager](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager): 추적 권한 요청과 앱의 추적 권한 상태를 제공하는 클래스입니다.
:::
