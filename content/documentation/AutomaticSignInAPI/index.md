---
route: /documentation/AutomaticSignInAPI
source_url: https://developer.apple.com/documentation/AutomaticSignInAPI
source_locale: en-US
section: docc
content_type: symbol
title: Automatic Sign-In API
original_title: Automatic Sign-In API
source_hash: 1aca07b80bb7cac4e0bc866f6d7106aa9b3b01ed10e0c96d562654c61868e0ff
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:12:36+00:00'
last_translated_at: '2026-03-14T00:45:00+09:00'
---

# Automatic Sign-In API

미디어 스트리밍 서비스 고객의 기기 전반에서 single sign-on을 가능하게 하는 웹 서버의 로그인 토큰을 관리합니다.

## 개요

Automatic Sign-In 기능은 미디어 스트리밍 앱을 위한 single sign-on 경험을 제공합니다. 사용자가 처음으로 앱을 통해 미디어 스트리밍 서비스에 로그인하면 앱은 [Video Subscriber Account](https://developer.apple.com/documentation/videosubscriberaccount) 프레임워크를 호출해 Automatic Sign-In 참여를 제안합니다. 사용자가 동의하면 앱은 문자열 값 토큰, 즉 *sign-in token*을 생성합니다. 이 토큰을 [Video Subscriber Account](https://developer.apple.com/documentation/videosubscriberaccount) 프레임워크에 제공하면, 프레임워크는 이를 사용자의 Apple Account에 저장하여 모든 기기에서 로그인할 수 있게 합니다. 사용자가 다른 기기에서 앱을 실행하면 운영 체제가 해당 Apple Account의 sign-in token을 제공하고, 앱은 이를 사용해 자동으로 로그인시킵니다. Apple 기기의 미디어 스트리밍 앱에 Automatic Sign-In을 구현하는 방법은 [Signing people in to their media accounts automatically](https://developer.apple.com/documentation/videosubscriberaccount/signing-people-in-to-media-apps-automatically)를 참고하십시오.

이 API는 [Video Subscriber Account](https://developer.apple.com/documentation/videosubscriberaccount)와 함께 동작하여 웹 서버에서 sign-in token을 업데이트하거나 삭제합니다. 다음과 같은 조건에서는 웹 서버에서 sign-in token을 업데이트하거나 삭제할 수 있습니다.

- 웹사이트가 사용자가 Automatic Sign-In에서 옵트아웃하거나, 특정 로그인을 승인되지 않은 것으로 표시할 수 있는 UI를 제공하는 경우
- 사용자가 암호를 변경하고 모든 기기에서 로그아웃하기를 원하는 경우

### 요청 인증

웹 서비스는 어떤 토큰에 대해 작업해야 하는지와 요청의 진위를 알아야 하며, 이를 위해 요청 헤더에 bearer token을 추가합니다. 자세한 내용은 [Authorizing API calls using bearer tokens](https://developer.apple.com/documentation/videosubscriberaccount/authorizing-api-calls-using-bearer-tokens)를 참고하십시오.

### 샌드박스 환경에서 테스트

개발 중 웹 서버에서 API를 테스트하려면 endpoint 요청을 샌드박스 환경으로 보내 테스트 데이터에 대해 작업할 수 있습니다. 웹 서버에서 샌드박스 기본 URL `https://api.storekit-sandbox.itunes.apple.com/`을 사용해 테스트 호출을 보내십시오. 예를 들어 샌드박스 환경에서 [Update Sign-In Token](https://developer.apple.com/documentation/automaticsigninapi/update-this-token-for-all-associated-users)을 호출하려면 다음 URL로 요청을 보냅니다.

```other
https://api.storekit-sandbox.itunes.apple.com/account/v1/autoSignIn/update
```

작업할 테스트 데이터를 생성하려면 다음을 수행합니다.

- 테스트 기기에서 Sandbox Apple Account로 로그인합니다. 자세한 내용은 [Create a Sandbox Apple Account](https://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-a-sandbox-apple-account)를 참고하십시오.
- 테스트 기기에서 development 또는 Ad Hoc 빌드를 실행합니다. 앱이 운영 체제에 제공하는 모든 sign-in token([updateAutoSignInToken(_:updateContext:)](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/updateautosignintoken(_:updatecontext:))를 통해 전달)는 앱의 development 또는 Ad Hoc 배포에서 이 상호 작용이 일어날 때 샌드박스 환경에 테스트 데이터를 생성합니다.

:::topic-grid
## 인증
- [Authorizing API calls using bearer tokens](https://developer.apple.com/documentation/videosubscriberaccount/authorizing-api-calls-using-bearer-tokens): 요청 헤더에 서명된 JWT 토큰을 포함해 endpoint 호출을 인증합니다.
:::

:::topic-grid
## 토큰 업데이트
- [Update Sign-In Token](https://developer.apple.com/documentation/automaticsigninapi/update-this-token-for-all-associated-users): 특정 sign-in token을 새 값으로 업데이트합니다.
- [UpdateAutoSignInTokenRequest](https://developer.apple.com/documentation/automaticsigninapi/updateautosignintokenrequest): 기존 sign-in token과 새 sign-in token을 담는 요청 본문입니다.
:::

:::topic-grid
## 토큰 삭제
- [Delete Sign-In Token](https://developer.apple.com/documentation/automaticsigninapi/delete-this-token-for-all-associated-users): 특정 sign-in token을 삭제합니다.
- [DeleteAutoSignInTokenRequest](https://developer.apple.com/documentation/automaticsigninapi/deleteautosignintokenrequest): 삭제할 sign-in token을 담는 요청 본문입니다.
:::
