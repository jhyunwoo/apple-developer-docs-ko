---
route: /documentation/SafariServices/safari-app-extensions
source_url: https://developer.apple.com/documentation/SafariServices/safari-app-extensions
source_locale: en-US
section: docc
content_type: article
title: Safari app extensions
original_title: Safari app extensions
source_hash: 81b0c5fe1e16cb1766749dcc402e2d0ea4f097710ec80de918a1f4b02cac5efd
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:14:53+00:00'
last_translated_at: '2026-03-13T16:45:00+09:00'
---

# Safari app extensions

웹 기술과 네이티브 코드를 활용해 Safari의 웹 브라우징 경험을 확장하는 Safari app extension을 알아봅니다.

## 개요

Safari app extension은 웹 페이지 콘텐츠를 읽고 수정하여 Safari에 새로운 기능을 추가할 수 있습니다. 이러한 기능은 사용하는 도구, 수행할 수 있는 작업, 브라우저에서 접근할 수 있는 데이터를 확장합니다. Safari app extension이 특히 유용한 이유는 네이티브 앱과 통신할 수 있기 때문입니다. 앱과 Safari 사이에서 데이터를 공유하면 앱 콘텐츠를 Safari에 통합하거나 웹 데이터를 다시 앱으로 보낼 수 있어, 앱의 웹 버전과 네이티브 버전 사이에 통합된 경험을 제공할 수 있습니다.

![Safari app extension이 포함 앱과 Safari 브라우저 사이에서 통신하는 모습을 보여 주는 다이어그램입니다. Safari app extension이라는 상자가 Containing app 상자 안에 들어 있으며, app extension과 containing app이 공유 리소스를 통해 정보를 주고받는 화살표와 app extension과 Safari가 정보를 주고받는 화살표가 표시됩니다.](https://developer.apple.com)

:::note Note
이전에는 Safari extension이 앱과 Safari 사이의 통신을 제공했습니다. 레거시 Safari extension을 마이그레이션하려면 [Converting a legacy Safari extension to a Safari app extension](https://developer.apple.com/documentation/safariservices/converting-a-legacy-safari-extension-to-a-safari-app-extension)을 참고하십시오.
:::

Safari app extension은 JavaScript, CSS, Objective-C 또는 Swift로 작성한 네이티브 코드를 조합해 사용합니다. Safari app extension을 표준 app extension 모델 위에 빌드하기 때문에 많은 네이티브 앱의 이점을 얻을 수 있습니다.

- Safari app extension을 앱 안에 번들로 포함해 App Store를 통해 배포합니다. Mac 앱이나 [Mac Catalyst](https://developer.apple.com/documentation/UIKit/mac-catalyst) 앱과 함께 Safari app extension을 배포할 수 있습니다.
- 앱과 Safari app extension을 함께 배포하므로 버전이 서로 맞지 않는 상태로 설치될 가능성을 줄일 수 있습니다.
- Safari app extension은 공유 리소스를 사용해 앱과 안전하게 통신할 수 있습니다.

app extension 개념에 익숙해지려면 [App Extensions](https://developer.apple.com/app-extensions/)를 참고하십시오. Chrome, Firefox, Edge용으로 만든 extension을 Safari에 배포하거나 Safari와 다른 브라우저 모두에서 동작하는 extension을 만들고 싶다면 [Safari web extensions](https://developer.apple.com/documentation/safariservices/safari-web-extensions)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [Building a Safari app extension](https://developer.apple.com/documentation/safariservices/building-a-safari-app-extension): Safari app extension을 추가하고 빌드하고 활성화합니다.
- [Converting a legacy Safari extension to a Safari app extension](https://developer.apple.com/documentation/safariservices/converting-a-legacy-safari-extension-to-a-safari-app-extension): 키를 사용해 자동으로 또는 수동으로 레거시 Safari extension을 Safari app extension으로 변환합니다.
- [Troubleshooting your Safari app extension](https://developer.apple.com/documentation/safariservices/troubleshooting-your-safari-app-extension): 이 기법을 사용해 Safari app extension을 디버깅합니다.
:::

:::topic-grid
## 주입된 스타일 시트와 스크립트
- [Using injected style sheets and scripts](https://developer.apple.com/documentation/safariservices/using-injected-style-sheets-and-scripts): 주입된 스타일 시트와 스크립트를 사용해 웹 페이지의 모양이나 동작에 어떤 영향을 줄 수 있는지 알아봅니다.
- [Injecting a script into a webpage](https://developer.apple.com/documentation/safariservices/injecting-a-script-into-a-webpage): Safari app extension용으로 작성한 스크립트를 웹 페이지에 주입합니다.
- [Injecting CSS style sheets into a webpage](https://developer.apple.com/documentation/safariservices/injecting-css-style-sheets-into-a-webpage): 웹 페이지에 CSS 스타일 시트를 주입해 스타일을 추가하거나 덮어씁니다.
- [Passing messages between Safari app extensions and injected scripts](https://developer.apple.com/documentation/safariservices/passing-messages-between-safari-app-extensions-and-injected-scripts): Safari app extension과 주입된 스크립트 사이에서 통신합니다.
- [SFSafariExtensionHandler](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandler): Safari app extension의 이벤트를 처리하기 위해 서브클래싱하는 기본 클래스입니다.
- [SFSafariExtensionManager](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager): 앱이 Safari extension의 현재 상태를 확인할 때 사용하는 클래스입니다.
- [SFSafariExtensionState](https://developer.apple.com/documentation/safariservices/sfsafariextensionstate): Safari extension의 상태입니다.
- [SFSafariPageProperties](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties): 웹 페이지에 대한 정보를 캡처하는 객체입니다.
- [SFSafariExtensionHandling](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling): Safari app extension에서 이벤트 처리를 구현하기 위한 프로토콜입니다.
- [SFExtensionProfileKey](https://developer.apple.com/documentation/safariservices/sfextensionprofilekey): 시스템이 user info dictionary에서 프로필 식별자를 식별하는 키로 사용하는 문자열입니다.
:::

:::topic-grid
## 정보 프로퍼티 리스트 키
- [Safari app extension information property list keys](https://developer.apple.com/documentation/safariservices/safari-app-extension-information-property-list-keys): Safari app extension, UI, 권한에 대한 정보를 운영 체제에 제공하는 정보 프로퍼티 리스트 파일의 키를 지정합니다.
:::
