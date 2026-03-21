---
route: /documentation/FileProvider
source_url: https://developer.apple.com/documentation/FileProvider
source_locale: en-US
section: docc
content_type: symbol
title: File Provider
original_title: File Provider
source_hash: 30bdfe5dd4bcd8f4e6e7b7e69fe11b0931f495708610c42e782500a36fdd56d5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:17:18+00:00'
last_translated_at: '2026-03-13T22:37:00+09:00'
---

# File Provider

다른 앱이 앱이 관리하고 원격 저장소와 동기화하는 파일과 폴더에 접근할 수 있도록 하는 extension입니다.

## 개요

앱이 원격 저장소의 사용자 문서를 제공하고 동기화하는 데 초점을 맞추고 있다면, 다른 앱을 사용하는 동안에도 사용자가 그 문서에 접근할 수 있도록 File Provider extension을 구현할 수 있습니다. 로컬 문서만 공유하면 되는 경우에는 아래의 [Share files locally](https://developer.apple.com/documentation/fileprovider#Share-files-locally)를 참고하십시오.

![File Provider extension을 통해 앱과 서버가 상호 작용하는 구조를 보여 주는 다이어그램입니다. 앱은 document browser와 통신하고, document browser는 File Provider extension에 데이터를 요청합니다. File Provider extension은 원격 서버와 업데이트를 동기화합니다.](https://developer.apple.com)

이 프레임워크에는 File Provider extension을 구축하는 두 가지 서로 다른 시작점이 있습니다.

:::term-list
[NSFileProviderReplicatedExtension](https://developer.apple.com/documentation/fileprovider/nsfileproviderreplicatedextension): 시스템이 File Provider extension을 통해 접근하는 콘텐츠를 관리합니다. macOS 11+ 및 iOS 16+에서 사용할 수 있습니다.
[NSFileProviderExtension](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension): extension이 File Provider extension을 통해 접근하는 파일을 호스팅하고 관리합니다. iOS 11+에서 사용할 수 있습니다.
:::

replicated extension은 문서의 로컬 사본을 모니터링하고 관리하는 책임을 집니다. file provider는 로컬 사본과 원격 저장소 사이의 데이터 동기화에 집중하며, 로컬 변경 사항은 업로드하고 원격 변경 사항은 다운로드합니다. 자세한 내용은 [Replicated File Provider extension](https://developer.apple.com/documentation/fileprovider/replicated-file-provider-extension)을 참고하십시오.

nonreplicated extension은 원격 파일용 placeholder 생성과 관리를 포함해 extension 콘텐츠의 로컬 사본을 관리합니다. 또한 그 콘텐츠를 원격 저장소와 동기화합니다. 자세한 내용은 [Nonreplicated File Provider extension](https://developer.apple.com/documentation/fileprovider/nonreplicated-file-provider-extension)을 참고하십시오.

### 파일을 로컬로 공유하기

앱이 로컬에 저장하는 문서에 접근하게 하려는 경우에는 File Provider extension이 필요하지 않습니다.

iOS에서 다른 앱이 `Documents` 디렉터리의 파일에 접근할 수 있게 하려면 앱의 Info 탭 또는 `Info.plist` 파일에 다음 키를 설정하십시오. document browser 기반 앱은 [UISupportsDocumentBrowser](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW37) 키를 설정합니다. 그 외 모든 앱은 [UIFileSharingEnabled](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW20)와 [LSSupportsOpeningDocumentsInPlace](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/plist/info/LSSupportsOpeningDocumentsInPlace) 키를 모두 설정합니다.

이 키들을 설정하면 다른 앱이 `Documents` 디렉터리의 콘텐츠를 제자리에서 열고 편집할 수 있습니다. 파일은 Files 앱과 document browser에도 나타납니다. 자세한 내용은 [UIDocumentBrowserViewController](https://developer.apple.com/documentation/UIKit/UIDocumentBrowserViewController) 클래스를 참고하십시오.

:::topic-grid
## 핵심 사항
- [File Provider updates](https://developer.apple.com/documentation/Updates/FileProvider): File Provider의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## extension 유형
- [Replicated File Provider extension](https://developer.apple.com/documentation/fileprovider/replicated-file-provider-extension): 파일의 로컬 사본을 원격 저장소와 동기화하는 File Provider extension을 구축합니다.
- [Nonreplicated File Provider extension](https://developer.apple.com/documentation/fileprovider/nonreplicated-file-provider-extension): 사용자의 로컬 파일을 호스팅하고 관리하는 File Provider extension을 구축합니다.
:::

:::topic-grid
## extension 관리
- [NSFileProviderManager](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager): 앱 또는 File Provider extension에서 file provider와 통신할 때 사용하는 manager 객체입니다.
:::

:::topic-grid
## 제공 항목
- [NSFileProviderItem](https://developer.apple.com/documentation/fileprovider/nsfileprovideritem-swift.typealias): File Provider extension이 관리하는 항목입니다.
- [NSFileProviderItemProtocol](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol): File Provider extension이 관리하는 항목의 속성을 정의하는 프로토콜입니다.
- [NSFileProviderItemIdentifier](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemidentifier): File Provider extension이 관리하는 항목의 고유 식별자입니다.
- [NSFileProviderItemCapabilities](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemcapabilities): 사용자가 document browser에서 수행할 수 있는 동작을 정의하는 항목의 capability입니다.
- [NSFileProviderTypeAndCreator](https://developer.apple.com/documentation/fileprovider/nsfileprovidertypeandcreator): 항목의 파일 타입과 파일 creator 코드를 담는 구조체입니다.
:::

:::topic-grid
## 클라우드 검색
- [NSFileProviderSearching](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearching): file provider에서 검색을 지원하기 위해 구현하는 프로토콜입니다.
:::

:::topic-grid
## 도메인
- [NSFileProviderDomain](https://developer.apple.com/documentation/fileprovider/nsfileproviderdomain): File Provider extension의 도메인입니다.
:::

:::topic-grid
## 오류
- [NSFileProviderError](https://developer.apple.com/documentation/fileprovider/nsfileprovidererror): File Provider extension 오류 정보를 담는 구조체입니다.
- [NSFileProviderError.Code](https://developer.apple.com/documentation/fileprovider/nsfileprovidererror/code): File Provider extension의 오류 코드입니다.
- [NSFileProviderErrorDomain](https://developer.apple.com/documentation/fileprovider/nsfileprovidererrordomain): File Provider extension의 오류 도메인입니다.
- [NSFileProviderErrorItemKey](https://developer.apple.com/documentation/fileprovider/nsfileprovidererroritemkey): 동기화 관련 오류 정보를 접근하기 위한 키입니다.
- [NSFileProviderErrorNonExistentItemIdentifierKey](https://developer.apple.com/documentation/fileprovider/nsfileprovidererrornonexistentitemidentifierkey): 항목이 존재하지 않을 때 지정된 항목의 식별자에 접근하기 위한 키입니다.
- [NSFileProviderErrorCollidingItemKey](https://developer.apple.com/documentation/fileprovider/nsfileprovidererrorcollidingitemkey): 파일명 충돌 오류의 user info dictionary에서 기존 항목에 접근하기 위한 키입니다.
:::

:::topic-grid
## 데이터 내보내기
- [Exporting file provider metrics data](https://developer.apple.com/documentation/fileprovider/exporting-file-provider-metrics-data): 사용량, 일관성, 오류 데이터를 다운로드하고 분석합니다.
:::

:::topic-grid
## 구조체
- [NSFileProviderUserInfoKey](https://developer.apple.com/documentation/fileprovider/nsfileprovideruserinfokey)
- [NSFileProviderVolumeUnsupportedReason](https://developer.apple.com/documentation/fileprovider/nsfileprovidervolumeunsupportedreason): 외부 볼륨이 도메인 저장에 적합하지 않을 수 있는 이유를 설명하는 상수입니다.
:::
