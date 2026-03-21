---
route: /documentation/CoreNFC
source_url: https://developer.apple.com/documentation/CoreNFC
source_locale: en-US
section: docc
content_type: symbol
title: Core NFC
original_title: Core NFC
source_hash: f51508165654d9c6d19e1f09065ea04763176629845425317153336daa0352eb
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:55:53+00:00'
last_translated_at: '2026-03-13T16:05:00+09:00'
---

# Core NFC

NFC 태그를 감지하고, NDEF 데이터를 포함한 메시지를 읽고, 쓰기 가능한 태그에 데이터를 저장합니다.

## 개요

앱은 태그를 읽어 사용자에게 물리적 환경과 그 안의 현실 세계 객체에 대한 더 많은 정보를 제공할 수 있습니다. Core NFC를 사용하면 NFC Data Exchange Format(NDEF)의 데이터를 포함하는 1형부터 5형까지의 Near Field Communication(NFC) 태그를 읽을 수 있습니다. 예를 들어 앱은 상점에서 발견한 제품이나 박물관에서 방문한 전시물에 대한 정보를 사용자에게 제공할 수 있습니다.

앱은 태그에 데이터를 기록할 수도 있고, ISO 7816, ISO 15693, FeliCa™, MIFARE® 태그 같은 프로토콜별 태그와 상호 작용할 수도 있습니다.

Core NFC는 앱 확장에서 사용할 수 없으며, Near Field Communication을 지원하는 기기가 필요합니다. 지원 여부를 확인하려면 reader session을 시작하기 전에 [readingAvailable](https://developer.apple.com/documentation/corenfc/nfcreadersession-swift.class/readingavailable) 클래스 프로퍼티를 확인하십시오.

:::topic-grid
## 핵심 사항
- [Building an NFC Tag-Reader App](https://developer.apple.com/documentation/corenfc/building-an-nfc-tag-reader-app): 앱에서 NDEF 메시지를 포함한 NFC 태그를 읽습니다.
- [Adding Support for Background Tag Reading](https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading): background tag reading을 사용해 앱 없이도 사용자가 NFC 태그를 스캔할 수 있게 합니다.
- [NFCReaderUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NFCReaderUsageDescription): 앱이 기기의 NFC 하드웨어 접근을 요청하는 이유를 사용자에게 설명하는 메시지입니다.
:::

:::topic-grid
## 리더 세션
- [NFCNDEFReaderSession](https://developer.apple.com/documentation/corenfc/nfcndefreadersession): NFC Data Exchange Format(NDEF) 태그를 감지하기 위한 reader session입니다.
- [NFCTagReaderSession](https://developer.apple.com/documentation/corenfc/nfctagreadersession): ISO7816, ISO15693, FeliCa, MIFARE 태그를 감지하기 위한 reader session입니다.
- [NFCPaymentTagReaderSession](https://developer.apple.com/documentation/corenfc/nfcpaymenttagreadersession): 결제 태그 사용을 지원하는 reader session입니다.
- [NFCVASReaderSession](https://developer.apple.com/documentation/corenfc/nfcvasreadersession): Value Added Service(VAS) 태그를 처리하기 위한 reader session입니다.
- [NFCReaderSession](https://developer.apple.com/documentation/corenfc/nfcreadersession-swift.class): NFC 태그를 감지하는 reader session을 나타내는 추상 기본 클래스입니다.
- [NFCReaderSessionProtocol](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol): reader session과 상호 작용하기 위한 일반 인터페이스입니다.
- [Near Field Communication Tag Reader Session Formats Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats): 앱이 읽을 수 있는 Near Field Communication 데이터 형식입니다.
:::

:::topic-grid
## 태그 유형
- [Creating NFC Tags from Your iPhone](https://developer.apple.com/documentation/corenfc/creating-nfc-tags-from-your-iphone): 태그에 데이터를 저장하고 네이티브 태그 프로토콜을 사용해 상호 작용합니다.
- [NFCISO7816Tag](https://developer.apple.com/documentation/corenfc/nfciso7816tag): ISO 7816 태그와 상호 작용하기 위한 인터페이스입니다.
- [NFCISO15693Tag](https://developer.apple.com/documentation/corenfc/nfciso15693tag): ISO 15693 태그와 상호 작용하기 위한 인터페이스입니다.
- [NFCFeliCaTag](https://developer.apple.com/documentation/corenfc/nfcfelicatag): FeliCa™ 태그와 상호 작용하기 위한 인터페이스입니다.
- [NFCMiFareTag](https://developer.apple.com/documentation/corenfc/nfcmifaretag): MIFARE® 태그와 상호 작용하기 위한 인터페이스입니다.
- [NFCNDEFTag](https://developer.apple.com/documentation/corenfc/nfcndeftag): NDEF 태그와 상호 작용하기 위한 인터페이스입니다.
- [NFCTag](https://developer.apple.com/documentation/corenfc/nfctag-swift.enum): NFC 태그 객체를 나타내는 객체입니다.
- [NFCTagCommandConfiguration](https://developer.apple.com/documentation/corenfc/nfctagcommandconfiguration): NFC 태그 명령의 구성을 정의할 때 사용하는 매개변수 집합입니다.
:::

:::topic-grid
## NDEF 메시지와 payload
- [NFCNDEFMessage](https://developer.apple.com/documentation/corenfc/nfcndefmessage): payload record 배열로 구성된 NFC NDEF 메시지입니다.
- [NFCNDEFPayload](https://developer.apple.com/documentation/corenfc/nfcndefpayload): NFC NDEF 메시지의 payload record입니다.
:::

:::topic-grid
## 카드 세션
- [CardSession](https://developer.apple.com/documentation/corenfc/cardsession): ISO 7816 카드 에뮬레이션 세션입니다.
- [NFCPresentmentIntentAssertion](https://developer.apple.com/documentation/corenfc/nfcpresentmentintentassertion): 앱이 기기의 비접촉식 기능을 독점적으로 사용하려는 의도를 알리는 객체입니다.
:::

:::topic-grid
## NFC window scene
- [NFCWindowSceneDelegate](https://developer.apple.com/documentation/corenfc/nfcwindowscenedelegate): NFC 관련 이벤트를 앱의 사용자 인터페이스에 알리는 프로토콜입니다.
- [NFCWindowSceneEvent](https://developer.apple.com/documentation/corenfc/nfcwindowsceneevent): 앱이 사용자 인터페이스를 업데이트할 때 사용하는 NFC 관련 이벤트입니다.
:::

:::topic-grid
## 오류
- [NFCReaderError.Code](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct/code): reader session과 태그 오류 코드입니다.
- [NFCReaderError](https://developer.apple.com/documentation/corenfc/nfcreadererror-swift.struct): reader session 또는 태그 문제를 나타내는 오류 타입입니다.
- [NFCErrorDomain](https://developer.apple.com/documentation/corenfc/nfcerrordomain): Core NFC API 관련 오류의 도메인입니다.
- [NFCTagResponseUnexpectedLengthErrorKey](https://developer.apple.com/documentation/corenfc/nfctagresponseunexpectedlengtherrorkey): 수신한 응답 패킷 길이가 잘못되었음을 나타내는 user-information dictionary 키입니다.
:::

:::topic-grid
## 레퍼런스
- [CoreNFC Enumerations](https://developer.apple.com/documentation/corenfc/corenfc-enumerations)
:::

:::topic-grid
## 클래스
- [NFCISO15693CustomCommandConfiguration](https://developer.apple.com/documentation/corenfc/nfciso15693customcommandconfiguration)
- [NFCISO15693ReadMultipleBlocksConfiguration](https://developer.apple.com/documentation/corenfc/nfciso15693readmultipleblocksconfiguration)
:::

:::topic-grid
## 구조체
- [NFCFeliCaPollingResponse](https://developer.apple.com/documentation/corenfc/nfcfelicapollingresponse)
- [NFCFeliCaRequestSpecificationVersionResponse](https://developer.apple.com/documentation/corenfc/nfcfelicarequestspecificationversionresponse)
- [NFCFeliCaRequsetServiceV2Response](https://developer.apple.com/documentation/corenfc/nfcfelicarequsetservicev2response)
- [NFCFeliCaStatusFlag](https://developer.apple.com/documentation/corenfc/nfcfelicastatusflag)
- [NFCISO15693MultipleBlockSecurityStatus](https://developer.apple.com/documentation/corenfc/nfciso15693multipleblocksecuritystatus)
- [NFCISO15693SystemInfo](https://developer.apple.com/documentation/corenfc/nfciso15693systeminfo)
:::
