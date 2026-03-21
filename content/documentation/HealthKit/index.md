---
route: /documentation/HealthKit
source_url: https://developer.apple.com/documentation/HealthKit
source_locale: en-US
section: docc
content_type: symbol
title: HealthKit
original_title: HealthKit
source_hash: 101c00db5f2ba7065cdff538db6070cf4c37593c7ccbd4cc8ed7af39e2f92c56
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:49:11+00:00'
last_translated_at: '2026-03-14T02:20:00+09:00'
---

# HealthKit

사용자의 개인 정보 보호와 제어를 유지하면서 건강 및 피트니스 데이터에 접근하고 이를 공유합니다.

## 개요

HealthKit은 iPhone과 Apple Watch의 건강 및 피트니스 데이터를 위한 중앙 저장소를 제공합니다. 사용자의 허가를 받으면 앱은 HealthKit 저장소와 통신해 이 데이터에 접근하고 이를 공유할 수 있습니다.

![건강 앱의 요약 화면을 보여 주는 이미지입니다.](https://developer.apple.com)

완전하고 개인화된 건강 및 피트니스 경험을 만들려면 다양한 작업이 필요합니다.

- 건강 및 피트니스 데이터 수집 및 저장
- 데이터 분석 및 시각화
- 소셜 상호 작용 지원

HealthKit 앱은 이런 경험을 구축할 때 협업적인 접근 방식을 취합니다. 앱이 이 모든 기능을 제공할 필요는 없습니다. 대신 가장 관심 있는 작업 부분집합에만 집중할 수 있습니다.

예를 들어 사용자는 자신의 필요에 맞게 조정된 체중 추적 앱, 걸음 수 측정 앱, 건강 챌린지 앱을 각각 선택할 수 있습니다. HealthKit 앱은 사용자 허가 아래 데이터를 자유롭게 교환할 수 있기 때문에, 이렇게 결합된 앱 모음은 단일 앱 하나만으로는 제공할 수 없는 더 맞춤화된 경험을 제공합니다. 예를 들어 친구들이 매일 걸음 수 챌린지에 참여할 때, 각 사람은 자신이 선호하는 하드웨어 기기와 앱으로 걸음 수를 추적하고, 그룹 전체는 동일한 소셜 앱을 사용해 챌린지를 진행할 수 있습니다.

HealthKit은 또한 여러 소스의 데이터를 관리하고 병합하도록 설계되었습니다. 예를 들어 사용자는 건강 앱에서 모든 데이터를 보고 관리할 수 있으며, 여기에는 데이터 추가, 데이터 삭제, 앱 권한 변경이 포함됩니다. 따라서 앱 외부에서 이런 변경이 발생하더라도 앱은 이를 처리할 수 있어야 합니다.

:::note Note
건강 데이터에는 민감한 개인 정보가 포함될 수 있으므로, 앱은 HealthKit 저장소에서 데이터를 읽거나 데이터를 쓸 때 사용자 허가를 받아야 합니다. 또한 항상 해당 데이터를 보호하기 위한 조치를 취해야 합니다. 자세한 내용은 [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy)를 참고하십시오.
:::

:::topic-grid
## 기초
- [About the HealthKit framework](https://developer.apple.com/documentation/healthkit/about-the-healthkit-framework): HealthKit 프레임워크의 아키텍처와 설계를 알아봅니다.
- [Setting up HealthKit](https://developer.apple.com/documentation/healthkit/setting-up-healthkit): HealthKit 저장소를 설정하고 구성합니다.
- [Authorizing access to health data](https://developer.apple.com/documentation/healthkit/authorizing-access-to-health-data): 앱에서 데이터를 읽고 공유하기 위한 권한을 요청합니다.
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy): 사용자의 개인 정보를 존중하고 보호합니다.
- [HealthKit updates](https://developer.apple.com/documentation/Updates/HealthKit): HealthKit의 중요한 변경 사항을 살펴봅니다.
- [HealthKitUI](https://developer.apple.com/documentation/healthkitui): 사용자가 자신의 건강 데이터를 보고 상호 작용할 수 있게 하는 사용자 인터페이스를 표시합니다.
:::

:::topic-grid
## 건강 데이터
- [Saving data to HealthKit](https://developer.apple.com/documentation/healthkit/saving-data-to-healthkit): HealthKit sample을 생성하고 공유합니다.
- [Reading data from HealthKit](https://developer.apple.com/documentation/healthkit/reading-data-from-healthkit): query를 사용해 HealthKit에서 sample 데이터를 요청합니다.
- [HKHealthStore](https://developer.apple.com/documentation/healthkit/hkhealthstore): HealthKit이 관리하는 모든 데이터에 접근하는 진입점입니다.
- [Creating a Mobility Health App](https://developer.apple.com/documentation/healthkit/creating-a-mobility-health-app): 임상 치료 팀이 이동성 데이터를 주고받을 수 있게 하는 건강 앱을 만듭니다.
- [Data types](https://developer.apple.com/documentation/healthkit/data-types): HealthKit에서 사용하는 데이터 종류를 지정합니다.
- [Samples](https://developer.apple.com/documentation/healthkit/samples): 건강 및 피트니스 sample을 생성하고 저장합니다.
- [Queries](https://developer.apple.com/documentation/healthkit/queries): 건강 및 피트니스 데이터를 질의합니다.
- [Visualizing HealthKit State of Mind in visionOS](https://developer.apple.com/documentation/healthkit/visualizing-healthkit-state-of-mind-in-visionos): 앱에 HealthKit State of Mind를 통합하고 visionOS에서 데이터를 시각화합니다.
- [Logging symptoms associated with a medication](https://developer.apple.com/documentation/healthkit/logging-symptoms-associated-with-a-medication): HealthKit 저장소에서 약물과 복용 이벤트를 가져오고, 이를 연결할 symptom sample을 생성합니다.
:::

:::topic-grid
## 운동 데이터
- [Workouts and activity rings](https://developer.apple.com/documentation/healthkit/workouts-and-activity-rings): workout, workout session, activity summary를 관리합니다.
:::

:::topic-grid
## 오류
- [HKError](https://developer.apple.com/documentation/healthkit/hkerror): HealthKit 메서드가 반환하는 오류입니다.
- [HKErrorDomain](https://developer.apple.com/documentation/healthkit/hkerrordomain): 모든 HealthKit 오류의 도메인입니다.
- [HKError.Code](https://developer.apple.com/documentation/healthkit/hkerror/code): HealthKit이 반환하는 오류 코드입니다.
:::

:::topic-grid
## 참고 자료
- [HealthKit Enumerations](https://developer.apple.com/documentation/healthkit/healthkit-enumerations)
- [HealthKit Classes](https://developer.apple.com/documentation/healthkit/healthkit-classes)
- [HealthKit Constants](https://developer.apple.com/documentation/healthkit/healthkit-constants)
- [HealthKit Data Types](https://developer.apple.com/documentation/healthkit/healthkit-data-types)
- [HealthKit Functions](https://developer.apple.com/documentation/healthkit/healthkit-functions)
- [Macros](https://developer.apple.com/documentation/healthkit/healthkit-macros)
- [HealthKit Variables](https://developer.apple.com/documentation/healthkit/healthkit-variables)
:::
