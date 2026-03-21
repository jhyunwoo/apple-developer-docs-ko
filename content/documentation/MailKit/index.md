---
route: /documentation/MailKit
source_url: https://developer.apple.com/documentation/MailKit
source_locale: en-US
section: docc
content_type: symbol
title: MailKit
original_title: MailKit
source_hash: 37eb4eb24d2e69db76a259b7e469dec9cf79a83c73378b6b7b8603e5b05631a2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:37:08+00:00'
last_translated_at: '2026-03-13T20:30:00+09:00'
---

# MailKit

사용자가 보내고 받는 이메일 메시지를 안전하게 만들고, 사용자화하고, 그 위에서 동작합니다.

## 개요

MailKit을 사용하면 앱에 Mail의 여러 기능을 사용자화하는 app extension을 포함할 수 있습니다. Mail app extension은 다음 향상 기능 중 하나 이상을 제공합니다.

- *content blocker*는 사용자가 메시지를 볼 때 콘텐츠 로드를 막는 규칙을 정의합니다.
- *action handler*는 Mail이 메시지를 다운로드할 때 플래그 지정, 색상 설정, 보관 같은 동작을 수행합니다.
- *compose session handler*는 수신자 이메일 주소를 검증하고, Mail의 작성 창에 view controller를 표시하고, 메시지가 전송에 적합한지 확인하며, 사용자 정의 헤더를 추가합니다.
- *message security handler*는 암호화와 디지털 서명을 사용해 메시지를 보호합니다.

확장의 진입점은 [MEExtension](https://developer.apple.com/documentation/mailkit/meextension)을 따르는 객체입니다. MailKit이 확장을 호출하면, 이 객체가 위 목록의 각 기능을 제공할 handler를 결정합니다.

:::topic-grid
## 핵심 사항
- [MEExtension](https://developer.apple.com/documentation/mailkit/meextension): 메시지에서 동작을 수행하거나 사용자가 메시지를 볼 때 콘텐츠를 차단하는 등 이메일 메시지를 조작하는 객체를 제공하는 타입입니다.
- [Build Mail App Extensions](https://developer.apple.com/documentation/mailkit/build-mail-app-extensions): 콘텐츠를 차단하고, 메시지와 작성 동작을 수행하며, 메시지 보안을 돕는 app extension을 만듭니다.
:::

:::topic-grid
## Content blocker
- [MEContentBlocker](https://developer.apple.com/documentation/mailkit/mecontentblocker): 메시지를 표시할 때 콘텐츠를 차단하기 위한 규칙 집합을 제공하는 객체입니다.
:::

:::topic-grid
## 메시지 동작
- [MEMessageActionHandler](https://developer.apple.com/documentation/mailkit/memessageactionhandler): 시스템이 메시지를 다운로드할 때 메시지에 대한 동작을 수행하는 객체입니다.
:::

:::topic-grid
## 작성 창 향상
- [MEComposeSessionHandler](https://developer.apple.com/documentation/mailkit/mecomposesessionhandler): 메일 메시지 작성에 참여하고 수신자 토큰에 주석을 다는 객체입니다.
:::

:::topic-grid
## 메시지 암호화, 복호화, 디지털 서명
- [MEMessageSecurityHandler](https://developer.apple.com/documentation/mailkit/memessagesecurityhandler): 사용자가 보내고 받는 메시지에 디지털 서명을 하거나 암호화하는 객체입니다.
:::

:::topic-grid
## 메시지 속성
- [MEMessage](https://developer.apple.com/documentation/mailkit/memessage): 제목, 수신자, 발송 날짜, 메시지 내용 같은 메일 메시지 정보를 담는 객체입니다.
- [MEMessageState](https://developer.apple.com/documentation/mailkit/memessagestate): 전송됨, 미전송, 수신됨 중 하나인 메시지의 상태입니다.
:::

:::topic-grid
## 사용자 정의 View Controller
- [MEExtensionViewController](https://developer.apple.com/documentation/mailkit/meextensionviewcontroller): compose session handler와 message security handler를 위한 view를 관리하는 객체입니다.
:::

:::topic-grid
## 구조체
- [MEMessageSecurityError](https://developer.apple.com/documentation/mailkit/memessagesecurityerror)
:::

:::topic-grid
## 클래스
- [MEComposeContext](https://developer.apple.com/documentation/mailkit/mecomposecontext)
- [MEDecodedMessageBanner](https://developer.apple.com/documentation/mailkit/medecodedmessagebanner)
- [MEEmailAddress](https://developer.apple.com/documentation/mailkit/meemailaddress)
- [MEExtensionManager](https://developer.apple.com/documentation/mailkit/meextensionmanager)
:::
