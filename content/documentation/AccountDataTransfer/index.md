---
route: /documentation/AccountDataTransfer
source_url: https://developer.apple.com/documentation/AccountDataTransfer
source_locale: en-US
section: docc
content_type: symbol
title: Account Data Transfer
original_title: Account Data Transfer
source_hash: 5552b612aee38d8bb3e1937afe10ee9e426f7f9ed9e7678923a8890a2900b46c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:59:24+00:00'
last_translated_at: '2026-03-14T02:52:00+09:00'
---

# Account Data Transfer

앱을 사용하는 사람을 대신해 App Store 정보, 앱 설치 활동, push notification 활동을 다운로드합니다.

## 개요

Account Data Transfer 웹 API를 사용해 앱을 사용하는 사람들에 대한 정보를 요청하고 다운로드하십시오. 제공되는 데이터는 Apple App Store 사용과 관련되며, 이전 거래와 다운로드 같은 정보를 포함합니다. 또한 앱 설치 및 push notification 활동과 관련된 정보도 포함합니다.

## scope 이해하기

scope는 데이터 제공에 동의한 개인의 승인을 바탕으로, 앱과 웹사이트가 하나의 Apple Account에서 접근할 수 있는 데이터의 하위 집합을 식별합니다. 앱과 웹사이트에 해당하는 scope만 선택하십시오.

### 사용자 정보 scope

다른 scope에 대한 접근을 요청할 때 개발자 포털은 자동으로 `data-transfer-user-profile` scope를 선택합니다.

:::term-list
`data-transfer-user-profile`: 사용자에 대한 App Store 정보, 앱 설치 활동, push notification 활동 같은 하나 이상의 scope를 요청할 때 사용하는 읽기 전용 scope입니다.
:::

### App Store 정보 scope

:::term-list
`appstore-info-account-data-for-EU-users`: EU 사용자에 대한 App Store 계정 정보에 접근할 때 사용하는 읽기 전용 scope입니다.
`appstore-info-account-data-for-JP-users`: 일본 사용자에 대한 App Store 계정 정보에 접근할 때 사용하는 읽기 전용 scope입니다.
`appstore-info-account-data-for-UK-users`: 영국 사용자에 대한 App Store 계정 정보에 접근할 때 사용하는 읽기 전용 scope입니다.
:::

:::note Note
이전에 `appstore-user-profile` scope와 예전 scope 이름을 함께 사용해 App Store 정보 접근을 요청한 적이 있다면, 시스템은 이러한 scope를 받아들이고 EU 및 UK scope 모두에 대해 자동 승인합니다. 새 token 요청을 다시 만들 필요는 없습니다.
:::

### 앱 설치 및 push notification 활동 scope

:::term-list
`app-install-activity-account-data-for-EU-users`: EU 사용자에 대한 앱 설치 및 push notification 활동에 접근할 때 사용하는 읽기 전용 scope입니다.
`app-install-activity-account-data-for-JP-users`: 일본 사용자에 대한 앱 설치 및 push notification 활동에 접근할 때 사용하는 읽기 전용 scope입니다.
`app-install-activity-account-data-for-UK-users`: 영국 사용자에 대한 앱 설치 및 push notification 활동에 접근할 때 사용하는 읽기 전용 scope입니다.
:::

## 특정 scope에 대한 권한 요청하기

App ID 또는 Services ID가 EU, 영국, 일본 사용자에 대한 App Store 정보와 앱 설치 및 push notification scope를 요청할 수 있도록 권한을 얻으려면 [Request access to the Account Data Transfer API](https://developer.apple.com/contact/request/account-data-transfer-api/)의 안내를 따르십시오.

:::note Note
이 API는 EU, 영국, 일본 사용자에 대한 account data를 반환합니다. 앱 개발자이며 App Store 정보, 앱 설치 또는 앱의 push notification 활동과 관련된 데이터를 대신 전송해야 한다면 [App Data Transfer](https://developer.apple.com/documentation/AppDataTransfer) API를 사용하십시오. Account Data Transfer API 접근을 요청했고 Apple이 이를 승인했다면, App Data Transfer API의 authorization token을 요청할 때 `consent_mode` query parameter를 제공할 필요가 없습니다.

이 API에서 제공되는 데이터에 대해 궁금한 점이 있다면, Apple이 사용자 개인 정보를 보호하기 위해 어떤 privacy measure를 적용하고 법적 의무를 어떻게 준수하는지에 대한 질문을 포함해, Feedback Assistant에서 다음 항목을 선택해 Apple에 문의하십시오.

Developer Tools & Resources > Account Data Transfer API > Data Request

[Feedback Assistant 사용 방법](https://support.apple.com/guide/feedback-assistant/welcome/mac)을 더 알아보십시오.
:::

### scope 유형 간 차이 이해하기

요청을 만들 때는 어떤 scope를 한 요청 안에서 함께 결합할 수 있는지, 어떤 scope는 별도로 요청해야 하는지, 어떤 요청은 일회성이고 어떤 요청은 일회성 또는 반복 요청이 가능한지를 이해하는 것이 중요합니다. 다음 표는 사용 가능한 scope 간 관계를 설명합니다.

| Scope | 동일한 요청에 추가할 수 있는 scope | 요청 빈도 |
| --- | --- | --- |
| `app-install-activity-account-data-for-EU-users` | `appstore-info-account-data-for-EU-users` | 일회성 및 반복 |
| `app-install-activity-account-data-for-UK-users` | `appstore-info-account-data-for-UK-users` | 일회성 및 반복 |
| `appstore-info-account-data-for-EU-users` | `app-install-activity-account-data-for-EU-users` | 일회성 및 반복 |
| `appstore-info-account-data-for-UK-users` | `app-install-activity-account-data-for-UK-users` | 일회성 및 반복 |
| `appstore-info-account-data-for-JP-users` | `app-install-activity-account-data-for-JP-users` | 일회성 및 반복 |
| `app-install-activity-account-data-for-JP-users` | `appstore-info-account-data-for-JP-users` | 일회성 및 반복 |

## 요청한 scope에 필요한 HTTP header 설정하기

:::term-list
`X-Apple-Transaction-Id`: 요청을 고유하게 식별하는 UUID로 값을 설정합니다. Apple 지원이 필요해 Apple에 문의할 경우 도움이 필요한 요청의 UUID를 함께 전달하십시오.
`Authorization`: 앱이 `data-transfer-user-profile` scope 및 관련된 하나 이상의 App Store 정보, 앱 설치 및 push notification, 또는 registration and activation scope로 데이터를 가져올 권한이 있음을 나타내기 위해 값을 `Bearer <ACCESS_TOKEN>`으로 설정합니다.
:::

### 요청 빈도 설정하기

[Submit request](https://developer.apple.com/documentation/accountdatatransfer/submit-request) endpoint에 HTTP `POST` 요청을 만들 때, App Store 또는 앱 설치 활동 scope를 요청하는 경우 지정한 scope에 따라 일회성 또는 반복 요청을 선택할 수 있습니다.

일회성 요청을 만들려면 `mode` key를 `ONE_TIME`으로 설정합니다. 앱 설치 또는 push notification 활동에 대한 반복 요청을 만들려면 다음 값 중 하나를 사용합니다.

:::term-list
`DAILY_30`: 30일 동안 매일 한 번 반복 요청
`WEEKLY_180`: 180일 동안 매주 한 번 반복 요청
:::

:::note Note
이미 대기 중인 반복 요청이 있을 때 또 다른 반복 요청을 만들면, 시스템은 기존 요청의 ID와 함께 오류를 반환합니다.
:::

### 서버 요청 ID와 delay 값 저장하기

Apple 서버는 요청 ID를 반환하며, 이 값은 요청 상태를 가져오거나, 다운로드 URL을 요청하거나, 요청을 취소할 때 사용합니다. 반복 요청의 경우 Apple 서버는 요청 ID와 함께 반복 요청 시리즈를 식별하는 parent ID도 반환합니다.

서버 응답에는 `statusCheckDelay`도 포함되며, 이는 요청 상태를 확인하기 전에 기다려야 하는 초 수입니다. 이 시간 이전에는 [Cancel request](https://developer.apple.com/documentation/accountdatatransfer/cancel-request) endpoint에 `POST` 요청을 보내 요청을 취소할 수 있습니다.

`DAILY_30` 반복 요청을 제출하고 이후 각 날짜에 반복 인스턴스를 다시 제출하지 않으면, 최초 요청 제출 후 40일이 지나면 반복 요청이 만료됩니다.

`WEEKLY_180` 반복 요청을 제출하고 이후 각 주에 반복 인스턴스를 다시 제출하지 않으면, 최초 요청 제출 후 190일이 지나면 반복 요청이 만료됩니다.

## 요청 상태 찾기

제출한 요청에 대응하는 데이터는 즉시 사용 가능하지 않습니다. status-check delay가 지난 뒤 [Get one-time request status](https://developer.apple.com/documentation/accountdatatransfer/get-one-time-request-status) 또는 [Get recurring request status](https://developer.apple.com/documentation/accountdatatransfer/get-recurring-request-status)에 `GET` 요청을 보내십시오. 요청한 보고서 scope에 맞는 endpoint를 사용하고 경로에 요청 식별자를 포함합니다.

job status가 `completed` 또는 `completed_with_error`이면, 요청과 연결된 데이터는 다운로드할 준비가 된 것입니다.

## 데이터 전송하기

완료된 요청의 다운로드 URL을 가져오려면 [Get one-time request download URLs](https://developer.apple.com/documentation/accountdatatransfer/get-one-time-request-download-urls) 또는 [Get recurring request download URLs](https://developer.apple.com/documentation/accountdatatransfer/get-recurring-request-download-urls)에 `GET` 요청을 보내고, 경로에 요청 식별자를 포함합니다.

응답에는 사용자의 데이터를 가져오기 위해 `GET` 요청을 보낼 URL 목록이 포함됩니다.

다운로드 URL은 다운로드 요청이 완료된 후 3일 동안 사용할 수 있습니다. 제공된 URL은 요청한 시점부터 15분 동안 유효합니다.

다운로드하는 파일 안의 콘텐츠와 용어에 대한 정보는 [Data and Privacy](https://privacy.apple.com/file-guides/transfer/accountdata)를 참고하십시오.

## 반복 요청 다시 제출하기

앱 설치 또는 push notification 요청의 경우 [Resubmit request](https://developer.apple.com/documentation/accountdatatransfer/resubmit-request) endpoint에 `POST` 요청을 보내 반복 요청의 다음 인스턴스를 queue에 추가합니다. 요청에는 parent request identifier와 가장 최근 인스턴스의 request identifier를 포함하십시오.

서버 응답에는 새 요청의 request identifier와, 새 요청 상태를 확인하기 전에 기다려야 하는 delay가 포함됩니다.

:::topic-grid
## 요청 생성
- [Submit request](https://developer.apple.com/documentation/accountdatatransfer/submit-request): 사용자의 데이터를 다운로드할 수 있도록 준비를 시작합니다.
- [JobSubmission](https://developer.apple.com/documentation/accountdatatransfer/jobsubmission): 사용자의 데이터를 요청하는 submission을 설명하는 객체입니다.
- [CreatedJob](https://developer.apple.com/documentation/accountdatatransfer/createdjob): 새로 생성된 다운로드 요청을 나타내는 객체입니다.
- [Resubmit request](https://developer.apple.com/documentation/accountdatatransfer/resubmit-request): 반복 요청의 다음 인스턴스를 queue에 넣습니다.
- [ResubmissionRequest](https://developer.apple.com/documentation/accountdatatransfer/resubmissionrequest): 반복 다운로드 요청을 다시 제출하기 위한 요청을 설명하는 객체입니다.
- [ResubmissionResponse](https://developer.apple.com/documentation/accountdatatransfer/resubmissionresponse): 다시 제출된 반복 다운로드 요청을 나타내는 객체입니다.
:::

:::topic-grid
## 상태
- [Get one-time request status](https://developer.apple.com/documentation/accountdatatransfer/get-one-time-request-status): 일회성 다운로드 요청의 상태를 찾습니다.
- [Get recurring request status](https://developer.apple.com/documentation/accountdatatransfer/get-recurring-request-status): 반복 다운로드 요청 인스턴스의 상태를 가져옵니다.
- [RequestStatus](https://developer.apple.com/documentation/accountdatatransfer/requeststatus): 다운로드 요청의 상태를 나타내는 객체입니다.
:::

:::topic-grid
## 다운로드
- [Get one-time request download URLs](https://developer.apple.com/documentation/accountdatatransfer/get-one-time-request-download-urls): 사용자의 데이터를 가져오기 위한 URL을 얻습니다.
- [Get recurring request download URLs](https://developer.apple.com/documentation/accountdatatransfer/get-recurring-request-download-urls): 반복 시리즈에서 사용자의 데이터 스냅샷을 다운로드하기 위한 URL을 얻습니다.
- [DownloadLinks](https://developer.apple.com/documentation/accountdatatransfer/downloadlinks): 사용자의 account data를 다운로드하기 위한 URL을 담는 객체입니다.
- [DownloadError](https://developer.apple.com/documentation/accountdatatransfer/downloaderror): 서버가 요청에 대한 다운로드 URL을 준비하는 동안 마주친 오류를 설명하는 객체입니다.
:::

:::topic-grid
## 취소
- [Cancel request](https://developer.apple.com/documentation/accountdatatransfer/cancel-request): 서버가 활성 요청 처리를 중지하도록 지시합니다.
- [CancellationRequest](https://developer.apple.com/documentation/accountdatatransfer/cancellationrequest): 취소할 일회성 요청 또는 반복 요청의 개별 인스턴스를 식별하는 객체입니다.
- [CancellationResponse](https://developer.apple.com/documentation/accountdatatransfer/cancellationresponse): 다운로드 요청 취소 결과를 설명하는 객체입니다.
:::
