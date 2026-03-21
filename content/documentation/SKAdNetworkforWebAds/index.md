---
route: /documentation/SKAdNetworkforWebAds
source_url: https://developer.apple.com/documentation/SKAdNetworkforWebAds
source_locale: en-US
section: docc
content_type: symbol
title: SKAdNetwork for Web Ads
original_title: SKAdNetwork for Web Ads
source_hash: b38ce2192feb48ae8d0a3dede43ad56b99381c6b6c4d525b01d3f34c038e19d5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:42:57+00:00'
last_translated_at: '2026-03-13T23:42:57+09:00'
---

# SKAdNetwork for Web Ads

웹에서 시작된 앱 설치 캠페인을 어트리뷰션합니다.

## 개요

[SKAdNetworkforWebAds](https://developer.apple.com/documentation/SKAdNetworkforWebAds) API를 사용하면 광고주는 사용자 개인정보를 보호하면서 웹에서 시작된 광고 캠페인의 성과를 측정할 수 있습니다. iOS 16.1 이상에서 광고 네트워크는 이 API를 사용해 Safari의 웹 광고 클릭이 App Store 앱 설치로 이어졌을 때 [SKAdNetwork](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) attribution을 받을 수 있습니다.

이 API를 사용하려면 다음 단계를 따르십시오.

1. 광고 네트워크를 등록합니다. 자세한 내용은 [광고 네트워크 등록하기](https://developer.apple.com/documentation/StoreKit/registering-an-ad-network)를 참고하십시오.
2. 웹 광고 링크를 구성하고 표시합니다. 자세한 내용은 [attributable ad link 만들기](https://developer.apple.com/documentation/skadnetworkforwebads/creating-an-attributable-ad-link)를 참고하십시오.
3. 광고된 앱이 앱 설치를 광고 캠페인에 attribution할 수 있도록 signed web ad payload를 제공하는 endpoint를 구현합니다. 자세한 내용은 [attributable web ad용 signature 생성하기](https://developer.apple.com/documentation/skadnetworkforwebads/generating-a-signature-for-attributable-web-ads)를 참고하십시오.
4. 수신한 attribution을 검증합니다. 자세한 내용은 [install validation postback 검증하기](https://developer.apple.com/documentation/StoreKit/verifying-an-install-validation-postback)를 참고하십시오.

광고 네트워크 API에 대한 추가 정보는 [SKAdNetwork](https://developer.apple.com/documentation/StoreKit/SKAdNetwork)를 참고하십시오.

:::note Note
광고 네트워크는 이 API를 사용해 Safari의 웹 광고 클릭에 대한 attribution만 받을 수 있습니다. 이 API는 [SFSafariViewController](https://developer.apple.com/documentation/SafariServices/SFSafariViewController) 또는 [WKWebView](https://developer.apple.com/documentation/WebKit/WKWebView) 안에서 발생한 웹 광고 클릭에는 attribution을 제공하지 않습니다.
:::

:::topic-grid
## 핵심
- [attributable ad link 만들기](https://developer.apple.com/documentation/skadnetworkforwebads/creating-an-attributable-ad-link): App Store 앱 설치를 광고 네트워크에 attribution하는 클릭형 웹 광고를 만듭니다.
:::

:::topic-grid
## 웹 광고 payload 요청 수신
- [Get a Signed Web Ad Impression Payload](https://developer.apple.com/documentation/skadnetworkforwebads/get-a-signed-skadnetwork-ad-payload-for-a-web-ad.): 기기로부터 서명된 광고 상호작용 제공 요청을 받기 위해 제공하는 endpoint입니다.
- [AdImpressionRequest](https://developer.apple.com/documentation/skadnetworkforwebads/adimpressionrequest): 기기가 광고 네트워크 서버에서 웹 광고 impression을 가져오기 위해 보내는 request body입니다.
:::

:::topic-grid
## 웹 광고 signature와 응답 제공
- [attributable web ad용 signature 생성하기](https://developer.apple.com/documentation/skadnetworkforwebads/generating-a-signature-for-attributable-web-ads): attributable web ad를 위한 서명된 매개변수를 제공해 install validation을 시작합니다.
- [AdImpressionResponse](https://developer.apple.com/documentation/skadnetworkforwebads/adimpressionresponse): 클릭된 웹 광고에 대한 signed payload를 담아 제공하는 응답입니다.
- [signature](https://developer.apple.com/documentation/skadnetworkforwebads/signature): 광고 네트워크가 웹 광고에 암호학적 서명을 적용할 때 사용하는 key-value 쌍입니다.
:::
