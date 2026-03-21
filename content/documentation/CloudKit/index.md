---
route: /documentation/CloudKit
source_url: https://developer.apple.com/documentation/CloudKit
source_locale: en-US
section: docc
content_type: symbol
title: CloudKit
original_title: CloudKit
source_hash: cdd0566ea72215e31b90fa75750ad547c810cc544ee08e0440a291531ab3d17b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:27:46+00:00'
last_translated_at: '2026-03-13T23:24:00+09:00'
---

# CloudKit

앱의 모든 사용자가 공유할 수 있는 iCloud container에 구조화된 앱 및 사용자 데이터를 저장합니다.

## 개요

CloudKit 프레임워크는 앱과 iCloud container 사이에서 데이터를 이동하기 위한 인터페이스를 제공합니다. CloudKit을 사용하면 앱의 기존 데이터를 클라우드에 저장해 사용자가 여러 기기에서 접근할 수 있게 할 수 있습니다. 모든 사용자가 접근할 수 있는 공개 영역에 데이터를 저장할 수도 있습니다.

### CloudKit 프레임워크 사용하기

CloudKit은 앱의 기존 데이터 객체를 대체하는 기술이 아닙니다. 대신 CloudKit은 iCloud 서버로 데이터를 보내고 가져오는 전송을 관리하기 위한 보완 서비스들을 제공합니다. 오프라인 캐싱 지원은 최소 수준이므로, CloudKit은 네트워크의 존재와 선택적으로 유효한 iCloud 계정에 의존합니다. 유효한 iCloud 계정은 단일 사용자에게 특화된 데이터를 저장하려는 경우에만 필요합니다. 앱은 언제나 모든 사용자가 읽을 수 있는 공개 영역에 데이터를 저장할 수 있습니다.

레코드는 CloudKit의 모든 데이터 트랜잭션의 핵심입니다. 레코드는 저장하려는 데이터를 표현하는 key-value pair의 dictionary입니다. 언제든지 레코드에 새 키와 값을 추가할 수 있고, 관련 레코드 간 링크를 만들어 데이터를 구성할 수 있습니다. [CKRecord](https://developer.apple.com/documentation/cloudkit/ckrecord) 클래스는 레코드 내용을 관리하기 위한 인터페이스를 정의합니다. CloudKit은 또한 서버로 데이터를 비동기적으로 보내고 가져오는 작업을 관리하기 위해 [Operation](https://developer.apple.com/documentation/Foundation/Operation) 객체 사용에 크게 의존합니다.

CloudKit을 사용하기 전에 이것이 앱에 가장 적합한 선택인지 확인합니다. 자세한 내용은 [Deciding whether CloudKit is right for your app](https://developer.apple.com/documentation/cloudkit/deciding-whether-cloudkit-is-right-for-your-app)를 참고합니다.

:::note Note
CloudKit 프레임워크의 클래스는 subclassing을 위한 것이 아닙니다. 이 클래스들을 있는 그대로 사용해 iCloud에서 데이터를 저장, 검색, 조작합니다. 또한 이 프레임워크의 많은 프로토콜은 CloudKit과 UIKit 외부의 클래스가 채택하도록 설계되지 않았습니다. 각 프로토콜 참조 문서에는 사용자가 자신의 클래스에서 해당 프로토콜을 채택할 수 있는지에 대한 정보가 포함되어 있습니다.
:::

:::topic-grid
## 핵심 항목
- [Deciding whether CloudKit is right for your app](https://developer.apple.com/documentation/cloudkit/deciding-whether-cloudkit-is-right-for-your-app): iCloud를 사용해 앱 데이터를 저장하고 동기화하는 여러 옵션을 살펴봅니다.
- [Enabling CloudKit in Your App](https://developer.apple.com/documentation/cloudkit/enabling-cloudkit-in-your-app): CloudKit을 사용해 앱이 iCloud에 데이터를 저장하도록 구성합니다.
:::

:::topic-grid
## 스키마
- [Designing and Creating a CloudKit Database](https://developer.apple.com/documentation/cloudkit/designing-and-creating-a-cloudkit-database): CloudKit을 사용해 앱 객체를 iCloud의 record로 저장할 스키마를 생성합니다.
- [Managing iCloud Containers with CloudKit Database App](https://developer.apple.com/documentation/cloudkit/managing-icloud-containers-with-cloudkit-database-app): 앱의 iCloud container에 대한 스키마와 데이터를 검사하고 수정합니다.
- [CKRecordZone](https://developer.apple.com/documentation/cloudkit/ckrecordzone): 관련 record를 담는 데이터베이스 파티션입니다.
- [CKRecord](https://developer.apple.com/documentation/cloudkit/ckrecord): 앱 데이터를 저장하는 key-value pair의 컬렉션입니다.
- [CKRecord.Reference](https://developer.apple.com/documentation/cloudkit/ckrecord/reference): record zone 안의 두 record 사이의 관계입니다.
- [CKAsset](https://developer.apple.com/documentation/cloudkit/ckasset): record에 속한 외부 파일입니다.
- [Integrating a Text-Based Schema into Your Workflow](https://developer.apple.com/documentation/cloudkit/integrating-a-text-based-schema-into-your-workflow): CloudKit Schema Language로 스키마를 정의하고 업데이트합니다.
:::

:::topic-grid
## 레코드
- [Local Records](https://developer.apple.com/documentation/cloudkit/local-records): 기기에서 record를 조작하고 변경 사항을 서버에 저장합니다.
- [Remote Records](https://developer.apple.com/documentation/cloudkit/remote-records): subscription과 change token을 사용해 원격 record 변경을 효율적으로 관리합니다.
- [CKSyncEngine](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5): 로컬 및 원격 record 데이터의 동기화를 관리하는 객체입니다.
- [Shared Records](https://developer.apple.com/documentation/cloudkit/shared-records): 하나 이상의 record를 다른 iCloud 사용자와 공유합니다.
:::

:::topic-grid
## 사용자 발견
- [CKUserIdentity](https://developer.apple.com/documentation/cloudkit/ckuseridentity): 사용자의 신원입니다.
- [CKUserIdentity.LookupInfo](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class): 검색 가능한 iCloud 사용자를 찾을 때 사용할 기준입니다.
:::

:::topic-grid
## 핵심 객체
- [CKContainer](https://developer.apple.com/documentation/cloudkit/ckcontainer): 앱 데이터베이스로 가는 통로입니다.
- [CKDatabase](https://developer.apple.com/documentation/cloudkit/ckdatabase): record zone과 subscription의 컬렉션을 나타내는 객체입니다.
- [CKOperationGroup](https://developer.apple.com/documentation/cloudkit/ckoperationgroup): 둘 이상의 operation 간 명시적 연결입니다.
:::

:::topic-grid
## 개인 정보 보호
- [Encrypting User Data](https://developer.apple.com/documentation/cloudkit/encrypting-user-data): CloudKit 암호화를 사용해 업계 표준 보안 기술을 배포합니다.
- [Providing User Access to CloudKit Data](https://developer.apple.com/documentation/cloudkit/providing-user-access-to-cloudkit-data): 앱이 사용자를 대신해 저장하는 데이터에 대한 접근 권한을 사용자에게 제공합니다.
- [Changing Access Controls on User Data](https://developer.apple.com/documentation/cloudkit/changing-access-controls-on-user-data): 사용자의 요청에 따라 데이터 접근을 제한하거나 제한을 제거합니다.
- [CKFetchWebAuthTokenOperation](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation): CloudKit 웹 서비스에 사용할 인증 토큰을 생성하는 operation입니다.
- [Responding to Requests to Delete Data](https://developer.apple.com/documentation/cloudkit/responding-to-requests-to-delete-data): 사용자가 앱에서 자신의 CloudKit 데이터를 삭제할 수 있는 옵션을 제공합니다.
- [Identifying an App’s Containers](https://developer.apple.com/documentation/cloudkit/identifying-an-app-s-containers): Xcode의 Project navigator를 사용해 활성 CloudKit container의 식별자를 찾습니다.
:::

:::topic-grid
## 오류
- [CKErrorDomain](https://developer.apple.com/documentation/cloudkit/ckerrordomain): CloudKit 오류용 error domain입니다.
- [CKError](https://developer.apple.com/documentation/cloudkit/ckerror): CloudKit 오류를 설명하는 타입입니다.
- [CKError.Code](https://developer.apple.com/documentation/cloudkit/ckerror/code): CloudKit이 반환하는 오류 코드입니다.
- [CKErrorRetryAfterKey](https://developer.apple.com/documentation/cloudkit/ckerrorretryafterkey): 요청을 재시도하기 전에 기다려야 할 초 수를 가져오는 키입니다.
- [CKErrorUserDidResetEncryptedDataKey](https://developer.apple.com/documentation/cloudkit/ckerroruserdidresetencrypteddatakey): 사용자 동작 때문에 CloudKit이 record zone을 삭제했는지를 판별하는 키입니다.
- [CKPartialErrorsByItemIDKey](https://developer.apple.com/documentation/cloudkit/ckpartialerrorsbyitemidkey): 부분 오류를 가져오는 키입니다.
- [Record Changed Error Keys](https://developer.apple.com/documentation/cloudkit/record-changed-error-keys): 저장 작업에서 충돌하는 record를 나타내는 상수입니다.
:::

:::topic-grid
## 사용 중단됨
- [Deprecated Symbols](https://developer.apple.com/documentation/cloudkit/deprecated-symbols): 지원되지 않는 심볼과 그 대체 항목을 검토합니다.
:::

:::topic-grid
## 클래스
- [CKShareRequestAccessOperation](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation)
:::

:::topic-grid
## 변수
- [CKRecordParentKey](https://developer.apple.com/documentation/cloudkit/ckrecordparentkey-1elhg)
- [CKRecordShareKey](https://developer.apple.com/documentation/cloudkit/ckrecordsharekey-gc8w)
- [CKRecordTypeShare](https://developer.apple.com/documentation/cloudkit/ckrecordtypeshare-7lec1)
- [CKRecordTypeUserRecord](https://developer.apple.com/documentation/cloudkit/ckrecordtypeuserrecord-6iwgn)
- [CKRecordZoneDefaultName](https://developer.apple.com/documentation/cloudkit/ckrecordzonedefaultname-1uuiu)
- [CKShareThumbnailImageDataKey](https://developer.apple.com/documentation/cloudkit/cksharethumbnailimagedatakey-rxjd)
- [CKShareTitleKey](https://developer.apple.com/documentation/cloudkit/cksharetitlekey-1cs9j)
- [CKShareTypeKey](https://developer.apple.com/documentation/cloudkit/cksharetypekey-5m83p)
:::
