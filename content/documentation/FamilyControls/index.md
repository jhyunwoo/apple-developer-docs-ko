---
route: /documentation/FamilyControls
source_url: https://developer.apple.com/documentation/FamilyControls
source_locale: en-US
section: docc
content_type: symbol
title: Family Controls
original_title: Family Controls
source_hash: 9f583b2c5d1f062bb9ffcffec8234374bd294b1b7e783a327aaaf6f12d51f107
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:47:52+00:00'
last_translated_at: '2026-03-14T00:13:00+09:00'
---

# Family Controls

기기에서 앱이 자녀 보호 기능을 제공하도록 인증합니다.

## 개요

자녀 보호 앱을 인증하려면 공유 [AuthorizationCenter](https://developer.apple.com/documentation/familycontrols/authorizationcenter) 인스턴스를 사용합니다. 어떤 기기에서든 자녀 보호 기능을 인증할 수 있습니다.

![allow activity라는 레이블이 있는 그림입니다. Family Sharing 로고에서 화살표가 이어집니다.](https://developer.apple.com)

:::important Important
[requestAuthorization(for:)](https://developer.apple.com/documentation/familycontrols/authorizationcenter/requestauthorization(for:)) 또는 [revokeAuthorization(completionHandler:)](https://developer.apple.com/documentation/familycontrols/authorizationcenter/revokeauthorization(completionhandler:)) 메서드를 호출하기 전에 앱에 Family Controls capability를 추가해야 합니다. 이 capability는 앱에 [Family Controls](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.family-controls) entitlement를 추가합니다. App Store에 앱을 제출하기 전에 entitlement 사용을 위해 반드시 [request permission](https://developer.apple.com/contact/request/family-controls-distribution)을 해야 합니다. 자세한 내용은 [Adding capabilities to your app](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app)를 참고합니다.
:::

자녀에 대한 자녀 보호 기능 인증은 동일한 Family Sharing 그룹에 속한 부모 또는 보호자의 승인이 필요합니다. 시스템은 자녀의 기기에 인증 sheet를 표시하고, 부모 또는 보호자가 인증 요청을 승인하거나 거부합니다. 시스템은 결과를 앱의 `AuthorizationCenter`로 보냅니다.

개인에 대한 자녀 보호 기능 인증은 기기 소유자의 승인이 필요합니다. 시스템은 사용자가 인증 요청을 승인하거나 거부한 뒤 개인의 기기에 생체 인증 경고를 표시합니다. 시스템은 결과를 앱의 `AuthorizationCenter`로 보냅니다.

Family Controls 프레임워크는 부모 또는 보호자가 승인한 자녀 사용자가 자녀 보호 설정을 우회할 수 있는 동작을 수행하지 못하도록 막습니다. 예를 들어 앱이 인증되면 자녀 사용자가 자녀 보호 기능을 제공하는 앱을 삭제할 수 없습니다. 또한 부모 또는 보호자가 승인한 자녀 보호 앱이 하나라도 있는 동안에는 사용자가 iCloud에서 로그아웃할 수 없습니다.

visionOS에서 실행되는 호환 iPad 또는 iPhone 앱에서는 인증 시도가 항상 실패합니다.

:::topic-grid
## 인증
- [AuthorizationCenter](https://developer.apple.com/documentation/familycontrols/authorizationcenter): 자녀 보호 기능 제공을 위한 인증을 요청하는 중심 객체입니다.
- [AuthorizationStatus](https://developer.apple.com/documentation/familycontrols/authorizationstatus): 자녀 보호 기능을 제공하기 위한 앱 인증 상태입니다.
- [Family Controls](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.family-controls): 앱이 자녀 보호 기능 제공에 대한 인증을 요청하거나 철회할 수 있는지를 나타내는 Boolean 값입니다.
- [Requesting the Family Controls entitlement](https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement): Family Controls를 사용하도록 앱과 Screen Time API app extension을 등록합니다.
:::

:::topic-grid
## 계정 유형
- [FamilyControlsMember](https://developer.apple.com/documentation/familycontrols/familycontrolsmember): 현재 Family Controls가 관리하는 계정 유형입니다.
:::

:::topic-grid
## 활동 선택
- [FamilyActivityPicker](https://developer.apple.com/documentation/familycontrols/familyactivitypicker): 앱에 선택 내용을 노출하지 않고 사용자가 애플리케이션, 웹 도메인, 카테고리를 지정하는 뷰입니다.
- [FamilyActivitySelection](https://developer.apple.com/documentation/familycontrols/familyactivityselection): 사용자가 선택한 애플리케이션, 카테고리, 웹 도메인의 모음입니다.
:::

:::topic-grid
## 활동 레이블
- [Displaying Activity Labels](https://developer.apple.com/documentation/familycontrols/displayingactivitylabels): 애플리케이션, 카테고리 또는 웹 도메인에 대한 읽기 전용 시각 표현을 사용자에게 제공합니다.
:::

:::topic-grid
## 오류
- [FamilyControlsError](https://developer.apple.com/documentation/familycontrols/familycontrolserror): Family Controls 프레임워크가 보고하는 오류입니다.
:::

:::topic-grid
## 클래스
- [FamilyActivityData](https://developer.apple.com/documentation/familycontrols/familyactivitydata): 사용자의 family activity 데이터에 대한 인터페이스입니다.
:::
