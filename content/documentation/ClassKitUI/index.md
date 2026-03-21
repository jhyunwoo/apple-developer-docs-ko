---
route: /documentation/ClassKitUI
source_url: https://developer.apple.com/documentation/ClassKitUI
source_locale: en-US
section: docc
content_type: symbol
title: ClassKit UI
original_title: ClassKit UI
source_hash: 801eb3214629e9f4119e23563bf38549d5e60fec805cf352a91605a61363ed66
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:08:35+00:00'
last_translated_at: '2026-03-13T22:06:00+09:00'
---

# ClassKit UI

앱에서 학생이 할당된 문서를 제출하거나 제출을 철회할 수 있게 해 주는 view를 표시합니다.

## 개요

ClassKit UI는 학생이 앱 안에서 자신에게 할당된 문서를 관리하도록 도와줍니다. 교사가 활동을 할당하면 학생은 이 view를 사용해 작업 제출, 제출 철회, 앱 안에서의 진행 상황 추적 같은 동작을 수행합니다.

이 프레임워크는 할당된 문서를 제출하는 view와, 상태 및 마감일 같은 제출 정보를 표시하는 view를 모두 제공합니다. 각 view는 ClassKit에서 할당 문서 데이터를 자동으로 가져오며, 제출 상태가 바뀌면 업데이트됩니다. 제출 전후에 실행되는 [closure](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/closures/)를 사용해 제출 과정을 사용자화할 수 있습니다. 예를 들어 학생이 과제 문서를 제출하려 할 때 앱은 해당 문서가 제출 준비가 되었는지 확인할 수 있습니다. 또한 제출 후에는 제출이 성공했다는 점을 알리는 경고를 앱이 표시할 수도 있습니다.

ClassKit UI를 사용하려면 앱에 [ClassKit Environment Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.ClassKit-environment) entitlement를 추가해야 하며, 이를 통해 ClassKit 통합이 활성화됩니다.

:::topic-grid
## 할당 문서 제출
- [AssignedDocumentSubmissionButton](https://developer.apple.com/documentation/classkitui/assigneddocumentsubmissionbutton): 할당 문서에 대한 제출 기능을 제공하는 버튼입니다.
- [AssignedDocumentDeferredMenuElement](https://developer.apple.com/documentation/classkitui/assigneddocumentdeferredmenuelement): 할당 문서 제출 기능을 제공하는 지연 메뉴 요소입니다.
- [AssignedDocumentMenuItem](https://developer.apple.com/documentation/classkitui/assigneddocumentmenuitem): 할당 문서 제출 기능을 제공하는 메뉴 항목입니다.
:::

:::topic-grid
## 할당 문서 정보 표시
- [AssignedDocumentLabel](https://developer.apple.com/documentation/classkitui/assigneddocumentlabel): 할당 문서의 상태 또는 날짜 정보를 표시하는 view입니다.
:::
