---
route: /documentation/LocalAuthenticationEmbeddedUI
source_url: https://developer.apple.com/documentation/LocalAuthenticationEmbeddedUI
source_locale: en-US
section: docc
content_type: symbol
title: Local Authentication Embedded UI
original_title: Local Authentication Embedded UI
source_hash: 3a770c3cbaa9b4f3ad999d64606489b8aa94abe2fc6db208e904c79f28fc79a0
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:04:41+00:00'
last_translated_at: '2026-03-14T03:18:00+09:00'
---

# Local Authentication Embedded UI

사용자 정의 인증 view 안에 표준 local authentication view 아이콘을 표시합니다.

## 개요

`Local Authentication` 프레임워크로 사용자를 인증할 때 프레임워크는 기본적으로 모든 사용자 상호 작용을 처리합니다. 사용자 정의 인증 사용자 인터페이스를 만들고 싶다면 [LAAuthenticationView](https://developer.apple.com/documentation/localauthenticationembeddedui/laauthenticationview) 인스턴스를 중심으로 이를 구축하십시오. authentication view는 Touch ID 아이콘처럼 사용자가 biometric authentication과 연결해 인식하는 아이콘을 표시하고, 시간이 지남에 따라 인증 상태의 변화를 반영하도록 그 아이콘을 수정합니다. 필요하다면 사용자 정의 view에 다른 텍스트, 이미지, 상호 작용 요소를 추가할 수 있습니다.

![Access My Transactions 제목 아래 원형 지문 아이콘이 있고 그 아래에 보안 텍스트 입력 필드가 있는 view의 스크린샷입니다. 지문 아이콘이 강조되어 있습니다.](https://developer.apple.com)

모든 local authentication 작업에서 시스템은 기반이 되는 biometric 데이터를 관리하지만, local authentication view를 사용하면 앱 디자인에 맞게 인증 인터페이스를 사용자화할 수 있습니다. 동시에 익숙한 도상은 사용자가 무엇을 요청받고 있는지 이해하는 데 도움을 줍니다.

:::topic-grid
## Local Authentication View
- [LAAuthenticationView](https://developer.apple.com/documentation/localauthenticationembeddedui/laauthenticationview): biometric authentication 상태를 그래픽으로 표현한 것입니다.
:::

:::topic-grid
## 참고 자료
- [Local Authentication Embedded UI Data Types](https://developer.apple.com/documentation/localauthenticationembeddedui/local-authentication-embedded-ui-data-types)
:::
