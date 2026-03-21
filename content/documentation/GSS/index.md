---
route: /documentation/GSS
source_url: https://developer.apple.com/documentation/GSS
source_locale: en-US
section: docc
content_type: symbol
title: GSS
original_title: GSS
source_hash: 337adf80d3faa35c1ab644f9a46ef75d0c19ab36cbf6a50f4d19c135050f6089
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:44:32+00:00'
last_translated_at: '2026-03-14T00:03:00+09:00'
---

# GSS

안전하고 인증된 네트워크 트랜잭션을 수행합니다.

## 개요

오픈 소스 Generic Security Service Application Programming Interface(GSS-API)는 운영체제가 안전한 데이터 전송 작업을 제공하는 표준화된 인터페이스를 정의합니다. GSS 프레임워크는 해당 인터페이스와 기반 라이브러리의 구현을 제공합니다.

GSS-API를 사용하면 다음을 할 수 있습니다.

- 애플리케이션 간에 데이터를 주고받을 수 있는 보안 컨텍스트를 생성합니다. *context*는 두 애플리케이션 사이의 "신뢰 상태"를 나타냅니다. context를 공유하는 애플리케이션은 서로를 인식하며, context가 유지되는 동안 데이터 전송을 허용합니다.
- 전송할 데이터에 *security services*라고 하는 하나 이상의 보호 유형을 적용합니다. security services에 대한 자세한 내용은 [Security](https://developer.apple.com/documentation/Security)를 참고합니다.
- 데이터 변환, 오류 검사, 사용자 권한 위임, 정보 표시, 신원 비교를 수행합니다.

GSS-API 2의 결정판 설명은 [RFC 2743](https://tools.ietf.org/html/rfc2743)를 참고하고, 관련 C 바인딩에 대한 설명은 [RFC 2744](https://tools.ietf.org/html/rfc2744)를 참고합니다.

:::topic-grid
## 메모리와 컨텍스트
- [Allocating and Releasing Objects](https://developer.apple.com/documentation/gss/allocating-and-releasing-objects): 메모리와 객체 수명을 관리합니다.
- [Function Status](https://developer.apple.com/documentation/gss/function-status): 대부분의 GSS-API 함수가 작업 결과를 나타내기 위해 사용하는 반환 값을 평가합니다.
- [Buffer Management](https://developer.apple.com/documentation/gss/buffer-management): 다양한 데이터를 담는 구조체로 버퍼를 할당하고 해제합니다.
- [Context Services](https://developer.apple.com/documentation/gss/context-services): endpoint 사이의 안전한 작업을 관리하기 위해 context service를 사용합니다.
:::

:::topic-grid
## 자격 증명
- [Credential Management](https://developer.apple.com/documentation/gss/credential-management): endpoint 간 연결을 안전하게 설정합니다.
- [Security Mechanisms](https://developer.apple.com/documentation/gss/security-mechanisms): 구현에 사용할 보안 메커니즘을 제공합니다.
:::

:::topic-grid
## 이름과 객체 식별자
- [Name Handling](https://developer.apple.com/documentation/gss/name-handling): 사람, 기계, 애플리케이션 같은 GSS-API principal의 이름을 관리합니다.
- [Object Identifiers](https://developer.apple.com/documentation/gss/object-identifiers): 보안 메커니즘, QOP(Quality of Protection 값), 이름 타입을 저장합니다.
:::

:::topic-grid
## 메시지
- [Token Management](https://developer.apple.com/documentation/gss/token-management): token을 사용해 안전한 통신을 설정합니다.
- [Message Protection](https://developer.apple.com/documentation/gss/message-protection): 메시지 무결성을 안전하게 유지하기 위해 암호화 보호를 제공합니다.
- [Kerberos Implementation](https://developer.apple.com/documentation/gss/kerberos-implementation): Kerberos 기반 GSS-API 구현을 사용해 안전한 연결을 설정합니다.
:::
