---
route: /documentation/AppleMusicAPI
source_url: https://developer.apple.com/documentation/AppleMusicAPI
source_locale: en-US
section: docc
content_type: symbol
title: Apple Music API
original_title: Apple Music API
source_hash: 51f4b8289719ec882896c3aaf18d34275e2f51d7bee6e36a2f435c6473ff406f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:38:51+00:00'
last_translated_at: '2026-03-13T23:42:00+09:00'
---

# Apple Music API

카탈로그 콘텐츠와 개인 콘텐츠를 사용해 스트리밍 음악을 통합합니다.

## 개요

Apple Music API를 사용하면 Apple Music Catalog의 미디어 정보와 사용자의 개인 iCloud Music Library 정보에 접근할 수 있습니다.

- Apple Music Catalog에는 Apple Music에서 제공되는 모든 리소스가 포함됩니다.
- iCloud Music Library에는 사용자가 자신의 개인 라이브러리에 추가한 리소스만 포함됩니다. 예를 들어 Apple Music의 항목, iTunes Store에서 구입한 노래, 디스크와 다른 앱에서 가져온 항목이 포함됩니다. 이 라이브러리에는 Apple Music Catalog에 없는 콘텐츠가 포함될 수 있습니다.

이 API를 사용하면 앨범, 노래, 아티스트, 재생목록, 뮤직 비디오, Apple Music 스테이션, 평점, 차트, 추천, 그리고 사용자가 최근에 재생한 콘텐츠에 대한 정보를 가져올 수 있습니다. 사용자의 적절한 승인을 받으면 재생목록을 생성하거나 수정하고 사용자의 콘텐츠에 평점을 적용할 수도 있습니다.

:::note Note
Apple Music Catalog를 대량으로 접근하려면 [Apple Music Feed](https://developer.apple.com/documentation/AppleMusicFeed)를 사용합니다.
:::

:::topic-grid
## 핵심 항목
- [Generating Developer Tokens](https://developer.apple.com/documentation/applemusicapi/generating-developer-tokens): Apple Music API 요청에 필요한 developer token을 생성합니다.
- [User Authentication for MusicKit](https://developer.apple.com/documentation/applemusicapi/user-authentication-for-musickit): Music User Token을 사용해 사용자 데이터 요청을 인증합니다.
- [Handling Requests and Responses](https://developer.apple.com/documentation/applemusicapi/handling-requests-and-responses): 요청을 작성하고 API 응답을 처리합니다.
- [Handling Resource Representation and Relationships](https://developer.apple.com/documentation/applemusicapi/handling-resource-representation-and-relationships): 확장된 속성, 포함된 관계, relationship view와 함께 리소스를 가져옵니다.
- [Storefronts and Localization](https://developer.apple.com/documentation/applemusicapi/storefronts-and-localization): 카탈로그 정보를 가져올 지역별 지리적 위치를 선택하거나, 사용자의 개인 라이브러리에서 정보를 가져옵니다.
- [Common Objects](https://developer.apple.com/documentation/applemusicapi/common-objects): 프레임워크 응답에 포함되는 공통 JSON 객체를 이해합니다.
- [Managing Content Ratings, Alternate Versions, and Equivalencies](https://developer.apple.com/documentation/applemusicapi/managing-content-ratings-alternate-versions-and-equivalencies): 콘텐츠의 여러 버전과 대체 버전을 처리합니다.
- [Fetching Resources by Page](https://developer.apple.com/documentation/applemusicapi/fetching-resources-by-page): pagination을 사용해 다음 객체 집합을 가져옵니다.
:::

:::topic-grid
## 앨범, 아티스트, 노래, 비디오
- [Albums](https://developer.apple.com/documentation/applemusicapi/albums-api): 앨범 이름, 아티스트, 트랙 목록, 아트워크, 출시일, 녹음 정보를 가져오고, 사용자의 라이브러리에 새 앨범을 추가합니다.
- [Artists](https://developer.apple.com/documentation/applemusicapi/artists-api): 아티스트가 만든 콘텐츠와 재생목록 및 라디오 스테이션에서의 참조를 포함한 정보를 가져옵니다.
- [Songs](https://developer.apple.com/documentation/applemusicapi/songs-api): 특정 노래의 정보와 그 곡을 만든 아티스트, 수록된 앨범 정보를 가져옵니다.
- [Music Videos](https://developer.apple.com/documentation/applemusicapi/music-videos-api): 뮤직 비디오의 정보와 해당 아티스트, 관련 앨범 정보를 가져오고, 사용자의 라이브러리에 새 비디오를 추가합니다.
:::

:::topic-grid
## 재생목록 및 스테이션
- [Playlists](https://developer.apple.com/documentation/applemusicapi/playlists-api): 재생목록의 내용을 가져오고, 사용자의 라이브러리에 새 재생목록을 추가하고, 기존 재생목록에 트랙을 추가합니다.
- [Apple Music Stations](https://developer.apple.com/documentation/applemusicapi/apple-music-stations): Apple Music이 제공하는 스트리밍 콘텐츠에 대한 정보를 가져옵니다.
:::

:::topic-grid
## 검색
- [Search](https://developer.apple.com/documentation/applemusicapi/search): 사용자의 개인 라이브러리나 Apple Music Catalog에서 앨범, 노래, 아티스트 및 기타 정보를 검색합니다.
:::

:::topic-grid
## 평점, 장르, 차트
- [Ratings](https://developer.apple.com/documentation/applemusicapi/ratings-api): 앨범, 노래, 재생목록, 뮤직 비디오, 스테이션에 대한 평점을 가져오고 설정합니다.
- [Music Genres](https://developer.apple.com/documentation/applemusicapi/music-genres): 사용자의 음악 또는 Apple Music Catalog 항목의 장르 정보를 가져옵니다.
- [Charts](https://developer.apple.com/documentation/applemusicapi/charts-api): 앨범, 노래, 뮤직 비디오의 인기도를 보여 주는 차트 정보를 가져옵니다.
:::

:::topic-grid
## 활동, 큐레이터, 레코드 레이블
- [Activities](https://developer.apple.com/documentation/applemusicapi/activities-api): Apple Music Catalog와 관련된 요청 및 응답 활동 정보를 가져옵니다.
- [Curators](https://developer.apple.com/documentation/applemusicapi/curators-api): 재생목록이나 스테이션을 큐레이션한 사람에 대한 정보를 가져옵니다.
- [Record Labels](https://developer.apple.com/documentation/applemusicapi/record-labels-api): Apple Music Catalog의 레코드 레이블 정보를 가져옵니다.
:::

:::topic-grid
## 추천 및 기록
- [Recommendations](https://developer.apple.com/documentation/applemusicapi/recommendations): 사용자의 라이브러리와 구매 기록을 기반으로 음악 추천을 가져옵니다.
- [History](https://developer.apple.com/documentation/applemusicapi/history): 사용자가 최근에 재생한 노래와 스테이션에 대한 기록 정보를 가져옵니다.
:::

:::topic-grid
## 여러 리소스 타입 가져오기
- [Get Multiple Catalog Resources Using Resource-Typed ID Parameters](https://developer.apple.com/documentation/applemusicapi/get-multiple-catalog-resources-by-resource-typed-ids-parameters): 식별자를 사용해 하나 이상의 카탈로그 리소스를 가져옵니다.
- [Get Multiple Library Resources Using Resource-Typed ID Parameters](https://developer.apple.com/documentation/applemusicapi/get-multiple-library-resources-by-resource-typed-ids-parameters): 식별자를 사용해 하나 이상의 라이브러리 리소스를 가져옵니다.
:::

:::topic-grid
## 엔드포인트
- [Placeholder Endpoint to Test Connectivity](https://developer.apple.com/documentation/applemusicapi/dummy-endpoint-to-test-connectivity)
- [Get a User's Storefront](https://developer.apple.com/documentation/applemusicapi/get-a-user's-storefront): 특정 사용자의 storefront를 가져옵니다.
:::

:::topic-grid
## 딕셔너리
- [Artwork](https://developer.apple.com/documentation/applemusicapi/artwork): artwork를 나타내는 객체입니다.
- [DescriptionAttribute](https://developer.apple.com/documentation/applemusicapi/descriptionattribute): 설명 속성을 나타내는 객체입니다.
- [EditorialNotes](https://developer.apple.com/documentation/applemusicapi/editorialnotes): notes 속성을 나타내는 객체입니다.
- [LangageTagResponse](https://developer.apple.com/documentation/applemusicapi/langagetagresponse): language tag 요청에 대한 응답입니다.
- [PaginatedResourceCollectionResponse](https://developer.apple.com/documentation/applemusicapi/paginatedresourcecollectionresponse): 요청에 대한 paginated resource 객체들로 구성된 응답 객체입니다.
- [PlayParameters](https://developer.apple.com/documentation/applemusicapi/playparameters): 리소스의 재생 매개변수를 나타내는 객체입니다.
- [Preview](https://developer.apple.com/documentation/applemusicapi/preview): 리소스의 미리보기를 나타내는 객체입니다.
- [RelationshipResponse](https://developer.apple.com/documentation/applemusicapi/relationshipresponse): 직접 리소스 관계 가져오기에 대한 응답입니다.
- [RelationshipViewResponse](https://developer.apple.com/documentation/applemusicapi/relationshipviewresponse): 직접 리소스 view 가져오기에 대한 응답입니다.
- [StorefrontsResponse](https://developer.apple.com/documentation/applemusicapi/storefrontsresponse): storefront 요청에 대한 응답입니다.
- [View](https://developer.apple.com/documentation/applemusicapi/view): 흥미로운 연관성을 나타내는 다른 리소스 객체로의 일대일 또는 일대다 관계 view입니다.
:::
