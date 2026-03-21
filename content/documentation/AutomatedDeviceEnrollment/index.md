---
route: /documentation/AutomatedDeviceEnrollment
source_url: https://developer.apple.com/documentation/AutomatedDeviceEnrollment
source_locale: en-US
section: docc
content_type: symbol
title: Automated Device Enrollment
original_title: Automated Device Enrollment
source_hash: deccb73e61583030908da923c40884e7f12093037951ed47f4ba22d23521e71b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:21:35+00:00'
last_translated_at: '2026-03-13T23:21:47+09:00'
---

# Automated Device Enrollment

서드파티 MDM 앱 사용자가 macOS 및 iOS 기기를 조직에 추가할 수 있게 합니다.

## 개요

이 프레임워크는 기기 관리자가 macOS, iOS, iPadOS 기기를 Apple School Manager, Apple Business Manager, Apple Business Essentials 조직에 추가할 수 있는 사용자 인터페이스를 제공합니다. 제공되는 SwiftUI view를 사용하면 기기 등록 권한이 있는 사용자가 Managed Apple ID로 로그인하고 기기를 조직에 추가할 수 있습니다.

이 기능은 주변 기기를 발견하고 페어링하기 위한 Bluetooth 접근 권한, 그리고 시각적 페어링 PIN 코드를 스캔하기 위한 카메라 접근 권한이 필요합니다. 이 기능을 사용하려면 Automated Device Enrollment entitlement가 있어야 합니다. 이 entitlement 권한을 얻으려면 [Automated Device Enrollment Entitlement Request](https://developer.apple.com/contact/request/automated-device-enrollment/)를 참고하십시오.

:::topic-grid
## 핵심
- [automatedDeviceEnrollmentAddition(isPresented:)](https://developer.apple.com/documentation/SwiftUI/View/automatedDeviceEnrollmentAddition(isPresented:)): 사용자가 기기를 조직에 추가할 수 있도록 모달 view를 표시합니다.
- [com.apple.developer.automated-device-enrollment.add-devices](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.automated-device-enrollment.add-devices): 앱이 Automated Device Enrollment에 기기를 추가할 수 있는지 나타내는 Boolean 값입니다.
:::
