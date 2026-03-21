---
route: /documentation/HomeKit
source_url: https://developer.apple.com/documentation/HomeKit
source_locale: en-US
section: docc
content_type: symbol
title: HomeKit
original_title: HomeKit
source_hash: e12245a3045dcca3e6a8449cca7836b2829b8742c49d77414d4852aa7527cf42
canonical_source: manual-translation
last_crawled_at: '2026-03-13T02:53:03+00:00'
last_translated_at: '2026-03-13T02:53:03+00:00'
---

# HomeKit

홈 자동화 액세서리를 구성하고, 제어하고, 통신합니다.

## 개요

HomeKit은 앱이 여러 공급업체의 홈 자동화 액세서리를 조정하고 제어하여, 일관되고 사용자 중심적인 인터페이스를 제공할 수 있게 해 줍니다.

![중앙의 집 아이콘과 통신하고 있음을 나타내기 위해 파형을 내보내는 스타일화된 전화기가 그려진 도식입니다. 집 아이콘 오른쪽에는 반원 형태로 네 개의 아이콘이 배치되어 있으며, 차고 문, 온도계, 슬라이드형 전등 스위치, 램프 같은 연결된 액세서리를 나타냅니다.](https://developer.apple.com)

HomeKit을 사용하면 앱에서 다음을 수행할 수 있습니다:

- HomeKit과 호환되는 자동화 액세서리를 검색하고, 이를 지속적이며 기기 간에 공유되는 홈 구성 데이터베이스에 추가합니다.
- 홈 구성 데이터베이스의 데이터를 표시하고, 편집하고, 그에 따라 동작합니다.
- 구성된 액세서리 및 서비스와 통신하여 거실의 조명을 켜는 것과 같은 동작을 수행합니다.

:::topic-grid
## 핵심
- [Enabling HomeKit in your app](https://developer.apple.com/documentation/homekit/enabling-homekit-in-your-app): 앱이 HomeKit을 사용하려는 의도를 선언하고, 사용자가 홈 자동화 액세서리에 접근할 수 있도록 권한을 요청합니다.
- [HomeKit Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.homekit): 앱 사용자가 HomeKit 호환 액세서리를 관리할 수 있는지를 나타내는 Boolean 값입니다.
- [NSHomeKitUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHomeKitUsageDescription): 앱이 사용자의 HomeKit 구성 데이터에 접근 권한을 요청하는 이유를 알려 주는 메시지입니다.
:::

:::topic-grid
## 홈 관리자
- [Configuring a home automation device](https://developer.apple.com/documentation/homekit/configuring-a-home-automation-device): 사용자가 HomeKit 액세서리를 관리할 때 익숙한 경험을 제공하세요.
- [Testing your app with the HomeKit Accessory Simulator](https://developer.apple.com/documentation/homekit/testing-your-app-with-the-homekit-accessory-simulator): HomeKit이 활성화된 앱의 디버깅을 돕기 위해 HomeKit Accessory Simulator를 설치합니다.
- [HMHomeManager](https://developer.apple.com/documentation/homekit/hmhomemanager): 사용자의 하나 이상의 홈 컬렉션을 관리하는 관리자입니다.
:::

:::topic-grid
## 액세서리
- [HMAccessorySetupManager](https://developer.apple.com/documentation/homekit/hmaccessorysetupmanager): 새 액세서리를 설정하는 객체입니다.
- [HMAccessorySetupResult](https://developer.apple.com/documentation/homekit/hmaccessorysetupresult): 성공한 액세서리 설정 요청에 대한 정보를 설명하는 결과 객체입니다.
- [HMAccessorySetupRequest](https://developer.apple.com/documentation/homekit/hmaccessorysetuprequest): 새 액세서리를 추가하고 설정하는 방법을 설명하는 객체입니다.
- [Interacting with a home automation network](https://developer.apple.com/documentation/homekit/interacting-with-a-home-automation-network): 기본 홈에 있는 모든 자동화 액세서리를 찾고 그 상태를 제어합니다.
- [HMAccessory](https://developer.apple.com/documentation/homekit/hmaccessory): 차고 문 개폐기나 온도 조절기 같은 홈 자동화 액세서리입니다.
- [HMService](https://developer.apple.com/documentation/homekit/hmservice): 차고 문 개폐기에 연결된 조명처럼 액세서리의 제어 가능한 기능입니다.
- [HMCharacteristic](https://developer.apple.com/documentation/homekit/hmcharacteristic): 조광 가능한 조명의 밝기나 색온도처럼 서비스의 구체적인 특성입니다.
- [HMMediaSourceDisplayOrderProfile](https://developer.apple.com/documentation/homekit/hmmediasourcedisplayorderprofile): 입력 소스의 순서를 읽고, 액세서리에서 허용하는 경우 그 순서를 업데이트할 수 있는 인터페이스입니다.
:::

:::topic-grid
## 동작 세트
- [HMActionSet](https://developer.apple.com/documentation/homekit/hmactionset): 그룹으로 트리거하는 동작의 컬렉션입니다.
- [HMTimerTrigger](https://developer.apple.com/documentation/homekit/hmtimertrigger): 주기적인 타이머를 기준으로 동작 세트를 활성화하는 트리거입니다.
- [HMEventTrigger](https://developer.apple.com/documentation/homekit/hmeventtrigger): 이벤트 집합과 선택적 조건을 기준으로 동작 세트를 활성화하는 트리거입니다.
:::

:::topic-grid
## 오류
- [HMError](https://developer.apple.com/documentation/homekit/hmerror): HomeKit이 반환하는 오류입니다.
- [HMErrorDomain](https://developer.apple.com/documentation/homekit/hmerrordomain): HomeKit 오류 도메인을 식별하는 문자열입니다.
- [HMError.Code](https://developer.apple.com/documentation/homekit/hmerror/code): HomeKit API에서 반환될 수 있는 가능한 오류 값입니다.
- [HMErrorBlock](https://developer.apple.com/documentation/homekit/hmerrorblock): 오류를 제공하는 completion block입니다.
:::

:::topic-grid
## 클래스
- [HMAccessorySetupPayload](https://developer.apple.com/documentation/homekit/hmaccessorysetuppayload): HomeKit 액세서리를 인증하기 위한 페이로드입니다.
:::
