---
route: /documentation/Xcode/swift-packages
source_url: https://developer.apple.com/documentation/Xcode/swift-packages
source_locale: en-US
section: docc
content_type: article
title: Swift packages
original_title: Swift packages
source_hash: f00ae75c706001347939887011fc8063968cfbb22d2ad0e3c5cae44821f333e2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:54:03+00:00'
last_translated_at: '2026-03-14T02:30:00+09:00'
---

# Swift packages

재사용 가능한 코드를 만들고, 이를 가볍게 구성하며, Xcode 프로젝트 전반과 다른 개발자와 공유합니다.

## 개요

![Xcode가 코드, 리소스, 바이너리를 Swift package로 묶는 방식을 지원하는 모습을 설명하는 이미지입니다.](https://developer.apple.com)

Swift package는 개발자가 프로젝트에서 사용할 수 있는 Swift, Objective-C, Objective-C++, C, C++ 코드의 재사용 가능한 구성 요소입니다. source 파일, binary, resource를 앱 프로젝트에서 쉽게 사용할 수 있는 방식으로 묶어 제공합니다.

Xcode는 Swift package의 생성과 배포뿐 아니라 package dependency의 추가, 제거, 관리도 지원합니다. Swift package 지원은 오픈 소스 Swift Package Manager 프로젝트 위에 구축되어 있습니다.

package manifest에서 사용하는 API에 대해 더 알아보려면 [Package](https://developer.apple.com/documentation/PackageDescription/Package)를 참고하십시오. Swift Package Manager에 대해 더 알아보려면 [Swift.org](https://swift.org/package-manager/)와 오픈 소스 [Swift Package Manager repository](https://github.com/apple/swift-package-manager)를 참고하십시오.

:::topic-grid
## 패키지 의존성
- [Adding package dependencies to your app](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app): 프로젝트 간 코드를 공유하거나 다른 개발자의 코드를 활용하기 위해 package dependency를 통합합니다.
- [Identifying binary dependencies](https://developer.apple.com/documentation/xcode/identifying-binary-dependencies): package dependency가 binary를 참조하는지 확인하고 그 binary의 진위를 검증합니다.
- [Editing a package dependency as a local package](https://developer.apple.com/documentation/xcode/editing-a-package-dependency-as-a-local-package): package dependency를 local package로 추가해 override하고 그 내용을 편집합니다.
:::

:::topic-grid
## 패키지 생성
- [Creating a standalone Swift package with Xcode](https://developer.apple.com/documentation/xcode/creating-a-standalone-swift-package-with-xcode): 실행 가능한 코드나 공유 가능한 코드를 독립적인 Swift package로 묶습니다.
- [Bundling resources with a Swift package](https://developer.apple.com/documentation/xcode/bundling-resources-with-a-swift-package): Swift package에 resource 파일을 추가하고 코드에서 접근합니다.
- [Localizing package resources](https://developer.apple.com/documentation/xcode/localizing-package-resources): Swift package가 여러 locale용 localized resource를 제공하도록 구성합니다.
- [Distributing binary frameworks as Swift packages](https://developer.apple.com/documentation/xcode/distributing-binary-frameworks-as-swift-packages): 하나 이상의 XCFramework를 포함하는 Swift package를 만들어 binary를 다른 개발자에게 제공합니다.
- [Developing a Swift package in tandem with an app](https://developer.apple.com/documentation/xcode/developing-a-swift-package-in-tandem-with-an-app): 배포한 Swift package를 앱 프로젝트에 local package로 추가하고 package와 앱을 함께 개발합니다.
- [Organizing your code with local packages](https://developer.apple.com/documentation/xcode/organizing-your-code-with-local-packages): 앱 코드를 local Swift package로 구성해 유지 보수를 단순화하고, 모듈성을 높이며, 재사용을 장려합니다.
- [PackageDescription](https://developer.apple.com/documentation/PackageDescription): 재사용 가능한 코드를 만들고, 가볍게 구성하며, 프로젝트 전반과 다른 개발자와 공유합니다.
:::

:::topic-grid
## 패키지 배포
- [Publishing a Swift package with Xcode](https://developer.apple.com/documentation/xcode/publishing-a-swift-package-with-xcode): Swift package를 비공개로 배포하거나 다른 개발자에게 전 세계적으로 공유합니다.
:::

:::topic-grid
## 지속적 통합
- [Building Swift packages or apps that use them in continuous integration workflows](https://developer.apple.com/documentation/xcode/building-swift-packages-or-apps-that-use-them-in-continuous-integration-workflows): 기존 continuous integration 설정으로 Swift package를 빌드하고, 기존 CI pipeline 안에서 package dependency를 사용하는 앱을 준비합니다.
:::
