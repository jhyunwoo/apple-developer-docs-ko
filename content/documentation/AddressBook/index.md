---
route: /documentation/AddressBook
source_url: https://developer.apple.com/documentation/AddressBook
source_locale: en-US
section: docc
content_type: symbol
title: Address Book
original_title: Address Book
source_hash: ee42c15a289cdc97eca05005dfaf850016b6eb52187db9043cf1e984a61ed8c2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:10:37+00:00'
last_translated_at: '2026-03-14T00:36:00+09:00'
---

# Address Book

사용자의 연락처를 저장하는 중앙 데이터베이스에 접근합니다.

## 개요

Address Book은 연락처와 그들의 개인 정보를 담는 중앙 데이터베이스입니다. 사용자는 자신과 친구들에 대한 개인 정보를 필요할 때마다 반복해서 입력하지 않고, 한 번만 입력하면 됩니다. AddressBook 프레임워크를 지원하는 앱은 Apple의 Mail과 Messages를 포함한 다른 앱과 이 연락처 정보를 공유합니다.

:::important 중요
macOS 10.11 이상에서는 AddressBook 프레임워크를 사용하지 마십시오. 대신 [Contacts](https://developer.apple.com/documentation/Contacts) 프레임워크에 정의된 API를 사용하십시오.
:::

:::topic-grid
## 핵심 사항
- [ABAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class): Address Book 데이터베이스에 접근할 때 사용하는 기본 객체입니다.
:::

:::topic-grid
## 데이터 타입
- [ABPerson](https://developer.apple.com/documentation/addressbook/abperson): Address Book 데이터베이스에서 한 사람에 대한 모든 정보를 캡슐화하는 객체입니다.
- [ABGroup](https://developer.apple.com/documentation/addressbook/abgroup): Address Book 데이터베이스의 record 그룹을 나타내는 객체입니다.
- [ABMultiValue](https://developer.apple.com/documentation/addressbook/abmultivalue-swift.class): 여러 값을 가질 수 있는 프로퍼티의 불변 표현입니다.
- [ABMutableMultiValue](https://developer.apple.com/documentation/addressbook/abmutablemultivalue-swift.class): 여러 값을 가질 수 있는 프로퍼티의 가변 표현입니다.
- [ABImageClient](https://developer.apple.com/documentation/addressbook/abimageclient): 연락처와 연관된 이미지를 불러오는 요청에 응답하기 위한 메서드입니다.
- [ABRecord](https://developer.apple.com/documentation/addressbook/abrecord-swift.class): 모든 Address Book record의 공통 프로퍼티를 정의하는 추상 클래스입니다.
:::

:::topic-grid
## Pickers
- [ABPeoplePickerView](https://developer.apple.com/documentation/addressbook/abpeoplepickerview): 앱 사용자 인터페이스에서 people-picker view의 동작을 사용자화할 때 사용하는 객체입니다.
- [ABPersonView](https://developer.apple.com/documentation/addressbook/abpersonview): 연락처를 표시하고 편집하기 위한 view를 제공하는 객체입니다.
:::

:::topic-grid
## 검색 요소
- [ABSearchElement](https://developer.apple.com/documentation/addressbook/absearchelement): Address Book 데이터베이스의 record에 대한 검색 쿼리를 지정할 때 사용하는 객체입니다.
- [ABSearchElementRef](https://developer.apple.com/documentation/addressbook/absearchelementref): ABSearchElement 객체에 대한 참조입니다.
:::

:::topic-grid
## Action Plug-In
- [ABActionDelegate](https://developer.apple.com/documentation/addressbook/abactiondelegate): 사용자 정의 항목 위에 표시되는 rollover menu를 지원하려면 Address Book action plug-in을 구현합니다.
:::

:::topic-grid
## C 인터페이스
- [C Types](https://developer.apple.com/documentation/addressbook/c-types): Address Book 객체에 대응하는 C 타입을 식별합니다.
- [AddressBook Functions](https://developer.apple.com/documentation/addressbook/addressbook-functions): Address Book 데이터를 조작할 때 사용하는 C 함수와 함수형 매크로를 찾습니다.
- [Address Book Constants](https://developer.apple.com/documentation/addressbook/address-book-constants): Address Book 정보를 지정할 때 사용하는 상수를 확인합니다.
- [AddressBook Enumerations](https://developer.apple.com/documentation/addressbook/addressbook-enumerations): Address Book 정보를 지정할 때 사용하는 열거형을 확인합니다.
- [AddressBook Data Types](https://developer.apple.com/documentation/addressbook/addressbook-data-types): Address Book 정보를 지정할 때 사용하는 데이터 타입을 확인합니다.
:::

:::topic-grid
## Deprecated symbols
- [Deprecated symbols](https://developer.apple.com/documentation/addressbook/deprecated-symbols): 더 이상 지원되지 않는 symbol과 그 대체 항목을 검토합니다.
:::
