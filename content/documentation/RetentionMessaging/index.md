---
route: /documentation/RetentionMessaging
source_url: https://developer.apple.com/documentation/RetentionMessaging
source_locale: en-US
section: docc
content_type: symbol
title: Retention Messaging API
original_title: Retention Messaging API
source_hash: 92052d9c9a18782864621718c3250217506c70fff1e7c04d66660dfed44e0ed0
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:04:57+00:00'
last_translated_at: '2026-03-13T07:05:46+00:00'
---

# Retention Messaging API

제품과 로캘에 맞게 실시간으로 선택할 수 있는 사전 구성 메시지로 고객이 구독을 유지할 이유를 제공합니다.

## 개요

Retention Messaging API는 고객이 구독 세부 정보 페이지를 보고 취소를 고려할 때 시스템이 어떤 메시지를 표시할지 선택할 수 있게 해 주는 서버 간 서비스입니다. 제품과 로캘별로 메시지를 미리 업로드하고 구성할 수 있습니다.

:::important Important
이 사전 공개 기능에 대해 자세히 알아보고 관심을 표시하려면 [Request access to the Retention Messaging API](https://developer.apple.com/contact/request/retention-messaging-api/)를 참고하세요.
:::

메시지는 고객에게 구독을 통해 이용할 수 있는 기능이나 콘텐츠를 상기시키거나, 대체 제안을 보여 줄 수 있습니다. 리텐션 메시지에는 네 가지 유형이 있습니다.

- 텍스트 기반 메시지
- 이미지가 포함된 텍스트 기반 메시지
- 텍스트와 함께 고객이 전환할 수 있는 추천 구독을 포함하는 플랜 전환 메시지
- 텍스트와 함께 할인된 가격으로 서비스를 계속 이용할 수 있는 프로모션 오퍼를 포함하는 프로모션 오퍼 메시지. 동일한 서비스 등급일 수도 있고 다른 등급일 수도 있습니다.

고객이 구독 세부 정보 페이지에서 `Cancel Subscription`을 탭하면 시스템이 리텐션 메시지를 표시합니다. 이어서 고객이 `Cancel Subscription`을 탭해 취소를 계속 진행할 수 있는 `Confirm Cancellation` 페이지가 표시됩니다. 고객은 `Don’t Cancel`을 탭할 수도 있고, 리텐션 메시지 유형에 따라 오퍼를 사용하거나 추천한 구독으로 가입할 수도 있습니다.

다음 두 예시는 취소 확인 화면에 표시되는 텍스트 기반 메시지와 이미지가 포함된 텍스트 기반 메시지를 보여 줍니다.

다음 두 예시는 취소 확인 화면에 표시되는 플랜 전환 메시지와 프로모션 오퍼 메시지를 보여 줍니다.

이 API를 사용해 고객에게 보여 줄 리텐션 메시지를 선택하는 방법은 두 가지입니다.

- 특정 제품과 로캘에 적용되는 기본 메시지를 구성하는 방법입니다. 기본 메시지는 이미지 포함 여부와 관계없이 텍스트 기반 메시지입니다.
- App Store 서버로부터 오는 서버 간 호출에 응답할 때 실시간으로 리텐션 메시지를 선택하는 방법입니다. 실시간 호출이 어떤 이유로든 실패할 경우를 대비해 시스템이 사용할 기본 메시지도 함께 구성합니다.

### 이미지와 메시지 업로드

모든 리텐션 메시지는 업로드한 텍스트와 선택적 이미지로 시작합니다. 자세한 내용은 [Upload Image](https://developer.apple.com/documentation/retentionmessaging/upload-image)와 [Upload Message](https://developer.apple.com/documentation/retentionmessaging/upload-message)를 참고하세요.

오해를 불러일으키거나 부정확한 콘텐츠는 업로드하지 마세요.

### 기본 리텐션 메시지 구성

이 API를 사용하는 가장 간단한 방법은 기본 메시지를 구성하는 것입니다. 먼저 이미지와 메시지를 업로드합니다. 그런 다음 기본 메시지로 사용할 메시지를 지정합니다. 자세한 내용은 [Setting up retention messages](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messages)를 참고하세요.

기본 메시지 옵션은 이미지 포함 여부와 관계없이 텍스트 기반 메시지만 지원합니다. 오퍼가 포함된 리텐션 메시지를 사용하려면 실시간 메시징 흐름을 사용하세요.

### 오퍼를 포함한 실시간 메시지 제공

실시간 메시징 흐름은 활성 구독자가 `Cancel` 버튼이 있는 구독 세부 정보 페이지를 볼 때 서버를 호출합니다. 예를 들어 고객은 Apple Account > Subscriptions 페이지나 App Store의 구독 세부 정보 페이지에서 취소를 고려할 수 있습니다.

실시간 호출은 원래 트랜잭션 ID와 고객의 로캘을 포함해 해당 구독에 대한 정보를 전달합니다. 여러분은 시스템이 표시할 적절한 사전 구성 메시지를 선택해 응답합니다. 플랜 전환이나 프로모션 오퍼가 포함된 메시지를 포함해 모든 리텐션 메시지 유형 중에서 선택할 수 있습니다.

실시간 흐름을 구현하려면 다음 단계를 따르세요.

1. 리텐션 메시지를 업로드하고 준비합니다. 자세한 내용은 [Setting up retention messages](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messages)를 참고하세요.
2. 각 로캘의 모든 제품에 대해 기본 리텐션 메시지를 구성합니다. 어떤 이유로든 서버에 대한 실시간 호출이 실패할 경우를 대비해 시스템이 기본 메시지를 폴백으로 사용하므로, 기본 메시지는 필수입니다. 자세한 내용은 [Configure Default Message](https://developer.apple.com/documentation/retentionmessaging/configure-default-message)를 참고하세요.
3. 서버에서 `Get Retention Message` 엔드포인트를 구현합니다. 자세한 내용은 [Setting up your Get Retention Message endpoint](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messaging-endpoint)를 참고하세요.
4. 표시할 리텐션 메시지를 실시간으로 선택해 App Store 요청에 응답합니다. 자세한 내용은 [Responding to real-time retention messaging requests](https://developer.apple.com/documentation/retentionmessaging/responding-to-realtime-retention-messaging-requests)를 참고하세요.

### 시스템 요구 사항

리텐션 메시지는 iOS 15.1 이상, iPadOS 15.1 이상, visionOS 1 이상, 또는 macOS 14 이상을 실행하는 기기에서만 표시됩니다.

:::topic-grid
## 필수 항목
- [리텐션 메시지 설정하기](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messages): 리텐션 메시지용 이미지와 메시지를 업로드하고, 기본 메시지를 구성하며, 프로모션 오퍼 및 플랜 전환 메시지 설정을 완료합니다.
- [속도 제한 식별하기](https://developer.apple.com/documentation/retentionmessaging/identifying-rate-limits): Retention Messaging API 엔드포인트에 적용되는 속도 제한을 파악하고 코드에서 처리합니다.
- [Retention Messaging API 변경 로그](https://developer.apple.com/documentation/retentionmessaging/retention-messaging-changelog): Retention Messaging API의 새로운 기능과 업데이트를 알아봅니다.
:::

:::topic-grid
## 이미지 구성
- [Upload Image](https://developer.apple.com/documentation/retentionmessaging/upload-image): 리텐션 메시지에 사용할 이미지를 업로드합니다.
- [Delete Image](https://developer.apple.com/documentation/retentionmessaging/delete-image): 이전에 업로드한 이미지를 삭제합니다.
- [Get Image List](https://developer.apple.com/documentation/retentionmessaging/get-image-list): 업로드한 모든 이미지의 식별자와 상태를 가져옵니다.
- [GetImageListResponse](https://developer.apple.com/documentation/retentionmessaging/getimagelistresponse): 모든 이미지의 상태 정보를 포함하는 응답입니다.
- [GetImageListResponseItem](https://developer.apple.com/documentation/retentionmessaging/getimagelistresponseitem): 이미지 하나의 식별자와 상태 정보입니다.
:::

:::topic-grid
## 메시지 구성
- [Upload Message](https://developer.apple.com/documentation/retentionmessaging/upload-message): 리텐션 메시지에 사용할 메시지를 업로드합니다.
- [Delete Message](https://developer.apple.com/documentation/retentionmessaging/delete-message): 이전에 업로드한 메시지를 삭제합니다.
- [Get Message List](https://developer.apple.com/documentation/retentionmessaging/get-message-list): 업로드한 모든 메시지의 식별자와 상태를 가져옵니다.
- [UploadMessageRequestBody](https://developer.apple.com/documentation/retentionmessaging/uploadmessagerequestbody): 메시지 텍스트와 선택적 이미지 참조를 포함하는 메시지 업로드 요청 본문입니다.
- [UploadMessageImage](https://developer.apple.com/documentation/retentionmessaging/uploadmessageimage): 대체 텍스트와 함께 이미지를 정의합니다.
- [GetMessageListResponse](https://developer.apple.com/documentation/retentionmessaging/getmessagelistresponse): 모든 메시지의 상태 정보를 포함하는 응답입니다.
- [GetMessageListResponseItem](https://developer.apple.com/documentation/retentionmessaging/getmessagelistresponseitem): 메시지 하나의 식별자와 상태 정보입니다.
:::

:::topic-grid
## 기본 메시지 구성
- [Configure Default Message](https://developer.apple.com/documentation/retentionmessaging/configure-default-message): 특정 로캘의 특정 제품에 대한 기본 메시지를 구성합니다.
- [Delete Default Message](https://developer.apple.com/documentation/retentionmessaging/delete-default-message): 특정 로캘의 제품에 설정된 기본 메시지를 삭제합니다.
- [DefaultConfigurationRequest](https://developer.apple.com/documentation/retentionmessaging/defaultconfigurationrequest): 기본 구성 정보를 담은 요청 본문입니다.
:::

:::topic-grid
## 실시간 리텐션 메시징
- [Get Retention Message 엔드포인트 설정하기](https://developer.apple.com/documentation/retentionmessaging/setting-up-retention-messaging-endpoint): App Store 서버 요청에 응답하는 서버 엔드포인트를 구현해 고객에게 보여 줄 리텐션 메시지를 실시간으로 선택합니다.
- [실시간 리텐션 메시징 요청에 응답하기](https://developer.apple.com/documentation/retentionmessaging/responding-to-realtime-retention-messaging-requests): Get Retention Message 엔드포인트 요청에 응답하여 고객에게 보여 줄 리텐션 메시지를 실시간으로 선택합니다.
- [RealtimeRequestBody](https://developer.apple.com/documentation/retentionmessaging/realtimerequestbody): App Store 서버가 Get Retention Message 엔드포인트로 보내는 요청 본문입니다.
- [DecodedRealtimeRequestBody](https://developer.apple.com/documentation/retentionmessaging/decodedrealtimerequestbody): 실시간 리텐션 메시지를 요청하기 위해 App Store가 서버로 보내는 요청 본문을 디코딩한 형태입니다.
- [RealtimeResponseBody](https://developer.apple.com/documentation/retentionmessaging/realtimeresponsebody): 시스템이 고객에게 표시할 리텐션 메시지를 실시간으로 선택하기 위해 제공하는 응답입니다.
:::

:::topic-grid
## 서버 성능 테스트
- [Initiate Performance Test](https://developer.apple.com/documentation/retentionmessaging/initiate-performance-test): 성능 테스트를 시작합니다.
- [Get Performance Test Results](https://developer.apple.com/documentation/retentionmessaging/get-performance-test-results): 지정한 식별자에 대한 성능 테스트 결과를 가져옵니다.
:::

:::topic-grid
## 데이터 타입
- [데이터 타입](https://developer.apple.com/documentation/retentionmessaging/data-types): 요청 및 응답 페이로드에 사용하는 데이터 타입을 참고하세요.
:::

:::topic-grid
## 오류 정보
- [오류 코드](https://developer.apple.com/documentation/retentionmessaging/error-codes): Retention Messaging API 응답이 반환하는 오류 코드를 이해합니다.
:::
