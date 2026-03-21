---
route: /documentation/FinanceKitUI
source_url: https://developer.apple.com/documentation/FinanceKitUI
source_locale: en-US
section: docc
content_type: symbol
title: FinanceKitUI
original_title: FinanceKitUI
source_hash: 8dd43550e3550718c908d62acc39a89794d91c254f8eca8c97f80bc9bf60d99e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:33:50+00:00'
last_translated_at: '2026-03-14T00:58:00+09:00'
---

# FinanceKitUI

Apple Wallet에 주문을 추가합니다.

## 개요

`FinanceKitUI` 프레임워크는 [FinanceKit](https://developer.apple.com/documentation/FinanceKit) 및 [FinanceStore](https://developer.apple.com/documentation/FinanceKit/FinanceStore)와 안전하게 상호 작용하는 표준화된 UI를 담고 있으며, 사용자의 Apple Wallet에 주문을 추가할 수 있도록 지원합니다.

`FinanceKitUI`는 SwiftUI용 `AddOrderToWalletButton`을 제공합니다. 사용자가 자신의 Apple Wallet에 주문을 추가할 수 있게 하고 싶을 때 이 버튼을 UI에 배치하십시오. 버튼의 스타일 옵션은 표준 Apple Pay 및 Wallet 디자인 언어와 일치하므로, 사용자는 이 버튼과 상호 작용할 때 익숙함과 신뢰감을 느낄 수 있습니다.

:::topic-grid
## Apple Wallet에 주문 추가하기
- [AddOrderToWalletButton](https://developer.apple.com/documentation/financekitui/addordertowalletbutton): 사용자의 Apple Wallet에 주문을 추가할 때 사용하는 버튼입니다.
- [AddOrderToWalletButtonStyle](https://developer.apple.com/documentation/financekitui/addordertowalletbuttonstyle): Add Order to Apple Wallet 버튼의 스타일을 결정하는 값입니다.
:::

:::topic-grid
## 프로토콜
- [FinancialConnectionUIExtension](https://developer.apple.com/documentation/financekitui/financialconnectionuiextension)
- [FinancialConnectionUIExtensionProviding](https://developer.apple.com/documentation/financekitui/financialconnectionuiextensionproviding)
- [FinancialConnectionUIExtensionScene](https://developer.apple.com/documentation/financekitui/financialconnectionuiextensionscene)
:::

:::topic-grid
## 구조체
- [FinancialConnectionExtensionAuthorizationRequest](https://developer.apple.com/documentation/financekitui/financialconnectionextensionauthorizationrequest)
- [FinancialConnectionExtensionAuthorizationResult](https://developer.apple.com/documentation/financekitui/financialconnectionextensionauthorizationresult)
- [FinancialConnectionUIExtensionAuthorizationScene](https://developer.apple.com/documentation/financekitui/financialconnectionuiextensionauthorizationscene): 앱의 Financial Connection을 인증하려면 이 scene을 구현합니다.
- [TransactionPicker](https://developer.apple.com/documentation/financekitui/transactionpicker): FinanceKit에서 트랜잭션을 선택할 수 있는 transaction picker를 표시하는 view입니다.
:::

:::topic-grid
## 타입 별칭
- [FinancialConnectionExtensionAuthorizationParams](https://developer.apple.com/documentation/financekitui/financialconnectionextensionauthorizationparams)
:::
