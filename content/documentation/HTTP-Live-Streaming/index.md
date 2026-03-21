---
route: /documentation/HTTP-Live-Streaming
source_url: https://developer.apple.com/documentation/HTTP-Live-Streaming
source_locale: en-US
section: docc
content_type: article
title: HTTP Live Streaming
original_title: HTTP Live Streaming
source_hash: 0c44eb0e472c2db07f470d598583498bb32be92dbe7e5f69368d584d97f432a2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:20:36+00:00'
last_translated_at: '2026-03-13T08:55:00+00:00'
---

# HTTP Live Streaming

iOS, tvOS, macOS 기기로 오디오와 비디오를 전송합니다.

## 개요

HTTP Live Streaming(HLS)은 일반적인 웹 서버를 통해 HTTP로 오디오와 비디오를 전송하여 iPhone, iPad, iPod touch, Apple TV 같은 iOS 기반 기기와 데스크톱 컴퓨터(macOS)에서 재생할 수 있게 합니다. 웹을 구동하는 것과 같은 프로토콜을 사용하여, HLS는 일반 웹 서버와 콘텐츠 전송 네트워크를 이용해 콘텐츠를 배포합니다. HLS는 신뢰성을 목표로 설계되었으며, 유선 및 무선 연결에서 사용 가능한 속도에 맞춰 재생을 최적화함으로써 네트워크 상태에 동적으로 적응합니다.

HLS는 다음을 지원합니다.

- 생방송과 사전 녹화 콘텐츠(주문형 비디오, VOD)
- 서로 다른 비트레이트의 다중 대체 스트림
- 네트워크 대역폭 변화에 대응하는 지능적인 스트림 전환
- 미디어 암호화와 사용자 인증

### 스트리밍 미디어 인코딩 및 전달

다음 그림은 HTTP Live Stream의 세 구성 요소인 서버 구성 요소, 배포 구성 요소, 클라이언트 소프트웨어를 보여 줍니다.

![미디어 녹화가 서버로 전송되고, 웹을 통해 배포된 뒤, 클라이언트 앱으로 전달되는 HTTP Live Stream의 네 부분을 보여 주는 흐름도입니다.](https://developer.apple.com)

일반적인 구성에서 하드웨어 인코더는 오디오-비디오 입력을 받아 HEVC 비디오와 AC-3 오디오로 인코딩하고, 조각난 MPEG-4 파일 또는 MPEG-2 전송 스트림을 출력합니다. 그런 다음 소프트웨어 스트림 세그멘터가 스트림을 여러 개의 짧은 미디어 파일로 나누고, 이 파일들을 웹 서버에 배치합니다. 세그멘터는 또한 미디어 파일 목록을 담은 인덱스 파일을 생성하고 유지합니다. 이 인덱스 파일의 URL이 웹 서버에 게시됩니다. 클라이언트 소프트웨어는 인덱스를 읽고, 목록에 있는 미디어 파일을 순서대로 요청해 세그먼트 사이의 멈춤이나 공백 없이 표시합니다.

### 서버 구성 요소로 미디어 준비하기

서버 구성 요소는 입력 미디어 스트림을 받아 디지털 방식으로 인코딩하는 역할을 합니다. 또한 이를 전송에 적합한 형식으로 캡슐화하고, 분배를 위해 캡슐화된 미디어를 준비합니다.

라이브 이벤트의 경우 서버에는 상용 하드웨어일 수 있는 미디어 인코더와, 인코딩된 미디어를 세그먼트로 나누어 파일로 저장하는 방법이 필요합니다. 이 기능은 Apple이 제공하는 media stream segmenter 같은 소프트웨어일 수도 있고, 통합된 서드파티 솔루션의 일부일 수도 있습니다.

### 배포 구성 요소로 파일 전달하기

배포 시스템은 미디어 파일과 인덱스 파일을 HTTP를 통해 클라이언트에 전달하는 웹 서버 또는 웹 캐싱 시스템입니다. 콘텐츠를 전달하기 위해 별도의 사용자 정의 서버 모듈은 필요하지 않으며, 일반적으로 웹 서버에서 필요한 설정도 매우 적습니다. 실제로 HTTP Live Streaming을 배포하려면 브라우저용 HTML 페이지나 수신기 역할을 할 클라이언트 앱을 만들어야 합니다. 또한 웹 서버와, HEVC 또는 H.264 비디오 및 AAC 또는 AC-3 오디오를 담은 조각난 MPEG-4 미디어 파일로 라이브 스트림을 인코딩하는 방법이 필요합니다.

### 클라이언트 소프트웨어를 통한 미디어 접근

클라이언트 소프트웨어는 어떤 미디어를 요청할지 결정하고, 해당 리소스를 다운로드한 다음, 이를 다시 조합하여 사용자에게 끊김 없는 스트림으로 보여 주는 역할을 합니다. HLS 플레이어와 서버 간 상호 작용을 규정하는 규칙은 [HTTP Live Streaming 2nd Edition](https://datatracker.ietf.org/doc/html/draft-pantos-hls-rfc8216bis)을 참고하세요.

Apple은 [AVKit](https://developer.apple.com/documentation/AVKit), [AVFoundation](https://developer.apple.com/documentation/AVFoundation), [WebKit](https://developer.apple.com/documentation/WebKit)을 포함해 HTTP Live Streaming을 지원하는 여러 프레임워크를 제공합니다. 이 지원은 iOS 3.0과 Safari 4.0부터 제공되어 왔으므로, 직접 클라이언트 소프트웨어를 개발할 필요는 없습니다.

하지만 자체 클라이언트 소프트웨어를 개발하는 경우에는, 먼저 스트림을 식별하는 URL로 인덱스 파일을 가져오는 것부터 시작하세요. 인덱스 파일에는 사용 가능한 미디어 파일, 복호화 키, 사용할 수 있는 대체 스트림의 위치가 지정되어 있습니다. 선택한 스트림에 대해 사용 가능한 각 미디어 파일을 순서대로 다운로드하세요. 각 파일에는 스트림의 연속된 세그먼트가 들어 있습니다. 충분한 양의 데이터를 다운로드한 뒤에는 재조립된 스트림을 사용자에게 표시합니다.

:::important Important
클라이언트는 필요한 경우 복호화 키를 가져오고, 인증을 수행하거나 인증을 허용하는 사용자 인터페이스를 제시하며, 미디어 파일을 복호화하는 책임을 집니다.
:::

클라이언트가 인덱스 파일에서 `EXT-X-ENDLIST` 태그를 만날 때까지 이 과정을 계속합니다. `EXT-X-ENDLIST` 태그가 없으면 인덱스 파일은 진행 중인 방송의 일부입니다. 진행 중인 방송에서는 새 버전의 인덱스 파일을 주기적으로 불러오세요. 업데이트된 인덱스에서 새 미디어 파일과 암호화 키를 찾고, 이 URL들을 재생 큐에 추가합니다.

:::topic-grid
## 필수 항목
- [기본 HTTP Live Streaming(HLS) 스트림 배포하기](https://developer.apple.com/documentation/http-live-streaming/deploying-a-basic-http-live-streaming-hls-stream): HLS를 전달하는 기본 웹페이지를 생성합니다.
- [HTTP Live Streaming용 오디오 준비하기](https://developer.apple.com/documentation/http-live-streaming/preparing-audio-for-http-live-streaming): 오디오와 비디오 재생이 동기화되도록 미디어를 올바르게 인코딩합니다.
:::

:::topic-grid
## 스트림 생성
- [HTTP Live Streaming용 예제 플레이리스트](https://developer.apple.com/documentation/http-live-streaming/example-playlists-for-http-live-streaming): 다양한 HLS 애플리케이션용 플레이리스트를 보고 비교합니다.
- [EXT-X-VERSION 태그 정보](https://developer.apple.com/documentation/http-live-streaming/about-the-ext-x-version-tag): 앱이 지원하는 HLS 기능에 대응하는 프로토콜 버전을 찾습니다.
:::

:::topic-grid
## 도구 사용 및 검증
- [Apple의 HTTP Live Streaming(HLS) 도구 사용하기](https://developer.apple.com/documentation/http-live-streaming/using-apple-s-http-live-streaming-hls-tools): Apple이 제공하는 도구를 사용해 비디오 스트림을 세그먼트화하고, 안정적인 전송을 위한 미디어 플레이리스트를 생성합니다.
:::

:::topic-grid
## 사양 및 기타 문서
- [Apple 기기용 HTTP Live Streaming(HLS) 저작 사양](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices): HLS를 사용한 라이브 및 주문형 오디오/비디오 콘텐츠 전달 요구 사항을 알아봅니다.
- [HLS와 함께 콘텐츠 보호 시스템 사용하기](https://developer.apple.com/documentation/http-live-streaming/using-content-protection-systems-with-hls): 미디어 플레이리스트에 암호화 키를 추가합니다.
- [HTTP Live Streaming(HLS)과 Common Media Application Format](https://developer.apple.com/documentation/http-live-streaming/about-the-common-media-application-format-with-http-live-streaming-hls): HLS에 적용되는 Common Media Application Format을 알아봅니다.
- [저지연 HTTP Live Streaming(HLS) 활성화하기](https://developer.apple.com/documentation/http-live-streaming/enabling-low-latency-http-live-streaming-hls): 확장성을 유지하면서 콘텐츠 스트림에 Low-Latency HLS를 추가합니다.
- [추가 사양 및 비디오 링크](https://developer.apple.com/documentation/http-live-streaming/links-to-additional-specifications-and-videos): 추가 사양과 문서를 검토합니다.
- [HLS 관련 비디오](https://developer.apple.com/documentation/http-live-streaming/videos-about-hls): HTTP Live Streaming에 대한 정보성 비디오를 검토합니다.
- [xHE-AAC 비디오 사운드트랙용 메타데이터 제공하기](https://developer.apple.com/documentation/http-live-streaming/providing-metadata-for-xhe-aac-video-soundtracks): loudness와 dynamic range control 메타데이터를 포함해 볼륨 정규화를 보장합니다.
- [기준 loudness 조정하기](https://developer.apple.com/documentation/http-live-streaming/adjusting-anchor-loudness): 전체 믹스의 음성 게이트 loudness 측정이 부정확할 수 있는 경우(예: 음성 활동이 낮을 때) 기준 loudness를 조정합니다.
- [JSON 챕터 제공하기](https://developer.apple.com/documentation/http-live-streaming/providing-javascript-object-notation-json-chapters): HTTP Live Streaming용 JSON 챕터를 준비합니다.
:::
