---
route: /documentation/SystemExtensions
source_url: https://developer.apple.com/documentation/SystemExtensions
source_locale: en-US
section: docc
content_type: symbol
title: System Extensions
original_title: System Extensions
source_hash: 575a78b4ec57912a97fa0b9e46c509ce0d3e9c8425d6d1d3212d650a6436ef8a
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:28:07+00:00'
last_translated_at: '2026-03-13T09:26:00+00:00'
---

# System Extensions

macOS 기능을 확장하는 사용자 공간 코드를 설치하고 관리합니다.

## 개요

드라이버와 기타 저수준 코드를 커널이 아니라 사용자 공간에서 설치하고 관리하여 macOS의 기능을 확장합니다. 시스템 확장은 사용자 공간에서 실행되므로 macOS의 보안이나 안정성을 손상시킬 수 없습니다. 시스템은 이 확장에 높은 수준의 권한을 부여하여, 이전에는 커널 확장(KEXT)에만 허용되던 작업을 수행할 수 있게 합니다.

[DriverKit](https://developer.apple.com/documentation/DriverKit), [Endpoint Security](https://developer.apple.com/documentation/EndpointSecurity), [Network Extension](https://developer.apple.com/documentation/NetworkExtension) 같은 프레임워크를 사용해 시스템 확장을 작성하고, 확장을 앱 번들에 포함합니다. 런타임에는 SystemExtensions 프레임워크를 사용해 사용자의 시스템에 확장을 설치하거나 업데이트합니다. 일단 설치되면 확장은 시스템의 모든 사용자가 사용할 수 있습니다. 사용자가 앱을 삭제하면 확장도 함께 삭제되므로, 확장을 비활성화할 수 있습니다.

### 시스템 확장과 호스트 앱 구성하기

확장을 성공적으로 활성화하려면 다음 규칙을 따라야 합니다.

- 확장은 파일 확장자를 제외한 bundle identifier와 일치해야 합니다. 예를 들어 bundle identifier가 `com.example.usbdriver`인 DriverKit 확장은 파일명을 `com.example.usbdriver.dext`로 사용해야 합니다. 마찬가지로 bundle identifier가 `com.example.networkextension`인 NetworkExtension 확장은 파일명을 `com.example.networkextension.systemextension`으로 사용해야 합니다.
- 확장에 `com.apple.developer.system-extension.redistributable` entitlement가 없는 한, 앱 서명에 사용한 것과 같은 Team ID를 확장 서명에도 사용해야 합니다.
- 앱과 확장을 Mac App Store를 통해 배포하거나, 둘 다 notarization해야 합니다. 자세한 내용은 [Notarizing macOS software before distribution](https://developer.apple.com/documentation/Security/notarizing-macos-software-before-distribution)을 참고하세요.

:::topic-grid
## 필수 항목
- [드라이버, 시스템 확장, kext 구현하기](https://developer.apple.com/documentation/systemextensions/implementing-drivers-system-extensions-and-kexts): 하드웨어와 통신하고 저수준 서비스를 제공하기 위한 드라이버와 시스템 확장을 만들고, 일부 작업에만 커널 확장을 사용합니다.
- [시스템 확장 디버깅 및 테스트](https://developer.apple.com/documentation/DriverKit/debugging-and-testing-system-extensions): 설치 과정에서 macOS가 수행하는 보안 검사를 일시적으로 비활성화해 시스템 확장을 디버깅합니다.
- [System Extension Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.system-extension.install): 앱이 시스템 확장을 활성화하거나 비활성화할 권한이 있는지 나타내는 불리언 값입니다.
:::

:::topic-grid
## 사용 설명
- [NSSystemExtensionUsageDescriptionKey](https://developer.apple.com/documentation/systemextensions/nssystemextensionusagedescriptionkey): 앱이 시스템 확장 번들을 설치하려는 이유를 사용자에게 알려 주는 메시지입니다.
- [OSBundleUsageDescriptionKey](https://developer.apple.com/documentation/systemextensions/osbundleusagedescriptionkey): 앱이 드라이버 확장 번들을 설치하려는 이유를 사용자에게 알려 주는 메시지입니다.
:::

:::topic-grid
## 확장 활성화 및 비활성화
- [시스템 확장과 드라이버 설치하기](https://developer.apple.com/documentation/systemextensions/installing-system-extensions-and-drivers): 시스템 확장과 드라이버를 활성화하여 시스템에서 사용할 수 있게 하고, 필요에 따라 업데이트하거나 비활성화합니다.
- [OSSystemExtensionManager](https://developer.apple.com/documentation/systemextensions/ossystemextensionmanager): 시스템 확장의 활성화와 비활성화를 돕는 타입입니다.
- [OSSystemExtensionRequest](https://developer.apple.com/documentation/systemextensions/ossystemextensionrequest): 시스템 확장을 활성화하거나 비활성화하기 위한 요청입니다.
- [System Extension Redistributable Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.system-extension.redistributable): 다른 개발 팀이 여러분이 만든 시스템 확장을 배포할 수 있는지 나타내는 불리언 값입니다.
:::

:::topic-grid
## 오류
- [OSSystemExtensionError](https://developer.apple.com/documentation/systemextensions/ossystemextensionerror): 실패한 확장 관리자 요청을 설명하는 오류입니다.
- [OSSystemExtensionError.Code](https://developer.apple.com/documentation/systemextensions/ossystemextensionerror/code): 시스템 확장용 오류 코드입니다.
- [OSSystemExtensionErrorDomain](https://developer.apple.com/documentation/systemextensions/ossystemextensionerrordomain): 시스템 확장 오류를 식별하는 오류 도메인입니다.
:::

:::topic-grid
## 참고 자료
- [SystemExtensions Constants](https://developer.apple.com/documentation/systemextensions/systemextensions-constants)
:::

:::topic-grid
## 클래스
- [OSSystemExtensionInfo](https://developer.apple.com/documentation/systemextensions/ossystemextensioninfo)
- [OSSystemExtensionsWorkspace](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspace)
:::

:::topic-grid
## 프로토콜
- [OSSystemExtensionsWorkspaceObserver](https://developer.apple.com/documentation/systemextensions/ossystemextensionsworkspaceobserver)
:::
