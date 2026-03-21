---
route: /documentation/XcodeKit
source_url: https://developer.apple.com/documentation/XcodeKit
source_locale: en-US
section: docc
content_type: symbol
title: XcodeKit
original_title: XcodeKit
source_hash: 82ef091bcd2bfd4d85cec7091fddcb15bd0dfa4f92c9fe67b5a78af1f32c12f8
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:26:19+00:00'
last_translated_at: '2026-03-13T23:26:32+09:00'
---

# XcodeKit

Xcode 소스 편집기에 명령을 추가하는 extension을 만듭니다.

## 개요

XcodeKit 프레임워크를 사용하면 소스 편집기 extension으로 Xcode를 사용자화하여, 소스 편집기에 기능과 특수 동작을 추가할 수 있습니다. 소스 편집기 extension은 Xcode의 Editor 메뉴에 기본 제공 명령과 함께 표시되는 편집기 명령 그룹을 제공합니다. 소스 편집기 extension은 소스 파일의 내용을 읽고 수정할 수 있을 뿐 아니라, 편집기 안의 현재 텍스트 선택 영역도 읽고 수정할 수 있습니다. 소스 편집기 extension은 Mac App Store를 통해 배포하는 개발자 앱 안에 포함하십시오.

:::topic-grid
## 핵심
- [Creating a Source Editor Extension](https://developer.apple.com/documentation/xcodekit/creating-a-source-editor-extension): Xcode 프로젝트에 소스 편집기 extension을 추가하고 구성합니다.
- [Testing Your Source Editor Extension](https://developer.apple.com/documentation/xcodekit/testing-your-source-editor-extension): 특수한 Xcode 인스턴스를 실행해 소스 편집기 extension을 테스트합니다.
- [XCSourceEditorExtension](https://developer.apple.com/documentation/xcodekit/xcsourceeditorextension): Xcode 소스 편집기 extension을 만들기 위해 구현하는 protocol입니다.
:::

:::topic-grid
## 편집기 명령
- [XCSourceEditorCommand](https://developer.apple.com/documentation/xcodekit/xcsourceeditorcommand): 소스 편집기 extension 안에서 명령 호출을 처리하기 위해 구현하는 protocol입니다.
- [XCSourceEditorCommandInvocation](https://developer.apple.com/documentation/xcodekit/xcsourceeditorcommandinvocation): extension에 전달된 명령을 식별하고 현재 활성 소스 편집기의 내용을 제공하는 객체입니다.
:::

:::topic-grid
## 소스 텍스트
- [XCSourceTextBuffer](https://developer.apple.com/documentation/xcodekit/xcsourcetextbuffer): 소스 편집기 안의 텍스트 내용과 텍스트 선택 영역에 접근하고 수정할 때 사용하는 buffer입니다.
- [XCSourceTextPosition](https://developer.apple.com/documentation/xcodekit/xcsourcetextposition): 줄 번호와 열 번호로 정의되는, 소스 편집기 안의 0 기반 위치입니다.
- [XCSourceTextRange](https://developer.apple.com/documentation/xcodekit/xcsourcetextrange): 텍스트를 선택하거나 새 텍스트의 삽입 지점을 지정할 때 사용하는, buffer 안의 반열린 범위입니다.
:::

:::topic-grid
## XcodeKit 상수
- [XcodeKit Version Constants](https://developer.apple.com/documentation/xcodekit/xcodekit-version-constants): Xcode 인스턴스에서 사용 가능한 XcodeKit 버전을 판별합니다.
:::
