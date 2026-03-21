---
route: /documentation/IdentityDocumentServicesUI
source_url: https://developer.apple.com/documentation/IdentityDocumentServicesUI
source_locale: en-US
section: docc
content_type: symbol
title: IdentityDocumentServicesUI
original_title: IdentityDocumentServicesUI
source_hash: 23d5f3459a5a17916d88aa6d49bca6b0ee3893d19ef1e83d98d75830caee1cd1
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:21:28+00:00'
last_translated_at: '2026-03-14T01:05:00+09:00'
---

# IdentityDocumentServicesUI

사용자가 모바일 문서를 제시할 수 있는 인터페이스를 제공합니다.

## 개요

`IdentityDocumentServicesUI` 프레임워크에는 [IdentityDocumentServices](https://developer.apple.com/documentation/IdentityDocumentServices)의 기능을 지원하는 사용자 인터페이스 객체가 포함되어 있습니다. 여기에는 [IdentityDocumentProvider](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentprovider) 앱을 위한 인증 UI를 구현하는 타입이 포함됩니다. 또한 브라우저가 Digital Credentials API를 구현할 수 있게 하는 controller도 포함됩니다.

:::topic-grid
## 신원 문서 제공자 인증 UI 빌드
- [IdentityDocumentProvider](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentprovider): 신원 문서를 제공하는 app extension입니다.
- [IdentityDocumentRequestScene](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentrequestscene): 특정 문서 요청 유형 지원을 나타내는 scene입니다.
- [ISO18013MobileDocumentRequestScene](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrequestscene)
- [ISO18013MobileDocumentRequestContext](https://developer.apple.com/documentation/identitydocumentservicesui/iso18013mobiledocumentrequestcontext): ISO 18013 모바일 문서 요청의 세부 정보를 담는 객체입니다.
- [IdentityDocumentRequestSceneBuilder](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentrequestscenebuilder): 하나 이상의 scene을 하나의 scene으로 결합하는 result builder입니다.
:::

:::topic-grid
## 브라우저에 웹 presentment 흐름 구현
- [Implementing as an identity document provider](https://developer.apple.com/documentation/IdentityDocumentServices/Implenting-as-an-identity-document-provider): 모바일 문서 웹 presentment를 위한 선택지로 앱을 추가합니다.
- [IdentityDocumentWebPresentmentController](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentwebpresentmentcontroller): 웹에서 시작된 신원 문서 요청을 수행하는 controller입니다.
- [IdentityDocumentWebPresentmentControllerDelegate](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentwebpresentmentcontrollerdelegate): 시스템이 웹 presentment controller와 함께 사용하는 delegate를 정의합니다.
- [IdentityDocumentPresentmentControllerPresentationContextProviding](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentpresentmentcontrollerpresentationcontextproviding): controller가 presentation context를 전달받기 위해 사용하는 인터페이스입니다.
- [IdentityDocumentPresentationAnchor](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentpresentationanchor): 시스템이 앱 UI를 표시할 때 사용하는 presentation anchor입니다.
- [IdentityDocumentPresentmentControlling](https://developer.apple.com/documentation/identitydocumentservicesui/identitydocumentpresentmentcontrolling): 이 객체가 시스템이 신원 문서 presentment에 사용하는 controller임을 나타내는 폐쇄형 프로토콜입니다.
:::
