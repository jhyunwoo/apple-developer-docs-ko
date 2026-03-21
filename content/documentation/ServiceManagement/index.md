---
route: /documentation/ServiceManagement
source_url: https://developer.apple.com/documentation/ServiceManagement
source_locale: en-US
section: docc
content_type: symbol
title: Service Management
original_title: Service Management
source_hash: cb8dc98724823e311cd4d131259e3c1f357b67484641e5979add2b103d8cb62d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:22:14+00:00'
last_translated_at: '2026-03-13T16:55:00+09:00'
---

# Service Management

앱 내부에서 startup item, launch agent, launch daemon을 관리합니다.

## 개요

Service Management를 사용하면 macOS가 지원하는 세 가지 보조 helper executable을 설치하고 권한 설정을 관찰할 수 있습니다. 이 세 가지 모두 앱 번들 내부에서 앱과 관련된 추가 기능을 제공하는 데 사용할 수 있습니다.

:::term-list
LoginItems: 사용자가 로그인할 때 `launchd`가 시작하는 앱입니다. `LoginItem`은 사용자가 로그아웃하거나 수동으로 종료할 때까지 계속 실행되는 앱입니다. 주된 목적은 시스템이 helper executable을 자동으로 실행할 수 있게 하는 것입니다.
LaunchAgents: 현재 로그인한 사용자를 대신해 실행되는 프로세스입니다. 시스템 수준 프로세스인 `launchd`가 agent를 관리합니다. agent는 같은 사용자 세션의 다른 프로세스 및 시스템 컨텍스트의 시스템 전역 daemon과 통신할 수 있습니다.
LaunchDaemons: `launchd`가 사용자를 대신해 관리하는 독립형 백그라운드 프로세스로, root 권한으로 실행되며 시스템에 사용자가 로그인하기 전에도 실행될 수 있습니다. daemon은 사용자 프로세스와 직접 상호 작용하지 않으며, [XPC](https://developer.apple.com/documentation/Foundation/xpc) 같은 저수준 프로세스 간 통신 시스템 요청처럼 사용자 프로세스가 보내는 저수준 요청에만 응답할 수 있습니다.
:::

:::topic-grid
## 핵심 사항
- [Updating helper executables from earlier versions of macOS](https://developer.apple.com/documentation/servicemanagement/updating-helper-executables-from-earlier-versions-of-macos): 앱의 helper executable을 단순화하고 새로운 권한 제어를 지원합니다.
- [Updating your app package installer to use the new Service Management API](https://developer.apple.com/documentation/servicemanagement/updating-your-app-package-installer-to-use-the-new-service-management-api): GUI가 없는 agent 앱과 함께 Service Management API를 알아봅니다.
:::

:::topic-grid
## 관리
- [SMAppService](https://developer.apple.com/documentation/servicemanagement/smappservice): 앱의 메인 번들 내부에 있는 helper executable을 제어할 때 프레임워크가 사용하는 객체입니다.
- [SMJobBless(_:_:_:_:)](https://developer.apple.com/documentation/servicemanagement/smjobbless(_:_:_:_:)): 지정된 label의 executable을 `launchd`의 job으로 제출합니다.
- [Authorization Constants](https://developer.apple.com/documentation/servicemanagement/authorization-constants): helper executable을 인증하거나 daemon 애플리케이션을 수정하는 기능을 설명하는 상수입니다.
- [Property List Keys](https://developer.apple.com/documentation/servicemanagement/property-list-keys): 프레임워크가 관리하는 애플리케이션, daemon, helper executable의 종류를 설명하는 프로퍼티 리스트 키입니다.
:::

:::topic-grid
## 활성화
- [SMLoginItemSetEnabled(_:_:)](https://developer.apple.com/documentation/servicemanagement/smloginitemsetenabled(_:_:)): 메인 앱 번들 디렉터리의 helper executable을 활성화합니다.
:::

:::topic-grid
## 상태
- [SMAppService.Status](https://developer.apple.com/documentation/servicemanagement/smappservice/status-swift.enum): helper executable의 등록 또는 권한 상태를 설명하는 상수입니다.
:::

:::topic-grid
## 오류
- [Service Management Errors](https://developer.apple.com/documentation/servicemanagement/service-management-errors): 프레임워크가 반환하는 오류입니다.
:::

:::topic-grid
## 더 이상 사용되지 않음
- [Deprecated Symbols](https://developer.apple.com/documentation/servicemanagement/deprecated-symbols)
:::

:::topic-grid
## 변수
- [SMAppServiceErrorDomain](https://developer.apple.com/documentation/servicemanagement/smappserviceerrordomain)
:::
