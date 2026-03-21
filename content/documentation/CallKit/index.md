---
route: /documentation/CallKit
source_url: https://developer.apple.com/documentation/CallKit
source_locale: en-US
section: docc
content_type: symbol
title: CallKit
original_title: CallKit
source_hash: e5f8226988509857ab38c7c8f8bed6a796f0aa997bf1482088d8ec27ad780417
canonical_source: manual-translation
last_crawled_at: '2026-03-13T05:19:27+00:00'
last_translated_at: '2026-03-13T05:19:27+00:00'
---

# CallKit

앱의 VoIP 서비스에 시스템 통화 UI를 표시하고, 앱 및 시스템의 다른 호출 서비스와 조정합니다.

## 개요

CallKit을 사용해 시스템의 다른 통화 관련 앱과 여러분의 호출 서비스를 통합하세요. CallKit은 통화 인터페이스를 제공하고, VoIP 서비스와의 백엔드 통신은 앱이 처리합니다. 자세한 내용은 [Making and receiving VoIP calls](https://developer.apple.com/documentation/callkit/making-and-receiving-voip-calls)를 참고하세요.

수신 및 발신 통화에 대해 CallKit은 Phone 앱과 동일한 인터페이스를 표시하므로 앱이 더 네이티브한 모양과 느낌을 갖게 됩니다. CallKit은 또한 방해 금지 모드 같은 시스템 수준 동작에도 적절히 대응합니다.

통화 처리 외에도, Call Directory 앱 확장을 사용해 서비스와 연결된 발신자 ID 정보와 차단된 번호 목록을 제공할 수 있습니다. 자세한 내용은 [Identifying and blocking calls](https://developer.apple.com/documentation/callkit/identifying-and-blocking-calls)를 참고하세요.

### 사용자 개인정보 관리

사용자의 허가가 있으면 [SensorKit](https://developer.apple.com/documentation/SensorKit) entitlement를 사용하는 설치된 건강 연구 앱이 CallKit 앱 사용 중 Speech Metrics 데이터를 수집할 수 있습니다. 이를 방지하려면 [SRResearchDataGeneration](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SRResearchDataGeneration) 정보 프로퍼티 리스트 키를 `NO`로 설정할 수 있습니다.

:::important Important
사용자가 CallKit을 사용하는 앱에서 전화를 걸면, 앱은 수신자의 연락처 정보를 시스템에 제공합니다. 시스템은 그 정보를 Journal 앱이나 [Journaling Suggestions](https://developer.apple.com/documentation/JournalingSuggestions) 프레임워크를 사용하는 다른 앱에서 그 사람과의 소통을 제안으로 나타내는 데 사용할 수 있습니다.
:::

### 기본 통화 앱 되기

iOS 및 iPadOS 18.2 이상에서는 사용자가 Phone 앱이나 FaceTime이 아닌 다른 앱을 기본 통화 앱으로 선택할 수 있습니다. CallKit 또는 [LiveCommunicationKit](https://developer.apple.com/documentation/LiveCommunicationKit) 앱이 기본 통화 앱 설정을 지원하게 하려면 [Preparing your app to be the default calling app](https://developer.apple.com/documentation/callkit/preparing-your-app-to-be-the-default-calling-app)을 참고하세요.

:::topic-grid
## 핵심
- [CXProvider](https://developer.apple.com/documentation/callkit/cxprovider): 전화 통신 제공자를 나타내는 객체입니다.
- [CXProviderDelegate](https://developer.apple.com/documentation/callkit/cxproviderdelegate): 전화 통신 제공자 객체가 호출하는 메서드 모음입니다.
- [CXProviderConfiguration](https://developer.apple.com/documentation/callkit/cxproviderconfiguration): 제공자 객체의 구성을 캡슐화한 객체입니다.
- [Making and receiving VoIP calls](https://developer.apple.com/documentation/callkit/making-and-receiving-voip-calls): VoIP로 발신 통화를 시작하고 앱이 수신 통화를 받을 수 있도록 구성합니다.
- [VoIP calling with CallKit](https://developer.apple.com/documentation/callkit/voip-calling-with-callkit): CallKit 프레임워크를 사용해 네이티브 VoIP 통화를 통합합니다.
- [Preparing your app to be the default calling app](https://developer.apple.com/documentation/callkit/preparing-your-app-to-be-the-default-calling-app): 사용자가 기기에서 기본 통화 앱으로 설정할 수 있도록 CallKit 또는 LiveCommunicationKit 앱을 구성합니다.
- [CallKit updates](https://developer.apple.com/documentation/Updates/CallKit): CallKit의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 수신 통화
- [Responding to VoIP Notifications from PushKit](https://developer.apple.com/documentation/PushKit/responding-to-voip-notifications-from-pushkit): 수신 Voice-over-IP(VoIP) 푸시 알림을 받아 사용자에게 시스템 통화 인터페이스를 표시하는 데 사용합니다.
- [CXCallUpdate](https://developer.apple.com/documentation/callkit/cxcallupdate): 통화에 대한 새 정보와 변경된 정보를 캡슐화한 객체입니다.
- [CXAnswerCallAction](https://developer.apple.com/documentation/callkit/cxanswercallaction): 수신 전화를 받는 행위를 캡슐화한 객체입니다.
:::

:::topic-grid
## 발신 통화
- [Sending End-to-End Encrypted VoIP Calls](https://developer.apple.com/documentation/callkit/sending-end-to-end-encrypted-voip-calls): 메타데이터 암호화로 인해 서버가 발신 알림이 VoIP 통화 요청인지 판단할 수 없을 때 VoIP 통화를 시작합니다.
- [CXCallController](https://developer.apple.com/documentation/callkit/cxcallcontroller): 통화와 상호작용하고 이를 관찰하기 위한 프로그래밍 인터페이스입니다.
- [CXTransaction](https://developer.apple.com/documentation/callkit/cxtransaction): call controller가 수행할 0개 이상의 action 객체를 포함하는 객체입니다.
- [CXStartCallAction](https://developer.apple.com/documentation/callkit/cxstartcallaction): 발신 통화를 시작하는 행위를 캡슐화한 객체입니다.
:::

:::topic-grid
## 통화 관련 동작
- [CXAction](https://developer.apple.com/documentation/callkit/cxaction): 전화 통신 동작을 나타내는 객체를 위한 프로그래밍 인터페이스를 선언하는 추상 클래스입니다.
- [CXCallAction](https://developer.apple.com/documentation/callkit/cxcallaction): 통화 객체와 연관된 전화 통신 동작을 나타내는 객체를 위한 프로그래밍 인터페이스입니다.
- [CXEndCallAction](https://developer.apple.com/documentation/callkit/cxendcallaction): 통화를 종료하는 행위를 캡슐화한 객체입니다.
- [CXPlayDTMFCallAction](https://developer.apple.com/documentation/callkit/cxplaydtmfcallaction): DTMF(듀얼 톤 다중 주파수) 시퀀스를 재생하는 행위를 캡슐화한 객체입니다.
- [CXSetGroupCallAction](https://developer.apple.com/documentation/callkit/cxsetgroupcallaction): 통화를 그룹화하거나 그룹 해제하는 행위를 캡슐화한 객체입니다.
- [CXSetHeldCallAction](https://developer.apple.com/documentation/callkit/cxsetheldcallaction): 통화를 보류 상태로 두거나 보류에서 해제하는 행위를 캡슐화한 객체입니다.
- [CXSetMutedCallAction](https://developer.apple.com/documentation/callkit/cxsetmutedcallaction): 통화를 음소거하거나 음소거 해제하는 행위를 캡슐화한 객체입니다.
- [CXSetTranslatingCallAction](https://developer.apple.com/documentation/callkit/cxsettranslatingcallaction): 통화를 번역하는 행위를 캡슐화한 객체입니다.
:::

:::topic-grid
## 통화 정보
- [CXCall](https://developer.apple.com/documentation/callkit/cxcall): 전화 통화입니다.
- [CXCallObserver](https://developer.apple.com/documentation/callkit/cxcallobserver): 활성 통화 목록을 관리하고 통화 변경을 관찰하는 객체를 위한 프로그래밍 인터페이스입니다.
- [CXCallObserverDelegate](https://developer.apple.com/documentation/callkit/cxcallobserverdelegate): 통화 상태가 바뀔 때 시스템이 호출하는 메서드 모음입니다.
- [CXHandle](https://developer.apple.com/documentation/callkit/cxhandle): 전화번호나 이메일 주소처럼 통화 수신자에게 도달하는 방법입니다.
:::

:::topic-grid
## 발신자 ID
- [Identifying and blocking calls](https://developer.apple.com/documentation/callkit/identifying-and-blocking-calls): 전화번호를 기준으로 수신 발신자를 식별하고 차단하는 Call Directory 앱 확장을 만듭니다.
- [CXCallDirectoryProvider](https://developer.apple.com/documentation/callkit/cxcalldirectoryprovider): 호스트 앱용 Call Directory 앱 확장의 principal 객체입니다.
- [CXCallDirectoryExtensionContext](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontext): Call Directory 앱 확장에 식별 및 차단 항목을 추가하기 위한 프로그래밍 인터페이스입니다.
- [CXCallDirectoryExtensionContextDelegate](https://developer.apple.com/documentation/callkit/cxcalldirectoryextensioncontextdelegate): 요청이 실패할 때 Call Directory extension context 객체가 호출하는 메서드 모음입니다.
- [CXCallDirectoryManager](https://developer.apple.com/documentation/callkit/cxcalldirectorymanager): Call Directory 앱 확장을 관리하는 객체를 위한 프로그래밍 인터페이스입니다.
:::

:::topic-grid
## 레퍼런스
- [CallKit Enumerations](https://developer.apple.com/documentation/callkit/callkit-enumerations)
- [CallKit Constants](https://developer.apple.com/documentation/callkit/callkit-constants)
:::
