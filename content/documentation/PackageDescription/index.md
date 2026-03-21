---
route: /documentation/PackageDescription
source_url: https://developer.apple.com/documentation/PackageDescription
source_locale: en-US
section: docc
content_type: symbol
title: PackageDescription
original_title: PackageDescription
source_hash: 806d41f66ebe04724a0b45dde9b3054b3868d4f7cfd7a2d2eda73c8875006eb3
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:51+00:00'
last_translated_at: '2026-03-13T18:25:00+09:00'
---

# PackageDescription

재사용 가능한 코드를 만들고, 가볍게 구성하며, 프로젝트와 다른 개발자와 공유합니다.

## 개요

Swift 패키지는 개발자가 자신의 프로젝트에서 사용할 수 있는 Swift, Objective-C, Objective-C++, C, 또는 C++ 코드의 재사용 가능한 구성 요소입니다. 소스 파일, 바이너리, 리소스를 앱 프로젝트에서 쉽게 사용할 수 있는 방식으로 묶어 제공합니다.

각 Swift 패키지는 패키지의 기본 디렉터리에 `Package.swift` 파일이 필요하며, 이를 패키지 매니페스트라고 부릅니다. Swift 패키지를 만들 때는 패키지 매니페스트에서 PackageDescription 라이브러리를 사용해 의존성을 나열하고, 지역화된 리소스를 구성하며, 그 밖의 구성 옵션을 설정합니다.

예를 들어 아래의 [SlothCreator: Building DocC Documentation in Xcode](https://developer.apple.com/documentation/xcode/slothcreator_building_docc_documentation_in_xcode) 샘플 프로젝트에 있는 패키지 매니페스트는 SlothCreator 패키지를 정의하며, 그 안에 SlothCreator 라이브러리를 포함합니다. 또한 배포 타깃과 리소스가 `Resources` 폴더에 있음을 지정합니다.

```swift
import PackageDescription

let package = Package(
    name: "SlothCreator",
    platforms: [
        .macOS(.v11),
        .iOS(.v14),
        .watchOS(.v7),
        .tvOS(.v13)
    ],
    products: [
        .library(
            name: "SlothCreator",
            targets: ["SlothCreator"]
        )
    ],
    targets: [
        .target(
            name: "SlothCreator",
            resources: [
                .process("Resources/")
            ]
        )
    ]
)
```

패키지 매니페스트를 사용하면 실행 파일 제품도 정의할 수 있으며, Swift Package Manager가 매니페스트의 다른 제품을 빌드하는 데 사용할 플러그인도 정의할 수 있습니다.

앱 프로젝트에 패키지 의존성을 추가하는 방법과 Xcode로 Swift 패키지를 만드는 방법에 대한 자세한 내용은 [Adding Package Dependencies to Your App](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app), [Creating a Standalone Swift Package with Xcode](https://developer.apple.com/documentation/xcode/creating-a-standalone-swift-package-with-xcode), [Swift Packages](https://developer.apple.com/documentation/xcode/swift-packages)를 참고하십시오.

Xcode의 Swift 패키지 지원은 오픈 소스 Swift Package Manager 프로젝트를 기반으로 합니다. Swift Package Manager에 대해 더 알아보려면 [Swift.org](https://www.swift.org/package-manager/)와 [GitHub](https://github.com/swiftlang/swift-package-manager)의 Swift Package Manager 저장소를 방문하십시오.

:::topic-grid
## 패키지 생성
- [Package](https://developer.apple.com/documentation/packagedescription/package): Swift 패키지의 구성입니다.
- [Context](https://developer.apple.com/documentation/packagedescription/context): Swift 패키지의 컨텍스트 정보입니다.
:::

:::topic-grid
## 구조체
- [GitInformation](https://developer.apple.com/documentation/packagedescription/gitinformation): 사용할 수 있는 경우 지정된 패키지의 git 상태 정보입니다.
- [Version](https://developer.apple.com/documentation/packagedescription/version): 시맨틱 버전 규칙에 따른 버전입니다.
:::

:::topic-grid
## 열거형
- [WarningLevel](https://developer.apple.com/documentation/packagedescription/warninglevel): 컴파일러 경고를 어떻게 취급할지 나타내는 수준입니다.
:::
