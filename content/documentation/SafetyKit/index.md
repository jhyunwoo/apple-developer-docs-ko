---
route: /documentation/SafetyKit
source_url: https://developer.apple.com/documentation/SafetyKit
source_locale: en-US
section: docc
content_type: symbol
title: SafetyKit
original_title: SafetyKit
source_hash: 4317a2fece7ed0d0dd122ce5caddd3e6eec9578002f60e43e1ea31859ca44c7a
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:04:19+00:00'
last_translated_at: '2026-03-13T21:56:00+09:00'
---

# SafetyKit

앱에서 자동차 충돌 이벤트를 감지하고 대응합니다.

## 개요

SafetyKit은 Crash Detection 기능을 제공합니다. 이 기능은 iPhone 14, iPhone 14 Pro, Apple Watch Series 8, Apple Watch SE(2세대), Apple Watch Ultra가 심각한 차량 충돌을 감지했을 때 권한이 부여된 앱으로 충돌 이벤트를 보냅니다. 이 기기들은 Emergency SOS - Call After Severe Crash라는 기능을 제공합니다. 이 기능이 활성화되어 있으면 차량 충돌이 발생했을 때 Emergency SOS가 911 같은 지역 긴급 서비스로 전화를 겁니다. Emergency SOS가 전화를 건 후에는 Crash Detection이 앱이 지정한 연락처(예: 긴급 출동 서비스 제공자)에게 전화를 걸도록 도와 사용자를 지원할 수 있습니다.

SafetyKit은 세 가지 충돌 시나리오를 지원합니다. 각 시나리오에서 Apple은 first party이고, 앱은 third party입니다.

첫 번째 시나리오는 first-party Emergency SOS가 꺼져 있고 third-party 공유가 켜져 있는 경우입니다. 기기가 충돌을 감지하면 중요한 경고가 발생하고 third party가 충돌 정보를 받습니다.

![“first-party Emergency SOS turned off with third-party sharing”이라는 제목의 타임라인으로, 기기가 충돌을 감지하면 중요한 경고가 발생하고 third party가 충돌 정보를 수신하는 순서를 보여줍니다.](https://developer.apple.com)

두 번째 시나리오는 first-party Emergency SOS와 third-party 공유가 모두 켜져 있는 경우입니다. 기기가 충돌을 감지하면 first-party Emergency SOS가 자동으로 실행됩니다. first party가 절차를 마친 후 중요한 경고가 발생하고 third party가 충돌 정보를 받습니다.

![“first-party Emergency SOS turned on with third-party sharing”이라는 제목의 타임라인으로, 기기가 충돌을 감지하면 first-party SOS가 자동으로 실행되고 이후 중요한 경고가 발생하며 third party가 충돌 정보를 수신하는 순서를 보여줍니다.](https://developer.apple.com)

세 번째 시나리오는 first-party Emergency SOS가 켜져 있고 third-party 공유가 없는 경우입니다. 기기가 충돌을 감지하면 first-party Emergency SOS가 자동으로 실행됩니다.

![“first-party Emergency SOS only”라는 제목의 타임라인으로, 기기가 충돌을 감지한 뒤 first-party SOS가 자동으로 실행되는 순서를 보여줍니다.](https://developer.apple.com)

:::important 중요
Crash Detection을 사용하려면 [com.apple.developer.severe-vehicular-crash-event](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.severe-vehicular-crash-event) entitlement가 필요합니다. 이 entitlement를 신청하려면 [Request Access to the Vehicular Crash Event Entitlement](https://developer.apple.com/contact/request/vehicular-crash-events/)를 참고하십시오.
:::

Crash Detection을 지원하려면 [SACrashDetectionManager](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager)를 사용해 기능 사용 가능 여부를 확인하고, 가능하다면 앱이 충돌 이벤트를 받을 수 있도록 권한을 요청하십시오. 그런 다음 이벤트를 받는 객체에 [delegate](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager/delegate)를 설정합니다. 하나의 기기에서는 하나의 앱만 Crash Detection 이벤트를 받을 수 있습니다.

앱이 Crash Detection 이벤트를 받으면 [SAEmergencyResponseManager](https://developer.apple.com/documentation/safetykit/saemergencyresponsemanager)를 사용해 지원을 제공하십시오.

:::topic-grid
## 충돌 감지
- [SACrashDetectionManager](https://developer.apple.com/documentation/safetykit/sacrashdetectionmanager): Crash Detection 이벤트의 등록과 관리를 제공합니다.
- [SAAuthorizationStatus](https://developer.apple.com/documentation/safetykit/saauthorizationstatus): 현재 Crash Detection 이벤트 권한 상태를 나타내는 열거형입니다.
- [SACrashDetectionEvent](https://developer.apple.com/documentation/safetykit/sacrashdetectionevent): 차량 충돌에 대한 정보를 설명합니다.
- [SACrashDetectionDelegate](https://developer.apple.com/documentation/safetykit/sacrashdetectiondelegate): Crash Detection 이벤트와 권한 상태 변화를 받기 위해 객체가 채택하는 프로토콜입니다.
:::

:::topic-grid
## 충돌 대응
- [SAEmergencyResponseManager](https://developer.apple.com/documentation/safetykit/saemergencyresponsemanager): Crash Detection 이벤트에 대응하는 action을 제공합니다.
- [SAEmergencyResponseDelegate](https://developer.apple.com/documentation/safetykit/saemergencyresponsedelegate): 요청된 긴급 대응 action에 대한 업데이트를 받기 위한 인터페이스입니다.
- [SACrashDetectionEvent.Response](https://developer.apple.com/documentation/safetykit/sacrashdetectionevent/response-swift.enum): Crash Detection 이벤트에 대한 가능한 긴급 대응을 정의하는 열거형입니다.
:::

:::topic-grid
## 오류 처리
- [SAErrorDomain](https://developer.apple.com/documentation/safetykit/saerrordomain): SafetyKit이 생성하는 오류 객체의 도메인입니다.
- [SAError.Code](https://developer.apple.com/documentation/safetykit/saerror/code): SafetyKit의 오류를 식별하는 코드입니다.
- [SAError](https://developer.apple.com/documentation/safetykit/saerror): SafetyKit이 보고하는 오류입니다.
:::
