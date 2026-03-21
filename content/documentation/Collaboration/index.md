---
route: /documentation/Collaboration
source_url: https://developer.apple.com/documentation/Collaboration
source_locale: en-US
section: docc
content_type: symbol
title: Collaboration
original_title: Collaboration
source_hash: 9494ed3e6f9e8aade032fd55f7227169e9bc89f1ae63e38718544b19b5da145f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:41:06+00:00'
last_translated_at: '2026-03-14T01:17:00+09:00'
---

# Collaboration

사용자와 그룹 같은 identity를 찾고 접근합니다. 또한 사용자가 identity를 만들고 선택할 수 있는 Identity Picker를 표시합니다.

## 개요

Collaboration 프레임워크를 사용하면 개발자가 identity와 그 속성을 모니터링할 수 있습니다. Identity는 사용자의 시스템 로컬에 있거나 네트워크 디렉터리에 있는 identity authority 안에 존재합니다. Collaboration 프레임워크는 앱이 identity를 선택할 수 있도록 identity picker라고 하는 sheet도 관리합니다.

Collaboration 프레임워크는 Core Services Identity API와 긴밀하게 함께 동작해 Identity Services 기술을 구성합니다. identity를 만들고 조작하는 기능이 필요하다면 [Core Services Identity Reference](https://developer.apple.com/library/archive/documentation/Networking/Reference/IdentityServices_Ref/index.html#//apple_ref/doc/uid/TP40004673)를 읽어 보십시오.

:::topic-grid
## 클래스
- [CBGroupIdentity](https://developer.apple.com/documentation/collaboration/cbgroupidentity): 그룹 identity를 나타내는 객체이며, identity authority에서 그룹 identity의 속성을 확인하는 데 사용합니다. 이 객체의 주요 속성은 POSIX 그룹 식별자(GID)와 구성원 목록입니다.
- [CBIdentity](https://developer.apple.com/documentation/collaboration/cbidentity): identity authority에 저장된 identity의 속성에 접근할 때 사용하는 객체입니다. identity 객체를 사용해 identity를 찾고, 이를 access control list(ACL)에 저장할 수 있습니다. 이러한 속성을 편집해야 한다면 Core Services의 클래스를 활용하십시오.
- [CBIdentityAuthority](https://developer.apple.com/documentation/collaboration/cbidentityauthority): identity authority는 identity 정보를 저장하는 데이터베이스입니다. 이 클래스는 하나 이상의 identity authority를 정의합니다. 클래스 factory method와 함께 이 데이터베이스에서 identity를 검색할 수 있습니다.
- [CBIdentityPicker](https://developer.apple.com/documentation/collaboration/cbidentitypicker): 사용자가 하나 이상의 서비스나 공유 리소스에 접근 권한을 줄 identity, 예를 들어 사용자 또는 그룹 객체를 선택할 수 있게 하는 객체입니다. identity picker는 앱 모달 대화상자나 문서 윈도우에 부착된 sheet로 표시할 수 있습니다. identity picker는 선택된 레코드를 반환해 Collaboration을 사용한 access control list에 추가할 수 있게 합니다. 선택한 레코드가 사용자나 그룹 identity가 아니라면, identity picker는 해당 레코드를 공유 계정으로 승격하기 위해 암호 같은 추가 정보를 사용자에게 요청합니다.
- [CBUserIdentity](https://developer.apple.com/documentation/collaboration/cbuseridentity): 사용자 identity를 나타내는 객체이며, identity authority에서 사용자 identity의 속성에 접근하는 데 사용합니다. 주요 속성은 POSIX 사용자 식별자(UID), 암호, 인증서입니다.
:::
