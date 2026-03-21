---
route: /documentation/AddressBookUI
source_url: https://developer.apple.com/documentation/AddressBookUI
source_locale: en-US
section: docc
content_type: symbol
title: Address Book UI
original_title: Address Book UI
source_hash: 35b912b006abdae5d91c8e6e397d12dc83595c0f8d78d0e0e07984ee993bfb33
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:11:25+00:00'
last_translated_at: '2026-03-13T23:11:40+09:00'
---

# Address Book UI

사용자의 연락처에 접근하고 이를 그래픽 인터페이스로 표시합니다.

## 개요

AddressBookUI 프레임워크는 Address Book 데이터베이스에 있는 레코드를 표시하고, 편집하고, 선택하고, 생성하는 작업을 쉽게 해 주는 컨트롤러를 제공합니다.

:::important Important
iOS 9 이상에서는 AddressBookUI 프레임워크를 사용하지 마십시오. 대신 [Contacts UI](https://developer.apple.com/documentation/ContactsUI) 프레임워크에 정의된 API를 사용하십시오.
:::

:::topic-grid
## 사람 선택기
- [ABPeoplePickerNavigationController](https://developer.apple.com/documentation/addressbookui/abpeoplepickernavigationcontroller): 주소록에서 연락처나 연락처 정보 항목 하나를 선택할 수 있도록 여러 뷰를 관리하는 뷰 컨트롤러입니다.
:::

:::topic-grid
## 상세 표시
- [ABNewPersonViewController](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller): 연락처를 생성하는 인터페이스를 제공하는 뷰 컨트롤러입니다.
- [ABPersonViewController](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller): 사람 레코드를 표시하는 데 사용하는 뷰를 구현합니다.
- [ABUnknownPersonViewController](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller): 사람 속성 집합으로부터 사람 레코드를 생성하는 데 사용하는 뷰 컨트롤러를 구현합니다.
- [ABCreateStringWithAddressDictionary(_:_:)](https://developer.apple.com/documentation/addressbookui/abcreatestringwithaddressdictionary(_:_:)): 주소 속성으로부터 서식이 적용된 주소 문자열을 반환합니다.
:::
