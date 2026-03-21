---
route: /documentation/AppStoreConnectAPI
source_url: https://developer.apple.com/documentation/AppStoreConnectAPI
source_locale: en-US
section: docc
content_type: symbol
title: App Store Connect API
original_title: App Store Connect API
source_hash: 5f468aa656333144d618918e3088787bd09e1737d01c75e02ce618a5e00cd81b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:27:46+00:00'
last_translated_at: '2026-03-13T23:24:00+09:00'
---

# App Store Connect API

Apple Developer 웹사이트와 App Store Connect에서 수행하는 작업을 자동화합니다.

## 개요

App Store Connect API는 App Store Connect에서 수행하는 작업을 자동화할 수 있게 하는 REST API입니다. 명세 파일을 다운로드하려면 [OpenAPI specification](https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip)을 클릭합니다.

API 호출에는 인증을 위해 JSON Web Token(JWT)이 필요합니다. 토큰 생성에 필요한 키는 조직의 App Store Connect 계정에서 얻습니다. 키와 토큰을 생성하려면 [Creating API Keys for App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api)를 참고합니다.

:::important Important
App Store Connect API를 사용해 변경한 내용은 개발 및 배포에 사용하는 프로덕션 데이터에 영향을 줍니다.
:::

이 API는 App Store Connect의 다음 영역을 자동화하기 위한 리소스를 제공합니다.

- **In-App Purchases and Subscriptions.** 앱의 앱 내 구입과 자동 갱신 구독을 관리합니다.
- **TestFlight.** 앱의 베타 빌드, 테스터, 그룹을 관리합니다.
- **Xcode Cloud.** Xcode Cloud 데이터를 읽고, 워크플로를 관리하며, 빌드를 시작합니다.
- **Users and Access.** 사용자를 팀에 초대하고, 접근 수준을 조정하거나, 사용자를 제거합니다.
- **Provisioning.** bundle ID, capability, 서명 인증서, 기기, provisioning profile을 관리합니다.
- **App Metadata.** 새 버전을 만들고, App Store 정보를 관리하며, 앱을 App Store에 제출합니다.
- **App Clip Experiences.** App Clip을 생성하고 App Clip 경험을 관리합니다.
- **Reporting.** 판매 및 재무 보고서를 다운로드합니다.
- **Power and Performance Metrics.** 앱의 App Store 버전에 대한 집계 메트릭과 진단 정보를 다운로드합니다.
- **Customer Reviews and Review Responses.** 앱에 대한 고객 리뷰를 가져오고 고객 리뷰에 대한 응답을 관리합니다.

App Store Connect API는 일관된 JSON 데이터로 구성된 리소스 응답을 반환하며, 관련된 추가 리소스에 대한 링크도 함께 포함합니다. 이러한 관계를 사용해 관련 리소스로 이동할 수 있습니다. 예를 들어 TestFlight의 특정 베타 그룹에 속한 베타 테스터를 찾을 수 있습니다. 특정 리소스에 대한 요청에 필터링을 적용해 응답을 더 정교하게 만들 수 있습니다.

:::topic-grid
## 핵심 항목
- [Creating API Keys for App Store Connect API](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api): JSON Web Token(JWT)에 서명하고 API 요청을 인증하기 위한 API 키를 생성합니다.
- [Generating Tokens for API Requests](https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests): 개인 키로 서명한 JSON Web Token(JWT)을 생성해 API 요청을 인증합니다.
- [Revoking API Keys](https://developer.apple.com/documentation/appstoreconnectapi/revoking-api-keys): 사용하지 않거나 분실했거나 손상된 개인 키를 폐기합니다.
- [Identifying Rate Limits](https://developer.apple.com/documentation/appstoreconnectapi/identifying-rate-limits): REST API 응답이 제공하는 rate limit를 식별하고 코드에서 이를 처리합니다.
- [Uploading Assets to App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi/uploading-assets-to-app-store-connect): 스크린샷, 앱 미리보기, App Review용 첨부 파일, 경로 안내 앱 커버리지 파일을 App Store Connect에 업로드합니다.
- [App Store Connect API Release Notes](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-release-notes): App Store Connect API의 새 기능과 업데이트를 알아봅니다.
:::

:::topic-grid
## App Store
- [App Store](https://developer.apple.com/documentation/appstoreconnectapi/app-store): App Store에서 앱, App Clip, 앱 내 구입, 고객 리뷰의 모든 측면을 관리합니다.
:::

:::topic-grid
## TestFlight
- [Prerelease Versions and Beta Testers](https://developer.apple.com/documentation/appstoreconnectapi/prerelease-versions-and-beta-testers): 베타 테스터와 그룹, 앱, App Clip, 빌드를 포함한 베타 테스트 프로그램을 관리합니다.
:::

:::topic-grid
## Game Center
- [Game Center](https://developer.apple.com/documentation/appstoreconnectapi/game-center): 앱의 Game Center 데이터와 구성을 관리합니다.
:::

:::topic-grid
## Provisioning
- [Bundle IDs](https://developer.apple.com/documentation/appstoreconnectapi/bundle-ids): 앱을 고유하게 식별하는 bundle ID를 관리합니다.
- [Bundle ID Capabilities](https://developer.apple.com/documentation/appstoreconnectapi/bundle-id-capabilities): bundle ID의 앱 capability를 관리합니다.
- [Certificates](https://developer.apple.com/documentation/appstoreconnectapi/certificates): 앱 개발 및 배포용 서명 인증서를 생성, 다운로드, 폐기합니다.
- [Devices](https://developer.apple.com/documentation/appstoreconnectapi/devices): 개발 및 테스트용 기기를 등록합니다.
- [Profiles](https://developer.apple.com/documentation/appstoreconnectapi/profiles): 개발 및 배포를 위한 앱 설치를 가능하게 하는 provisioning profile을 생성, 삭제, 다운로드합니다.
- [Merchant ID](https://developer.apple.com/documentation/appstoreconnectapi/merchantids): Apple Pay용 merchant ID를 관리합니다.
- [Pass type Ids](https://developer.apple.com/documentation/appstoreconnectapi/pass-type-id): 앱 개발 및 배포용 pass type id를 생성, 다운로드, 폐기합니다.
:::

:::topic-grid
## Xcode Cloud
- [Xcode Cloud Workflows and Builds](https://developer.apple.com/documentation/appstoreconnectapi/xcode-cloud-workflows-and-builds): Xcode Cloud 데이터 읽기, 워크플로 관리, 빌드 시작을 자동화합니다.
:::

:::topic-grid
## Webhooks
- [Webhook notifications](https://developer.apple.com/documentation/appstoreconnectapi/webhook-notifications): App Store에서 제공하는 앱 및 상태 알림을 관리합니다.
:::

:::topic-grid
## Reporting
- [Sales and Finance](https://developer.apple.com/documentation/appstoreconnectapi/sales-and-finance): 판매 및 재무 보고서를 다운로드합니다.
- [Power and Performance Metrics and Logs](https://developer.apple.com/documentation/appstoreconnectapi/power-and-performance-metrics-and-logs): 전력 및 성능 메트릭, 로그, 서명을 가져옵니다.
- [Analytics](https://developer.apple.com/documentation/appstoreconnectapi/analytics): 앱과 사용 현황에 대한 데이터를 가져옵니다.
:::

:::topic-grid
## Users and Access
- [Users](https://developer.apple.com/documentation/appstoreconnectapi/users): App Store Connect 팀의 사용자를 관리합니다.
- [User Invitations](https://developer.apple.com/documentation/appstoreconnectapi/user-invitations): App Store Connect 팀에 참여하도록 이메일 초대를 보냅니다.
- [Sandbox Testers](https://developer.apple.com/documentation/appstoreconnectapi/sandbox-testers): App Store Connect 팀의 샌드박스 테스터를 관리합니다.
:::

:::topic-grid
## Error Handling
- [Interpreting and Handling Errors](https://developer.apple.com/documentation/appstoreconnectapi/interpreting-and-handling-errors): App Store Connect API가 오류를 반환하는 방식을 이해하고 코드에서 처리합니다.
:::

:::topic-grid
## Paging
- [Large Data Sets](https://developer.apple.com/documentation/appstoreconnectapi/large-data-sets): 페이징 정보를 사용해 대용량 데이터 집합을 가져옵니다.
:::

:::topic-grid
## Alternative App Distribution
- [Alternative Marketplaces and Web Distribution](https://developer.apple.com/documentation/appstoreconnectapi/alternative-marketplaces-and-web-distribution): 대체 앱 배포를 위한 키와 패키지를 관리하고 검색합니다.
:::

:::asset-list
- `https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip` -> `https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip` (pending)
:::
