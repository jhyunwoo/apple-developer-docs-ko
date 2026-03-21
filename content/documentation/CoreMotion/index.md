---
route: /documentation/CoreMotion
source_url: https://developer.apple.com/documentation/CoreMotion
source_locale: en-US
section: docc
content_type: symbol
title: Core Motion
original_title: Core Motion
source_hash: 0e62d52bf01aaa3e40c1b3b42a58ba5682856b7a8472e7e4b3f13e4a6ffe550e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:26:22+00:00'
last_translated_at: '2026-03-13T09:18:00+00:00'
---

# Core Motion

가속도계, 자이로스코프, 만보계, 환경 관련 이벤트를 처리합니다.

## 개요

Core Motion은 iOS, iPadOS, watchOS, visionOS 기기에서 사용 가능한 온보드 하드웨어로부터 동작 및 환경 관련 데이터를 보고합니다. 여기에는 기기의 가속도계와 자이로스코프, 그리고 사용 가능한 경우 만보계, 자기계, 기압계가 포함됩니다. 이 데이터를 앱에서 사용자 상호 작용, 피트니스 추적, 건강 관련 기능 등의 입력으로 사용할 수 있습니다. 예를 들어 게임은 화면상의 게임 동작을 제어하기 위해 가속도계와 자이로스코프 입력을 사용할 수 있습니다.

이 프레임워크의 서비스는 원시 값 또는 처리된 값 형태로 동작 데이터에 접근할 수 있게 하며, 많은 서비스가 두 종류의 값을 모두 제공합니다. 원시 값은 하드웨어에서 수정 없이 얻은 데이터를 반영하고, 처리된 값은 데이터 사용에 부정적인 영향을 줄 수 있는 편향 요소를 제거합니다. 예를 들어 처리된 가속도계 값은 중력으로 인한 가속이 아니라 사용자가 발생시킨 가속만 반영합니다.

모든 서비스가 모든 기기에서 사용 가능한 것은 아니며, 필요한 하드웨어가 있더라도 일부 서비스는 사용할 수 없을 수 있습니다. 예를 들어 많은 Core Motion 서비스가 visionOS 앱에서 사용 가능하지만, visionOS에서 실행되는 호환 iPad 및 iPhone 앱에서는 사용할 수 없습니다. 동작 관련 서비스를 사용하기 전에 [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager) 객체로 해당 서비스의 사용 가능 여부를 확인하세요.

:::important Important
iOS 앱은 필요한 데이터 유형에 대해 `Info.plist` 파일에 사용 목적 설명 키를 포함해야 합니다. 이 키가 없으면 해당 서비스에 접근하려 할 때 앱이 크래시합니다. 동작 및 피트니스 데이터에 접근하려면 [NSMotionUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription)을 포함하세요. 낙상 감지 서비스에 접근하려면 [NSFallDetectionUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription)을 포함하세요.
:::

:::topic-grid
## 필수 항목
- [Core Motion 업데이트](https://developer.apple.com/documentation/Updates/CoreMotion): Core Motion의 중요한 변경 사항을 알아봅니다.
- [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager): 모션 서비스를 시작하고 관리하는 객체입니다.
:::

:::topic-grid
## 기기 동작
- [처리된 기기 동작 데이터 가져오기](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data): 중력 효과 같은 환경적 편향을 제거하도록 시스템이 처리한 동작 데이터를 가져옵니다.
- [CMDeviceMotion](https://developer.apple.com/documentation/coremotion/cmdevicemotion): 기기의 자세, 회전 속도, 가속도 측정값을 캡슐화한 객체입니다.
- [CMAttitude](https://developer.apple.com/documentation/coremotion/cmattitude): 특정 시점의 기준 좌표계에 대한 기기의 방향입니다.
- [CMAttitudeReferenceFrame](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe): 자세 관련 동작 데이터의 기준 좌표계를 나타내는 상수입니다.
- [CMHeadphoneMotionManager](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager): 헤드폰 동작 서비스를 시작하고 관리하는 객체입니다.
:::

:::topic-grid
## 가속도계
- [원시 가속도계 이벤트 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-accelerometer-events): 내장 가속도계로부터 데이터를 가져옵니다.
- [CMAccelerometerData](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata): 기기의 3축 가속도계에서 얻은 데이터 샘플입니다.
- [CMRecordedAccelerometerData](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata): 기기가 기록한 단일 가속도계 데이터입니다.
- [CMSensorRecorder](https://developer.apple.com/documentation/coremotion/cmsensorrecorder): 기기의 가속도계 데이터를 수집하고 가져오는 객체입니다.
- [CMSensorDataList](https://developer.apple.com/documentation/coremotion/cmsensordatalist): 시스템이 기록한 가속도계 데이터 목록입니다.
:::

:::topic-grid
## 자이로스코프
- [원시 자이로스코프 이벤트 가져오기](https://developer.apple.com/documentation/coremotion/getting-raw-gyroscope-events): 내장 자이로스코프로부터 데이터를 가져옵니다.
- [CMGyroData](https://developer.apple.com/documentation/coremotion/cmgyrodata): 기기의 회전 속도에 대한 단일 측정값입니다.
:::

:::topic-grid
## 자기계
- [CMMagnetometerData](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata): 기기를 기준으로 측정한 지구 자기장 값입니다.
:::

:::topic-grid
## 고도 데이터
- [CMAltimeter](https://developer.apple.com/documentation/coremotion/cmaltimeter): 고도 관련 변화 전달을 시작하는 객체입니다.
- [CMAbsoluteAltitudeData](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata): 절대 고도 변화가 기록된 데이터입니다.
- [CMAltitudeData](https://developer.apple.com/documentation/coremotion/cmaltitudedata): 고도 변화가 기록된 데이터입니다.
:::

:::topic-grid
## 주변 기압
- [CMRecordedPressureData](https://developer.apple.com/documentation/coremotion/cmrecordedpressuredata): 기록된 기압 측정값입니다.
- [CMAmbientPressureData](https://developer.apple.com/documentation/coremotion/cmambientpressuredata): 주변 기압과 온도의 측정값입니다.
:::

:::topic-grid
## 수중 잠김
- [잠김 데이터에 접근하기](https://developer.apple.com/documentation/coremotion/accessing-submersion-data): water-submersion manager를 사용해 Apple Watch Ultra에서 수압, 수온, 수심 데이터를 받습니다.
- [CMWaterSubmersionManager](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanager): 잠수 중 압력과 온도 데이터 수집을 관리하는 객체입니다.
- [CMWaterSubmersionManagerDelegate](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmanagerdelegate): 주변 기압, 수압, 수온, 잠김 이벤트에 대한 업데이트를 받는 delegate입니다.
- [CMWaterSubmersionEvent](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent): 기기의 잠김 상태가 바뀌었음을 나타내는 이벤트입니다.
- [CMWaterSubmersionMeasurement](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement): 압력과 수심 데이터를 담은 업데이트입니다.
- [CMWaterTemperature](https://developer.apple.com/documentation/coremotion/cmwatertemperature): 수온 데이터를 담은 업데이트입니다.
:::

:::topic-grid
## 활동
- [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager): 기기에 저장된 동작 데이터에 대한 접근을 관리하는 객체입니다.
- [CMHeadphoneActivityManager](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager): 헤드폰 활동 서비스를 시작하고 관리하는 객체입니다.
- [CMMotionActivity](https://developer.apple.com/documentation/coremotion/cmmotionactivity): 단일 동작 업데이트 이벤트에 대한 데이터입니다.
- [헤드폰에서 모션 활동 데이터 가져오기](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones): 앱이 헤드폰의 모션 활동 변화를 수신하도록 구성합니다.
:::

:::topic-grid
## 만보계와 피트니스
- [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer): 시스템이 생성한 실시간 보행 데이터를 가져오는 객체입니다.
- [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata): 사용자가 걸어서 이동한 거리에 대한 정보입니다.
- [CMPedometerEvent](https://developer.apple.com/documentation/coremotion/cmpedometerevent): 사용자의 보행 활동 변화입니다.
- [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter): 사용자가 기기와 함께 걸은 걸음 수입니다.
- [CMOdometerData](https://developer.apple.com/documentation/coremotion/cmodometerdata): 운동용 odometer 데이터를 나타내는 클래스입니다.
- [CMHighFrequencyHeartRateData](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata): 1Hz로 수집된 심박수 데이터를 나타내는 클래스입니다.
:::

:::topic-grid
## 운동 장애
- [운동 장애 증상 데이터 가져오기](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data): Apple Watch의 운동 장애 관리자에서 데이터를 가져옵니다.
- [운동 장애 데이터 수집 요구 사항 준수하기](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements): 사용자가 앱이 수집하는 데이터를 이해하고 통제할 수 있도록 보장합니다.
- [운동 장애 알고리즘 변경 로그](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog): 운동 장애 알고리즘의 주요 변경 사항을 시간순으로 기록한 로그입니다.
- [CMMovementDisorderManager](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager): 운동 장애 데이터를 기록하고 질의하는 관리자입니다.
- [CMTremorResult](https://developer.apple.com/documentation/coremotion/cmtremorresult): 1분 간격 동안 떨림의 존재 여부와 강도에 대한 데이터를 담는 결과 객체입니다.
- [CMDyskineticSymptomResult](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult): 1분 간격 동안 운동이상증 증상이 존재할 가능성에 대한 데이터를 담는 결과 객체입니다.
:::

:::topic-grid
## 낙상 감지
- [CMFallDetectionManager](https://developer.apple.com/documentation/coremotion/cmfalldetectionmanager): 낙상 감지 이벤트를 관리하는 객체입니다.
- [CMFallDetectionDelegate](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate): 낙상 감지 이벤트와 권한 상태 변경에 대한 정보를 받는 delegate입니다.
- [CMFallDetectionEvent](https://developer.apple.com/documentation/coremotion/cmfalldetectionevent): 낙상 감지 이벤트 데이터를 담는 객체입니다.
- [NSFallDetectionUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFallDetectionUsageDescription): 앱이 낙상 감지 이벤트 데이터 접근 권한을 요청하는 이유를 사용자에게 설명하는 메시지입니다.
:::

:::topic-grid
## 과거 데이터
- [CMBatchedSensorManager](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager)
:::

:::topic-grid
## 공통 데이터
- [CMLogItem](https://developer.apple.com/documentation/coremotion/cmlogitem): 모든 동작 관련 데이터 객체의 기반 클래스입니다.
:::
