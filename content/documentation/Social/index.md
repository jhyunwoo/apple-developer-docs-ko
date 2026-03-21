---
route: /documentation/Social
source_url: https://developer.apple.com/documentation/Social
source_locale: en-US
section: docc
content_type: symbol
title: Social
original_title: Social
source_hash: 28fbe29d709ea6daca61f197d51ac774948a199d5fa552a74641155e8728b364
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:33:48+00:00'
last_translated_at: '2026-03-14T00:58:00+09:00'
---

# Social

표준 시스템 인터페이스를 사용해 지원되는 소셜 네트워킹 서비스에 콘텐츠를 게시합니다.

## 개요

iOS와 macOS에서 이 프레임워크는 HTTP 요청을 생성하기 위한 템플릿을 제공합니다. iOS에서는 여기에 더해, 사용자를 대신해 게시 요청을 보낼 수 있는 일반화된 인터페이스도 제공합니다.

이 프레임워크를 사용하는 일반적인 방식은 다음과 같습니다.

- 네트워크 세션을 생성합니다.
- 사용자의 활동 피드를 가져옵니다.
- 새 게시물을 만듭니다.
- 게시물 속성을 설정하고 첨부 파일 등을 추가합니다.
- 활동 피드에 게시물을 올립니다.

:::topic-grid
## 작성 인터페이스
- [SLComposeServiceViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller): 사용자가 소셜 미디어 게시물을 작성할 수 있도록 share app extension에서 표시하는 view controller입니다.
- [SLComposeViewController](https://developer.apple.com/documentation/social/slcomposeviewcontroller): 사용자가 소셜 미디어 게시물을 작성할 수 있게 하는 view controller입니다.
:::

:::topic-grid
## 서버 통신
- [SLRequest](https://developer.apple.com/documentation/social/slrequest): 소셜 미디어 서비스와 통신하기 위한 HTTP 요청을 구성하는 데 사용하는 객체입니다.
:::
