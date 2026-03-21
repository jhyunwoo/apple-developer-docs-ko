---
route: /documentation/LiveCommunicationKit
source_url: https://developer.apple.com/documentation/LiveCommunicationKit
source_locale: en-US
section: docc
content_type: symbol
title: LiveCommunicationKit
original_title: LiveCommunicationKit
source_hash: 342ba8abd5d392d9d4414a702f4e3a1bd6a0b2980857efe7e77d80a5a251d9d2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:39:21+00:00'
last_translated_at: '2026-03-14T01:09:00+09:00'
---

# LiveCommunicationKit

VoIP 및 셀룰러 대화를 시작하고 처리하며, 이를 다른 통신 앱 및 시스템과 조정하고, 기본 통화 앱 또는 다이얼러 앱이 될 준비를 합니다.

## 개요

LiveCommunicationKit을 사용하면 앱에서 VoIP 대화 기능을 제공하고, 시스템 안의 다른 통신 앱과 통신 서비스를 통합할 수 있습니다. LiveCommunicationKit을 사용하면 앱에서 다음을 수행할 수 있습니다.

- VoIP 대화를 시작하고 수신합니다.
- 셀룰러 네트워크 대화를 시스템으로 전달합니다.

앱에서 LiveCommunicationKit을 사용하면 사용자가 자신의 기기에서 앱을 기본 다이얼러 앱 또는 기본 통화 앱으로 설정할 수 있습니다.

### 사용자 개인 정보 보호 관리

사용자의 허가가 있으면 [SensorKit](https://developer.apple.com/documentation/SensorKit) entitlement를 사용하는 설치된 건강 연구 앱이 LiveCommunicationKit 앱이 사용 중일 때 Speech Metrics 데이터를 수집할 수 있습니다. 이를 방지하려면 [SRResearchDataGeneration](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SRResearchDataGeneration) 정보 property list 키를 `NO`로 설정하십시오.

:::important Important
LiveCommunicationKit을 사용하는 앱에서 사용자가 대화를 시작하면, 앱은 수신자의 연락처 정보를 시스템에 제공합니다. 시스템은 이 정보를 사용해 해당 인물과의 통신을 Journal 앱이나 [Journaling Suggestions](https://developer.apple.com/documentation/JournalingSuggestions) 프레임워크를 사용하는 다른 앱에서 제안으로 표시할 수 있습니다.
:::

:::topic-grid
## 핵심 사항
- [Initiating VoIP conversations with LiveCommunicationKit](https://developer.apple.com/documentation/livecommunicationkit/initiating-voip-conversations-with-livecommunicationkit): 사용자가 VoIP 대화를 시작하고 받을 수 있게 하며, 앱이 사용자의 기기에서 기본 통화 앱이 될 수 있도록 구성합니다.
- [Preparing your app to be the default dialer app](https://developer.apple.com/documentation/livecommunicationkit/preparing-your-app-to-be-the-default-dialer-app): 사용자가 자신의 기기에서 앱을 기본 다이얼러 앱으로 설정할 수 있게 합니다.
- [LiveCommunicationKit updates](https://developer.apple.com/documentation/Updates/LiveCommunicationKit): LiveCommunicationKit의 중요한 변경 사항을 알아봅니다.
:::

:::topic-grid
## 셀룰러 네트워크 대화
- [TelephonyConversationManager](https://developer.apple.com/documentation/livecommunicationkit/telephonyconversationmanager): 셀룰러 네트워크 대화를 시작하기 위한 인터페이스입니다.
- [StartCellularConversationAction](https://developer.apple.com/documentation/livecommunicationkit/startcellularconversationaction): 기본 통화 앱을 사용해 셀룰러 대화를 시작하는 action입니다.
- [CellularService](https://developer.apple.com/documentation/livecommunicationkit/cellularservice): 대화를 시작하거나 참가할 때 사용할 셀룰러 서비스 계정을 나타내는 구조체입니다.
- [Handle](https://developer.apple.com/documentation/livecommunicationkit/handle): 전화번호나 이메일 주소처럼 참가자에게 도달할 수 있는 방법입니다.
:::

:::topic-grid
## VoIP 대화
- [ConversationManager](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager): VoIP 대화를 관리하고 관찰하는 인터페이스입니다.
- [ConversationManagerDelegate](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate): 대화를 관리하고 VoIP 대화 업데이트를 받을 때 사용하는 메서드입니다.
- [ConversationHistoryManager](https://developer.apple.com/documentation/livecommunicationkit/conversationhistorymanager): 대화 기록을 관리하고 제공하는 인터페이스입니다.
- [Conversation](https://developer.apple.com/documentation/livecommunicationkit/conversation): 비디오 또는 오디오 대화를 설명하는 타입입니다.
:::

:::topic-grid
## 대화 action
- [ConversationAction](https://developer.apple.com/documentation/livecommunicationkit/conversationaction): 대화용 action을 나타내는 타입입니다.
- [EndConversationAction](https://developer.apple.com/documentation/livecommunicationkit/endconversationaction): 로컬 참가자를 대화에서 제거하고 모든 오디오 및 비디오 스트림을 중지하는 action입니다.
- [JoinConversationAction](https://developer.apple.com/documentation/livecommunicationkit/joinconversationaction): 수신 대화에 참가하는 action입니다.
- [MergeConversationAction](https://developer.apple.com/documentation/livecommunicationkit/mergeconversationaction): 서로 분리된 두 대화를 하나로 합치는 action입니다.
- [MuteConversationAction](https://developer.apple.com/documentation/livecommunicationkit/muteconversationaction): 대화를 음소거하거나 음소거 해제하는 action입니다.
- [PauseConversationAction](https://developer.apple.com/documentation/livecommunicationkit/pauseconversationaction): 대화의 모든 오디오 및 비디오 스트림을 중지하거나 다시 시작하는 action입니다.
- [PlayToneAction](https://developer.apple.com/documentation/livecommunicationkit/playtoneaction): 대화 참가자가 키패드와 상호 작용했음을 알리기 위해 톤 시퀀스를 재생하는 action입니다.
- [SetTranslatingAction](https://developer.apple.com/documentation/livecommunicationkit/settranslatingaction): 번역을 시작하거나 중지하는 action입니다.
- [StartConversationAction](https://developer.apple.com/documentation/livecommunicationkit/startconversationaction): 발신 대화를 시작하고 원격 참가자의 기기를 울리게 하는 action입니다.
- [UnmergeConversationAction](https://developer.apple.com/documentation/livecommunicationkit/unmergeconversationaction): 이전에 병합한 두 대화를 다시 분리하는 action입니다.
:::
