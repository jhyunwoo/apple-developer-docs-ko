---
route: /documentation/ServicesAccountLinking
source_url: https://developer.apple.com/documentation/ServicesAccountLinking
source_locale: en-US
section: docc
content_type: symbol
title: ServicesAccountLinking
original_title: ServicesAccountLinking
source_hash: 3f8a8fd965c2ad7a84c971e0d2e26b1c8ba4ad8bb6508c65010ebb5643239ad7
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:27:10+00:00'
last_translated_at: '2026-03-13T20:00:00+09:00'
---

# ServicesAccountLinking

리셀러 계정을 Apple Media & Purchases 계정과 연결합니다.

## 개요

이 프레임워크를 사용하면 애플리케이션이 사용자의 Apple Media & Purchases 계정에 리셀러 계정 식별자 또는 토큰을 등록할 수 있습니다. 이 기능을 통해 콘텐츠 제공업체와 채널 파트너는 자신의 사용자 계정을 Apple 생태계와 연결할 수 있습니다.

이 프레임워크를 사용하려면 다음이 필요합니다.

- 애플리케이션이 Apple의 채널 파트너십 프로그램에 등록되어 있어야 합니다.
- 토큰 또는 식별자를 생성하기 위한 파트너 자격 증명을 획득해야 합니다.
- 프로젝트 대상이 iOS 16.4 이상이어야 합니다.

애플리케이션이 승인된 파트너로 등록되어 있지 않으면 등록이 [notEligible](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror/noteligible) 오류와 함께 실패합니다. 승인된 파트너가 되려면 Apple 채널 파트너십 프로그램에 문의하십시오.

:::topic-grid
## 등록
- [ResellerAccount](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount): Apple Media & Purchases 계정과 연결하기 위한 리셀러 계정 타입입니다.
:::

:::topic-grid
## 오류 처리
- [RegistrationError](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror): 등록 오류 코드입니다.
- [RegistrationErrorDomain](https://developer.apple.com/documentation/servicesaccountlinking/registrationerrordomain): 계정 등록 실패에 대한 오류 도메인입니다.
:::
