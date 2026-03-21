---
route: /documentation/ApplePayontheWeb
source_url: https://developer.apple.com/documentation/ApplePayontheWeb
source_locale: en-US
section: docc
content_type: symbol
title: Apple Pay on the Web
original_title: Apple Pay on the Web
source_hash: f1eab28ee890577baa374841de36e03a59cd918e65b5236108fd590b200e5515
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:14:19+00:00'
last_translated_at: '2026-03-13T23:14:51+09:00'
---

# Apple Pay on the Web

JavaScript 기반 API로 웹사이트에서 Apple Pay를 지원합니다.

## 개요

Safari는 웹사이트에서 고객의 Apple Pay 결제를 받을 수 있도록 해 주는 두 가지 JavaScript API를 지원합니다.

- [Payment Request API](https://developer.apple.com/documentation/ApplePayontheWeb/payment-request-api): [W3C candidate API](https://www.w3.org/TR/payment-request/)
- [Apple Pay JS API](https://developer.apple.com/documentation/ApplePayontheWeb/apple-pay-js-api): 앱 안의 Apple Pay를 위한 [PassKit (Apple Pay and Wallet)](https://developer.apple.com/documentation/PassKit) 프레임워크에 대응하는 API

:::tip Tip
데모 페이지에서 Apple Pay 거래를 직접 시험해 볼 수 있습니다. [Apple Pay on the Web Interactive Demo](https://applepaydemo.apple.com)를 참고하십시오.
:::

Apple Pay는 결제 정보를 안전하게 저장하도록 설계된 업계 표준 인증 칩인 Secure Element를 탑재한 모든 iOS 기기에서 사용할 수 있습니다. macOS에서는 결제를 승인하려면 Touch ID가 있는 Mac이 필요하거나, Apple Pay를 지원하는 iPhone 또는 Apple Watch가 필요합니다.

### 지역 및 플랫폼별 Apple Pay 사용 가능 여부

Apple Pay는 [지원 지역](https://www.apple.com/ios/feature-availability/#apple-pay)에서 사용할 수 있습니다.

Apple Pay API는 Safari에서 다음 플랫폼을 지원합니다.

|  | **전 세계(중국 제외)** | **중국** |
| --- | --- | --- |
| **Apple Pay JS** | iOS 10 이상, macOS 10.12 이상 | iOS 11.2 이상, macOS에서는 사용할 수 없음 |
| **Payment Request API** | iOS 11.3 이상, macOS 10.12.6 이상에서 Safari 11.1 이상 | iOS 11.3 이상, macOS에서는 사용할 수 없음 |

iOS에서는 Safari와 [SFSafariViewController](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) 객체가 Apple Pay를 지원합니다.

지원되는 기기에서만 Apple Pay 버튼을 표시하도록 구현하려면 [Checking for Apple Pay availability](https://developer.apple.com/documentation/ApplePayontheWeb/checking-for-apple-pay-availability)를 참고하십시오.

:::note Note
일부 지역의 규정은 구현에서 특정 구성을 요구할 수 있습니다. 자세한 내용은 [Complying with regional regulations](https://developer.apple.com/documentation/PassKit/complying-with-regional-regulations)를 참고하십시오.
:::

### Apple Pay 요구 사항

웹사이트에서 Apple Pay를 사용하려면 다음 요구 사항을 충족해야 합니다.

- Apple Pay 가이드라인을 준수하는 웹사이트
  자세한 내용은 [Acceptable Use Guidelines for Apple Pay on the Web](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/)를 참고하십시오.
- Apple Developer 계정과 등록 절차 완료
  자세한 내용은 [Configuring Your Environment](https://developer.apple.com/documentation/ApplePayontheWeb/configuring-your-environment)를 참고하십시오.
- Apple Pay를 포함하는 모든 페이지를 HTTPS로 제공
  자세한 내용은 [Setting Up Your Server](https://developer.apple.com/documentation/ApplePayontheWeb/setting-up-your-server)를 참고하십시오.

디자인 가이드는 [Human Interface Guidelines > Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/introduction/)를 참고하십시오.

:::topic-grid
## 핵심
- [Loading the latest version of the Apple Pay JS SDK](https://developer.apple.com/documentation/applepayontheweb/loading-the-latest-version-of-apple-pay-js): 자동 업데이트되는 최신 Apple Pay JS SDK 버전 또는 원하는 버전에 연결합니다.
:::

:::topic-grid
## Apple Pay 설정
- [Setting Up Your Server](https://developer.apple.com/documentation/applepayontheweb/setting-up-your-server): Apple Pay와 안전하게 통신하도록 서버를 설정합니다.
- [Configuring Your Environment](https://developer.apple.com/documentation/applepayontheweb/configuring-your-environment): Apple Pay merchant ID와 인증서를 만들고 도메인을 검증합니다.
- [Maintaining Your Environment](https://developer.apple.com/documentation/applepayontheweb/maintaining-your-environment): 인증서와 도메인 검증을 최신 상태로 유지해 Apple Pay 서비스 중단을 방지합니다.
:::

:::topic-grid
## Apple Pay Later 시각 merchandising 위젯
- [Adding an Apple Pay Later visual merchandising widget](https://developer.apple.com/documentation/applepayontheweb/adding-an-apple-pay-later-visual-merchandising-widget): 웹사이트에 맞게 Apple Pay Later 위젯을 구성하고 스타일을 지정합니다.
:::

:::topic-grid
## Apple 주문 추적 버튼
- [Adding a Track with Apple Wallet button](https://developer.apple.com/documentation/applepayontheweb/adding-a-track-with-apple-wallet-button): 웹사이트에 맞게 Apple Wallet 버튼을 구성하고 스타일을 지정합니다.
:::

:::topic-grid
## Apple Pay 버튼
- [Displaying Apple Pay Buttons Using JavaScript](https://developer.apple.com/documentation/applepayontheweb/displaying-apple-pay-buttons-using-javascript): JavaScript Apple Pay 버튼을 로드하고 구성합니다.
- [ApplePayButton](https://developer.apple.com/documentation/applepayontheweb/applepaybutton): Apple Pay 결제를 시작하거나 사용자가 카드를 설정하도록 유도하는 버튼을 표시하는 객체입니다.
- [Displaying Apple Pay Buttons Using CSS](https://developer.apple.com/documentation/applepayontheweb/displaying-apple-pay-buttons-using-css): Safari에서 CSS 템플릿을 사용해 Apple Pay 버튼을 표시합니다.
:::

:::topic-grid
## Apple Pay JavaScript API
- [Choosing an API for Implementing Apple Pay on Your Website](https://developer.apple.com/documentation/applepayontheweb/choosing-an-api-for-implementing-apple-pay-on-your-website): Apple Pay JS와 Payment Request API를 비교해 웹사이트에 적합한 구현을 선택합니다.
- [Apple Pay on the Web version history](https://developer.apple.com/documentation/applepayontheweb/apple-pay-on-the-web-version-history): Apple Pay on the Web 각 버전의 기능을 살펴봅니다.
- [Apple Pay JS API](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-api): Apple의 JavaScript API로 웹에서 Apple Pay를 구현합니다.
- [Payment Request API](https://developer.apple.com/documentation/applepayontheweb/payment-request-api): Payment Request API를 사용해 웹사이트에서 Apple Pay 결제를 처리합니다.
:::

:::topic-grid
## 지원 결제 네트워크
- [Supporting payment networks](https://developer.apple.com/documentation/applepayontheweb/supported-networks): Apple Pay on the Web가 지원하는 결제 네트워크를 확인합니다.
:::

:::topic-grid
## 오류
- [ApplePayError](https://developer.apple.com/documentation/applepayontheweb/applepayerror): Apple Pay 시트의 주소 또는 연락처 정보 문제를 나타내기 위해 생성하는 사용자 정의 오류 타입입니다.
:::

:::topic-grid
## Apple Pay JS SDK 변경 로그
- [Apple Pay JS change log](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-change-log): Apple Pay JS SDK의 새 기능과 업데이트를 살펴봅니다.
:::
