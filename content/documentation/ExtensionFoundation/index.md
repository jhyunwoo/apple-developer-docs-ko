---
route: /documentation/ExtensionFoundation
source_url: https://developer.apple.com/documentation/ExtensionFoundation
source_locale: en-US
section: docc
content_type: symbol
title: ExtensionFoundation
original_title: ExtensionFoundation
source_hash: 7356ed45140918e0bd4291d502365e80cff0b39bbe3ead446d2c4f65c3f860c7
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:59:25+00:00'
last_translated_at: '2026-03-14T02:52:00+09:00'
---

# ExtensionFoundation

다른 앱의 기능을 확장하기 위한 실행 가능한 bundle을 만듭니다.

## 개요

app extension은 시스템의 기능 또는 다른 앱의 기능을 확장하는 실행 코드 bundle입니다. 시스템 수준에서 app extension은 시스템 기능에 사용자 정의 기능을 추가하는 방법을 제공합니다. 예를 들어 [Creating a widget extension](https://developer.apple.com/documentation/WidgetKit/Creating-a-Widget-Extension)을 사용하면 iOS 홈 화면과 잠금 화면 같은 특정 위치에 앱 콘텐츠를 표시할 수 있습니다. 시스템 기능용 app extension을 빌드할 때는 일반적으로 이 프레임워크 대신 다른 프레임워크 또는 전용 타입 집합을 사용합니다.

자체 앱에 app extension 지원을 추가하려면 `ExtensionFoundation` 프레임워크를 직접 채택하십시오. app extension 모델은 앱 기능을 여러 방식으로 안전하게 확장할 수 있게 합니다. 앱이 위험한 코드를 실행해야 한다면, 그 코드가 앱의 나머지 부분에 영향을 주지 않도록 app extension에 격리할 수 있습니다. 또는 생산성 앱이라면 다른 개발자가 앱의 핵심 기능 집합을 확장하는 app extension을 만들 수 있는 방법을 제공할 수 있습니다.

host app은 `ExtensionFoundation` 프레임워크를 사용해 사용 가능한 app extension을 찾아 실행합니다. app extension은 host app과 통신하고 비 UI 기능을 지원하기 위해 이 프레임워크를 사용합니다. 앱이 app extension의 사용자 정의 UI도 통합한다면, 이 프레임워크와 함께 [ExtensionKit](https://developer.apple.com/documentation/ExtensionKit) 프레임워크도 채택하십시오.

:::topic-grid
## 기초
- [Adding support for app extensions to your app](https://developer.apple.com/documentation/extensionfoundation/adding-support-for-app-extensions-to-your-app): 코드의 extension point를 정의하고 런타임에 app extension과 통신하여 app extension 모델을 만듭니다.
:::

:::topic-grid
## app extension 설정
- [Building an app extension to support a host app](https://developer.apple.com/documentation/extensionfoundation/building-an-app-extension-to-support-a-host-app): host app과 별도 프로세스에서 작업을 수행하는 app extension을 만듭니다.
- [AppExtension](https://developer.apple.com/documentation/extensionfoundation/appextension): app extension의 콘텐츠, 구조, 동작을 선언하는 데 사용하는 인터페이스입니다.
- [AppExtensionConfiguration](https://developer.apple.com/documentation/extensionfoundation/appextensionconfiguration): app extension의 XPC 연결을 구성하는 데 사용하는 인터페이스입니다.
- [ConnectionHandler](https://developer.apple.com/documentation/extensionfoundation/connectionhandler): 들어오는 XPC 연결을 처리하는 사용자 정의 closure를 담는 타입입니다.
:::

:::topic-grid
## host app 구성
- [Discovering app extensions from your app](https://developer.apple.com/documentation/extensionfoundation/discovering-app-extensions-from-your-app): host app의 extension point와 일치하고 사용할 수 있는 app extension을 찾습니다.
- [AppExtensionProcess](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess): host app이 app extension을 실행하고 관리하기 위해 생성하는 타입입니다.
- [AppExtensionIdentity](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity): 시스템에서 app extension을 고유하게 식별하는 타입입니다.
:::

:::topic-grid
## extension point 관리
- [AppExtensionPoint](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint): host app의 extension point를 선언하고 app extension에서 여기에 바인딩하는 데 사용하는 타입입니다.
- [ExtensionPointDefining](https://developer.apple.com/documentation/extensionfoundation/extensionpointdefining): extension point 타입이 채택하는 인터페이스입니다.
:::
