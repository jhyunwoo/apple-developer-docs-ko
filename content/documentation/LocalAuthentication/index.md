---
route: /documentation/LocalAuthentication
source_url: https://developer.apple.com/documentation/LocalAuthentication
source_locale: en-US
section: docc
content_type: symbol
title: Local Authentication
original_title: Local Authentication
source_hash: e9c55035a69b94732fc8bf3f9324e78eee53f35db4d5d3ee255b51b623edae51
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:55+00:00'
last_translated_at: '2026-03-13T18:25:00+09:00'
---

# Local Authentication

생체 인증 또는 사용자가 이미 알고 있는 암호 구문으로 사용자를 인증합니다.

## 개요

많은 사용자가 Face ID, Touch ID, Optic ID와 같은 생체 인증에 의존해 자신의 기기에 안전하고 손쉬운 접근을 활성화합니다. 대체 옵션으로, 그리고 생체 인증이 없는 기기에서는 암호 또는 비밀번호가 비슷한 역할을 합니다. LocalAuthentication 프레임워크를 사용하면 앱에서 이러한 메커니즘을 활용하고, 앱이 이미 구현한 인증 절차를 확장할 수 있습니다.

![사용자 공간에서 동작하는 앱, 운영 체제의 LocalAuthentication 프레임워크, Secure Enclave 사이의 관계를 보여 주는 다이어그램입니다.](https://developer.apple.com)

보안을 최대화하기 위해 앱은 기본 인증 데이터에 절대 접근할 수 없습니다. 예를 들어 지문 이미지에 접근할 수 없습니다. 시스템의 나머지 부분과 격리된 하드웨어 기반 보안 프로세서인 Secure Enclave가 이 데이터를 관리하며, 운영 체제조차 접근할 수 없도록 보호합니다. 대신 특정 정책을 지정하고 사용자가 왜 인증해야 하는지 알려 주는 메시지를 제공합니다. 그러면 프레임워크가 Secure Enclave와 협조하여 작업을 수행합니다. 이후 앱은 인증 성공 또는 실패를 나타내는 Boolean 결과만 받습니다.

:::topic-grid
## 핵심 사항
- [Logging a User into Your App with Face ID or Touch ID](https://developer.apple.com/documentation/localauthentication/logging-a-user-into-your-app-with-face-id-or-touch-id): 자체 인증 체계에 생체 인증을 보완적으로 추가하여 사용자가 앱의 민감한 부분에 쉽게 접근할 수 있게 합니다.
- [Accessing Keychain Items with Face ID or Touch ID](https://developer.apple.com/documentation/localauthentication/accessing-keychain-items-with-face-id-or-touch-id): 생체 인증으로 keychain 항목을 보호합니다.
:::

:::topic-grid
## 인증과 접근
- [LARight](https://developer.apple.com/documentation/localauthentication/laright): 리소스나 작업에 대한 접근을 통제하는 요구 사항의 묶음입니다.
- [LARight.State](https://developer.apple.com/documentation/localauthentication/laright/state-swift.enum): 권한 부여 중 right가 가질 수 있는 상태입니다.
- [LAContext](https://developer.apple.com/documentation/localauthentication/lacontext): 인증 정책과 접근 제어를 평가하는 메커니즘입니다.
:::

:::topic-grid
## 영속성
- [LARightStore](https://developer.apple.com/documentation/localauthentication/larightstore): right로 보호되는 데이터를 담는 컨테이너입니다.
- [LAPersistedRight](https://developer.apple.com/documentation/localauthentication/lapersistedright): 키와 비밀에 대한 접근을 통제하는 right입니다.
- [LASecret](https://developer.apple.com/documentation/localauthentication/lasecret): 영속화된 right로 보호되는 데이터입니다.
:::

:::topic-grid
## 키 쌍
- [LAPublicKey](https://developer.apple.com/documentation/localauthentication/lapublickey): 비대칭 키 쌍의 공개 부분입니다.
- [LAPrivateKey](https://developer.apple.com/documentation/localauthentication/laprivatekey): 비대칭 키 쌍의 개인 부분입니다.
:::

:::topic-grid
## 요구 사항
- [LAAuthenticationRequirement](https://developer.apple.com/documentation/localauthentication/laauthenticationrequirement): right를 보호하는 요구 사항 집합입니다.
- [LABiometryFallbackRequirement](https://developer.apple.com/documentation/localauthentication/labiometryfallbackrequirement): 생체 인증을 사용할 수 없을 때 대체로 사용하는 요구 사항 집합입니다.
:::

:::topic-grid
## 인증 view
- [LocalAuthenticationView](https://developer.apple.com/documentation/localauthentication/localauthenticationview): 인증 인터페이스를 표시하는 SwiftUI view입니다.
:::

:::topic-grid
## 오류
- [LAError](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct): LocalAuthentication 프레임워크가 발생시키는 오류입니다.
- [LAError.Code](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code): LocalAuthentication 프레임워크가 발생시키는 오류 코드입니다.
- [LAErrorDomain](https://developer.apple.com/documentation/localauthentication/laerrordomain): 프레임워크가 오류를 발생시킬 때 사용하는 오류 도메인입니다.
:::

:::topic-grid
## 참고 자료
- [LocalAuthentication Constants](https://developer.apple.com/documentation/localauthentication/localauthentication-constants)
:::

:::topic-grid
## 클래스
- [LADomainState](https://developer.apple.com/documentation/localauthentication/ladomainstate)
- [LADomainStateBiometry](https://developer.apple.com/documentation/localauthentication/ladomainstatebiometry)
- [LADomainStateCompanion](https://developer.apple.com/documentation/localauthentication/ladomainstatecompanion)
- [LAEnvironment](https://developer.apple.com/documentation/localauthentication/laenvironment)
:::

:::topic-grid
## 변수
- [kLAAccessControlOperationCreateItem](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationcreateitem)
- [kLAAccessControlOperationCreateKey](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationcreatekey)
- [kLAAccessControlOperationUseItem](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationuseitem)
- [kLAAccessControlOperationUseKeyDecrypt](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationusekeydecrypt)
- [kLAAccessControlOperationUseKeyKeyExchange](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationusekeykeyexchange)
- [kLAAccessControlOperationUseKeySign](https://developer.apple.com/documentation/localauthentication/klaaccesscontroloperationusekeysign)
- [kLACompanionTypeMac](https://developer.apple.com/documentation/localauthentication/klacompaniontypemac)
- [kLACompanionTypeNone](https://developer.apple.com/documentation/localauthentication/klacompaniontypenone)
- [kLACompanionTypeVision](https://developer.apple.com/documentation/localauthentication/klacompaniontypevision)
- [kLACompanionTypeWatch](https://developer.apple.com/documentation/localauthentication/klacompaniontypewatch)
- [kLAErrorCompanionNotAvailable](https://developer.apple.com/documentation/localauthentication/klaerrorcompanionnotavailable)
- [kLAPolicyDeviceOwnerAuthenticationWithBiometricsOrCompanion](https://developer.apple.com/documentation/localauthentication/klapolicydeviceownerauthenticationwithbiometricsorcompanion)
- [kLAPolicyDeviceOwnerAuthenticationWithCompanion](https://developer.apple.com/documentation/localauthentication/klapolicydeviceownerauthenticationwithcompanion)
:::

:::topic-grid
## 열거형
- [LACompanionType](https://developer.apple.com/documentation/localauthentication/lacompaniontype)
:::
