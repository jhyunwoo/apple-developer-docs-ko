---
route: /documentation/SiriKitCloudMedia
source_url: https://developer.apple.com/documentation/SiriKitCloudMedia
source_locale: en-US
section: docc
content_type: symbol
title: SiriKit Cloud Media
original_title: SiriKit Cloud Media
source_hash: 8925772934186c08cdbfde96b446eebf9ace71bdba05e925055bd44dc440b3a8
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:14:56+00:00'
last_translated_at: '2026-03-13T16:55:00+09:00'
---

# SiriKit Cloud Media

미디어 서비스에서 직접 HomePod 스피커로 음악을 스트리밍합니다.

## 개요

사용자가 권한이 부여된 HomePod 스피커에 어떤 미디어를 재생해 달라고 요청하면, 미디어 장치는 중간의 iOS 기기를 거치지 않고 직접 `SiriKitCloudMedia` 서비스에 연락할 수 있습니다.

SiriKit Cloud Media [OpenAPI Specification](https://developer.apple.com/sample-code/siri/sirikit-cloud-media-open-api.zip)을 다운로드하십시오. HomePod용 SiriKit Media Intents 프로그램 신청에 대한 자세한 내용은 [Siri for Developers](https://developer.apple.com/siri)의 HomePod 절을 참고하십시오.

### 사용자의 HomePod 구성

iOS 앱에서 [Media Setup](https://developer.apple.com/documentation/MediaSetup)을 채택하고 OAuth 서비스에서 토큰을 제공하여 HomePod 스피커가 미디어 서비스에 연락할 수 있도록 승인합니다. 사용자가 집 안의 기기들에 대해 서비스를 활성화한 뒤에는 Home 앱에서 접근을 관리할 수 있습니다.

구성 엔드포인트를 구현하여 HomePod 스피커에 서비스로 요청을 보내는 방법에 대한 세부 정보를 제공합니다. 지원하는 엔드포인트의 경로와 필수 헤더를 포함하십시오. 자세한 내용은 [Configure Your Service Endpoints](https://developer.apple.com/documentation/sirikitcloudmedia/configuration-resource)를 참고하십시오.

:::note Note
하나의 세션 동안 일부 요청은 사용자의 집 안에 있는 다른 HomePod 스피커 또는 Apple TV에서 올 수 있습니다. 이 요청에도 하나의 장치가 모든 요청을 보내는 경우와 동일하게 응답하십시오. 연속성을 유지하려면 [Session](https://developer.apple.com/documentation/sirikitcloudmedia/session) 객체를 사용하십시오.
:::

### 미디어 재생 큐로 Siri intent에 응답

[Process a Play Media Intent](https://developer.apple.com/documentation/sirikitcloudmedia/playmedia-1g2o9) 엔드포인트를 구현해 사용자의 요청을 수신하고, 재생하려는 미디어를 해석하며, intent를 처리합니다. [UserActivity](https://developer.apple.com/documentation/sirikitcloudmedia/useractivity)로 응답하면, 클라이언트는 이를 사용해 [Get a Media Queue](https://developer.apple.com/documentation/sirikitcloudmedia/playmedia-1onzj) 엔드포인트에서 미디어 [Content](https://developer.apple.com/documentation/sirikitcloudmedia/content)의 [Queue](https://developer.apple.com/documentation/sirikitcloudmedia/queue)를 요청합니다.

각 큐에 포함하는 [PlayMediaControl](https://developer.apple.com/documentation/sirikitcloudmedia/playmediacontrol)을 사용해 사용자가 큐에서 콘텐츠를 얼마나 자주 건너뛸 수 있는지, 각 콘텐츠에 어떤 재생 제어를 제공할지를 관리합니다. [Report Playback Progress and Activity](https://developer.apple.com/documentation/sirikitcloudmedia/updateactivity) 엔드포인트에 주기적으로 업데이트를 보내 사용자의 상호 작용과 재생 진행 상태를 모니터링합니다. 선택적으로 [Report Playback Progress and Activity](https://developer.apple.com/documentation/sirikitcloudmedia/updateactivity) 요청에 응답하면서 현재 재생 큐를 교체하거나 수정할 큐 세그먼트를 반환할 수도 있습니다.

### 사용자의 취향에 맞추기

[Process an Add Media Intent](https://developer.apple.com/documentation/sirikitcloudmedia/addmedia) 엔드포인트를 사용해 사용자가 자신의 라이브러리와 재생목록을 사용자화할 수 있게 하십시오. 사용자는 Siri에게 특정 아티스트의 최신 앨범을 라이브러리에 추가해 달라고 하거나, 현재 재생 중인 노래를 Karaoke Practice 재생목록에 추가해 달라고 요청할 수 있습니다.

[Process an Update Media Affinity Intent](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinity) intent로 사용자가 공유한 선호도를 반영해 알고리즘 기반 재생목록을 조정할 수도 있습니다. 예를 들어 사용자가 “I like rock-and-roll”이라고 말하면 다음번에 음악 재생을 요청할 때 그 장르의 곡을 더 많이 포함할 수 있습니다. 또는 “I don’t like this song”이라고 말하면 현재 재생 중인 곡을 이후 추천에서 제외할 수 있습니다.

:::topic-grid
## 기기 구성
- [Configure Your Service Endpoints](https://developer.apple.com/documentation/sirikitcloudmedia/configuration-resource): HomePod 스피커 또는 Apple TV에 미디어 서버 엔드포인트의 구성 세부 정보를 제공합니다.
- [ExtensionConfigTag](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfigtag): 특정 미디어 서비스 구성에 대한 고유 식별자입니다.
- [ExtensionConfig](https://developer.apple.com/documentation/sirikitcloudmedia/extensionconfig): 미디어 서비스 엔드포인트에 접근하기 위한 지침입니다.
- [PlayMediaControlActivity](https://developer.apple.com/documentation/sirikitcloudmedia/playmediacontrolactivity): 재생 진행 상황 보고를 위한 옵션입니다.
:::

:::topic-grid
## 미디어 재생 큐
- [Process a Play Media Intent](https://developer.apple.com/documentation/sirikitcloudmedia/playmedia-1g2o9): 사용자의 미디어 재생 요청을 해석하고, 해당 재생 큐에 접근하는 지침을 제공합니다.
- [Get a Media Queue](https://developer.apple.com/documentation/sirikitcloudmedia/playmedia-1onzj): 성공적으로 처리된 play media intent로부터 재생 큐를 제공합니다.
:::

:::topic-grid
## 콘텐츠 보호
- [Retrieve an Asset’s Content Protection Key](https://developer.apple.com/documentation/sirikitcloudmedia/contentprotectionkey): 특정 보호 자산의 콘텐츠 키를 제공합니다.
- [ContentProtectionKeyRequest](https://developer.apple.com/documentation/sirikitcloudmedia/contentprotectionkeyrequest): 항목의 콘텐츠 보호 키에 대한 요청입니다.
- [ContentProtectionKeyResponse](https://developer.apple.com/documentation/sirikitcloudmedia/contentprotectionkeyresponse): 항목의 콘텐츠 보호 키 요청에 대한 응답입니다.
- [ContentProtectionKeySystem](https://developer.apple.com/documentation/sirikitcloudmedia/contentprotectionkeysystem): SiriKit Cloud Media가 지원하는 콘텐츠 보호 키 시스템입니다.
:::

:::topic-grid
## 재생 이벤트
- [QueueActivityReportEvent](https://developer.apple.com/documentation/sirikitcloudmedia/queueactivityreportevent): 콘텐츠 재생 중 발생하는 이벤트입니다.
- [Report Playback Progress and Activity](https://developer.apple.com/documentation/sirikitcloudmedia/updateactivity): 재생 큐에서의 진행 상태를 모니터링합니다.
- [UpdateActivityRequest](https://developer.apple.com/documentation/sirikitcloudmedia/updateactivityrequest): 클라이언트의 현재 재생 상태와 최근 사용자 상호 작용에 대한 보고이며, 서비스가 클라이언트의 재생 큐를 수정할 기회도 제공합니다.
- [UpdateActivityResponse](https://developer.apple.com/documentation/sirikitcloudmedia/updateactivityresponse): 재생 진행 상태 보고에 대한 응답으로 클라이언트 큐와 user activity를 업데이트합니다.
- [Process an Update Media Affinity Intent](https://developer.apple.com/documentation/sirikitcloudmedia/updatemediaaffinity): 특정 미디어 항목 또는 더 넓은 범주의 미디어에 대한 사용자의 선호도를 기록합니다.
:::

:::topic-grid
## 재생 실패
- [Recover from Content Playback Failure](https://developer.apple.com/documentation/sirikitcloudmedia/contentplaybackfailure): 오류 이후 클라이언트가 재생을 재개할 수 있도록 복구 큐를 제공합니다.
- [ContentFailure](https://developer.apple.com/documentation/sirikitcloudmedia/contentfailure): 클라이언트가 특정 콘텐츠를 재생할 수 없는 이유를 설명하는 객체입니다.
- [ContentPlaybackFailureRequest](https://developer.apple.com/documentation/sirikitcloudmedia/contentplaybackfailurerequest): 실패한 콘텐츠 재생에서 복구하기 위해 클라이언트가 보내는 요청입니다.
- [ContentPlaybackFailureResponse](https://developer.apple.com/documentation/sirikitcloudmedia/contentplaybackfailureresponse): 클라이언트가 실패한 콘텐츠 재생에서 복구할 수 있게 해 주는 응답입니다.
:::

:::topic-grid
## 라이브러리와 재생목록
- [Process an Add Media Intent](https://developer.apple.com/documentation/sirikitcloudmedia/addmedia): 사용자의 라이브러리 또는 재생목록에 미디어 항목을 추가합니다.
:::

:::topic-grid
## 미디어 항목
- [MediaItem](https://developer.apple.com/documentation/sirikitcloudmedia/mediaitem): 노래, 팟캐스트 에피소드, 재생목록처럼 intent가 참조하는 특정 미디어 항목입니다.
- [MediaReference](https://developer.apple.com/documentation/sirikitcloudmedia/mediareference): 메타데이터 대신 현재 미디어 항목을 식별하는 방법입니다.
- [MediaSearch](https://developer.apple.com/documentation/sirikitcloudmedia/mediasearch): 사용자가 재생하거나 재생목록에 추가하거나 선호도를 표현하려는 미디어 항목에 대한 설명입니다.
- [MediaItemType](https://developer.apple.com/documentation/sirikitcloudmedia/mediaitemtype): 미디어 항목 또는 미디어 검색의 유형입니다.
:::

:::topic-grid
## 요청
- [Invocation](https://developer.apple.com/documentation/sirikitcloudmedia/invocation): 클라이언트가 모든 intent 엔드포인트 요청에 포함하는 프로퍼티입니다.
- [Session](https://developer.apple.com/documentation/sirikitcloudmedia/session): intent를 처리하기 위한 요청 및 응답 시퀀스에 대해 클라이언트가 제공하는 정보입니다.
- [Constraints](https://developer.apple.com/documentation/sirikitcloudmedia/constraints): 명시적 콘텐츠 포함 여부나 클라이언트 기기가 응답으로 받을 수 있는 콘텐츠 양처럼, 요청 처리 방식에 대한 클라이언트 측 제한입니다.
- [PlayerContext](https://developer.apple.com/documentation/sirikitcloudmedia/playercontext): 현재 재생 콘텐츠에 대한 정보입니다.
- [InvocationResponse](https://developer.apple.com/documentation/sirikitcloudmedia/invocationresponse): 모든 intent 엔드포인트 응답에 포함하는 프로퍼티입니다.
:::

:::topic-grid
## intent
- [Intent](https://developer.apple.com/documentation/sirikitcloudmedia/intent): 서비스가 수행해야 하는 사용자 요청입니다.
- [IntentResponse](https://developer.apple.com/documentation/sirikitcloudmedia/intentresponse): intent에 대한 서비스의 응답입니다.
- [UserActivity](https://developer.apple.com/documentation/sirikitcloudmedia/useractivity): 미디어 큐 재생의 컨텍스트입니다.
- [IntentResolutionResult](https://developer.apple.com/documentation/sirikitcloudmedia/intentresolutionresult): intent의 매개변수와 일치하는 객체 또는 서비스가 해당 매개변수 값을 결정할 수 없는 이유에 대한 정보입니다.
- [BooleanResolutionResult](https://developer.apple.com/documentation/sirikitcloudmedia/booleanresolutionresult): intent 매개변수와 일치하는 Boolean 값 또는 서비스가 그 값을 결정할 수 없는 이유에 대한 정보입니다.
:::

:::topic-grid
## 예외
- [ProtocolExceptionInvocationResponse](https://developer.apple.com/documentation/sirikitcloudmedia/protocolexceptioninvocationresponse): 서비스가 클라이언트 요청을 처리하지 못했을 때를 나타내는 응답 객체입니다.
- [ProtocolException](https://developer.apple.com/documentation/sirikitcloudmedia/protocolexception): 미디어 서비스의 예외 응답입니다.
- [ProtocolExceptionReason](https://developer.apple.com/documentation/sirikitcloudmedia/protocolexceptionreason): 서비스가 만날 수 있는 예외의 범주입니다.
:::

:::topic-grid
## 오류
- [UnderlyingError](https://developer.apple.com/documentation/sirikitcloudmedia/underlyingerror): 시스템 프레임워크 오류를 설명하는 객체입니다.
:::

:::asset-list
- `https://developer.apple.com/sample-code/siri/sirikit-cloud-media-open-api.zip` -> `https://developer.apple.com/sample-code/siri/sirikit-cloud-media-open-api.zip` (pending)
:::
