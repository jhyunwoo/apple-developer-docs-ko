---
route: /documentation/SecurityInterface
source_url: https://developer.apple.com/documentation/SecurityInterface
source_locale: en-US
section: docc
content_type: symbol
title: Security Interface
original_title: Security Interface
source_hash: 4714f72da9022bd594db35d0d9ed40fcaba78db7de33f1d83b4bb2d181e6fc3a
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:47:52+00:00'
last_translated_at: '2026-03-14T00:13:00+09:00'
---

# Security Interface

인증, 디지털 인증서 접근, keychain 항목 접근 같은 보안 기능을 위한 사용자 인터페이스 요소를 제공합니다.

## 개요

:::note Note
이 문서는 이전에 *Security Objective-C API*라는 제목이었습니다. `SFAuthorization` 클래스 문서는 이제 별도 문서인 [Security Foundation](https://developer.apple.com/documentation/SecurityFoundation)에 있습니다.
:::

Security Interface 프레임워크는 인증, 디지털 인증서 접근, keychain 항목 접근 같은 보안 기능을 구현하는 프로그램을 위한 사용자 인터페이스 요소를 제공하는 Objective-C 클래스 집합입니다.

:::topic-grid
## 클래스
- [SFAuthorizationPluginView](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview): 인증 플러그인 개발자가 자신의 플러그인이 표시할 사용자 정의 뷰를 만들 수 있게 합니다.
- [SFAuthorizationView](https://developer.apple.com/documentation/securityinterface/sfauthorizationview): 사용자 인터페이스가 제한된 접근을 갖는다는 것을 나타내는 잠금 아이콘을 표시하는 역할을 하는 클래스입니다.
- [SFCertificatePanel](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel): 하나 이상의 인증서를 표시하는 패널 또는 시트입니다.
- [SFCertificateTrustPanel](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel): 인증서 체인 안의 인증서에 대한 신뢰 설정을 사용자가 편집할 수 있게 하는 패널 또는 시트입니다.
- [SFCertificateView](https://developer.apple.com/documentation/securityinterface/sfcertificateview): 인증서 세부 정보 표시, 신뢰 설정 표시, 사용자의 인증서 신뢰 설정 편집 허용 옵션과 함께 인증서 내용을 표시하는 뷰입니다.
- [SFChooseIdentityPanel](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel): 사용자가 선택할 수 있는 identity 목록을 담는 패널 또는 시트입니다.
- [SFChooseIdentityTableCellView](https://developer.apple.com/documentation/securityinterface/sfchooseidentitytablecellview)
- [SFKeychainSavePanel](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel): 사용자가 keychain을 생성할 수 있게 하는 패널 또는 시트입니다.
- [SFKeychainSettingsPanel](https://developer.apple.com/documentation/securityinterface/sfkeychainsettingspanel): 사용자가 자신의 keychain 설정을 변경할 수 있게 하는 패널 또는 시트입니다.
:::

:::topic-grid
## 참고 자료
- [SFAuthorizationViewState](https://developer.apple.com/documentation/securityinterface/sfauthorizationviewstate): authorization view의 현재 상태를 정의합니다.
- [SFButtonType](https://developer.apple.com/documentation/securityinterface/sfbuttontype): 인증 플러그인에서 사용하는 버튼 타입을 정의하는 상수입니다.
- [SFViewType](https://developer.apple.com/documentation/securityinterface/sfviewtype): 인증 플러그인이 요청하는 view 타입을 정의하는 상수입니다.
- [SecurityInterface Constants](https://developer.apple.com/documentation/securityinterface/securityinterface-constants): SecurityInterface 프레임워크의 상수입니다.
- [SecurityInterface Data Types](https://developer.apple.com/documentation/securityinterface/securityinterface-data-types): Security Interface 프레임워크에서 찾을 수 있는 데이터 타입입니다.
- [SecurityInterface Enumerations](https://developer.apple.com/documentation/securityinterface/securityinterface-enumerations)
:::
