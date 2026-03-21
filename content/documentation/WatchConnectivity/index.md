---
route: /documentation/WatchConnectivity
source_url: https://developer.apple.com/documentation/WatchConnectivity
source_locale: en-US
section: docc
content_type: symbol
title: Watch Connectivity
original_title: Watch Connectivity
source_hash: b5825e62348894e5b6fc6d705631bb9a23859e80b8248ec21e7637388c35c128
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:10:35+00:00'
last_translated_at: '2026-03-14T00:36:00+09:00'
---

# Watch Connectivity

iOS 앱과 짝지어진 watchOS 앱 사이에 양방향 통신을 구현합니다.

## 개요

이 프레임워크를 사용하면 iOS 앱과 짝지어진 watchOS 앱의 WatchKit extension 사이에 데이터를 전송할 수 있습니다. 소량의 데이터만 보낼 수도 있고, 전체 파일을 전달할 수도 있습니다. 또한 이 프레임워크를 사용해 watchOS 앱의 complication 업데이트를 트리거할 수도 있습니다.

앱에서 전송을 시작한 뒤에는 시스템이 모든 데이터 전송에 대한 책임을 맡습니다. 대부분의 전송은 수신 앱이 비활성 상태일 때 background에서 이루어집니다. 앱이 깨어나면 비활성 상태 동안 도착한 데이터에 대해 알림을 받습니다. 두 앱이 모두 활성 상태일 때는 실시간 통신도 가능합니다.

:::topic-grid
## 핵심 사항
- [WCSession](https://developer.apple.com/documentation/watchconnectivity/wcsession): WatchKit extension과 companion iOS 앱 간의 통신을 시작하는 객체입니다.
- [WCSessionDelegate](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate): 객체가 보낸 메시지를 수신하기 위한 메서드를 정의하는 delegate 프로토콜입니다.
:::

:::topic-grid
## 데이터 객체
- [WCSessionFile](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile): iOS 앱과 WatchKit extension 사이에서 현재 전송 중인 파일에 대한 정보입니다.
- [WCSessionFileTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer): 진행 중인 파일 전송에 대한 정보입니다.
- [WCSessionUserInfoTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer): 진행 중인 데이터 전송에 대한 정보입니다.
:::

:::topic-grid
## 샘플 코드
- [Transferring data with Watch Connectivity](https://developer.apple.com/documentation/watchconnectivity/transferring-data-with-watch-connectivity): watchOS 앱과 companion iOS 앱 사이에 데이터를 전송합니다.
:::
