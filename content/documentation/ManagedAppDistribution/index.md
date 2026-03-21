---
route: /documentation/ManagedAppDistribution
source_url: https://developer.apple.com/documentation/ManagedAppDistribution
source_locale: en-US
section: docc
content_type: symbol
title: ManagedAppDistribution
original_title: ManagedAppDistribution
source_hash: d7d3621f615c0776690ea941bf2c9110ddcaa9e165b9f25754146d8deef90741
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:26:19+00:00'
last_translated_at: '2026-03-13T23:26:32+09:00'
---

# ManagedAppDistribution

조직 내부에서 앱 배포를 관리합니다.

## 개요

*Managed app*은 기업, 교육 기관, 기타 조직이 직원이나 학생에게 제공하는 추천 가능한 다운로드 앱입니다. Managed App Distribution 프레임워크를 사용하면 기기 관리 솔루션 개발자가 이러한 managed app을 제공할 수 있습니다. 이 프레임워크는 누군가가 앱 설치를 시작했는지 검증하고, 상태와 다운로드 진행 상황을 제공하며, 앱 다운로드가 끝나면 앱을 실행할 수도 있습니다.

:::important Important
이 프레임워크를 사용하려면 [Managed App Installation UI](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.managed-app-distribution.install-ui) entitlement가 필요합니다.
:::

![iPhone 화면에 앱 상단 배너 이미지가 표시되어 있고, 화면 가운데에는 제목, 부제, 설치 버튼을 포함한 두 개의 앱 배너가 위아래로 배치된 모습입니다.](https://developer.apple.com)

Managed App Distribution 프레임워크는 declarative management와 함께 동작하여 기기에 할당된 managed app 목록을 제공합니다. 앱은 이 목록을 정렬하거나 필터링하고, Managed App Distribution 프레임워크가 표시할 view를 요청할 수 있습니다. 자세한 내용은 [Integrating Declarative Management](https://developer.apple.com/documentation/DeviceManagement/integrating-declarative-management)를 참고하십시오.

:::topic-grid
## 핵심
- [Fetching and displaying managed apps](https://developer.apple.com/documentation/managedappdistribution/fetching-and-displaying-managed-apps): managed app을 표시할 때 일관된 앱 프레젠테이션을 제공합니다.
- [ManagedApp](https://developer.apple.com/documentation/managedappdistribution/managedapp): managed app의 표현입니다.
- [ManagedAppLibrary](https://developer.apple.com/documentation/managedappdistribution/managedapplibrary): managed app 라이브러리의 표현입니다.
:::

:::topic-grid
## 앱 정보
- [Platform](https://developer.apple.com/documentation/managedappdistribution/platform): 앱이 지원하는 플랫폼입니다.
:::

:::topic-grid
## 뷰 생성
- [ManagedAppView](https://developer.apple.com/documentation/managedappdistribution/managedappview): managed app을 표시하는 view입니다.
- [ManagedContentView](https://developer.apple.com/documentation/managedappdistribution/managedcontentview)
- [ManagedContentOfferState](https://developer.apple.com/documentation/managedappdistribution/managedcontentofferstate): managed content view offer의 상태입니다.
- [ManagedContentStyle](https://developer.apple.com/documentation/managedappdistribution/managedcontentstyle): managed content view에 사용자 정의 모양을 적용하는 타입입니다.
:::

:::topic-grid
## 오류
- [ManagedAppDistributionError](https://developer.apple.com/documentation/managedappdistribution/managedappdistributionerror): Managed App Distribution의 오류를 식별하는 코드입니다.
:::

:::topic-grid
## 클래스
- [ManagedPackageLibrary](https://developer.apple.com/documentation/managedappdistribution/managedpackagelibrary): managed package 라이브러리의 표현입니다.
:::

:::topic-grid
## 구조체
- [ManagedPackage](https://developer.apple.com/documentation/managedappdistribution/managedpackage): managed package의 표현입니다.
- [ManagedPackageView](https://developer.apple.com/documentation/managedappdistribution/managedpackageview): managed software package의 정보와 제어를 표시하는 view입니다.
:::
