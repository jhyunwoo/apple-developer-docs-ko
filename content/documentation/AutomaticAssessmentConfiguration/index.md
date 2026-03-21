---
route: /documentation/AutomaticAssessmentConfiguration
source_url: https://developer.apple.com/documentation/AutomaticAssessmentConfiguration
source_locale: en-US
section: docc
content_type: symbol
title: Automatic Assessment Configuration
original_title: Automatic Assessment Configuration
source_hash: 6221df4522eb91cd3cb7906d9708cfe17b02ac64373597ee1d4f7ebc83e74b07
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:22:11+00:00'
last_translated_at: '2026-03-13T22:52:00+09:00'
---

# Automatic Assessment Configuration

시험을 치르는 동안 single-app mode로 진입하고 학생이 특정 시스템 기능에 접근하지 못하도록 막습니다.

## 개요

AutomaticAssessmentConfiguration 프레임워크를 사용하면 시스템 기능 접근을 제한하는 평가 세션을 만들 수 있습니다. 이 세션은 사용자가 앱이 제공하는 범위를 넘어 정보를 얻기 위해 기기를 사용하는 것을 막고, 앱 안의 민감한 정보를 외부로 배포하는 것도 방지합니다. 이렇게 제한된 접근은 앱이 진행하는 시험 같은 평가의 무결성을 보호하는 데 도움이 됩니다.

AutomaticAssessmentConfiguration 프레임워크를 사용하는 앱은 [com.apple.developer.automatic-assessment-configuration](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.automatic-assessment-configuration) entitlement를 가져야 합니다. entitlement를 설정한 뒤에는 [AEAssessmentSession](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession) 클래스의 인스턴스를 사용해 평가 세션을 시작하고 중지합니다.

세션은 다음과 같은 데스크톱 요소 접근을 막아 보호 기능을 제공합니다.

- Dock
- 애플리케이션 메뉴 막대
- Mission Control
- Notification Center
- 현재 공간 외의 다른 Space
- 선택적으로 허용한 앱을 제외한 다른 앱

또한 세션은 다음도 수행합니다.

- 화면 녹화와 화면 캡처를 막습니다.
- Siri를 비활성화합니다.
- 재생 중인 미디어를 멈춥니다.
- 네트워크 접근을 앱에만 허용합니다.
- Handoff를 비활성화합니다.
- 세션을 시작하고 종료할 때 pasteboard buffer를 비웁니다.

:::note 참고
학생에게 시험을 제공하는 교육용 앱을 배포한다면 [Automatic Assessment Configuration Entitlement Request](https://developer.apple.com/contact/request/automatic-assessment-configuration/) 양식을 작성해 [com.apple.developer.automatic-assessment-configuration](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.automatic-assessment-configuration) entitlement 사용 권한을 요청할 수 있습니다.
:::

이 프레임워크는 visionOS에서 실행 중인 앱이 평가를 시작하려고 하면 오류를 보고합니다.

:::topic-grid
## 핵심 사항
- [com.apple.developer.automatic-assessment-configuration](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.automatic-assessment-configuration): 앱이 평가 세션을 만들 수 있는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 세션
- [Preparing an educational assessment app for distribution](https://developer.apple.com/documentation/automaticassessmentconfiguration/preparing-an-educational-assessment-app-for-distribution): 평가 관행을 검토하고 시스템 capability를 관리하여 앱이 학업적 무결성을 유지하도록 합니다.
- [Build an Educational Assessment App](https://developer.apple.com/documentation/automaticassessmentconfiguration/build-an-educational-assessment-app): Automatic Assessment Configuration을 사용해 평가 앱의 학업적 무결성을 보장합니다.
- [AEAssessmentConfiguration](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentconfiguration): 평가 세션을 위한 구성 정보입니다.
- [AEAssessmentSession](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmentsession): 앱이 평가를 보호하기 위해 사용하는 세션입니다.
:::

:::topic-grid
## 오류
- [AEAssessmentError](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmenterror): 평가 세션이 delegate에 전달하는 오류입니다.
- [AEAssessmentError.Code](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmenterror/code): 세션이 실패했을 때 프레임워크가 반환하는 오류 코드입니다.
- [AEAssessmentErrorDomain](https://developer.apple.com/documentation/automaticassessmentconfiguration/aeassessmenterrordomain): 프레임워크가 오류를 발행할 때 사용하는 오류 도메인을 나타내는 상수입니다.
:::
