---
route: /documentation/EventKit
source_url: https://developer.apple.com/documentation/EventKit
source_locale: en-US
section: docc
content_type: symbol
title: EventKit
original_title: EventKit
source_hash: 99f0b4c08566477968358e9eef24956eb2205aff5efc0247abcee6bca3a35bab
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:46:57+00:00'
last_translated_at: '2026-03-14T01:23:00+09:00'
---

# EventKit

캘린더 이벤트와 미리 알림을 생성하고, 보고, 편집합니다.

## 개요

EventKit 프레임워크는 캘린더와 미리 알림 데이터에 접근할 수 있게 하여, 사용자가 앱 안에서 캘린더 항목을 생성, 조회, 편집할 수 있도록 합니다. iOS에서는 [EventKit UI](https://developer.apple.com/documentation/EventKitUI)가 앱 안에서 구현할 수 있는 사용자 인터페이스를 제공하여, 사용자가 캘린더 항목을 생성하고 편집할 수 있게 합니다.

EventKit을 사용해 알람을 설정하고 반복 이벤트를 만들 수 있습니다. 또한 앱 외부에서 Calendar 데이터베이스에 변경이 생기면 EventKit이 이를 감지해 알림을 보내므로, 앱이 최신 상태를 유지할 수 있습니다.

:::topic-grid
## 핵심 사항
- [Accessing the event store](https://developer.apple.com/documentation/eventkit/accessing-the-event-store): event store를 통해 사용자의 캘린더 데이터 접근 권한을 요청합니다.
- [EKEventStore](https://developer.apple.com/documentation/eventkit/ekeventstore): 사용자의 캘린더 이벤트와 미리 알림에 접근하고 새 이벤트 일정을 지원하는 객체입니다.
- [Accessing Calendar using EventKit and EventKitUI](https://developer.apple.com/documentation/eventkit/accessing-calendar-using-eventkit-and-eventkitui): 앱에 적절한 Calendar 접근 수준을 선택하고 구현합니다.
:::

:::topic-grid
## 이벤트 및 미리 알림
- [Creating events and reminders](https://developer.apple.com/documentation/eventkit/creating-events-and-reminders): 사용자의 데이터베이스에서 이벤트와 미리 알림을 생성하고 수정합니다.
- [Retrieving events and reminders](https://developer.apple.com/documentation/eventkit/retrieving-events-and-reminders): Calendar 데이터베이스에서 이벤트와 미리 알림을 가져옵니다.
- [Updating with notifications](https://developer.apple.com/documentation/eventkit/updating-with-notifications): 변경 알림을 등록하고 앱을 최신 상태로 유지합니다.
- [Managing location-based reminders](https://developer.apple.com/documentation/eventkit/managing-location-based-reminders): 사용자의 캘린더에 설정된 geofence 기반 알람이 있는 미리 알림에 접근합니다.
- [EKEvent](https://developer.apple.com/documentation/eventkit/ekevent): 캘린더의 이벤트를 나타내는 클래스입니다.
- [EKReminder](https://developer.apple.com/documentation/eventkit/ekreminder): 캘린더의 미리 알림을 나타내는 클래스입니다.
:::

:::topic-grid
## 캘린더
- [EKCalendar](https://developer.apple.com/documentation/eventkit/ekcalendar): EventKit의 캘린더를 나타내는 클래스입니다.
- [EKParticipant](https://developer.apple.com/documentation/eventkit/ekparticipant): 캘린더 이벤트에 초대된 사람, 그룹, 또는 room을 나타내는 클래스입니다.
:::

:::topic-grid
## 반복
- [Creating a recurring event](https://developer.apple.com/documentation/eventkit/creating-a-recurring-event): 반복되는 이벤트 또는 미리 알림을 설정합니다.
- [EKRecurrenceDayOfWeek](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek): 요일을 나타내는 클래스입니다.
- [EKRecurrenceEnd](https://developer.apple.com/documentation/eventkit/ekrecurrenceend): 반복 규칙의 종료를 정의하는 클래스입니다.
- [EKRecurrenceRule](https://developer.apple.com/documentation/eventkit/ekrecurrencerule): 반복 이벤트의 패턴을 설명하는 클래스입니다.
:::

:::topic-grid
## 알람
- [Setting an alarm](https://developer.apple.com/documentation/eventkit/setting-an-alarm): 알람으로 사용자에게 이벤트와 미리 알림을 알려 줍니다.
- [EKAlarm](https://developer.apple.com/documentation/eventkit/ekalarm): 알람을 나타내는 클래스입니다.
- [EKStructuredLocation](https://developer.apple.com/documentation/eventkit/ekstructuredlocation): 캘린더 항목의 알람을 활성화할 geofence를 지정하는 클래스입니다.
:::

:::topic-grid
## 공통 객체
- [EKCalendarItem](https://developer.apple.com/documentation/eventkit/ekcalendaritem): 캘린더 이벤트와 미리 알림의 추상 상위 클래스입니다.
- [EKObject](https://developer.apple.com/documentation/eventkit/ekobject): 영속 인스턴스를 가지는 모든 EventKit 클래스의 추상 상위 클래스입니다.
- [EKSource](https://developer.apple.com/documentation/eventkit/eksource): 캘린더가 속한 계정을 나타내는 추상 상위 클래스입니다.
:::

:::topic-grid
## 가상 회의
- [Implementing a virtual conference extension](https://developer.apple.com/documentation/eventkit/implementing-a-virtual-conference-extension): Calendar의 이벤트에 가상 회의실을 추가할 수 있도록 지원합니다.
- [EKVirtualConferenceProvider](https://developer.apple.com/documentation/eventkit/ekvirtualconferenceprovider): 사용자의 캘린더에 있는 이벤트 객체와 가상 회의 세부 정보를 연결하는 객체입니다.
- [EKVirtualConferenceDescriptor](https://developer.apple.com/documentation/eventkit/ekvirtualconferencedescriptor): 사용자 정의 room type을 사용하는 가상 회의에 대한 세부 정보입니다.
- [EKVirtualConferenceRoomTypeDescriptor](https://developer.apple.com/documentation/eventkit/ekvirtualconferenceroomtypedescriptor): 가상 회의가 열리는 room에 대한 세부 정보입니다.
:::

:::topic-grid
## 오류
- [EKError](https://developer.apple.com/documentation/eventkit/ekerror): EventKit 오류입니다.
- [EKError.Code](https://developer.apple.com/documentation/eventkit/ekerror/code): EventKit 오류용 코드입니다.
- [EKErrorDomain](https://developer.apple.com/documentation/eventkit/ekerrordomain): EventKit 오류 도메인을 식별하는 문자열입니다.
:::
