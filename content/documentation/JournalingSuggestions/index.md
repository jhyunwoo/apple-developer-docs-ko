---
route: /documentation/JournalingSuggestions
source_url: https://developer.apple.com/documentation/JournalingSuggestions
source_locale: en-US
section: docc
content_type: symbol
title: Journaling Suggestions
original_title: Journaling Suggestions
source_hash: c647f85fac97841c567936c97f068015397e34b458790107ebd2d69ac5d83479
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:08:41+00:00'
last_translated_at: '2026-03-14T00:28:00+09:00'
---

# Journaling Suggestions

누군가가 앱의 창작 워크플로에 기여하도록 영감을 주는 최근의 개인적 사건 모음을 표시합니다.

## 개요

Journaling Suggestions는 iPhone 앱을 위한 시각적 picker 인터페이스를 제공합니다. 이 picker는 사용자가 방문한 장소, 연락한 사람, 사진 보관함의 사진, 반복해서 재생한 노래처럼 누군가의 삶에서 일어나는 개인적인 사건을 표시합니다.

앱이 개인적인 글쓰기를 지원한다면, picker를 표시해 사용자가 창작 콘텐츠에 대한 아이디어를 얻도록 도울 수 있습니다. 사용자가 picker에서 suggestion 하나를 선택하면, 시스템은 해당 사건에 대한 고수준 세부 정보를 앱에 제공합니다. 예를 들어 journaling 앱은 이 세부 정보를 사용해 선택된 suggestion에 대한 새 저널 항목의 시작 부분을 표시할 수 있습니다.

![왼쪽에서 오른쪽으로 진행되는 앱 워크플로를 보여 주는 두 개의 iPhone 프레임 그림입니다. 왼쪽 프레임은 꽃 사진을 포함한 여러 사진 썸네일과 함께 Highlights from Photo Memories라는 텍스트를 보여 주며, 아래에는 Suggestions picker라는 callout이 있습니다. 오른쪽 프레임은 Coastal Hike라는 사용자 정의 텍스트 아래에 같은 꽃 썸네일의 상세 화면을 보여 주고, 이미지 아래 막대는 글쓰기 내용을 나타내며 아래에는 Journal entry라는 callout이 있습니다.](https://developer.apple.com)

앱에 suggestions picker([JournalingSuggestionsPicker](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker))를 통합하려면, 이를 [SwiftUI](https://developer.apple.com/documentation/SwiftUI)로 선언하고 picker를 표시하는 버튼의 텍스트를 선택하십시오.

Picker가 나타나려면 앱의 코드 서명에 특별한 entitlement가 필요합니다. 사용자가 picker에서 선택하여 공유하기 전까지는 앱이 suggestion의 세부 정보에 접근할 수 없으므로, 별도의 추가 권한을 요청할 필요는 없습니다.

:::note 참고
Mac Catalyst로 빌드한 Mac 앱은 사용자가 suggestions picker 버튼을 탭해도 입력을 무시합니다.
:::

:::topic-grid
## 핵심 사항
- [Journaling Suggestions updates](https://developer.apple.com/documentation/Updates/JournalingSuggestions): Journaling Suggestions의 중요한 변경 사항을 알아봅니다.
- [Presenting the suggestions picker and processing a selection](https://developer.apple.com/documentation/journalingsuggestions/presenting-the-suggestions-picker-and-processing-a-selection): journaling suggestions picker를 표시하고 사용자가 선택한 suggestion을 처리합니다.
- [com.apple.developer.journal.allow](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.journal.allow): 앱이 journaling suggestions picker를 표시할 수 있게 하는 entitlement입니다.
:::

:::topic-grid
## 구현
- [JournalingSuggestionsPicker](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker): 누군가의 삶에서 최근 일어난 여러 유형의 사건을 나열하는 view입니다.
- [JournalingSuggestion](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion): journaling suggestions picker에서 사용자가 선택한 suggestion에 대한 고수준 정보입니다.
- [JournalingSuggestionAsset](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionasset): suggestions picker가 표시하는 콘텐츠를 위한 인터페이스입니다.
:::

:::topic-grid
## 알림
- [Receiving journaling suggestions system notifications](https://developer.apple.com/documentation/journalingsuggestions/receiving-journaling-suggestions-from-system-notifications): 사용자가 시스템 알림을 탭했을 때 journaling suggestions를 수신하도록 앱을 등록합니다.
- [JournalingSuggestionPresentationToken](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionpresentationtoken): Journaling Suggestion 식별자를 담는 컨테이너입니다.
- [JournalingSuggestionsConfiguration](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionsconfiguration): Journaling Suggestion 알림의 구성입니다.
:::
