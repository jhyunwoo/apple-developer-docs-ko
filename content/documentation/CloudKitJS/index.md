---
route: /documentation/CloudKitJS
source_url: https://developer.apple.com/documentation/CloudKitJS
source_locale: en-US
section: docc
content_type: symbol
title: CloudKit JS
original_title: CloudKit JS
source_hash: 55d79a065ad280b043922d567df505a975a701310d0484982fe27206d06a02ab
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:42:57+00:00'
last_translated_at: '2026-03-13T23:42:57+09:00'
---

# CloudKit JS

웹 앱에서 CloudKit 앱의 container와 database에 접근할 수 있게 합니다.

## 개요

CloudKit JS를 사용하면 iOS나 macOS에서 실행되는 CloudKit 앱과 동일한 public/private database에 사용자가 접근할 수 있는 웹 인터페이스를 만들 수 있습니다. CloudKit JS를 사용하려면 기존 CloudKit 앱이 있어야 하며 웹 서비스를 활성화해야 합니다.

### 시작하기 전에

앱의 container를 설정하고 CloudKit JS를 구성하십시오.

1. 앱의 container와 schema를 만듭니다.  
   CloudKit이 처음이라면 [CloudKit Quick Start](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014987)를 먼저 읽으십시오. Xcode를 사용해 앱의 container를 만들고 CloudKit Dashboard에서 container를 확인할 수 있습니다. 그런 다음 CloudKit을 사용해 앱 데이터를 저장하는 iOS 또는 Mac 앱을 만듭니다.
2. CloudKit Dashboard에서 API token 또는 server-to-server key를 만들어 웹 서비스를 활성화합니다.  
   웹사이트나 네이티브 앱 안의 임베디드 웹 뷰에서 사용하거나, 사용자를 인증해야 하는 경우에는 API token을 사용합니다. API token 생성 방법은 [iCloud container용 API token 얻기](https://developer.apple.com/documentation/CloudKit/obtaining-an-api-token-for-an-icloud-container)를 참고하십시오.  
   서버 프로세스나 스크립트에서 관리자 권한으로 public database에 접근하려면 server-to-server key를 사용합니다. server-to-server key 생성 방법은 [Setting Up Web Services](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/SettingUpWebServices.html#//apple_ref/doc/uid/TP40015240-CH24-SW6)를 참고하십시오. 또한 server-to-server key를 사용하는 JavaScript 예제는 [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](https://developer.apple.com/library/archive/samplecode/CloudAtlas/Introduction/Intro.html#//apple_ref/doc/uid/TP40014599)를 참고하십시오.
3. 웹페이지에 CloudKit JS를 포함합니다.  
   `script` 태그를 사용해 Apple이 호스팅하는 CloudKit JS 버전 `https://cdn.apple-CloudKit.com/ck/2/CloudKit.js`를 연결합니다.

```javascript
<script src="https://cdn.apple-CloudKit.com/ck/2/CloudKit.js">
```

:::note Note
CloudKit JS 버전 번호는 URL 안에 있습니다. 예를 들어 `2`는 CloudKit JS 2.0을 의미합니다.
:::

4. JavaScript strict mode를 활성화합니다.  
   스크립트 전체에 strict mode를 적용하려면 다른 모든 문장보다 앞에 `"use strict";`를 넣으십시오.

```javascript
"use strict";
```

5. CloudKit JS를 구성합니다.  
   [CloudKit.configure](https://developer.apple.com/documentation/CloudKitJS/CloudKit/configure) 메서드를 사용해 앱의 container 정보를 CloudKit JS에 제공합니다. 또한 development 환경과 production 환경 중 어느 것을 사용할지 지정해야 합니다. 예제는 [CloudKit](https://developer.apple.com/documentation/CloudKitJS/CloudKit)를 참고하고, 설정 가능한 속성의 세부 사항은 [CloudKit JS Data Types](https://developer.apple.com/documentation/CloudKitJS/cloudkit-js-data-types)와 [CloudKit.CloudKitConfig](https://developer.apple.com/documentation/CloudKitJS/CloudKit.CloudKitConfig)를 참고하십시오.

이제 JavaScript 코드에서 [CloudKit.getDefaultContainer](https://developer.apple.com/documentation/CloudKitJS/CloudKit/getDefaultContainer) 메서드를 사용해 앱 container([CloudKit.Container](https://developer.apple.com/documentation/CloudKitJS/CloudKit.Container))와 그 database 객체([CloudKit.Database](https://developer.apple.com/documentation/CloudKitJS/CloudKit.Database))를 가져올 수 있습니다.

### 다음 단계

CloudKit JS를 배우려면 [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](https://developer.apple.com/library/archive/samplecode/CloudAtlas/Introduction/Intro.html#//apple_ref/doc/uid/TP40014599) 샘플 코드 프로젝트를 내려받고, API 세부 정보를 위해 CloudKit JS 클래스 레퍼런스 문서를 참고하십시오. CloudKit JS 코드를 실행하고 CloudKit 서버 응답을 확인할 수 있는 이 샘플의 호스팅 버전은 [CloudKit Catalog Hosted Sample](https://cdn.apple-CloudKit.com/CloudKit-catalog/)에서 확인할 수 있습니다.

다음 자료도 CloudKit 이해에 도움이 됩니다.

- [CloudKit Quick Start](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014987): CloudKit 네이티브 앱을 만드는 방법을 빠르게 시작합니다.
- [CloudKit](https://developer.apple.com/documentation/CloudKitJS/CloudKit): CloudKit JS 코드 작성 방법을 배웁니다.
- [CloudKit Web Services Reference](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240): CloudKit container와 database에 대한 HTTP 인터페이스를 설명합니다.
- [iCloud Design Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/Introduction.html#//apple_ref/doc/uid/TP40012094): App Store 또는 Mac App Store에 제출하는 앱에서 사용할 수 있는 iCloud 서비스 전반을 개괄합니다.

:::topic-grid
## 클래스
- [CloudKit](https://developer.apple.com/documentation/cloudkitjs/cloudkit): `CloudKit` namespace를 사용해 CloudKit JS를 구성하고, 앱 container와 전역 상수에 접근합니다.
- [CloudKit.CKError](https://developer.apple.com/documentation/cloudkitjs/cloudkit.ckerror): CloudKit JS를 사용할 때 발생할 수 있는 오류를 캡슐화하는 `CloudKit.CKError` 객체입니다. 여기에는 CloudKit 서버 오류와 로컬 오류가 포함됩니다.
- [CloudKit.Container](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container): 앱 container에 접근하고, 그 container를 통해 database에 접근할 수 있게 해 주는 객체입니다. 인증 및 사용자 조회 메서드도 포함합니다.
- [CloudKit.Database](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database): 앱 container 안의 public 또는 private database를 나타내는 객체입니다.
- [CloudKit.DatabaseChangesResponse](https://developer.apple.com/documentation/cloudkitjs/cloudkit.databasechangesresponse): database 안에서 변경된 record zone을 가져온 결과를 캡슐화하는 객체입니다.
- [CloudKit.Notification](https://developer.apple.com/documentation/cloudkitjs/cloudkit.notification): 앱으로 전송된 push notification을 나타내는 객체입니다.
- [CloudKit.QueryNotification](https://developer.apple.com/documentation/cloudkitjs/cloudkit.querynotification): subscription 객체가 생성한 push notification을 나타내는 객체입니다.
- [CloudKit.QueryResponse](https://developer.apple.com/documentation/cloudkitjs/cloudkit.queryresponse): query를 사용해 record를 가져온 결과를 캡슐화하는 객체입니다.
- [CloudKit.RecordInfosResponse](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordinfosresponse): 일반 record와 공유 record에 대한 정보를 가져온 결과를 캡슐화하는 객체입니다.
- [CloudKit.RecordsBatchBuilder](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsbatchbuilder): 단일 database 작업에서 여러 record 변경 결과를 다루는 객체입니다.
- [CloudKit.RecordsResponse](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsresponse): record를 가져온 결과를 캡슐화하는 객체입니다.
- [CloudKit.RecordZoneChangesResponse](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordzonechangesresponse): 하나 이상의 record zone 변경 결과를 캡슐화하는 객체입니다.
- [CloudKit.RecordZoneNotification](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordzonenotification): record zone 내용 변경으로 인해 발생한 push notification을 나타내는 객체입니다.
- [CloudKit.RecordZonesResponse](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordzonesresponse): record zone에 대한 database 작업 결과를 캡슐화하는 객체입니다.
- [CloudKit.Response](https://developer.apple.com/documentation/cloudkitjs/cloudkit.response): 서버 요청 응답을 캡슐화하는 하위 클래스들의 추상 상위 클래스입니다.
- [CloudKit.ShareRecordType](https://developer.apple.com/documentation/cloudkitjs/cloudkit.sharerecordtype): 공유 record의 record type 정보를 표시합니다.
- [CloudKit.SubscriptionsResponse](https://developer.apple.com/documentation/cloudkitjs/cloudkit.subscriptionsresponse): subscription에 대한 database 작업 결과를 캡슐화하는 객체입니다.
- [CloudKit.UserIdentitiesResponse](https://developer.apple.com/documentation/cloudkitjs/cloudkit.useridentitiesresponse): 사용자 identity를 가져온 결과를 캡슐화하는 객체입니다.
:::

:::topic-grid
## 참고 자료
- [CloudKit JS Data Types](https://developer.apple.com/documentation/cloudkitjs/cloudkit-js-data-types): 개별 클래스 레퍼런스 문서에서 다루지 않는 CloudKit JS 데이터 타입을 설명합니다.
- [CloudKit JS Enumerations](https://developer.apple.com/documentation/cloudkitjs/cloudkit-js-enumerations)
:::
