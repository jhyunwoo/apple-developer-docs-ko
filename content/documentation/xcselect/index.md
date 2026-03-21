---
route: /documentation/xcselect
source_url: https://developer.apple.com/documentation/xcselect
source_locale: en-US
section: docc
content_type: symbol
title: xcselect
original_title: xcselect
source_hash: 7bd19eccb16562538397cfb61f1c88217adc20bca3f6bf0eb3bad45c10370581
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:28:21+00:00'
last_translated_at: '2026-03-13T23:28:34+09:00'
---

# xcselect

호스트 시스템에서 사용 가능한 macOS SDK의 경로에 접근합니다.

## 개요

시스템은 [xcselect_host_sdk_path](https://developer.apple.com/documentation/xcselect/xcselect_host_sdk_path) 함수를 제공하며, 이를 사용해 로컬 Mac에서 실행되는 실행 파일, 라이브러리, 기타 콘텐츠를 빌드할 때 필요한 macOS SDK 버전의 경로를 찾을 수 있습니다. Xcode 빌드 도구를 사용하지 않는다면 이 함수를 사용해 필요한 macOS SDK 버전을 얻을 수 있습니다.

:::note Note
`xcselect` 프레임워크는 Swift에서 사용할 수 없습니다.
:::
