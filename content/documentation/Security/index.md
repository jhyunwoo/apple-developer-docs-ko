---
route: /documentation/Security
source_url: https://developer.apple.com/documentation/Security
source_locale: en-US
section: docc
content_type: symbol
title: Security
original_title: Security
source_hash: f66301f820aaaad24717c6bc4734a4463815a253d4478740132a07618fe8638e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:59+00:00'
last_translated_at: '2026-03-13T18:10:00+09:00'
---

# Security

앱이 관리하는 데이터를 보호하고, 앱에 대한 접근을 제어합니다.

## 개요

Security 프레임워크를 사용하면 정보를 보호하고, 신뢰를 확립하며, 소프트웨어 접근을 제어할 수 있습니다. 보안 서비스는 크게 다음 목표를 지원합니다.

- 사용자 신원을 확립하고(authentication), 그다음 리소스 접근을 선택적으로 허용합니다(authorization).
- 디스크에 저장된 데이터와 네트워크 연결을 통해 이동 중인 데이터를 모두 보호합니다.
- 특정 목적을 위해 실행할 코드의 유효성을 보장합니다.

아래 이미지에 보이듯이 더 낮은 수준의 암호화 리소스를 사용해 새로운 보안 서비스를 만들 수도 있습니다. 하지만 암호화는 구현이 어렵고, 버그로 인한 비용이 대체로 매우 크기 때문에 자체 암호화 솔루션을 구현하는 일은 거의 항상 좋은 선택이 아닙니다. 앱에서 암호화가 필요하다면 Security 프레임워크를 활용하십시오.

![앱 위에 Security 프레임워크가 자리하고 있으며, 이 프레임워크가 사용자, 데이터, 코드와의 안전한 상호 작용을 가능하게 하는 도구를 제공하는 모습을 보여주는 다이어그램입니다.](https://developer.apple.com)

:::note 참고
항상 요구 사항을 충족하는 가장 높은 수준의 API를 사용하십시오. Security 프레임워크가 언제나 최선의 선택은 아닙니다. 예를 들어 안전한 네트워크 통신을 수행하려면, Security 프레임워크를 기반으로 구축된 [Foundation](https://developer.apple.com/documentation/Foundation) 프레임워크의 [URL Loading System](https://developer.apple.com/documentation/Foundation/url-loading-system)부터 먼저 고려하십시오. 앱에서 보안 프로토콜 기능에 더 낮은 수준으로 접근해야 할 때에만 secure transport API를 직접 사용하면 됩니다.
:::

:::topic-grid
## 필수 항목
- [Security updates](https://developer.apple.com/documentation/Updates/Security): Security의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 권한 부여와 인증
- [Password AutoFill](https://developer.apple.com/documentation/security/password-autofill): 앱의 로그인 및 온보딩 절차를 간소화합니다.
- [Shared Web Credentials](https://developer.apple.com/documentation/security/shared-web-credentials): iOS 앱과 해당 웹사이트 사이에서 자격 증명을 공유합니다.
- [Authorization Services](https://developer.apple.com/documentation/security/authorization-services): 운영 체제의 제한된 영역에 접근하고, macOS 앱의 특정 기능에 대한 접근을 제어합니다.
- [Authorization Plug-ins](https://developer.apple.com/documentation/security/authorization-plug-ins): 권한 부여 결정에 참여할 수 있는 플러그인을 만들어 authorization services API를 확장합니다.
- [Sessions](https://developer.apple.com/documentation/security/sessions): macOS에서 로그인, 권한 부여, 보안 세션을 관리합니다.
- [One-time codes](https://developer.apple.com/documentation/security/one-time-codes): 인증 코드와 복구 코드 입력을 간소화합니다.
:::

:::topic-grid
## 안전한 데이터
- [Keychain services](https://developer.apple.com/documentation/security/keychain-services): 사용자를 대신해 작은 데이터 조각을 안전하게 저장합니다.
- [Preventing Insecure Network Connections](https://developer.apple.com/documentation/security/preventing-insecure-network-connections): App Transport Security를 활용해 앱에서 안전한 네트워크 연결을 강제합니다.
:::

:::topic-grid
## 안전한 코드
- [Code Signing Services](https://developer.apple.com/documentation/security/code-signing-services): 시스템에서 실행 중인 서명된 코드를 검사하고 검증합니다.
- [Notarizing macOS software before distribution](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution): macOS 소프트웨어를 Apple에 공증 제출해 사용자 신뢰를 더욱 높입니다.
- [Preparing your app to work with pointer authentication](https://developer.apple.com/documentation/security/preparing-your-app-to-work-with-pointer-authentication): 앱이 향상된 보안 기능과 매끄럽게 동작하도록 arm64e 아키텍처에서 테스트합니다.
- [App Sandbox](https://developer.apple.com/documentation/security/app-sandbox): 앱이 손상되더라도 피해를 제한할 수 있도록 macOS 앱의 시스템 리소스 및 사용자 데이터 접근을 제한합니다.
- [Hardened Runtime](https://developer.apple.com/documentation/security/hardened-runtime): macOS 앱을 위한 보안 보호와 리소스 접근을 관리합니다.
- [Disabling and Enabling System Integrity Protection](https://developer.apple.com/documentation/security/disabling-and-enabling-system-integrity-protection): 드라이버, 커널 확장, 기타 저수준 코드를 테스트하기 위한 개발 과정에서만 일시적으로 시스템 보호를 비활성화합니다.
- [Using the latest code signature format](https://developer.apple.com/documentation/Xcode/using-the-latest-code-signature-format): 앱이 최신 OS 릴리스에서 실행되도록 레거시 앱 코드 서명을 업데이트합니다.
- [Updating Mac Software](https://developer.apple.com/documentation/security/updating-mac-software): 코드 서명 충돌을 일으키지 않으면서 Mac 소프트웨어 업데이트를 구현합니다.
- [TN3125: Inside Code Signing: Provisioning Profiles](https://developer.apple.com/documentation/Technotes/tn3125-inside-code-signing-provisioning-profiles): provisioning profile이 Apple 플랫폼에서 서드파티 코드 실행을 어떻게 가능하게 하는지 알아봅니다.
:::

:::topic-grid
## 실행 환경 제약
- [Applying launch environment and library constraints](https://developer.apple.com/documentation/security/applying-launch-environment-and-library-constraints): 프로세스가 로드할 수 있는 라이브러리와 실행될 수 있는 상황을 제한합니다.
- [Defining launch environment and library constraints](https://developer.apple.com/documentation/security/defining-launch-environment-and-library-constraints): 앱 구성 요소가 예상된 맥락에서만 동작하도록 제한합니다.
- [Constraining a tool’s launch environment](https://developer.apple.com/documentation/security/constraining-a-tool's-launch-environment): 구성 요소의 실행 방식을 제한해 macOS 앱의 보안을 향상합니다.
:::

:::topic-grid
## 암호화
- [Complying with Encryption Export Regulations](https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations): 앱 제출 절차를 간소화할 수 있도록 앱에서 암호화를 사용하는 사실을 신고합니다.
- [Certificate, Key, and Trust Services](https://developer.apple.com/documentation/security/certificate-key-and-trust-services): 인증서와 암호화 키를 사용해 신뢰를 수립합니다.
- [Cryptographic Message Syntax Services](https://developer.apple.com/documentation/security/cryptographic-message-syntax-services): S/MIME 메시지에 암호화 서명과 암호화를 수행합니다.
- [Randomization Services](https://developer.apple.com/documentation/security/randomization-services): 암호학적으로 안전한 난수를 생성합니다.
- [Security Transforms](https://developer.apple.com/documentation/security/security-transforms): 인코딩, 암호화, 서명, 서명 검증 같은 암호화 기능을 수행합니다.
- [ASN.1](https://developer.apple.com/documentation/security/asn-1): Distinguished Encoding Rules(DER) 및 Basic Encoding Rules(BER) 데이터 스트림을 인코딩하고 디코딩합니다.
:::

:::topic-grid
## 결과 코드
- [Security Framework Result Codes](https://developer.apple.com/documentation/security/security-framework-result-codes): 여러 Security 프레임워크 함수에서 공통으로 사용하는 결과 코드를 해석합니다.
:::

:::topic-grid
## 레거시 인터페이스
- [Common Security Services Manager](https://developer.apple.com/documentation/security/common-security-services-manager): Security 프레임워크의 레거시 구현을 뒷받침하는 오픈 소스 모듈 집합입니다.
- [Secure Transport](https://developer.apple.com/documentation/security/secure-transport): 표준화된 transport layer security 메커니즘을 사용해 안전한 네트워크 통신을 수행합니다.
- [Secure Download](https://developer.apple.com/documentation/security/secure-download): macOS에서 Apple의 Secure Download System을 구현합니다.
- [Security legacy reference](https://developer.apple.com/documentation/security/security-legacy-reference): 레거시 API를 알아봅니다.
:::

:::topic-grid
## 레퍼런스
- [Security Structures](https://developer.apple.com/documentation/security/security-structures)
- [Security Constants](https://developer.apple.com/documentation/security/security-constants)
- [Security Functions](https://developer.apple.com/documentation/security/security-functions)
- [Security Data Types](https://developer.apple.com/documentation/security/security-data-types)
:::

:::topic-grid
## 변수
- [CSSM_APPLE_PRIVATE_CSPDL_CODE_28](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_28)
- [TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256](https://developer.apple.com/documentation/security/tls_ecdhe_psk_with_chacha20_poly1305_sha256)
- [errSecMissingQualifiedCertStatement](https://developer.apple.com/documentation/security/errsecmissingqualifiedcertstatement)
- [kSecPolicyAppleEAPClient](https://developer.apple.com/documentation/security/ksecpolicyappleeapclient)
- [kSecPolicyAppleEAPServer](https://developer.apple.com/documentation/security/ksecpolicyappleeapserver)
- [kSecPolicyAppleIPSecClient](https://developer.apple.com/documentation/security/ksecpolicyappleipsecclient)
- [kSecPolicyAppleIPSecServer](https://developer.apple.com/documentation/security/ksecpolicyappleipsecserver)
- [kSecPolicyAppleSSLClient](https://developer.apple.com/documentation/security/ksecpolicyapplesslclient)
- [kSecPolicyAppleSSLServer](https://developer.apple.com/documentation/security/ksecpolicyapplesslserver)
- [kSecTrustQCStatements](https://developer.apple.com/documentation/security/ksectrustqcstatements)
- [kSecTrustQWACValidation](https://developer.apple.com/documentation/security/ksectrustqwacvalidation)
:::

:::topic-grid
## 함수
- [SecIdentityCreate(_:_:_:)](https://developer.apple.com/documentation/security/secidentitycreate(_:_:_:))
- [sec_protocol_metadata_copy_negotiated_protocol(_:)](https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_negotiated_protocol(_:))
- [sec_protocol_metadata_copy_server_name(_:)](https://developer.apple.com/documentation/security/sec_protocol_metadata_copy_server_name(_:))
:::

:::topic-grid
## 타입 별칭
- [CE_DataType](https://developer.apple.com/documentation/security/ce_datatype-swift.typealias)
- [CE_ExtendedKeyUsage](https://developer.apple.com/documentation/security/ce_extendedkeyusage-swift.typealias)
- [CE_GeneralNameType](https://developer.apple.com/documentation/security/ce_generalnametype-swift.typealias)
:::
