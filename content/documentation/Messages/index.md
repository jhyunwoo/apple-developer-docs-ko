---
route: /documentation/Messages
source_url: https://developer.apple.com/documentation/Messages
source_locale: en-US
section: docc
content_type: symbol
title: Messages
original_title: Messages
source_hash: 8b26395908bebe0c8a3b19a5d34cfed61b5635aa1e1ecd47be3af3d2ff36e764
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:20:23+00:00'
last_translated_at: '2026-03-13T22:45:00+09:00'
---

# Messages

사용자가 텍스트, 스티커, 미디어 파일, 상호작용 메시지를 보낼 수 있게 해 주는 app extension을 만듭니다.

## 개요

Messages 프레임워크를 사용하면 sticker pack과 iMessage 앱을 만들 수 있습니다. sticker pack과 iMessage 앱은 독립 실행형 앱으로 만들 수도 있고, iOS 앱 안의 app extension으로 만들 수도 있습니다. app extension 생성과 활용에 대한 자세한 내용은 [App extensions](https://developer.apple.com/app-extensions/)를 참고하십시오.

iMessage 앱과 스티커는 사람들이 Messages 대화의 맥락 안에서 상호 작용하고 소통하는 데 도움을 줍니다. 디자인 지침은 [Human Interface Guidelines > iMessage apps and stickers](https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers)를 참고하십시오.

### iMessage 앱

iMessage 앱은 Messages 앱과 상호 작용하기 위해 프레임워크 전체를 활용합니다.

:::note 참고
충돌을 피하려면 iOS 10 이상을 기준으로 링크되는 iMessage 앱은 `Info.plist` 파일에 접근하려는 기기 기능에 대한 usage description 키를 포함해야 합니다. 구체적으로 기기 카메라에 접근하려면 [NSCameraUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription)을 포함해야 하고, 기기의 microphone에 접근하려면 [NSMicrophoneUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription)을 포함해야 합니다.
:::

iMessage 앱은 다음과 같은 용도로 사용합니다.

- Messages 앱 안에 사용자 정의 사용자 인터페이스를 표시합니다. [MSMessagesAppViewController](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller)를 참고하십시오.
- 사용자 정의 또는 동적 sticker browser를 생성합니다. [MSStickerBrowserViewController](https://developer.apple.com/documentation/messages/msstickerbrowserviewcontroller)를 참고하십시오.
- 텍스트, 스티커, 미디어 파일을 Messages 앱의 입력 필드에 삽입합니다. [MSConversation](https://developer.apple.com/documentation/messages/msconversation)을 참고하십시오.
- 앱 전용 데이터를 담는 상호작용 메시지를 생성합니다. [MSMessage](https://developer.apple.com/documentation/messages/msmessage)를 참고하십시오.
- 상호작용 메시지를 업데이트합니다. 예를 들어 게임이나 협업 앱을 만들 때 사용할 수 있습니다. [MSSession](https://developer.apple.com/documentation/messages/mssession)을 참고하십시오.

App Store에 iMessage 앱을 제출하는 방법에 대한 자세한 내용은 [Preparing Your iMessage App for Submission](https://developer.apple.com/app-store/imessage-app-submissions/)을 참고하십시오.

iOS 17에서 Messages는 세로 pan gesture를 사용해 iMessage 앱 크기를 상호작용적으로 조절할 수 있습니다. Messages는 resize gesture와 사용자 정의 gesture 사이의 충돌을 처리합니다. 앱이 [touchesBegan(_:with:)](https://developer.apple.com/documentation/UIKit/UIGestureRecognizer/touchesBegan(_:with:)), [touchesMoved(_:with:)](https://developer.apple.com/documentation/UIKit/UIGestureRecognizer/touchesMoved(_:with:)), [touchesEnded(_:with:)](https://developer.apple.com/documentation/UIKit/UIGestureRecognizer/touchesEnded(_:with:)) 같은 수동 touch 처리를 사용한다면 다음 둘 중 하나를 수행할 수 있습니다.

- 수동 touch 처리 코드를 gesture recognizer를 사용하도록 변경합니다.
- [UIView](https://developer.apple.com/documentation/UIKit/UIView)를 사용해 [gestureRecognizerShouldBegin(_:)](https://developer.apple.com/documentation/UIKit/UIGestureRecognizerDelegate/gestureRecognizerShouldBegin(_:))를 override하고, iMessage 앱이 해당 gesture를 소유하지 않을 때 `NO`를 반환합니다.

### 기본 메시징 앱 되기

iOS 및 iPadOS 18.2 이상에서는 사용자가 Messages 앱 대신 다른 앱을 선택해 즉시 메시지를 보낼 수 있습니다. 앱을 기본 메시지 앱으로 만들고 싶다면 [Preparing your app to be the default messaging app](https://developer.apple.com/documentation/messages/preparing-your-app-to-be-the-default-messaging-app)을 참고하십시오.

:::topic-grid
## 기본 메시징 앱
- [Preparing your app to be the default messaging app](https://developer.apple.com/documentation/messages/preparing-your-app-to-be-the-default-messaging-app): 사용자가 자신의 기기에서 기본 앱으로 설정할 수 있도록 메시징 앱을 구성합니다.
:::

:::topic-grid
## 사용자 정의 스티커 팩
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](https://developer.apple.com/documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime): media context에서 Sticker pack 또는 iMessage 앱을 사용할 수 있게 합니다.
- [Adding your sticker packs to Messages](https://developer.apple.com/documentation/messages/adding-your-sticker-packs-to-messages): Stickers asset catalog에 sticker pack을 드래그 앤 드롭하여 사용자가 Messages에서 스티커를 사용할 수 있게 합니다.
- [MSStickerBrowserViewController](https://developer.apple.com/documentation/messages/msstickerbrowserviewcontroller): 표준 sticker browser에 동적 콘텐츠를 제공하는 view controller입니다.
- [MSStickerBrowserView](https://developer.apple.com/documentation/messages/msstickerbrowserview): 동적으로 생성된 스티커 목록을 표시하는 browser view입니다.
- [MSStickerView](https://developer.apple.com/documentation/messages/msstickerview): sticker를 표시하기 위한 view입니다.
- [MSStickerSize](https://developer.apple.com/documentation/messages/msstickersize): browser view 안 스티커의 크기입니다.
:::

:::topic-grid
## 사용자 정의 iMessage 앱 인터페이스
- [IceCreamBuilder: Building an iMessage Extension](https://developer.apple.com/documentation/messages/icecreambuilder-building-an-imessage-extension): 사용자가 아이스크림 선데이 스티커 디자인을 함께 작업할 수 있게 합니다.
- [Creating a Sticker App with a Custom Layout](https://developer.apple.com/documentation/messages/creating-a-sticker-app-with-a-custom-layout): Messages sticker 앱 템플릿을 확장해 사용자 정의 사용자 인터페이스를 가진 앱을 만듭니다.
- [MSMessagesAppViewController](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller): iMessage 앱의 주 view controller입니다.
- [MSMessagesAppTranscriptPresentation](https://developer.apple.com/documentation/messages/msmessagesapptranscriptpresentation): Messages 앱 transcript 안에 실시간 메시지를 표시하도록 지원하는 프로토콜입니다.
- [MSMessagesAppPresentationStyle](https://developer.apple.com/documentation/messages/msmessagesapppresentationstyle): iMessage 앱의 외형을 설명하는 표시 스타일입니다.
:::

:::topic-grid
## 메시지 콘텐츠
- [MSConversation](https://developer.apple.com/documentation/messages/msconversation): Messages 앱 안의 대화를 나타내는 객체입니다.
- [MSSticker](https://developer.apple.com/documentation/messages/mssticker): 새 메시지로 보낼 수도 있고 Messages 앱 transcript의 기존 balloon에 첨부할 수도 있는 sticker입니다.
:::

:::topic-grid
## 상호작용 메시지
- [MSMessage](https://developer.apple.com/documentation/messages/msmessage): 사용자 정의 메시지 객체입니다.
- [MSSession](https://developer.apple.com/documentation/messages/mssession): 메시지를 생성하고 업데이트하는 데 사용하는 session 객체입니다.
- [MSMessageLayout](https://developer.apple.com/documentation/messages/msmessagelayout): 대화 transcript 안 객체의 외형을 정의하는 추상 기본 클래스입니다.
- [MSMessageTemplateLayout](https://developer.apple.com/documentation/messages/msmessagetemplatelayout): 사용자 정의 메시지를 위한 template 기반 레이아웃입니다.
- [MSMessageLiveLayout](https://developer.apple.com/documentation/messages/msmessagelivelayout): transcript 안에 사용자 정의 상호작용 view를 제공하는 레이아웃입니다.
:::

:::topic-grid
## 중요 메시지
- [Sending SMS messages from an app](https://developer.apple.com/documentation/messages/critical-messaging-api): Critical Messaging API를 사용해 앱 내부에서 중요 메시지를 전송합니다.
- [MSCriticalSMSMessenger](https://developer.apple.com/documentation/messages/mscriticalsmsmessenger): Critical Messaging API의 사용자 인터페이스입니다.
- [MSRecipient](https://developer.apple.com/documentation/messages/msrecipient): 중요 메시지 수신자를 설명하는 구조체입니다.
- [MSCriticalMessage](https://developer.apple.com/documentation/messages/mscriticalmessage): 중요한 통신을 위한 메시지입니다.
- [MSCriticalMessagingAuthorizationStatus](https://developer.apple.com/documentation/messages/mscriticalmessagingauthorizationstatus): Critical Messaging API의 권한 상태를 설명하는 값입니다.
:::

:::topic-grid
## 오류
- [MSStickersErrorDomain](https://developer.apple.com/documentation/messages/msstickerserrordomain): sticker용 오류 도메인입니다.
- [MSMessagesErrorDomain](https://developer.apple.com/documentation/messages/msmessageserrordomain): iMessage 앱용 오류 도메인입니다.
- [MSMessageErrorCode](https://developer.apple.com/documentation/messages/msmessageerrorcode): Messages 프레임워크가 생성하는 오류 코드입니다.
- [MSCriticalMessagingError](https://developer.apple.com/documentation/messages/mscriticalmessagingerror): Critical Messaging API가 반환하는 오류를 설명하는 값입니다.
:::
