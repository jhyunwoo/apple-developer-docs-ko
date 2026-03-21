---
route: /documentation/SwiftData
source_url: https://developer.apple.com/documentation/SwiftData
source_locale: en-US
section: docc
content_type: symbol
title: SwiftData
original_title: SwiftData
source_hash: 08370ebd22ac82750815a60b5ac6862bdcce1adfbe9129307cb281f24b0b9913
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:27+00:00'
last_translated_at: '2026-03-13T17:10:00+09:00'
---

# SwiftData

선언형으로 모델 코드를 작성해 관리형 영속성과 효율적인 모델 가져오기를 추가합니다.

## 개요

SwiftData는 Core Data의 검증된 영속성 기술과 Swift의 현대적인 동시성 기능을 결합하여, 최소한의 코드와 외부 의존성 없이 앱에 빠르게 영속성을 추가할 수 있게 해 줍니다. 매크로 같은 현대적인 언어 기능을 사용하여 SwiftData는 빠르고 효율적이며 안전한 코드를 작성할 수 있게 하고, 앱의 전체 모델 계층 또는 객체 그래프를 기술할 수 있게 합니다. 프레임워크는 기본 모델 데이터 저장을 처리하고, 필요하면 여러 기기 간 동기화도 담당합니다.

SwiftData는 로컬에서 생성한 콘텐츠를 영속화하는 것 이상의 용도가 있습니다. 예를 들어 원격 웹 서비스에서 데이터를 가져오는 앱은 SwiftData를 사용해 가벼운 캐싱 메커니즘을 구현하고 제한적인 오프라인 기능을 제공할 수 있습니다.

![파란 도면 스타일 배경 위에 0과 1이 포함된 흰색 Swift 로고입니다.](https://developer.apple.com)

SwiftData는 설계상 침습적이지 않으며 앱의 기존 모델 클래스를 보완합니다. 어떤 모델 클래스든 [Model()](https://developer.apple.com/documentation/swiftdata/model()) 매크로를 부착하면 영속 가능한 모델로 만들 수 있습니다. [Attribute(_:originalName:hashModifier:)](https://developer.apple.com/documentation/swiftdata/attribute(_:originalname:hashmodifier:)) 및 [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](https://developer.apple.com/documentation/swiftdata/relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:)) 매크로를 사용해 그 모델의 프로퍼티 동작을 사용자화합니다. [ModelContext](https://developer.apple.com/documentation/swiftdata/modelcontext) 클래스를 사용해 해당 모델의 인스턴스를 삽입, 업데이트, 삭제하고 저장되지 않은 변경 사항을 디스크에 기록합니다.

SwiftUI view에서 모델을 표시하려면 [Query()](https://developer.apple.com/documentation/swiftdata/query()) 매크로를 사용하고 predicate 또는 fetch descriptor를 지정합니다. SwiftData는 view가 나타날 때 fetch를 수행하고, 이후 가져온 모델에 변경이 생기면 SwiftUI에 알려 view가 적절히 갱신되도록 합니다. 어떤 SwiftUI view에서든 [modelContext](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/modelContext) 환경 값을 사용해 model context에 접근할 수 있고, [modelContainer(_:)](https://developer.apple.com/documentation/SwiftUI/View/modelContainer(_:)) 및 [modelContext(_:)](https://developer.apple.com/documentation/SwiftUI/View/modelContext(_:)) view modifier를 사용해 특정 model container나 context를 지정할 수 있습니다.

:::topic-grid
## 핵심 사항
- [Preserving your app’s model data across launches](https://developer.apple.com/documentation/swiftdata/preserving-your-apps-model-data-across-launches): 프레임워크의 매크로를 사용해 모델 클래스를 SwiftData에 설명하고, 앱 런타임을 넘어 존재하도록 그 모델 인스턴스를 저장합니다.
- [Adding and editing persistent data in your app](https://developer.apple.com/documentation/swiftdata/adding-and-editing-persistent-data-in-your-app): SwiftData가 관리하는 데이터를 수집하고 변경하기 위한 데이터 입력 폼을 만듭니다.
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app): Swift 고유의 영속성 프레임워크를 사용해 직관적으로 앱의 데이터를 영속화합니다.
- [SwiftData updates](https://developer.apple.com/documentation/Updates/SwiftData): SwiftData의 중요한 변경 사항을 알아봅니다.
- [Adopting inheritance in SwiftData](https://developer.apple.com/documentation/swiftdata/adopting-inheritance-in-swiftdata): 클래스 상속을 사용해 모델에 유연성을 더합니다.
:::

:::topic-grid
## 모델 정의
- [Model()](https://developer.apple.com/documentation/swiftdata/model()): Swift 클래스를 SwiftData가 관리하는 저장 모델로 변환합니다.
- [Attribute(_:originalName:hashModifier:)](https://developer.apple.com/documentation/swiftdata/attribute(_:originalname:hashmodifier:)): SwiftData가 소유 클래스 관리 시 주석 처리된 프로퍼티에 적용할 사용자 정의 동작을 지정합니다.
- [Unique(_:)](https://developer.apple.com/documentation/swiftdata/unique(_:)): SwiftData가 모델 인스턴스의 고유성을 보장하는 데 사용할 key-path를 지정합니다.
- [Index(_:)](https://developer.apple.com/documentation/swiftdata/index(_:)-74ia2): SwiftData가 연결된 모델에 대해 하나 이상의 이진 인덱스를 만들 때 사용할 key-path를 지정합니다.
- [Index(_:)](https://developer.apple.com/documentation/swiftdata/index(_:)-7d4z0): SwiftData가 연결된 모델에 대해 하나 이상의 인덱스를 만들 때 사용할 key-path를 지정하며, 각 인덱스는 이진 또는 R-tree일 수 있습니다.
- [Defining data relationships with enumerations and model classes](https://developer.apple.com/documentation/swiftdata/defining-data-relationships-with-enumerations-and-model-classes): 앱에 저장된 정적 및 동적 데이터에 대한 관계를 생성합니다.
- [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](https://developer.apple.com/documentation/swiftdata/relationship(_:deleterule:minimummodelcount:maximummodelcount:originalname:inverse:hashmodifier:)): SwiftData가 주석 처리된 프로퍼티를 두 모델 간의 관계로 관리하는 데 필요한 옵션을 지정합니다.
- [Transient()](https://developer.apple.com/documentation/swiftdata/transient()): 소유 클래스를 관리할 때 SwiftData가 주석 처리된 프로퍼티를 영속화하지 않도록 지시합니다.
:::

:::topic-grid
## 모델 생명 주기
- [ModelContainer](https://developer.apple.com/documentation/swiftdata/modelcontainer): 앱의 스키마와 모델 저장 구성을 관리하는 객체입니다.
- [ModelContext](https://developer.apple.com/documentation/swiftdata/modelcontext): 모델을 가져오고 삽입하고 삭제하며 변경 사항을 디스크에 저장할 수 있게 하는 객체입니다.
- [Fetching and filtering time-based model changes](https://developer.apple.com/documentation/swiftdata/fetching-and-filtering-time-based-model-changes): 데이터 저장소에서 발생하는 모든 삽입, 업데이트, 삭제를 추적하고 이를 시간순 트랜잭션 시리즈로 처리합니다.
- [HistoryDescriptor](https://developer.apple.com/documentation/swiftdata/historydescriptor): 이력 데이터를 가져올 때 사용할 기준과 선택적 정렬 순서를 설명하는 타입입니다.
- [Deleting persistent data from your app](https://developer.apple.com/documentation/swiftdata/deleting-persistent-data-from-your-app): SwiftData를 사용해 영속 데이터를 삭제하는 다양한 방법을 살펴봅니다.
- [Reverting data changes using the undo manager](https://developer.apple.com/documentation/swiftdata/reverting-data-changes-using-the-undo-manager): SwiftUI 앱에서 사용자가 수행한 데이터 변경 작업을 자동으로 기록하고, 이를 실행 취소 및 다시 실행할 수 있게 합니다.
- [Syncing model data across a person’s devices](https://developer.apple.com/documentation/swiftdata/syncing-model-data-across-a-persons-devices): SwiftData가 iCloud를 사용해 앱의 모델 데이터를 자동으로 동기화할 수 있도록 필요한 capability를 추가하고 호환되는 스키마를 정의합니다.
- [Concurrency support](https://developer.apple.com/documentation/swiftdata/concurrencysupport): 모델 속성에 접근하고 저장소 관련 작업을 안전하고 격리된 방식으로 수행하는 데 사용하는 타입입니다.
:::

:::topic-grid
## 모델 가져오기
- [Filtering and sorting persistent data](https://developer.apple.com/documentation/swiftdata/filtering-and-sorting-persistent-data): predicate와 동적 쿼리를 사용해 데이터 저장소 표시를 관리합니다.
- [Query()](https://developer.apple.com/documentation/swiftdata/query()): 연결된 모델 타입의 모든 인스턴스를 가져옵니다.
- [Additional query macros](https://developer.apple.com/documentation/swiftdata/additionalquerymacros): 쿼리 결과를 좁히고 SwiftData에 결과 정렬과 순서를 알려 주는 보조 매크로입니다.
- [Query](https://developer.apple.com/documentation/swiftdata/query): 지정된 기준으로 모델을 가져오고, 기본 데이터와 계속 동기화되도록 관리하는 타입입니다.
- [FetchDescriptor](https://developer.apple.com/documentation/swiftdata/fetchdescriptor): fetch 수행 시 사용할 기준, 정렬 순서, 추가 구성을 설명하는 타입입니다.
:::

:::topic-grid
## 모델 저장소
- [Maintaining a local copy of server data](https://developer.apple.com/documentation/swiftdata/maintaining-a-local-copy-of-server-data): 읽기 전용 네트워크 데이터를 캐시하기 위한 영속 저장소를 생성하고 업데이트합니다.
- [DefaultStore](https://developer.apple.com/documentation/swiftdata/defaultstore): Core Data를 기본 저장 메커니즘으로 사용하는 데이터 저장소입니다.
- [DataStore](https://developer.apple.com/documentation/swiftdata/datastore): 기본 저장 메커니즘을 알지 못해도 SwiftData가 모델 데이터를 읽고 쓸 수 있게 하는 인터페이스입니다.
- [DataStoreBatching](https://developer.apple.com/documentation/swiftdata/datastorebatching): 사용자 정의 데이터 저장소가 배치 요청을 지원할 수 있게 하는 인터페이스입니다.
- [HistoryProviding](https://developer.apple.com/documentation/swiftdata/historyproviding): 사용자 정의 데이터 저장소가 영속 모델 변경 이력을 제공할 수 있게 하는 인터페이스입니다.
- [Building a document-based app using SwiftData](https://developer.apple.com/documentation/SwiftUI/Building-a-document-based-app-using-SwiftData): WWDC 발표자와 함께 SwiftData 기반 앱으로 변환하는 과정을 따라갑니다.
- [ModelDocument](https://developer.apple.com/documentation/swiftdata/modeldocument): SwiftData를 사용해 저장소를 관리하는 문서 타입입니다.
:::

:::topic-grid
## 이력 생명 주기
- [HistoryChange](https://developer.apple.com/documentation/swiftdata/historychange): 데이터 이력 트랜잭션을 설명하는 값입니다.
- [HistoryDelete](https://developer.apple.com/documentation/swiftdata/historydelete): 사용자 정의 데이터 저장소가 영속 모델 변경 이력에서 항목을 삭제할 수 있게 하는 인터페이스입니다.
- [HistoryInsert](https://developer.apple.com/documentation/swiftdata/historyinsert)
- [HistoryToken](https://developer.apple.com/documentation/swiftdata/historytoken)
- [HistoryTransaction](https://developer.apple.com/documentation/swiftdata/historytransaction)
- [HistoryUpdate](https://developer.apple.com/documentation/swiftdata/historyupdate)
- [HistoryTombstone](https://developer.apple.com/documentation/swiftdata/historytombstone)
- [DefaultHistoryInsert](https://developer.apple.com/documentation/swiftdata/defaulthistoryinsert)
- [DefaultHistoryUpdate](https://developer.apple.com/documentation/swiftdata/defaulthistoryupdate)
- [DefaultHistoryDelete](https://developer.apple.com/documentation/swiftdata/defaulthistorydelete)
- [DefaultHistoryToken](https://developer.apple.com/documentation/swiftdata/defaulthistorytoken)
- [DefaultHistoryTransaction](https://developer.apple.com/documentation/swiftdata/defaulthistorytransaction)
:::

:::topic-grid
## Codable 지원
- [DataStoreSnapshotCodingKey](https://developer.apple.com/documentation/swiftdata/datastoresnapshotcodingkey): 데이터 저장소 스냅샷용 사용자 정의 encoder와 decoder를 구현할 때 사용할 키 공간입니다.
:::

:::topic-grid
## 오류
- [SwiftDataError](https://developer.apple.com/documentation/swiftdata/swiftdataerror): SwiftData 오류를 설명하는 타입입니다.
- [DataStoreError](https://developer.apple.com/documentation/swiftdata/datastoreerror): 데이터 저장소 오류를 설명하는 타입입니다.
:::
