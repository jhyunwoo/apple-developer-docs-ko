---
route: /documentation/BackgroundTasks
source_url: https://developer.apple.com/documentation/BackgroundTasks
source_locale: en-US
section: docc
content_type: symbol
title: Background Tasks
original_title: Background Tasks
source_hash: e2bc94848bd28dfe7fb3d65b41641705d648189d245c2a7d1763c0a59ce5c94f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:34+00:00'
last_translated_at: '2026-03-13T17:10:00+09:00'
---

# Background Tasks

앱의 가장 중요한 작업을 프레임워크가 제공하는 task로 감싸 앱에서 백그라운드 처리를 지원합니다.

## 개요

이 프레임워크를 사용하면 앱이 백그라운드에 있어도 앱 콘텐츠를 최신 상태로 유지하고 완료까지 몇 분이 걸리는 작업을 실행할 수 있습니다. 더 긴 작업은 지원되는 기기에서 외부 전원, 네트워크 연결, GPU를 활용할 수 있습니다.

앱을 백그라운드에서 실행해 필요한 작업을 수행하려면 프레임워크 제공 task에 대한 launch handler를 등록하고 필요에 따라 task를 예약하십시오.

사용자가 작업이 끝나기 전에 앱을 백그라운드로 보내는 경우, 앱은 프레임워크 제공 task를 사용해 포그라운드에서 중요한 작업을 실행하고 이를 백그라운드에서 마무리할 수도 있습니다.

:::topic-grid
## 핵심 사항
- [Background Tasks updates](https://developer.apple.com/documentation/Updates/BackgroundTasks): Background Tasks의 중요한 변경 사항을 알아봅니다.
- [BGTaskScheduler](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler): 앱의 가장 중요한 작업에 백그라운드 지원을 추가하는 task를 예약하는 클래스입니다.
- [BGTask](https://developer.apple.com/documentation/backgroundtasks/bgtask): 프레임워크 task를 위한 추상 클래스입니다.
:::

:::topic-grid
## 백그라운드 task
- [Using background tasks to update your app](https://developer.apple.com/documentation/UIKit/using-background-tasks-to-update-your-app): 처리 시간과 전력을 효율적으로 사용하기 위해 앱이 백그라운드에서 task를 수행하도록 구성합니다.
- [Refreshing and Maintaining Your App Using Background Tasks](https://developer.apple.com/documentation/backgroundtasks/refreshing-and-maintaining-your-app-using-background-tasks): 예약된 백그라운드 task를 사용해 앱 콘텐츠를 새로 고치고 유지 관리 작업을 수행합니다.
- [Choosing Background Strategies for Your App](https://developer.apple.com/documentation/backgroundtasks/choosing-background-strategies-for-your-app): 앱의 백그라운드 실행 시간을 예약하는 최선의 방법을 선택합니다.
- [BGProcessingTask](https://developer.apple.com/documentation/backgroundtasks/bgprocessingtask): 앱이 백그라운드에 있는 동안 실행되는 시간이 오래 걸리는 처리 task입니다.
- [BGAppRefreshTask](https://developer.apple.com/documentation/backgroundtasks/bgapprefreshtask): 일반적으로 앱이 백그라운드에 있을 때 콘텐츠를 새로 고치는 데 사용하는 짧은 task를 나타내는 객체입니다.
- [BGHealthResearchTask](https://developer.apple.com/documentation/backgroundtasks/bghealthresearchtask): 사용자가 참여하는 건강 연구에 필수적인 데이터를 준비하기 위해 앱이 백그라운드에 있는 동안 실행되는 시간이 오래 걸리는 필수 처리 task입니다.
:::

:::topic-grid
## 백그라운드 지원을 갖춘 포그라운드 task
- [Performing long-running tasks on iOS and iPadOS](https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados): 필요에 따라 완료될 수 있는 작업을 위해 연속 백그라운드 task를 사용합니다.
- [BGContinuedProcessingTask](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask): 포그라운드에서 시작해 필요에 따라 백그라운드에서 계속 실행할 수 있는 task입니다.
- [Background GPU Access](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.background-tasks.continued-processing.gpu): 연속 백그라운드 task가 GPU를 사용하기 위해 시스템이 요구하는 entitlement입니다.
:::

:::topic-grid
## task 요청
- [BGProcessingTaskRequest](https://developer.apple.com/documentation/backgroundtasks/bgprocessingtaskrequest): 완료까지 몇 분이 걸릴 수 있는 처리 task를 실행하기 위해 앱을 백그라운드에서 시작하는 요청입니다.
- [BGAppRefreshTaskRequest](https://developer.apple.com/documentation/backgroundtasks/bgapprefreshtaskrequest): 짧은 새로 고침 task를 실행하기 위해 앱을 백그라운드에서 시작하는 요청입니다.
- [BGTaskRequest](https://developer.apple.com/documentation/backgroundtasks/bgtaskrequest): task 요청을 표현하는 추상 클래스입니다.
- [BGHealthResearchTaskRequest](https://developer.apple.com/documentation/backgroundtasks/bghealthresearchtaskrequest): 사용자가 참여하는 건강 연구의 처리를 실행하기 위해 앱을 백그라운드에서 시작하는 요청입니다.
- [BGContinuedProcessingTaskRequest](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest): 사용자가 앱을 백그라운드로 보내더라도 시스템이 계속 처리하는 워크로드에 대한 요청입니다.
:::

:::topic-grid
## 개발 및 테스트
- [Starting and Terminating Tasks During Development](https://developer.apple.com/documentation/backgroundtasks/starting-and-terminating-tasks-during-development): 개발 중 디버거를 사용해 task를 시작하고 완료 전에 종료합니다.
:::
