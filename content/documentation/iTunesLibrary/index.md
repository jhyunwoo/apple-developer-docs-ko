---
route: /documentation/iTunesLibrary
source_url: https://developer.apple.com/documentation/iTunesLibrary
source_locale: en-US
section: docc
content_type: symbol
title: iTunes Library
original_title: iTunes Library
source_hash: 6eb4376a240627f6a2337efe70385bf3a1ec110cd62a593d43ddae09643eff34
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:24:07+00:00'
last_translated_at: '2026-03-14T01:12:00+09:00'
---

# iTunes Library

사용자의 iTunes 보관함에 있는 미디어의 속성을 가져옵니다.

## 개요

이 프레임워크를 사용하면 트랙과 플레이리스트 메타데이터 같은 미디어 정보를 사용자의 iTunes XML 파일에 질의하지 않고 직접 iTunes 보관함에서 가져올 수 있습니다.

이 프레임워크를 사용하려면 [libraryWithAPIVersion:error:](https://developer.apple.com/documentation/ituneslibrary/itlibrary/librarywithapiversion:error:) 클래스 메서드를 호출해 [ITLibrary](https://developer.apple.com/documentation/ituneslibrary/itlibrary) 객체를 생성합니다. 반환된 인스턴스를 조회하여 해당 객체의 속성과 미디어 항목의 속성을 얻을 수 있습니다. 예를 들면 다음과 같습니다.

:::important 중요
이 프레임워크로 정보를 가져오려면 앱에 코드 서명이 되어 있어야 하며, iTunes 보관함 접근은 읽기 전용입니다. 이 프레임워크는 iTunes 11 이상 사용자에게 제공됩니다.
:::

:::topic-grid
## 핵심 사항
- [ITLibrary](https://developer.apple.com/documentation/ituneslibrary/itlibrary): iTunesLibrary 프레임워크의 진입점 역할을 하는 클래스입니다.
:::

:::topic-grid
## 앨범 및 플레이리스트
- [ITLibAlbum](https://developer.apple.com/documentation/ituneslibrary/itlibalbum): iTunes 보관함의 앨범 정보를 제공하는 클래스입니다.
- [ITLibPlaylist](https://developer.apple.com/documentation/ituneslibrary/itlibplaylist): iTunes 보관함의 플레이리스트를 설명하는 클래스입니다.
:::

:::topic-grid
## 미디어 항목
- [ITLibMediaItem](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitem): 노래, 비디오, 팟캐스트 등 iTunes 보관함의 미디어 항목(트랙)을 설명하는 클래스입니다.
- [ITLibMediaEntity](https://developer.apple.com/documentation/ituneslibrary/itlibmediaentity): 오디오 트랙과 같은 미디어 항목이 될 수 있는 media entity를 설명하는 클래스입니다.
- [ITLibArtist](https://developer.apple.com/documentation/ituneslibrary/itlibartist): 노래의 연주자와 같은 아티스트를 나타내는 클래스입니다.
- [ITLibArtwork](https://developer.apple.com/documentation/ituneslibrary/itlibartwork): 미디어 항목의 artwork를 나타내는 클래스입니다.
- [ITLibMediaItemVideoInfo](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitemvideoinfo): 비디오 미디어 항목의 비디오 정보를 캡슐화하는 클래스입니다.
:::

:::topic-grid
## 구조체
- [DidChangeLibraryMessage](https://developer.apple.com/documentation/ituneslibrary/didchangelibrarymessage)
:::
