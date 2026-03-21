---
route: /documentation/SensitiveContentAnalysis
source_url: https://developer.apple.com/documentation/SensitiveContentAnalysis
source_locale: en-US
section: docc
content_type: symbol
title: SensitiveContentAnalysis
original_title: SensitiveContentAnalysis
source_hash: 59f54e0dbe81007ccc0e64dbd55ccd6f29bcd1901cbf124dc2175c7489f072f8
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:23:47+00:00'
last_translated_at: '2026-03-13T23:24:01+09:00'
---

# SensitiveContentAnalysis

이미지와 비디오를 화면에 표시하기 전에 그 안의 노출 장면을 감지하고 사용자에게 알려 더 안전한 앱 경험을 제공합니다.

## 개요

이 프레임워크를 사용하면 앱에서 콘텐츠의 노출 여부를 검사할 수 있습니다. iOS와 macOS에서는 Sensitive Content Warning 사용자 환경설정 또는 Screen Time의 Communication Safety 보호자 제어를 통해, 사용자가 원치 않거나 예상하지 못한 노출 이미지로부터 보호받고 싶다는 의사를 표시할 수 있습니다. SensitiveContentAnalysis를 사용하면 콘텐츠를 표시하기 전에 민감한 내용인지 검사하여 이러한 설정에서 사용자가 요청한 경험을 제공할 수 있습니다.

앱이 외부에서 가져온 이미지나 비디오를 획득하는 상황을 고려하고, 이 프레임워크를 사용해 해당 미디어가 민감한지 확인하십시오. 예를 들어 메시징 앱은 연락처로부터 받은 각 이미지를 검사할 수 있습니다. 교실 앱은 수업 과제 제출이나 다른 학급 활동을 위해 개인 기기에서 공유 위치로 업로드되는 항목을 평가할 수 있습니다. 화상 회의 앱은 통화 중인 모든 참가자의 비디오 스트림을 실시간으로 분석할 수 있습니다.

![왼쪽에서 오른쪽으로 진행되는 흐름도입니다. 왼쪽에는 서드파티 앱이 네트워크를 통해 이미지를 받는 장면이 있고, 중앙 Sensitive Content Analysis 영역의 Sensitivity Analyzer로 화살표가 이어집니다. 여기에서 Is Sensitive 조건에 따라 Yes와 No로 갈라지고, Yes는 앱이 민감한 콘텐츠 표시를 피하는 흐름으로, No는 앱이 민감하지 않은 콘텐츠를 표시하는 흐름으로 이어집니다.](https://developer.apple.com)

### 콘텐츠가 민감할 때 개입하기

프레임워크가 어떤 미디어에 민감한 콘텐츠가 있다고 판단하면, 사용자에게 그 사실을 알리고 사용자가 무엇을 할지 결정할 때까지 미디어를 표시하지 않도록 하십시오. 예를 들어 아래 이미지는 iOS 17의 Messages에서 잠재적으로 노골적인 이미지가 도착했을 때의 모습을 보여 줍니다. 사용자 인터페이스는 이미지를 흐리게 처리하고 다음과 같이 동작합니다.

- 사용자가 선택하면 표시된 콘텐츠를 보여 줍니다.
- 연락처 차단 같은 추가 작업 메뉴를 제공합니다.

![나란히 놓인 두 대의 iPhone에 Messages 앱이 표시됩니다. 왼쪽 기기에는 받은 이미지가 흐리게 처리되어 있고 This may be sensitive 문구와 Show 버튼이 보입니다. 오른쪽 기기에는 같은 대화에서 상세 이미지가 표시되고, 경고 삼각형 버튼에서 대체 또는 추가 옵션을 가리키는 설명이 이어집니다.](https://developer.apple.com)

:::topic-grid
## 설정
- [Detecting nudity in media and providing intervention options](https://developer.apple.com/documentation/sensitivecontentanalysis/detecting-nudity-in-media-and-providing-intervention-options): 민감할 수 있는 이미지나 비디오를 표시하기 전에 사람들에게 경고합니다.
:::

:::topic-grid
## 권한 부여
- [com.apple.developer.sensitivecontentanalysis.client](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.sensitivecontentanalysis.client): 앱이 이미지와 비디오의 노출 여부를 감지할 수 있게 하는 코드 서명 entitlement입니다.
:::

:::topic-grid
## 이미지 및 비디오 파일 분석
- [SCSensitivityAnalyzer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalyzer): 민감한 콘텐츠 여부를 분석하는 객체입니다.
- [SCSensitivityAnalysisPolicy](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysispolicy): 프레임워크가 민감한 콘텐츠를 검사하는 방식과 앱이 이에 응답하는 방식을 나타내는 구성입니다.
:::

:::topic-grid
## 비디오 스트림 분석
- [SCVideoStreamAnalyzer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer): 프레임을 분석해 민감한 콘텐츠를 확인하면서 비디오 스트림을 모니터링하는 객체입니다.
:::

:::topic-grid
## 분석 결과
- [SCSensitivityAnalysis](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis): 민감한 콘텐츠 존재 여부와 개입 지침을 나타내는 객체입니다.
:::

:::topic-grid
## 테스트
- [Testing your app’s response to sensitive media](https://developer.apple.com/documentation/sensitivecontentanalysis/testing-your-app-s-response-to-sensitive-media): Apple이 테스트용으로 제공하는 특수 QR 코드와 프로파일을 사용해 앱의 개입 흐름을 실행합니다.
:::
