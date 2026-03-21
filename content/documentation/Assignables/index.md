---
route: /documentation/Assignables
source_url: https://developer.apple.com/documentation/Assignables
source_locale: en-US
section: docc
content_type: symbol
title: Assignables
original_title: Assignables
source_hash: 3fa93386eeb64b4b06f27a7d5c563ea00fa01d361211e850ba7be9c413edf1f0
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:54:28+00:00'
last_translated_at: '2026-03-13T21:38:00+09:00'
---

# Assignables

평가를 만들고 그 평가 위에서 학생 작업을 수행할 수 있도록 PDF를 감싸는 래퍼를 포함하는 프레임워크입니다.

## 개요

[AssignableDocument](https://developer.apple.com/documentation/assignables/assignabledocument)는 기본 PDF를 포함하고, 해당 PDF에 추가된 markup, annotation, question, scoring option을 저장하는 문서입니다.

이 프레임워크는 학생과 교사의 경험에 초점을 둡니다. 교사는 [AssignableDocument](https://developer.apple.com/documentation/assignables/assignabledocument)로부터 [AssignedWorkDocument](https://developer.apple.com/documentation/assignables/assignedworkdocument)를 만들어 문서를 학생에게 할당할 수 있습니다. 이러한 데이터 타입 외에도 Assignables는 자체 view 안에서 이 문서들을 편집할 수 있도록 SwiftUI view 클래스도 제공합니다.

학생이 작업을 마치면 이를 교사에게 반환해 점수를 받고 작업에 대한 의견을 받을 수 있습니다.

이 모든 단계에서 저작자 정보가 중요하므로, Assignables는 [UserIdentity](https://developer.apple.com/documentation/assignables/useridentity)를 따르는 타입을 사용해 어떤 문서에 대한 변경 사항이 누구에게 속하는지 표시할 수 있도록 지원합니다.

교사들이 assignable을 만들거나 학생 작업을 채점하는 과정에서 협업할 수 있고, 학생들 또한 문서에서 협업할 수 있으므로, 두 문서 타입 모두 동일한 문서의 다른 사본과 현재 문서 사본을 병합할 수 있도록 지원합니다.

:::topic-grid
## 할당 가능한 문서
- [AssignableDocument](https://developer.apple.com/documentation/assignables/assignabledocument): assignable document는 학생이 평가를 수행할 수 있도록 교사가 PDF에 markup을 추가할 수 있게 하는 확장된 PDF입니다.
- [AssignedWorkDocument](https://developer.apple.com/documentation/assignables/assignedworkdocument): assigned work document는 특정 응시자에 대한 응시자 및 채점자 markup을 포함하는 문서입니다. 또한 기반이 되는 assignable document의 사본도 포함합니다.
- [Assignable](https://developer.apple.com/documentation/assignables/assignable): 이 프로토콜을 따르는 문서는 사용자에게 할당할 수 있습니다.
:::

:::topic-grid
## 구성
- [AssignableDocumentConfiguration](https://developer.apple.com/documentation/assignables/assignabledocumentconfiguration): assignable document의 옵션을 지정하는 타입입니다.
- [AssignedWorkDocumentConfiguration](https://developer.apple.com/documentation/assignables/assignedworkdocumentconfiguration): 문서의 점수를 지정하는 타입입니다.
:::

:::topic-grid
## 표현
- [AssignableDocumentView](https://developer.apple.com/documentation/assignables/assignabledocumentview): 문서를 표시하는 SwiftUI View입니다.
- [AssignedWorkDocumentView](https://developer.apple.com/documentation/assignables/assignedworkdocumentview): 할당된 작업 문서를 표시하는 SwiftUI View입니다.
:::

:::topic-grid
## 문서 요소
- [DocumentElement](https://developer.apple.com/documentation/assignables/documentelement): 문서 안에 포함된 요소를 나타냅니다. 이러한 요소는 문서 안에서 자신을 고유하게 식별하는 identifier를 가질 수 있습니다.
- [BasicDocumentElementID](https://developer.apple.com/documentation/assignables/basicdocumentelementid): 문서 요소 식별자에 대한 기본 구현입니다.
- [DocumentElementID](https://developer.apple.com/documentation/assignables/documentelementid): 문서 안의 요소를 식별하는 identifier입니다.
- [AssignableDocumentElement](https://developer.apple.com/documentation/assignables/assignabledocumentelement): assignable document의 요소입니다.
- [AssignedWorkDocumentElement](https://developer.apple.com/documentation/assignables/assignedworkdocumentelement): assigned work document의 요소입니다.
:::

:::topic-grid
## 병합 가능한 문서
- [MergeableDocument](https://developer.apple.com/documentation/assignables/mergeabledocument): 이 프로토콜을 따르는 문서는 문서의 여러 사본을 하나의 문서로 병합할 수 있습니다.
- [MergeablePartsContainerPartID](https://developer.apple.com/documentation/assignables/mergeablepartscontainerpartid): 부품의 ID입니다.
- [MergeableDocumentPage](https://developer.apple.com/documentation/assignables/mergeabledocumentpage): 이 프로토콜을 따르는 타입은 자신이 적합한 객체 안의 페이지임을 나타냅니다.
- [MergeablePartsContainer](https://developer.apple.com/documentation/assignables/mergeablepartscontainer): 이 프로토콜을 따르는 객체는 자신의 다른 복제본을 병합하거나 자신의 개별 부품을 병합할 수 있습니다.
- [DocumentThumbnail](https://developer.apple.com/documentation/assignables/documentthumbnail): 페이지 전체 또는 일부의 이미지와 그 이미지가 속한 페이지의 ID를 담는 구조체입니다.
:::

:::topic-grid
## 정체성
- [UserIdentity](https://developer.apple.com/documentation/assignables/useridentity): 이 프로토콜을 따르는 타입은 문서 편집자의 사용자 identity 역할을 할 수 있습니다.
- [AnonymousUserIdentity](https://developer.apple.com/documentation/assignables/anonymoususeridentity): 알 수 없는 편집자를 위한 사용자 identity입니다.
- [AnyUserIdentity](https://developer.apple.com/documentation/assignables/anyuseridentity): 다른 사용자 identity를 감싸 type erasure를 수행하는 사용자 identity입니다.
- [StringUserIdentity](https://developer.apple.com/documentation/assignables/stringuseridentity): 문자열로 정의된 사용자 identity입니다.
- [UserIdentityTypeRegistry](https://developer.apple.com/documentation/assignables/useridentitytyperegistry): 사용자 identity 타입을 위한 registry입니다. assignable document와 document element는 사용자 identity 데이터를 객체 형태로 저장합니다. 이 데이터를 역직렬화하려면 어떤 타입으로 역직렬화할지 `Assignables`가 알아야 합니다. 사용자 identity를 등록하지 않으면 사용자 정의 타입은 역직렬화할 수 없습니다.
- [UserIdentityFactory](https://developer.apple.com/documentation/assignables/useridentityfactory): 사용자 identity 객체를 생성하는 도우미를 담는 타입입니다.
:::
