---
route: /documentation/ApplePayWebMerchantRegistrationAPI
source_url: https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI
source_locale: en-US
section: docc
content_type: symbol
title: Apple Pay Web Merchant Registration API
original_title: Apple Pay Web Merchant Registration API
source_hash: 5f0042ce1d5e16ea4d48da1716763e2343d7ec2a39100bb3b46679b7d9681015
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:55:53+00:00'
last_translated_at: '2026-03-13T16:05:00+09:00'
---

# Apple Pay Web Merchant Registration API

웹 플랫폼을 통해 판매자 등록을 관리합니다.

## 개요

Apple Pay Web Merchant Registration API는 결제 서비스 제공업체나 전자상거래 플랫폼 같은 플랫폼 통합자가 웹에서 Apple Pay를 제공하려는 웹 판매자를 등록할 수 있게 해 주는 REST API입니다.

플랫폼 통합자는 [Register Merchant](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/register-merchant)를 호출할 때 판매자를 대신해 Apple Pay 구성을 관리합니다. 판매자가 Apple Developer 계정을 설정하거나 자체 키와 인증서를 구성할 필요는 없습니다. 플랫폼 통합자가 전체 판매자 포트폴리오를 위한 공유 키 및 인증서 집합을 설정합니다. 판매자를 자체 웹사이트 도메인으로 등록할 수도 있고, 플랫폼이 호스팅하는 웹 페이지로 등록할 수도 있습니다.

:::note Note
이 API는 production 환경과 sandbox 환경에서 사용할 수 있습니다. sandbox 환경에서 이 API를 사용하려면 `apple-pay-gateway-cert.apple.com` 도메인을 사용해 엔드포인트를 호출하십시오. 예를 들어 [Register Merchant](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/register-merchant)의 sandbox 엔드포인트는 `POST https://apple-pay-gateway-cert.apple.com/paymentservices/registerMerchant`입니다.
:::

### 사용을 위한 API 요구 사항

Apple Pay Web Merchant Registration API를 사용하려면 다음 요구 사항을 충족해야 합니다.

- 조직이 Apple Developer Program에 등록되어 있어야 합니다. 등록에 대한 자세한 내용은 [What You Need To Enroll](https://developer.apple.com/programs/enroll/)의 “Enrolling as an Organization” 섹션을 참고하십시오.
- API 사용 권한을 신청해야 합니다. 신청에 대한 자세한 내용은 [Registering with Apple Pay and Applying to Use the API](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/registering-with-apple-pay-and-applying-to-use-the-api)를 참고하십시오.
- 서버는 TLS(Transport Layer Security) 1.2 이상과 지원되는 암호 스위트 중 하나를 사용하는 상호 인증 방식으로 API를 호출해야 합니다. 지원되는 암호 스위트 목록은 [Setting Up Your Server](https://developer.apple.com/documentation/ApplePayontheWeb/setting-up-your-server)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [Registering with Apple Pay and Applying to Use the API](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/registering-with-apple-pay-and-applying-to-use-the-api): 상거래 파트너를 Apple Pay에 등록하고 웹 서비스를 사용할 수 있도록 신청합니다.
:::

:::topic-grid
## 웹 판매자 등록
- [Preparing merchant domains for verification](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/preparing-merchant-domains-for-verification): 등록을 요청하기 전에 각 도메인에 도메인 검증 파일을 호스팅합니다.
- [Register Merchant](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/register-merchant): 판매자와 그에 대응하는 정규화된 도메인 집합을 등록합니다.
- [RegisterMerchantRequest](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/registermerchantrequest): 판매자를 등록할 때 사용하는 요청 본문입니다.
:::

:::topic-grid
## 웹 판매자 등록 해제
- [Unregister Merchant](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/unregister-merchant): 이전에 등록된 판매자와 연결된 하나 이상의 도메인 등록을 해제합니다.
- [UnregisterMerchantRequest](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/unregistermerchantrequest): 하나 이상의 판매자 도메인 등록을 해제할 때 사용하는 요청 본문입니다.
:::

:::topic-grid
## 웹 판매자 세부 정보
- [Get Merchant Details](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/get-merchant): 판매자의 내부 merchant identifier를 사용해 등록된 판매자의 현재 상태 정보를 가져옵니다.
- [MerchantDetails](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/merchantdetails): 단일 등록 판매자에 대한 상세 정보입니다.
:::

:::topic-grid
## 문서
- [Applying to use the registration API and configuring IDs](https://developer.apple.com/documentation/applepaywebmerchantregistrationapi/applying-to-use-the-registration-api-and-configuring-ids): Registration API 접근 권한을 요청하고 웹 서비스를 사용할 ID를 등록합니다.
:::
