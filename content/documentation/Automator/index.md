---
route: /documentation/Automator
source_url: https://developer.apple.com/documentation/Automator
source_locale: en-US
section: docc
content_type: symbol
title: Automator
original_title: Automator
source_hash: fce1cfc605c6f198f5cfc76457cadb65cfdca343a9a78ffd85bd1ff08472907c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T02:34:17+00:00'
last_translated_at: '2026-03-13T02:34:17+00:00'
---

# Automator

Automator 앱이 로드하고 실행할 수 있는 동작을 개발합니다. 앱에서 Automator 워크플로를 보고, 편집하고, 실행합니다.

## 개요

Automator 프레임워크는 Automator 앱용 동작 개발과 함께, 개발자 앱에서 워크플로를 실행하는 기능도 지원합니다. *동작*은 로드되어 실행될 때 파일 복사나 이미지 자르기처럼 특정 작업을 수행하는 번들입니다. 사용자는 Automator를 사용해 일련의 동작으로 구성된 *워크플로*를 만들고 실행할 수 있습니다. 개발자도 자신의 앱에서 워크플로를 로드하고 실행할 수 있습니다. 워크플로가 실행되는 동안에는 일반적으로 한 동작의 출력이 다음 동작의 입력으로 전달됩니다. Automator는 파일 시스템의 표준 위치인 `/System/Library/Automator`, `/Library/Automator`, `~/Library/Automator`에서 동작 번들을 로드합니다.

:::topic-grid
## 동작
- [AMBundleAction](https://developer.apple.com/documentation/automator/ambundleaction): 로드 가능한 번들인 Automator 동작을 나타내는 객체입니다.
- [AMShellScriptAction](https://developer.apple.com/documentation/automator/amshellscriptaction): 런타임 동작이 셸 스크립트나 Perl 또는 Python 스크립트에 의해 구동되는 Automator 동작을 나타내는 객체입니다.
- [AMAction](https://developer.apple.com/documentation/automator/amaction): Automator 동작의 인터페이스와 일반적인 특성을 정의하는 추상 클래스입니다.
:::

:::topic-grid
## 워크플로
- [AMWorkflow](https://developer.apple.com/documentation/automator/amworkflow): 앱에서 Automator 워크플로를 사용할 수 있게 해 주는 객체입니다.
- [AMWorkflowController](https://developer.apple.com/documentation/automator/amworkflowcontroller): 앱에서 Automator 워크플로를 관리할 수 있게 해 주는 객체입니다.
- [AMWorkflowView](https://developer.apple.com/documentation/automator/amworkflowview): 앱에서 Automator 워크플로를 보고 편집할 수 있게 해 주는 객체입니다.
- [AMWorkspace](https://developer.apple.com/documentation/automator/amworkspace): Automator 워크플로를 실행하기 위한 작업 공간입니다.
:::

:::topic-grid
## 오류
- [AMAutomatorErrorDomain](https://developer.apple.com/documentation/automator/amautomatorerrordomain): Automator 오류 도메인을 식별하는 문자열입니다.
- [AMActionErrorKey](https://developer.apple.com/documentation/automator/amactionerrorkey): 오류를 일으킨 동작을 가져오기 위한 키입니다.
- [AMError](https://developer.apple.com/documentation/automator/amerror): Automator 오류입니다.
- [AMError.Code](https://developer.apple.com/documentation/automator/amerror/code): Automator 오류 코드입니다.
:::

:::topic-grid
## 지원 중단됨
- [AMAppleScriptAction](https://developer.apple.com/documentation/automator/amapplescriptaction): 런타임 동작이 AppleScript 스크립트에 의해 구동되는 Automator 동작을 나타내는 객체입니다.
:::
