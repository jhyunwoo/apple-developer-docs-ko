---
route: /documentation/SecureElementCredential
source_url: https://developer.apple.com/documentation/SecureElementCredential
source_locale: en-US
section: docc
content_type: symbol
title: SecureElementCredential
original_title: SecureElementCredential
source_hash: 6df7aa9ed58ca6a403a574644f68b4b2ecc427c3f941e016f5750ffab0d10496
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:38:45+00:00'
last_translated_at: '2026-03-13T23:38:45+09:00'
---

# SecureElementCredential

기기의 Secure Element 안에 있는 자격 증명에 접근할 수 있게 합니다.

## 개요

SecureElementCredential 프레임워크를 사용하면 앱이 비접촉식 거래 기능을 갖춘 Secure Element 자격 증명을 관리하고 사용할 수 있습니다. 요구 사항, 제공 여부, 플랫폼 접근 요청 방법은 [NFC & SE Platform](https://developer.apple.com/support/nfc-se-platform)을 참고하십시오.

이 프레임워크를 사용하려면 먼저 [Applet Bundle Registry](https://register.apple.com/login) (ABR)에 applet bundle을 등록해야 합니다. applet에는 거래를 완료하는 데 필요한 암호화 코드가 들어 있습니다. 이 프레임워크를 사용해 applet과 자격 증명을 provisioning하면 ABR에서 bundle을 내려받아 Secure Element에 설치합니다. provisioning 결과로 [CredentialSession.Credential](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential) 인스턴스가 반환되며, 이후 프레임워크 호출에 이 값을 사용합니다.

[CredentialSession](https://developer.apple.com/documentation/secureelementcredential/credentialsession) 클래스는 이 프레임워크의 진입점 역할을 합니다. 이 클래스는 다음 세 가지 주요 기능을 제공합니다.

:::term-list
Management: 앱이 Secure Element 안의 자격 증명을 생성, 읽기, 업데이트, 삭제할 수 있게 합니다.
Wired actions: 자격 증명이 주어졌을 때, 해당 자격 증명과 대응하는 *applet*과 데이터를 교환할 수 있게 합니다.
Card emulation: 자격 증명이 비접촉식 리더와 통신할 수 있게 합니다.
:::

이 프레임워크는 적절한 사용자 인터페이스를 제공하면서 wired action과 card emulation을 수행하는 SwiftUI 및 UIKit 확장도 함께 제공합니다.

SecureElementCredential은 매장 결제, 자동차 키, 폐쇄형 대중교통, 사내 출입 배지, 학생증, 홈 키, 호텔 키, 가맹점 멤버십 및 리워드 카드, 이벤트 티켓 거래를 지원합니다.

:::warning Warning
이 프레임워크의 SwiftUI 확장에서 심볼을 가져오는 파일에서는 UIKit을 함께 import하지 마십시오. 반대로 UIKit 확장을 사용할 때는 같은 파일에서 SwiftUI를 함께 import하지 마십시오. SwiftUI와 UIKit을 같은 파일에서 함께 import하면 컴파일 시 모호성이 발생합니다.
:::

:::topic-grid
## 핵심
- [Secure Element 자격 증명에 접근하고 사용하기](https://developer.apple.com/documentation/secureelementcredential/accessing-and-using-secure-element-credentials): 결제 카드와 기타 자격 증명을 관리하고 사용합니다.
:::

:::topic-grid
## Entitlement
- [com.apple.developer.secure-element-credential](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.secure-element-credential): 앱이 SecureElementCredential 프레임워크를 사용할 수 있는지 나타내는 Boolean 값입니다.
- [com.apple.developer.secure-element-credential.default-contactless-app](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.secure-element-credential.default-contactless-app): SecureElementCredential 프레임워크를 사용하는 앱이 기본 비접촉식 앱이 될 수 있는지 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 자격 증명
- [CredentialSession](https://developer.apple.com/documentation/secureelementcredential/credentialsession): Secure Element에 저장된 자격 증명에 대해 작업을 수행하는 클래스입니다.
:::

:::topic-grid
## 거래
- [CredentialTransaction](https://developer.apple.com/documentation/secureelementcredential/credentialtransaction): SwiftUI 뷰에서 wired 및 비접촉식 작업을 수행하는 transaction 객체입니다.
:::

:::topic-grid
## UIKit scene delegate
- [CredentialSessionWindowSceneDelegate](https://developer.apple.com/documentation/secureelementcredential/credentialsessionwindowscenedelegate): `CredentialSession` 이벤트가 발생했음을 `UIWindowSceneDelegate`에 알려 주는 delegate입니다.
:::
