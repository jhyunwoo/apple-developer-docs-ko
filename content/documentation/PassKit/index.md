---
route: /documentation/PassKit
source_url: https://developer.apple.com/documentation/PassKit
source_locale: en-US
section: docc
content_type: symbol
title: PassKit (Apple Pay and Wallet)
original_title: PassKit (Apple Pay and Wallet)
source_hash: ace151af0b931a74bf14fedf42a8f54a9a0f0e12493d2081b0aa7822c1dfc780
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:03:24+00:00'
last_translated_at: '2026-03-13T16:25:00+09:00'
---

# PassKit (Apple Pay and Wallet)

앱에서 Apple Pay 결제를 처리하고 Wallet 앱용 패스를 생성하고 배포합니다.

## 개요

PassKit 프레임워크를 사용하면 다음 작업을 수행할 수 있습니다.

- 앱에 Apple Pay를 추가합니다.
- 사용자의 Wallet 앱에 있는 패스를 관리합니다.

![Apple Pay 로고입니다.](https://developer.apple.com)

Apple Pay는 사용자가 매장, 앱, 웹에서 구매를 수행할 수 있는 안전하고 간편한 방법입니다. iOS 및 watchOS 앱에서 PassKit API를 사용해 Apple Pay를 지원하면, 사용자는 앱을 벗어나지 않고도 실물 상품과 서비스를 구매하거나 비영리 단체에 기부할 수 있습니다.

:::note Note
웹 애플리케이션에 Apple Pay를 추가하려면 [Apple Pay on the Web](https://developer.apple.com/documentation/ApplePayontheWeb)을 참고하십시오.

앱 내부에서 제공되는 디지털 상품 및 서비스의 경우에는 [In-App Purchase](https://developer.apple.com/in-app-purchase/)를 대신 참고하십시오.
:::

![Wallet을 나타내는 아이콘입니다.](https://developer.apple.com)

Wallet 앱을 사용하면 사용자가 탑승권, 티켓, 상품권, 멤버십 카드를 정리할 수 있습니다. 또한 Apple Pay용 결제 카드도 관리할 수 있습니다. PassKit 프레임워크를 사용하면 Wallet에 패스를 추가하고, 패스가 관련되는 시간과 장소에 따라 사용자의 잠금 화면에 표시되도록 할 수 있습니다. 또한 push notification을 사용해 패스의 내용을 업데이트할 수도 있습니다.

:::topic-grid
## Apple Pay 지원
- [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay): 앱에서 Apple Pay 결제를 요청하고 처리합니다.
:::

:::topic-grid
## Wallet 지원
- [Wallet](https://developer.apple.com/documentation/passkit/wallet): Wallet 앱에서 티켓, 탑승권, 결제 카드 및 기타 패스를 관리합니다.
:::
