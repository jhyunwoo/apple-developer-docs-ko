---
route: /documentation/CoreTelephony
source_url: https://developer.apple.com/documentation/CoreTelephony
source_locale: en-US
section: docc
content_type: symbol
title: Core Telephony
original_title: Core Telephony
source_hash: 9545c876404b6b61a0918bb0659889aada85433944834b3490749228fcb53547
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:48:38+00:00'
last_translated_at: '2026-03-13T21:12:00+09:00'
---

# Core Telephony

사용자의 이동통신 서비스 제공자에 대한 정보(예: 고유 식별자, 해당 통신사가 VoIP를 허용하는지 여부)에 접근합니다.

## 개요

Core Telephony 프레임워크를 사용하면 사용자의 홈 이동통신 서비스 제공자에 대한 정보를 얻을 수 있습니다. 통신사는 이 정보를 사용해 자신의 가입자에게만 서비스를 제공하는 앱을 만들 수 있습니다. 이 프레임워크를 사용해 현재 진행 중인 셀룰러 통화에 대한 정보를 얻는 것도 가능합니다.

[CTCarrier](https://developer.apple.com/documentation/coretelephony/ctcarrier) 객체는 사용자의 이동통신 서비스 제공자에 대한 정보, 예를 들어 해당 네트워크에서 VoIP(Voice over Internet Protocol) 사용을 허용하는지 여부를 제공합니다. [CTCall](https://developer.apple.com/documentation/coretelephony/ctcall) 객체는 현재 통화에 대한 정보(고유 식별자와 발신 중, 수신 중, 연결됨, 연결 해제됨 같은 상태 정보 포함)를 제공합니다.

:::note 참고
visionOS에서 실행되는 호환 iPad 및 iPhone 앱에서는 Core Telephony를 통한 VoIP와 셀룰러 서비스를 사용할 수 없습니다. 이 프레임워크의 API 자체는 계속 사용할 수 있지만, 서비스는 통신사 정보를 반환하지 않습니다.
:::

:::topic-grid
## 서비스 정보
- [CTTelephonyNetworkInfo](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo): 사용자의 이동통신 서비스 제공자 변경 알림을 제공하는 객체입니다.
:::

:::topic-grid
## eSIM
- [CTCellularPlanProvisioning](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioning): 통신사 eSIM을 다운로드하고 설치할 때 사용하는 객체입니다.
- [CTCellularPlanProvisioningRequest](https://developer.apple.com/documentation/coretelephony/ctcellularplanprovisioningrequest): 다운로드하고 설치할 eSIM을 지정하는 요청입니다.
- [CTCellularPlanProperties](https://developer.apple.com/documentation/coretelephony/ctcellularplanproperties): eSIM에 사용하는 객체입니다.
- [CTCellularPlanCapability](https://developer.apple.com/documentation/coretelephony/ctcellularplancapability): eSIM에 사용할 수 있는 셀룰러 요금제 유형입니다.
:::

:::topic-grid
## SIM
- [CTCellularPlanStatus](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus): 토큰을 검색하고 그 유효성을 확인하는 데 사용하는 객체입니다.
:::

:::topic-grid
## 가입자 정보
- [CTSubscriber](https://developer.apple.com/documentation/coretelephony/ctsubscriber): 셀룰러 네트워크 가입자입니다.
- [CTSubscriberDelegate](https://developer.apple.com/documentation/coretelephony/ctsubscriberdelegate): 가입자 정보 변경을 처리하는 프로토콜입니다.
- [CTSubscriberInfo](https://developer.apple.com/documentation/coretelephony/ctsubscriberinfo): 셀룰러 네트워크 가입자 배열을 제공하는 객체입니다.
:::

:::topic-grid
## 셀룰러 데이터 접근
- [CTCellularData](https://developer.apple.com/documentation/coretelephony/ctcellulardata): 앱이 셀룰러 데이터에 접근할 수 있는지를 나타내는 객체입니다.
:::

:::topic-grid
## 네트워크 슬라이싱
- [CTSlicingManager](https://developer.apple.com/documentation/coretelephony/ctslicingmanager): 셀룰러 네트워크 트래픽 라우팅을 제어하고 모니터링하기 위한 네트워크 슬라이싱 기능을 제공하는 관리자입니다.
:::

:::topic-grid
## 오류
- [CTError](https://developer.apple.com/documentation/coretelephony/cterror): Core Telephony 오류를 나타내는 타입입니다.
:::

:::topic-grid
## 더 이상 사용되지 않음
- [CTCarrier](https://developer.apple.com/documentation/coretelephony/ctcarrier): 고유 식별자나 해당 네트워크에서 VoIP 통화를 허용하는지 여부 같은 사용자의 이동통신 서비스 제공자 정보를 나타냅니다.
- [CTCall](https://developer.apple.com/documentation/coretelephony/ctcall): 셀룰러 통화를 식별하고 상태를 확인하는 데 사용하는 객체입니다.
- [CTCallCenter](https://developer.apple.com/documentation/coretelephony/ctcallcenter): 현재 셀룰러 통화 목록을 제공하고 통화 상태 변경에 대응하는 기능을 제공하는 객체입니다.
:::
