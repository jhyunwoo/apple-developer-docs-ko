---
route: /documentation/ProximityReader
source_url: https://developer.apple.com/documentation/ProximityReader
source_locale: en-US
section: docc
content_type: symbol
title: ProximityReader
original_title: ProximityReader
source_hash: c56e9884781e25eb6b05184923d58b3f0784a7fc745b3a6b5096467d8408edef
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:51:13+00:00'
last_translated_at: '2026-03-13T18:40:00+09:00'
---

# ProximityReader

iPhone을 사용해 비접촉식 실물 카드와 디지털 지갑 카드를 읽습니다.

## 개요

ProximityReader 프레임워크는 *Tap to Pay on iPhone*을 지원하며, 이를 통해 추가 하드웨어 없이도 사용자의 iPhone이 판매 시점(point-of-sale) 기기로 동작할 수 있습니다. ProximityReader는 Wallet 앱의 로열티 카드 읽기도 지원합니다. 앱에서 이 프레임워크를 사용해 결제 프로세스를 시작하십시오.

이 프레임워크를 사용하려면 Level 3 인증을 받은 참여 결제 서비스 제공업체와 협력해야 합니다. 결제 제공업체에 연락하여 결제 처리 워크플로를 설정하십시오. 준비가 되면 Apple에 연락하여 Tap to Pay on iPhone 지원을 앱에 통합하는 데 필요한 entitlement를 요청하십시오. entitlement 요청에 대한 정보는 [Setting up Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone)을 참고하십시오.

:::note 참고
Tap to Pay on iPhone은 PCI CPoC Standard를 따르며, 이 표준은 Level 2 인증 결제 커널과 비접촉식 결제 카드를 읽기 위한 사용자 인터페이스를 사용합니다.
:::

:::topic-grid
## 결제 카드 리더
- [Setting up Tap to Pay on iPhone](https://developer.apple.com/documentation/proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone): Tap to Pay on iPhone 지원에 필요한 entitlement를 요청하고 구성합니다.
- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-pay-on-iPhone-to-your-app): 앱이 비접촉식 결제 카드를 읽도록 Tap to Pay on iPhone을 사용하도록 구성합니다.
- [PaymentCardReader](https://developer.apple.com/documentation/proximityreader/paymentcardreader): 현재 기기에서 Tap to Pay on iPhone을 구성하는 데 사용하는 객체입니다.
- [PaymentCardReaderSession](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession): 비접촉식 결제 카드 또는 로열티 카드를 읽기 시작할 때 사용하는 객체입니다.
:::

:::topic-grid
## 결제 요청
- [PaymentCardTransactionRequest](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest): 구매 금액과 통화 정보를 포함하는 비접촉식 구매 또는 환불 요청입니다.
- [PaymentCardVerificationRequest](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest): 비접촉식 결제 카드의 세부 정보를 확인하기 위한 요청입니다.
- [PaymentCardReadResult](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult): 결제 카드 읽기 작업의 결과입니다.
:::

:::topic-grid
## Store and Forward 모드
- [StoreAndForwardBatch](https://developer.apple.com/documentation/proximityreader/storeandforwardbatch): 결제 서비스 제공업체에 보내 처리할 데이터를 저장하는 구조체입니다.
- [StoreAndForwardBatchDeletionToken](https://developer.apple.com/documentation/proximityreader/storeandforwardbatchdeletiontoken): Store and Forward 배치를 삭제할 때 사용하는 보안 토큰입니다.
- [StoreAndForwardPaymentCardReaderSession](https://developer.apple.com/documentation/proximityreader/storeandforwardpaymentcardreadersession): Store and Forward 모드에서 비접촉식 결제 카드 또는 로열티 카드를 읽기 시작할 때 사용하는 객체입니다.
- [StoreAndForwardStatus](https://developer.apple.com/documentation/proximityreader/storeandforwardstatus): Store and Forward 세션 상태를 설명하는 구조체입니다.
- [PaymentCardReaderStore](https://developer.apple.com/documentation/proximityreader/paymentcardreaderstore): 모든 Store and Forward 읽기 결과가 들어 있는 저장소를 관리하는 구조체입니다.
:::

:::topic-grid
## 로열티 카드 요청
- [Accepting loyalty passes from Wallet](https://developer.apple.com/documentation/proximityreader/accepting-loyalty-passes-from-wallet): 앱이 Tap to Pay on iPhone을 사용해 로열티 패스를 읽고 발급할 수 있도록 필요한 구성 요소를 설정합니다.
- [VASRequest](https://developer.apple.com/documentation/proximityreader/vasrequest): 비접촉식 로열티 카드를 읽고 사용자의 로열티 프로그램 식별자를 가져오기 위한 요청입니다.
- [VASReadResult](https://developer.apple.com/documentation/proximityreader/vasreadresult): 로열티 카드 정보를 읽는 요청의 결과입니다.
:::

:::topic-grid
## 가맹점 검색
- [ProximityReaderDiscovery](https://developer.apple.com/documentation/proximityreader/proximityreaderdiscovery): Tap to Pay on iPhone 사용 방법 정보를 포함한 UI를 표시하는 객체입니다.
:::

:::topic-grid
## 모바일 문서 리더
- [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iPhone-app): 모바일 문서를 읽기 위한 ID Verifier 지원을 앱에서 구성하고 테스트합니다.
- [Generating reader tokens for the Verifier API](https://developer.apple.com/documentation/proximityreader/generating-reader-tokens-for-the-verifier-api): 모바일 문서 읽기를 준비하기 위해 서버가 reader token을 생성하도록 구성합니다.
- [Checking IDs with the Verifier API](https://developer.apple.com/documentation/proximityreader/checking-ids-with-the-verifier-api): 추가 하드웨어 없이 모바일 운전면허증 정보를 읽고 검증합니다.
- [MobileDocumentReader](https://developer.apple.com/documentation/proximityreader/mobiledocumentreader): 현재 기기에서 모바일 문서 읽기를 구성하는 객체입니다.
- [MobileDocumentReaderSession](https://developer.apple.com/documentation/proximityreader/mobiledocumentreadersession): 모바일 문서를 읽기 시작할 때 사용하는 객체입니다.
:::

:::topic-grid
## 모바일 문서 요청
- [MobileDriversLicenseDisplayRequest](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedisplayrequest): 소지자로부터 요소를 가져와 화면에 표시하여 육안으로 검사할 수 있게 하는 모바일 운전면허증 요청입니다.
- [MobileDriversLicenseDataRequest](https://developer.apple.com/documentation/proximityreader/mobiledriverslicensedatarequest): 소지자로부터 요소를 가져와 검증된 문서 요소를 반환하는 모바일 운전면허증 요청입니다.
- [MobileDriversLicenseRawDataRequest](https://developer.apple.com/documentation/proximityreader/mobiledriverslicenserawdatarequest): 소지자로부터 요소를 가져와 처리용 원시 응답 데이터를 반환하는 모바일 운전면허증 요청입니다.
- [MobileNationalIDCardDisplayRequest](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddisplayrequest): 소지자로부터 요소를 가져와 화면에 표시하여 육안으로 검사할 수 있게 하는 모바일 국가 신분증 요청입니다.
- [MobileNationalIDCardDataRequest](https://developer.apple.com/documentation/proximityreader/mobilenationalidcarddatarequest): 소지자로부터 요소를 가져와 검증된 문서 요소를 반환하는 모바일 국가 신분증 요청입니다.
- [MobileNationalIDCardRawDataRequest](https://developer.apple.com/documentation/proximityreader/mobilenationalidcardrawdatarequest): 소지자로부터 요소를 가져와 처리용 원시 응답 데이터를 반환하는 모바일 국가 신분증 요청입니다.
- [MobileDocumentDisplayRequest](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest): 소지자로부터 요소를 가져와 화면에 표시하여 육안으로 검사할 수 있게 하는 모바일 문서 요청입니다.
- [MobileDocumentRequest](https://developer.apple.com/documentation/proximityreader/mobiledocumentrequest): 모바일 문서 요청을 나타내는 타입입니다.
- [MobileDocumentDataRequest](https://developer.apple.com/documentation/proximityreader/mobiledocumentdatarequest): 모바일 문서 데이터 요청을 나타내는 타입입니다.
- [MobileDocumentRawDataRequest](https://developer.apple.com/documentation/proximityreader/mobiledocumentrawdatarequest): 모바일 문서 원시 데이터 요청을 나타내는 타입입니다.
- [MobilePhotoIDDataRequest](https://developer.apple.com/documentation/proximityreader/mobilephotoiddatarequest): 소지자로부터 요소를 가져와 검증된 문서 요소를 반환하는 사진 신분증 요청입니다.
- [MobilePhotoIDRawDataRequest](https://developer.apple.com/documentation/proximityreader/mobilephotoidrawdatarequest): 소지자로부터 요소를 가져와 처리용 원시 응답 데이터를 반환하는 사진 신분증 요청입니다.
- [MobileDocumentAnyOfDataRequest](https://developer.apple.com/documentation/proximityreader/mobiledocumentanyofdatarequest): 요청 그룹 중 하나의 모바일 문서에 대한 데이터 요청을 설명하는 타입입니다.
- [MobileDocumentAnyOfRawDataRequest](https://developer.apple.com/documentation/proximityreader/mobiledocumentanyofrawdatarequest): 요청 그룹 중 하나의 모바일 문서에 대한 원시 데이터 요청을 설명하는 타입입니다.
:::

:::topic-grid
## 오류
- [PaymentCardReaderError](https://developer.apple.com/documentation/proximityreader/paymentcardreadererror): 리더 구성 문제를 나타내는 오류 타입입니다.
- [MobileDocumentReaderError](https://developer.apple.com/documentation/proximityreader/mobiledocumentreadererror): 모바일 문서 리더 세션 준비 및 문서 요청 수행 중 문제를 나타내는 오류 타입입니다.
:::
