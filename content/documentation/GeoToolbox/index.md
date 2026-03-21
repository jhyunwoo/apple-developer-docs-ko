---
route: /documentation/GeoToolbox
source_url: https://developer.apple.com/documentation/GeoToolbox
source_locale: en-US
section: docc
content_type: symbol
title: GeoToolbox
original_title: GeoToolbox
source_hash: 76a2b21e63de14c3a3e3c0e3f4bae262e0083e24453d1d9e8ced8109e1ea57c1
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:22:13+00:00'
last_translated_at: '2026-03-13T16:55:00+09:00'
---

# GeoToolbox

지도 좌표에 대한 장소 설명자 정보를 판별합니다.

## 개요

`GeoToolbox`를 사용해 Maps 기술과 서드파티 매핑 시스템 전반에서 사용할 `PlaceDescriptor` 구조체를 생성합니다.

:::topic-grid
## 장소에 대한 풍부한 정보 얻기
- [PlaceDescriptor](https://developer.apple.com/documentation/geotoolbox/placedescriptor): 매핑 서비스가 전화번호, 웹사이트 등 풍부한 장소 정보를 찾으려고 시도할 때 사용할 수 있는 장소 식별 정보를 담는 구조체입니다.
:::

:::topic-grid
## 장소 설명자 생성
- [init(item:)](https://developer.apple.com/documentation/geotoolbox/placedescriptor/init(item:)): map item으로부터 장소 설명자를 생성합니다.
- [init(representations:commonName:supportingRepresentations:)](https://developer.apple.com/documentation/geotoolbox/placedescriptor/init(representations:commonname:supportingrepresentations:)): 장소를 검색하거나 풍부한 데이터를 가져올 때 사용하기에 적합한 장소 설명자를 생성합니다.
:::

:::topic-grid
## 장소와 매핑 서비스 제공자를 설명하는 값
- [PlaceDescriptor.PlaceRepresentation](https://developer.apple.com/documentation/geotoolbox/placedescriptor/placerepresentation): 장소를 검색하거나 풍부한 데이터를 가져올 때 사용하기 적합한 실제 장소를 나타내는 값입니다.
- [PlaceDescriptor.SupportingPlaceRepresentation](https://developer.apple.com/documentation/geotoolbox/placedescriptor/supportingplacerepresentation): 매핑 서비스 제공자의 영숫자 위치 식별자처럼 고유 속성을 사용해 실제 장소의 표현을 설명하는 값입니다.
:::
