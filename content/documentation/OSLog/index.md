---
route: /documentation/OSLog
source_url: https://developer.apple.com/documentation/OSLog
source_locale: en-US
section: docc
content_type: symbol
title: OSLog
original_title: OSLog
source_hash: 8dcdf28f8ce03b9e11070aad95f3f0d62e056bd90d69d043261b7c37990bc530
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:29+00:00'
last_translated_at: '2026-03-13T17:10:00+09:00'
---

# OSLog

과거 데이터 읽기를 위한 통합 로깅 시스템입니다.

## 개요

OSLog 프레임워크를 사용하면 로그를 읽을 수 있습니다. 통합 로깅 시스템을 사용하면 Instruments와 Console 같은 Apple 도구와 함께 사용할 사용자 정의 디버깅 및 분석 도구를 만들 수 있습니다. 로그 생성 방법에 대한 자세한 내용은 [Logging](https://developer.apple.com/documentation/os/logging)을 참고하십시오.

:::topic-grid
## 로그 항목 읽기
- [OSLogStore](https://developer.apple.com/documentation/oslog/oslogstore): 통합 로깅 시스템의 항목 집합입니다.
- [OSLogEnumerator](https://developer.apple.com/documentation/oslog/oslogenumerator): 로그 항목에 접근하고 나열할 수 있는 enumerator입니다.
:::

:::topic-grid
## 로그 항목
- [OSLogEntry](https://developer.apple.com/documentation/oslog/oslogentry): 통합 로깅 시스템의 단일 항목입니다.
- [OSLogEntryActivity](https://developer.apple.com/documentation/oslog/oslogentryactivity): activity 이벤트에 의해 생성된 항목입니다.
- [OSLogEntryBoundary](https://developer.apple.com/documentation/oslog/oslogentryboundary): 다른 항목들의 시퀀스를 구분하는 메타데이터입니다.
- [OSLogEntryLog](https://developer.apple.com/documentation/oslog/oslogentrylog): 로그 항목입니다.
- [OSLogEntrySignpost](https://developer.apple.com/documentation/oslog/oslogentrysignpost): signpost를 포함하는 항목입니다.
- [OSLogEntryFromProcess](https://developer.apple.com/documentation/oslog/oslogentryfromprocess): 프로세스에 대한 메타데이터를 포함하는 서브클래스를 정의하는 프로토콜입니다.
- [OSLogEntryWithPayload](https://developer.apple.com/documentation/oslog/oslogentrywithpayload): handle과 format string을 사용해 생성된 항목을 나타내는 서브클래스를 정의하는 프로토콜입니다.
:::

:::topic-grid
## 항목 데이터
- [OSLogMessageComponent](https://developer.apple.com/documentation/oslog/oslogmessagecomponent): 특정 항목의 메시지 인수입니다.
- [OSLogPosition](https://developer.apple.com/documentation/oslog/oslogposition): 통합 로깅 시스템의 항목 시퀀스 안에서 한 지점을 나타내는 표현입니다.
:::

:::topic-grid
## 레퍼런스
- [OSLog Enumerations](https://developer.apple.com/documentation/oslog/oslog-enumerations)
:::
