---
route: /documentation/ManagedSettingsUI
source_url: https://developer.apple.com/documentation/ManagedSettingsUI
source_locale: en-US
section: docc
content_type: symbol
title: Managed Settings UI
original_title: Managed Settings UI
source_hash: a8a32649da7896751ff191ce180051e3c9a5564aa1f53a7c0cd947f8053edef6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:03:25+00:00'
last_translated_at: '2026-03-13T16:25:00+09:00'
---

# Managed Settings UI

차단(shield) view의 외형을 정의하고 구성합니다.

## 개요

Managed Settings UI를 사용하면 누군가 앱이나 웹사이트에 접근 제한을 적용했을 때 시스템이 표시하는 shield의 모양을 사용자화할 수 있습니다. shield는 누군가가 일일 사용 시간 제한 같은 앱 또는 웹사이트 사용 한도를 초과했거나, 제한 시간이 적용되는 동안 접근을 시도할 때 나타납니다.

이 프레임워크는 [Managed Settings](https://developer.apple.com/documentation/managedsettings)와 함께 동작하여 접근 제어 차단 화면을 사용자화합니다. [Managed Settings](https://developer.apple.com/documentation/managedsettings)는 shield의 동작과 적용을 처리하고, Managed Settings UI는 사용자 정의 버튼 스타일, 제목, 아이콘, 색상, 하위 메뉴 항목으로 시각적 표현을 사용자화할 수 있게 해 줍니다.

:::topic-grid
## shield 외형
- [ShieldConfiguration](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration): 앱 또는 웹사이트 위에 표시할 shield의 외형을 정의하는 객체입니다.
- [ShieldConfigurationDataSource](https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource): shield의 외형을 구성하는 app extension의 principal object를 위한 기본 클래스입니다.
:::
