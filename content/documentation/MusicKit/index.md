---
route: /documentation/MusicKit
source_url: https://developer.apple.com/documentation/MusicKit
source_locale: en-US
section: docc
content_type: symbol
title: MusicKit
original_title: MusicKit
source_hash: c7bda96fcd2b19487e10408454263ccd3f2fe1a12758bae3ece594dffb7789e9
canonical_source: manual-translation
last_crawled_at: '2026-03-13T02:33:25+00:00'
last_translated_at: '2026-03-13T02:33:25+00:00'
---

# MusicKit

앱을 Apple Music과 통합합니다.

## 개요

MusicKit을 사용하여 앱을 [Apple Music API](https://developer.apple.com/documentation/AppleMusicAPI)와 통합하세요. Apple Music API는 Apple Music 카탈로그의 음악 항목 정보에 접근할 때 사용하는 웹 서비스입니다. MusicKit을 사용하면 Apple Music과 연동되는 앱을 더 쉽게 구축할 수 있습니다.

이 프레임워크는 Swift에서 음악 항목에 접근하기 위한 모델 계층과, 앱에 음악을 추가할 수 있도록 하는 재생 지원을 제공합니다. 또한 음악 항목의 아트워크에 해당하는 이미지를 표시하는 뷰나, 활성 Apple Music 구독이 없을 수 있는 사용자에게 음악 구독 제안을 표시하는 방법처럼 관련된 사용자 인터페이스 요소도 일부 제공합니다.

:::important Important
사용자가 앱이 자신의 음악 데이터에 접근하도록 허가해야 합니다. 앱의 `Info.plist` 파일에 [NSAppleMusicUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) 키를 추가하고, 사용자의 미디어를 어떻게 사용할지에 대한 설명을 포함하세요. 이 키가 없으면 시스템은 앱이 사용자의 음악에 접근하려고 할 때 앱을 종료합니다.
:::

앱이 MusicKit을 사용할 수 있도록 [MusicAuthorization](https://developer.apple.com/documentation/musickit/musicauthorization)으로 권한을 요청하세요. 현재 [MusicSubscription](https://developer.apple.com/documentation/musickit/musicsubscription)의 구체적인 기능을 확인해 음악 관련 기능을 사용자가 이용할 수 있는지 확인하세요. [MusicCatalogSearchRequest](https://developer.apple.com/documentation/musickit/musiccatalogsearchrequest)로 검색어를 사용해 음악 항목을 찾거나, [MusicCatalogResourceRequest](https://developer.apple.com/documentation/musickit/musiccatalogresourcerequest)로 필터를 사용해 음악 항목을 찾을 수 있습니다. MusicKit이 제공하는 두 가지 음악 플레이어 중 하나를 사용해 앱에서 음악을 재생하세요. 음악 구독 제안을 표시하여 사용자가 앱 안에서 Apple Music 무료 체험을 시작할 수 있도록 할 수도 있습니다.

[MusicDataRequest](https://developer.apple.com/documentation/musickit/musicdatarequest)를 사용하면 임의의 Apple Music API 엔드포인트에서 콘텐츠를 로드하여, Apple Music API에서 제공하는 추가 기능을 더욱 폭넓게 활용할 수 있습니다.

:::topic-grid
## 핵심
- [Using Automatic Developer Token Generation for Apple Music API](https://developer.apple.com/documentation/musickit/using-automatic-token-generation-for-apple-music-api): 개발자 포털에서 앱의 MusicKit App Service 연동을 활성화합니다.
- [Using MusicKit to Integrate with Apple Music](https://developer.apple.com/documentation/musickit/using_musickit_to_integrate_with_apple_music): 사용자의 컬렉션에 있는 CD에 해당하는 앨범을 Apple Music에서 찾고, 그 앨범의 정보를 표시합니다.
- [NSAppleMusicUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription): 앱이 미디어 라이브러리에 접근 권한을 요청하는 이유를 알려 주는 메시지입니다.
:::

:::topic-grid
## 음악 항목
- [Album](https://developer.apple.com/documentation/musickit/album): 앨범을 나타내는 음악 항목입니다.
- [Artist](https://developer.apple.com/documentation/musickit/artist): 아티스트를 나타내는 음악 항목입니다.
- [Curator](https://developer.apple.com/documentation/musickit/curator): 큐레이터를 나타내는 음악 항목입니다.
- [Genre](https://developer.apple.com/documentation/musickit/genre): 장르를 나타내는 음악 항목입니다.
- [MusicVideo](https://developer.apple.com/documentation/musickit/musicvideo): 뮤직 비디오를 나타내는 음악 항목입니다.
- [Playlist](https://developer.apple.com/documentation/musickit/playlist): 플레이리스트를 나타내는 음악 항목입니다.
- [RadioShow](https://developer.apple.com/documentation/musickit/radioshow): 라디오 쇼를 나타내는 음악 항목입니다.
- [RecordLabel](https://developer.apple.com/documentation/musickit/recordlabel): 음반사를 나타내는 음악 항목입니다.
- [Song](https://developer.apple.com/documentation/musickit/song): 곡을 나타내는 음악 항목입니다.
- [Station](https://developer.apple.com/documentation/musickit/station): 스테이션을 나타내는 음악 항목입니다.
- [Track](https://developer.apple.com/documentation/musickit/track): 트랙을 나타내는 음악 항목입니다.
:::

:::topic-grid
## 음악 항목 속성
- [ContentRating](https://developer.apple.com/documentation/musickit/contentrating): 리소스를 재생하는 동안 재생될 수 있는 콘텐츠의 등급입니다.
- [EditorialNotes](https://developer.apple.com/documentation/musickit/editorialnotes): 에디토리얼 노트를 나타내는 객체입니다.
- [PreviewAsset](https://developer.apple.com/documentation/musickit/previewasset): 리소스의 미리보기를 나타내는 객체입니다.
:::

:::topic-grid
## 카탈로그 검색
- [MusicCatalogSearchRequest](https://developer.apple.com/documentation/musickit/musiccatalogsearchrequest): 앱이 검색어를 사용해 Apple Music 카탈로그에서 항목을 가져오는 데 사용하는 요청입니다.
- [MusicCatalogSearchResponse](https://developer.apple.com/documentation/musickit/musiccatalogsearchresponse): 카탈로그 검색 요청의 결과를 포함하는 객체입니다.
- [MusicCatalogSearchable](https://developer.apple.com/documentation/musickit/musiccatalogsearchable): 앱이 카탈로그 검색 요청을 사용해 가져올 수 있는 음악 항목을 위한 프로토콜입니다.
:::

:::topic-grid
## 필터를 사용한 리소스 로드
- [MusicCatalogResourceRequest](https://developer.apple.com/documentation/musickit/musiccatalogresourcerequest): 앱이 필터를 사용해 Apple Music 카탈로그에서 항목을 가져오는 데 사용하는 요청입니다.
- [MusicCatalogResourceResponse](https://developer.apple.com/documentation/musickit/musiccatalogresourceresponse): 카탈로그 리소스 요청의 결과를 포함하는 객체입니다.
- [AlbumFilter](https://developer.apple.com/documentation/musickit/albumfilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 앨범 속성입니다.
- [ArtistFilter](https://developer.apple.com/documentation/musickit/artistfilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 아티스트 속성입니다.
- [CuratorFilter](https://developer.apple.com/documentation/musickit/curatorfilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 큐레이터 속성입니다.
- [GenreFilter](https://developer.apple.com/documentation/musickit/genrefilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 장르 속성입니다.
- [MusicVideoFilter](https://developer.apple.com/documentation/musickit/musicvideofilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 뮤직 비디오 속성입니다.
- [PlaylistFilter](https://developer.apple.com/documentation/musickit/playlistfilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 플레이리스트 속성입니다.
- [RadioShowFilter](https://developer.apple.com/documentation/musickit/radioshowfilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 라디오 쇼 속성입니다.
- [RecordLabelFilter](https://developer.apple.com/documentation/musickit/recordlabelfilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 음반사 속성 집합입니다.
- [SongFilter](https://developer.apple.com/documentation/musickit/songfilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 곡 속성입니다.
- [StationFilter](https://developer.apple.com/documentation/musickit/stationfilter): 앱이 카탈로그 리소스 요청의 필터로 사용하는 스테이션 속성 집합입니다.
- [FilterableMusicItem](https://developer.apple.com/documentation/musickit/filterablemusicitem): 앱이 카탈로그 리소스 요청의 필터로 사용하는 음악 항목 속성 집합을 담는 연관 타입에 대한 선언입니다.
:::

:::topic-grid
## 범용 데이터 요청
- [MusicDataRequest](https://developer.apple.com/documentation/musickit/musicdatarequest): 임의의 Apple Music API 엔드포인트에서 데이터를 로드하기 위한 요청입니다.
- [MusicDataResponse](https://developer.apple.com/documentation/musickit/musicdataresponse): 데이터 요청의 결과를 포함하는 객체입니다.
:::

:::topic-grid
## 재생
- [ApplicationMusicPlayer](https://developer.apple.com/documentation/musickit/applicationmusicplayer): 앱이 Music 앱의 상태에 영향을 주지 않는 방식으로 음악을 재생할 때 사용하는 객체입니다.
- [SystemMusicPlayer](https://developer.apple.com/documentation/musickit/systemmusicplayer): 앱이 Music 앱의 상태를 제어하여 음악을 재생할 때 사용하는 객체입니다.
- [MusicPlayer](https://developer.apple.com/documentation/musickit/musicplayer): 앱이 음악을 재생하는 데 사용하는 객체입니다.
- [PlayableMusicItem](https://developer.apple.com/documentation/musickit/playablemusicitem): 음악 플레이어가 음악 항목의 재생을 시작할 때 사용하는 속성 집합입니다.
- [PlayParameters](https://developer.apple.com/documentation/musickit/playparameters): 음악 플레이어를 사용해 재생 가능한 음악 항목의 재생을 시작하기 위한 매개변수를 나타내는 불투명 객체입니다.
:::

:::topic-grid
## 아트워크
- [Artwork](https://developer.apple.com/documentation/musickit/artwork): 음악 항목의 아트워크를 나타내는 객체입니다.
- [ArtworkImage](https://developer.apple.com/documentation/musickit/artworkimage): 음악 항목의 아트워크 이미지를 표시하는 뷰입니다.
:::

:::topic-grid
## 권한 부여
- [MusicAuthorization](https://developer.apple.com/documentation/musickit/musicauthorization): 앱이 사용자의 음악 데이터에 접근하도록 사용자에게 충분한 설명에 기반한 동의를 요청할 수 있게 해 주는 타입입니다.
:::

:::topic-grid
## Apple Music 구독
- [MusicSubscription](https://developer.apple.com/documentation/musickit/musicsubscription): 사용자의 현재 Apple Music 구독 상태를 나타냅니다.
- [MusicSubscriptionOffer](https://developer.apple.com/documentation/musickit/musicsubscriptionoffer): Apple Music 구독 제안을 표시하기 위한 여러 타입을 묶는 타입입니다.
:::

:::topic-grid
## 토큰 관리
- [MusicTokenProvider](https://developer.apple.com/documentation/musickit/musictokenprovider): 음악 요청이 Apple Music API에 접근할 때 사용하는 객체입니다.
- [MusicDeveloperTokenProvider](https://developer.apple.com/documentation/musickit/musicdevelopertokenprovider): 음악 요청이 Apple Music API에 접근할 때 사용하는 메서드 집합입니다.
- [MusicUserTokenProvider](https://developer.apple.com/documentation/musickit/musicusertokenprovider): 음악 요청이 Apple Music API에 접근하기 위해 앱에 필요한 사용자 토큰을 가져올 때 사용하는 클래스입니다.
- [MusicTokenRequestOptions](https://developer.apple.com/documentation/musickit/musictokenrequestoptions): 음악 요청이 Apple Music API 접근에 필요한 토큰을 가져오기 위해 토큰 제공자 메서드에 전달하는 옵션입니다.
- [MusicTokenRequestError](https://developer.apple.com/documentation/musickit/musictokenrequesterror): Apple Music API 접근에 필요한 토큰을 요청할 때 토큰 제공자나 음악 요청이 던질 수 있는 오류입니다.
- [DefaultMusicTokenProvider](https://developer.apple.com/documentation/musickit/defaultmusictokenprovider): 음악 요청이 Apple Music API에 접근할 때 사용하는 기본 토큰 제공자입니다.
:::

:::topic-grid
## 유틸리티
- [MusicItem](https://developer.apple.com/documentation/musickit/musicitem): 음악 항목의 기본 요구사항을 정의하는 프로토콜입니다.
- [MusicItemID](https://developer.apple.com/documentation/musickit/musicitemid): 음악 항목의 고유 식별자를 나타내는 객체입니다.
- [MusicItemCollection](https://developer.apple.com/documentation/musickit/musicitemcollection): 음악 항목의 컬렉션입니다.
- [MusicPropertyContainer](https://developer.apple.com/documentation/musickit/musicpropertycontainer): 비동기적으로 가져올 수 있는 추가 속성의 로드를 허용하는 음악 항목을 위한 프로토콜입니다.
- [MusicRelationshipProperty](https://developer.apple.com/documentation/musickit/musicrelationshipproperty): 특정 루트 타입에서 결과 컬렉션의 요소에 대한 특정 값 타입으로 향하는 음악 항목 관계 속성의 식별자입니다.
- [MusicExtendedAttributeProperty](https://developer.apple.com/documentation/musickit/musicextendedattributeproperty): 특정 루트 타입에서 특정 결과 값 타입으로 향하는 음악 항목 확장 속성의 식별자입니다.
- [MusicAttributeProperty](https://developer.apple.com/documentation/musickit/musicattributeproperty): 특정 루트 타입에서 특정 결과 값 타입으로 향하는 음악 항목 속성의 식별자입니다.
- [PartialMusicAsyncProperty](https://developer.apple.com/documentation/musickit/partialmusicasyncproperty): 구체적인 루트 타입에서 임의의 결과 값 타입으로 비동기적으로 가져올 수 있는 음악 항목 속성의 부분적 타입 소거 식별자입니다.
- [PartialMusicProperty](https://developer.apple.com/documentation/musickit/partialmusicproperty): 구체적인 루트 타입에서 임의의 결과 값 타입으로 향하는 음악 항목 속성의 부분적 타입 소거 식별자입니다.
- [AnyMusicProperty](https://developer.apple.com/documentation/musickit/anymusicproperty): 임의의 루트 타입에서 임의의 결과 값 타입으로 향하는 음악 항목 속성의 타입 소거 식별자입니다.
:::

:::topic-grid
## 클래스
- [MusicLibrary](https://developer.apple.com/documentation/musickit/musiclibrary): 앱이 사용자의 음악 라이브러리에 접근할 때 사용하는 객체입니다.
:::

:::topic-grid
## 프로토콜
- [LibraryAlbumFilter](https://developer.apple.com/documentation/musickit/libraryalbumfilter): 앱이 라이브러리 요청의 필터로 사용하는 앨범 속성입니다.
- [LibraryAlbumSortProperties](https://developer.apple.com/documentation/musickit/libraryalbumsortproperties): 앱이 라이브러리 요청 결과를 정렬할 때 사용하는 앨범 속성입니다.
- [LibraryArtistFilter](https://developer.apple.com/documentation/musickit/libraryartistfilter): 앱이 라이브러리 요청의 필터로 사용하는 아티스트 속성입니다.
- [LibraryArtistSortProperties](https://developer.apple.com/documentation/musickit/libraryartistsortproperties): 앱이 라이브러리 요청 결과를 정렬할 때 사용하는 아티스트 속성입니다.
- [LibraryGenreFilter](https://developer.apple.com/documentation/musickit/librarygenrefilter): 앱이 라이브러리 요청의 필터로 사용하는 장르 속성입니다.
- [LibraryGenreSortProperties](https://developer.apple.com/documentation/musickit/librarygenresortproperties): 앱이 라이브러리 요청 결과를 정렬할 때 사용하는 장르 속성입니다.
- [LibraryMusicVideoFilter](https://developer.apple.com/documentation/musickit/librarymusicvideofilter): 앱이 라이브러리 요청의 필터로 사용하는 뮤직 비디오 속성입니다.
- [LibraryMusicVideoSortProperties](https://developer.apple.com/documentation/musickit/librarymusicvideosortproperties): 앱이 라이브러리 요청 결과를 정렬할 때 사용하는 뮤직 비디오 속성입니다.
- [LibraryPlaylistEntryFilter](https://developer.apple.com/documentation/musickit/libraryplaylistentryfilter): 앱이 라이브러리 요청의 필터로 사용하는 플레이리스트 항목 속성입니다.
- [LibraryPlaylistEntrySortProperties](https://developer.apple.com/documentation/musickit/libraryplaylistentrysortproperties): 앱이 라이브러리 요청 결과를 정렬할 때 사용하는 플레이리스트 항목 속성입니다.
- [LibraryPlaylistFilter](https://developer.apple.com/documentation/musickit/libraryplaylistfilter): 앱이 라이브러리 요청의 필터로 사용하는 플레이리스트 속성입니다.
- [LibraryPlaylistSortProperties](https://developer.apple.com/documentation/musickit/libraryplaylistsortproperties): 앱이 라이브러리 요청 결과를 정렬할 때 사용하는 플레이리스트 속성입니다.
- [LibrarySongFilter](https://developer.apple.com/documentation/musickit/librarysongfilter): 앱이 라이브러리 요청의 필터로 사용하는 곡 속성입니다.
- [LibrarySongSortProperties](https://developer.apple.com/documentation/musickit/librarysongsortproperties): 앱이 라이브러리 요청 결과를 정렬할 때 사용하는 곡 속성입니다.
- [LibraryTrackFilter](https://developer.apple.com/documentation/musickit/librarytrackfilter): 앱이 라이브러리 요청의 필터로 사용하는 트랙 속성입니다.
- [LibraryTrackSortProperties](https://developer.apple.com/documentation/musickit/librarytracksortproperties): 앱이 라이브러리 요청 결과를 정렬할 때 사용하는 트랙 속성입니다.
- [MusicCatalogChartRequestable](https://developer.apple.com/documentation/musickit/musiccatalogchartrequestable): 앱이 카탈로그 차트 요청을 사용해 가져올 수 있는 음악 항목을 위한 프로토콜입니다.
- [MusicCatalogTopLevelResourceRequesting](https://developer.apple.com/documentation/musickit/musiccatalogtoplevelresourcerequesting): 앱이 필터 없이 카탈로그 리소스 요청을 사용해 가져올 수 있는 음악 항목을 위한 프로토콜입니다.
- [MusicLibraryAddable](https://developer.apple.com/documentation/musickit/musiclibraryaddable): 앱이 음악 라이브러리에 추가할 수 있는 음악 항목을 위한 프로토콜입니다.
- [MusicLibraryRequestFilterValueEquatable](https://developer.apple.com/documentation/musickit/musiclibraryrequestfiltervalueequatable): 앱이 음악 라이브러리 요청으로 항목을 가져올 때 동등성 필터와 함께 사용할 수 있는 값 타입을 위한 프로토콜입니다.
- [MusicLibraryRequestFilterValueMembershipComparable](https://developer.apple.com/documentation/musickit/musiclibraryrequestfiltervaluemembershipcomparable): 앱이 음악 라이브러리 요청으로 항목을 가져올 때 멤버십 필터와 함께 사용할 수 있는 값 타입을 위한 프로토콜입니다.
- [MusicLibraryRequestable](https://developer.apple.com/documentation/musickit/musiclibraryrequestable): 앱이 라이브러리 요청을 사용해 가져올 수 있는 음악 항목을 위한 프로토콜입니다.
- [MusicLibrarySearchable](https://developer.apple.com/documentation/musickit/musiclibrarysearchable): 앱이 라이브러리 검색 요청을 사용해 가져올 수 있는 음악 항목을 위한 프로토콜입니다.
- [MusicLibrarySectionRequestable](https://developer.apple.com/documentation/musickit/musiclibrarysectionrequestable): 앱이 라이브러리 섹션화 요청으로 항목을 가져올 때 섹션으로 사용하는 타입을 위한 프로토콜입니다.
- [MusicPersonalRecommendationItem](https://developer.apple.com/documentation/musickit/musicpersonalrecommendationitem): 앱이 개인화 추천 요청을 사용해 가져올 수 있는 음악 항목을 위한 프로토콜입니다.
- [MusicPlaylistAddable](https://developer.apple.com/documentation/musickit/musicplaylistaddable): 앱이 플레이리스트에 추가할 수 있는 음악 항목을 위한 프로토콜입니다.
- [MusicRecentlyPlayedRequestable](https://developer.apple.com/documentation/musickit/musicrecentlyplayedrequestable): 앱이 최근 재생 요청을 사용해 가져올 수 있는 음악 항목을 위한 프로토콜입니다.
:::

:::topic-grid
## 구조체
- [MusicCatalogChart](https://developer.apple.com/documentation/musickit/musiccatalogchart): Apple Music 카탈로그의 인기 항목을 포함하는 객체입니다.
- [MusicCatalogChartsRequest](https://developer.apple.com/documentation/musickit/musiccatalogchartsrequest): 앱이 Apple Music 카탈로그에서 가장 인기 있는 항목을 가져오는 데 사용하는 요청입니다.
- [MusicCatalogChartsResponse](https://developer.apple.com/documentation/musickit/musiccatalogchartsresponse): 카탈로그 차트 요청의 결과를 포함하는 객체입니다.
- [MusicCatalogResourceRequestOption](https://developer.apple.com/documentation/musickit/musiccatalogresourcerequestoption): Apple Music 카탈로그에서 리소스를 요청할 때 사용하는 옵션입니다.
- [MusicCatalogSearchSuggestionsRequest](https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsrequest): 앱이 검색어를 사용해 Apple Music 카탈로그에서 제안을 가져오는 데 사용하는 요청입니다.
- [MusicCatalogSearchSuggestionsResponse](https://developer.apple.com/documentation/musickit/musiccatalogsearchsuggestionsresponse): 카탈로그 검색 제안 요청의 결과를 포함하는 객체입니다.
- [MusicLibraryRequest](https://developer.apple.com/documentation/musickit/musiclibraryrequest): 앱이 사용자의 음악 라이브러리에서 항목을 가져오는 데 사용하는 요청입니다.
- [MusicLibraryResponse](https://developer.apple.com/documentation/musickit/musiclibraryresponse): 라이브러리 요청의 결과를 포함하는 객체입니다.
- [MusicLibrarySearchRequest](https://developer.apple.com/documentation/musickit/musiclibrarysearchrequest): 앱이 검색어를 사용해 사용자의 라이브러리에서 항목을 가져오는 데 사용하는 요청입니다.
- [MusicLibrarySearchResponse](https://developer.apple.com/documentation/musickit/musiclibrarysearchresponse): 라이브러리 검색 요청의 결과를 포함하는 객체입니다.
- [MusicLibrarySection](https://developer.apple.com/documentation/musickit/musiclibrarysection): 라이브러리 섹션화 응답을 위한 섹션입니다.
- [MusicLibrarySectionedRequest](https://developer.apple.com/documentation/musickit/musiclibrarysectionedrequest): 앱이 사용자의 음악 라이브러리에서 섹션별로 묶인 항목을 가져오는 데 사용하는 요청입니다.
- [MusicLibrarySectionedResponse](https://developer.apple.com/documentation/musickit/musiclibrarysectionedresponse): 라이브러리 섹션화 요청의 결과를 포함하는 객체입니다.
- [MusicPersonalRecommendation](https://developer.apple.com/documentation/musickit/musicpersonalrecommendation): 사용자의 라이브러리와 청취 기록을 바탕으로 추천 항목을 포함하는 객체입니다.
- [MusicPersonalRecommendationsRequest](https://developer.apple.com/documentation/musickit/musicpersonalrecommendationsrequest): 앱이 사용자의 라이브러리와 청취 기록을 바탕으로 음악 추천을 가져오는 데 사용하는 요청입니다.
- [MusicPersonalRecommendationsResponse](https://developer.apple.com/documentation/musickit/musicpersonalrecommendationsresponse): 개인화 추천 요청의 결과를 포함하는 객체입니다.
- [MusicRecentlyPlayedRequest](https://developer.apple.com/documentation/musickit/musicrecentlyplayedrequest): 앱이 사용자가 최근에 재생한 항목을 가져오는 데 사용하는 요청입니다.
- [MusicRecentlyPlayedResponse](https://developer.apple.com/documentation/musickit/musicrecentlyplayedresponse): 사용자가 최근에 재생한 항목을 포함하는 객체입니다.
- [TitledSection](https://developer.apple.com/documentation/musickit/titledsection): 제목별로 묶인 라이브러리 항목을 요청할 때 사용할 수 있는 섹션입니다.
:::

:::topic-grid
## 타입 별칭
- [MusicRecentlyPlayedContainerRequest](https://developer.apple.com/documentation/musickit/musicrecentlyplayedcontainerrequest): 앱이 사용자가 최근에 재생한 앨범, 플레이리스트 또는 스테이션을 가져오는 데 사용하는 요청입니다.
- [MusicRecentlyPlayedContainerResponse](https://developer.apple.com/documentation/musickit/musicrecentlyplayedcontainerresponse): 사용자가 최근에 재생한 앨범, 플레이리스트 또는 스테이션을 포함하는 객체입니다.
:::

:::topic-grid
## 열거형
- [AudioVariant](https://developer.apple.com/documentation/musickit/audiovariant): 항목에서 이용 가능한 오디오 품질을 나타내는 변형입니다.
- [MusicCatalogChartKind](https://developer.apple.com/documentation/musickit/musiccatalogchartkind): 사용 가능한 카탈로그 차트 종류입니다.
- [MusicPropertySource](https://developer.apple.com/documentation/musickit/musicpropertysource): 속성과 관계를 요청할 때 사용할 소스를 지정하는 열거형입니다.
- [RecentlyPlayedMusicItem](https://developer.apple.com/documentation/musickit/recentlyplayedmusicitem): 사용자가 최근에 재생한 앨범, 플레이리스트 또는 스테이션을 나타내는 항목입니다.
:::
