---
route: /documentation/AccountOrganizationalDataSharing
source_url: https://developer.apple.com/documentation/AccountOrganizationalDataSharing
source_locale: en-US
section: docc
content_type: symbol
title: Account & Organizational Data Sharing
original_title: Account & Organizational Data Sharing
source_hash: f1e82de004baae42e0649d6a23e9b8e69fbd5b794eb2bc644849c8e1f6cfb3d2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:16:02+00:00'
last_translated_at: '2026-03-13T22:31:00+09:00'
---

# Account & Organizational Data Sharing

Roster API 같은 Apple REST 서비스에서 사용자 정보를 접근하는 앱과 웹사이트를 사람들이 승인할 수 있도록 합니다.

## 개요

[OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749)을 기반으로 하는 Account & Organizational Data Sharing은 앱과 웹사이트가 Apple 서비스(예: [Roster API](https://developer.apple.com/documentation/RosterAPI))에 있는 사용자 정보에 접근하도록 사용자가 안전하게 승인할 수 있는 방법을 제공합니다.

:::topic-grid
## 토큰 생성
- [Creating a client secret](https://developer.apple.com/documentation/accountorganizationaldatasharing/creating-a-client-secret): 클라이언트 애플리케이션을 식별하기 위한 서명된 토큰을 생성합니다.
- [Fetch Apple's public key for verifying token signature](https://developer.apple.com/documentation/accountorganizationaldatasharing/fetch-apple's-public-key-for-verifying-token-signature): Apple이 토큰에 서명할 때 사용하는 암호학적 신원과 연결된 공개 키를 가져옵니다.
- [Generate and validate tokens](https://developer.apple.com/documentation/accountorganizationaldatasharing/generate-and-validate-tokens): 앱에 전달된 authorization grant code를 검증해 토큰을 얻거나, 기존 refresh token을 검증합니다.
:::

:::topic-grid
## 토큰 사용 및 폐기
- [Request an authorization](https://developer.apple.com/documentation/accountorganizationaldatasharing/request-an-authorization): Account & Organizational Data Sharing 앱과 웹 서비스에 대한 사용자 승인을 요청합니다.
- [Token revocation](https://developer.apple.com/documentation/accountorganizationaldatasharing/revoke-tokens): 사용자가 더 이상 앱과 연관되지 않을 때 토큰과 관련 사용자 승인을 무효화합니다.
:::

:::topic-grid
## 공통 객체
- [JWKSet](https://developer.apple.com/documentation/accountorganizationaldatasharing/jwkset): JSON 웹 키 집합입니다.
- [TokenResponse](https://developer.apple.com/documentation/accountorganizationaldatasharing/tokenresponse): 요청이 성공했을 때 반환되는 응답 토큰 객체입니다.
- [ErrorResponse](https://developer.apple.com/documentation/accountorganizationaldatasharing/errorresponse): 요청이 실패했을 때 반환되는 오류 객체입니다.
:::
