---
route: /documentation/FoveatedStreaming
source_url: https://developer.apple.com/documentation/FoveatedStreaming
source_locale: en-US
section: docc
content_type: symbol
title: Foveated Streaming
original_title: Foveated Streaming
source_hash: 7b4c244797cd410dbcfa8dfacf440650b55a8acdee948adfd2252fd40fa1109c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:25:15+00:00'
last_translated_at: '2026-03-13T23:12:00+09:00'
---

# Foveated Streaming

Foveated Streaming은 visionOS 앱이 스트리밍 엔드포인트에서 고해상도 저지연 몰입형 콘텐츠를 표시할 수 있게 합니다.

## 개요

Foveated Streaming 프레임워크는 Apple Vision Pro에서 로컬 및 클라우드 스트리밍 엔드포인트로 연결을 설정하기 위한 세션 기반 API를 제공합니다. 엔드포인트 호스트는 사용자가 대략 어느 영역을 보고 있는지에 대한 정보를 바탕으로 필요한 부분에만 고품질 콘텐츠를 스트리밍해 성능을 보장합니다. 애플리케이션과 게임은 NVIDIA CloudXR™ SDK와 통합해 스트리밍 엔드포인트가 될 수 있습니다.

Apple Vision Pro에서 Foveated Streaming을 사용하면 스트리밍 콘텐츠와 함께 visionOS 공간 콘텐츠를 표시할 수 있습니다. 예를 들어 비행 시뮬레이터 앱은 [RealityKit](https://developer.apple.com/documentation/RealityKit)을 사용해 조종석을 렌더링하고, 원격 컴퓨터에서 기기로 처리 집약적인 풍경을 스트리밍할 수 있습니다.

핵심 워크플로는 [FoveatedStreamingSession](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession)을 생성하고, 외부 스트리밍 엔드포인트에 연결을 설정한 다음, 앱의 [ImmersiveSpace](https://developer.apple.com/documentation/SwiftUI/ImmersiveSpace) 안에 스트리밍된 콘텐츠를 표시하는 과정으로 이루어집니다. `ImmersiveSpace`의 모든 기능을 사용할 수 있으며, 여기에는 점진적 몰입 스타일과 혼합 몰입 스타일도 포함됩니다. 양방향 메시지 채널 시스템을 사용하면 visionOS 앱이 스트리밍 엔드포인트와 사용자 정의 데이터를 주고받을 수 있어, 앱이 네이티브 [SwiftUI](https://developer.apple.com/documentation/SwiftUI) 인터페이스로 스트리밍 콘텐츠를 구성할 수 있습니다.

:::topic-grid
## 핵심 항목
- [Streaming a CloudXR application to Apple Vision Pro with foveation](https://developer.apple.com/documentation/foveatedstreaming/streaming-a-cloudxr-application-to-apple-vision-pro-with-foveation): NVIDIA CloudXR™와 세션 관리 연결 프로토콜을 데스크톱 또는 클라우드 애플리케이션에 통합해 Apple Vision Pro로 고충실도 공간 콘텐츠를 스트리밍합니다.
- [Establishing foveated streaming sessions with Apple Vision Pro](https://developer.apple.com/documentation/foveatedstreaming/establishing-foveated-streaming-sessions-with-apple-vision-pro): 세션 관리 연결 프로토콜을 구현해 Apple Vision Pro와 로컬 스트리밍 엔드포인트 사이의 스트리밍 세션을 발견하고, 페어링하고, 관리합니다.
- [Creating a foveated streaming client on visionOS](https://developer.apple.com/documentation/foveatedstreaming/creating-a-foveated-streaming-client-on-visionos): Foveated Streaming 프레임워크를 사용해 컴퓨터 또는 클라우드에서 고충실도 몰입형 콘텐츠를 스트리밍하는 visionOS 앱을 빌드합니다.
:::

:::topic-grid
## 클래스
- [FoveatedStreamingSession](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession): 로컬 또는 원격 스트리밍 엔드포인트에 대한 foveated streaming 연결을 관리하는 세션입니다.
:::

:::topic-grid
## 구조체
- [FoveatedStreamingSpaceContent](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingspacecontent): foveated stream을 표시하는 몰입형 공간의 콘텐츠를 정의하는 타입입니다.
:::
