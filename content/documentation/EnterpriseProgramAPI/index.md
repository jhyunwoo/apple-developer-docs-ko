---
route: /documentation/EnterpriseProgramAPI
source_url: https://developer.apple.com/documentation/EnterpriseProgramAPI
source_locale: en-US
section: docc
content_type: symbol
title: Enterprise Program API
original_title: Enterprise Program API
source_hash: ce0c4c159fb4b6febbbdcc1d77ae2fc2510b76501113f9a57a403cc7a4c4f694
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:55:51+00:00'
last_translated_at: '2026-03-13T16:05:00+09:00'
---

# Enterprise Program API

Apple Developer 웹사이트에서 수행하는 작업을 자동화합니다.

## 개요

Enterprise Program API는 [Apple Developer 웹사이트](https://developer.apple.com)에서 수행하는 동작을 자동화할 수 있게 해 주는 REST API입니다. 사양 파일을 다운로드하려면 [OpenAPI specification](http://developer.apple.com/sample-code/enterprise/enterprise-program-openapi-oas.zip)을 클릭하십시오.

API 호출에는 인증을 위한 JSON Web Token(JWT)이 필요하며, 토큰을 생성하는 데 사용하는 키는 조직의 Enterprise Program 계정에서 얻습니다. 키와 토큰을 생성하려면 [Creating API Keys for Enterprise Program API](https://developer.apple.com/documentation/enterpriseprogramapi/creating-api-keys-for-enterprise-program-api)를 참고하십시오.

:::important Important
Enterprise Program API를 사용해 수행한 변경 사항은 개발 및 배포에 사용하는 실제 운영 데이터에 영향을 줍니다.
:::

이 API는 [Apple Developer 웹사이트](https://developer.apple.com)의 다음 영역을 자동화할 수 있는 리소스를 제공합니다.

- **Provisioning**. 번들 ID, capability, 서명 인증서, 기기, provisioning profile을 관리합니다.
- **Users and Roles**. 사용자를 팀에 초대하고, 접근 수준을 조정하거나 사용자를 제거합니다.

Enterprise Program API는 일관된 JSON 데이터와 추가 관련 리소스로 연결되는 링크를 포함한 응답을 반환합니다.

:::topic-grid
## 핵심 사항
- [Creating API Keys for Enterprise Program API](https://developer.apple.com/documentation/enterpriseprogramapi/creating-api-keys-for-enterprise-program-api): JSON Web Token(JWT)에 서명하고 API 요청을 인증하는 API 키를 생성합니다.
- [Generating Tokens for API Requests](https://developer.apple.com/documentation/enterpriseprogramapi/generating-tokens-for-api-requests): 개인 키로 서명한 JSON Web Token(JWT)을 생성해 API 요청을 인증합니다.
- [Revoking API Keys](https://developer.apple.com/documentation/enterpriseprogramapi/revoking-api-keys): 사용하지 않거나 분실했거나 손상된 개인 키를 폐기합니다.
- [Identifying Rate Limits](https://developer.apple.com/documentation/enterpriseprogramapi/identifying-rate-limits): REST API 응답이 제공하는 rate limit을 인식하고 코드에서 처리합니다.
- [Enterprise Program API Release Notes](https://developer.apple.com/documentation/enterpriseprogramapi/enterprise-api-release-notes): Enterprise Program API의 새로운 기능과 업데이트를 확인합니다.
:::

:::topic-grid
## Provisioning
- [Bundle IDs](https://developer.apple.com/documentation/enterpriseprogramapi/bundle-ids): 앱을 고유하게 식별하는 번들 ID를 관리합니다.
- [Bundle ID Capabilities](https://developer.apple.com/documentation/enterpriseprogramapi/bundle-id-capabilities): 번들 ID의 앱 capability를 관리합니다.
- [Certificates](https://developer.apple.com/documentation/enterpriseprogramapi/certificates): 앱 개발 및 배포를 위한 서명 인증서를 생성, 다운로드, 폐기합니다.
- [Devices](https://developer.apple.com/documentation/enterpriseprogramapi/devices): 개발과 테스트를 위해 기기를 등록합니다.
- [Pass Type Ids](https://developer.apple.com/documentation/enterpriseprogramapi/passtypeids): 앱 개발 및 배포를 위한 pass type id를 생성, 다운로드, 폐기합니다.
- [Profiles](https://developer.apple.com/documentation/enterpriseprogramapi/profiles): 개발 및 배포를 위한 provisioning profile을 생성, 삭제, 다운로드합니다.
:::

:::topic-grid
## 사용자와 역할
- [Users](https://developer.apple.com/documentation/enterpriseprogramapi/users): Enterprise Program 팀의 사용자를 관리합니다.
- [User Invitations](https://developer.apple.com/documentation/enterpriseprogramapi/user-invitations): Enterprise Program 팀에 참여하도록 초대 이메일을 보냅니다.
:::

:::topic-grid
## 오류 처리
- [Interpreting and Handling Errors](https://developer.apple.com/documentation/enterpriseprogramapi/interpreting-and-handling-errors): Enterprise Program API가 오류를 반환하는 방식을 이해하고 코드에서 이를 처리합니다.
- [ErrorResponse](https://developer.apple.com/documentation/enterpriseprogramapi/errorresponse): API 요청이 성공하지 않았을 때 API가 응답 본문에 반환하는 오류 상세 정보입니다.
:::

:::topic-grid
## 페이징
- [Large Data Sets](https://developer.apple.com/documentation/enterpriseprogramapi/large-data-sets): 페이징 정보를 사용해 대규모 데이터 집합을 가져옵니다.
:::

:::topic-grid
## 딕셔너리
- [JsonPointer](https://developer.apple.com/documentation/enterpriseprogramapi/jsonpointer): 오류 위치를 가리키는 JSON pointer를 포함하는 객체입니다.
- [Parameter](https://developer.apple.com/documentation/enterpriseprogramapi/parameter): 오류를 유발한 query parameter를 포함하는 객체입니다.
- [RelationshipLinks](https://developer.apple.com/documentation/enterpriseprogramapi/relationshiplinks): 관련 데이터 링크와 관계의 self-link를 포함합니다.
:::

:::asset-list
- `http://developer.apple.com/sample-code/enterprise/enterprise-program-openapi-oas.zip` -> `http://developer.apple.com/sample-code/enterprise/enterprise-program-openapi-oas.zip` (pending)
:::
