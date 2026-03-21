---
route: /documentation/ClassKitCatalogAPI
source_url: https://developer.apple.com/documentation/ClassKitCatalogAPI
source_locale: en-US
section: docc
content_type: symbol
title: ClassKit Catalog API
original_title: ClassKit Catalog API
source_hash: 9127539213d42134ac1bc3db298b25a0ad439d3f1f16b8116f0dd7bdfbf06020
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:22:50+00:00'
last_translated_at: '2026-03-13T09:02:00+00:00'
---

# ClassKit Catalog API

교육용 앱이 지원하는 활동을 웹 인터페이스를 통해 선언합니다.

## 개요

[ClassKit](https://developer.apple.com/documentation/ClassKit) 프레임워크를 채택한 앱이 있을 때, 컴퓨터나 서버에서 ClassKit Catalog API에 접근하여 앱의 교육 활동을 선언할 수 있습니다. 전통적으로 앱은 [Schoolwork](https://apps.apple.com/us/app/schoolwork/id1355112526) 앱에서 교사가 활동을 과제로 지정할 수 있도록, 실행 시간에 컨텍스트로 표현되는 활동을 ClassKit 프레임워크에 선언합니다. 대안으로 ClassKit Catalog API를 사용하면 컨텍스트를 중앙 서버에 미리 선언할 수 있으며, 그 결과 다음이 가능해집니다.

- 교사가 기기에서 앱을 처음 실행하기 전에도 Schoolwork 앱에서 앱의 활동을 탐색할 수 있습니다.
- 활동을 설명하는 키워드를 포함해 교사가 콘텐츠를 더 쉽게 찾을 수 있습니다.
- 앱이 실행 시간에 모든 콘텐츠를 ClassKit 프레임워크에 선언하지 않아도 많은 수의 과제 지정 가능한 활동을 지원할 수 있습니다.

ClassKit Catalog API에 업로드한 콘텐츠는 Schoolwork 앱을 사용하는 모든 교사에게 공개됩니다. 동적으로 생성되거나 사용자별로 달라지는 콘텐츠가 있다면, 그런 콘텐츠는 계속 ClassKit 프레임워크를 통해서만 게시하세요.

:::topic-grid
## 필수 항목
- [ClassKit Catalog API 호출 인증하기](https://developer.apple.com/documentation/classkitcatalogapi/authenticating-calls-to-the-classkit-catalog-api): 각 호출마다 암호학적으로 서명된 토큰을 제공하여 ClassKit Catalog 서버에 자신의 신원을 확립합니다.
- [ClassKit Catalog 구현 테스트하기](https://developer.apple.com/documentation/classkitcatalogapi/testing-your-classkit-catalog-implementation): 개발 환경에서 동작시켜 배포 전에 서버 상호 작용을 검증합니다.
:::

:::topic-grid
## 컨텍스트 선언
- [컨텍스트 데이터 준비하기](https://developer.apple.com/documentation/classkitcatalogapi/preparing-context-data): 웹 API와 함께 작업할 때 컨텍스트 데이터 관리 방식을 조정합니다.
- [컨텍스트 생성 또는 교체](https://developer.apple.com/documentation/classkitcatalogapi/create-or-replace-contexts): 교육용 앱이 제공하는 과제 지정 가능한 콘텐츠 정보를 저장합니다.
- [컨텍스트 가져오기](https://developer.apple.com/documentation/classkitcatalogapi/get-a-context): 이전에 저장한 앱의 과제 지정 가능한 활동 정보를 가져옵니다.
- [컨텍스트 삭제](https://developer.apple.com/documentation/classkitcatalogapi/delete-a-context): 이전에 저장한 앱의 과제 지정 가능한 활동 정보를 제거합니다.
- [Context](https://developer.apple.com/documentation/classkitcatalogapi/context): 퀴즈나 장처럼 과제로 지정할 수 있는 작업을 나타내는 앱의 한 영역입니다.
- [ContextsRequest](https://developer.apple.com/documentation/classkitcatalogapi/contextsrequest): 컨텍스트 정보를 수정할 때 보내는 요청입니다.
- [ContextsResponse](https://developer.apple.com/documentation/classkitcatalogapi/contextsresponse): 컨텍스트 정보를 수정한 뒤 받는 응답입니다.
:::

:::topic-grid
## 썸네일 업로드
- [썸네일 생성 또는 교체](https://developer.apple.com/documentation/classkitcatalogapi/create-or-replace-a-thumbnail): 앱의 과제 지정 가능한 활동 중 하나를 나타내는 이미지를 저장합니다.
- [썸네일 가져오기](https://developer.apple.com/documentation/classkitcatalogapi/get-a-thumbnail): 앱의 과제 지정 가능한 활동 중 하나에 대한 이미지를 가져옵니다.
- [썸네일 삭제](https://developer.apple.com/documentation/classkitcatalogapi/delete-a-thumbnail): 앱의 과제 지정 가능한 활동 이미지 중 하나를 제거합니다.
:::

:::topic-grid
## 상태 조회
- [상태 가져오기](https://developer.apple.com/documentation/classkitcatalogapi/get-status): 이전에 시작한 작업의 상태를 가져옵니다.
- [Status](https://developer.apple.com/documentation/classkitcatalogapi/status): API가 이전에 수락했지만 즉시 완료하지 않은 요청의 상태입니다.
:::
