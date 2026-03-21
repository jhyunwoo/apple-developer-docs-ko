---
route: /documentation/SensorKit
source_url: https://developer.apple.com/documentation/SensorKit
source_locale: en-US
section: docc
content_type: symbol
title: SensorKit
original_title: SensorKit
source_hash: 451a42f9217eed703cff94d0495eb5a2753e27d1a2f00a23508909f8c5addafc
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:16+00:00'
last_translated_at: '2026-03-13T10:02:00+00:00'
---

# SensorKit

iPhone 또는 페어링된 Apple Watch의 센서에서 데이터와 파생 메트릭을 가져옵니다.

## 개요

시스템이 기기의 여러 센서를 사용해 정보를 수집할 때, SensorKit는 앱이 선택된 원시 데이터나 센서에서 시스템이 처리한 메트릭에 접근할 수 있게 합니다. 예를 들면 다음과 같습니다.

- 걸음 수 정보
- 가속도계 또는 회전 속도 데이터
- 사용자의 손목에 착용된 watch의 구성
- 물리적 환경의 주변광
- 사용자의 일상적인 통근 또는 이동에 대한 세부 정보

전체 목록은 [SRSensor](https://developer.apple.com/documentation/sensorkit/srsensor)를 참고하세요.

:::note Note
이 프레임워크는 Mac Catalyst로 빌드한 Mac 앱과, visionOS에서 실행되는 호환 iPad 및 iPhone 앱의 호출을 무시합니다.
:::

:::topic-grid
## 필수 항목
- [SensorKit 업데이트](https://developer.apple.com/documentation/Updates/SensorKit): SensorKit의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 설정
- [센서 읽기를 위해 프로젝트 구성하기](https://developer.apple.com/documentation/sensorkit/configuring-your-project-for-sensor-reading): 센서 데이터에 접근하기 위한 시스템 및 사용자 권한을 얻을 수 있도록 앱에 메타데이터를 추가합니다.
- [SRSensorReader](https://developer.apple.com/documentation/sensorkit/srsensorreader): 특정 센서에 대한 사용자 승인 절차를 수립하고 데이터를 기록하는 객체입니다.
:::

:::topic-grid
## 권한 부여
- [com.apple.developer.sensorkit.reader.allow](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.sensorkit.reader.allow): 앱의 사전 승인된 연구에서 필요로 하는 센서 데이터에 접근하기 위한 entitlement입니다.
:::

:::topic-grid
## 데이터 질의
- [SRFetchRequest](https://developer.apple.com/documentation/sensorkit/srfetchrequest): 샘플 질의 조건을 정의하는 객체입니다.
- [SRFetchResult](https://developer.apple.com/documentation/sensorkit/srfetchresult): 센서 리더가 가져온 기록 데이터입니다.
:::

:::topic-grid
## 데이터 해석
- [SRAmbientLightSample](https://developer.apple.com/documentation/sensorkit/srambientlightsample): 사용자의 환경에 있는 주변광의 양입니다.
- [SRDeviceUsageReport](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport): 사용자가 자신의 기기, 특정 Apple 앱, 또는 웹사이트를 사용하는 빈도와 상대적 지속 시간입니다.
- [SRKeyboardMetrics](https://developer.apple.com/documentation/sensorkit/srkeyboardmetrics): 기기 키보드의 구성과 사용 패턴입니다.
- [SRMediaEvent](https://developer.apple.com/documentation/sensorkit/srmediaevent): 이미지나 비디오 같은 미디어 객체에 대한 사용자 상호 작용입니다.
- [SRMessagesUsageReport](https://developer.apple.com/documentation/sensorkit/srmessagesusagereport): 일정 기간 동안 사용자의 Messages 앱 활동을 설명하는 객체입니다.
- [SRPhoneUsageReport](https://developer.apple.com/documentation/sensorkit/srphoneusagereport): 일정 기간 동안 사용자의 전화 활동을 설명하는 객체입니다.
- [SRVisit](https://developer.apple.com/documentation/sensorkit/srvisit): 사용자의 일상적인 이동 루틴에서의 진행 상황입니다.
- [SRWristDetection](https://developer.apple.com/documentation/sensorkit/srwristdetection): 착용자의 손목 위에 있는 watch의 구성입니다.
:::

:::topic-grid
## 샘플 삭제
- [SRDeletionRecord](https://developer.apple.com/documentation/sensorkit/srdeletionrecord): 프레임워크가 샘플을 삭제하는 이유를 설명하는 객체입니다.
:::

:::topic-grid
## 음성 분석
- [SRSpeechMetrics](https://developer.apple.com/documentation/sensorkit/srspeechmetrics): 일정 구간의 음성에 대한 메트릭을 나타내는 객체입니다.
- [SRSpeechExpression](https://developer.apple.com/documentation/sensorkit/srspeechexpression): 일정 구간의 음성에 대한 메트릭과 음성 분석 정보를 나타내는 객체입니다.
:::

:::topic-grid
## 얼굴 분석
- [SRFaceMetrics](https://developer.apple.com/documentation/sensorkit/srfacemetrics): 사용자의 얼굴에 대한 메트릭을 나타내는 객체입니다.
- [SR_ARKIT_SUPPORTED](https://developer.apple.com/documentation/sensorkit/sr_arkit_supported): SensorKit 프레임워크용 SDK에서 ARKit 프레임워크를 사용할 수 있는지 나타내는 플래그입니다.
:::

:::topic-grid
## 손목 온도 기록
- [SRWristTemperatureSession](https://developer.apple.com/documentation/sensorkit/srwristtemperaturesession): 일정 기간 동안 기기가 기록한 손목 온도를 나타내는 객체입니다.
- [SRWristTemperature](https://developer.apple.com/documentation/sensorkit/srwristtemperature): 사용자가 잠든 동안의 손목 온도입니다.
:::

:::topic-grid
## 심전도 데이터 기록
- [SRElectrocardiogramSample](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample): 샘플 심전도 센서 데이터입니다.
:::

:::topic-grid
## 광용적맥파 데이터 기록
- [SRPhotoplethysmogramSample](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramsample): 샘플 광용적맥파(PPG) 센서 데이터입니다.
:::

:::topic-grid
## 클래스
- [SRAcousticSettings](https://developer.apple.com/documentation/sensorkit/sracousticsettings)
- [SRSleepSession](https://developer.apple.com/documentation/sensorkit/srsleepsession)
:::
