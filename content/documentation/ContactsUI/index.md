---
route: /documentation/ContactsUI
source_url: https://developer.apple.com/documentation/ContactsUI
source_locale: en-US
section: docc
content_type: symbol
title: Contacts UI
original_title: Contacts UI
source_hash: 41c78bff0e1b0a91f9c240ccd875085cd15a75694100a4d337e180859e28b296
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:16:02+00:00'
last_translated_at: '2026-03-13T22:31:00+09:00'
---

# Contacts UI

사용자가 자신의 연락처 정보를 표시할 수 있게 해 주는 인터페이스를 제공합니다.

## 개요

Contacts UI 프레임워크는 앱 안에서 사용자의 연락처에 접근할 수 있게 해 주는 사용자 인터페이스 객체를 포함합니다. 연락처 사용에 대한 앱의 권한 수준([authorizationStatus(for:)](https://developer.apple.com/documentation/Contacts/CNContactStore/authorizationStatus(for:))이 나타내는 값)에 따라 앱은 연락처를 표시, 편집, 선택, 생성할 수 있습니다. 권한 수준이 [CNAuthorizationStatus.limited](https://developer.apple.com/documentation/Contacts/CNAuthorizationStatus/limited)인 경우, 사용자가 현재 앱에 허용한 제한된 연락처 집합을 넘어 더 많은 연락처 접근을 요청하기 위해 [ContactAccessButton](https://developer.apple.com/documentation/contactsui/contactaccessbutton)을 표시할 수 있습니다.

:::topic-grid
## 연락처 뷰어
- [CNContactViewController](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller): 새 연락처, 알 수 없는 연락처, 기존 연락처를 표시하는 view controller입니다.
:::

:::topic-grid
## 연락처 선택기
- [CNContactPickerViewController](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller): 연락처를 선택하는 인터페이스를 표시하는 view controller입니다.
- [CNContactPicker](https://developer.apple.com/documentation/contactsui/cncontactpicker): 연락처 선택을 위한 popover 기반 인터페이스입니다.
:::

:::topic-grid
## 연락처 접근
- [ContactAccessButton](https://developer.apple.com/documentation/contactsui/contactaccessbutton): 사용자가 앱과 공유하는 연락처 집합에 항목을 추가할 때 사용하는 SwiftUI button입니다.
:::

:::topic-grid
## 클래스
- [CNHostingRemovePhotoButton](https://developer.apple.com/documentation/contactsui/cnhostingremovephotobutton)
:::
