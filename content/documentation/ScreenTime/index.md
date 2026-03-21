---
route: /documentation/ScreenTime
source_url: https://developer.apple.com/documentation/ScreenTime
source_locale: en-US
section: docc
content_type: symbol
title: Screen Time
original_title: Screen Time
source_hash: 5649f43cd23a5d586a9fb6d173675c67a553f525fc4ae687e6ddfc23670b3076
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:39:23+00:00'
last_translated_at: '2026-03-14T01:09:00+09:00'
---

# Screen Time

웹 사용 데이터를 공유하고 관리하며, 부모나 보호자가 적용한 변경 사항을 관찰합니다.

## 개요

Screen Time 프레임워크는 부모와 보호자가 자녀의 웹 사용을 감독할 수 있도록 돕는 데 필요한 도구를 제공합니다. 이 프레임워크를 사용하면 다음을 수행할 수 있습니다.

- 웹 사용 데이터를 보고합니다.
- 기록을 삭제합니다.
- 부모나 보호자가 URL을 차단하거나 자녀 제한을 적용하기 시작할 때 조치를 취합니다.

:::note Note
visionOS에서 실행되는 호환 iPad 또는 iPhone 앱에서는 이 프레임워크의 API가 아무 동작도 하지 않습니다.
:::

:::topic-grid
## 핵심 사항
- [STWebpageController](https://developer.apple.com/documentation/screentime/stwebpagecontroller): 웹 사용을 보고하고 제한된 웹페이지를 차단할 때 사용하는 controller입니다.
:::

:::topic-grid
## 구성 쿼리
- [STScreenTimeConfigurationObserver](https://developer.apple.com/documentation/screentime/stscreentimeconfigurationobserver): 현재 구성의 변경 사항을 관찰할 때 사용하는 객체입니다.
- [STScreenTimeConfiguration](https://developer.apple.com/documentation/screentime/stscreentimeconfiguration): 이 기기의 구성입니다.
:::

:::topic-grid
## 웹 사용 데이터 삭제
- [STWebHistory](https://developer.apple.com/documentation/screentime/stwebhistory): 웹 사용 데이터를 삭제할 때 사용하는 객체입니다.
:::
