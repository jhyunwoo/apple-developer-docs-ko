---
route: /documentation/AppleMusicFeed
source_url: https://developer.apple.com/documentation/AppleMusicFeed
source_locale: en-US
section: docc
content_type: symbol
title: Apple Music Feed
original_title: Apple Music Feed
source_hash: 7e602460a2e9a376db4b2d37c86a991da244879cd50e6e6715ba98a4a011884c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:19:45+00:00'
last_translated_at: '2026-03-13T19:40:00+09:00'
---

# Apple Music Feed

Apple Music Catalog의 콘텐츠에 대량으로 접근합니다.

## 개요

Apple Music Feed는 피드 내보내기 형태로 소비할 수 있도록 Apple Music 제품의 카탈로그 콘텐츠를 대량으로 제공합니다. 이러한 대량 내보내기는 온라인 사용에 가장 적합한 Apple Music API를 보완하는 오프라인 사용 사례에 적합합니다. Apple Music Feed에는 앨범, 노래, 아티스트, 인기 차트에 대한 콘텐츠 메타데이터가 포함되며 24시간마다 전체 새로 고침이 이루어집니다. 데이터 세트의 [Requesting a feed export](https://developer.apple.com/documentation/applemusicfeed/requesting-a-feed-export)를 위해 Apple Media Feed API를 사용하여 Apple Music Feed에 접근합니다.

:::important 중요
Apple Music Feed와 Apple Music Feed를 통해 접근한 모든 콘텐츠 및 데이터는 앱 내에서 Apple Music 콘텐츠를 공개적으로 홍보하는 목적에 한해서만 사용할 수 있습니다. Apple Music Feed를 다른 어떤 목적으로든 사용하는 것은 엄격히 금지됩니다. 여기에는 내부 시스템 및 도구를 구동하거나 향상하는 행위, 제3자와 데이터를 공유하는 행위, 앱에서 Apple Music을 홍보하는 목적 이외의 이유로 음악 및 아티스트 관련 정보를 분석하는 행위가 포함되지만 이에 국한되지 않습니다.
:::

원시 데이터와 이 문서의 정보를 활용하면 Apple Music Feed를 다양한 방식으로 사용할 수 있습니다. 예를 들어 Apple Music용 discovery engine을 구축하려는 경우, 팀은 데이터를 검토하고 그러한 엔진을 제공하기 위한 endpoint 요청을 결정할 수 있습니다.

Apple Music Feed는 Parquet 포맷을 사용합니다. Parquet은 대규모 데이터 세트의 저장과 처리를 최적화하는 오픈 소스 컬럼형 저장 파일 포맷입니다. Parquet 포맷은 선택적으로 데이터를 읽거나 처리해야 하는 시나리오에서 쿼리 성능을 향상하고 저장 비용을 줄입니다. 이는 데이터를 열 단위로 구성하고 각 열의 값을 함께 저장함으로써 가능하며, 각 열에 특화된 효율적인 압축 및 인코딩 기법을 적용할 수 있게 합니다. Hadoop과 Spark 같은 많은 대규모 데이터 처리 프레임워크가 이 포맷을 사용합니다.

:::note 참고
피드는 Parquet 포맷이지만, 이 문서에서는 설명 목적상 데이터 예시를 JSON 포맷으로 제공합니다.
:::

## 샘플 스크립트 사용

[music-feed-examples](https://github.com/apple/music-feed-examples) 공개 GitHub 저장소에서 다음 단계를 수행하는 Java 및 Python 샘플 스크립트를 찾을 수 있습니다.

- developer token을 생성합니다.
- 이 토큰을 사용해 특정 데이터 세트의 최신 feed export에 대한 메타데이터를 요청합니다.
- 이 토큰을 사용해 feed export의 데이터 부분들에 대한 링크를 요청합니다.
- 지정한 출력 디렉터리로 feed 데이터를 다운로드합니다.
- Parquet 데이터 파일을 로드하고 간단한 쿼리를 실행합니다.

:::topic-grid
## 핵심 사항
- [Generating developer tokens](https://developer.apple.com/documentation/applemusicfeed/generating-developer-tokens): Apple Media Feed API 요청을 인증하기 위한 JSON Web Token을 생성합니다.
- [Requesting a feed export](https://developer.apple.com/documentation/applemusicfeed/requesting-a-feed-export): Apple Music Catalog 메타데이터에 대한 요청을 생성합니다.
- [Interpreting responses](https://developer.apple.com/documentation/applemusicfeed/interpreting-responses): Apple Music Feed 요청에 대한 Apple Media Feed API 응답을 이해합니다.
:::

:::topic-grid
## 객체
- [Album](https://developer.apple.com/documentation/applemusicfeed/album): Album 리소스를 나타내는 데이터 구조입니다.
- [Song](https://developer.apple.com/documentation/applemusicfeed/song): Song 리소스를 나타내는 데이터 구조입니다.
- [Artist](https://developer.apple.com/documentation/applemusicfeed/artist): Artist 리소스를 나타내는 데이터 구조입니다.
- [PopularityTopChartAlbums](https://developer.apple.com/documentation/applemusicfeed/popularitytopchartalbums): 앨범 인기 차트 리소스를 나타내는 데이터 구조입니다.
- [PopularityTopChartSongs](https://developer.apple.com/documentation/applemusicfeed/popularitytopchartsongs): 노래 인기 차트 리소스를 나타내는 데이터 구조입니다.
:::
