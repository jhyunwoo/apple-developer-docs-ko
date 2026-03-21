---
route: /documentation/ExtensionKit
source_url: https://developer.apple.com/documentation/ExtensionKit
source_locale: en-US
section: docc
content_type: symbol
title: ExtensionKit
original_title: ExtensionKit
source_hash: b816a7ba46351ceb27390873609bcd38072ac1ac2d1c59bb402806aa3169ed4e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:26:31+00:00'
last_translated_at: '2026-03-14T00:42:00+09:00'
---

# ExtensionKit

앱 extension의 사용자 정의 UI를 호스트 앱에서 사용할 수 있게 하고, 활성화되거나 비활성화된 앱 extension 목록을 관리합니다.

## 개요

앱 extension은 시스템의 기능이나 다른 앱의 기능을 확장하는 코드 번들입니다. 시스템 수준에서 앱 extension은 시스템 기능에 사용자 정의 기능을 추가하는 방법을 제공합니다. 예를 들어 [Creating a widget extension](https://developer.apple.com/documentation/WidgetKit/Creating-a-Widget-Extension)은 iOS 홈 화면이나 잠금 화면 같은 특정 위치에 앱의 콘텐츠를 표시합니다. 시스템 기능은 일반적으로 관련 앱 extension을 만들기 위한 사용자 정의 워크플로를 제공하지만, 그 기능 지원을 구현할 때는 여전히 이 프레임워크를 사용합니다.

앱이 사용자 정의 앱 extension의 콘텐츠를 포함하도록 지원한다면 이 프레임워크와 [ExtensionFoundation](https://developer.apple.com/documentation/ExtensionFoundation) 프레임워크를 채택해 해당 기능을 지원하십시오. 앱 extension에서는 `ExtensionKit`을 채택하고 표시하려는 뷰를 정의하는 데 사용합니다. 호스트 앱에서는 이 프레임워크를 사용해 앱 extension이 제공하는 인터페이스를 표시합니다. 이 프레임워크는 앱 인터페이스에서 활성화 및 비활성화된 앱 extension을 보여 주는 view controller도 제공합니다.

:::topic-grid
## 핵심 사항
- [Including extension-based UI in your interface](https://developer.apple.com/documentation/extensionkit/including-extension-based-ui-in-your-interface): 사용자 정의 UI를 제공하는 앱 extension을 만들고, 그 뷰를 앱 인터페이스 안에 호스팅합니다.
:::

:::topic-grid
## UI 정의
- [AppExtensionScene](https://developer.apple.com/documentation/extensionkit/appextensionscene): 앱 extension UI에서 특정 scene을 제공할 때 사용하는 인터페이스입니다.
- [PrimitiveAppExtensionScene](https://developer.apple.com/documentation/extensionkit/primitiveappextensionscene): 앱 extension 기반 UI의 콘텐츠를 전달할 때 사용하는 타입입니다.
- [AppExtensionSceneBuilder](https://developer.apple.com/documentation/extensionkit/appextensionscenebuilder): closure에서 extension scene을 구성하는 사용자 정의 parameter attribute입니다.
:::

:::topic-grid
## 앱 extension 구성
- [AppExtensionSceneConfiguration](https://developer.apple.com/documentation/extensionkit/appextensionsceneconfiguration): 사용자 정의 UI를 제공하는 앱 extension을 구성할 때 사용하는 객체입니다.
:::

:::topic-grid
## 호스트 앱 표시
- [Displaying the app extensions available to your app](https://developer.apple.com/documentation/extensionkit/displaying-the-app-extensions-available-to-your-app): 사용자가 승인, 활성화, 비활성화할 수 있도록 앱에서 사용할 수 있는 앱 extension을 표시합니다.
- [EXHostViewController](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller): 앱 extension이 제공하는 원격 뷰를 호스팅하는 view controller입니다.
- [EXAppExtensionBrowserViewController](https://developer.apple.com/documentation/extensionkit/exappextensionbrowserviewcontroller): 호스트 앱의 extension을 활성화하거나 비활성화하는 인터페이스를 표시하는 view controller입니다.
:::
