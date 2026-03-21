---
route: /documentation/apple-silicon
source_url: https://developer.apple.com/documentation/apple-silicon
source_locale: en-US
section: docc
content_type: article
title: Apple silicon
original_title: Apple silicon
source_hash: ee9e9a7ade69df61497f4804aa14db64135a4abd8b9fda540e1d692c57c95cbe
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:41:40+00:00'
last_translated_at: '2026-03-13T23:51:00+09:00'
---

# Apple silicon

Apple silicon이 탑재된 Mac용 소프트웨어를 만드는 데 필요한 리소스를 얻습니다.

## 개요

Apple silicon에서 네이티브로 실행되는 앱, 라이브러리, 프레임워크, 플러그인, 기타 실행 코드를 빌드합니다. Apple 프레임워크와 기술 위에 실행 파일을 빌드하는 경우, 일반적으로 필요한 유일한 중요한 단계는 코드를 `arm64` 아키텍처용으로 다시 컴파일하는 것입니다. 하드웨어별 세부 사항에 의존하거나 저수준 기능에 대해 가정을 하고 있다면, Apple silicon을 지원하도록 필요에 맞게 코드를 수정합니다.

![Apple silicon 로고입니다.](https://developer.apple.com)

Apple silicon에서 최고의 성능을 얻으려면 하드웨어 리소스를 사용하는 방식을 조정해야 하는 경우가 있습니다. 가능하다면 항상 더 높은 수준의 기술을 사용해 하드웨어에 대한 의존성을 최소화합니다. 예를 들어 스레드를 직접 생성하고 관리하는 대신 Grand Central Dispatch를 사용합니다. Apple silicon에서 변경 사항을 테스트해 코드가 최적으로 동작하는지 확인합니다.

:::topic-grid
## 핵심 항목
- [Porting your macOS apps to Apple silicon](https://developer.apple.com/documentation/apple-silicon/porting-your-macos-apps-to-apple-silicon): Apple silicon과 Intel 기반 Mac 모두에서 실행되는 macOS 앱 버전을 만듭니다.
- [Building a universal macOS binary](https://developer.apple.com/documentation/apple-silicon/building-a-universal-macos-binary): Apple silicon과 Intel 기반 Mac 모두에서 네이티브로 실행되는 macOS 앱 및 기타 실행 파일을 만듭니다.
:::

:::topic-grid
## 일반 포팅 팁
- [Addressing architectural differences in your macOS code](https://developer.apple.com/documentation/apple-silicon/addressing-architectural-differences-in-your-macos-code): Apple silicon과 Intel 기반 Mac 컴퓨터 간의 아키텍처 차이에서 비롯되는 문제를 해결합니다.
- [Porting your audio code to Apple silicon](https://developer.apple.com/documentation/apple-silicon/porting-your-audio-code-to-apple-silicon): Apple silicon Mac에서 실행할 때 오디오 전용 코드의 문제를 제거합니다.
- [Porting just-in-time compilers to Apple silicon](https://developer.apple.com/documentation/apple-silicon/porting-just-in-time-compilers-to-apple-silicon): Hardened Runtime capability 및 Apple silicon과 함께 동작하도록 just-in-time(JIT) 컴파일러를 업데이트합니다.
:::

:::topic-grid
## 그래픽
- [Porting your Metal code to Apple silicon](https://developer.apple.com/documentation/apple-silicon/porting-your-metal-code-to-apple-silicon): Apple silicon과 Intel 기반 Mac 모두에서 실행되는 Metal 앱 버전을 만듭니다.
:::

:::topic-grid
## 성능
- [Tuning your code’s performance for Apple silicon](https://developer.apple.com/documentation/apple-silicon/tuning-your-code-s-performance-for-apple-silicon): Apple silicon과 Intel 기반 Mac 모두에서 최고의 성능을 얻도록 코드를 개선합니다.
- [Apple Silicon CPU Optimization Guide Version 4](https://developer.apple.com/documentation/apple-silicon/cpu-optimization-guide): Apple silicon M-series 및 A-series 칩을 위한 성능 최적화 전략을 식별합니다.
:::

:::topic-grid
## Rosetta
- [About the Rosetta translation environment](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment): Rosetta가 실행 파일을 어떻게 번역하는지, 그리고 무엇을 번역할 수 없는지 이해합니다.
:::

:::topic-grid
## Mac에서의 iOS 앱
- [Running your iOS apps in macOS](https://developer.apple.com/documentation/apple-silicon/running-your-ios-apps-in-macos): Mac에서 Apple silicon으로 실행할 iOS 앱을 현대화하거나, 아예 Mac 실행에서 제외합니다.
- [Adapting iOS code to run in the macOS environment](https://developer.apple.com/documentation/apple-silicon/adapting-ios-code-to-run-in-the-macos-environment): Apple silicon에서 실행할 때 더 나은 사용자 경험을 제공하는 최신 iOS 기능을 지원합니다.
- [Providing touch gesture equivalents using Touch Alternatives](https://developer.apple.com/documentation/apple-silicon/providing-touch-gesture-equivalents-using-touch-alternatives): Apple silicon이 탑재된 Mac에서 iOS 앱이 실행될 때 키보드, 마우스, 트랙패드에 대응하는 Touch Alternatives를 제공합니다.
- [Providing an edge-to-edge, full-screen experience in your iPad app running on a Mac](https://developer.apple.com/documentation/apple-silicon/providing-an-edge-to-edge-full-screen-experience-in-your-ipad-app-running-on-a-mac): Mac에서 iPad 앱을 전체 화면으로 실행할 때 Mac 디스플레이의 진정한 네이티브 해상도를 활용합니다.
:::

:::topic-grid
## 커널 및 드라이버
- [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts): 하드웨어와 통신하고 저수준 서비스를 제공하는 드라이버와 시스템 확장을 만들고, 일부 작업에만 kernel extension을 사용합니다.
- [Installing a custom kernel extension](https://developer.apple.com/documentation/apple-silicon/installing-a-custom-kernel-extension): 사용자 정의 installer package를 사용해 kernel extension을 설치하고, 사용자가 설치 과정을 이해하도록 돕습니다.
- [Debugging a custom kernel extension](https://developer.apple.com/documentation/apple-silicon/debugging-a-custom-kernel-extension): 두 번째 Mac에서 사용자 정의 kernel extension을 디버깅할 수 있도록 시스템을 구성합니다.
:::

:::topic-grid
## 보안
- [Improving control flow integrity with pointer authentication](https://developer.apple.com/documentation/apple-silicon/improving-control-flow-integrity-with-pointer-authentication): 코드가 포인터를 올바르게 사용하고 있다는 신뢰를 높입니다.
:::
