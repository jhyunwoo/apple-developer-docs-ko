---
route: /documentation/IdentityDocumentServices
source_url: https://developer.apple.com/documentation/IdentityDocumentServices
source_locale: en-US
section: docc
content_type: symbol
title: IdentityDocumentServices
original_title: IdentityDocumentServices
source_hash: 709f69554a98cd430a8f2e3316bea0dc84bf081552372622e05ef130d6bafdff
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:32+00:00'
last_translated_at: '2026-03-13T17:10:00+09:00'
---

# IdentityDocumentServices

Digital Credentials API를 사용해 모바일 문서를 공유합니다.

## 개요

Identity Document Services는 기기에서 신원 문서를 제시하는 기능과 Digital Credentials API에 대한 웹 브라우저 지원을 제공합니다.

![작은 신원 문서와 직사각형 웹 페이지를 보여 주는 개념 이미지입니다.](https://developer.apple.com)

권한이 부여되면 사용자는 identity document 요청 중에 앱을 선택할 수 있고, 그 과정에서 [IdentityDocumentServicesUI](https://developer.apple.com/documentation/IdentityDocumentServicesUI)로 만든 UI를 사용해 신원 제시를 승인할 수 있습니다.

이 프레임워크는 웹 브라우저가 Digital Credentials API의 제시 흐름을 구현할 수 있게도 해 줍니다. 웹 브라우저 지원을 통해 사용자는 자신의 기기에서 로컬로 또는 동일한 iCloud 계정을 사용하는 다른 기기에서 원격으로 신원 문서를 제시할 수 있습니다. 신원 문서에는 운전면허증이나 신분증 같은 문서가 포함될 수 있습니다.

:::topic-grid
## 핵심 사항
- [Requesting a mobile document on the web](https://developer.apple.com/documentation/identitydocumentservices/requesting-a-mobile-document-on-the-web): 기기에 설치된 앱에 대해 모바일 문서 정보 요청을 보냅니다.
- [Implementing as an identity document provider](https://developer.apple.com/documentation/identitydocumentservices/implenting-as-an-identity-document-provider): 앱을 모바일 문서 웹 제시 옵션으로 추가합니다.
- [Verifying a mobile document from a passport](https://developer.apple.com/documentation/identitydocumentservices/verifying-a-mobile-document-from-a-passport): 여권에서 파생된 모바일 문서 정보의 응답을 검증합니다.
:::

:::topic-grid
## identity document provider로 등록
- [IdentityDocumentProviderRegistrationStore](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore): 앱이 제시에 사용할 수 있는 문서를 시스템에 알려 주는 저장소입니다.
- [IdentityDocumentRegistration](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentregistration): identity document 등록을 정의하는 프로토콜입니다.
- [MobileDocumentRegistration](https://developer.apple.com/documentation/identitydocumentservices/mobiledocumentregistration): 모바일 문서를 등록할 때 사용하는 타입입니다.
:::

:::topic-grid
## 브라우저에 웹 제시 흐름 구현
- [IdentityDocumentWebPresentmentRawRequestValidator](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrawrequestvalidator): 들어오는 웹 제시 raw request를 검증하는 함수를 포함하는 타입입니다.
- [IdentityDocumentWebPresentmentRequest](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrequest): 시스템이 identity document 웹 제시를 수행할 때 사용하는 객체임을 나타내는 closed protocol입니다.
- [ISO18013MobileDocumentRequest](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentrequest): 들어오는 ISO 18013-5 모바일 문서 요청을 나타내는 타입입니다.
- [IdentityDocumentWebPresentmentResponse](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentresponse): 시스템이 웹 제시 응답을 나타낼 때 사용하는 객체임을 나타내는 closed protocol입니다.
- [ISO18013MobileDocumentResponse](https://developer.apple.com/documentation/identitydocumentservices/iso18013mobiledocumentresponse): 웹 제시 요청의 문서 응답을 나타내는 타입입니다.
- [IdentityDocumentWebPresentmentRawRequest](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentwebpresentmentrawrequest): raw 웹 제시 요청을 나타내는 타입을 정의하는 구조체입니다.
:::

:::topic-grid
## 구조체
- [IdentityDocumentPresentmentError](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentpresentmenterror): identity document 웹 제시 controller에서 던지는 오류 타입입니다.
:::
