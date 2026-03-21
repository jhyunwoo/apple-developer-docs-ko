---
route: /documentation/DeviceCheck
source_url: https://developer.apple.com/documentation/DeviceCheck
source_locale: en-US
section: docc
content_type: symbol
title: DeviceCheck
original_title: DeviceCheck
source_hash: 1116140e659cff85201d0ee6e60fbb8c4b213d8d0b0a99710abfdee59eae55c2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:47:38+00:00'
last_translated_at: '2026-03-13T15:35:00+09:00'
---

# DeviceCheck

기기 상태를 관리하고 앱 무결성을 검증하여 서비스의 부정 사용을 줄입니다.

## 개요

DeviceCheck 서비스는 앱에서 접근하는 프레임워크 인터페이스와 자체 서버에서 접근하는 Apple 서버 인터페이스로 구성됩니다.

앱에서 [DCDevice](https://developer.apple.com/documentation/devicecheck/dcdevice) 클래스를 사용하면 서버에서 활용할 수 있는 토큰을 얻을 수 있습니다. 이 토큰을 사용하면 사용자 개인 정보를 보호하면서 기기당 두 개의 이진 데이터 비트를 설정하고 조회할 수 있습니다. 예를 들어 이 데이터를 사용해 이미 프로모션 혜택을 받은 기기를 식별하거나, 사기성이라고 판단한 기기에 표시를 남길 수 있습니다. 서버 간 API를 사용하면 수신한 토큰이 Apple 기기에서 실행 중인 앱에서 온 것인지도 검증할 수 있습니다.

누군가 앱을 수정해 App Store 밖에서 배포하면 게임 치트, 광고 제거, 프리미엄 콘텐츠 접근 같은 승인되지 않은 기능을 추가할 수 있습니다. App Attest 서비스는 앱이 자신의 정당성을 입증할 수 있는 방법을 제공하여, 서버가 민감한 리소스에 대한 접근을 더 신뢰할 수 있게 합니다. [DCAppAttestService](https://developer.apple.com/documentation/devicecheck/dcappattestservice) 클래스를 사용해 기기에서 특별한 암호화 키를 생성하고, Apple이 해당 키의 유효성을 증명하도록 합니다. 이후 서버에서 민감한 데이터를 요청할 때마다 이 키를 사용해 앱의 유효성을 검증합니다.

![앱과 App Attest 사이의 연결, 앱과 서버 사이의 연결, 서버와 Apple 서버 사이의 연결을 보여 주는 다이어그램입니다.](https://developer.apple.com)

단일 정책만으로 모든 사기를 없앨 수는 없습니다. 예를 들어 App Attest는 운영 체제가 손상된 기기를 결정적으로 식별할 수는 없습니다. 대신 DeviceCheck 서비스는 특정 기기에 대한 전체 위험 평가에 통합할 수 있는 정보를 제공합니다.

:::topic-grid
## 기기 식별
- [Accessing and modifying per-device data](https://developer.apple.com/documentation/devicecheck/accessing-and-modifying-per-device-data): 앱의 토큰을 사용해 Apple 서버에 저장된 기기별 이진 비트 두 개를 조회하고 수정합니다.
- [DCDevice](https://developer.apple.com/documentation/devicecheck/dcdevice): 고유하고 인증된 토큰을 제공하는 기기 표현입니다.
:::

:::topic-grid
## App Attest
- [Establishing your app’s integrity](https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity): 서버가 수신하는 요청이 앱의 정당한 인스턴스에서 왔는지 확인합니다.
- [Validating apps that connect to your server](https://developer.apple.com/documentation/devicecheck/validating-apps-that-connect-to-your-server): 서버로 연결하는 앱이 앱의 정당한 인스턴스인지 검증합니다.
- [Assessing fraud risk](https://developer.apple.com/documentation/devicecheck/assessing-fraud-risk): 서버 간 호출을 사용해 위험 데이터를 요청하고 분석합니다.
- [Preparing to use the app attest service](https://developer.apple.com/documentation/devicecheck/preparing-to-use-the-app-attest-service): 개발 환경에서 구현을 테스트하고 사용자를 점진적으로 온보딩합니다.
- [Attestation Object Validation Guide](https://developer.apple.com/documentation/devicecheck/attestation-object-validation-guide): 증명 객체 검증 프로세스 구현을 검증할 때 사용하는 가이드입니다.
- [DCAppAttestService](https://developer.apple.com/documentation/devicecheck/dcappattestservice): 기기에서 실행 중인 앱 인스턴스를 검증하는 데 사용하는 서비스입니다.
- [App Attest Environment](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.devicecheck.appattest-environment): App Attest 서비스를 사용해 자신을 검증하는 앱의 환경입니다.
:::

:::topic-grid
## 오류
- [DCError](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct): DeviceCheck에서 오류가 발생했을 때 이를 나타내는 타입입니다.
- [DCError.Code](https://developer.apple.com/documentation/devicecheck/dcerror-swift.struct/code): DeviceCheck 오류 코드입니다.
- [DCErrorDomain](https://developer.apple.com/documentation/devicecheck/dcerrordomain): DeviceCheck API 관련 오류의 도메인입니다.
:::
