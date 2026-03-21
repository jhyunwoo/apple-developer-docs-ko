---
route: /documentation/AppLicenseDeliverySDK
source_url: https://developer.apple.com/documentation/AppLicenseDeliverySDK
source_locale: en-US
section: docc
content_type: symbol
title: App License Delivery SDK
original_title: App License Delivery SDK
source_hash: 7caa8ac041d7f4e07823c867c440e6c751171d312a36b64f0add353ae5af28ae
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:10:36+00:00'
last_translated_at: '2026-03-14T00:36:00+09:00'
---

# App License Delivery SDK

웹 서버에서 라이선스를 발급해 iOS 또는 iPadOS 기기에서 대체 배포 앱의 설치를 안전하게 보호합니다.

## 개요

이 Swift SDK는 대체 배포 앱을 위한 *디지털 권리 관리*(DRM)를 가능하게 합니다. 이 SDK를 사용해 [MarketplaceKit](https://developer.apple.com/documentation/MarketplaceKit)으로 만든 대체 앱 마켓플레이스나 웹사이트에서 배포하는 다른 앱을 위한 라이선스를 생성할 수 있습니다. 대체 앱 마켓플레이스는 이 SDK를 사용해 마켓플레이스에서 개발자가 배포하는 각 앱마다 라이선스를 생성합니다. 다운로드를 개별적으로 라이선스 처리함으로써 App Store와 유사한 안전한 설치 경험을 제공할 수 있습니다.

이 SDK의 프레임워크를 사용해 컴파일된 Swift 코드를 실행할 수 있는 라이선스 서버를 웹사이트 백엔드에 구현하십시오. 그런 다음 기기의 운영 체제가 기대하는 표준 위치에 라이선스 서버용 endpoint를 게시합니다. 필요할 때 시스템은 사용자가 다음 중 하나를 다운로드할 때 endpoint에서 라이선스를 가져옵니다.

- 웹사이트에서 대체 앱 마켓플레이스를 다운로드할 때
- 대체 앱 마켓플레이스에서 개발자가 배포하는 앱을 다운로드할 때
- 사용자가 직접 개발해 웹사이트에서 배포하는 앱을 다운로드할 때

![위아래로 쌓인 두 개의 상자로 구성된 흐름도입니다. 위쪽 상자의 제목은 App web server, 아래쪽 상자의 제목은 The device’s OS입니다. 흐름은 아래 상자의 왼쪽 단계인 Install request에서 시작해 Checks licensing endpoint로 이어지고, 다시 위쪽 상자의 Provides licensing endpoint로 올라갑니다. 이후 아래 상자로 돌아와 Requests app license로 진행한 뒤, 위쪽 상자의 Swift licensing endpoint 단계로 올라가고, 그 안의 Generates app license 박스 옆에 App License Delivery SDK라는 callout이 표시됩니다. 마지막으로 아래 상자로 돌아와 Downloads app 단계로 이어집니다.](https://developer.apple.com)

개발자 계정이 웹사이트에서 앱을 배포할 자격이 있다면 [Downloads](https://developer.apple.com/download/all/)에서 이 SDK를 다운로드할 수 있습니다. 자세한 내용은 [Distributing your app from your website](https://developer.apple.com/documentation/appdistribution/distributing-your-app-from-your-website)를 참고하십시오.

:::note 플랫폼, OS, 도구 요구 사항
Apple silicon Mac, Intel Mac, macOS 13.5 이상, x86_64용 일부 Linux 버전, 그리고 Xcode 15 이상(macOS 14 SDK 포함)이 필요합니다.
:::

:::topic-grid
## 핵심 사항
- [Configuring your app licensing environment](https://developer.apple.com/documentation/applicensedeliverysdk/configuring-the-app-licensing-environment): 계정 수준 서명 자산을 만들고 대상 플랫폼에 맞게 SDK를 빌드합니다.
:::

:::topic-grid
## 앱 라이선싱
- [Licensing alternative distribution apps](https://developer.apple.com/documentation/applicensedeliverysdk/licensing-alternative-distribution-apps): 앱과 마켓플레이스에서 제공하는 앱의 설치를 지원하는 라이선스 서버를 빌드합니다.
- [Renewing and revoking app licenses](https://developer.apple.com/documentation/applicensedeliverysdk/renewing-and-revoking-app-licenses): 라이선스를 발급한 앱이 실행되는지를 판단합니다.
- [ALDAppKey](https://developer.apple.com/documentation/applicensedeliverysdk/aldappkey): 앱과, 앱의 라이선스 요청을 복호화하는 데 필요한 키를 식별하는 구조체입니다.
- [ALDLicenseAttribute](https://developer.apple.com/documentation/applicensedeliverysdk/aldlicenseattribute): 세션에서 요청된 라이선스 유형을 정의하는 구조체입니다.
- [ALDProvider](https://developer.apple.com/documentation/applicensedeliverysdk/aldprovider): 대체 앱 마켓플레이스의 서명 자산으로 세션을 생성하는 객체입니다.
- [ALDSession](https://developer.apple.com/documentation/applicensedeliverysdk/aldsession): 라이선스 요청의 세부 정보와 라이선스 응답 생성 메서드를 담는 구조체입니다.
:::
