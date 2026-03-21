---
route: /documentation/CKToolJS
source_url: https://developer.apple.com/documentation/CKToolJS
source_locale: en-US
section: docc
content_type: symbol
title: CKTool JS
original_title: CKTool JS
source_hash: 40e514ce0652e3236399c14a014e0732ae21c3adf252761de653dadc67463799
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:52:39+00:00'
last_translated_at: '2026-03-13T21:30:00+09:00'
---

# CKTool JS

JavaScript에서 CloudKit container와 database를 관리합니다.

## 개요

CKTool JS는 CloudKit Console API가 제공하는 기능에 접근할 수 있게 해 주며, 로컬 개발과 통합 테스트를 위한 CloudKit 설정 작업을 더 쉽게 만들어 줍니다. 이 라이브러리는 Xcode와 함께 배포되는 macOS `cktool` 명령줄 유틸리티를 대신하는 JavaScript 클라이언트 라이브러리입니다. `cktool`에 대해 더 알아보려면 [Automating CloudKit Development](https://developer.apple.com/icloud/cloudkit/automating/)를 참고하십시오.

이 라이브러리를 사용하면 다음을 할 수 있습니다.

- CloudKit schema 파일을 Sandbox database에 적용합니다. CloudKit schema 파일에 대한 자세한 내용은 [Integrating a Text-Based Schema into Your Workflow](https://developer.apple.com/documentation/CloudKit/integrating-a-text-based-schema-into-your-workflow)를 참고하십시오.
- database를 테스트 데이터로 채웁니다.
- Sandbox database를 production 구성으로 재설정합니다.
- 통합 테스트에 포함할 script를 작성합니다.

라이브러리는 세 가지 주요 모듈로 구성됩니다.

- [CKToolDatabaseModule](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule): CloudKit 관련 타입과 메서드, 인증된 사용자의 team과 container를 가져오는 작업, CloudKit 서버와 통신하기 위한 유틸리티 함수와 타입을 담고 있는 패키지입니다. 이 패키지에는 CloudKit record와 함께 작업하기 위한 기능도 포함되어 있습니다. 이 패키지에 접근하려면 `package.json` 파일의 의존성에 `@apple/cktool.database`를 추가합니다.
- [CKToolNodeJsModule](https://developer.apple.com/documentation/cktooljs/cktoolnodejsmodule): Node.js에서 실행되는 프로젝트에 사용하는 [createConfiguration](https://developer.apple.com/documentation/cktooljs/cktoolnodejsmodule/createconfiguration) 함수를 포함하는 패키지입니다. 이 패키지에 접근하려면 `package.json` 파일의 의존성에 `@apple/cktool.target.nodejs`를 추가합니다.
- [CKToolBrowserModule](https://developer.apple.com/documentation/cktooljs/cktoolbrowsermodule): 브라우저 기반 프로젝트에서 사용하는 [createConfiguration](https://developer.apple.com/documentation/cktooljs/cktoolbrowsermodule/createconfiguration) 함수를 포함하는 패키지입니다. 이 패키지에 접근하려면 `package.json` 파일의 의존성에 `@apple/cktool.target.browser`를 추가합니다.

:::topic-grid
## 핵심 사항
- [Integrating CloudKit access into your JavaScript automation scripts](https://developer.apple.com/documentation/cktooljs/integrating-cloudkit-access-into-your-javascript-automation-scripts): JavaScript 프로젝트가 CKTool JS를 사용하도록 구성합니다.
:::

:::topic-grid
## Promises API
- [PromisesApi](https://developer.apple.com/documentation/cktooljs/promisesapi): API와 상호 작용하는 promise 기반 함수를 노출하는 클래스입니다.
- [CancellablePromise](https://developer.apple.com/documentation/cktooljs/cancellablepromise): 작업을 취소하는 함수를 가진 promise입니다.
- [CKToolDatabaseModule](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule): CloudKit container와 database에 접근할 수 있게 해 주는 import된 패키지입니다.
:::

:::topic-grid
## 구성
- [Configuration](https://developer.apple.com/documentation/cktooljs/configuration): API 서버와 통신할 때 사용할 옵션을 보관하는 객체입니다.
- [CKToolNodeJsModule](https://developer.apple.com/documentation/cktooljs/cktoolnodejsmodule): Node.js 환경에서 클라이언트 라이브러리를 사용할 수 있도록 지원하는 import 패키지입니다.
- [CKToolBrowserModule](https://developer.apple.com/documentation/cktooljs/cktoolbrowsermodule): 웹 브라우저 안에서 클라이언트 라이브러리를 사용할 수 있도록 지원하는 import 패키지입니다.
:::

:::topic-grid
## 전역 구조체와 열거형
- [Container](https://developer.apple.com/documentation/cktooljs/container): CloudKit container에 대한 세부 정보입니다.
- [ContainersResponse](https://developer.apple.com/documentation/cktooljs/containersresponse): 여러 CloudKit container를 가져온 결과를 나타내는 객체입니다.
- [CKEnvironment](https://developer.apple.com/documentation/cktooljs/ckenvironment): container 환경에 대한 열거형입니다.
- [ContainersSortByField](https://developer.apple.com/documentation/cktooljs/containerssortbyfield): 가져온 container의 정렬 옵션을 나타내는 열거형입니다.
- [SortDirection](https://developer.apple.com/documentation/cktooljs/sortdirection): 사용자 정의 정렬을 적용할 때의 정렬 방향을 나타내는 열거형입니다.
:::

:::topic-grid
## 오류
- [ErrorBase](https://developer.apple.com/documentation/cktooljs/errorbase): 클라이언트 라이브러리 함수가 발생시키는 모든 오류의 기본 클래스입니다.
- [Database, Length, Validation, and Value Errors](https://developer.apple.com/documentation/cktooljs/database-length-validation-and-value-errors)
:::

:::topic-grid
## 클래스
- [Blob](https://developer.apple.com/documentation/cktooljs/blob)
- [File](https://developer.apple.com/documentation/cktooljs/file)
:::
