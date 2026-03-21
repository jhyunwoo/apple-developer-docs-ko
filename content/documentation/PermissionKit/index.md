---
route: /documentation/PermissionKit
source_url: https://developer.apple.com/documentation/PermissionKit
source_locale: en-US
section: docc
content_type: symbol
title: PermissionKit
original_title: PermissionKit
source_hash: 472d23f29abe8becad3c408e26c1d6f249442a56ee3a2f66c15d44ae61158d7f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:43:01+00:00'
last_translated_at: '2026-03-13T18:25:00+09:00'
---

# PermissionKit

자녀와 부모 또는 보호자 사이의 커뮤니케이션 경험을 생성합니다.

## 개요

앱에서 `PermissionKit`을 사용해 iCloud의 자녀 계정에 대한 커뮤니케이션 규칙을 조정할 수 있습니다. `PermissionKit`은 자녀와 부모 또는 보호자 사이에 일관된 요청 경험을 만들 수 있는 방법을 제공하며, 시스템 전반의 다른 커뮤니케이션 경험과 UI 일관성을 유지합니다.

:::important 중요
`PermissionKit` 프레임워크를 사용하는 커뮤니케이션 경험은 iMessage를 통해서만 사용할 수 있습니다.
:::

:::topic-grid
## 핵심 사항
- [Creating a communication experience](https://developer.apple.com/documentation/permissionkit/creating-a-communication-experience): 자녀의 커뮤니케이션 규칙을 수정하기 위해 부모 또는 보호자에게 권한을 요청합니다.
- [AskCenter](https://developer.apple.com/documentation/permissionkit/askcenter): 승인을 위해 부모 또는 보호자에게 보내는 권한 요청을 관리하는 클래스입니다.
- [PermissionQuestion](https://developer.apple.com/documentation/permissionkit/permissionquestion): 사람이 제기한 권한 질문을 캡처하는 클래스입니다.
:::

:::topic-grid
## 권한 주제
- [SignificantAppUpdateTopic](https://developer.apple.com/documentation/permissionkit/significantappupdatetopic): 중요한 앱 업데이트에 대한 권한을 요청하기 위한 주제입니다.
- [CommunicationTopic](https://developer.apple.com/documentation/permissionkit/communicationtopic): 특정 사람들과의 커뮤니케이션 권한을 요청하기 위한 주제입니다.
:::

:::topic-grid
## 표시
- [PermissionButton](https://developer.apple.com/documentation/permissionkit/permissionbutton): 자녀의 커뮤니케이션 제한에 대한 예외를 요청하기 위해 부모 또는 보호자에게 시스템 UI를 표시하는 버튼입니다.
:::

:::topic-grid
## 응답 관리
- [responses(for:)](https://developer.apple.com/documentation/permissionkit/askcenter/responses(for:)): 주제 타입을 시스템에 등록하고 응답의 비동기 시퀀스를 반환합니다.
- [PermissionResponse](https://developer.apple.com/documentation/permissionkit/permissionresponse): 원래 질문과 선택된 답변을 포함하는 전체 권한 응답입니다.
- [CommunicationHandle](https://developer.apple.com/documentation/permissionkit/communicationhandle): 사람을 식별하고 연락하는 데 사용하는 연락처 정보입니다.
- [PermissionChoice](https://developer.apple.com/documentation/permissionkit/permissionchoice): 특정하고 정적으로 정의된 권한 선택지를 고유하게 식별하는 클래스입니다.
- [CommunicationLimits](https://developer.apple.com/documentation/permissionkit/communicationlimits): 앱의 커뮤니케이션 제한을 캡슐화하는 타입입니다.
:::

:::topic-grid
## 지원 타입
- [QuestionTopic](https://developer.apple.com/documentation/permissionkit/questiontopic): 사람이 무엇을 요청하는지 해석하는 데 사용할 수 있는 질문 주제를 정의하는 프로토콜입니다.
:::

:::topic-grid
## 오류
- [AskError](https://developer.apple.com/documentation/permissionkit/askerror): 사람이 커뮤니케이션 권한 질문을 보내도록 요청할 때 마주치는 오류를 나타냅니다.
:::

:::topic-grid
## 지원 중단된 API
- [CommunicationLimitsButton](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton): 자녀의 커뮤니케이션 제한에 대한 예외를 요청하기 위해 부모 또는 보호자에게 시스템 UI를 표시하는 버튼입니다.
:::
