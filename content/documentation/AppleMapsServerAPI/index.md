---
route: /documentation/AppleMapsServerAPI
source_url: https://developer.apple.com/documentation/AppleMapsServerAPI
source_locale: en-US
section: docc
content_type: symbol
title: Apple Maps Server API
original_title: Apple Maps Server API
source_hash: 766f18466b424fc1e6493fa3cd01694a650011bb80c73e65ceb40439051997c0
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:03:27+00:00'
last_translated_at: '2026-03-13T16:25:00+09:00'
---

# Apple Maps Server API

앱의 지리 관련 검색을 간소화하여 API 호출을 줄이고 기기 전력 사용을 절약합니다.

## 개요

이 웹 기반 서비스를 사용하면 장소, 관심 지점, 지오코딩, 경로, 검색 자동 완성 후보, 예상 도착 시간(ETA) 계산과 같은 지리 관련 검색을 앱 내부가 아니라 서버로 옮겨 앱의 API를 간소화할 수 있습니다.

Maps Server API를 시험해 보려면 [Creating a Maps token](https://developer.apple.com/documentation/MapKitJS/creating-a-maps-token)에 설명된 방식으로 임시 토큰을 생성하십시오. 이 자격 증명을 사용해 앱에서 API에 접근하거나, [Try Maps Server API](https://developer.apple.com/maps/try-maps-server-api/)에서 사용할 수 있습니다.

Apple Maps Server API는 [MapKit JS](https://developer.apple.com/documentation/MapKitJS) API와 유사한 웹 기반 API이며, 동일한 인증 인프라를 사용합니다. API 호출에는 JSON Web Token(JWT)을 이용한 인증이 필요합니다. Apple Developer 계정에서 설정을 마치면 토큰 생성에 사용할 키를 얻을 수 있습니다.

API 사용을 시작하려면 먼저 식별자와 비공개 키를 생성하고, 아래 단계에 따라 서비스에 인증해야 합니다.

- 식별자와 비공개 키를 생성하려면 [Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key)의 단계를 따르십시오.
- 식별자와 비공개 키를 사용해 Apple Maps Server API용 토큰을 생성하려면 [Creating and using tokens with Maps Server API](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api)의 단계를 따르십시오.
- Token API를 사용해 API 접근용 [Generate a Maps token](https://developer.apple.com/documentation/applemapsserverapi/-v1-token)을 호출하십시오.

이 서비스는 Apple Maps Server API와 MapKit JS를 합쳐 팀당 하루 최대 25,000회의 서비스 호출을 제공합니다. 앱이 이 할당량을 초과하면 서비스는 HTTP 429 오류(Too Many Requests)를 반환하며, 앱은 나중에 다시 시도해야 합니다. 더 큰 일일 할당량이 필요하면 [quota increase request form](https://developer.apple.com/contact/request/mapkitjs/)을 제출하십시오.

:::topic-grid
## 핵심 사항
- [Creating and using tokens with Maps Server API](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api): Maps Server API를 사용하기 위한 JSON Web Token에 서명하고 일반적인 서명 오류를 디버깅합니다.
- [Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key): MapKit JS용 토큰을 생성하기 전에 Maps 식별자와 비공개 키를 생성합니다.
- [Generate a Maps token](https://developer.apple.com/documentation/applemapsserverapi/-v1-token): 서비스 API를 호출할 때 사용하는 JWT Maps 접근 토큰을 반환합니다.
- [Debugging an Invalid token](https://developer.apple.com/documentation/applemapsserverapi/debugging-an-invalid-token): JavaScript 콘솔 로그, 토큰, 이벤트를 살펴보며 토큰이 유효하지 않은 이유를 파악합니다.
- [Common objects](https://developer.apple.com/documentation/applemapsserverapi/common-objects): API 응답에 포함되는 공통 JSON 객체를 이해합니다.
- [Integrating the Apple Maps Server API into Java server applications](https://developer.apple.com/documentation/applemapsserverapi/integrating-the-apple-maps-server-api-into-java-server-applications): 지리 관련 검색을 앱 내부가 아닌 서버로 옮겨 앱의 API를 간소화합니다.
:::

:::topic-grid
## 지오코딩
- [Geocode an address](https://developer.apple.com/documentation/applemapsserverapi/-v1-geocode): 지정한 주소의 위도와 경도를 반환합니다.
- [Reverse geocode a location](https://developer.apple.com/documentation/applemapsserverapi/-v1-reversegeocode): 지정한 좌표에 존재하는 주소 배열을 반환합니다.
:::

:::topic-grid
## 검색
- [AddressCategory](https://developer.apple.com/documentation/applemapsserverapi/addresscategory): 정치적 지리 경계와 관련된 검색 카테고리입니다.
- [SearchACResultType](https://developer.apple.com/documentation/applemapsserverapi/searchacresulttype): 검색 요청의 결과 타입을 나타내는 열거형 문자열입니다.
- [SearchResultType](https://developer.apple.com/documentation/applemapsserverapi/searchresulttype): 검색 자동 완성 요청의 결과 타입을 나타내는 열거형 문자열입니다.
- [AlternateIdsResponse](https://developer.apple.com/documentation/applemapsserverapi/alternateidsresponse): 대체 Place ID와 관련 오류의 목록입니다.
- [AlternateIdsResponse.AlternateIds](https://developer.apple.com/documentation/applemapsserverapi/alternateidsresponse/alternateids): 특정 Place ID에 대한 대체 Place ID 목록을 포함합니다.
- [PlacesResponse](https://developer.apple.com/documentation/applemapsserverapi/placesresponse): Place ID와 오류의 목록입니다.
- [PlacesResponse.PlaceLookupError](https://developer.apple.com/documentation/applemapsserverapi/placesresponse/placelookuperror): 조회 호출과 연관된 오류입니다.
- [Search for places that match specific criteria](https://developer.apple.com/documentation/applemapsserverapi/-v1-search): 이름 또는 특정 검색 기준으로 장소를 찾습니다.
- [Search for places that meet specific criteria to autocomplete a place search](https://developer.apple.com/documentation/applemapsserverapi/-v1-searchautocomplete): 검색 자동 완성에 사용할 결과를 찾습니다.
- [Search for a place using an identifier](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-:id): 지정된 Place ID에 대한 Place 객체를 가져옵니다.
- [Search for places using mulitple identifiers](https://developer.apple.com/documentation/applemapsserverapi/-v1-place): 지정된 Place ID 집합에 대한 Place 객체 집합을 가져옵니다.
- [Obtain a list of alternate place identifiers](https://developer.apple.com/documentation/applemapsserverapi/-v1-place-alternateids): 하나 이상의 Place ID에 대한 대체 Place ID 목록을 가져옵니다.
:::

:::topic-grid
## 경로
- [Search for directions and estimated travel time between locations](https://developer.apple.com/documentation/applemapsserverapi/-v1-directions): 특정 기준으로 경로를 찾습니다.
- [Determine estimated arrival times and distances to one or more destinations](https://developer.apple.com/documentation/applemapsserverapi/-v1-etas): 출발지와 도착지 사이의 예상 도착 시간(ETA)과 거리를 반환합니다.
:::
