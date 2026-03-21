---
route: /documentation/DeviceActivity
source_url: https://developer.apple.com/documentation/DeviceActivity
source_locale: en-US
section: docc
content_type: symbol
title: Device Activity
original_title: Device Activity
source_hash: ed6288f3d20c8638e430fb85984e1c75936ce455c60d6ceeb9d818feae796a6d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:04:39+00:00'
last_translated_at: '2026-03-14T03:18:00+09:00'
---

# Device Activity

개인 정보 보호를 유지하면서 app extension으로 기기 활동을 모니터링합니다.

## 개요

Device Activity는 애플리케이션이 사용자의 앱 및 웹사이트 활동을 개인 정보 보호를 지키는 방식으로 모니터링할 수 있게 합니다. 예를 들어 사용자가 자야 하는 동안 기기 활동을 모니터링하는 취침 시간 일정을 설정할 수 있습니다. app extension은 활동 일정이 시작되거나 끝나기 전에 경고를 받거나, 활동이 미리 정의한 임계값에 도달하기 직전에 경고를 받을 수 있습니다. 웹사이트와 앱에서 보낸 시간을 모니터링해 사용자가 임계값에 도달했을 때 경고를 표시할 수 있습니다.

![프레임워크가 모니터링할 수 있는 다양한 종류의 device activity를 보여 주는 다이어그램입니다. 왼쪽에는 App Store, Settings, Safari 아이콘 세 개가 세로로 있고, 모두 시계를 향한 화살표가 있습니다.](https://developer.apple.com)

:::topic-grid
## 활동 관리
- [DeviceActivityEvent](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent): 애플리케이션, category, 또는 웹사이트 활동을 나타내는 이벤트입니다.
- [DeviceActivityName](https://developer.apple.com/documentation/deviceactivity/deviceactivityname): 활동의 고유 이름입니다.
- [DeviceActivitySchedule](https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule): 기기 활동을 언제 모니터링할지에 대한 calendar 기반 일정입니다.
- [DeviceActivityCenter](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter): 애플리케이션의 extension이 예정된 device activity 모니터링을 시작할 수 있게 하는 클래스입니다.
:::

:::topic-grid
## 활동 모니터링
- [DeviceActivityMonitor](https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor): 예정된 device activity를 모니터링하는 객체입니다.
:::

:::topic-grid
## 활동 보고
- [DeviceActivityReport](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport): 사용자의 애플리케이션, category, 웹 도메인 활동을 개인 정보 보호를 유지하는 방식으로 보고하는 view입니다.
- [DeviceActivityReportExtension](https://developer.apple.com/documentation/deviceactivity/deviceactivityreportextension): device activity 데이터를 보고하는 app extension입니다.
- [DeviceActivityReportScene](https://developer.apple.com/documentation/deviceactivity/deviceactivityreportscene): 사용자 정의 device activity report scene을 정의합니다.
- [DeviceActivityReportBuilder](https://developer.apple.com/documentation/deviceactivity/deviceactivityreportbuilder): 하나 이상의 scene을 하나의 scene으로 결합하는 result builder입니다.
:::

:::topic-grid
## 활동 데이터 필터링
- [DeviceActivityFilter](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter): 보고서에 포함할 device activity 데이터를 필터링하는 타입입니다.
- [DeviceActivityData](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata): 특정 기기에서 한 사람의 activity 데이터입니다.
- [DeviceActivityResults](https://developer.apple.com/documentation/deviceactivity/deviceactivityresults): 필터링된 device activity 결과의 비동기 시퀀스입니다.
:::

:::topic-grid
## 접근 권한 승인
- [DeviceActivityAuthorization](https://developer.apple.com/documentation/deviceactivity/deviceactivityauthorization)
- [DeviceActivityAuthorizing](https://developer.apple.com/documentation/deviceactivity/deviceactivityauthorizing)
:::

:::topic-grid
## 오류 처리
- [DeviceActivityCenter.MonitoringError](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror): 활동 모니터링을 시작할 때 발생할 수 있는 오류입니다.
:::
