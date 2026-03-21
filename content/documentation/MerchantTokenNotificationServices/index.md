---
route: /documentation/MerchantTokenNotificationServices
source_url: https://developer.apple.com/documentation/MerchantTokenNotificationServices
source_locale: en-US
section: docc
content_type: symbol
title: Apple Pay Merchant Token Management API
original_title: Apple Pay Merchant Token Management API
source_hash: 07d0c5278dbd4ec90a71b407902a02b2e9a09f157acf4109d03b9e289f7d4cf4
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:26:22+00:00'
last_translated_at: '2026-03-13T09:18:00+00:00'
---

# Apple Pay Merchant Token Management API

Apple Pay merchant token에 대한 결제 수명주기 이벤트를 조회하고 관리합니다.

## 개요

Apple Pay Merchant Token Management API는 merchant token 이벤트 알림을 받은 뒤 merchant가 수명주기 이벤트의 세부 정보를 가져올 수 있게 해 주는 REST API입니다. 또한 이 API를 사용해 더 이상 사용하지 않는 token을 무효화하도록 Apple Pay 서버에 알릴 수도 있습니다.

merchant token은 Apple Pay로 반복 결제, 연기 결제, 자동 충전 결제를 처리할 때 신뢰할 수 있는 해법을 제공합니다. 사용자는 Wallet에서 자신의 merchant token을 관리할 수 있습니다. [Apple Pay Merchant Token Usage Information API](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation)를 사용해 사용 정보도 제공하면 token 관리 경험을 더 풍부하게 만들 수 있습니다. 이를 통해 사용자는 과거 결제를 이해하고 예정된 결제를 추적할 수 있습니다.

Apple Pay는 merchant token 관련 이벤트를 전달하기 위해 tap-and-pull 모델을 사용합니다. 이 과정에서 Apple Pay 서버는 먼저 여러분에게 이벤트를 알리고, 이후 제공된 `eventId`를 사용해 이벤트 세부 정보를 가져오도록 합니다. 이벤트 세부 정보는 7일 동안 접근할 수 있습니다. 기기와 merchant 사이의 API는 TLS(Transport Layer Security)를 요구하며, 기기는 요청을 인증하기 위해 merchant가 제공한 `authenticationToken`을 제시합니다.

또한 Apple Pay 서버를 호출해 Merchant Payment Account Number(MPAN)를 연결 해제할 수 있습니다. Apple Pay 서버와 merchant 사이의 API에 접근하려면 mutual TLS가 필요합니다.

*merchant token*은 결제 카드, merchant, 사용자 사이의 연관 관계를 나타냅니다. 고객이 앱이나 웹사이트에서 Apple Pay로 구매를 시작하면 Apple Pay가 merchant token을 발급합니다. 앱이나 웹사이트가 반복 결제 또는 자동 충전 결제에 대한 결제 요청을 만들 때, 서버의 알림 URL을 `tokenNotificationURL` 매개변수에 전달합니다. `tokenNotificationURL`에 대한 자세한 내용은 [PKAutomaticReloadPaymentRequest](https://developer.apple.com/documentation/PassKit/PKAutomaticReloadPaymentRequest), [PKRecurringPaymentRequest](https://developer.apple.com/documentation/PassKit/PKRecurringPaymentRequest), [ApplePayAutomaticReloadPaymentRequest](https://developer.apple.com/documentation/ApplePayontheWeb/ApplePayAutomaticReloadPaymentRequest), [ApplePayRecurringPaymentRequest](https://developer.apple.com/documentation/ApplePayontheWeb/ApplePayRecurringPaymentRequest), [PKDeferredPaymentRequest](https://developer.apple.com/documentation/PassKit/PKDeferredPaymentRequest), [ApplePayDeferredPaymentRequest](https://developer.apple.com/documentation/ApplePayontheWeb/ApplePayDeferredPaymentRequest)를 참고하세요.

만약 카드 만료일 변경이나 사용자/발급기관의 token 삭제처럼 token에 영향을 주는 수명주기 이벤트가 발생하면, Apple Pay는 그 `tokenNotificationURL`로 이벤트 식별자가 포함된 알림을 보냅니다. 여러분은 그 이벤트 식별자로 [Get Details of a Merchant Token Event](https://developer.apple.com/documentation/merchanttokennotificationservices/merchant-token-event-retrieval)를 호출해 이벤트 세부 정보를 가져옵니다.

:::topic-grid
## 필수 항목
- [merchant token 사용 정보 추가하기](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/adding-merchant-token-usage-information): merchant token 사용 정보 패키지를 위해 디렉터리를 만들고 파일, 이미지, 현지화 리소스를 추가합니다.
- [Apple Pay Merchant Token Usage Information API](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation): merchant token 사용 정보 패키지에 대한 세부 정보를 추가합니다.
:::

:::topic-grid
## merchant token 알림 처리
- [merchant token 알림 수신 및 처리](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/receiving-and-handling-merchant-token-notifications): Apple Pay로부터 merchant token 수명주기 업데이트를 수신하고 처리하는 엔드포인트를 구현합니다.
- [Send Merchant Token Event](https://developer.apple.com/documentation/merchanttokennotificationservices/send-merchant-token-event): Apple Pay로부터 merchant token 수명주기 업데이트를 수신하고 처리합니다.
- [Update Merchant Metadata](https://developer.apple.com/documentation/merchanttokennotificationservices/update-merchant-metadata): merchant token의 알림 URL을 업데이트합니다.
:::

:::topic-grid
## merchant token 이벤트 조회
- [merchant token 이벤트 세부 정보 가져오기](https://developer.apple.com/documentation/merchanttokennotificationservices/merchant-token-event-retrieval): 알림을 받은 뒤 merchant token 이벤트 세부 정보를 가져옵니다.
- [MerchantTokenEventResponse](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokeneventresponse): merchant token의 수명주기 이벤트 정보를 담는 응답 본문입니다.
- [MerchantTokenMetadata](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenmetadata): 카드 아트와 메타데이터를 포함한 merchant token 관련 카드 정보입니다.
- [CardArt](https://developer.apple.com/documentation/merchanttokennotificationservices/cardart): 카드를 나타내는 아트를 표시하기 위한 데이터입니다.
- [CardMetadata](https://developer.apple.com/documentation/merchanttokennotificationservices/cardmetadata): 만료일과 suffix를 포함한 카드 데이터입니다.
:::

:::topic-grid
## merchant token 사용 정보
- [merchant token 공개 키 가져오기](https://developer.apple.com/documentation/merchanttokennotificationservices/retrieve-merchant-token-public-key): merchant token 공개 키를 가져옵니다.
- [MerchantToken Usage Data Availability Notification](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttoken-usage-data-availability-notification): 사용자의 기기에서 merchant token 사용 정보를 가져올 수 있음을 Apple 서버에 알립니다.
- [MerchantTokenUsageDataAvailabilityNotificationRequest](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenusagedataavailabilitynotificationrequest): merchant token 사용 데이터 가용성 알림 요청에 대한 데이터입니다.
- [Get MerchantToken Usage Information Package](https://developer.apple.com/documentation/merchanttokennotificationservices/get-merchanttoken-usage-information-package): merchant 서버에서 merchant token 사용 정보 패키지를 가져옵니다.
- [GetMerchantTokenUsageInformationPackageResponse](https://developer.apple.com/documentation/merchanttokennotificationservices/getmerchanttokenusageinformationpackageresponse): 암호화된 merchant token 사용 정보 패키지입니다.
- [AutomaticReloadPaymentDetails](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/automaticreloadpaymentdetails): 자동 충전 결제에 대한 세부 정보입니다.
- [CurrencyAmount](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/currencyamount): 금액을 나타냅니다.
- [DeferredPaymentDetails](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/deferredpaymentdetails): 호텔 예약이나 사전 주문 같은 연기 결제의 세부 정보입니다.
- [PastPayment](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/pastpayment): 과거 결제입니다.
- [RecurringPaymentDetails](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/recurringpaymentdetails): 일반적으로 구독과 같은 반복 결제의 세부 정보입니다.
- [UpcomingPayment](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/upcomingpayment): 예정된 결제입니다.
- [UsageInformation](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/usageinformation): 과거 결제와 예정 결제 등 merchant token 사용 정보입니다.
:::

:::topic-grid
## merchant token 무효화
- [merchant token 무효화](https://developer.apple.com/documentation/merchanttokennotificationservices/unlinking-merchanttoken): merchant 식별자와 연결된 merchant token을 무효화하여 이후 거래 승인에 사용할 수 없게 합니다.
- [MerchantTokenUnlinkRequest](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenunlinkrequest): merchant token을 무효화할 때 사용하는 요청 본문입니다.
:::

:::topic-grid
## 오류 처리
- [ErrorResponse](https://developer.apple.com/documentation/merchanttokennotificationservices/errorresponse): API 요청이 실패했을 때 응답 본문에 반환되는 오류 정보입니다.
:::

:::topic-grid
## 사전
- [MerchantMetadata](https://developer.apple.com/documentation/merchanttokennotificationservices/merchantmetadata): 서버에서 업데이트된 merchant의 메타데이터입니다.
- [MerchantTokenUsageMetadata](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenusagemetadata): 최신 사용 정보를 어디서 어떻게 가져올지에 대한 메타데이터입니다.
- [RetrieveMerchantTokenPublicKeyRequest](https://developer.apple.com/documentation/merchanttokennotificationservices/retrievemerchanttokenpublickeyrequest): merchant token 공개 키 요청입니다.
- [RetrieveMerchantTokenPublicKeyResponse](https://developer.apple.com/documentation/merchanttokennotificationservices/retrievemerchanttokenpublickeyresponse): merchant token 공개 키 응답입니다.
- [UpdateMerchantMetadataRequest](https://developer.apple.com/documentation/merchanttokennotificationservices/updatemerchantmetadatarequest): merchant token의 알림 메타데이터를 업데이트합니다.
:::
