---
route: /documentation/ManagedApp
source_url: https://developer.apple.com/documentation/ManagedApp
source_locale: en-US
section: docc
content_type: symbol
title: ManagedApp
original_title: ManagedApp
source_hash: bfac4c8f24df81fe9664dfbad617dda21893752f41bfb9a5a3f3995296bfbd5f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:21:29+00:00'
last_translated_at: '2026-03-14T01:05:00+09:00'
---

# ManagedApp

관리형 배포를 위해 앱을 사용자화하고, 관리자가 provisioning한 비밀값과 데이터에 대한 안전한 접근을 기반으로 동작하는 구성 가능한 기능을 제공합니다.

## 개요

이 프레임워크는 MDM(mobile device management)을 사용해 여러 기기에 앱을 설치하기 위한 관리형 배포를 구성하는 API를 정의합니다. 관리자는 조직 내 사람들을 위해 고유한 구성을 만들어 특정 회사, 학교, 정부 조직에 맞게 앱을 구성하거나, 즉 앱을 *관리*합니다.

이 프레임워크는 [Device Management](https://developer.apple.com/documentation/DeviceManagement)와 함께 동작하여 *secrets*와 *configuration*에 대해 간소화되고 안전한 접근을 제공합니다. Secrets에는 암호, 인증서, 신원이 포함됩니다. Configuration에는 예를 들어 서버 URL과 초 단위 timeout 같은 일반 정보가 포함됩니다.

관리형 secrets와 configuration을 활성화하면 MDM 관리자가 앱의 동작을 사용자화할 수 있습니다. 예를 들어 MDM 관리자는 앱이 최초 설정을 건너뛰고 바로 사용할 수 있도록, 이미 사용자가 로그인된 상태이며 앱 환경설정이나 직무별 정보가 미리 채워진 상태로 실행되도록 구성할 수 있습니다.

![두 개의 iPhone 렌더링이 나란히 배치된 그림입니다. 왼쪽 기기에는 Unmanaged App, 오른쪽 기기에는 Managed app이라는 레이블이 있습니다. 관리되지 않은 앱은 Company Name 헤더 아래에 username과 password라는 빈 텍스트 필드 두 개가 있는 로그인 프롬프트를 표시하고, Login required라는 callout이 연결됩니다. 관리형 앱은 Company Name 헤더와 탭 레이아웃을 표시하며, 첫 번째 탭은 Dashboard로 선택되어 있고 두 번째 탭은 Sales입니다. Sales 탭에는 Access-control roles automatically setup이라는 callout이 연결됩니다. 탭 안에는 Juan Chavez라는 이름 옆에 아바타가 있는 프로필 영역이 있고 Automatically logged in이라는 callout이 연결됩니다. 설정 영역에는 여러 슬라이더가 있으며 일부는 켜져 있고 일부는 꺼져 있습니다. 여기에 Preconfigured라는 callout이 연결됩니다. 마지막으로 To Do라는 제목의 영역에는 텍스트를 나타내는 회색 사각형들이 있고, Info loaded immediately라는 callout이 연결됩니다.](https://developer.apple.com)

## 비밀값을 사용해 관리형 기능 구현

ManagedApp에서 사용할 수 있는 서버 provisioning secrets와 configuration을 사용하면 다음과 같은 일반적인 Device Management 기능을 앱에 추가할 수 있습니다.

- 사용자의 역할 강제
- 관리자 provisioning한 신원을 받아 인증과 서명에 사용
- API 액세스 토큰 수신
- 예를 들어 인증서 pinning 같은 사용자 정의 신뢰를 위한 인증서 획득
- 강력한 장치 인증을 위한 하드웨어 바운드 키와 Managed Device Attestation 사용

## 앱 또는 app extension provisioning

ManagedApp은 앱과 app extension 모두에서 동작합니다. 문서가 앱에서의 프레임워크 사용을 설명하는 경우, app extension에도 동일하게 적용됩니다.

MDM 관리자는 용도에 따라 앱과 각 app extension을 서로 다르게 provisioning할 수 있습니다. 예를 들어 MDM 관리자는 앱에서 접근할 수 없는 VPN 인증 신원을 사용해 앱의 [Packet tunnel provider](https://developer.apple.com/documentation/NetworkExtension/packet-tunnel-provider) extension을 provisioning할 수 있으며, 이는 보안을 강화합니다.

앱과 app extension 각각의 고유한 provisioning 요구 사항은 개발자가 설계하고 MDM 관리자에게 전달해야 하며, 관리자는 이에 맞춰 준비할 수 있습니다.

:::topic-grid
## 구성
- [Specifying and decoding a configuration](https://developer.apple.com/documentation/managedapp/specifying-and-decoding-a-configuration): 구성 사양을 공개하고, MDM 관리자가 제공한 구성을 파싱하고 검증하는 decoder를 구현합니다.
- [ManagedAppConfigurationProvider](https://developer.apple.com/documentation/managedapp/managedappconfigurationprovider): 관리형 앱 또는 extension에 대해 MDM 관리자가 provisioning한 구성을 제공하는 클래스입니다.
:::

:::topic-grid
## 비밀값 및 식별자
- [Accessing provisioned secrets with identifiers](https://developer.apple.com/documentation/managedapp/accessing-provisioned-secrets-with-identifiers): 장치 관리 기능에 필요한 비밀값을 지정하고, MDM 서버로부터 비밀값을 받아 앱에서 사용합니다.
- [ManagedAppCertificatesProvider](https://developer.apple.com/documentation/managedapp/managedappcertificatesprovider): 관리형 앱 또는 extension에 대해 MDM 관리자가 provisioning한 인증서를 제공하는 클래스입니다.
- [ManagedAppIdentitiesProvider](https://developer.apple.com/documentation/managedapp/managedappidentitiesprovider): 관리형 앱 또는 extension에 대해 MDM 관리자가 provisioning한 신원을 제공하는 클래스입니다.
- [ManagedAppPasswordsProvider](https://developer.apple.com/documentation/managedapp/managedapppasswordsprovider): 관리형 앱 또는 extension에 대해 MDM 관리자가 provisioning한 암호를 제공하는 클래스입니다.
:::

:::topic-grid
## 오류
- [ManagedAppError](https://developer.apple.com/documentation/managedapp/managedapperror): ManagedApp 프레임워크의 함수가 throw할 수 있는 오류입니다.
- [ManagedAppConfigurationDecodingError](https://developer.apple.com/documentation/managedapp/managedappconfigurationdecodingerror): 구성 디코딩 문제를 설명하는 오류용 프로토콜입니다.
- [ManagedAppConfigurationDecodingErrorCode](https://developer.apple.com/documentation/managedapp/managedappconfigurationdecodingerrorcode): 구성 디코딩 중 발생하는 오류 코드입니다.
:::
