---
route: /documentation/MediaPlayer
source_url: https://developer.apple.com/documentation/MediaPlayer
source_locale: en-US
section: docc
content_type: symbol
title: Media Player
original_title: Media Player
source_hash: 57f0a13f59beb4c3205b46979046f5ac375a745e34c0c8ed43a17cf78d3db1ef
canonical_source: manual-translation
last_crawled_at: '2026-03-13T05:17:57+00:00'
last_translated_at: '2026-03-13T05:17:57+00:00'
---

# Media Player

앱 안에서 노래, 오디오 팟캐스트, 오디오북 등을 찾고 재생합니다.

## 개요

[MusicKit](https://developer.apple.com/musickit/)의 일부인 Media Player 프레임워크를 사용하여 앱에서 사용자의 미디어 재생을 제어하세요. 앱에 음악이 포함되어 있다면, 이 프레임워크를 사용해 사용자의 라이브러리에서 노래, 팟캐스트, 책 같은 오디오 콘텐츠를 검색할 수 있습니다. 그런 다음 해당 콘텐츠를 직접 재생하거나 시스템 Music 앱에 재생을 요청할 수 있습니다. 예를 들어 게임은 사용자가 특정 게임 레벨을 진행하는 동안 자신의 음악을 재생할 수 있는 옵션을 제공할 수 있습니다.

:::important Important
사용자 개인정보를 보호하기 위해서는 앱이 사용자의 미디어 라이브러리에 접근할 수 있도록 사용자의 허가를 받아야 합니다. 앱의 `Info.plist` 파일에 [NSAppleMusicUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) 키를 추가하고, 사용자의 라이브러리를 어떻게 사용할지에 대한 설명을 포함하세요. 이 키가 없으면 시스템은 앱이 사용자의 라이브러리에 접근하려고 할 때 앱을 종료합니다.
:::

Media Player 프레임워크를 사용해 사용자의 라이브러리에 있는 콘텐츠를 재생하려면, 내장된 [MPMusicPlayerController](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller) 객체 중 하나를 사용합니다:

- *애플리케이션 플레이어*는 앱 안에서 로컬로 음악을 재생합니다. 사용자에게 재생하는 오디오를 더 세밀하게 제어하고 싶을 때 이 플레이어를 사용하세요. 이 플레이어는 내장된 Music 앱의 상태를 바꾸지 않습니다.
- *시스템 플레이어*는 사용자를 대신해 Music 앱을 사용하여 오디오를 재생합니다. 사용자가 앱을 벗어나도 오디오가 계속 재생되기를 원할 때 이 플레이어를 사용하세요.

미디어 쿼리를 사용해 재생하려는 항목을 가져오고, 선택한 미디어 플레이어의 큐를 채우세요. 사용자가 앱에 자신의 Apple Music 계정 접근 권한을 부여하면, 앱은 노래를 추가하고, 플레이리스트를 만들고, Apple Music의 노래를 재생할 수 있습니다. 앱이 사용자가 Apple Music 구독자가 아니라는 점을 감지하면 체험판을 제안할 수 있습니다.

Media Player 프레임워크를 사용해서는 비디오 미디어 항목을 직접 재생할 수 없습니다. [MPMediaItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem) 객체를 포함하는 비디오를 재생하려면 [AVFoundation](https://developer.apple.com/documentation/AVFoundation)의 [AVPlayer](https://developer.apple.com/documentation/AVFoundation/AVPlayer) 객체를 사용하세요. 시스템 플레이어 역시 시스템 앱을 사용해 비디오 항목을 재생하는 방법을 제공합니다.

:::important Important
이 프레임워크는 앱 안에서 사용자의 오디오 콘텐츠 재생을 지원하는 용도로만 사용하세요. 다른 목적을 위해 사용자의 오디오 콘텐츠 정보를 수집해서는 안 됩니다. Apple Music 콘텐츠 접근에 대한 자세한 내용은 [App Store review guidelines](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services)를 참고하세요.
:::

:::topic-grid
## 핵심
- [NSAppleMusicUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription): 앱이 미디어 라이브러리에 접근 권한을 요청하는 이유를 알려 주는 메시지입니다.
:::

:::topic-grid
## 내장 음악 재생
- [Playing audio using the built-in music player](https://developer.apple.com/documentation/mediaplayer/playing-audio-using-the-built-in-music-player): 앱 안에 미디어 플레이어를 만들어 사용자의 미디어 라이브러리에 있는 오디오를 재생합니다.
- [MPMusicPlayerController](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller): 기기의 Music 앱 라이브러리에 있는 오디오 미디어 항목을 재생하는 객체입니다.
- [MPMediaPlayback](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback): 오디오 미디어 재생을 제어하기 위한 인터페이스를 정의하는 프로토콜입니다.
- [MPSystemMusicPlayerController](https://developer.apple.com/documentation/mediaplayer/mpsystemmusicplayercontroller): Music 앱에서 비디오를 재생하기 위한 프로토콜입니다.
:::

:::topic-grid
## 미디어 라이브러리 동기화
- [MPMediaLibrary](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary): 기기에서 동기화된 미디어 항목의 상태를 나타내는 객체입니다.
:::

:::topic-grid
## 미디어 항목 쿼리
- [Using filters to create specialized queries](https://developer.apple.com/documentation/mediaplayer/using-filters-to-create-specialized-queries): 음악 플레이어 큐를 채우기 전에 쿼리에 필터 집합을 추가합니다.
- [MPMediaQuery](https://developer.apple.com/documentation/mediaplayer/mpmediaquery): 필터와 그룹화 유형을 사용해 기기의 미디어 라이브러리에서 미디어 항목 집합을 지정하는 쿼리입니다.
- [MPMediaQuerySection](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection): 미디어 쿼리 안에 있는 미디어 항목 또는 미디어 항목 컬렉션의 범위입니다.
- [MPMediaPropertyPredicate](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate): 미디어 쿼리의 필터를 정의하기 위한 조건 집합입니다.
- [MPMediaPredicate](https://developer.apple.com/documentation/mediaplayer/mpmediapredicate): 미디어 쿼리에서 미디어를 필터링하는 클래스를 정의하는 추상 클래스입니다.
:::

:::topic-grid
## 미디어 플레이어 큐
- [MPMusicPlayerControllerQueue](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollerqueue): 재생할 미디어 항목을 담은 변경 불가능한 큐입니다.
- [MPMusicPlayerControllerMutableQueue](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollermutablequeue): 재생할 미디어 항목을 담은 변경 가능한 큐입니다.
- [MPMusicPlayerApplicationController](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerapplicationcontroller): 현재 재생 중인 큐를 수정할 때 사용하는 미디어 플레이어 객체입니다.
- [MPMusicPlayerMediaItemQueueDescriptor](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor): 플레이어의 미디어 큐 안에 있는 오디오 미디어 항목을 수정하기 위한 속성과 메서드 집합입니다.
- [MPMusicPlayerStoreQueueDescriptor](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor): 플레이어 큐 안의 항목을 store 식별자를 기준으로 수정하기 위한 속성과 메서드 집합입니다.
- [MPMusicPlayerPlayParametersQueueDescriptor](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparametersqueuedescriptor): 프레임워크가 반환하는 재생 매개변수를 기준으로 항목 재생 방식을 수정하기 위한 속성과 메서드 집합입니다.
- [MPMusicPlayerQueueDescriptor](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerqueuedescriptor): 오디오 미디어 항목 큐 설명자와 스토어 큐 설명자를 위한 추상 기본 클래스입니다.
:::

:::topic-grid
## 미디어 항목 및 플레이리스트
- [Providing animated artwork for media items](https://developer.apple.com/documentation/mediaplayer/providing-animated-artwork-for-media-items): 지금 재생 중 정보에 비디오 에셋을 제공하여 잠금 화면 같은 시스템 뷰에 앱 미디어의 애니메이션 아트워크를 표시합니다.
- [MPMediaItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem): 미디어 라이브러리의 단일 항목을 나타내는 속성 집합입니다.
- [MPMediaItemArtwork](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork): 음악 앨범 커버 아트처럼 미디어 항목과 연결된 그래픽 이미지입니다.
- [MPMediaItemAnimatedArtwork](https://developer.apple.com/documentation/mediaplayer/mpmediaitemanimatedartwork): 애니메이션 음악 앨범 커버 아트처럼 미디어 항목용 애니메이션 이미지입니다.
- [MPMediaItemCollection](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection): 미디어 라이브러리의 정렬된 미디어 항목 집합입니다.
- [MPMediaPlaylist](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist): 관련된 미디어 항목으로 구성된 재생 가능한 컬렉션입니다.
- [MPMediaPlaylistCreationMetadata](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata): 플레이리스트를 생성할 때 설명에 사용하는 속성 집합입니다.
- [MPMediaEntity](https://developer.apple.com/documentation/mediaplayer/mpmediaentity): 미디어 항목, 미디어 항목 컬렉션, 미디어 플레이리스트 인스턴스를 위한 추상 슈퍼클래스입니다.
:::

:::topic-grid
## 미디어 플레이어 사용자 인터페이스
- [Displaying a media picker from your app](https://developer.apple.com/documentation/mediaplayer/displaying-a-media-picker-from-your-app): 앱 안에서 미디어 선택기 인터페이스를 표시해 사용자가 재생할 음악을 선택할 수 있게 합니다.
- [MPMediaPickerController](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller): 미디어 항목을 선택하기 위한 그래픽 인터페이스를 제공하는 특수한 뷰 컨트롤러입니다.
- [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview): 시스템 오디오 출력 볼륨을 설정하는 슬라이더 컨트롤과 오디오 출력 경로를 선택하는 버튼입니다.
:::

:::topic-grid
## 지금 재생 중 정보
- [Becoming a now playable app](https://developer.apple.com/documentation/mediaplayer/becoming-a-now-playable-app): 지금 재생 중 정보 제공과 remote command center 동작 등록을 위한 모범 사례를 채택하여 앱이 Now Playing 앱이 될 수 있도록 합니다.
- [MPNowPlayingSession](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession): 여러 플레이어에 대한 Now Playing 정보와 원격 명령을 관리하는 객체입니다.
- [MPNowPlayingInfoCenter](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter): 앱이 재생하는 미디어의 Now Playing 정보를 설정하기 위한 객체입니다.
- [MPNowPlayingInfoLanguageOption](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption): Now Playing 항목의 언어 옵션을 설정하기 위한 인터페이스 집합입니다.
- [MPNowPlayingInfoLanguageOptionGroup](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup): 한 번에 하나의 언어 옵션만 활성화할 수 있는 언어 옵션 그룹입니다.
- [Language option characteristic constants](https://developer.apple.com/documentation/mediaplayer/language-option-characteristic-constants): 언어 특성을 정의하기 위한 상수입니다.
:::

:::topic-grid
## 외부 플레이어 및 시스템 이벤트 처리
- [Handling external player events notifications](https://developer.apple.com/documentation/mediaplayer/handling-external-player-events-notifications): 외부 미디어 플레이어의 이벤트를 처리합니다.
- [Remote command center events](https://developer.apple.com/documentation/mediaplayer/remote-command-center-events): 미디어 플레이어 이벤트를 처리하도록 remote command center를 설정합니다.
- [Track navigation events](https://developer.apple.com/documentation/mediaplayer/track-navigation-events): 미디어 항목의 어느 부분을 재생할지 변경해 달라는 요청에 응답합니다.
- [Media playback mode events](https://developer.apple.com/documentation/mediaplayer/media-playback-mode-events): 미디어 항목 재생 방식의 변경에 응답합니다.
- [Feedback and rating events](https://developer.apple.com/documentation/mediaplayer/feedback-and-rating-events): 들어오는 피드백 및 평가 이벤트에 응답합니다.
:::

:::topic-grid
## 외부 미디어 플레이어 항목
- [MPContentItem](https://developer.apple.com/documentation/mediaplayer/mpcontentitem): 표시되는 미디어 항목의 정보를 담는 객체입니다.
:::

:::topic-grid
## 미디어 플레이어 오류
- [MPError](https://developer.apple.com/documentation/mediaplayer/mperror): 프레임워크 오류를 나타내는 구조체입니다.
:::

:::topic-grid
## 지원 중단됨
- [Deprecated types](https://developer.apple.com/documentation/mediaplayer/deprecated-types): 지원 중단된 심벌을 검토하고 앱에서 사용을 피하세요.
:::
