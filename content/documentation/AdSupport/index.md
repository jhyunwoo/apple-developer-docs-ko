---
route: /documentation/AdSupport
source_url: https://developer.apple.com/documentation/AdSupport
source_locale: en-US
section: docc
content_type: symbol
title: AdSupport
original_title: AdSupport
source_hash: 622b78635a0230d5e70e52dd404531e4e8e1a166488a80118472319b06ccd01d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:47:10+00:00'
last_translated_at: '2026-03-13T21:05:00+09:00'
---

# AdSupport

앱이 광고 식별자에 접근할 수 있도록 제공합니다.

## 개요

AdSupport 프레임워크를 사용해 광고 식별자를 얻으십시오. [advertisingIdentifier](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier)는 각 기기마다 고유한 영숫자 문자열이며, 광고 목적으로만 사용합니다. iOS 14.5 이상과 iPadOS 14.5 이상이 실행되는 기기에서는 앱이 [advertisingIdentifier](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier) 프로퍼티를 얻기 전에 `App Tracking Transparency`를 지원하고 [NSUserTrackingUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserTrackingUsageDescription) 목적 문자열을 정의해야 합니다.

### 광고 식별자 가져오기

처음으로 광고 식별자를 요청하기 전에 앱은 [requestTrackingAuthorization(completionHandler:)](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/requestTrackingAuthorization(completionHandler:))를 한 번 호출해야 합니다. 이 메서드는 사용자에게 앱 추적 권한 요청을 표시합니다. 사용자는 추적 허용 여부를 선택하며, 이후에도 언제든지 설정 > 개인 정보 보호 > 추적에서 앱의 권한을 변경할 수 있습니다. 사용자의 의도는 [trackingAuthorizationStatus](https://developer.apple.com/documentation/AppTrackingTransparency/ATTrackingManager/trackingAuthorizationStatus)로 앱의 권한 상태를 확인해 파악할 수 있습니다.

광고 식별자를 얻으려면 다음 단계를 따르십시오.

1. AdSupport 프레임워크를 사용해 [shared()](https://developer.apple.com/documentation/adsupport/asidentifiermanager/shared()) 클래스 메서드를 호출하고 [ASIdentifierManager](https://developer.apple.com/documentation/adsupport/asidentifiermanager)의 인스턴스를 검색합니다.
2. [advertisingIdentifier](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier) 프로퍼티를 사용해 UUID를 얻습니다.

아래 코드는 광고 식별자를 검색하는 방법을 보여줍니다.

```swift
import AdSupport

let sharedASIdentifierManager = ASIdentifierManager.shared()
var adID = sharedASIdentifierManager.advertisingIdentifier

```

광고 식별자는 고유한 UUID 또는 모두 0으로 이루어진 값을 반환합니다. 반환되는 값에 대한 자세한 내용은 [advertisingIdentifier](https://developer.apple.com/documentation/adsupport/asidentifiermanager/advertisingidentifier)를 참고하십시오.

사용자에게 추적 권한을 요청하는 방법에 대한 자세한 내용은 [User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [ASIdentifierManager](https://developer.apple.com/documentation/adsupport/asidentifiermanager): 광고 식별자를 담는 객체입니다.
:::
