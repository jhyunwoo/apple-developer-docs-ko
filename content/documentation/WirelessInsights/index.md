---
route: /documentation/WirelessInsights
source_url: https://developer.apple.com/documentation/WirelessInsights
source_locale: en-US
section: docc
content_type: symbol
title: WirelessInsights
original_title: WirelessInsights
source_hash: ac6e9283b4df4b9cf2e798155de7347e6332eabd09b63473abe545959000fa8e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:54:06+00:00'
last_translated_at: '2026-03-14T02:30:00+09:00'
---

# WirelessInsights

셀룰러 데이터 서비스 상태가 변할 것으로 예상될 때 알림을 받습니다.

## 개요

WirelessInsights 프레임워크는 네트워크 상태가 앱의 데이터 사용 능력에 영향을 줄 수 있을 때 이를 앱에 알려 줍니다. 이 프레임워크는 기기 위에서 셀룰러 상태에 대한 metric을 수집합니다. 예를 들면 기기가 서비스 가능 상태인지, 현재 셀룰러 혼잡도가 어떤지 등이 있습니다. 이 정보를 사용하면 앱 사용 경험을 개선할 수 있습니다.

앱이 셀룰러 서비스가 저하될 가능성에 대한 알림을 받으면, 다음과 같은 여러 방식으로 문제에 적응할 수 있습니다.

- 이벤트 전에 데이터를 prefetch하고 buffer하기
- bit rate 줄이기
- 셀룰러 상태가 더 나아질 때까지 작업 미루기
- 추가 retry 로직 구축하기

앱은 영향도와 예상 시점으로 예측 이벤트를 설명하는 [ServicePrediction](https://developer.apple.com/documentation/wirelessinsights/serviceprediction) 인스턴스의 비동기 sequence를 받습니다. 예측에는 예측의 각 요소에 대한 신뢰 수준을 나타내는 metric도 함께 포함됩니다.

앱은 셀룰러 데이터 사용 방식에 맞는 적절한 조치를 취할 수 있습니다. 예를 들면 다음과 같습니다.

- 스트리밍 미디어 앱은 길고 영향도가 큰 이벤트 예측에 대해 이벤트 전에 미디어를 buffer하거나 bit rate를 선제적으로 낮출 수 있습니다.
- 큰 파일을 일회성으로 다운로드하는 앱은 이벤트가 지나간 뒤까지 다운로드를 미룰 수 있습니다.

:::important Important
WirelessInsights 프레임워크는 Mac Catalyst로 빌드한 앱 안에도 존재하지만 기능은 없습니다. 대신 [servicePredictions](https://developer.apple.com/documentation/wirelessinsights/servicepredictionprovider/servicepredictions) sequence를 순회하려 하면 [ServicePredictionError.unsupportedDevice](https://developer.apple.com/documentation/wirelessinsights/servicepredictionerror/unsupporteddevice) 오류가 발생합니다. 이 동작은 visionOS에서 실행되는 iOS 앱이나 Apple silicon 기반 macOS에서 실행되는 iOS 앱에서도 동일하게 나타납니다. iPad에서는 셀룰러 지원 iPad 기기에서 예측을 제공할 수 있지만 Wi-Fi 전용 기기에서는 제공하지 않을 수 있습니다. 앱이 이 오류를 예상하고 지원되지 않는 기기에서 이를 자연스럽게 처리하도록 하십시오.
:::

:::topic-grid
## 기초
- [ServicePredictionProvider](https://developer.apple.com/documentation/wirelessinsights/servicepredictionprovider): 다가오는 이벤트와 이상 현상에 대한 셀룰러 서비스 예측을 제공하는 클래스입니다.
- [Wireless Insights Service Predictions](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.wireless-insights.service-predictions): 앱이 WirelessInsights 프레임워크를 사용해 무선 서비스 예측을 가져올 수 있는지를 나타내는 Boolean 값입니다.
:::
