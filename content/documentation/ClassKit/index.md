---
route: /documentation/ClassKit
source_url: https://developer.apple.com/documentation/ClassKit
source_locale: en-US
section: docc
content_type: symbol
title: ClassKit
original_title: ClassKit
source_hash: d3cd639e4b74ba689fb4c2beeaa484ef9e4a16a80be9497280f9d0e108b97cc4
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:56:51+00:00'
last_translated_at: '2026-03-14T02:40:00+09:00'
---

# ClassKit

교사가 앱 콘텐츠에서 활동을 과제로 배정하고 학생 진행 상황을 볼 수 있게 합니다.

## 개요

교육용 앱은 책과 비디오 같은 리소스에 대한 접근을 제공하는 동시에, 인터랙티브한 시각화, 게임, 평가를 통해 학습을 강화합니다. ClassKit을 사용하면 교육 자료를 구성해 교사가 학생에게 활동을 배정하고 진행 상황을 확인할 수 있습니다.

ClassKit 환경은 iCloud를 통해 통신하는 교사의 기기와 다수의 학생 기기로 구성됩니다. 각 기기에는 Apple의 Schoolwork 앱과 함께 앱(그리고 다른 교육용 앱들)이 실행되며, ClassKit은 기기 위에서 허브 역할을 합니다. 교사는 Schoolwork를 사용해 앱이 ClassKit에 노출하는 assignable content를 볼 수 있습니다. 그런 다음 그 콘텐츠를 바탕으로 과제를 만들고 모든 학생의 진행 상황을 모니터링할 수 있습니다. 반면 학생은 Schoolwork를 사용해 앱의 콘텐츠에 직접 연결되는 과제를 받습니다.

![앱이 가상 교실의 다른 요소와 어떻게 연결되는지 보여 주는 다이어그램입니다.](https://developer.apple.com)

ClassKit은 앱에 이미 존재하는 로직이나 저장 메커니즘을 대체하지 않으며, 새로운 사용자 인터페이스를 생성하는 데에도 사용하지 않습니다. 대신 이미 갖춘 구조를 ClassKit에 공개해, 교사가 Apple의 Schoolwork 앱을 사용해 앱 콘텐츠를 기반으로 과제를 만들고 그 과제를 통한 학생 진행 상황을 측정할 수 있게 합니다.

학생이 보는 제출 기능에는 [ClassKit UI](https://developer.apple.com/documentation/classkitui) 프레임워크를 사용하십시오. 이 프레임워크는 학생이 앱 안에서 직접 배정된 문서를 제출하고 제출 상태를 추적할 수 있게 하는 view를 제공합니다.

:::note Note
ClassKit은 [Apple School Manager and Managed Apple IDs](https://www.apple.com/education/it/)를 사용하는 교육 기관을 위해 설계되었습니다. 교육 시장이 의도한 대상이라면 ClassKit 채택을 고려하십시오.
:::

:::topic-grid
## 기초
- [Enabling ClassKit in your app](https://developer.apple.com/documentation/classkit/enabling-classkit-in-your-app): 앱과 개발 환경이 ClassKit을 채택할 수 있도록 준비합니다.
- [ClassKit Environment Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.ClassKit-environment): Schoolwork 앱과 함께 동작하는 교육용 앱을 위한 ClassKit 개발 또는 운영 환경 entitlement입니다.
- [Incorporating ClassKit into an Educational App](https://developer.apple.com/documentation/classkit/incorporating-classkit-into-an-educational-app): 과제를 설정하고 학생 진행 상황을 기록하는 과정을 단계별로 살펴봅니다.
- [ClassKit UI](https://developer.apple.com/documentation/classkitui): 학생이 앱에서 배정된 문서를 제출하고 제출을 철회할 수 있게 하는 view를 표시합니다.
- [CLSDataStore](https://developer.apple.com/documentation/classkit/clsdatastore): 앱 안의 모든 ClassKit 데이터를 담는 container입니다.
:::

:::topic-grid
## 컨텍스트
- [Advertising your app’s assignable content](https://developer.apple.com/documentation/classkit/advertising-your-app-s-assignable-content): context 계층 구조를 조립하고 앱의 assignable content를 선언합니다.
- [CLSContext](https://developer.apple.com/documentation/classkit/clscontext): quiz나 chapter처럼 배정 가능한 작업을 나타내는 앱의 한 영역입니다.
- [CLSContextProvider](https://developer.apple.com/documentation/classkit/clscontextprovider): ClassKit context provider app extension이 context를 업데이트하도록 지시하는 데 사용하는 인터페이스입니다.
:::

:::topic-grid
## 활동
- [Recording student progress](https://developer.apple.com/documentation/classkit/recording-student-progress): 과제를 통한 학생 진행 상황을 기록하기 위한 activity를 생성합니다.
- [CLSActivity](https://developer.apple.com/documentation/classkit/clsactivity): context와의 사용자 상호 작용을 나타내는 표현입니다.
:::

:::topic-grid
## 활동 항목
- [Recording additional metrics about a completed task](https://developer.apple.com/documentation/classkit/recording-additional-metrics-about-a-completed-task): activity에 activity item을 추가해 학생의 과제 완료 시도에 대한 추가 정보를 기록합니다.
- [CLSScoreItem](https://developer.apple.com/documentation/classkit/clsscoreitem): 가능한 최대값 대비 점수를 나타내는 activity 정보입니다.
- [CLSBinaryItem](https://developer.apple.com/documentation/classkit/clsbinaryitem): 참 또는 거짓, 합격 또는 불합격, 예 또는 아니오를 나타내는 activity 정보입니다.
- [CLSQuantityItem](https://developer.apple.com/documentation/classkit/clsquantityitem): 수량을 나타내는 activity 정보입니다.
- [CLSActivityItem](https://developer.apple.com/documentation/classkit/clsactivityitem): activity에 대한 정보를 수집하기 위한 추상 기본 클래스입니다.
:::

:::topic-grid
## 오류
- [CLSError](https://developer.apple.com/documentation/classkit/clserror): ClassKit이 발생시키는 오류입니다.
- [CLSErrorCodeDomain](https://developer.apple.com/documentation/classkit/clserrorcodedomain): ClassKit이 오류를 발생시킬 때 사용하는 오류 도메인입니다.
- [CLSError.Code](https://developer.apple.com/documentation/classkit/clserror/code): ClassKit이 발생시키는 오류 코드입니다.
- [CLSErrorUserInfoKey](https://developer.apple.com/documentation/classkit/clserroruserinfokey): ClassKit이 생성하는 오류의 user info dictionary 안에 나타나는 key입니다.
:::
