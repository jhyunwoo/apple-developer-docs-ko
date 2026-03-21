---
route: /documentation/Xcode/Xcode-Cloud
source_url: https://developer.apple.com/documentation/Xcode/Xcode-Cloud
source_locale: en-US
section: docc
content_type: article
title: Xcode Cloud
original_title: Xcode Cloud
source_hash: 13fe676a48824ad6304c9a5d11837b228b90f63f454720b43f451eb7a127b6cb
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:21:30+00:00'
last_translated_at: '2026-03-14T01:05:00+09:00'
---

# Xcode Cloud

Xcode Cloud로 앱을 자동으로 빌드, 테스트, 배포하여 변경 사항을 검증하고 고품질 앱을 만듭니다.

## 개요

Xcode Cloud를 사용하면 *지속적 통합 및 전달*(CI/CD)을 도입할 수 있습니다. 이는 코드를 개발하고 유지하며 테스터와 사용자에게 앱을 전달하는 데 도움을 주는 표준 소프트웨어 개발 방식입니다. Xcode Cloud는 Apple 플랫폼용 앱과 프레임워크를 만들 때 사용하는 도구들인 [Xcode](https://developer.apple.com/xcode/), [TestFlight](https://developer.apple.com/testflight/), [App Store Connect](https://appstoreconnect.apple.com)를 결합한 CI/CD 시스템입니다.

![Xcode Cloud가 프로젝트를 빌드하고 다양한 기기에 앱을 배포하는 방식을 보여 주는 개념 일러스트입니다.](https://developer.apple.com)

Xcode Cloud를 사용하면 다음을 자동으로, 그리고 자주 수행할 수 있습니다.

- 프로젝트를 빌드합니다.
- 테스트를 실행하고 검증을 수행합니다.
- [TestFlight](https://developer.apple.com/testflight/)를 사용해 빌드를 테스터에게 배포하고 피드백을 수집하면서 사용자 개인정보를 보호합니다.

Xcode Cloud와 TestFlight로 앱의 새 버전을 성공적으로 검증한 뒤에는, App Store에 빠르게 출시할 수 있습니다.

지속적 통합 및 전달에 대한 자세한 내용은 [About continuous integration and delivery with Xcode Cloud](https://developer.apple.com/documentation/xcode/about-continuous-integration-and-delivery-with-xcode-cloud)를 참고하십시오. 프로젝트나 workspace를 Xcode Cloud에 맞게 구성하는 방법은 [Configuring your first Xcode Cloud workflow](https://developer.apple.com/documentation/xcode/configuring-your-first-xcode-cloud-workflow)를 참고하십시오.

:::note 참고
WWDC21과 WWDC22의 비디오를 포함한 Xcode Cloud 추가 정보는 [The Xcode Cloud toolkit](https://developer.apple.com/news/?id=076p6dmy)을 참고하십시오.
:::

:::topic-grid
## 핵심 사항
- [Getting started with Xcode Cloud](https://developer.apple.com/documentation/xcode/getting-started-with-xcode-cloud): 프로젝트를 지속적 통합, 개발, 배포용 Xcode Cloud에 설정하는 빠른 시작 가이드입니다.
- [About continuous integration and delivery with Xcode Cloud](https://developer.apple.com/documentation/xcode/about-continuous-integration-and-delivery-with-xcode-cloud): Xcode Cloud를 활용한 지속적 통합 및 전달이 고품질 앱과 프레임워크 제작에 어떻게 도움이 되는지 알아봅니다.
- [Setting up your project to use Xcode Cloud](https://developer.apple.com/documentation/xcode/setting-up-your-project-to-use-xcode-cloud): 프로젝트나 workspace를 Xcode Cloud에 맞게 구성하기 전에 필요한 계정, 프로젝트, 소스 제어 요구 사항을 검토합니다.
- [Configuring your first Xcode Cloud workflow](https://developer.apple.com/documentation/xcode/configuring-your-first-xcode-cloud-workflow): 프로젝트나 workspace를 Xcode Cloud에 맞게 설정하고 지속적 통합 및 전달을 도입합니다.
:::

:::topic-grid
## 설정 및 유지 보수
- [Making dependencies available to Xcode Cloud](https://developer.apple.com/documentation/xcode/making-dependencies-available-to-xcode-cloud): 프로젝트를 Xcode Cloud에 구성하기 전에 의존성을 검토하고 Xcode Cloud에서 사용할 수 있게 합니다.
- [Configuring Xcode Cloud for your team](https://developer.apple.com/documentation/xcode/configuring-xcode-cloud-for-your-team): 팀 단위로 Xcode Cloud의 지속적 통합 및 전달을 시작합니다.
- [Sharing macOS and Xcode versions across Xcode Cloud workflows](https://developer.apple.com/documentation/xcode/sharing-custom-aliases-across-xcode-cloud-workflows): 사용자 정의 alias를 사용해 여러 workflow 간에 구성을 공유합니다.
- [Sharing environment variables across Xcode Cloud workflows](https://developer.apple.com/documentation/xcode/sharing-environment-variables-across-xcode-cloud-workflows): 공유 environment variable을 사용해 여러 workflow에 공통 구성을 적용합니다.
- [Building Swift packages and Swift Playgrounds app projects with Xcode Cloud](https://developer.apple.com/documentation/xcode/building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud): Swift package나 Swift Playgrounds 앱 프로젝트를 Xcode 프로젝트에 추가해 Xcode Cloud에서 빌드합니다.
- [Setting the next build number for Xcode Cloud builds](https://developer.apple.com/documentation/xcode/setting-the-next-build-number-for-xcode-cloud-builds): 기존 Mac 앱의 버전 충돌을 피하기 위해 사용자 정의 빌드 번호부터 번호 매기기를 시작합니다.
- [Including notes for testers with a beta release of your app](https://developer.apple.com/documentation/xcode/including-notes-for-testers-with-a-beta-release-of-your-app): Xcode 프로젝트에 텍스트 파일을 추가해 베타 테스터에게 테스트 포인트를 전달합니다.
- [Removing your project from Xcode Cloud](https://developer.apple.com/documentation/xcode/removing-your-project-from-xcode-cloud): 프로젝트를 Xcode Cloud에서 제거하여 앱 및 workflow 데이터를 삭제하고, Git 저장소 연결과 Slack 통합을 해제합니다.
- [Changing the bundle identifier](https://developer.apple.com/documentation/xcode/changing-the-bundle-identifier): 앱의 bundle identifier를 수정하고 나타나는 모든 위치를 갱신합니다.
:::

:::topic-grid
## 사용량 데이터
- [Reviewing Xcode Cloud usage data](https://developer.apple.com/documentation/xcode/reviewing-xcode-cloud-usage-data): 나와 팀이 Xcode Cloud를 어떻게 사용하는지 이해하기 위해 사용량 정보를 확인합니다.
:::

:::topic-grid
## Workflow
- [Developing a workflow strategy for Xcode Cloud](https://developer.apple.com/documentation/xcode/developing-a-workflow-strategy-for-xcode-cloud): 지속적 통합 및 전달 방식을 다듬기 위해 사용자 정의 Xcode Cloud workflow를 가장 잘 만드는 방법을 검토합니다.
- [Xcode Cloud workflow reference](https://developer.apple.com/documentation/xcode/xcode-cloud-workflow-reference): 메타데이터, 시작 조건, action, post-action 등을 구성해 사용자 정의 Xcode Cloud workflow를 만듭니다.
- [Creating a workflow that builds your app for distribution](https://developer.apple.com/documentation/xcode/creating-a-workflow-that-builds-your-app-for-distribution): 앱을 TestFlight 테스터용, App Store용, 또는 notarized 앱용으로 빌드하고 서명하는 workflow를 구성합니다.
- [Understanding Xcode Cloud infrastructure validation builds](https://developer.apple.com/documentation/xcode/understanding-infrastructure-validation-builds): infrastructure validation build가 무엇인지, 옵트아웃이 필요한지 알아봅니다.
:::

:::topic-grid
## 소스 코드 관리
- [Source code management setup](https://developer.apple.com/documentation/xcode/source-code-management-setup): Xcode Cloud가 Git 저장소에 접근할 수 있게 합니다.
- [Configuring requirements for merging a pull request](https://developer.apple.com/documentation/xcode/configuring-requirements-for-merging-a-pull-request): pull request를 병합하기 전에 성공적인 Xcode Cloud 빌드나 action을 요구하여 안정적인 브랜치를 보호합니다.
:::

:::topic-grid
## 사용자 정의 빌드 스크립트
- [Writing custom build scripts](https://developer.apple.com/documentation/xcode/writing-custom-build-scripts): 사용자 정의 작업을 수행하거나 추가 도구를 설치하는 build script로 Xcode Cloud workflow를 확장합니다.
- [Environment variable reference](https://developer.apple.com/documentation/xcode/environment-variable-reference): 사용자 정의 build script에서 사용하는 사전 정의된 environment variable을 검토합니다.
:::

:::topic-grid
## 문제 해결
- [Resolving common configuration and build issues](https://developer.apple.com/documentation/xcode/resolving-common-configuration-and-build-issues): 일반적인 구성 및 빌드 문제를 검토하고 해결 방법을 알아봅니다.
- [Resolve GitHub Enterprise connection issues](https://developer.apple.com/documentation/xcode/resolve-github-enterprise-connection-issues): Xcode Cloud가 GitHub Enterprise 저장소에 접근할 수 있는지 확인하고 구성 문제를 수정합니다.
- [Reporting feedback for Xcode Cloud](https://developer.apple.com/documentation/xcode/reporting-feedback-for-xcode-cloud): Xcode Cloud로 빌드하면서 겪는 문제에 대한 피드백을 제공합니다.
:::

:::topic-grid
## 알림
- [Configuring webhooks in Xcode Cloud](https://developer.apple.com/documentation/xcode/configuring-webhooks-in-xcode-cloud): Xcode Cloud를 다른 서비스와 도구에 연결하는 webhook을 구성합니다.
- [Xcode Cloud webhook payload reference](https://developer.apple.com/documentation/xcode/webhook-payload): 제품, workflow, build, action, 결과, SCM 메타데이터를 포함해 Xcode Cloud가 보내는 webhook payload의 세부 정보를 검토합니다.
- [Connecting Xcode Cloud to Slack](https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-slack): Xcode Cloud를 Slack에 연결해 팀이 최신 Xcode Cloud 빌드 상황을 알 수 있게 합니다.
:::

:::topic-grid
## REST API
- [Xcode Cloud Workflows and Builds](https://developer.apple.com/documentation/AppStoreConnectAPI/xcode-cloud-workflows-and-builds): Xcode Cloud 데이터 읽기, workflow 관리, 빌드 시작을 자동화합니다.
:::
