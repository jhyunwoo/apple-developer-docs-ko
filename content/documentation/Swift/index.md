---
route: /documentation/Swift
source_url: https://developer.apple.com/documentation/Swift
source_locale: en-US
section: docc
content_type: symbol
title: Swift
original_title: Swift
source_hash: 4bae2c1e3efc5d7a34ec2c859f3b142ec8485b466406226088d9590541b75a7c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:25:09+00:00'
last_translated_at: '2026-03-13T19:50:00+09:00'
---

# Swift

강력하고 개방적인 언어를 사용해 앱을 만듭니다.

## 개요

Swift에는 타입 추론, optional, closure 같은 현대적인 기능이 포함되어 있어 문법이 간결하면서도 표현력이 풍부합니다. Swift는 코드가 빠르고 효율적으로 동작하도록 보장하며, 메모리 안전성과 기본 오류 처리를 통해 언어 자체가 안전하도록 설계되었습니다. Swift Playgrounds, Xcode의 playground, REPL에서는 Swift 코드를 상호작용적으로 즐겁게 작성할 수 있습니다.

```swift
var interestingNumbers = [
    "primes": [2, 3, 5, 7, 11, 13, 17],
    "triangular": [1, 3, 6, 10, 15, 21, 28],
    "hexagonal": [1, 6, 15, 28, 45, 66, 91]
]

for key in interestingNumbers.keys {
    interestingNumbers[key]?.sort(by: >)
}

print(interestingNumbers["primes"]!)
// Prints "[17, 13, 11, 7, 5, 3, 2]"
```

### Swift 배우기

Swift가 처음이라면 [The Swift Programming Language](https://docs.swift.org/swift-book/)를 읽고 빠른 둘러보기, 포괄적인 언어 가이드, 전체 레퍼런스 매뉴얼을 확인하십시오. 프로그래밍이 처음이라면 iPad의 [Swift Playgrounds](https://www.apple.com/swift/playgrounds/)를 확인해 보십시오.

Swift는 공개적으로 개발됩니다. 오픈 소스 Swift 프로젝트와 커뮤니티에 대해 더 알아보려면 [Swift.org](https://swift.org)를 방문하십시오.

:::topic-grid
## 핵심 사항
- [Swift updates](https://developer.apple.com/documentation/Updates/Swift): Swift의 중요한 변경 사항을 알아봅니다.
- [Adopting strict concurrency in Swift 6 apps](https://developer.apple.com/documentation/swift/adoptingswift6): 컴파일 타임에 데이터 레이스를 찾기 위해 strict concurrency 검사를 활성화합니다.
:::

:::topic-grid
## 표준 라이브러리
- [Int](https://developer.apple.com/documentation/swift/int): 부호 있는 정수 값 타입입니다.
- [Double](https://developer.apple.com/documentation/swift/double): 배정밀도(64비트) 부동소수점 값 타입입니다.
- [String](https://developer.apple.com/documentation/swift/string): 문자 모음으로 이루어진 Unicode 문자열 값입니다.
- [Array](https://developer.apple.com/documentation/swift/array): 순서가 있고 임의 접근이 가능한 컬렉션입니다.
- [Dictionary](https://developer.apple.com/documentation/swift/dictionary): 요소가 키-값 쌍으로 이루어진 컬렉션입니다.
- [Swift Standard Library](https://developer.apple.com/documentation/swift/swift-standard-library): 복잡한 문제를 해결하고 고성능이며 읽기 쉬운 코드를 작성합니다.
:::

:::topic-grid
## Observation
- [Observation](https://developer.apple.com/documentation/swift#Observation)
:::

:::topic-grid
## 분산 액터
- [Distributed](https://developer.apple.com/documentation/distributed): 여러 프로세스와 기기에서 분산 코드를 실행하는 시스템을 구축합니다.
:::

:::topic-grid
## 정규식 DSL
- [RegexBuilder](https://developer.apple.com/documentation/regexbuilder): 텍스트 검색과 치환 같은 작업을 위해 표현력 있는 도메인 특화 언어로 정규식을 구축합니다.
:::

:::topic-grid
## 저수준 원자적 연산
- [Synchronization](https://developer.apple.com/documentation/synchronization): 저수준의 기본 연산을 사용해 동기화 구조를 구축합니다.
:::

:::topic-grid
## 데이터 모델링
- [Choosing Between Structures and Classes](https://developer.apple.com/documentation/swift/choosing-between-structures-and-classes): 데이터를 저장하고 동작을 모델링하는 방법을 결정합니다.
- [Adopting Common Protocols](https://developer.apple.com/documentation/swift/adopting-common-protocols): 사용자 정의 타입이 Swift 프로토콜을 따르도록 하여 더 쉽게 사용할 수 있게 합니다.
:::

:::topic-grid
## 데이터 흐름과 제어 흐름
- [Maintaining State in Your Apps](https://developer.apple.com/documentation/swift/maintaining-state-in-your-apps): 열거형을 사용해 앱의 상태를 포착하고 추적합니다.
- [Preventing Timing Problems When Using Closures](https://developer.apple.com/documentation/swift/preventing-timing-problems-when-using-closures): closure에 대한 서로 다른 API 호출이 앱에 어떤 영향을 주는지 이해합니다.
:::

:::topic-grid
## Objective-C 및 C와의 언어 상호 운용성
- [Objective-C and C Code Customization](https://developer.apple.com/documentation/swift/objective-c-and-c-code-customization): Objective-C API에 매크로를 적용하여 Swift로 import되는 방식을 사용자화합니다.
- [Migrating Your Objective-C Code to Swift](https://developer.apple.com/documentation/swift/migrating-your-objective-c-code-to-swift): 코드를 마이그레이션하는 권장 단계를 알아봅니다.
- [Cocoa Design Patterns](https://developer.apple.com/documentation/swift/cocoa-design-patterns): Swift 앱에서 Cocoa 디자인 패턴을 채택하고 상호 운용합니다.
- [Handling Dynamically Typed Methods and Objects in Swift](https://developer.apple.com/documentation/swift/handling-dynamically-typed-methods-and-objects-in-swift): Objective-C 타입의 인스턴스를 특정 Swift 타입으로 캐스팅합니다.
- [Using Objective-C Runtime Features in Swift](https://developer.apple.com/documentation/swift/using-objective-c-runtime-features-in-swift): selector와 key path를 사용해 동적인 Objective-C API와 상호 작용합니다.
- [Imported C and Objective-C APIs](https://developer.apple.com/documentation/swift/imported-c-and-objective-c-apis): C와 Objective-C의 타입 및 함수와 상호 운용하기 위해 네이티브 Swift 문법을 사용합니다.
- [Calling Objective-C APIs Asynchronously](https://developer.apple.com/documentation/swift/calling-objective-c-apis-asynchronously): completion handler를 받는 함수와 메서드가 Swift 비동기 함수로 어떻게 변환되는지 알아봅니다.
:::

:::topic-grid
## C++와의 언어 상호 운용성
- [Mixing Languages in an Xcode project](https://developer.apple.com/documentation/swift/mixinglanguagesinanxcodeproject): 단일 framework target에서 Swift와 C++ API를 함께 사용하고, 별도의 앱 target에서 framework API를 소비합니다.
- [Calling APIs Across Language Boundaries](https://developer.apple.com/documentation/swift/callingapisacrosslanguageboundaries): Xcode 프로젝트의 여러 target과 framework 전반에서 다양한 C++ API를 Swift에서 사용하고 그 반대도 수행합니다.
:::
