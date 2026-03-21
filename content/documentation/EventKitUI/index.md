---
route: /documentation/EventKitUI
source_url: https://developer.apple.com/documentation/EventKitUI
source_locale: en-US
section: docc
content_type: symbol
title: EventKit UI
original_title: EventKit UI
source_hash: 994dc65dd23c94deab548f9dba8266dcd9ce36839fc646677cfcbb537e969297
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:03:26+00:00'
last_translated_at: '2026-03-13T16:25:00+09:00'
---

# EventKit UI

캘린더 이벤트와 미리 알림을 보고 선택하고 편집하는 인터페이스를 표시합니다.

## 개요

iOS에서는 EventKitUI 프레임워크를 사용해 캘린더와 미리 알림 정보를 사용자에게 모달 방식으로 보여 줍니다. EventKitUI는 캘린더와 미리 알림 정보를 보고 편집하는 view controller, 어떤 캘린더를 볼지 선택하는 view controller, 캘린더를 읽기 전용으로 표시할지 읽기/쓰기 가능하게 표시할지 결정하는 view controller를 제공합니다.

iOS에서 사용할 view controller는 다음과 같습니다.

- [EKEventViewController](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller): 기존 이벤트를 표시합니다.
- [EKEventEditViewController](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller): 이벤트를 생성, 편집, 삭제합니다.
- [EKCalendarChooser](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser): 하나 이상의 캘린더를 선택하고, 캘린더가 읽기 전용인지 읽기/쓰기 가능한지 결정합니다.

이 인터페이스는 앱 내부에서 표시합니다. 표시되면 시스템이 사용자와의 모든 상호 작용을 관리하고, 인터페이스가 닫힐 때 이를 앱에 알려 줍니다.

EventKitUI는 기본 캘린더 선택, 버튼 표시, 사용자가 하나 이상의 캘린더를 선택할 수 있도록 하는 여러 구성 가능한 클래스도 제공합니다.

:::note Note
캘린더 및 미리 알림 데이터를 포함하는 event store에 접근하려면 EventKit을 사용하십시오. 자세한 내용은 [Accessing the event store](https://developer.apple.com/documentation/EventKit/accessing-the-event-store)를 참고하십시오.
:::

:::topic-grid
## 캘린더 뷰
- [EKEventViewController](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller): 기존 캘린더 및 미리 알림 이벤트를 표시하고, 선택적으로 이를 편집하는 view controller입니다.
:::

:::topic-grid
## 캘린더 편집
- [EKEventEditViewController](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller): 캘린더 이벤트를 생성, 편집, 삭제하는 view controller입니다.
:::

:::topic-grid
## 캘린더 선택
- [EKCalendarChooser](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser): 사용자가 하나 이상의 캘린더를 선택할 수 있는지 결정하는 view controller입니다.
:::

:::topic-grid
## EventKit 번들 접근
- [EventKitUIBundle()](https://developer.apple.com/documentation/eventkitui/eventkituibundle()): 앱 번들 내부 리소스에 접근할 때 사용합니다.
:::

:::topic-grid
## 레퍼런스
- [EventKitUI Constants](https://developer.apple.com/documentation/eventkitui/eventkitui-constants)
:::
