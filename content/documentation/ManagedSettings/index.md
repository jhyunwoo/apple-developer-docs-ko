---
route: /documentation/ManagedSettings
source_url: https://developer.apple.com/documentation/ManagedSettings
source_locale: en-US
section: docc
content_type: symbol
title: Managed Settings
original_title: Managed Settings
source_hash: 21df611588f972bf8c8803d3404d8a6bb1c4bf37e75756be62776284be118b6c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:31:17+00:00'
last_translated_at: '2026-03-13T20:20:00+09:00'
---

# Managed Settings

사용자 개인정보와 제어를 유지하면서 앱에서 설정에 접근하고 변경합니다.

## 개요

Managed Settings는 사용자가 자신의 기기에서 특정 설정과 기능에 대한 접근을 제한할 수 있게 하는 개인정보 보호 중심 방식입니다. 사용자의 허가를 받으면 앱은 미디어 표시를 제한하고, 앱 구매를 제한하고, 암호 설정을 잠그며, 그 밖의 기기 동작을 구성할 수 있습니다.

![세 개의 아이콘과 각 아이콘 아래의 on/off 토글 스위치로 구성된 다이어그램입니다. 왼쪽은 on 상태를 나타내는 토글과 함께 표시된 Settings 아이콘입니다. 가운데는 off 상태를 나타내는 토글과 함께 표시된 App Store 아이콘입니다. 오른쪽은 on 상태를 나타내는 토글과 함께 표시된 Safari 아이콘입니다.](https://developer.apple.com)

Managed Settings는 [ManagedSettingsUI](https://developer.apple.com/documentation/ManagedSettingsUI), [Device Activity](https://developer.apple.com/documentation/DeviceActivity), [Family Controls](https://developer.apple.com/documentation/FamilyControls)와 함께 동작하여 앱이 기기 사용을 제한하고, 허용하고, 모니터링할 수 있게 합니다. 앱에서 Managed Settings 권한을 부여하는 방법에 대해 더 알아보려면 [Family Controls](https://developer.apple.com/documentation/FamilyControls)를 참고하십시오. 앱으로 기기 사용을 모니터링하고 예약하는 방법에 대한 자세한 내용은 [Device Activity](https://developer.apple.com/documentation/DeviceActivity)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [Manage settings on devices in a Family Sharing group](https://developer.apple.com/documentation/managedsettings/connectionwithframeworks): 가족의 개인정보를 유지하면서 부모와 보호자가 다른 기기에서 제약을 구성할 수 있게 합니다.
- [Confirming the effective TV and movie ratings](https://developer.apple.com/documentation/managedsettings/readingmedia): 기기의 미디어 등급을 읽고 앱에서 어떤 미디어를 표시할지 결정합니다.
:::

:::topic-grid
## 설정
- [ManagedSettingsStore](https://developer.apple.com/documentation/managedsettings/managedsettingsstore): 현재 사용자 또는 기기에 설정을 적용하는 데이터 저장소입니다.
:::

:::topic-grid
## Shield 동작
- [ShieldAction](https://developer.apple.com/documentation/managedsettings/shieldaction): 확장이 처리할 사용자 동작을 설명하는 상수입니다.
- [ShieldActionDelegate](https://developer.apple.com/documentation/managedsettings/shieldactiondelegate): shield 동작을 처리하는 확장을 위한 클래스입니다.
:::

:::topic-grid
## 가족 개인정보 보호
- [Token](https://developer.apple.com/documentation/managedsettings/token): 앱이나 웹사이트처럼 정체를 드러내지 않는 활동의 표현입니다.
:::

:::topic-grid
## 앱
- [Application](https://developer.apple.com/documentation/managedsettings/application): 사용자 기기의 애플리케이션 표현입니다.
- [ApplicationToken](https://developer.apple.com/documentation/managedsettings/applicationtoken): 애플리케이션의 표현입니다.
:::

:::topic-grid
## 카테고리
- [ActivityCategory](https://developer.apple.com/documentation/managedsettings/activitycategory): 엔터테인먼트나 소셜 같은 활동 카테고리입니다.
- [ActivityCategoryToken](https://developer.apple.com/documentation/managedsettings/activitycategorytoken): 앱 또는 웹사이트 활동의 카테고리를 나타내는 토큰입니다.
:::

:::topic-grid
## 웹사이트
- [WebDomain](https://developer.apple.com/documentation/managedsettings/webdomain): 웹사이트를 나타내는 객체입니다.
- [WebDomainToken](https://developer.apple.com/documentation/managedsettings/webdomaintoken): 사용자의 개인정보를 보호하는 웹 도메인의 표현입니다.
:::
