---
route: /documentation/CoreData
source_url: https://developer.apple.com/documentation/CoreData
source_locale: en-US
section: docc
content_type: symbol
title: Core Data
original_title: Core Data
source_hash: 0d70bd6a146977e642c510f125543aa0e7f2820626727725d706329bd59eb4f3
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:38:51+00:00'
last_translated_at: '2026-03-13T23:42:00+09:00'
---

# Core Data

단일 기기에서 데이터를 영구 저장하거나 캐시하고, CloudKit으로 여러 기기에 데이터를 동기화합니다.

## 개요

Core Data를 사용하면 단일 기기에서 오프라인용 영구 데이터를 저장하고, 임시 데이터를 캐시하고, 앱에 undo 기능을 추가할 수 있습니다. 하나의 iCloud 계정에 속한 여러 기기 사이에서 데이터를 동기화하려면, Core Data가 스키마를 CloudKit container에 자동으로 미러링합니다.

Core Data의 Data Model editor를 통해 데이터 타입과 관계를 정의하고, შესაბამის 클래스 정의를 생성합니다. 그런 다음 Core Data는 런타임에 객체 인스턴스를 관리해 다음 기능을 제공합니다.

### 영속성

Core Data는 객체를 저장소에 매핑하는 세부 사항을 추상화하므로, 데이터베이스를 직접 관리하지 않고도 Swift와 Objective-C에서 데이터를 쉽게 저장할 수 있습니다.

![앱이 persistent store에 데이터를 저장하고 persistent store에서 데이터를 로드하는 흐름을 보여 주는 다이어그램입니다.](https://developer.apple.com)

### 개별 변경 및 일괄 변경의 실행 취소와 다시 실행

Core Data의 undo manager는 변경 사항을 추적하고 이를 개별적으로, 그룹 단위로, 또는 한 번에 모두 되돌릴 수 있어 앱에 undo 및 redo 지원을 쉽게 추가할 수 있습니다.

![흔들어서 실행 취소하는 동작으로 인해 목록에서 요소가 제거되는 모습을 보여 주는 그림입니다.](https://developer.apple.com)

### 백그라운드 데이터 작업

JSON을 객체로 파싱하는 것처럼 UI를 막을 수 있는 데이터 작업을 백그라운드에서 수행합니다. 그런 다음 결과를 캐시하거나 저장해 서버 왕복 횟수를 줄일 수 있습니다.

![엔드포인트의 데이터가 백그라운드에서 객체를 채운 뒤 UI를 업데이트하는 흐름을 보여 주는 다이어그램입니다.](https://developer.apple.com)

### 뷰 동기화

Core Data는 table view와 collection view를 위한 데이터 소스를 제공해 뷰와 데이터를 동기화된 상태로 유지하도록 돕습니다.

### 버전 관리 및 마이그레이션

Core Data는 앱이 발전함에 따라 데이터 모델의 버전을 관리하고 사용자 데이터를 마이그레이션하는 메커니즘을 포함합니다.

:::topic-grid
## 핵심 항목
- [Creating a Core Data model](https://developer.apple.com/documentation/coredata/creating-a-core-data-model): 데이터 모델 파일로 앱의 객체 구조를 정의합니다.
- [Setting up a Core Data stack](https://developer.apple.com/documentation/coredata/setting-up-a-core-data-stack): 앱의 객체를 관리하고 영속화하는 클래스를 설정합니다.
- [Core Data stack](https://developer.apple.com/documentation/coredata/core-data-stack): 앱의 모델 레이어를 관리하고 영속화합니다.
- [Handling Different Data Types in Core Data](https://developer.apple.com/documentation/coredata/handling-different-data-types-in-core-data): 다양한 데이터 타입의 record를 생성하고 저장하고 표시합니다.
- [Linking Data Between Two Core Data Stores](https://developer.apple.com/documentation/coredata/linking-data-between-two-core-data-stores): 서로 다른 두 저장소에 데이터를 구성하고 그 사이의 링크를 구현합니다.
:::

:::topic-grid
## 데이터 모델링
- [Modeling data](https://developer.apple.com/documentation/coredata/modeling-data): 앱의 object graph를 담도록 데이터 모델 파일을 구성합니다.
- [Core Data model](https://developer.apple.com/documentation/coredata/core-data-model): 앱의 객체 구조를 설명합니다.
:::

:::topic-grid
## Fetch request
- [NSFetchRequest](https://developer.apple.com/documentation/coredata/nsfetchrequest): persistent store에서 데이터를 가져오는 데 사용하는 검색 기준 설명입니다.
- [NSAsynchronousFetchRequest](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest): 결과를 비동기적으로 가져오고 진행 알림을 지원하는 fetch request입니다.
- [NSAsynchronousFetchResult](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult): 실행된 비동기 fetch request의 응답을 포함하는 fetch result 객체입니다.
- [NSFetchedResultsController](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller): Core Data fetch request의 결과를 관리하고 데이터를 사용자에게 표시할 때 사용하는 controller입니다.
:::

:::topic-grid
## SwiftData 마이그레이션 및 공존
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/coredata/adopting-swiftdata-for-a-core-data-app): Swift 네이티브 persistence framework로 앱의 데이터를 직관적으로 영속화합니다.
:::

:::topic-grid
## CloudKit 미러링
- [Mirroring a Core Data store with CloudKit](https://developer.apple.com/documentation/coredata/mirroring-a-core-data-store-with-cloudkit): CloudKit private database의 로컬 복제본으로 사용자 인터페이스를 뒷받침합니다.
- [Synchronizing a local store to the cloud](https://developer.apple.com/documentation/coredata/synchronizing-a-local-store-to-the-cloud): 사용자의 기기와 다른 iCloud 사용자 사이에서 데이터를 공유합니다.
- [NSPersistentCloudKitContainer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer): 앱의 Core Data stack을 캡슐화하고, 선택한 persistent store를 CloudKit private database에 미러링하는 container입니다.
- [NSPersistentCloudKitContainerOptions](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontaineroptions): store description이 CloudKit database와 어떻게 정렬되는지를 사용자화하는 객체입니다.
- [Sharing Core Data objects between iCloud users](https://developer.apple.com/documentation/coredata/sharing-core-data-objects-between-icloud-users): Core Data와 CloudKit을 사용해 한 iCloud 사용자의 기기 사이에서 데이터를 동기화하고, 서로 다른 iCloud 사용자 간에 데이터를 공유합니다.
:::

:::topic-grid
## 변경 처리
- [Accessing data when the store changes](https://developer.apple.com/documentation/coredata/accessing-data-when-the-store-changes): context가 저장소 변경을 볼 시점을 사용자가 지정하기 전까지는 이를 보지 않도록 보장합니다.
- [Consuming relevant store changes](https://developer.apple.com/documentation/coredata/consuming-relevant-store-changes): 현재 뷰와 관련된 변경만 남기도록 store transaction을 필터링합니다.
- [Persistent history](https://developer.apple.com/documentation/coredata/persistent-history): persistent history tracking이 활성화된 이후 저장소에서 어떤 변경이 발생했는지 확인하기 위해 persistent history tracking을 사용합니다.
:::

:::topic-grid
## 백그라운드 작업
- [Using Core Data in the background](https://developer.apple.com/documentation/coredata/using-core-data-in-the-background): 단일 스레드 앱과 멀티스레드 앱 모두에서 Core Data를 사용합니다.
- [Loading and displaying a large data feed](https://developer.apple.com/documentation/SwiftUI/loading-and-displaying-a-large-data-feed): 백그라운드에서 데이터를 소비하고, import를 일괄 처리하고 중복 record를 방지해 메모리 사용량을 줄입니다.
- [Conflict resolution](https://developer.apple.com/documentation/coredata/conflict-resolution): 여러 스레드에서 데이터가 변경될 때 발생하는 충돌을 감지하고 해결합니다.
- [Batch processing](https://developer.apple.com/documentation/coredata/batch-processing): 대규모 데이터 변경을 관리하기 위해 batch process를 사용합니다.
:::

:::topic-grid
## 데이터 모델 마이그레이션
- [Migrating your data model automatically](https://developer.apple.com/documentation/coredata/migrating-your-data-model-automatically): lightweight migration을 활성화해 데이터 모델과 기본 데이터가 일관된 상태를 유지하게 합니다.
- [Staged migrations](https://developer.apple.com/documentation/coredata/staged-migrations): lightweight migration과 호환되지 않는 변경을 포함한 복잡한 데이터 모델을 마이그레이션합니다.
- [Manual migrations](https://developer.apple.com/documentation/coredata/manual-migrations): lightweight migration과 staged migration 모두의 범위를 넘어서는 변경이 있는 정교한 데이터 모델을 마이그레이션합니다.
:::

:::topic-grid
## 관련 타입
- [Core Data Constants](https://developer.apple.com/documentation/coredata/core-data-constants): persistent store와 Core Data의 notification에 사용하는 키입니다.
:::
