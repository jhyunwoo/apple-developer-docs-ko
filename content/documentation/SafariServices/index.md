---
route: /documentation/SafariServices
source_url: https://developer.apple.com/documentation/SafariServices
source_locale: en-US
section: docc
content_type: symbol
title: Safari Services
original_title: Safari Services
source_hash: f05fb17e23c996ef8bd2acc97812b86d61e09d15239d5b6b6b4b0df01a2237a1
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:20+00:00'
last_translated_at: '2026-03-13T10:02:00+00:00'
---

# Safari Services

앱에서 웹 뷰와 서비스를 활성화합니다.

## 개요

Safari Services 프레임워크를 사용하면 iOS 또는 macOS 앱에 Safari 동작을 통합하거나, Safari의 동작을 확장할 수 있습니다.

다음과 같은 작업을 할 수 있습니다.

- Safari 앱이 제공하는 사용자 인터페이스와 거의 동일한 사용자 인터페이스를 제공합니다. 사용자는 이 뷰에서 웹을 탐색한 뒤 앱의 콘텐츠로 돌아갈 수 있습니다. 이 뷰는 자체적인 사용자 정의 브라우징 솔루션을 구현하는 것보다 Safari 사용자 인터페이스와 더 일관되며, 더 적은 코드로 구현할 수 있습니다. (iOS)
- 사용자의 Safari Reading List에 항목을 추가합니다. (iOS)
- 기존 Chrome, Firefox, Edge 확장을 Safari web extension으로 변환하거나, 다른 브라우저에서도 동작할 수 있는 새로운 Safari web extension을 만듭니다. (iOS 및 macOS)
- 앱에서 content blocker extension이 로드되었는지 확인하고, 로드된 경우 내용 새로 고침을 요청합니다. (iOS 및 macOS)
- Safari app extension을 구현합니다. 앱에서 Safari app extension이 로드되었는지 확인합니다. (macOS)
- [ASWebAuthenticationSession](https://developer.apple.com/documentation/AuthenticationServices/ASWebAuthenticationSession)을 사용해 앱과 Safari가 쿠키 및 웹사이트 데이터를 공유하도록 하여 싱글 사인온(SSO) 경험을 제공합니다.

:::topic-grid
## Safari web extensions
- [Safari web extensions](https://developer.apple.com/documentation/safariservices/safari-web-extensions): Safari와 다른 브라우저에서 동작하는 web extension을 생성합니다.
:::

:::topic-grid
## Content blockers
- [content blocker 생성하기](https://developer.apple.com/documentation/safariservices/creating-a-content-blocker): Xcode에서 Safari용 content blocker를 생성합니다.
- [SFContentBlockerManager](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager): 앱이 content blocker extension과 상호 작용할 때 사용하는 클래스입니다.
- [SFContentBlockerState](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate): content blocker extension의 상태입니다.
:::

:::topic-grid
## Safari app extensions
- [Safari app extensions](https://developer.apple.com/documentation/safariservices/safari-app-extensions): Safari app extension이 웹 기술과 네이티브 코드를 활용해 Safari의 웹 브라우징 경험을 어떻게 확장하는지 알아봅니다.
- [SFSafariExtension](https://developer.apple.com/documentation/safariservices/sfsafariextension): Safari extension의 프록시입니다.
- [SFSafariApplication](https://developer.apple.com/documentation/safariservices/sfsafariapplication): Safari 앱의 프록시입니다.
- [SFSafariWindow](https://developer.apple.com/documentation/safariservices/sfsafariwindow): Safari window의 프록시입니다.
- [SFSafariPage](https://developer.apple.com/documentation/safariservices/sfsafaripage): Safari 웹페이지의 프록시입니다.
- [SFSafariTab](https://developer.apple.com/documentation/safariservices/sfsafaritab): Safari window 안의 탭 프록시입니다.
:::

:::topic-grid
## Safari 설정
- [SFSafariSettings](https://developer.apple.com/documentation/safariservices/sfsafarisettings): 앱에서 Safari 설정을 열 때 사용하는 클래스입니다.
:::

:::topic-grid
## 앱 안의 Safari 콘텐츠
- [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller): 웹 탐색을 위한 표시 가능한 표준 인터페이스를 제공하는 객체입니다.
- [SFAuthenticationSession.CompletionHandler](https://developer.apple.com/documentation/safariservices/sfauthenticationsession/completionhandler): 사용자가 로그인을 취소하거나 완료했을 때 인증 세션의 completion handler입니다.
- [Safari에서 내보낸 데이터 가져오기](https://developer.apple.com/documentation/safariservices/importing-data-exported-from-safari): 북마크, 저장된 비밀번호, 기타 정보를 브라우저 간에 이전합니다.
:::

:::topic-grid
## 연관 도메인
- [연관 도메인 지원하기](https://developer.apple.com/documentation/Xcode/supporting-associated-domains): 앱과 웹사이트를 연결해 네이티브 앱 경험과 브라우저 경험을 모두 제공합니다.
- [SFUniversalLink](https://developer.apple.com/documentation/safariservices/sfuniversallink): 브라우저가 앱과 웹사이트 사이의 연관 관계를 발견할 수 있게 하는 객체입니다.
- [Associated Domains Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.associated-domains): 공유 웹 자격 증명, universal link, App Clip 같은 특정 서비스용 연관 도메인입니다.
:::

:::topic-grid
## 사용 가능 여부
- [SFSafariServicesAvailable(_:)](https://developer.apple.com/documentation/safariservices/sfsafariservicesavailable(_:)): 주어진 버전의 Safari services를 사용할 수 있는지 나타냅니다.
- [SFSafariServicesVersion](https://developer.apple.com/documentation/safariservices/sfsafariservicesversion): Safari services의 버전입니다.
:::

:::topic-grid
## Safari Reading List
- [SSReadingList](https://developer.apple.com/documentation/safariservices/ssreadinglist): 사용자의 Safari Reading List에 항목을 추가하는 객체입니다.
- [SSReadingListErrorDomain](https://developer.apple.com/documentation/safariservices/ssreadinglisterrordomain): Safari Reading List 오류의 도메인입니다.
- [SSReadingListError.Code](https://developer.apple.com/documentation/safariservices/ssreadinglisterror/code): Safari Reading List 오류를 설명하는 메시지입니다.
- [SSReadingListError](https://developer.apple.com/documentation/safariservices/ssreadinglisterror): Safari Reading List 오류입니다.
:::

:::topic-grid
## 홈 화면 북마크
- [SFAddToHomeScreenActivityItem](https://developer.apple.com/documentation/safariservices/sfaddtohomescreenactivityitem): 사용자가 홈 화면에 추가할 수 있는 북마크를 설명하는 프로토콜입니다.
:::

:::topic-grid
## 기타 오류
- [SFError](https://developer.apple.com/documentation/safariservices/sferror): content blocker 또는 Safari app extension 오류입니다.
- [SFError.Code](https://developer.apple.com/documentation/safariservices/sferror/code): content blocker 또는 Safari app extension 오류를 설명하는 메시지입니다.
- [SFErrorDomain](https://developer.apple.com/documentation/safariservices/sferrordomain): content blocker 또는 Safari app extension 오류의 도메인입니다.
:::

:::topic-grid
## Deprecated
- [Deprecated symbols](https://developer.apple.com/documentation/safariservices/deprecated-symbols): 지원되지 않는 심볼과 그 대체 항목을 검토합니다.
:::
