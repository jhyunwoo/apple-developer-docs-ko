---
route: /documentation/StoreKitTest
source_url: https://developer.apple.com/documentation/StoreKitTest
source_locale: en-US
section: docc
content_type: symbol
title: StoreKit Test
original_title: StoreKit Test
source_hash: 58a00c332aab74d7f2d855c524b1aab917d07d2d682255e4a81091493e25e86e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:42:57+00:00'
last_translated_at: '2026-03-13T23:42:57+09:00'
---

# StoreKit Test

앱의 구독과 In-App Purchase 거래, 그리고 SKAdNetwork 구현을 위한 테스트를 Xcode에서 만들고 자동화합니다.

## 개요

StoreKitTest 프레임워크는 Xcode에서 StoreKit 테스트를 자동화할 수 있게 해 줍니다. 이 프레임워크를 사용해 unit test와 continuous integration test를 작성하십시오. 테스트 환경을 제어하려면 [SKTestSession](https://developer.apple.com/documentation/StoreKitTest/SKTestSession)과 [SKAdTestSession](https://developer.apple.com/documentation/StoreKitTest/SKAdTestSession)을 사용합니다.

In-App Purchase 거래를 테스트할 때는 `SKTestSession`을 사용합니다. 각 `SKTestSession` 인스턴스는 Xcode에서 StoreKit 테스트를 위해 수동으로 변경하는 것과 동일한 설정에 접근할 수 있게 해 줍니다. 이 클래스를 사용해 구독 갱신, Ask to Buy 거래 같은 다양한 In-App Purchase 시나리오를 테스트하고, 테스트 환경에서 거래를 계속 제어할 수 있습니다.

광고 impression과 postback을 테스트할 때는 `SKAdTestSession`을 사용합니다. 각 `SKAdTestSession` 인스턴스는 직접 생성한 test postback 세트를 보관하며, 이를 여러 unit test에서 사용할 수 있습니다. [SKAdNetwork](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) API를 사용하는 광고 네트워크는 이 클래스를 이용해 자신이 서명한 광고 impression을 검증하고, 서버에서 postback을 수신하는 흐름을 테스트할 수 있습니다. 광고되는 앱은 자신의 conversion value update를 테스트할 수 있습니다.

iOS, watchOS, tvOS 앱에서 StoreKit을 테스트하려면 macOS 10.15 이상에서 실행되는 Xcode 12 이상이 필요합니다. macOS 앱에서 StoreKit을 테스트하려면 macOS 11 이상에서 실행되는 Xcode 12 이상이 필요합니다.

:::note Related session from WWDC20
Session 10659: [Meet StoreKit Testing in Xcode](https://developer.apple.com/wwdc20/10659)
:::

:::topic-grid
## StoreKit 거래 테스트
- [Xcode에서 StoreKit Testing 설정하기](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode): 로컬에서 구성한 데이터로 In-App Purchase를 테스트할 수 있도록 테스트 환경을 준비합니다.
- [SKTestSession](https://developer.apple.com/documentation/storekittest/sktestsession): Xcode에서 StoreKit 거래를 테스트할 때 사용하는 제어와 환경 구성입니다.
- [SKTestTransaction](https://developer.apple.com/documentation/storekittest/sktesttransaction): 테스트 환경에서 발생하는 거래입니다.
:::

:::topic-grid
## StoreKit 거래 테스트 오류
- [SKTestErrorDomain](https://developer.apple.com/documentation/storekittest/sktesterrordomain): 테스트 환경 오류 코드의 도메인을 나타내는 상수입니다.
- [SKTestError](https://developer.apple.com/documentation/storekittest/sktesterror): 테스트 환경이 반환하는 오류에 대한 정보입니다.
:::

:::topic-grid
## 광고 impression 및 postback 테스트
- [SKAdNetwork용 광고 impression signature와 postback 테스트 및 검증](https://developer.apple.com/documentation/storekittest/testing-and-validating-ad-impression-signatures-and-postbacks-for-skadnetwork): StoreKit Test 프레임워크로 unit test를 만들어 광고 impression을 검증하고 postback을 테스트합니다.
- [SKAdTestSession](https://developer.apple.com/documentation/storekittest/skadtestsession): Xcode에서 광고 impression과 postback을 테스트하는 데 사용하는 클래스입니다.
- [SKAdTestPostback](https://developer.apple.com/documentation/storekittest/skadtestpostback): 테스트 환경에서 광고 conversion 정보를 담고 있는 test postback입니다.
- [SKAdTestPostbackResponse](https://developer.apple.com/documentation/storekittest/skadtestpostbackresponse): 테스트 환경에서 시스템이 전송한 postback의 상태와 오류 정보입니다.
- [SKAdTestPostbackVersion](https://developer.apple.com/documentation/storekittest/skadtestpostbackversion): postback 버전을 나타내는 상수입니다.
:::

:::topic-grid
## 광고 impression 및 postback 오류
- [SKAdTestErrorDomain](https://developer.apple.com/documentation/storekittest/skadtesterrordomain): 테스트 환경에서 SKAdNetwork 테스트 오류 도메인을 식별하는 문자열입니다.
- [SKAdTestError](https://developer.apple.com/documentation/storekittest/skadtesterror): 테스트 환경이 반환하는 SKAdNetwork 테스트 오류입니다.
:::

:::topic-grid
## 구조체
- [StoreKitAppStoreSyncAPI](https://developer.apple.com/documentation/storekittest/storekitappstoresyncapi)
- [StoreKitAppTransactionAPI](https://developer.apple.com/documentation/storekittest/storekitapptransactionapi)
- [StoreKitLoadProductsAPI](https://developer.apple.com/documentation/storekittest/storekitloadproductsapi)
- [StoreKitManageSubscriptionsAPI](https://developer.apple.com/documentation/storekittest/storekitmanagesubscriptionsapi)
- [StoreKitOfferCodeRedeemAPI](https://developer.apple.com/documentation/storekittest/storekitoffercoderedeemapi)
- [StoreKitPurchaseAPI](https://developer.apple.com/documentation/storekittest/storekitpurchaseapi)
- [StoreKitRefundRequestAPI](https://developer.apple.com/documentation/storekittest/storekitrefundrequestapi)
- [StoreKitSubscriptionStatusAPI](https://developer.apple.com/documentation/storekittest/storekitsubscriptionstatusapi)
- [StoreKitVerificationAPI](https://developer.apple.com/documentation/storekittest/storekitverificationapi)
:::

:::topic-grid
## 열거형
- [SKTestFailures](https://developer.apple.com/documentation/storekittest/sktestfailures)
:::

:::topic-grid
## 프로토콜
- [FailableStoreKitAPI](https://developer.apple.com/documentation/storekittest/failablestorekitapi)
- [SKTestFailure](https://developer.apple.com/documentation/storekittest/sktestfailure)
:::
