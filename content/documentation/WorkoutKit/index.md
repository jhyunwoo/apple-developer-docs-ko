---
route: /documentation/WorkoutKit
source_url: https://developer.apple.com/documentation/WorkoutKit
source_locale: en-US
section: docc
content_type: symbol
title: WorkoutKit
original_title: WorkoutKit
source_hash: ac7a73c43727de0df91da09237e7c8b70afee1f365481008b241d4f5e5af5cc9
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:56:49+00:00'
last_translated_at: '2026-03-14T02:40:00+09:00'
---

# WorkoutKit

운동 구성을 생성하고 미리 보고 Workout 앱과 동기화합니다.

## 개요

WorkoutKit 프레임워크는 iOS 및 watchOS 앱에서 운동을 생성하고 미리 보기 위한 모델과 유틸리티를 제공하며, 예약된 운동을 Apple Watch의 Workout 앱과 동기화할 수 있게 합니다. 이 프레임워크는 다음과 같은 유형의 운동을 지원합니다.

:::term-list
[CustomWorkout](https://developer.apple.com/documentation/workoutkit/customworkout): 사용자 정의 목표와 알림이 들어 있는 단계들의 연속으로 구성된 구조화된 interval 운동입니다.
[SingleGoalWorkout](https://developer.apple.com/documentation/workoutkit/singlegoalworkout): 거리, 에너지, 시간처럼 단일 목표를 가지는 운동입니다.
[PacerWorkout](https://developer.apple.com/documentation/workoutkit/pacerworkout): 거리 목표와 시간 목표를 함께 가지는 운동입니다.
[SwimBikeRunWorkout](https://developer.apple.com/documentation/workoutkit/swimbikerunworkout): 철인 3종 선수가 수영, 자전거, 달리기 활동 사이를 자연스럽게 전환할 수 있게 하는 운동입니다.
:::

이러한 운동 유형 중 하나를 초기화해 운동을 정의합니다. 그런 다음 그 운동을 사용해 [WorkoutPlan](https://developer.apple.com/documentation/workoutkit/workoutplan)을 만들며, 이 객체는 계획을 미리 보고, 동기화하고, 내보내기 위한 메서드를 제공합니다. Apple Watch의 Workout 앱에서 계획을 열려면 [openInWorkoutApp()](https://developer.apple.com/documentation/workoutkit/workoutplan/openinworkoutapp())을 호출합니다. 계획을 내보내려면 `dataRepresentation(as:)` 메서드를 호출합니다.

WorkoutKit을 사용해 운동 일정을 생성하고 유지할 수도 있으며, 사용자의 허가를 받으면 예약된 구성을 Apple Watch와 동기화할 수 있습니다. 이러한 구성은 Workout 앱의 전용 공간에 나타나며 앱 아이콘과 이름을 포함합니다.

운동을 예약하기 전에 먼저 허가를 요청해야 합니다. 공유 [WorkoutScheduler](https://developer.apple.com/documentation/workoutkit/workoutscheduler) 인스턴스를 가져오고 [requestAuthorization()](https://developer.apple.com/documentation/workoutkit/workoutscheduler/requestauthorization()) 메서드를 호출합니다. 그런 다음 [schedule(_:at:)](https://developer.apple.com/documentation/workoutkit/workoutscheduler/schedule(_:at:)) 메서드를 호출해 운동을 예약합니다.

운동에 대한 건강 데이터에 접근하려면 [HealthKit](https://developer.apple.com/documentation/HealthKit) 프레임워크를 참고하십시오.

:::topic-grid
## 기초
- [Customizing workouts with WorkoutKit](https://developer.apple.com/documentation/workoutkit/customizing-workouts-with-workoutkit): Apple Watch의 Workout 앱에서 사용할 운동을 생성하고, 미리 보고, 동기화합니다.
:::

:::topic-grid
## 공통 운동
- [SingleGoalWorkout](https://developer.apple.com/documentation/workoutkit/singlegoalworkout): 단일 목표를 가진 운동입니다.
- [PacerWorkout](https://developer.apple.com/documentation/workoutkit/pacerworkout): 사용자가 주어진 시간 안에 특정 거리를 이동하는 운동입니다.
- [SwimBikeRunWorkout](https://developer.apple.com/documentation/workoutkit/swimbikerunworkout): 달리기, 자전거, 수영을 포함하는 multisport 활동을 위한 운동입니다.
:::

:::topic-grid
## 사용자 정의 interval 운동
- [CustomWorkout](https://developer.apple.com/documentation/workoutkit/customworkout): 작업 단계와 회복 단계가 반복되는 운동입니다.
- [WorkoutStep](https://developer.apple.com/documentation/workoutkit/workoutstep): 운동의 한 단계입니다.
- [IntervalBlock](https://developer.apple.com/documentation/workoutkit/intervalblock): 사용자 정의 운동 안에서 반복되는 작업 단계와 회복 단계의 block입니다.
- [IntervalStep](https://developer.apple.com/documentation/workoutkit/intervalstep): 운동의 작업 단계 또는 회복 단계를 나타내는 interval입니다.
- [WorkoutGoal](https://developer.apple.com/documentation/workoutkit/workoutgoal): 운동의 목표를 지정하는 값입니다.
- [WorkoutAlert](https://developer.apple.com/documentation/workoutkit/workoutalert): 운동 중 중요한 이벤트를 사용자에게 알리는 alert입니다.
:::

:::topic-grid
## 운동 계획과 일정
- [WorkoutPlan](https://developer.apple.com/documentation/workoutkit/workoutplan): 앱이 운동 객체를 Workout에서 열거나 나중을 위해 예약하는 데 사용할 수 있는 wrapper입니다.
- [ScheduledWorkoutPlan](https://developer.apple.com/documentation/workoutkit/scheduledworkoutplan): 앱이 운동 계획을 예약하는 데 사용할 수 있는 운동 계획 wrapper입니다.
- [WorkoutScheduler](https://developer.apple.com/documentation/workoutkit/workoutscheduler): 운동을 예약하고 관리하는 객체입니다.
:::

:::topic-grid
## 오류
- [StateError](https://developer.apple.com/documentation/workoutkit/stateerror): 운동 구성을 미리 보는 동안 발생하는 오류입니다.
:::
