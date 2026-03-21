---
route: /documentation/CryptoTokenKit
source_url: https://developer.apple.com/documentation/CryptoTokenKit
source_locale: en-US
section: docc
content_type: symbol
title: CryptoTokenKit
original_title: CryptoTokenKit
source_hash: df5972dee3f1ed4dfb8314e98ce1fa845da1661b121e1571fc73697bca898778
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:47:52+00:00'
last_translated_at: '2026-03-14T00:13:00+09:00'
---

# CryptoTokenKit

보안 토큰과 그 안에 저장된 암호화 자산에 접근합니다.

## 개요

CryptoTokenKit 프레임워크를 사용하면 암호화 토큰에 쉽게 접근할 수 있습니다. 토큰은 시스템에 내장된 물리 장치이거나, 연결된 하드웨어(예: 스마트 카드)에 있거나, 네트워크 연결을 통해 접근 가능한 장치입니다. 토큰은 키와 인증서 같은 암호화 객체를 저장합니다. 또한 이러한 객체를 사용해 암호화나 디지털 서명 검증 같은 작업을 수행할 수도 있습니다. 이 프레임워크를 사용하면 토큰의 자산이 토큰 안에서 안전하게 보호된 상태를 유지하면서도 마치 시스템의 일부인 것처럼 다룰 수 있습니다.

이 프레임워크를 사용하면 macOS에서 토큰을 이중 인증용으로 활성화할 수도 있습니다. 인증 서비스는 사용자와 토큰에 저장된 신원 사이의 연결을 관리하며, 적절한 토큰이 존재하고 잠금 해제되어 있을 때 사용자에게 접근 권한을 부여합니다. 사용자는 인증 서비스와 기본 토큰 하드웨어 사이의 간극을 메우는 app extension 형태의 토큰 드라이버를 제공합니다.

macOS 10.15.4부터 CryptoTokenKit 프레임워크는 항상 사용 가능한 토큰, 즉 persistent token을 지원합니다. persistent token 지원은 Hardware Security Module(HSM)의 토큰에 대한 접근을 제공합니다. 토큰 extension을 호스팅하는 앱은 시스템이 사용 가능한 토큰을 식별하고 사용하게 하며, 토큰에 접근해 사용 가능한 identity를 식별하고 사용하게 하며, 토큰에 대한 추가 구성 정보에도 접근할 수 있게 합니다. persistent token은 사용자별 기준으로 사용 가능하므로 사용자가 로그인한 뒤에야 접근할 수 있기 때문에, 사용자 로그인 검증에는 적합하지 않습니다.

:::note Note
특정 컴퓨터에서 사용자와 토큰 사이의 연결을 관리하려면 `sc_auth` 명령줄 유틸리티를 사용합니다. 자세한 내용은 `sc_auth(8)` man page를 참고합니다.
:::

:::topic-grid
## 스마트 카드
- [Using Cryptographic Assets Stored on a Smart Card](https://developer.apple.com/documentation/cryptotokenkit/using-cryptographic-assets-stored-on-a-smart-card): 스마트 카드에 저장된 인증서, 키, identity에 마치 keychain의 일부인 것처럼 접근합니다.
- [TKSmartCardSlotManager](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager): 사용 가능한 모든 스마트 카드 리더 슬롯에 대한 인터페이스입니다.
- [TKSmartCardSlot](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot): 시스템 안의 단일 스마트 카드 리더 슬롯입니다.
- [TKSmartCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard): 스마트 카드를 나타내는 표현입니다.
:::

:::topic-grid
## 스마트 카드 App Extension
- [Authenticating Users with a Cryptographic Token](https://developer.apple.com/documentation/cryptotokenkit/authenticating-users-with-a-cryptographic-token): 스마트 카드 app extension을 생성해 사용자 계정과 keychain에 대한 접근 권한을 부여합니다.
- [Configuring Smart Card Authentication](https://developer.apple.com/documentation/cryptotokenkit/configuring-smart-card-authentication): 관리형 기기에서의 설정을 포함해 스마트 카드 인증 작업의 환경설정을 지정합니다.
- [TKSmartCardTokenDriver](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriver): 스마트 카드 app extension의 진입점 역할을 하는 드라이버입니다.
- [TKSmartCardToken](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken): 스마트 카드 기반 암호화 토큰을 나타내는 표현입니다.
- [TKSmartCardTokenSession](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokensession): 스마트 카드 토큰을 기반으로 하는 토큰 세션입니다.
:::

:::topic-grid
## 토큰
- [TKTokenWatcher](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher): 시스템에서 사용 가능한 토큰을 추적하는 객체입니다.
- [TKTokenDriver](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver): 토큰 드라이버를 빌드하기 위한 기본 클래스입니다.
- [TKToken](https://developer.apple.com/documentation/cryptotokenkit/tktoken): 하드웨어 기반 암호화 토큰을 나타내는 표현입니다.
- [TKTokenSession](https://developer.apple.com/documentation/cryptotokenkit/tktokensession): 토큰의 인증 상태를 관리하는 토큰 세션입니다.
:::

:::topic-grid
## 오류
- [TKError](https://developer.apple.com/documentation/cryptotokenkit/tkerror): CryptoTokenKit 프레임워크 고유의 오류입니다.
- [TKErrorDomain](https://developer.apple.com/documentation/cryptotokenkit/tkerrordomain): 모든 CryptoTokenKit 프레임워크 오류의 도메인입니다.
- [TKError.Code](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code): CryptoTokenKit의 오류 코드입니다.
:::

:::topic-grid
## 클래스
- [TKSmartCardSlotNFCSession](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotnfcsession): 생성된 NFC 스마트 카드 슬롯과 관련된 NFC 세션입니다.
- [TKSmartCardTokenRegistrationManager](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokenregistrationmanager): 토큰 ID를 사용해 smart card를 등록하고 등록 해제하기 위한 중앙 집중식 관리 시스템을 제공합니다.
:::

:::topic-grid
## 타입 별칭
- [TKTokenObjectID](https://developer.apple.com/documentation/cryptotokenkit/tktokenobjectid-8mo7f)
:::
