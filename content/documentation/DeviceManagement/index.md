---
route: /documentation/DeviceManagement
source_url: https://developer.apple.com/documentation/DeviceManagement
source_locale: en-US
section: docc
content_type: symbol
title: Device Management
original_title: Device Management
source_hash: 79ed7e967f72f21975e17d5c38ba24b9b83bf1d6006138af7998ca24e1782802
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:31:22+00:00'
last_translated_at: '2026-03-13T23:34:00+09:00'
---

# Device Management

조직의 기기를 원격으로 관리합니다.

## 개요

모바일 기기 관리(MDM) 솔루션을 배포하면 관리자가 등록된 기기를 안전하게 원격 구성할 수 있습니다. 관리자는 Apple School Manager 또는 Apple Business Manager를 사용해 조직 소유 기기를 등록하고, 사용자는 자신의 기기를 직접 등록할 수 있습니다. 기기가 등록되면 관리자는 소프트웨어와 기기 설정을 업데이트하고, 조직 정책 준수 여부를 모니터링하고, 기기를 원격으로 지우거나 잠그고, 사내에서 개발했거나 Apple School Manager 또는 Apple Business Manager를 통해 구입한 앱과 책을 설치할 수 있습니다.

MDM은 Managed App Distribution과 함께 동작해 매끄러운 다운로드 및 실행 경험을 제공합니다. 자세한 내용은 [ManagedAppDistribution](https://developer.apple.com/documentation/ManagedAppDistribution)을 참고합니다.

:::topic-grid
## 구성 프로파일
- [Configuring Multiple Devices Using Profiles](https://developer.apple.com/documentation/devicemanagement/configuring-multiple-devices-using-profiles): 조직 내 사용자에게 배포할 구성 프로파일을 생성하고 배포합니다.
- [Profile-Specific Payload Keys](https://developer.apple.com/documentation/devicemanagement/profile-specific-payload-keys): 구성 요구 사항에 맞는 적절한 payload를 사용합니다.
:::

:::topic-grid
## MDM 프로토콜
- [Implementing Device Management](https://developer.apple.com/documentation/devicemanagement/implementing-device-management): MDM 서버를 설정하고 관리되는 기기에 명령을 보냅니다.
- [Commands and Queries](https://developer.apple.com/documentation/devicemanagement/commands-and-queries): 기기의 구성과 동작을 관리합니다.
- [Check-in](https://developer.apple.com/documentation/devicemanagement/check-in): 이러한 명령으로 기기를 인증하고 push token을 유지합니다.
- [Account-driven enrollment](https://developer.apple.com/documentation/devicemanagement/account-driven-enrollment): 사용자 신원 중심 워크플로를 사용해 기기를 인증합니다.
- [Migrating managed devices](https://developer.apple.com/documentation/devicemanagement/migrating-managed-devices): 관리되는 기기를 한 기기 관리 서비스에서 다른 서비스로 마이그레이션합니다.
:::

:::topic-grid
## 선언형 관리
- [Leveraging the declarative management data model to scale devices](https://developer.apple.com/documentation/devicemanagement/leveraging-the-declarative-management-data-model-to-scale-devices): 선언형 관리를 사용해 기기가 더 자율적이고 능동적으로 동작하게 합니다.
- [Integrating Declarative Management](https://developer.apple.com/documentation/devicemanagement/integrating-declarative-management): 기기 등록과 등록 해제, 기기 및 사용자 인증 같은 MDM 기능을 관리하기 위해 선언형 관리 프로토콜을 사용합니다.
- [Deploying apps with declarative management](https://developer.apple.com/documentation/devicemanagement/deploying-apps-with-declarative-management): 선언형 앱 구성을 사용해 관리형 앱을 기기에 배포합니다.
- [Declarations](https://developer.apple.com/documentation/devicemanagement/devicemanagement-declarations): 기기 관리에 사용할 수 있는 declaration입니다.
- [Status Reports](https://developer.apple.com/documentation/devicemanagement/status-reports): 기기의 현재 상태에 대한 보고서입니다.
:::

:::topic-grid
## 배포 서비스
- [Device Assignment](https://developer.apple.com/documentation/devicemanagement/device-assignment): 학생과 직원의 기기를 관리합니다.
- [Roster Management](https://developer.apple.com/documentation/devicemanagement/roster-management): 학생과 교사를 위한 학급을 관리합니다.
- [App and Book Management](https://developer.apple.com/documentation/devicemanagement/app-and-book-management): 학생과 직원을 위한 앱과 책을 관리합니다.
:::

:::topic-grid
## 엔드포인트
- [Fetch a apps resource's relationship](https://developer.apple.com/documentation/devicemanagement/fetch-a-apps-resource's-relationship)
- [Fetch a books resource's relationship](https://developer.apple.com/documentation/devicemanagement/fetch-a-books-resource's-relationship)
- [Get Multiple Genres](https://developer.apple.com/documentation/devicemanagement/get-multiple-genres): 식별자를 사용해 카탈로그에서 여러 장르의 메타데이터를 가져옵니다.
- [Get a Genre](https://developer.apple.com/documentation/devicemanagement/get-a-genre): 식별자를 사용해 카탈로그에서 장르 하나의 메타데이터를 가져옵니다.
:::

:::topic-grid
## 딕셔너리
- [ManifestURL](https://developer.apple.com/documentation/devicemanagement/manifesturl): 앱 manifest의 URL입니다.
- [PasswordHash](https://developer.apple.com/documentation/devicemanagement/passwordhash): 계정의 암호 해시를 담는 dictionary입니다.
- [RelationshipResponse](https://developer.apple.com/documentation/devicemanagement/relationshipresponse)
- [ResponseErrorCode](https://developer.apple.com/documentation/devicemanagement/responseerrorcode): 오류 코드입니다.
:::
