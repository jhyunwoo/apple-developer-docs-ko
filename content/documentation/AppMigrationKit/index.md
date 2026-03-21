---
route: /documentation/AppMigrationKit
source_url: https://developer.apple.com/documentation/AppMigrationKit
source_locale: en-US
section: docc
content_type: symbol
title: AppMigrationKit
original_title: AppMigrationKit
source_hash: a1fe48c2c9c4ef8394c09a43ee16efaedffd3b403097c17deb777c0882389dcb
canonical_source: manual-translation
last_crawled_at: '2026-03-13T05:22:38+00:00'
last_translated_at: '2026-03-13T05:22:38+00:00'
---

# AppMigrationKit

앱의 기기 내 데이터를 다른 플랫폼을 실행하는 기기로 한 번만 전송합니다.

## 개요

AppMigrationKit을 사용해 앱의 기기 내 데이터를 Apple이 아닌 플랫폼을 실행하는 다른 기기로 내보내거나, 다른 플랫폼에서 가져오거나, 또는 둘 다 수행할 수 있습니다.

크로스 플랫폼 마이그레이션에 참여하려면 앱이 [AppMigrationExtension](https://developer.apple.com/documentation/appmigrationkit/appmigrationextension) 프로토콜과 그 하위 프로토콜 중 하나 이상을 따르는 [앱 확장](https://developer.apple.com/app-extensions/)을 생성해야 합니다. 채택하는 프로토콜은 앱이 데이터를 가져오는지, 내보내는지, 또는 둘 다 수행하는지를 나타냅니다.

앱이 클라우드에도 데이터를 저장하는 경우, 다른 플랫폼의 앱이 마이그레이션이 완료된 뒤 그 데이터를 가져오게 하세요. 마찬가지로 다른 플랫폼에서 데이터를 가져오는 경우에도 마이그레이션이 완료된 뒤 클라우드 데이터를 가져오세요.

:::note Note
AppMigrationKit은 Android 같은 Apple 이외의 플랫폼으로의 마이그레이션과 그 반대 방향만 지원합니다. 시스템은 iOS 또는 iPadOS 기기 사이의 마이그레이션에는 이 프레임워크를 사용하지 않습니다. 또한 이 프레임워크는 visionOS에서 실행되는 iOS 앱이나 Apple silicon의 macOS에서 기능을 제공하지 않습니다. Mac Catalyst로 빌드한 Mac 앱에서의 호출은 무시합니다.
:::

:::topic-grid
## 앱 확장
- [AppMigrationExtension](https://developer.apple.com/documentation/appmigrationkit/appmigrationextension): 데이터 내보내기와 가져오기에 참여하기 위해 확장하는 앱 확장입니다.
- [com.apple.developer.app-migration.data-container-access](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.app-migration.data-container-access): 앱 확장이 다른 플랫폼으로 또는 다른 플랫폼에서 기기 내 데이터를 한 번만 전송하는 작업을 수행하는 데 필요한 entitlement입니다.
:::

:::topic-grid
## 내보내기 작업
- [ResourcesExportingWithOptions](https://developer.apple.com/documentation/appmigrationkit/resourcesexportingwithoptions): 보관 형식으로 전송 가능한 리소스를 내보내기 위한 프로토콜입니다.
- [ResourcesExporting](https://developer.apple.com/documentation/appmigrationkit/resourcesexporting): 대상 플랫폼이 특별한 마이그레이션 옵션을 요구하지 않을 때 스트리밍 아카이브 형식으로 전송 가능한 리소스를 내보내기 위한 프로토콜입니다.
:::

:::topic-grid
## 가져오기 작업
- [ResourcesImporting](https://developer.apple.com/documentation/appmigrationkit/resourcesimporting): 스트리밍 아카이브 형식으로 전송 가능한 리소스를 가져오기 위한 프로토콜입니다.
:::

:::topic-grid
## 마이그레이션 상태
- [MigrationStatus](https://developer.apple.com/documentation/appmigrationkit/migrationstatus): 포함 앱이 완료된 가져오기의 상태를 판단하는 데 사용하는 타입입니다.
:::

:::topic-grid
## 마이그레이션 코드 테스트
- [AppMigrationTester](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester): 앱이 앱 마이그레이션 확장을 테스트할 때 사용하는 테스트 전용 타입입니다.
:::
