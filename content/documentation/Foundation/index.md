---
route: /documentation/Foundation
source_url: https://developer.apple.com/documentation/Foundation
source_locale: en-US
section: docc
content_type: symbol
title: Foundation
original_title: Foundation
source_hash: 4b6f90001709d69a1bd667ad92b2033441603a10407075287962af6b7a4117a9
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:20:23+00:00'
last_translated_at: '2026-03-13T22:45:00+09:00'
---

# Foundation

앱 기능의 기반 계층을 정의하기 위해 필수 데이터 타입, 컬렉션, 운영체제 서비스를 사용합니다.

## 개요

Foundation 프레임워크는 데이터 저장 및 지속성, 텍스트 처리, 날짜 및 시간 계산, 정렬 및 필터링, 네트워킹을 포함하여 앱과 프레임워크를 위한 기반 기능 계층을 제공합니다. Foundation이 정의하는 클래스, 프로토콜, 데이터 타입은 macOS, iOS, watchOS, tvOS SDK 전반에서 사용됩니다.

:::topic-grid
## 기초
- [Numbers, Data, and Basic Values](https://developer.apple.com/documentation/foundation/numbers-data-and-basic-values): 원시 값과 Cocoa 전반에서 사용하는 기타 기본 타입으로 작업합니다.
- [Strings and Text](https://developer.apple.com/documentation/foundation/strings-and-text): Unicode 문자로 된 문자열을 생성하고 처리하며, 정규식을 사용해 패턴을 찾고, 텍스트의 자연어 분석을 수행합니다.
- [Collections](https://developer.apple.com/documentation/foundation/collections): array, dictionary, set, 특수 컬렉션을 사용해 객체나 값의 그룹을 저장하고 순회합니다.
- [Dates and Times](https://developer.apple.com/documentation/foundation/dates-and-times): 날짜와 시간을 비교하고, 달력 및 시간대 계산을 수행합니다.
- [Units and Measurement](https://developer.apple.com/documentation/foundation/units-and-measurement): 숫자량에 물리 단위를 붙여 locale에 맞는 포맷팅과 관련 단위 간 변환을 가능하게 합니다.
- [Data Formatting](https://developer.apple.com/documentation/foundation/data-formatting): 숫자, 날짜, 측정값 및 기타 값을 locale에 맞는 문자열 표현으로 변환하거나 그 반대로 변환합니다.
- [Filters and Sorting](https://developer.apple.com/documentation/foundation/filters-and-sorting): predicate, expression, sort descriptor를 사용해 컬렉션 및 기타 서비스 안의 요소를 검사합니다.
:::

:::topic-grid
## 앱 지원
- [Task Management](https://developer.apple.com/documentation/foundation/task-management): 앱의 작업과, Handoff 및 Shortcuts 같은 시스템 서비스와의 상호 작용 방식을 관리합니다.
- [Resources](https://developer.apple.com/documentation/foundation/resources): 앱에 번들된 asset과 기타 데이터에 접근합니다.
- [Notifications](https://developer.apple.com/documentation/foundation/notifications): 정보를 방송하고 그 방송을 구독하는 디자인 패턴입니다.
- [App Extension Support](https://developer.apple.com/documentation/foundation/app-extension-support): app extension과 이를 호스팅하는 앱 사이의 상호 작용을 관리합니다.
- [Errors and Exceptions](https://developer.apple.com/documentation/foundation/errors-and-exceptions): API와 상호 작용할 때 문제 상황에 대응하고, 더 나은 디버깅을 위해 앱을 세밀하게 조정합니다.
- [Scripting Support](https://developer.apple.com/documentation/foundation/scripting-support): 사용자가 AppleScript 및 기타 자동화 기술로 앱을 제어하거나, 앱 안에서 script를 실행할 수 있게 합니다.
:::

:::topic-grid
## 파일과 데이터 지속성
- [File System](https://developer.apple.com/documentation/foundation/file-system): 파일 시스템 안에서 파일과 폴더를 생성, 읽기, 쓰기, 검사합니다.
- [Archives and Serialization](https://developer.apple.com/documentation/foundation/archives-and-serialization): 객체와 값을 property list, JSON, 기타 평면 바이너리 표현으로 변환하거나 다시 복원합니다.
- [Settings](https://developer.apple.com/documentation/foundation/settings): 로컬 디스크 또는 iCloud에 지속적으로 저장하는 데이터를 사용해 앱을 구성합니다.
- [Spotlight](https://developer.apple.com/documentation/foundation/spotlight): 로컬 기기에서 파일과 기타 항목을 검색하고, 검색을 위해 앱 콘텐츠를 인덱싱합니다.
- [iCloud](https://developer.apple.com/documentation/foundation/icloud): 사용자의 iCloud 기기 사이에서 자동으로 동기화되는 파일과 key-value 데이터를 관리합니다.
- [Optimizing Your App’s Data for iCloud Backup](https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup): purgeable 데이터와 nonpurgeable 데이터를 백업에서 제외해 백업 생성에 필요한 공간과 시간을 최소화합니다.
:::

:::topic-grid
## 네트워킹
- [URL Loading System](https://developer.apple.com/documentation/foundation/url-loading-system): URL과 상호 작용하고 표준 인터넷 프로토콜을 사용해 서버와 통신합니다.
- [Bonjour](https://developer.apple.com/documentation/foundation/bonjour): 로컬 네트워크에서 손쉽게 찾을 수 있도록 서비스를 알리거나, 다른 사람이 알린 서비스를 탐색합니다.
:::

:::topic-grid
## 저수준 유틸리티
- [XPC](https://developer.apple.com/documentation/foundation/xpc): 안전한 프로세스 간 통신을 관리합니다.
- [Object Runtime](https://developer.apple.com/documentation/foundation/object-runtime): 기본 Objective-C 기능, Cocoa 디자인 패턴, Swift 통합을 위한 저수준 지원을 얻습니다.
- [Processes and Threads](https://developer.apple.com/documentation/foundation/processes-and-threads): 앱과 호스트 운영체제 및 다른 프로세스 사이의 상호 작용을 관리하고, 저수준 동시성 기능을 구현합니다.
- [Streams, Sockets, and Ports](https://developer.apple.com/documentation/foundation/streams-sockets-and-ports): 저수준 Unix 기능을 사용해 파일, 프로세스, 네트워크 간 입출력을 관리합니다.
:::

:::topic-grid
## 참고 자료
- [Foundation Enumerations](https://developer.apple.com/documentation/foundation/foundation-enumerations)
- [Foundation Data Types](https://developer.apple.com/documentation/foundation/foundation-data-types): 이 문서는 Foundation 프레임워크에서 찾을 수 있는 데이터 타입과 상수를 설명합니다.
:::

:::topic-grid
## 프로토콜
- [NSPredicateValidating](https://developer.apple.com/documentation/foundation/nspredicatevalidating)
:::
