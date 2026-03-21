---
route: /documentation/FinderSync
source_url: https://developer.apple.com/documentation/FinderSync
source_locale: en-US
section: docc
content_type: symbol
title: Finder Sync
original_title: Finder Sync
source_hash: 47a799256e4dd97f993e86019e14f9fd9eace60d7a1ef006f637ecc6f3655d1f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:16:02+00:00'
last_translated_at: '2026-03-13T22:31:00+09:00'
---

# Finder Sync

파일 동기화 상태와 제어를 표현하기 위해 Finder의 사용자 인터페이스를 수정합니다.

## 개요

Finder Sync를 사용하면 파일 동기화 상태와 제어를 표현하기 위해 Finder의 사용자 인터페이스를 깔끔하고 안전하게 수정할 수 있습니다. 대부분의 extension point와 달리 Finder Sync는 호스트 앱에 기능을 추가하지 않습니다. 대신 Finder 자체의 동작을 수정할 수 있게 해 줍니다.

로컬 폴더의 콘텐츠를 원격 데이터 소스와 동기화해야 할 때 이 프레임워크를 사용하십시오. 그런 다음 [FIFinderSync](https://developer.apple.com/documentation/findersync/fifindersync-swift.class) 클래스를 확장하고 [FIFinderSyncProtocol](https://developer.apple.com/documentation/findersync/fifindersyncprotocol) 프로토콜에 정의된 appearance 메서드를 재정의하여 Finder에 시각적 피드백을 제공하십시오.

Finder Sync extension을 만드는 방법을 더 알아보려면 [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)의 [Finder Sync](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Finder.html#//apple_ref/doc/uid/TP40014214-CH15)를 참고하십시오.

:::topic-grid
## 클래스
- [FIFinderSync](https://developer.apple.com/documentation/findersync/fifindersync-swift.class): Finder에 badge, 사용자 정의 shortcut menu, toolbar button을 추가하기 위해 subclass하는 타입입니다.
- [FIFinderSyncController](https://developer.apple.com/documentation/findersync/fifindersynccontroller): Finder Sync extension과 Finder 자체 사이의 다리 역할을 하는 controller입니다.
:::

:::topic-grid
## 프로토콜
- [FIFinderSyncProtocol](https://developer.apple.com/documentation/findersync/fifindersyncprotocol): 파일 동기화 상태와 제어를 표현하기 위해 Finder 사용자 인터페이스를 수정할 때 구현하는 메서드 그룹입니다.
:::

:::topic-grid
## 참고 자료
- [FinderSync Enumerations](https://developer.apple.com/documentation/findersync/findersyncenumerations)
:::
