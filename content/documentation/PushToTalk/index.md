---
route: /documentation/PushToTalk
source_url: https://developer.apple.com/documentation/PushToTalk
source_locale: en-US
section: docc
content_type: symbol
title: Push to Talk
original_title: Push to Talk
source_hash: 9ba554cc5b671fe8fa1785de899b547f80719b38f2ee428ee2ea0b4971248e74
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:54:13+00:00'
last_translated_at: '2026-03-13T19:05:00+09:00'
---

# Push to Talk

앱의 Push to Talk 서비스를 위한 시스템 사용자 인터페이스를 표시합니다.

## 개요

Push to Talk 프레임워크는 전력 효율이 높고, 사용자 친화적이며, 개인정보 보호에 초점을 둔 API입니다. 이 프레임워크는 사용자가 어디서든 오디오를 전송할 수 있게 하는 사용자 인터페이스 컨트롤을 앱이 제공할 수 있게 해 줍니다. 또한 세션이 진행 중일 때 시스템이 백그라운드에서 앱을 깨워 들어오는 오디오를 처리할 수 있도록 임시 Apple Push Notification service token을 제공합니다.

:::note 참고
Push to Talk 서비스는 visionOS에서 실행되는 호환 iPad 및 iPhone 앱에서는 사용할 수 없습니다.
:::

:::topic-grid
## 핵심 사항
- [Creating a Push to Talk app](https://developer.apple.com/documentation/pushtotalk/creating-a-push-to-talk-app): 시스템 사용자 인터페이스 컨트롤을 갖춘 워키토키 스타일 앱을 빌드합니다.
- [PTChannelManager](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager): push-to-talk 채널 관리자를 나타내는 객체입니다.
:::

:::topic-grid
## 채널 관리
- [PTChannelManagerDelegate](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate): 채널 관리자의 수명 주기를 나타내는 타입입니다.
- [PTTransmissionMode](https://developer.apple.com/documentation/pushtotalk/pttransmissionmode): 오디오 전송 모드의 종류를 식별합니다.
- [PTServiceStatus](https://developer.apple.com/documentation/pushtotalk/ptservicestatus): 서비스 상태를 나타내는 타입을 식별합니다.
- [PTChannelJoinReason](https://developer.apple.com/documentation/pushtotalk/ptchanneljoinreason): 채널에 참여한 이유를 나타내는 타입을 식별합니다.
- [PTChannelLeaveReason](https://developer.apple.com/documentation/pushtotalk/ptchannelleavereason): 채널을 떠난 이유를 나타내는 타입을 식별합니다.
- [PTChannelTransmitRequestSource](https://developer.apple.com/documentation/pushtotalk/ptchanneltransmitrequestsource): 전송 요청의 출처를 나타내는 타입을 식별합니다.
:::

:::topic-grid
## 채널 복원
- [PTChannelDescriptor](https://developer.apple.com/documentation/pushtotalk/ptchanneldescriptor): 채널을 설명하는 객체입니다.
- [PTChannelRestorationDelegate](https://developer.apple.com/documentation/pushtotalk/ptchannelrestorationdelegate): 채널 복원 동작을 나타내는 타입입니다.
:::

:::topic-grid
## 채널 참가자
- [PTParticipant](https://developer.apple.com/documentation/pushtotalk/ptparticipant): 참가자를 나타내는 객체입니다.
:::

:::topic-grid
## 푸시 알림 결과
- [PTPushResult](https://developer.apple.com/documentation/pushtotalk/ptpushresult): 푸시 결과를 나타내는 객체입니다.
:::

:::topic-grid
## Push to Talk 오류
- [PTChannelError](https://developer.apple.com/documentation/pushtotalk/ptchannelerror-swift.struct): 채널 오류를 나타내는 구조체입니다.
- [PTChannelError.Code](https://developer.apple.com/documentation/pushtotalk/ptchannelerror-swift.struct/code): 채널 작업에 대한 오류 코드입니다.
- [PTInstantiationError](https://developer.apple.com/documentation/pushtotalk/ptinstantiationerror-swift.struct): 인스턴스화 오류를 나타내는 구조체입니다.
- [PTInstantiationError.Code](https://developer.apple.com/documentation/pushtotalk/ptinstantiationerror-swift.struct/code): 인스턴스화 작업에 대한 오류 코드입니다.
- [PTChannelErrorDomain](https://developer.apple.com/documentation/pushtotalk/ptchannelerrordomain): 채널 오류 도메인의 문자열 표현입니다.
- [PTInstantiationErrorDomain](https://developer.apple.com/documentation/pushtotalk/ptinstantiationerrordomain): 인스턴스화 오류 도메인의 문자열 표현입니다.
:::
