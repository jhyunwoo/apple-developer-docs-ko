---
route: /documentation/MarketplaceKit
source_url: https://developer.apple.com/documentation/MarketplaceKit
source_locale: en-US
section: docc
content_type: symbol
title: MarketplaceKit
original_title: MarketplaceKit
source_hash: 70cf34561f2e063509777be7e6e4c041d5f03e4d798bad9831117aa806d553e2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:11:24+00:00'
last_translated_at: '2026-03-13T23:11:40+09:00'
---

# MarketplaceKit

대체 앱 마켓플레이스를 만들고, 대체 앱 마켓플레이스를 통해 앱을 배포하거나, 웹사이트에서 직접 앱을 배포합니다.

## 개요

*대체 앱 마켓플레이스*는 App Store의 대안으로, 다른 개발자의 앱을 설치할 수 있게 해 주는 앱입니다. MarketplaceKit은 대체 앱 마켓플레이스가 자신이 배포하는 앱을 사람들의 기기에 설치할 수 있도록 해 줍니다. 이 프레임워크는 Spotlight Search, App Thinning처럼 품질 높은 탐색 및 설치 경험을 구성하는 기능도 함께 지원합니다. 이 프레임워크를 사용하면 기존 앱 설치를 관리하고, 다운로드 진행 상황을 전달하고, 앱 라이선스를 업데이트하고, 앱 검색 동작을 사용자화할 수 있습니다.

이 프레임워크는 대체 앱 마켓플레이스 외에도 다음과 같은 경우를 지원합니다.

- 웹페이지에서 앱 설치를 요청하는 웹 브라우저
- 런타임에 설치 출처를 판별해야 하는 앱

이 덕분에 앱은 설치 출처에 따라 기능을 분기할 수 있습니다.

![MarketplaceKit의 여러 사용 사례를 설명하는 세 개의 다이어그램입니다. 왼쪽부터 웹페이지에서 앱 설치, 대체 앱 마켓플레이스에서 앱 설치, 런타임에 앱의 설치 출처 판별을 보여 줍니다.](https://developer.apple.com)

:::important Important
대체 앱 마켓플레이스를 개발하려면 marketplace entitlement 사용 승인을 요청해야 합니다. 요청 절차는 지역에 따라 다릅니다. 자세한 내용과 entitlement 요청 방법은 [Participating in alternative distribution for specific regions](https://developer.apple.com/documentation/marketplacekit/participating-in-alternative-distribution-for-specific-regions)를 참고하십시오.
:::

:::topic-grid
## 핵심
- [Creating an alternative app marketplace](https://developer.apple.com/documentation/marketplacekit/creating-an-alternative-app-marketplace): 마켓플레이스 앱 안에서 다른 서드파티 앱을 배포할 수 있게 합니다.
- [Distributing your app from your website](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-from-your-website): 웹사이트에서 사람들이 기기에 앱을 설치할 수 있도록 앱과 웹사이트를 구성합니다.
- [Distributing your app on an alternative app marketplace](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-on-an-alternative-marketplace): 대체 앱 마켓플레이스를 통한 대체 배포에 맞게 앱을 설계합니다.
:::

:::topic-grid
## 웹 서비스
- [Processing alternative app marketplace notifications](https://developer.apple.com/documentation/marketplacekit/processing-alternative-marketplace-notifications): 대체 마켓플레이스에서 제공하는 앱의 추가 및 제거를 관리합니다.
- [Ingesting an alternative distribution package](https://developer.apple.com/documentation/marketplacekit/ingesting-an-alternative-distribution-package): App Store Connect에서 제공되는 앱 버전을 처리해 서버에서 다운로드할 수 있도록 저장합니다.
- [Installing your app from your website](https://developer.apple.com/documentation/marketplacekit/installing-your-app-from-your-website): 개발한 앱을 웹사이트를 통해 배포할 때 그 설치 과정을 관리합니다.
- [Installing apps from an alternative marketplace](https://developer.apple.com/documentation/marketplacekit/installing-apps-from-an-alternative-marketplace): 개발자들이 마켓플레이스 앱을 통해 배포하는 앱의 설치를 관리합니다.
- [Supplying an install verification token](https://developer.apple.com/documentation/marketplacekit/supplying-an-install-verification-token): 서명된 JSON web token을 생성해 대체 배포 앱의 설치를 지원합니다.
:::

:::topic-grid
## 권한 부여
- [Reauthenticating a person to manage apps](https://developer.apple.com/documentation/marketplacekit/reauthenticating-a-person-to-manage-apps): 앱을 업데이트해야 하거나 기기가 백업에서 복원되었을 때 앱의 권한을 다시 갱신합니다.
- [Providing age-rating appropriate content](https://developer.apple.com/documentation/marketplacekit/providing-age-rating-appropriate-content): 연령 등급 기반 콘텐츠 제한을 확인하고, 기기에서 허용된 최대 등급을 초과하는 앱에 대해 승인을 요청할 수 있도록 합니다.
- [com.apple.developer.marketplace.app-installation](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.marketplace.app-installation): 앱이 대체 앱 마켓플레이스로서 다른 앱을 배포할 수 있게 해 주는 entitlement입니다.
- [com.apple.developer.browser.app-installation](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.browser.app-installation): 브라우저가 웹사이트에서 대체 배포 앱을 설치할 수 있게 해 주는 entitlement입니다.
- [App License Delivery SDK](https://developer.apple.com/documentation/AppLicenseDeliverySDK): 웹 서버에서 라이선스를 제공해 iOS 또는 iPadOS 기기에서 대체 배포 앱 설치를 보호합니다.
:::

:::topic-grid
## 브라우저 지원
- [Enabling alternative distribution app installation in a browser](https://developer.apple.com/documentation/marketplacekit/enabling-alternative-distribution-app-installation-in-a-browser): 브라우저 앱이 웹사이트에서 대체 배포 앱을 설치할 수 있도록 지원을 추가합니다.
:::

:::topic-grid
## 앱 관리
- [AppLibrary](https://developer.apple.com/documentation/marketplacekit/applibrary): 설치된 모든 앱의 카탈로그를 나타내며, 마켓플레이스가 배포한 앱에 다양한 서비스를 제공하는 클래스입니다.
- [AppVersion](https://developer.apple.com/documentation/marketplacekit/appversion): 앱의 식별자와 버전 번호를 포함해 앱을 설명하는 정보입니다.
- [AutomaticUpdate](https://developer.apple.com/documentation/marketplacekit/automaticupdate): 업데이트 가능한 앱과 다운로드 URL을 설명하는 정보입니다.
- [InstallRequirements](https://developer.apple.com/documentation/marketplacekit/installrequirements): 기기에 대한 앱의 설치 조건입니다.
- [AppleItemID](https://developer.apple.com/documentation/marketplacekit/appleitemid): 앱을 나타내는 식별자입니다.
- [AppleVersionID](https://developer.apple.com/documentation/marketplacekit/appleversionid): 특정 앱 버전 하나를 나타내는 식별자입니다.
- [MarketplaceKitURIScheme](https://developer.apple.com/documentation/marketplacekit/marketplacekiturischeme): 대체 배포 앱 설치 링크를 정의하는 URI scheme입니다.
:::

:::topic-grid
## 백그라운드 서비스
- [MarketplaceAppExtension](https://developer.apple.com/documentation/marketplacekit/marketplaceappextension): 인증, 설치, deep link를 통한 마켓플레이스 실행을 지원하는 extension입니다.
:::

:::topic-grid
## 앱 배포 UI
- [ActionButton](https://developer.apple.com/documentation/marketplacekit/actionbutton): 사람이 탭하여 앱을 설치, 업데이트, 실행할 수 있게 하는 사용자 인터페이스 요소입니다.
- [InstallMetadata](https://developer.apple.com/documentation/marketplacekit/installmetadata): 특정 앱을 설치하거나 업데이트할 때 필요한 정보와 이를 시작한 사람에 대한 정보입니다.
- [InstallConfiguration](https://developer.apple.com/documentation/marketplacekit/installconfiguration): 요청된 앱 설치 또는 앱 업데이트를 설명하는 정보입니다.
- [InstallConfirmationResult](https://developer.apple.com/documentation/marketplacekit/installconfirmationresult): 사람이 앱 설치 버튼과 상호 작용할 때 앱 설치를 진행할지 여부를 나타내는 옵션입니다.
- [BatchInstallConfiguration](https://developer.apple.com/documentation/marketplacekit/batchinstallconfiguration): 여러 앱 설치 또는 업데이트를 설명하는 정보입니다.
- [BatchInstallConfirmationResult](https://developer.apple.com/documentation/marketplacekit/batchinstallconfirmationresult): 사람이 앱 설치 버튼과 상호 작용할 때 여러 앱 설치를 진행할지 여부를 나타내는 옵션입니다.
- [MarketplaceDisplayOption](https://developer.apple.com/documentation/marketplacekit/marketplacedisplayoption): 운영체제가 마켓플레이스로 연결할 때 사용하는 deep link 유형입니다.
- [MarketplaceSceneDelegate](https://developer.apple.com/documentation/marketplacekit/marketplacescenedelegate): 마켓플레이스 앱으로 들어오는 deep link 요청을 처리하는 delegate입니다.
:::

:::topic-grid
## 설치 출처
- [AppDistributor](https://developer.apple.com/documentation/marketplacekit/appdistributor): 앱이 어떤 마켓플레이스에서 설치되었는지 설명하는 옵션입니다.
:::

:::topic-grid
## 토큰 및 거래 보고
- [Reporting transactions for the Core Technology Commission](https://developer.apple.com/documentation/marketplacekit/reporting-transactions-for-core-technology-commission): 앱과 관련해 사람에게 제공하는 적격 구매를 추적하고, 토큰을 사용해 Apple에 보고합니다.
- [TransactionReporting](https://developer.apple.com/documentation/marketplacekit/transactionreporting): 거래 보고를 위한 토큰 서비스를 제공하는 열거형입니다.
:::

:::topic-grid
## 오류
- [MarketplaceKitError](https://developer.apple.com/documentation/marketplacekit/marketplacekiterror): MarketplaceKit 프레임워크가 던질 수 있는 오류입니다.
:::

:::topic-grid
## 지역 지원
- [Participating in alternative distribution for specific regions](https://developer.apple.com/documentation/marketplacekit/participating-in-alternative-distribution-for-specific-regions): 지역마다 지원되는 기능 차이에 맞춰 앱의 대체 배포를 준비합니다.
:::

:::topic-grid
## 지원 중단 항목
- [MarketplaceExtension](https://developer.apple.com/documentation/marketplacekit/marketplaceextension)
- [MarketplaceExtensionConfiguration](https://developer.apple.com/documentation/marketplacekit/marketplaceextensionconfiguration)
:::

:::topic-grid
## 구조체
- [RequestAppDeletionAction](https://developer.apple.com/documentation/marketplacekit/requestappdeletionaction)
:::
