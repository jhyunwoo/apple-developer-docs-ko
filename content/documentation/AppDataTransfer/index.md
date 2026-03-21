---
route: /documentation/AppDataTransfer
source_url: https://developer.apple.com/documentation/AppDataTransfer
source_locale: en-US
section: docc
content_type: symbol
title: App Data Transfer
original_title: App Data Transfer
source_hash: 6aeae1281dcb4ff58c28d2f8f9034d59c4929b8e0e7046eb550554cdb6b7a0c8
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:37:07+00:00'
last_translated_at: '2026-03-13T20:30:00+09:00'
---

# App Data Transfer

앱에 대한 App Store 정보와 앱 설치 활동 데이터를 다운로드합니다.

## 개요

App Data Transfer 웹 API를 사용하면 앱에 대한 App Store 정보와 앱 설치 활동 데이터를 요청하고 다운로드할 수 있습니다. 사용 가능한 데이터는 사용자의 Apple App Store 사용과 관련되며 이전 거래 내역과 다운로드 같은 정보를 포함합니다. 여러 개의 앱이 있다면 사용자가 자신의 데이터를 여러분에게 이전할 수 있도록 각 앱을 이 API와 별도로 통합해야 합니다.

데이터에 접근하려면 `data-transfer-user-profile` 읽기 전용 범위와 다음 범위 중 하나 이상을 사용해 access token을 획득해야 합니다.

- `appstore-info-readonly`
- `app-install-activity-readonly`

:::note 참고
이전에 오래된 범위 이름과 함께 `appstore-user-profile` 범위를 사용해 App Store 정보 접근을 요청한 적이 있다면, 시스템은 이 범위들을 허용하고 EU 및 UK 범위 모두에 대해 자동 승인합니다. 새로운 토큰 요청을 만들 필요가 없습니다.
:::

자세한 내용은 [Request an authorization](https://developer.apple.com/documentation/AccountOrganizationalDataSharing/Request-an-authorization)을 참고하십시오.

App ID 또는 Services ID가 이 범위를 요청할 수 있는 권한을 얻으려면 [Account & Organizational Data Sharing](https://developer.apple.com/help/account/share-account-data/share-account-and-organizational-data/)의 안내를 따르십시오.

:::note 참고
이 API는 EU와 UK 사용자에 대한 앱 관련 데이터를 반환합니다. 사용자가 승인한 제3자인 경우, 사용자 대신 Apple에서 관련 사용자 데이터를 이전할 수 있도록 [Account Data Transfer](https://developer.apple.com/documentation/AccountDataTransfer) API 접근을 요청할 수 있습니다.

이 API에서 제공되는 데이터에 대해, 특히 Apple이 사용자 개인정보를 보호하고 법적 의무를 준수하기 위해 어떤 개인정보 보호 조치를 적용하는지에 대해 질문이 있으면, 다음 옵션을 선택해 Feedback Assistant를 통해 Apple에 문의하십시오.

Developer Tools & Resources > App Data Transfer API > Data Request

Feedback Assistant 사용 방법에 대한 자세한 내용은 [Learn more](https://support.apple.com/guide/feedback-assistant/welcome/mac)를 참고하십시오.
:::

### 필요한 HTTP 헤더 설정

아래 나열된 endpoint 중 하나를 사용해 앱의 App Store 정보 또는 앱 설치 활동을 요청할 때는 다음 HTTP 헤더를 설정하십시오.

:::term-list
`Authorization`: 값을 `Bearer <ACCESS_TOKEN>`으로 설정하여 앱이 `appstore-info-account-data-for-EU-users`와 `appstore-info-account-data-for-UK-users`, 또는 `app-install-activity-account-data-for-EU-users` 또는 `app-install-activity-account-data-for-UK-users` 범위로 데이터를 가져올 권한이 있음을 주장합니다.
`X-Apple-Transaction-Id`: 요청을 고유하게 식별하는 UUID로 값을 설정합니다. 지원을 받기 위해 Apple에 문의해야 하는 경우 도움이 필요한 요청의 UUID를 함께 전달하십시오.
:::

### 요청 제출

`app-store` 데이터 유형을 요청하며 [Submit request](https://developer.apple.com/documentation/appdatatransfer/submit-request) endpoint로 HTTP `POST` 요청을 보냅니다. 일회성 요청을 만들려면 `mode` 키를 `ONE_TIME`으로 설정합니다. 반복 요청을 만들려면 다음 값 중 하나를 사용하십시오.

:::term-list
`DAILY_30`: 30일 동안 매일 1회 반복 요청
`WEEKLY_180`: 180일 동안 매주 1회 반복 요청
:::

Apple 서버는 요청 상태를 가져오거나, 다운로드 URL을 요청하거나, 요청을 취소할 때 사용하는 request ID를 반환합니다. 반복 요청의 경우 Apple 서버는 request ID와 함께 반복 요청 시리즈를 식별하는 parent ID도 반환합니다.

서버 응답에는 `statusCheckDelay`도 포함되며, 이는 요청 상태를 확인하기 전에 기다려야 하는 초 수입니다. 이 시간 전에 [Cancel request](https://developer.apple.com/documentation/appdatatransfer/cancel-request) endpoint로 `POST` 요청을 보내면 요청을 취소할 수 있습니다.

`DAILY_30` 반복 요청을 제출한 뒤 이후 각 날짜에 반복 인스턴스를 다시 제출하지 않으면, 요청 제출 후 40일이 지나면 반복 요청이 만료됩니다.

`WEEKLY_180` 반복 요청을 제출한 뒤 이후 각 주에 반복 인스턴스를 다시 제출하지 않으면, 요청 제출 후 190일이 지나면 반복 요청이 만료됩니다.

:::note 참고
이미 대기 중인 반복 요청이 있는데 또 다른 반복 요청을 만들면, 시스템은 기존 요청의 ID와 함께 오류를 반환합니다.
:::

### 요청 상태 확인

제출한 요청에 해당하는 데이터는 즉시 사용할 수 없습니다. 상태 확인 지연 시간이 지난 뒤, 요청 식별자를 경로에 포함하여 [Get one-time request status](https://developer.apple.com/documentation/appdatatransfer/get-one-time-request-status) 또는 [Get recurring request status](https://developer.apple.com/documentation/appdatatransfer/get-recurring-request-status)로 `GET` 요청을 보내십시오.

작업 상태가 `completed` 또는 `completed_with_error`이면 요청과 연결된 데이터를 다운로드할 준비가 된 것입니다.

### 데이터 이전

완료된 요청의 다운로드 URL을 얻으려면, 요청 식별자를 경로에 포함해 [Get one-time request download URLs](https://developer.apple.com/documentation/appdatatransfer/get-one-time-request-download-urls) 또는 [Get recurring request download URLs](https://developer.apple.com/documentation/appdatatransfer/get-recurring-request-download-urls)로 `GET` 요청을 보내십시오.

응답에는 앱과 관련된 사용자의 데이터를 가져오기 위해 `GET` 요청을 보낼 URL 목록이 포함됩니다.

다운로드 URL은 다운로드 요청이 완료된 후 3일 동안 사용할 수 있습니다. 받은 URL은 요청 후 15분 동안 유효합니다.

다운로드한 파일의 내용과 용어에 대한 정보는 [Data and Privacy](https://privacy.apple.com/file-guides/transfer/appdata)를 참고하십시오.

### 반복 요청 다시 제출

반복 요청의 다음 인스턴스를 대기열에 넣으려면 [Resubmit request](https://developer.apple.com/documentation/appdatatransfer/resubmit-request) endpoint로 `POST` 요청을 보내고, parent request identifier와 가장 최근 인스턴스의 request identifier를 전달하십시오.

서버 응답에는 새 요청의 request identifier와 새 요청의 상태를 확인하기 전에 기다려야 하는 지연 시간이 포함됩니다.

:::topic-grid
## 요청 생성
- [Submit request](https://developer.apple.com/documentation/appdatatransfer/submit-request): 사용자의 데이터를 다운로드할 수 있도록 준비를 시작합니다.
- [JobSubmission](https://developer.apple.com/documentation/appdatatransfer/jobsubmission): 사용자의 데이터를 요청하는 제출을 설명하는 객체입니다.
- [CreatedJob](https://developer.apple.com/documentation/appdatatransfer/createdjob): 새로 생성된 다운로드 요청을 나타내는 객체입니다.
- [Resubmit request](https://developer.apple.com/documentation/appdatatransfer/resubmit-request): 반복 요청의 다음 인스턴스를 대기열에 넣습니다.
- [ResubmissionRequest](https://developer.apple.com/documentation/appdatatransfer/resubmissionrequest): 반복 다운로드 요청을 다시 제출하기 위한 요청을 설명하는 객체입니다.
- [ResubmissionResponse](https://developer.apple.com/documentation/appdatatransfer/resubmissionresponse): 다시 제출된 반복 다운로드 요청을 나타내는 객체입니다.
:::

:::topic-grid
## 상태
- [Get one-time request status](https://developer.apple.com/documentation/appdatatransfer/get-one-time-request-status): 일회성 다운로드 요청의 상태를 확인합니다.
- [Get recurring request status](https://developer.apple.com/documentation/appdatatransfer/get-recurring-request-status): 반복 다운로드 요청 인스턴스의 상태를 가져옵니다.
- [RequestStatus](https://developer.apple.com/documentation/appdatatransfer/requeststatus): 다운로드 요청의 상태를 나타내는 객체입니다.
:::

:::topic-grid
## 다운로드
- [Get one-time request download URLs](https://developer.apple.com/documentation/appdatatransfer/get-one-time-request-download-urls): 사용자의 데이터를 가져올 URL을 얻습니다.
- [Get recurring request download URLs](https://developer.apple.com/documentation/appdatatransfer/get-recurring-request-download-urls): 반복 시리즈에서 앱과 관련된 사용자 데이터 스냅샷을 다운로드할 URL을 얻습니다.
- [DownloadLinks](https://developer.apple.com/documentation/appdatatransfer/downloadlinks): 앱과 관련된 사용자 데이터를 다운로드할 URL을 담은 객체입니다.
- [DownloadError](https://developer.apple.com/documentation/appdatatransfer/downloaderror): 요청에 대한 다운로드 URL을 준비하는 동안 서버가 마주치는 오류를 설명하는 객체입니다.
:::

:::topic-grid
## 취소
- [Cancel request](https://developer.apple.com/documentation/appdatatransfer/cancel-request): 서버에 활성 요청 처리를 중단하라고 지시합니다.
- [CancellationRequest](https://developer.apple.com/documentation/appdatatransfer/cancellationrequest): 취소할 일회성 요청 또는 반복 요청의 개별 인스턴스를 식별하는 객체입니다.
- [CancellationResponse](https://developer.apple.com/documentation/appdatatransfer/cancellationresponse): 다운로드 요청 취소 결과를 설명하는 객체입니다.
:::
