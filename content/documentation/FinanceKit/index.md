---
route: /documentation/FinanceKit
source_url: https://developer.apple.com/documentation/FinanceKit
source_locale: en-US
section: docc
content_type: symbol
title: FinanceKit
original_title: FinanceKit
source_hash: 9cb696e4ae1efbc29cc3a7387d21a48fbca779d3ac42f6f6b3f92071e4cb363c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:01:49+00:00'
last_translated_at: '2026-03-14T03:05:00+09:00'
---

# FinanceKit

금융 데이터에 접근하고 Wallet 안의 Apple Card, Apple Cash, 주문과 상호 작용합니다.

## 개요

FinanceKit을 사용해 기기 내 금융 데이터와 Apple Cash에 접근하고 Apple Wallet 안의 주문과 상호 작용하십시오.

[FinanceStore](https://developer.apple.com/documentation/financekit/financestore) 및 [FinanceKitUI](https://developer.apple.com/documentation/FinanceKitUI)를 통해 FinanceKit과 상호 작용하며, FinanceKitUI는 사용자가 접근하는 표준화된 UI를 제공합니다.

![FinanceKit hero 로고 이미지입니다.](https://developer.apple.com)

FinanceKit 프레임워크를 사용하면 다음 작업을 수행할 수 있습니다.

- 기기 내 금융 데이터에 접근하기
- Wallet의 주문을 추가, 업데이트, 저장, 상호 작용하기
- Apple Card 및 Apple Cash와 상호 작용하기

:::important Important
누군가의 금융 데이터에 접근하려면 [Get started with FinanceKit](https://developer.apple.com/financekit/)에 명시된 기준을 충족해야 하며, [FinanceKit managed entitlement](https://developer.apple.com/contact/request/financekit/)를 요청하고, 조직 수준 Apple Developer 계정을 보유하고, Account Holder로 로그인하고, `Info.plist`에 `NSFinancialDataUsageDescription` 문자열을 포함해야 합니다. Apple은 [Get started with FinanceKit](https://developer.apple.com/financekit/)를 기준으로 각 신청을 검토합니다. 요청이 기준을 충족하면 Apple은 managed capability를 사용해 entitlement를 개발자 계정에 추가합니다. 접근 요청 방법은 [FinanceKit managed entitlement](https://developer.apple.com/contact/request/financekit/)를 참고하십시오. managed entitlement에 대한 자세한 내용은 [Provisioning with capabilities](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities)를 참고하십시오.
:::

:::topic-grid
## 기초
- [Implementing a background delivery extension](https://developer.apple.com/documentation/financekit/implementing-a-background-delivery-extension): background delivery extension을 추가해 앱과 extension에서 최신 금융 데이터를 수신합니다.
- [FinanceKit updates](https://developer.apple.com/documentation/Updates/FinanceKit): FinanceKit의 변경 사항을 알아봅니다.
:::

:::topic-grid
## 데이터 저장소
- [FinanceStore](https://developer.apple.com/documentation/financekit/financestore): Apple Wallet 주문을 위한 안전한 저장소입니다.
:::

:::topic-grid
## 권한
- [authorizationStatus()](https://developer.apple.com/documentation/financekit/financestore/authorizationstatus()): 호출한 애플리케이션의 권한 상태를 확인합니다.
- [requestAuthorization()](https://developer.apple.com/documentation/financekit/financestore/requestauthorization()): 사용자가 금융 데이터 접근에 대한 FinanceKit 권한을 부여하도록 요청합니다.
- [AuthorizationStatus](https://developer.apple.com/documentation/financekit/authorizationstatus)
:::

:::topic-grid
## 계정
- [accounts(query:)](https://developer.apple.com/documentation/financekit/financestore/accounts(query:)): 제공된 account query 기준을 만족하는, 사용자가 Wallet에 추가한 계정 목록을 반환합니다.
- [accountHistory(since:isMonitoring:)](https://developer.apple.com/documentation/financekit/financestore/accounthistory(since:ismonitoring:)): 제공된 financial history token이 지정하는 시점 이후에 사용자가 추가한 계정 목록을 반환합니다.
- [AssetAccount](https://developer.apple.com/documentation/financekit/assetaccount): asset account의 특성을 설명하는 구조체입니다.
- [LiabilityAccount](https://developer.apple.com/documentation/financekit/liabilityaccount): liability account의 특성을 설명하는 구조체입니다.
- [Account](https://developer.apple.com/documentation/financekit/account): 금융 계정을 설명하는 구조체입니다.
:::

:::topic-grid
## 잔액
- [accountBalances(query:)](https://developer.apple.com/documentation/financekit/financestore/accountbalances(query:)): 제공된 account query 기준을 만족하는 잔액 목록을 반환합니다.
- [accountBalanceHistory(forAccountID:since:isMonitoring:)](https://developer.apple.com/documentation/financekit/financestore/accountbalancehistory(foraccountid:since:ismonitoring:)): 제공된 financial history token이 지정하는 시점 이후의 계정 잔액 이력을 반환합니다.
- [AccountBalance](https://developer.apple.com/documentation/financekit/accountbalance): 특정 시점의 계정 금융 잔액을 설명하는 구조체입니다.
- [AccountBalanceQuery](https://developer.apple.com/documentation/financekit/accountbalancequery): account balance query를 정의하는 구조체입니다.
- [Balance](https://developer.apple.com/documentation/financekit/balance): 계정 잔액을 설명하는 구조체입니다.
- [CreditDebitIndicator](https://developer.apple.com/documentation/financekit/creditdebitindicator): 프레임워크가 거래를 입금 또는 출금으로 설명할 때 사용하는 값입니다.
- [CurrentBalance](https://developer.apple.com/documentation/financekit/currentbalance): 계정 신용 잔액 상태를 설명하는 값입니다.
:::

:::topic-grid
## 주문
- [FullyQualifiedOrderIdentifier](https://developer.apple.com/documentation/financekit/fullyqualifiedorderidentifier): 주문의 특성을 지정하는 구조체입니다.
- [saveOrder(signedArchive:)](https://developer.apple.com/documentation/financekit/financestore/saveorder(signedarchive:)): 저장소에 주문을 추가하거나 기존 주문을 업데이트합니다.
:::

:::topic-grid
## 거래
- [transactionHistory(forAccountID:since:isMonitoring:)](https://developer.apple.com/documentation/financekit/financestore/transactionhistory(foraccountid:since:ismonitoring:)): 지정한 account ID, 선택적 시작 시점, 장시간 실행되는 transaction query용 monitoring indicator에 대한 거래를 반환합니다.
- [transactions(query:)](https://developer.apple.com/documentation/financekit/financestore/transactions(query:)): 제공된 transaction query와 일치하는 거래를 반환합니다.
- [AccountQuery](https://developer.apple.com/documentation/financekit/accountquery): account query를 정의하는 구조체입니다.
- [AccountCreditInformation](https://developer.apple.com/documentation/financekit/accountcreditinformation): 계정과 연결된 신용 정보를 설명하는 구조체입니다.
- [CurrencyAmount](https://developer.apple.com/documentation/financekit/currencyamount): 금액과 해당 통화를 설명하는 구조체입니다.
- [Transaction](https://developer.apple.com/documentation/financekit/transaction): 특정 금융 계정과 관련된 거래를 나타내는 구조체입니다.
- [TransactionQuery](https://developer.apple.com/documentation/financekit/transactionquery): transaction query에 사용할 매개변수를 설명하는 구조체입니다.
- [TransactionType](https://developer.apple.com/documentation/financekit/transactiontype): 거래 종류를 설명하는 값입니다.
- [TransactionStatus](https://developer.apple.com/documentation/financekit/transactionstatus): 거래 상태를 설명하는 값입니다.
:::

:::topic-grid
## query
- [FinanceStore.HistoryToken](https://developer.apple.com/documentation/financekit/financestore/historytoken): 금융 데이터 query에 사용할 시작 지점을 설명하는 구조체입니다.
:::

:::topic-grid
## 가맹점 카테고리
- [MerchantCategoryCode](https://developer.apple.com/documentation/financekit/merchantcategorycode)
:::

:::topic-grid
## 오류
- [FinanceError](https://developer.apple.com/documentation/financekit/financeerror): 금융 데이터 접근 중 발생할 수 있는 오류를 설명하는 값입니다.
:::

:::topic-grid
## 프로토콜
- [BackgroundDeliveryExtension](https://developer.apple.com/documentation/financekit/backgrounddeliveryextension): finance store 안의 데이터 변경에 대한 업데이트를 받기 위해 사용하는 extension입니다.
- [BackgroundDeliveryExtensionProviding](https://developer.apple.com/documentation/financekit/backgrounddeliveryextensionproviding)
:::
