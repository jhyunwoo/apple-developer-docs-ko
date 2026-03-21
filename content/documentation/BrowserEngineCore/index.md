---
route: /documentation/BrowserEngineCore
source_url: https://developer.apple.com/documentation/BrowserEngineCore
source_locale: en-US
section: docc
content_type: symbol
title: BrowserEngineCore
original_title: BrowserEngineCore
source_hash: 335475252f2fa1663d592c63f132c1664eeef7870ea009ee32cca8122a4f32bb
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:54+00:00'
last_translated_at: '2026-03-13T17:35:00+09:00'
---

# BrowserEngineCore

웹 브라우저 앱에 대체 브라우저 엔진을 통합합니다.

## 개요

`BrowserEngineCore` 프레임워크를 사용하면 [BrowserEngineKit](https://developer.apple.com/documentation/BrowserEngineKit)을 사용해 UI를 렌더링하는 대체 브라우저 엔진의 저수준 기능을 지원할 수 있습니다. 웹 브라우저 앱 개발에 대한 자세한 내용은 [Designing your browser architecture](https://developer.apple.com/documentation/BrowserEngineKit/designing-your-browser-architecture)를 참고하십시오.

:::topic-grid
## 커널 이벤트
- [be_kevent(_:_:_:_:_:_:)](https://developer.apple.com/documentation/browserenginecore/be_kevent(_:_:_:_:_:_:)): 지정된 큐의 커널 이벤트를 등록하고 32비트 데이터 타입을 사용해 큐에서 대기 중인 이벤트를 반환합니다.
- [be_kevent64(_:_:_:_:_:_:)](https://developer.apple.com/documentation/browserenginecore/be_kevent64(_:_:_:_:_:_:)): 지정된 큐의 커널 이벤트를 등록하고 64비트 데이터 타입을 사용해 큐에서 대기 중인 이벤트를 반환합니다.
- [BE_KEVENT_NO_FLAGS](https://developer.apple.com/documentation/browserenginecore/be_kevent_no_flags): 커널 이벤트 수신 요청에 플래그가 설정되지 않았음을 나타냅니다.
- [BE_KEVENT_RETURN_IMMEDIATELY](https://developer.apple.com/documentation/browserenginecore/be_kevent_return_immediately): 커널 이벤트 수신 요청이 이벤트를 기다리지 않고 바로 반환되어야 함을 나타냅니다.
:::

:::topic-grid
## JIT 컴파일
- [BE_JIT_WRITE_PROTECT_TAG](https://developer.apple.com/documentation/browserenginecore/be_jit_write_protect_tag): 시스템이 JIT 컴파일용 포인터 인증 코드를 생성할 때 사용하는 구분 값입니다.
:::

:::topic-grid
## 클래스
- [BEAudioSession](https://developer.apple.com/documentation/browserenginecore/beaudiosession-6b7ig): 오디오 session을 나타내는 객체입니다.
- [BEAudioSession](https://developer.apple.com/documentation/browserenginecore/beaudiosession-7bb2q): 오디오 session을 나타내는 객체입니다.
:::
