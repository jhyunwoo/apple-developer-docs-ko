---
route: /documentation/AdServices
source_url: https://developer.apple.com/documentation/AdServices
source_locale: en-US
section: docc
content_type: symbol
title: AdServices
original_title: AdServices
source_hash: 1086304179f330af1805f1f70af488c60c780314f44558e540ea75118caea509
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:21+00:00'
last_translated_at: '2026-03-13T10:02:00+00:00'
---

# AdServices

iOS 기기의 App Store에서 시작된 앱 다운로드 캠페인의 어트리뷰션을 측정합니다.

## 개요

Apple Ads Attribution API는 `AdServices` 프레임워크와 Apple의 attribution 서버와의 서버 측 통신을 위한 RESTful API를 결합한 솔루션입니다. 이 API는 Apple Ads 캠페인에서 Apple Ads attribution 데이터를 가져옵니다. 특정 Apple Ads 캠페인 메타데이터를 Apple Ads 캠페인의 성과와 비교해 attribution 데이터를 측정할 수 있습니다.

다음 다이어그램은 RESTful 엔드포인트와 함께 `AdServices` 프레임워크를 사용해 attribution 데이터를 가져오는 과정을 보여 줍니다.

![AdServices 프레임워크와 RESTful API 사이의 상호 작용 순서를 보여 주는 다이어그램입니다.](https://developer.apple.com)

- 1단계에서는 `AdServices` 프레임워크에 토큰을 요청합니다.
- 2단계에서는 `AdServices` 프레임워크가 토큰을 생성합니다.
- 3단계에서는 그 토큰을 RESTful API 요청에 사용해 Apple의 attribution 서버에서 attribution record를 가져옵니다. 자세한 내용은 [attributionToken()](https://developer.apple.com/documentation/adservices/aaattribution/attributiontoken())를 참고하세요.
- 4단계에서는 반환된 attribution record에 Apple Ads Campaign Management API의 캠페인에 대응하는 key-value 쌍이 포함됩니다. 자세한 내용은 [Attribution payload descriptions](https://developer.apple.com/documentation/adservices/aaattribution/attributiontoken()#Attribution-payload-descriptions)를 참고하세요.

:::topic-grid
## 필수 항목
- [Changelog](https://developer.apple.com/documentation/adservices/changelog): Ad Services 프레임워크 업데이트 로그입니다.
:::

:::topic-grid
## 토큰
- [AAAttribution](https://developer.apple.com/documentation/adservices/aaattribution): 프레임워크가 토큰을 요청할 때 사용하는 상위 클래스입니다.
:::

:::topic-grid
## 오류
- [AAAttributionError](https://developer.apple.com/documentation/adservices/aaattributionerror): 상위 클래스가 발생시키는 오류 코드입니다.
- [AAAttributionErrorDomain](https://developer.apple.com/documentation/adservices/aaattributionerrordomain): 프레임워크 attribution 오류 도메인입니다.
- [AAAttributionError.Code](https://developer.apple.com/documentation/adservices/aaattributionerror/code): 상위 클래스가 발생시키는 오류 코드입니다.
:::
