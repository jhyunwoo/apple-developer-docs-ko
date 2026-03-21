---
route: /documentation/GameSave
source_url: https://developer.apple.com/documentation/GameSave
source_locale: en-US
section: docc
content_type: symbol
title: GameSave
original_title: GameSave
source_hash: 81f934978bf44835aa77630ad1db2d09e311739d43a9e0984e2290ebd7628db5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:16:24+00:00'
last_translated_at: '2026-03-13T08:28:00+00:00'
---

# GameSave

iCloud에 애플리케이션의 저장 파일을 저장하고 동기화합니다.

## 개요

GameSave는 iCloud Drive를 사용해 애플리케이션의 저장 데이터를 여러 기기 사이에서 동기화합니다. 이 프레임워크는 iCloud 개념을 직접 다루지 않아도 되도록 추상화하면서, 하나 이상의 파일을 디렉터리에 읽고 쓰는 API 집합을 제공합니다. 충돌 해결이나 오프라인 플레이 같은 일반적인 저장 동기화 시나리오도 처리합니다. 또한 이런 전형적인 상황을 위한 편의 UI 알림도 제공합니다. 기기가 iCloud Drive에 로그인하지 않은 경우를 위해 로컬 저장도 지원합니다.

:::important Important
GameSave가 플레이어의 iCloud 계정에 게임 데이터를 저장하려면 데이터를 저장할 iCloud 컨테이너 식별자를 제공해야 합니다. 프로젝트에 iCloud capability를 추가하고 `iCloud Documents` 체크상자를 선택하세요. 자세한 내용은 [Configuring iCloud services](https://developer.apple.com/documentation/Xcode/configuring-icloud-services)를 참고하세요.
:::

:::topic-grid
## 동기화 디렉터리
- [GameSaveSyncedDirectory](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory): 게임 저장 데이터용 클라우드 동기화 디렉터리입니다.
:::

:::topic-grid
## 오류 도메인
- [GameSaveErrorDomain](https://developer.apple.com/documentation/gamesave/gamesaveerrordomain): GameSave 오류의 오류 도메인 이름입니다.
:::

:::topic-grid
## 동기화 디렉터리(Objective-C)
- [GSSyncedDirectory](https://developer.apple.com/documentation/gamesave/gssynceddirectory): 게임 저장 데이터용 클라우드 동기화 디렉터리입니다.
:::
