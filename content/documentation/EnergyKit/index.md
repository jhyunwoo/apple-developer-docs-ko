---
route: /documentation/EnergyKit
source_url: https://developer.apple.com/documentation/EnergyKit
source_locale: en-US
section: docc
content_type: symbol
title: EnergyKit
original_title: EnergyKit
source_hash: 7c64fea8fce85701ad4f19f6eca01c94c27b440ced30b4ee1e08b7a0f0d161ef
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:03:27+00:00'
last_translated_at: '2026-03-13T16:25:00+09:00'
---

# EnergyKit

사람들이 언제 전기를 사용할지 선택하는 데 도움을 주도록 앱에 전력망 예측 정보를 제공합니다.

## 개요

EnergyKit은 사람들이 언제 전기를 사용할지 선택할 수 있도록 앱에 전력망 예측 정보를 제공합니다. 이 예측은 각 사람의 Home 위치에 맞게 개인화되며 다양한 환경 정보와 전력망 입력을 기반으로 하고, 전력망에서 상대적으로 더 청정한 전기가 공급되는 시간을 식별합니다. 사용자가 Home App에서 전력 회사 계정에 연결한 경우에는 요금제 정보도 함께 반영됩니다.

EnergyKit은 사용자가 가정 내 기기의 전력 사용량을 관리하여 더 청정한 전력망으로의 전환을 지원할 수 있는 앱을 만드는 데 도움을 줍니다. 이는 가정용 계량기 이후 구간에서의 주거용 활용을 위한 것으로, 가전 제품, 기기, 전기차 충전과 같은 가정 내 기기의 전력 사용을 대상으로 합니다. 상업용 또는 산업용 애플리케이션을 위한 것은 아닙니다. 시스템은 스마트 온도 조절기(HVAC)와 EV 충전 같은 초기 사용 사례를 염두에 두고 설계되었습니다.

![청정 에너지 안내 기능이 활성화된 전기차 충전 앱 인터페이스입니다. 오전 7시까지 충전되도록 설정되어 있고, 설정 아래에 'Begin Charging' 버튼이 표시됩니다.](https://developer.apple.com)

EnergyKit을 사용하면 앱에서 다음 작업을 수행할 수 있습니다.

- 전력망에서 상대적으로 더 청정한 전기가 공급되는 시간대로 사용자의 전력 사용을 이동합니다.
- 사용자가 전력 회사 계정에 연결해 시간대별 요금제를 사용하는 경우, 기기 전력 소비량 또는 작동 시간에 대한 인사이트를 제공하고 더 청정한 에너지 시간대와 피크 또는 비피크 요금 시간대에 대한 안내를 제공합니다.

:::important Important
에너지 안내는 미국 본토 48개 주에서만 사용할 수 있습니다.
:::

## 앱에 entitlement 추가

EnergyKit을 사용하려면 시스템이 앱에 값이 `true`인 [com.apple.developer.energykit](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.energykit) entitlement를 요구합니다. Xcode에서 앱 타깃에 EnergyKit capability를 활성화해 이 entitlement를 추가하십시오. 자세한 내용은 [Adding capabilities to your app](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app)을 참고하십시오.

:::topic-grid
## 핵심 사항
- [Optimizing home electricity usage](https://developer.apple.com/documentation/energykit/optimizing-home-electricity-usage): 전력망이 더 청정하고 잠재적으로 더 저렴한 시간대로 전기차 충전 일정을 이동합니다.
- [com.apple.developer.energykit](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.energykit): 앱이 EnergyKit 프레임워크를 사용하기 위해 시스템이 요구하는 entitlement입니다.
:::

:::topic-grid
## 부하 이벤트
- [ElectricHVACLoadEvent](https://developer.apple.com/documentation/energykit/electrichvacloadevent): HVAC 시스템이 소비한 전력을 측정한 값입니다.
- [ElectricVehicleLoadEvent](https://developer.apple.com/documentation/energykit/electricvehicleloadevent): 충전기에 연결된 동안 전기차가 소비하거나 생성한 전력을 측정한 값입니다.
- [EnergyVenue](https://developer.apple.com/documentation/energykit/energyvenue): 해당 위치에서 전기를 사용하거나 생산하는 물리적 장소입니다.
- [ElectricityFlowDirection](https://developer.apple.com/documentation/energykit/electricityflowdirection): 전기가 어느 방향으로 이동하는지에 대한 정보입니다.
- [ElectricalLoadEventProtocol](https://developer.apple.com/documentation/energykit/electricalloadeventprotocol): 전기 부하 이벤트를 나타낼 수 있는 타입입니다.
:::

:::topic-grid
## 안내
- [ElectricityGuidance](https://developer.apple.com/documentation/energykit/electricityguidance): 언제 전기가 더 청정하고 더 저렴한지에 대한 안내를 제공하는 데이터 모델입니다.
:::

:::topic-grid
## 인사이트
- [ElectricityInsightRecord](https://developer.apple.com/documentation/energykit/electricityinsightrecord): 특정 기간 동안 전력 사용의 환경 영향과 비용 인사이트를 제공하는 구조체입니다.
- [ElectricityInsightService](https://developer.apple.com/documentation/energykit/electricityinsightservice): 전력 소비에 대한 인사이트를 가져오는 서비스입니다.
- [ElectricityInsightQuery](https://developer.apple.com/documentation/energykit/electricityinsightquery): 전력 인사이트 레코드 형태의 환경 영향 정보를 얻기 위해 사용하는 쿼리를 설명하는 구조체입니다.
- [ElectricityInsightMeasure](https://developer.apple.com/documentation/energykit/electricityinsightmeasure): 전력 사용 데이터를 측정할 수 있는 타입용 프로토콜입니다.
:::

:::topic-grid
## 오류 응답
- [EnergyKitError](https://developer.apple.com/documentation/energykit/energykiterror): 오류와 그 발생 이유를 설명하는 localized message를 제공하는 특수 오류입니다.
:::
