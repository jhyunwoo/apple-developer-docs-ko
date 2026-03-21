---
route: /documentation/ShazamKit
source_url: https://developer.apple.com/documentation/ShazamKit
source_locale: en-US
section: docc
content_type: symbol
title: ShazamKit
original_title: ShazamKit
source_hash: 853306f536e857168556305eb1346dfdbc8295deac567e1197f2df9fd9737bad
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:23:48+00:00'
last_translated_at: '2026-03-13T23:24:01+09:00'
---

# ShazamKit

Shazam 카탈로그 또는 사용자 정의 카탈로그에 있는 오디오 녹음의 일부가 캡처된 소리에 포함되어 있을 때, 그 특정 녹음에 대한 정보를 찾습니다.

## 개요

ShazamKit은 오디오 녹음의 고유한 음향 *signature*를 사용해 일치 항목을 찾습니다. 이 signature는 오디오 신호 에너지의 시간-주파수 분포를 포착하며, 원본 오디오보다 훨씬 작습니다. 또한 일방향 변환이기 때문에 signature를 다시 녹음본으로 되돌릴 수는 없습니다.

ShazamKit은 검색 가능한 전체 오디오 녹음 각각에 대해 *reference signature*를 생성합니다. *catalog*는 reference signature와 그에 연결된 메타데이터, 즉 *media item*을 저장합니다.

일치 항목 검색은, 캡처된 오디오로부터 ShazamKit이 생성한 *query signature*를 catalog 안의 reference signature와 비교하는 방식으로 이루어집니다. query signature가 reference signature의 일부와 충분히 일치하면 매치가 발생합니다. 식당에서 흘러나오는 배경 음악의 일부를 녹음한 것처럼 캡처된 오디오가 시끄럽더라도 매치는 일어날 수 있습니다.

아래 그림은 query signature가 catalog 안의 reference signature와 일치하는 모습을 보여 줍니다. 일치 결과 정보에는 query가 시작되는 시점과 일치하는 reference 녹음의 timecode가 포함됩니다.

![특정 시점에서 query signature가 reference signature와 일치하는 모습을 보여 주는 스펙트로그램입니다.](https://developer.apple.com)

예를 들어 Shazam 앱은 기기 마이크의 사운드 스트림을 query signature로 변환한 뒤 Shazam 음악 카탈로그에서 매치를 검색합니다. 이 매치에는 노래 제목, 아티스트 이름, 기타 세부 정보 같은 reference signature의 메타데이터가 포함됩니다.

자신만의 reference signature와 관련 메타데이터를 사용해 사용자 정의 catalog를 만들 수도 있습니다. 예를 들어 가상 학습 앱의 catalog에는 강의 비디오용 reference signature와 질문의 timecode를 포함한 메타데이터가 들어갈 수 있습니다. ShazamKit을 사용하면 앱은 매치의 timecode를 바탕으로 현재 질문을 식별하고 가능한 답안을 제시할 수 있습니다. 학생이 비디오를 앞으로 넘기거나 뒤로 되감으면, 앱은 학생이 보고 있는 사운드에 맞춰 내용을 업데이트합니다.

:::topic-grid
## 오디오 매칭
- [SHSession](https://developer.apple.com/documentation/shazamkit/shsession): 특정 오디오 녹음의 일부가 Shazam 카탈로그 또는 사용자 정의 카탈로그의 캡처된 소리에 포함될 때 그 녹음을 매칭하는 객체입니다.
- [SHManagedSession](https://developer.apple.com/documentation/shazamkit/shmanagedsession): 캡처된 소리와 Shazam 카탈로그 또는 사용자 정의 카탈로그를 비교하기 위해 녹음하고 매칭하는 객체입니다.
- [SHSessionDelegate](https://developer.apple.com/documentation/shazamkit/shsessiondelegate): 세션이 매치 요청 결과를 전달할 때 호출하는 메서드입니다.
- [SHMatch](https://developer.apple.com/documentation/shazamkit/shmatch): query와 일치하는 catalog media item을 나타내는 객체입니다.
- [SHMatchedMediaItem](https://developer.apple.com/documentation/shazamkit/shmatchedmediaitem): 일치한 reference signature의 메타데이터를 나타내는 객체입니다.
- [SHMediaItem](https://developer.apple.com/documentation/shazamkit/shmediaitem): reference signature의 메타데이터를 나타내는 객체입니다.
:::

:::topic-grid
## 오디오에서 signature 만들기
- [SHSignature](https://developer.apple.com/documentation/shazamkit/shsignature): signature의 불투명 데이터와 기타 정보를 담는 객체입니다.
- [SHSignatureGenerator](https://developer.apple.com/documentation/shazamkit/shsignaturegenerator): 오디오 데이터를 signature로 변환하는 객체입니다.
:::

:::topic-grid
## 사용자 정의 오디오 카탈로그 만들기
- [Building a Custom Catalog and Matching Audio](https://developer.apple.com/documentation/shazamkit/building-a-custom-catalog-and-matching-audio): 오디오를 사용자 정의 reference signature 및 관련 메타데이터와 매칭해 학습 비디오와 동기화된 수업 콘텐츠를 표시합니다.
- [ShazamKit Dance Finder with Managed Session](https://developer.apple.com/documentation/shazamkit/shazamkit-dance-finder-with-managed-session): 오디오를 사용자 정의 카탈로그와 매칭해 특정 곡의 춤 동영상을 찾고, 인식한 노래의 기록을 보여 줍니다.
- [SHCustomCatalog](https://developer.apple.com/documentation/shazamkit/shcustomcatalog): 사용자 정의 오디오 녹음의 reference signature와 관련 메타데이터를 저장하는 객체입니다.
- [SHCatalog](https://developer.apple.com/documentation/shazamkit/shcatalog): reference signature와 관련 메타데이터를 저장하는 추상 기반 클래스입니다.
:::

:::topic-grid
## 사용자의 Shazam 라이브러리 업데이트
- [SHLibrary](https://developer.apple.com/documentation/shazamkit/shlibrary): 사용자의 동기화된 Shazam 라이브러리를 나타내는 객체입니다.
- [SHMediaLibrary](https://developer.apple.com/documentation/shazamkit/shmedialibrary): 사용자의 Shazam 라이브러리를 나타내는 객체입니다.
:::

:::topic-grid
## Shazam 오류
- [SHError](https://developer.apple.com/documentation/shazamkit/sherror): catalog, 매치 시도, signature의 문제를 나타내거나 사용자의 Shazam 라이브러리에 저장할 때 시스템 또는 앱이 생성하는 오류 타입입니다.
:::

:::topic-grid
## 참고 자료
- [ShazamKit Enumerations](https://developer.apple.com/documentation/shazamkit/shazamkit-enumerations)
- [ShazamKit Constants](https://developer.apple.com/documentation/shazamkit/shazamkit-constants)
:::
