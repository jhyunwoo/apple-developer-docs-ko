---
route: /documentation/BackgroundAssets
source_url: https://developer.apple.com/documentation/BackgroundAssets
source_locale: en-US
section: docc
content_type: symbol
title: Background Assets
original_title: Background Assets
source_hash: 7af4eff68ef40e96c5c6b2e245add3eb841628b23d696b03983d1798710be909
canonical_source: manual-translation
last_crawled_at: '2026-03-13T02:34:56+00:00'
last_translated_at: '2026-03-13T02:34:56+00:00'
---

# Background Assets

앱이 에셋을 다운로드하는 동안 사용자가 기다리는 시간을 줄이거나 없앱니다.

## 개요

사용자의 기기에서 에셋 다운로드를 시스템이 여러분의 기본 설정에 따라 대신 관리하게 하고, 필요하면 Apple 서버에 에셋을 호스팅할 수도 있습니다. 예를 들어 게임은 첫 실행 전에 튜토리얼 에셋을 다운로드하고, 레벨 팩, 3D 캐릭터 모델, 텍스처 같은 다른 에셋은 플레이어가 게임을 진행하면서 필요할 때 다운로드하도록 지정할 수 있습니다. Managed Background Assets의 기본 구현은 다운로드, 업데이트, 압축 등을 대신 처리합니다. Apple-Hosted Background Assets를 선택하면 앱 빌드와 비슷한 방식으로 에셋을 App Store Connect에 업로드하고 সেখানে 유지 관리합니다.

![프레임워크의 로고와 오디오, 이미지, 업적 같은 추가 콘텐츠의 다운로드 상태를 보여 주는 여러 개의 원형 진행 표시기를 포함한 그래픽입니다. 각 진행 표시기에는 오디오의 음표처럼 해당 콘텐츠 유형을 나타내는 아이콘이 표시됩니다.](https://developer.apple.com)

:::note visionOS availability
호환되는 iPad 및 iPhone 앱의 경우 Background Assets는 visionOS 1.0 이상에서 사용할 수 있습니다. visionOS용으로 빌드한 앱의 경우 Background Assets는 visionOS 2.4 이상에서 사용할 수 있습니다.
:::

이 기능을 사용하려면 다음을 수행하세요:

1. 다운로드 정책과 기타 세부 사항을 지정하는 매니페스트 파일이 포함된 에셋 팩으로 에셋을 그룹화합니다. 시스템이 필수 에셋 팩은 실행 전에 다운로드하고, 다른 팩은 실행을 막지 않으면서 미리 가져오고, 일부는 필요할 때만 온디맨드로 다운로드하도록 지정할 수 있습니다. 자세한 내용은 [Creating managed asset packs](https://developer.apple.com/documentation/backgroundassets/creating-managed-asset-packs)를 참고하세요.
2. 프로젝트에 managed Background Download 확장을 추가하고, 그에 맞게 프로젝트를 구성합니다. 필요하다면 다운로더 확장을 사용자화하고, 필요한 시점에 온디맨드 에셋을 다운로드하는 코드를 앱에 추가합니다. 자세한 내용은 [Downloading Apple-hosted asset packs](https://developer.apple.com/documentation/backgroundassets/downloading-apple-hosted-asset-packs)를 참고하세요.
3. Apple 호스팅 에셋 팩이든 자체 호스팅 에셋 팩이든 앱을 배포하기 전에 Xcode 설치에 포함된 로컬 모의 서버를 사용해 코드를 테스트합니다. 자세한 내용은 [Testing asset packs locally](https://developer.apple.com/documentation/backgroundassets/testing-asset-packs-locally)를 참고하세요.
4. Apple이 호스팅하는 에셋의 경우, TestFlight나 App Store를 통해 앱을 배포하기 전에 에셋 팩을 App Store Connect에 업로드합니다. 자세한 내용은 App Store Connect 도움말의 [Overview of Apple-hosted asset packs](https://developer.apple.com/help/app-store-connect/manage-asset-packs/overview-of-apple-hosted-asset-packs)를 참고하세요.

또는 저수준 Background Assets API를 사용해 직접 에셋 다운로드를 관리하고 호스팅할 수도 있습니다. 자세한 내용은 [Configuring an unmanaged Background Assets project](https://developer.apple.com/documentation/backgroundassets/configuring-an-unmanaged-background-assets-project)와 [Downloading essential assets in the background](https://developer.apple.com/documentation/backgroundassets/downloading-essential-assets-in-the-background)를 참고하세요.

:::important Important
Background Assets 프레임워크는 앱의 추가 에셋을 다운로드하는 용도로만 사용하고, 다른 목적으로는 사용하지 마세요. 예를 들어 사용자나 기기를 식별하거나 광고 또는 광고 측정을 수행하기 위한 데이터를 수집하거나 전송해서는 안 됩니다.
:::

:::topic-grid
## 핵심
- [Creating managed asset packs](https://developer.apple.com/documentation/backgroundassets/creating-managed-asset-packs): Managed 에셋 팩을 생성하고, 다운로드 옵션을 선택하고, Apple이 호스팅하는 에셋 팩을 App Store Connect에 업로드합니다.
- [Downloading Apple-hosted asset packs](https://developer.apple.com/documentation/backgroundassets/downloading-apple-hosted-asset-packs): 프로젝트를 구성하고 Apple이 호스팅하는 에셋 팩을 다운로드하는 코드를 작성합니다.
- [Testing asset packs locally](https://developer.apple.com/documentation/backgroundassets/testing-asset-packs-locally): Mac의 모의 서버를 사용해 시스템이 관리하는 에셋 팩을 테스트합니다.
:::

:::topic-grid
## Managed 에셋 팩
- [AssetPack](https://developer.apple.com/documentation/backgroundassets/assetpack): 시스템이 함께 다운로드하는 에셋 아카이브입니다.
- [AssetPackManager](https://developer.apple.com/documentation/backgroundassets/assetpackmanager): 에셋 팩을 관리하는 actor입니다.
- [ManagedDownloaderExtension](https://developer.apple.com/documentation/backgroundassets/manageddownloaderextension): 시스템 구현을 사용해 에셋 팩 다운로드를 자동으로 예약하는 앱 확장입니다.
- [BAAppGroupID](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAAppGroupID): 앱과 에셋 팩을 사용하는 확장 사이에서 공유하는 앱 그룹 식별자입니다.
- [BAHasManagedAssetPacks](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAHasManagedAssetPacks): 시스템이 에셋 팩을 자동으로 관리하도록 허용하는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## Apple 호스팅 Managed 에셋 팩
- [BAUsesAppleHosting](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAUsesAppleHosting): 에셋 팩 호스팅에 Apple 서비스를 사용하는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 자체 호스팅 비관리형 에셋 팩
- [AssetPackManifest](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest): 다운로드 가능한 에셋 팩 목록을 나열하는 매니페스트의 표현입니다.
:::

:::topic-grid
## 비관리형 에셋 다운로드
- [Configuring an unmanaged Background Assets project](https://developer.apple.com/documentation/backgroundassets/configuring-an-unmanaged-background-assets-project): 앱과 확장 타깃을 구성하여 개별 에셋을 직접 관리하고 다운로드합니다.
- [Downloading essential assets in the background](https://developer.apple.com/documentation/backgroundassets/downloading-essential-assets-in-the-background): 앱이 처음 실행되기 전에 필요한 에셋을 앱 확장과 Background Assets 프레임워크를 사용해 가져옵니다.
- [BAManifestURL](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAManifestURL): 에셋의 이름과 크기가 들어 있는 앱 매니페스트 파일의 위치 URL입니다.
- [BAInitialDownloadRestrictions](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAInitialDownloadRestrictions): 앱 설치 직후 즉시 다운로드되는 에셋 집합에 적용되는 제한입니다.
- [BAEssentialMaxInstallSize](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAEssentialMaxInstallSize): 시스템이 앱 실행 전에 다운로드하는 필수 에셋의 총 최대 크기(바이트)입니다.
- [BAMaxInstallSize](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAMaxInstallSize): 앱 설치 직후 즉시 다운로드되는 비필수 에셋의 총 최대 크기(바이트)입니다.
- [BADownloadManager](https://developer.apple.com/documentation/backgroundassets/badownloadmanager): 예약된 에셋 다운로드 대기열을 관리하는 객체입니다.
- [BADownloaderExtension](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw): 앱이 실행되고 있지 않을 때 앱 생명 주기 이벤트에 반응하고 완료된 에셋 다운로드를 처리하기 위한 인터페이스입니다.
- [BADownloaderExtensionConfiguration](https://developer.apple.com/documentation/backgroundassets/badownloaderextensionconfiguration)
- [BAURLDownload](https://developer.apple.com/documentation/backgroundassets/baurldownload): 다운로드할 원격 에셋을 나타내는 객체입니다.
- [BADownload](https://developer.apple.com/documentation/backgroundassets/badownload): 진행 중이거나 완료된 에셋 다운로드를 나타내는 객체입니다.
:::

:::topic-grid
## 오류
- [ManagedBackgroundAssetsError](https://developer.apple.com/documentation/backgroundassets/managedbackgroundassetserror): Managed 에셋 팩을 위한 오류입니다.
- [BAErrorDomain](https://developer.apple.com/documentation/backgroundassets/baerrordomain)
- [BAErrorCode](https://developer.apple.com/documentation/backgroundassets/baerrorcode)
:::
