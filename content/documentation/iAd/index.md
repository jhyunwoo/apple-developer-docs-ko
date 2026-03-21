---
route: /documentation/iAd
source_url: https://developer.apple.com/documentation/iAd
source_locale: en-US
section: docc
content_type: symbol
title: iAd
original_title: iAd
source_hash: 84deafbe000a935a59fa55ce6330c8d6d75500d8cd5b53ef68b68a6711058c27
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:28:21+00:00'
last_translated_at: '2026-03-13T23:28:34+09:00'
---

# iAd

Apple Search Ads iAd Attribution API는 iOS 기기에서 Apple Search Ads 캠페인으로부터 발생한 앱 데이터를 attribution하는 레거시 프레임워크입니다.

## 개요

:::warning Warning
2023년 2월 7일 이후에는 Apple Search Ads iAd Attribution API로 보내는 모든 요청이 `"iad-attribution"` `=` `false` 값을 반환하거나 오류를 반환합니다. [requestAttributionDetails(_:)](https://developer.apple.com/documentation/iad/adclient/requestattributiondetails(_:))를 참고하십시오. iOS 14.3 이상 기기의 현재 attribution 통합에는 [Apple Ads](https://developer.apple.com/documentation/apple_ads) Campaign Management API와 함께 [AdServices](https://developer.apple.com/documentation/AdServices) 프레임워크를 사용하십시오. iOS 14.2 이하 기기에서의 다운로드 및 재다운로드에 대해서는 attribution을 사용할 수 없습니다.
:::

Attribution 데이터는 Apple Search Ads 사용자 인터페이스 또는 Apple Search Ads API를 통해 생성된 광고를 탭한 결과로 발생한 앱 다운로드 및 재다운로드 같은 앱 광고 캠페인 메타데이터로 구성됩니다.

Apple이 수집하는 모든 Apple Search Ads 데이터는 [Apple Privacy Policy](https://www.apple.com/privacy)의 적용을 받습니다.

:::topic-grid
## 핵심
- [iAd Changelog](https://developer.apple.com/documentation/iad/iad-changelog): Apple Search Ads iAd Attribution API의 새로운 내용을 살펴봅니다.
- [Setting Up Apple Search Ads Attribution](https://developer.apple.com/documentation/iad/setting-up-apple-search-ads-attribution): attribution dictionary를 가져옵니다.
- [ADClient](https://developer.apple.com/documentation/iad/adclient): attribution 응답을 요청할 때 사용하는 상위 클래스입니다.
:::

:::topic-grid
## Attribution 오류
- [ADClientErrorDomain](https://developer.apple.com/documentation/iad/adclienterrordomain): completion handler로 전달되는 오류 도메인입니다.
- [ADClientError](https://developer.apple.com/documentation/iad/adclienterror-swift.struct): attribution 응답에서 completion handler block으로 전달되는 오류 코드 그룹입니다.
- [ADClientError.Code](https://developer.apple.com/documentation/iad/adclienterror-swift.struct/code): attribution 응답에서 completion handler로 전달되는 오류 코드입니다.
:::

:::topic-grid
## 지원 중단
- [Deprecated Symbols](https://developer.apple.com/documentation/iad/deprecated-symbols): 기존 iAd 프레임워크의 참조 심볼입니다.
:::
