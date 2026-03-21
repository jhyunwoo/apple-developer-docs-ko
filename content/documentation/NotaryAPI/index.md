---
route: /documentation/NotaryAPI
source_url: https://developer.apple.com/documentation/NotaryAPI
source_locale: en-US
section: docc
content_type: symbol
title: Notary API
original_title: Notary API
source_hash: 81bb0eb4b33c4a466e761493f9c8c698f8917b83f3bed865799cdeed6bd5793e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:21:28+00:00'
last_translated_at: '2026-03-14T01:05:00+09:00'
---

# Notary API

웹 인터페이스를 통해 macOS 소프트웨어를 notarization에 제출합니다.

## 개요

Notarization은 Developer ID로 서명한 macOS 소프트웨어가 Apple에 의해 악성 코드 검사를 거쳤다는 확신을 사용자에게 제공합니다. Xcode나 `notarytool` 명령줄 유틸리티를 통해 notary 서비스와 상호 작용하는 것 외에도, `notarytool`을 우회하고 REST API를 통해 서비스와 직접 상호 작용할 수 있습니다. Notary API는 앱을 notary 서비스에 업로드할 때 macOS 의존성을 피해야 하는 경우에 특히 유용하며, 다음을 가능하게 하는 endpoint를 제공합니다.

- 새 버전의 소프트웨어를 받을 수 있도록 notary 서비스를 준비하고, Amazon S3 endpoint에 소프트웨어를 업로드할 때 사용하는 자격 증명을 얻습니다.
- 제출 상태를 확인합니다.
- 제출에 대한 세부 정보를 제공하는 로그 파일을 가져옵니다.
- 팀의 이전 제출 목록을 가져옵니다.

Notarization이 어떻게 동작하는지 알아보려면 [Notarizing macOS software before distribution](https://developer.apple.com/documentation/Security/notarizing-macos-software-before-distribution)을 참고하십시오. Notary 서비스 REST API를 사용해 소프트웨어를 업로드하는 자세한 내용은 [Submitting software for notarization over the web](https://developer.apple.com/documentation/notaryapi/submitting-software-for-notarization-over-the-web)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [Submitting software for notarization over the web](https://developer.apple.com/documentation/notaryapi/submitting-software-for-notarization-over-the-web): notary 서비스와 직접 연동하여 notarization 워크플로에서 macOS 의존성을 제거합니다.
:::

:::topic-grid
## 소프트웨어 제출
- [Submit Software](https://developer.apple.com/documentation/notaryapi/submit-software): 소프트웨어의 새 버전을 notary 서비스에 업로드하는 과정을 시작합니다.
- [NewSubmissionRequest](https://developer.apple.com/documentation/notaryapi/newsubmissionrequest): notary 서비스에 제출을 시작할 때 제공하는 데이터입니다.
- [NewSubmissionResponse](https://developer.apple.com/documentation/notaryapi/newsubmissionresponse): 소프트웨어 제출에 대한 notary 서비스의 응답입니다.
:::

:::topic-grid
## notarization 결과
- [Get Submission Status](https://developer.apple.com/documentation/notaryapi/get-submission-status): 소프트웨어 notarization 제출의 상태를 가져옵니다.
- [SubmissionResponse](https://developer.apple.com/documentation/notaryapi/submissionresponse): 제출 상태 요청에 대한 notary 서비스의 응답입니다.
- [Get Submission Log](https://developer.apple.com/documentation/notaryapi/get-submission-log): 완료된 단일 notarization의 세부 정보를 가져옵니다.
- [SubmissionLogURLResponse](https://developer.apple.com/documentation/notaryapi/submissionlogurlresponse): 완료된 제출의 로그 정보 요청에 대한 notary 서비스의 응답입니다.
:::

:::topic-grid
## 이력
- [Get Previous Submissions](https://developer.apple.com/documentation/notaryapi/get-previous-submissions): 팀의 이전 notarization 제출 목록을 가져옵니다.
- [SubmissionListResponse](https://developer.apple.com/documentation/notaryapi/submissionlistresponse): 팀의 이전 제출 정보 요청에 대한 notary 서비스의 응답입니다.
:::

:::topic-grid
## 오류
- [ErrorResponse](https://developer.apple.com/documentation/notaryapi/errorresponse): 오류가 발생했을 때 notary 서비스가 반환하는 응답입니다.
:::
