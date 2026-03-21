---
route: /documentation/DeclaredAgeRange
source_url: https://developer.apple.com/documentation/DeclaredAgeRange
source_locale: en-US
section: docc
content_type: symbol
title: Declared Age Range
original_title: Declared Age Range
source_hash: f7e4db9df03c1ece40a3543d5aa3af77c1550bb37dcd19ed695e5228c902e5a4
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:02:15+00:00'
last_translated_at: '2026-03-13T21:47:00+09:00'
---

# Declared Age Range

사용자에게 연령대 공유를 요청하여 앱에서 연령에 적합한 경험을 만듭니다.

## 개요

Declared Age Range API를 사용하면 사용자에게 자신의 연령대를 앱과 공유해 달라고 요청할 수 있습니다. Family Sharing 그룹에 속한 아동의 경우, 부모나 보호자 또는 Family Organizer가 아동의 연령 정보를 앱과 항상 공유할지, 매번 아동에게 물어볼지, 혹은 절대 공유하지 않을지를 결정할 수 있습니다. 시스템은 연령대와 함께 사용자가 제공한 연령대에 대한 [AgeRangeService.AgeRangeDeclaration](https://developer.apple.com/documentation/declaredagerange/agerangeservice/agerangedeclaration)도 반환합니다. Declared Age Range API를 사용하려면 Xcode에서 target의 Declared Age Range capability를 활성화하여 앱에 [com.apple.developer.declared-age-range](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.declared-age-range) entitlement를 추가하십시오. 자세한 내용은 [Adding capabilities to your app](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app)를 참고하십시오.

:::important 중요
Declared Age Range API의 데이터는 최종 사용자 또는 그 부모나 보호자가 직접 선언한 정보를 기반으로 합니다. 앱에 적용될 수 있는 관련 법률이나 규정을 준수하는 책임은 전적으로 개발자에게 있습니다.
:::

:::topic-grid
## 핵심 사항
- [com.apple.developer.declared-age-range](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.declared-age-range): 앱이 사용자의 연령대를 요청할 수 있는지를 나타내는 Boolean 값입니다.
- [Requesting people’s age range information in your app](https://developer.apple.com/documentation/declaredagerange/requesting-people-share-their-age-range-with-your-app): 개인 정보를 보호하면서 사용자에게 앱과 연령대를 공유하도록 요청하고, 성인, 청소년, 아동에 맞춰 기능을 조정합니다.
:::

:::topic-grid
## 연령대 요청
- [AgeRangeService](https://developer.apple.com/documentation/declaredagerange/agerangeservice): 현재 기기에 로그인한 사용자의 연령대를 요청하는 서비스입니다.
- [DeclaredAgeRangeAction](https://developer.apple.com/documentation/declaredagerange/declaredagerangeaction): 사용자의 연령대를 요청하는 action입니다.
:::

:::topic-grid
## 중요한 변경 확인
- [SignificantUpdateAction](https://developer.apple.com/documentation/declaredagerange/significantupdateaction): 중요한 앱 업데이트 확인을 위한 시스템 sheet를 표시하는 action입니다.
:::
