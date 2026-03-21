---
route: /documentation/BrowserKit
source_url: https://developer.apple.com/documentation/BrowserKit
source_locale: en-US
section: docc
content_type: symbol
title: BrowserKit
original_title: BrowserKit
source_hash: c65c74c9579d51c654477e8b36f694ef03695a994404ae3d0e30226b49588eb9
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:31:22+00:00'
last_translated_at: '2026-03-13T23:34:00+09:00'
---

# BrowserKit

브라우저 데이터를 다른 브라우저로 전송하거나, 대체 브라우저 엔진을 사용할 수 있는 기기인지 확인합니다.

## 개요

BrowserKit 프레임워크를 사용하면 브라우징 기록, 북마크, 브라우저 확장과 같은 데이터를 한 브라우저에서 다른 브라우저로 전송할 수 있고, 기기가 대체 브라우저 엔진을 구현할 자격이 있는지도 테스트할 수 있습니다.

## 대체 브라우저 엔진 사용 자격 테스트

기기가 대체 브라우저 엔진을 지원하는지 테스트하려면, WebKit으로 개발한 브라우저 앱에서 [isEligible(for:completionHandler:)](https://developer.apple.com/documentation/browserkit/beavailability/iseligible(for:completionhandler:))를 호출합니다.

```swift
do {
  guard await BEAvailability.isEligible(for: .webBrowser) else { return } 
...  
```

기기가 대체 브라우저 엔진을 지원한다면, 사용자가 대체 브라우저 엔진을 사용하는 앱의 대체 배포판을 다운로드할 수 있도록 링크를 제공할 수 있습니다. 대체 배포에 대한 자세한 내용은 [Distributing your app on an alternative app marketplace](https://developer.apple.com/documentation/marketplacekit/distributing-your-app-on-an-alternative-marketplace)를 참고합니다. 대체 브라우저 엔진을 개발하거나 임베드하는 자세한 내용은 [BrowserEngineKit](https://developer.apple.com/documentation/BrowserEngineKit)을 참고합니다.

:::topic-grid
## 핵심 항목
- [Transferring browsing data to another browser](https://developer.apple.com/documentation/browserkit/transferring-browsing-data-to-another-browser): 시스템이 제공하는 sheet를 사용해 브라우징 기록, 북마크, 읽기 목록, 브라우저 확장을 앱으로 또는 앱에서 전송할 수 있게 합니다.
- [BEAvailability](https://developer.apple.com/documentation/browserkit/beavailability): 기기가 대체 브라우저 엔진을 실행할 자격이 있는지 테스트하는 클래스입니다.
:::

:::topic-grid
## 데이터 내보내기 관리
- [BEBrowserDataExportManager](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager): 다른 브라우저로 브라우징 데이터를 내보내는 작업을 처리하는 클래스입니다.
- [BEExportOptions](https://developer.apple.com/documentation/browserkit/beexportoptions): 내보낼 데이터를 식별하는 옵션입니다.
- [BEExportMetadata](https://developer.apple.com/documentation/browserkit/beexportmetadata): 내보내기 가능한 브라우저 데이터를 설명하는 메타데이터입니다.
:::

:::topic-grid
## 데이터 가져오기 관리
- [BEBrowserDataImportManager](https://developer.apple.com/documentation/browserkit/bebrowserdataimportmanager): 다른 브라우저에서 브라우징 데이터를 가져오는 작업을 처리하는 클래스입니다.
- [BEImportMetadata](https://developer.apple.com/documentation/browserkit/beimportmetadata): 브라우저 데이터 전송의 가져오기 기능을 설명하는 메타데이터입니다.
- [BEImportOptions](https://developer.apple.com/documentation/browserkit/beimportoptions): 브라우징 데이터를 가져오기 위한 옵션입니다.
:::

:::topic-grid
## 브라우저 데이터
- [BEBrowserDataHistoryVisit](https://developer.apple.com/documentation/browserkit/bebrowserdatahistoryvisit): 브라우저 사이에서 페이지 방문 기록을 전송하는 클래스입니다.
- [BEBrowserDataBookmark](https://developer.apple.com/documentation/browserkit/bebrowserdatabookmark): 브라우저 사이에서 북마크 정보를 전송하는 클래스입니다.
- [BEBrowserDataReadingListItem](https://developer.apple.com/documentation/browserkit/bebrowserdatareadinglistitem): 브라우저 사이에서 읽기 목록 데이터를 전송하는 클래스입니다.
- [BEBrowserDataExtension](https://developer.apple.com/documentation/browserkit/bebrowserdataextension): 브라우저 사이에서 브라우저 확장 정보를 전송하는 클래스입니다.
- [BEBrowserData](https://developer.apple.com/documentation/browserkit/bebrowserdata): 원본 브라우저 앱의 브라우징 데이터를 표현한 것입니다.
:::

:::topic-grid
## 오류
- [BEBrowserDataExchangeError](https://developer.apple.com/documentation/browserkit/bebrowserdataexchangeerror-swift.struct): 브라우저 데이터 가져오기 또는 내보내기 작업 중 발생하는 오류입니다.
- [BEBrowserDataExchangeErrorDomain](https://developer.apple.com/documentation/browserkit/bebrowserdataexchangeerrordomain): 브라우저 데이터 교환 오류의 error domain을 식별하는 상수입니다.
:::
