---
route: /documentation/Accounts
source_url: https://developer.apple.com/documentation/Accounts
source_locale: en-US
section: docc
content_type: symbol
title: Accounts
original_title: Accounts
source_hash: fe815a3a142263a04672874d54aa59c6fae707143e63d73ba0399f84026bb682
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:52:39+00:00'
last_translated_at: '2026-03-13T21:30:00+09:00'
---

# Accounts

사용자가 로그인 자격 증명을 직접 입력하지 않고도 앱 안에서 외부 계정에 접근하고 관리할 수 있도록 돕습니다.

## 개요

Accounts 프레임워크는 시스템이 관리하는 Accounts 데이터베이스에 저장된 사용자 계정에 대한 접근을 제공합니다. 계정은 LinkedIn 같은 특정 서비스의 로그인 자격 증명을 저장하며, 앱은 이 자격 증명을 사용해 해당 서비스에 인증합니다. Accounts 프레임워크를 앱에 통합하면 계정 로그인 정보를 직접 저장할 필요가 없습니다. 대신 사용자가 자신의 계정 로그인 자격 증명을 앱이 사용할 수 있도록 권한을 부여하므로, 사용자 이름과 암호를 직접 입력할 필요가 없어집니다. 특정 서비스에 대한 계정이 사용자의 Accounts 데이터베이스에 없다면, 앱 안에서 계정을 만들고 저장하도록 할 수도 있습니다.

:::topic-grid
## 계정 관리
- [ACAccountStore](https://developer.apple.com/documentation/accounts/acaccountstore): 사용자의 계정 정보를 요청, 관리, 저장할 때 사용하는 객체입니다.
- [ACAccount](https://developer.apple.com/documentation/accounts/acaccount): 사용자의 계정 중 하나와 연관된 정보입니다.
- [ACAccountCredential](https://developer.apple.com/documentation/accounts/acaccountcredential): 사용자를 인증하는 데 필요한 정보를 캡슐화하는 자격 증명 객체입니다.
:::

:::topic-grid
## 계정 타입
- [ACAccountType](https://developer.apple.com/documentation/accounts/acaccounttype): 특정 타입의 모든 계정에 대한 정보를 캡슐화하는 객체입니다.
:::

:::topic-grid
## 오류
- [ACErrorCode](https://developer.apple.com/documentation/accounts/acerrorcode): 발생할 수 있는 오류에 대한 코드입니다.
- [ACErrorDomain](https://developer.apple.com/documentation/accounts/acerrordomain): Accounts 프레임워크의 오류 도메인입니다.
:::

:::topic-grid
## 더 이상 사용되지 않음
- [Deprecated Symbols](https://developer.apple.com/documentation/accounts/deprecated-symbols): 앱에서 deprecated symbol 사용을 피하십시오.
:::
