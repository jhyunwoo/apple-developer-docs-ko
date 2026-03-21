---
route: /documentation/UniformTypeIdentifiers
source_url: https://developer.apple.com/documentation/UniformTypeIdentifiers
source_locale: en-US
section: docc
content_type: symbol
title: Uniform Type Identifiers
original_title: Uniform Type Identifiers
source_hash: 18631c5410def526ae4869bbfa1bffc85a5cd958bc49477c5c5aa4bf6a0b8416
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:42:57+00:00'
last_translated_at: '2026-03-13T23:42:57+09:00'
---

# Uniform Type Identifiers

저장이나 전송에 사용하는 파일 유형을 설명하는 uniform type identifier를 제공합니다.

## 개요

[UniformTypeIdentifiers](https://developer.apple.com/documentation/UniformTypeIdentifiers) 프레임워크는 MIME 타입 및 파일 타입에 매핑되는 공통 타입 모음을 제공합니다. 프로젝트에서 이 타입들을 사용해 앱이 다루는 파일 유형을 설명하십시오. 이러한 설명은 시스템이 파일 저장 형식이나 전송용 메모리 내 데이터를 적절히 처리하도록 도와줍니다. 예를 들어 pasteboard로 데이터를 주고받을 때 활용할 수 있습니다. identifier 타입은 디렉터리, 볼륨, 패키지 같은 다른 리소스를 식별하는 데에도 사용할 수 있습니다.

타입 간 관계는 다른 타입의 subtype으로 명시해 표현할 수 있습니다. 예를 들어 [UTTypePNG](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTTypePNG) 타입은 `public.png` identifier를 가지며 [UTTypeImage](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTTypeImage) (`public.image`)의 subtype입니다. 그리고 [UTTypeImage](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTTypeImage)는 다시 다음 두 타입의 subtype입니다.

- [UTTypeContent](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTTypeContent) (`public.content`): 이 타입이 문서가 될 수 있음을 의미합니다.
- [UTTypeData](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTTypeData) (`public.data`): 이 타입이 바이트 스트림으로 표현 가능함을 의미합니다.

:::note Note
[UTTypeData](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTTypeData)는 [UTTypeItem](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTTypeItem) (`public.item`)도 준수합니다. 이 타입은 파일이나 디렉터리처럼 파일 시스템의 대부분 항목을 포괄하는 일반적인 기반 타입입니다.
:::

:::topic-grid
## 핵심
- [앱을 위한 파일 및 데이터 타입 정의하기](https://developer.apple.com/documentation/uniformtypeidentifiers/defining-file-and-data-types-for-your-app): 앱의 독점 데이터 형식을 지원하도록 uniform type identifier를 선언합니다.
- [시스템이 선언한 uniform type identifier](https://developer.apple.com/documentation/uniformtypeidentifiers/system-declared-uniform-type-identifiers): 시스템이 선언하는 공통 타입입니다.
:::

:::topic-grid
## Uniform type identifier
- [UTType](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct): 로드, 전송, 수신할 데이터 타입을 나타내는 구조체입니다.
- [UTTagClass](https://developer.apple.com/documentation/uniformtypeidentifiers/uttagclass): tag class를 나타내는 타입입니다.
- [UTTypeReference](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference): 로드, 전송, 수신할 데이터 타입을 나타내는 객체입니다.
:::

:::topic-grid
## 참고 자료
- [UniformTypeIdentifiers Constants](https://developer.apple.com/documentation/uniformtypeidentifiers/uniformtypeidentifiers-constants)
:::
