---
route: /documentation/MapKitJS
source_url: https://developer.apple.com/documentation/MapKitJS
source_locale: en-US
section: docc
content_type: symbol
title: MapKit JS
original_title: MapKit JS
source_hash: 72aadc9faec5a10924fa5c3243ecf16643342fce1ab22bfb01d6bdabc0c81c4e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:38:45+00:00'
last_translated_at: '2026-03-13T23:38:45+09:00'
---

# MapKit JS

웹사이트에 상호작용형 Apple 지도를 삽입하고, 관심 지점에 주석을 달며, 지리 관련 검색을 수행합니다.

## 개요

이 JavaScript API를 사용하면 iOS와 Android를 포함한 여러 플랫폼과 운영 체제의 웹페이지나 앱에 상호작용형 지도를 직접 삽입할 수 있습니다. 네이티브 앱용 [MapKit](https://developer.apple.com/documentation/MapKit)처럼, 지도에 annotation과 overlay를 추가해 관심 지점이나 사용자의 목적지를 강조할 수도 있습니다.

*샌프란시스코 지역 지도를 표시하는 웹 브라우저 창 이미지입니다.*

MapKit JS는 장소 세부 정보와 Look Around 이미지를 위한 상호작용형 뷰도 제공합니다.

*California Science Center의 세부 정보를 표시하는 Place Detail 뷰와 Look Around 뷰 예시가 함께 제시됩니다.*

MapKit JS는 초기화와 일부 API 호출을 위해 Maps token을 통한 권한 부여가 필요합니다. Maps token을 만드는 방법은 [Creating a Maps token](https://developer.apple.com/documentation/mapkitjs/creating-a-maps-token)을 참고하십시오.

### 브라우저 호환성

MapKit JS는 다음 브라우저 버전을 지원합니다.

- Firefox 79 이상
- Google Chrome 109 이상(데스크탑 모드만 지원)
- Microsoft Edge
- Safari 13.1 이상

:::topic-grid
## 핵심
- [Maps Embed API로 장소 정보 표시하기](https://developer.apple.com/documentation/mapkitjs/displaying-place-information-using-the-maps-embed-api): URL을 사용해 지도 위에 장소 정보를 표시합니다.
- [Maps token 만들기](https://developer.apple.com/documentation/mapkitjs/creating-a-maps-token): 적절한 권한 부여와 함께 MapKit 서비스에 접근할 token을 생성합니다.
- [최신 MapKit JS 버전 로드하기](https://developer.apple.com/documentation/mapkitjs/loading-the-latest-version-of-mapkit-js): 자동으로 업데이트되는 최신 MapKit JS 버전 또는 원하는 특정 버전에 연결합니다.
- [mapkit](https://developer.apple.com/documentation/mapkitjs/mapkit): 웹사이트에 Apple 지도를 삽입하기 위한 JavaScript API입니다.
:::

:::topic-grid
## 버전 노트
- [MapKit JS Release Notes](https://developer.apple.com/documentation/mapkitjs/mapkit-js-release-notes): MapKit JS의 업데이트, 버그 수정, API 변경 사항을 알아봅니다.
:::

:::topic-grid
## 열거형
- [RegionPriority](https://developer.apple.com/documentation/mapkitjs/regionpriority): 구성된 region의 중요도를 나타내는 값입니다.
:::
