---
route: /documentation/RosterAPI
source_url: https://developer.apple.com/documentation/RosterAPI
source_locale: en-US
section: docc
content_type: symbol
title: Roster API
original_title: Roster API
source_hash: d0c7a99c140c772b8ad97babf0a0677d748edb8ec793f07575cf0449d9779d41
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:03:28+00:00'
last_translated_at: '2026-03-13T16:25:00+09:00'
---

# Roster API

Apple School Manager 조직의 사람과 수업에 대한 정보를 읽습니다.

## 개요

Roster API는 Apple School Manager(ASM)의 사람 및 수업 정보에 접근할 수 있게 해 줍니다. 앱 안에서 학기 첫날 전에 학생 또는 교사 레코드를 자동으로 생성하는 워크플로를 지원해야 한다면 이 REST API를 사용하십시오. 대표적인 사용 사례는 앱이 각 수업의 학생에게 과제와 마감일을 입력해야 하는 경우입니다.

사용자와 수업 정보에 접근하려면 ASM 조직 관리자의 승인이 필요합니다. Roster API 권한 부여 흐름을 시작할 때는 아래 정의된 scope를 사용해 적절한 접근 수준을 요청하십시오.

:::term-list
`edu.users.read`: ASM 사용자에 대한 읽기 접근을 요청합니다.
`edu.classes.read`: ASM 수업에 대한 읽기 접근을 요청합니다.
:::

권한 부여 흐름이 끝나면 수신한 access token을 사용해 Roster API 엔드포인트에 접근하고, 이를 통해 사람과 수업 정보를 가져옵니다. access token 요청에 대한 자세한 내용은 [Token validation](https://developer.apple.com/documentation/SigninwithAppleRESTAPI/Generate-and-validate-tokens)을 참고하십시오.

수신한 access token은 모든 요청의 Authorization 헤더에 포함하십시오. Roster API는 access token을 ASM 조직과 연결합니다. 엔드포인트는 해당 ASM 조직에 포함된 사용자 및 수업 정보를 반환합니다. Sign in with Apple at Work & School의 고유 계정 식별자는 Roster API 사용자 정보에 제공되는 식별자와 동일합니다. 이 식별자를 사용해 Roster API의 사용자 정보를 앱에 로그인한 사용자와 연결할 수 있습니다.

:::topic-grid
## 핵심 사항
- [Obtaining information about people and classes](https://developer.apple.com/documentation/rosterapi/obtaining-information-about-people-and-classes): 서버에서 조직 정보를 요청할 수 있도록 앱을 준비합니다.
- [Validating with the Roster API test scope](https://developer.apple.com/documentation/rosterapi/validating-with-the-roster-api-test-scope): 테스트 데이터를 사용해 Roster API 통합이 올바르게 동작하는지 확인합니다.
:::

:::topic-grid
## 인증
- [Integrating with Roster API and Sign in with Apple](https://developer.apple.com/documentation/rosterapi/integrating-with-roster-api-and-sign-in-with-apple): 사용자의 Managed Apple Account를 Apple School Manager의 신원과 연결합니다.
:::

:::topic-grid
## 사용자 정보
- [Read a user](https://developer.apple.com/documentation/rosterapi/returns-a-specific-user-in-an-apple-school-manager-organization): Apple School Manager 조직의 사용자를 읽습니다.
- [User](https://developer.apple.com/documentation/rosterapi/user): Apple School Manager 조직의 사용자입니다.
- [RoleLocation](https://developer.apple.com/documentation/rosterapi/rolelocation): Apple School Manager 조직에서 사용자가 맡고 있는 역할과 그에 대응하는 위치 간의 매핑입니다.
- [List users](https://developer.apple.com/documentation/rosterapi/returns-a-list-of-users-in-an-apple-school-manager-organization): Apple School Manager 조직의 사용자 목록을 가져옵니다.
- [List users in a class](https://developer.apple.com/documentation/rosterapi/returns-a-users-for-an-apple-school-manager-class): Apple School Manager 조직의 특정 수업에 속한 사용자 목록을 가져옵니다.
- [Users](https://developer.apple.com/documentation/rosterapi/users): 페이지네이션 토큰이 포함된 사용자 목록입니다.
:::

:::topic-grid
## 수업 정보
- [Read a class](https://developer.apple.com/documentation/rosterapi/returns-a-specific-class-in-an-apple-school-manager-organization.): Apple School Manager 조직의 수업을 읽습니다.
- [Class](https://developer.apple.com/documentation/rosterapi/class): Apple School Manager 조직의 수업입니다.
- [List classes](https://developer.apple.com/documentation/rosterapi/returns-a-list-of-classes-for-an-apple-school-manager-organization): Apple School Manager 조직의 수업 목록을 가져옵니다.
- [Classes](https://developer.apple.com/documentation/rosterapi/classes): 페이지네이션 토큰이 포함된 수업 목록입니다.
:::

:::topic-grid
## 위치 정보
- [Read a location](https://developer.apple.com/documentation/rosterapi/returns-a-specific-location-in-an-apple-school-manager-organization): Apple School Manager 조직의 특정 위치를 반환합니다.
- [Location](https://developer.apple.com/documentation/rosterapi/location): Apple School Manager 조직의 위치입니다.
- [List locations](https://developer.apple.com/documentation/rosterapi/returns-a-list-of-locations-for-an-apple-school-manager-organization): Apple School Manager 조직의 위치 목록을 반환합니다.
- [Locations](https://developer.apple.com/documentation/rosterapi/locations): 페이지네이션 토큰이 포함된 위치 목록입니다.
:::

:::topic-grid
## 조직 정보
- [Read the organization](https://developer.apple.com/documentation/rosterapi/returns-organization-infrmation): Apple School Manager 조직 정보를 반환합니다.
- [Organization](https://developer.apple.com/documentation/rosterapi/organization): Apple School Manager 조직에 대한 정보입니다.
- [Domain](https://developer.apple.com/documentation/rosterapi/domain): Apple School Manager 조직과 연결된 DNS 도메인 이름입니다.
:::
