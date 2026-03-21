---
route: /documentation/MediaSetup
source_url: https://developer.apple.com/documentation/MediaSetup
source_locale: en-US
section: docc
content_type: symbol
title: Media Setup
original_title: Media Setup
source_hash: 8d0e89510564dda75ece7371a46cbb80b03acf713ac5612a8e749526a97b89fd
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:26:21+00:00'
last_translated_at: '2026-03-13T09:18:00+00:00'
---

# Media Setup

사용자가 HomePod 스피커를 구성해 미디어 서비스에서 직접 음악을 스트리밍할 수 있게 합니다.

## 개요

iOS 앱에서 Media Setup 프레임워크를 사용하면 사용자가 계정 자격 증명을 HomePod 스피커로 전달하도록 도울 수 있습니다. 예를 들어 음악 스트리밍을 위한 Siri media intent를 이미 지원하는 iOS 앱이 있다면, 사용자가 HomePod를 설정해 미디어 서비스에서 직접 음악을 스트리밍할 수 있도록 이 프레임워크를 채택하세요. HomePod 스피커가 접근할 수 있는 엔드포인트를 제공하려면 미디어 서비스에서 [SiriKit Cloud Media](https://developer.apple.com/documentation/SiriKitCloudMedia)를 채택합니다.

[MSSetupSession](https://developer.apple.com/documentation/mediasetup/mssetupsession)은 [presentationAnchor()](https://developer.apple.com/documentation/mediasetup/msauthenticationpresentationcontext/presentationanchor())에서 제공한 윈도우를 사용해 사용자에게 구성 화면을 표시합니다. 사용자가 구성을 확인하면, 세션은 자신의 [account](https://developer.apple.com/documentation/mediasetup/mssetupsession/account)로부터 token 요청을 조합해 OAuth 서비스에 보냅니다. OAuth 서비스가 token으로 응답하면 세션은 그 token과 [configurationURL](https://developer.apple.com/documentation/mediasetup/msserviceaccount/configurationurl)을 검증합니다. 그런 다음 그 token을 Home 앱에서 사용자의 Apple ID와 연관된 HomePod 스피커로 보냅니다.

HomePod용 SiriKit Media Intents 프로그램 신청 방법에 대한 자세한 내용은 [Siri for Developers](https://developer.apple.com/siri)의 HomePod 섹션을 참고하세요.

:::topic-grid
## HomePod 구성
- [MSSetupSession](https://developer.apple.com/documentation/mediasetup/mssetupsession): 앱, 시스템, 미디어 서비스, HomePod 스피커 사이의 구성 정보 전달을 관리하는 객체입니다.
- [MSServiceAccount](https://developer.apple.com/documentation/mediasetup/msserviceaccount): 스트리밍 미디어 서비스에 접근하기 위한 계정 세부 정보입니다.
:::
