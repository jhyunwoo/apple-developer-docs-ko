---
route: /documentation/Observation
source_url: https://developer.apple.com/documentation/Observation
source_locale: en-US
section: docc
content_type: symbol
title: Observation
original_title: Observation
source_hash: ce47065b5cc2a85d864827e0b26d25a7760eb0d11d22aa6b007fd182d63172ff
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:07:35+00:00'
last_translated_at: '2026-03-14T03:28:00+09:00'
---

# Observation

기반 데이터가 바뀔 때 표시가 업데이트되는 반응형 앱을 만듭니다.

## 개요

Observation은 Swift에서 observer 디자인 패턴을 견고하고 타입 안전하며 성능 좋게 구현한 프레임워크입니다. 이 패턴을 사용하면 관찰 가능한 객체가 observer 목록을 유지하고 특정 상태 변화 또는 일반 상태 변화를 알려 줄 수 있습니다. 이 방식은 객체를 직접 결합하지 않아도 되고, 잠재적으로 여러 observer에 걸쳐 업데이트를 암묵적으로 배포할 수 있다는 장점이 있습니다.

Observation 프레임워크는 다음 기능을 제공합니다.

- 타입을 observable로 표시하기
- observable 타입 인스턴스 내부의 변화를 추적하기
- 앱의 사용자 인터페이스 같은 다른 곳에서 그 변화를 관찰하고 활용하기

타입을 observable로 선언하려면 타입 선언에 [Observable()](https://developer.apple.com/documentation/observation/observable()) macro를 붙입니다. 이 macro는 컴파일 시점에 해당 타입에 [Observable](https://developer.apple.com/documentation/observation/observable) protocol 준수를 선언하고 구현합니다.

```swift
@Observable
class Car {
    var name: String = ""
    var needsRepairs: Bool = false
    
    init(name: String, needsRepairs: Bool = false) {
        self.name = name
        self.needsRepairs = needsRepairs
    }
}
```

변화를 추적하려면 [withObservationTracking(_:onChange:)](https://developer.apple.com/documentation/observation/withobservationtracking(_:onchange:)) 함수를 사용합니다. 예를 들어 다음 코드에서 이 함수는 차의 이름이 바뀔 때 `onChange` closure를 호출합니다. 하지만 차의 `needsRepair` 플래그가 바뀌어도 closure는 호출하지 않습니다. 그 이유는 이 함수가 `apply` closure 안에서 읽은 property만 추적하고, 그 closure는 `needsRepair` property를 읽지 않기 때문입니다.

```swift
func render() {
    withObservationTracking {
        for car in cars {
            print(car.name)
        }
    } onChange: {
        print("Schedule renderer.")
    }
}
```

:::topic-grid
## Observable 준수
- [Observable()](https://developer.apple.com/documentation/observation/observable()): Observable protocol에 대한 준수를 정의하고 구현합니다.
- [Observable](https://developer.apple.com/documentation/observation/observable): 기반 데이터가 바뀔 때 observer에게 알림을 방출하는 타입입니다.
:::

:::topic-grid
## 변경 추적
- [withObservationTracking(_:onChange:)](https://developer.apple.com/documentation/observation/withobservationtracking(_:onchange:)): property에 대한 접근을 추적합니다.
- [ObservationRegistrar](https://developer.apple.com/documentation/observation/observationregistrar): 데이터 변화 추적과 접근을 위한 저장소를 제공합니다.
:::

:::topic-grid
## SwiftUI에서의 Observation
- [Managing model data in your app](https://developer.apple.com/documentation/SwiftUI/Managing-model-data-in-your-app): 앱의 데이터 모델과 view 사이에 연결을 만듭니다.
- [Migrating from the Observable Object protocol to the Observable macro](https://developer.apple.com/documentation/SwiftUI/Migrating-from-the-observable-object-protocol-to-the-observable-macro): 기존 앱을 업데이트해 Swift Observation의 이점을 활용합니다.
:::

:::topic-grid
## 구조체
- [Observations](https://developer.apple.com/documentation/observation/observations): 타입의 트랜잭션 변화를 추적하는 closure에서 생성되는 비동기 시퀀스입니다.
:::

:::topic-grid
## Macro
- [ObservationIgnored()](https://developer.apple.com/documentation/observation/observationignored()): property에 대한 observation 추적을 비활성화합니다.
- [ObservationTracked()](https://developer.apple.com/documentation/observation/observationtracked()): 접근자를 위한 property를 합성합니다.
:::
