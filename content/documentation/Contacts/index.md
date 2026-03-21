---
route: /documentation/Contacts
source_url: https://developer.apple.com/documentation/Contacts
source_locale: en-US
section: docc
content_type: symbol
title: Contacts
original_title: Contacts
source_hash: 5d91145aa91466c9b5d5d8b339fad582662223fc399329dccb5bcdd3a85874f6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:44:32+00:00'
last_translated_at: '2026-03-14T00:03:00+09:00'
---

# Contacts

사용자의 연락처에 접근하고, 연락처 정보를 포맷하고 현지화합니다.

## 개요

Contacts 프레임워크는 사용자의 연락처 정보에 접근하기 위한 Swift 및 Objective-C API를 제공합니다. 대부분의 앱은 연락처 정보를 읽기만 하고 변경하지 않기 때문에, 이 프레임워크는 스레드 안전한 읽기 전용 사용에 최적화되어 있습니다.

### 사용자의 연락처 다루기

Contacts 프레임워크는 모든 Apple 플랫폼에서 사용할 수 있으며, iOS와 macOS의 Address Book 프레임워크를 대체합니다.

#### 연락처 객체

연락처 클래스([CNContact](https://developer.apple.com/documentation/contacts/cncontact))는 연락처의 이름, 이미지, 전화번호 같은 연락처 속성을 담는 스레드 안전한 불변 값 객체입니다.

![연락처 객체에 mutable 변형이 있으며, labeled value 객체가 나타내는 속성을 가질 수 있음을 보여 주는 조직도입니다.](https://developer.apple.com)

연락처 클래스는 [NSDictionary](https://developer.apple.com/documentation/Foundation/NSDictionary)와 비슷하게, 연락처 속성을 수정할 때 사용할 수 있는 mutable 서브클래스 [CNMutableContact](https://developer.apple.com/documentation/contacts/cnmutablecontact)를 갖고 있습니다. 전화번호나 이메일 주소처럼 여러 값을 가질 수 있는 연락처 속성에는 프레임워크가 [CNLabeledValue](https://developer.apple.com/documentation/contacts/cnlabeledvalue) 객체 배열을 사용합니다. labeled value 클래스는 스레드 안전한 불변 label-값 튜플입니다. label은 각 값을 사용자에게 설명해 주므로, 집 전화번호와 직장 전화번호처럼 서로를 구분할 수 있게 합니다. Contacts 프레임워크는 미리 정의된 몇 가지 label을 제공하며, 직접 사용자 정의 label을 만들 수도 있습니다.

```swift
import UIKit
import Contacts
 
// 연락처에 추가할 mutable 객체를 생성합니다.
let contact = CNMutableContact()

// 프로필 사진을 데이터로 저장합니다.
let image = UIImage(systemName: "person.crop.circle")
contact.imageData = image?.jpegData(compressionQuality: 1.0)

contact.givenName = "John"
contact.familyName = "Appleseed"

let homeEmail = CNLabeledValue(label: CNLabelHome, value: "john@example.com" as NSString)
let workEmail = CNLabeledValue(label: CNLabelWork, value: "j.appleseed@icloud.com" as NSString)
contact.emailAddresses = [homeEmail, workEmail]

contact.phoneNumbers = [CNLabeledValue(
    label: CNLabelPhoneNumberiPhone,
    value: CNPhoneNumber(stringValue: "(408) 555-0126"))]

let homeAddress = CNMutablePostalAddress()
homeAddress.street = "One Apple Park Way"
homeAddress.city = "Cupertino"
homeAddress.state = "CA"
homeAddress.postalCode = "95014"
contact.postalAddresses = [CNLabeledValue(label: CNLabelHome, value: homeAddress)]

var birthday = DateComponents()
birthday.day = 1
birthday.month = 4
birthday.year = 1988  // (선택 사항) 연도가 없는 생일이라면 year 값을 생략합니다.
contact.birthday = birthday

// 새로 만든 연락처를 저장합니다.
let store = CNContactStore()
let saveRequest = CNSaveRequest()
saveRequest.add(contact, toContainerWithIdentifier: nil)

do {
    try store.execute(saveRequest)
} catch {
    print("Saving contact failed, error: \(error)")
    // 오류를 처리합니다.
}
```

#### 포맷팅과 현지화

Contacts 프레임워크는 연락처 정보를 포맷하고 현지화하는 데 도움을 줍니다. 예를 들어 [CNContactFormatter](https://developer.apple.com/documentation/contacts/cncontactformatter)를 사용해 연락처 이름을 올바르게 포맷하거나, [CNPostalAddressFormatter](https://developer.apple.com/documentation/contacts/cnpostaladdressformatter)를 사용해 국제 우편 주소를 포맷할 수 있습니다.

```swift
// 연락처 이름 포맷팅.
let fullName = CNContactFormatter.string(from: contact, style: .fullName)
print("\(String(describing: fullName))")
// John Appleseed

// 우편 주소 포맷팅.
let postalString = CNPostalAddressFormatter().string(from: homeAddress)
print("\(postalString)")
// One Apple Park Way
// Cupertino
// CA
// 95014
```

기기의 현재 locale 설정을 기반으로 현지화된 객체 속성 이름과 미리 정의된 label을 표시할 수 있습니다. [CNContact](https://developer.apple.com/documentation/contacts/cncontact) 같은 Contacts 프레임워크의 많은 객체에는 [localizedString(forKey:)](https://developer.apple.com/documentation/contacts/cnsocialprofile/localizedstring(forkey:)) 메서드가 포함되어 있어, key 이름의 현지화된 버전을 얻을 수 있습니다. 또한 [CNLabeledValue](https://developer.apple.com/documentation/contacts/cnlabeledvalue) 클래스에는 [localizedString(forLabel:)](https://developer.apple.com/documentation/contacts/cnlabeledvalue/localizedstring(forlabel:)) 메서드가 포함되어 있어 Contacts 프레임워크의 미리 정의된 label에 대한 현지화된 label을 얻을 수 있습니다.

```swift
// 기기의 locale은 스페인어입니다.
let displayName = CNContact.localizedString(forKey: CNContactNicknameKey)
print(displayName)
// "alias"를 출력합니다.

let displayLabel = CNLabeledValue<NSString>.localizedString(forLabel: CNLabelHome)
print(displayLabel)
// "casa"를 출력합니다.
```

#### 연락처 가져오기

사용자의 연락처 데이터베이스를 나타내는 contact store([CNContactStore](https://developer.apple.com/documentation/contacts/cncontactstore))를 사용해 연락처를 가져올 수 있습니다. contact store는 모든 I/O 작업을 캡슐화하며 연락처와 그룹을 가져오고 저장하는 책임을 집니다. contact store 메서드는 동기식이므로, 백그라운드 스레드에서 사용하는 것이 모범 사례입니다. 필요하다면 불변 fetch 결과를 안전하게 메인 스레드로 다시 보낼 수 있습니다.

Contacts 프레임워크는 사전 정의된 predicate와 [keysToFetch](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) 속성을 포함해, fetch 결과로 반환될 연락처를 제한하는 여러 방법을 제공합니다.

[CNContact](https://developer.apple.com/documentation/contacts/cncontact)는 가져오려는 연락처를 필터링하기 위한 predicate를 제공합니다. 예를 들어 이름이 *Appleseed*인 연락처를 가져오려면 [predicateForContacts(matchingName:)](https://developer.apple.com/documentation/contacts/cncontact/predicateforcontacts(matchingname:))를 사용하고 `Appleseed`를 전달합니다.

```swift
let predicate = CNContact.predicateForContacts(matchingName: "Appleseed")
```

Contacts 프레임워크는 일반 predicate와 복합 predicate를 지원하지 않는다는 점에 유의합니다.

[keysToFetch](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch)를 사용해 가져올 연락처 속성을 제한할 수 있습니다. 예를 들어 연락처의 이름과 성만 가져오려면 [keysToFetch](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) 배열에 해당 연락처 key를 지정합니다.

```swift
let keysToFetch = [CNContactGivenNameKey, CNContactFamilyNameKey] as [CNKeyDescriptor]
```

predicate([predicateForContacts(matchingName:)](https://developer.apple.com/documentation/contacts/cncontact/predicateforcontacts(matchingname:)))와 [keysToFetch](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) 배열을 모두 사용해 연락처를 가져오려면 [unifiedContacts(matching:keysToFetch:)](https://developer.apple.com/documentation/contacts/cncontactstore/unifiedcontacts(matching:keystofetch:))를 사용합니다.

```swift
let store = CNContactStore()
do {
    let predicate = CNContact.predicateForContacts(matchingName: "Appleseed")
    let contacts = try store.unifiedContacts(matching: predicate, keysToFetch: keysToFetch)
    print("Fetched contacts: \(contacts)")
} catch {
    print("Failed to fetch contact, error: \(error)")
    // 오류를 처리합니다.
}
```

Contacts 프레임워크는 가져온 연락처에 대해 연락처 이름 포맷팅 같은 작업도 수행할 수 있습니다. 각 작업은 올바르게 수행되기 위해 특정 연락처 key 집합을 필요로 합니다. 이 연락처 key는 key descriptor 객체이며, [keysToFetch](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) 배열 안에 포함해야 합니다. 예를 들어 연락처의 이메일 주소를 가져오면서 동시에 [CNContactFormatter](https://developer.apple.com/documentation/contacts/cncontactformatter)를 사용해 연락처 이름을 포맷할 수 있게 하려면, [keysToFetch](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) 배열 안에 [CNContactEmailAddressesKey](https://developer.apple.com/documentation/contacts/cncontactemailaddresseskey)와 [descriptorForRequiredKeys(for:)](https://developer.apple.com/documentation/contacts/cncontactformatter/descriptorforrequiredkeys(for:))가 반환하는 key descriptor 객체를 모두 포함해야 합니다.

```swift
let keysToFetch = [CNContactEmailAddressesKey as CNKeyDescriptor, CNContactFormatter.descriptorForRequiredKeys(for: .fullName)]
```

#### 개인 정보 보호

사용자는 앱별로 연락처 데이터 접근을 허용하거나 거부할 수 있습니다. [CNContactStore](https://developer.apple.com/documentation/contacts/cncontactstore)를 호출하면 사용자가 접근을 허용할지 거부할지 묻는 동안 앱이 대기합니다. 사용자는 앱이 처음 접근을 요청할 때만 프롬프트를 받으며, 이후의 [CNContactStore](https://developer.apple.com/documentation/contacts/cncontactstore) 호출은 기존 권한을 사용한다는 점에 유의하세요. 앱 UI의 메인 스레드가 이 접근 때문에 막히는 것을 피하려면 비동기 메서드 [requestAccess(for:completionHandler:)](https://developer.apple.com/documentation/contacts/cncontactstore/requestaccess(for:completionhandler:))를 사용하거나, [CNContactStore](https://developer.apple.com/documentation/contacts/cncontactstore) 사용을 백그라운드 스레드로 보내면 됩니다.

:::important Important
iOS 10 이상에 링크되는 iOS 앱은 접근이 필요한 데이터 유형에 대한 usage description key를 `Info.plist` 파일에 포함해야 하며, 그렇지 않으면 앱이 크래시합니다. 특히 Contacts 데이터에 접근하려면 [NSContactsUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW14)을 포함해야 합니다.
:::

#### 부분 연락처

시스템이 contact store에서 연락처 객체의 일부 속성만 가져오면 부분 연락처가 만들어집니다. 가져온 모든 연락처 객체는 부분 연락처입니다. 시스템이 가져오지 않은 속성 값에 접근하려고 하면 예외가 발생합니다. 시스템이 연락처에서 어떤 key를 가져왔는지 확실하지 않다면, 속성 값에 접근하기 전에 사용 가능 여부를 확인합니다. [isKeyAvailable(_:)](https://developer.apple.com/documentation/contacts/cncontact/iskeyavailable(_:))를 사용해 단일 연락처 key의 사용 가능 여부를 확인하거나, [areKeysAvailable(_:)](https://developer.apple.com/documentation/contacts/cncontact/arekeysavailable(_:))를 사용해 여러 key를 확인할 수 있습니다. 원하는 key를 사용할 수 없다면, 해당 key를 포함해 연락처를 다시 가져옵니다.

```swift
// 지정한 연락처에서 전화번호를 사용할 수 있는지 확인합니다.
if contact.isKeyAvailable(CNContactPhoneNumbersKey) {
    print("\(contact.phoneNumbers)")
} else {
    // key를 다시 가져옵니다.
    let keysToFetch = [CNContactGivenNameKey, CNContactFamilyNameKey, CNContactPhoneNumbersKey] as [CNKeyDescriptor]

    do {
        let refetchedContact = try store.unifiedContact(withIdentifier: contact.identifier, keysToFetch: keysToFetch)
        print("\(refetchedContact.phoneNumbers)")
    } catch {
        print("Failed to fetch contact, error: \(error)")
        // 오류를 처리합니다.
    }
}
```

#### 통합 연락처

같은 사람을 나타내는 서로 다른 계정의 연락처를 자동으로 연결할 수 있습니다. 연결된 연락처는 macOS와 iOS 앱에서 통합 연락처로 표시됩니다. 통합 연락처는 시스템이 연결된 연락처 집합을 하나의 연락처로 병합한 메모리 내 임시 뷰입니다.

![한 사람의 iCloud 계정과 소셜 미디어 계정 연락처 정보가 단일 통합 연락처로 병합되는 모습을 보여 주는 다이어그램입니다.](https://developer.apple.com)

기본적으로 Contacts 프레임워크는 통합 연락처를 반환합니다. 가져온 각 통합 연락처 객체([CNContact](https://developer.apple.com/documentation/contacts/cncontact))는 연결된 연락처 집합 안의 개별 연락처 식별자와는 다른 고유 식별자를 가집니다. 통합 연락처를 다시 가져올 때는 반드시 해당 식별자를 사용해야 합니다.

#### 연락처 저장

contact store([CNContactStore](https://developer.apple.com/documentation/contacts/cncontactstore))는 Contacts 프레임워크 객체에 대한 변경 사항도 저장합니다. [CNSaveRequest](https://developer.apple.com/documentation/contacts/cnsaverequest) 클래스는 저장 작업을 가능하게 하며, 여러 연락처와 그룹에 대한 변경을 하나의 작업으로 일괄 처리할 수 있게 합니다. 아래 코드 예제처럼, 저장 요청에 모든 객체를 추가한 뒤 contact store를 사용해 실행할 수 있습니다. 저장이 실행되는 동안 저장 요청 안의 객체에 접근하지 마세요. 객체가 수정될 수 있기 때문입니다.

:::note Note
[CNSaveRequest](https://developer.apple.com/documentation/contacts/cnsaverequest)는 watchOS에서는 사용할 수 없습니다.
:::

새 연락처를 만들고 저장합니다.

```swift
// 새 연락처를 생성합니다.
let newContact = CNMutableContact()
newContact.givenName = "John"
newContact.familyName = "Appleseed"

// 연락처를 저장합니다.
let saveRequest = CNSaveRequest()
saveRequest.add(newContact, toContainerWithIdentifier: nil)

do {
    try store.execute(saveRequest)
} catch {
    print("Saving contact failed, error: \(error)")
    // 오류를 처리합니다.
}
```

기존 연락처를 수정하고 저장합니다.

```swift
// John Appleseed의 집 이메일 주소를 업데이트합니다.
guard let mutableContact = contact.mutableCopy() as? CNMutableContact else { return }
let newEmail = CNLabeledValue(label: CNLabelHome, value: "john@example.com" as NSString)
mutableContact.emailAddresses.append(newEmail)

let saveRequest = CNSaveRequest()
saveRequest.update(mutableContact)
do {
    try store.execute(saveRequest)
} catch {
    print("Saving contact failed, error: \(error)")
    // 오류를 처리합니다.
}
```

#### 연락처 변경 알림

저장을 성공적으로 실행한 뒤 contact store는 기본 notification center에 [CNContactStoreDidChange](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/CNContactStoreDidChange) 알림을 게시합니다. Contacts 프레임워크 객체를 캐시하고 있다면, 식별자나 원래 fetch에 사용했던 predicate를 사용해 해당 객체들을 다시 가져온 뒤 캐시된 객체를 해제해야 합니다. 캐시된 객체는 오래된 상태이지만 무효한 것은 아니라는 점에 유의하세요.

#### 컨테이너와 그룹

사용자는 기기의 로컬 계정 또는 연락처 동기화용으로 설정한 서버 계정에 연락처를 가질 수 있습니다. 각 계정에는 최소 하나 이상의 연락처 컨테이너가 있습니다. 하나의 연락처는 오직 하나의 컨테이너에만 속할 수 있습니다.

![한 사람의 iCloud 연락처용 컨테이너 하나와 소셜 미디어 계정 연락처용 컨테이너 하나, 총 두 개의 컨테이너를 보여 주는 다이어그램입니다.](https://developer.apple.com)

그룹은 컨테이너 안의 연락처 집합입니다. 모든 계정이 그룹을 지원하는 것은 아니며, 일부 계정은 하위 그룹도 지원합니다. iCloud 계정은 하나의 컨테이너만 가지며 많은 그룹을 가질 수 있지만 하위 그룹은 없습니다. Exchange 계정은 그룹을 지원하지 않지만, Exchange 폴더를 나타내는 여러 컨테이너를 가질 수 있습니다.

![한 사람의 iCloud 연락처용 컨테이너와 소셜 미디어 계정 연락처용 컨테이너를 보여 주는 다이어그램입니다. iCloud 컨테이너 안에는 각각 세 연락처를 가진 두 개의 그룹이 있으며, 이 두 그룹은 한 연락처를 공유합니다. 소셜 미디어 계정 컨테이너 안에는 두 연락처를 가진 하나의 그룹이 있습니다.](https://developer.apple.com)

:::topic-grid
## 핵심 항목
- [Accessing the contact store](https://developer.apple.com/documentation/contacts/accessing-the-contact-store): 사용자의 연락처 데이터를 읽고 쓸 수 있도록 권한을 요청합니다.
- [Accessing a person’s contact data using Contacts and ContactsUI](https://developer.apple.com/documentation/contacts/accessing-a-person-s-contact-data-using-contacts-and-contactsui): Contact access button과 Contact access picker를 앱에 추가해 사용자가 연락처 데이터 접근을 허용할 수 있게 합니다.
- [CNContactStore](https://developer.apple.com/documentation/contacts/cncontactstore): 사용자의 Contacts 데이터베이스에서 연락처, 그룹, 컨테이너를 가져오고 저장하는 객체입니다.
- [NSContactsUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSContactsUsageDescription): 앱이 왜 사용자의 연락처 접근을 요청하는지 알려 주는 메시지입니다.
- [com.apple.developer.contacts.notes](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.contacts.notes): 앱이 연락처 항목의 메모에 접근할 수 있는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 연락처 데이터
- [CNContact](https://developer.apple.com/documentation/contacts/cncontact): 연락처의 이름, 전화번호, 주소처럼 단일 연락처에 대한 정보를 저장하는 불변 객체입니다.
- [CNMutableContact](https://developer.apple.com/documentation/contacts/cnmutablecontact): 연락처의 이름, 전화번호, 주소처럼 단일 연락처에 대한 정보를 저장하는 mutable 객체입니다.
- [Data Objects](https://developer.apple.com/documentation/contacts/data-objects): 사용자의 우편 주소와 전화번호처럼 연락처 관련 데이터에 접근합니다.
- [Contact Keys](https://developer.apple.com/documentation/contacts/contact-keys): fetch 작업 중 연락처 관련 속성을 지정합니다.
:::

:::topic-grid
## Fetch 및 저장 요청
- [CNContactFetchRequest](https://developer.apple.com/documentation/contacts/cncontactfetchrequest): 연락처를 가져올 때 사용할 옵션을 정의하는 객체입니다.
- [CNFetchRequest](https://developer.apple.com/documentation/contacts/cnfetchrequest): 연락처 fetch 요청의 기본 클래스입니다.
- [CNFetchResult](https://developer.apple.com/documentation/contacts/cnfetchresult): 변경 기록 fetch 요청의 결과를 나타내는 객체입니다.
- [CNSaveRequest](https://developer.apple.com/documentation/contacts/cnsaverequest): 사용자의 연락처 데이터베이스에 저장하려는 변경 사항을 모으는 객체입니다.
:::

:::topic-grid
## 변경 기록 데이터
- [CNChangeHistoryAddContactEvent](https://developer.apple.com/documentation/contacts/cnchangehistoryaddcontactevent): 사용자가 연락처를 추가한 일을 나타내는 객체입니다.
- [CNChangeHistoryAddGroupEvent](https://developer.apple.com/documentation/contacts/cnchangehistoryaddgroupevent): 사용자가 그룹을 추가한 일을 나타내는 객체입니다.
- [CNChangeHistoryAddMemberToGroupEvent](https://developer.apple.com/documentation/contacts/cnchangehistoryaddmembertogroupevent): 사용자가 연락처를 그룹에 추가한 일을 나타내는 객체입니다.
- [CNChangeHistoryAddSubgroupToGroupEvent](https://developer.apple.com/documentation/contacts/cnchangehistoryaddsubgrouptogroupevent): 사용자가 하위 그룹을 그룹에 추가한 일을 나타내는 객체입니다.
- [CNChangeHistoryDeleteContactEvent](https://developer.apple.com/documentation/contacts/cnchangehistorydeletecontactevent): 사용자가 연락처를 삭제한 일을 나타내는 객체입니다.
- [CNChangeHistoryDeleteGroupEvent](https://developer.apple.com/documentation/contacts/cnchangehistorydeletegroupevent): 사용자가 그룹을 삭제한 일을 나타내는 객체입니다.
- [CNChangeHistoryDropEverythingEvent](https://developer.apple.com/documentation/contacts/cnchangehistorydropeverythingevent): 변경 이벤트를 처리하기 전에 delegate가 모든 연락처와 그룹을 버려야 함을 나타내는 객체입니다.
- [CNChangeHistoryEvent](https://developer.apple.com/documentation/contacts/cnchangehistoryevent): 사용자가 연락처나 그룹을 추가, 업데이트, 삭제한 일을 나타내는 객체입니다.
- [CNChangeHistoryFetchRequest](https://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest): 변경 기록을 가져오기 위한 기준을 지정하는 객체입니다.
- [CNChangeHistoryRemoveMemberFromGroupEvent](https://developer.apple.com/documentation/contacts/cnchangehistoryremovememberfromgroupevent): 사용자가 그룹에서 연락처를 제거한 일을 나타내는 객체입니다.
- [CNChangeHistoryRemoveSubgroupFromGroupEvent](https://developer.apple.com/documentation/contacts/cnchangehistoryremovesubgroupfromgroupevent): 사용자가 그룹에서 하위 그룹을 제거한 일을 나타내는 객체입니다.
- [CNChangeHistoryUpdateContactEvent](https://developer.apple.com/documentation/contacts/cnchangehistoryupdatecontactevent): 사용자가 연락처를 업데이트한 일을 나타내는 객체입니다.
- [CNChangeHistoryUpdateGroupEvent](https://developer.apple.com/documentation/contacts/cnchangehistoryupdategroupevent): 업데이트된 그룹 이벤트를 나타내는 객체입니다.
- [CNChangeHistoryEventVisitor](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor): 연락처와 그룹의 변경 알림을 받기 위한 인터페이스입니다.
:::

:::topic-grid
## 포매터
- [CNContactFormatter](https://developer.apple.com/documentation/contacts/cncontactformatter): 연락처 정보를 사용자에게 보여 주기 전에 포맷하는 데 사용하는 객체입니다.
- [CNPostalAddressFormatter](https://developer.apple.com/documentation/contacts/cnpostaladdressformatter): 연락처의 우편 주소를 포맷하는 데 사용하는 객체입니다.
- [CNContactVCardSerialization](https://developer.apple.com/documentation/contacts/cncontactvcardserialization): 사용자의 연락처를 vCard 표현과 상호 변환할 때 사용하는 객체입니다.
- [CNContactsUserDefaults](https://developer.apple.com/documentation/contacts/cncontactsuserdefaults): 연락처를 표시할 때 사용할 기본 옵션을 정의하는 객체입니다.
:::

:::topic-grid
## 오류
- [Error Information](https://developer.apple.com/documentation/contacts/error-information): Contacts 프레임워크가 생성한 오류를 진단합니다.
:::
