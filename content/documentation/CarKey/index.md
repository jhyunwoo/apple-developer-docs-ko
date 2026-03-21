---
route: /documentation/CarKey
source_url: https://developer.apple.com/documentation/CarKey
source_locale: en-US
section: docc
content_type: symbol
title: CarKey
original_title: CarKey
source_hash: 974d935f03371f786397ddef8dee442319fafc1c847ec4f97026e1028b03f0d6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:28+00:00'
last_translated_at: '2026-03-13T17:10:00+09:00'
---

# CarKey

Wallet 앱에서 구성된 차량의 원격 키리스 기능에 접근합니다.

## 개요

CarKey 프레임워크는 사용자의 Apple Wallet에 이미 provision된 차량과 통신하는 방법을 제공합니다. 자동차 제조사는 차량을 지원하고 제어하는 앱에 이 프레임워크를 채택합니다. 예를 들어 앱이 차량을 잠그거나 잠금 해제하거나 파노라마 선루프를 열 때 사용할 수 있습니다. 차량을 원격으로 제어하려면 해당 차량에 대한 다음 정보가 필요합니다.

- 차량 각 기능의 function 식별자
- 기능에서 수행할 수 있는 각 action의 action 식별자
- action에 대한 응답으로 차량이 반환할 수 있는 execution status

Wallet 앱은 회사 제조사와 일치하고 사용자가 이전에 원격 접근용으로 구성한 차량 목록을 유지합니다. 이 차량들에 대한 정보를 얻고 범위 안에 있는 차량과 연결을 설정하려면 session 객체를 생성하십시오. session을 사용해 현재 사용자가 사용할 수 있는 명령 목록을 가져오고 앱에서 action을 시작합니다.

:::note Note
이 프레임워크를 사용하려면 앱에 `com.apple.developer.carkey.session` entitlement가 있어야 합니다. entitlement를 요청하려면 MFi Program에 등록된 자동차 제조사여야 합니다. 자세한 내용은 [https://developer.apple.com/mfi/](https://developer.apple.com/mfi/)를 참고하십시오.
:::

:::topic-grid
## 설정
- [CarKeyRemoteControl](https://developer.apple.com/documentation/carkey/carkeyremotecontrol): 새 차량 관련 session을 시작할 때 사용하는 객체입니다.
- [CarKeyRemoteControlSession](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession): 제조한 차량과의 통신을 관리하는 객체입니다.
- [CarKeyRemoteControlSessionDelegate](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsessiondelegate): 시스템에서 session 및 차량 관련 정보를 받을 때 사용하는 인터페이스입니다.
- [VehicleReport](https://developer.apple.com/documentation/carkey/vehiclereport): 사용자의 Apple Wallet에 원격 키리스 엔트리용으로 구성된 차량 정보를 담는 타입입니다.
:::

:::topic-grid
## 차량 동작
- [RemoteKeylessEntryAction](https://developer.apple.com/documentation/carkey/remotekeylessentryaction): 차량에 수행하려는 자동 종료 action입니다.
- [RemoteKeylessEntryEnduringAction](https://developer.apple.com/documentation/carkey/remotekeylessentryenduringaction): 선택적인 종료 지점을 갖는 차량 action입니다.
- [FunctionIdentifier](https://developer.apple.com/documentation/carkey/functionidentifier): 차량 기능 중 하나의 지정 코드를 저장하는 타입입니다.
- [ActionIdentifier](https://developer.apple.com/documentation/carkey/actionidentifier): 차량 기능이 지원하는 action 중 하나의 지정 코드를 저장하는 타입입니다.
:::

:::topic-grid
## 오류 코드
- [CarKeyErrorCode](https://developer.apple.com/documentation/carkey/carkeyerrorcode): 차량에서 원격 키리스 엔트리 작업을 수행할 때 발생할 수 있는 오류입니다.
:::

:::topic-grid
## 구조체
- [ExecutionStatus](https://developer.apple.com/documentation/carkey/executionstatus): 차량이 action을 실행한 뒤 반환하는 상태 코드를 담는 타입입니다.
- [RemoteKeylessEntryConfigurableEnduringAction](https://developer.apple.com/documentation/carkey/remotekeylessentryconfigurableenduringaction): 선택적인 종료 지점을 갖는 차량 action입니다.
:::
