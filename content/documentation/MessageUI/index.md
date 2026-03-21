---
route: /documentation/MessageUI
source_url: https://developer.apple.com/documentation/MessageUI
source_locale: en-US
section: docc
content_type: symbol
title: Message UI
original_title: Message UI
source_hash: d0e2762836d9e2584aa7f8509794866e081116b49ed36ee0eb5bbb1d36e84a8d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:16:25+00:00'
last_translated_at: '2026-03-13T08:28:00+00:00'
---

# Message UI

이메일과 문자 메시지를 작성하는 사용자 인터페이스를 만들어, 사용자가 앱을 떠나지 않고도 메시지를 편집하고 전송할 수 있게 합니다.

## 개요

Message UI 프레임워크는 이메일과 SMS(Short Messaging Service) 문자 메시지를 위한 표준 작성 인터페이스를 표시하는 특수한 뷰 컨트롤러를 제공합니다. 이 인터페이스를 사용하면 사용자가 앱을 벗어나지 않아도 메시지 전송 기능을 앱에 추가할 수 있습니다.

작성 인터페이스를 표시하려면 앱에서 해당 뷰 컨트롤러를 모달 방식으로 표시하세요. 표시된 뒤에는 사용자가 전송 전에 내용을 수정하거나 메시지 전송을 취소할 수 있습니다. 이후 사용자 지정 delegate 객체가 사용자의 동작에 따라 뷰 컨트롤러를 닫는 처리를 담당합니다. 뷰 컨트롤러 표시와 해제 방법에 대한 자세한 내용은 [View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457)를 참고하세요.

:::important Important
이 프레임워크의 뷰 컨트롤러는 현재 iOS 기기에서 특정 메시지 유형을 전송할 수 있는지 판단하는 메서드를 제공합니다. 메시지를 보낼 수 없다면 해당 뷰 컨트롤러를 표시하지 마세요.
:::

:::topic-grid
## 이메일 작성 인터페이스
- [MFMailComposeViewController](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller): 사용자가 이메일 메시지를 관리하고, 편집하고, 전송할 수 있는 표준 뷰 컨트롤러입니다.
:::

:::topic-grid
## 메시지 작성 인터페이스
- [MFMessageComposeViewController](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller): 사용자가 SMS 또는 MMS 메시지를 작성하고 전송할 수 있는 표준 뷰 컨트롤러입니다.
:::

:::topic-grid
## 열거형
- [MFMailComposeControllerDeferredAction](https://developer.apple.com/documentation/messageui/mfmailcomposecontrollerdeferredaction)
:::
