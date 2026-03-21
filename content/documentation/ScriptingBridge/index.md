---
route: /documentation/ScriptingBridge
source_url: https://developer.apple.com/documentation/ScriptingBridge
source_locale: en-US
section: docc
content_type: symbol
title: Scripting Bridge
original_title: Scripting Bridge
source_hash: 6d4d9d0723e9298720f5248600a2a78bbfeadd8e47aaf5a6e831652ab629638c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:46:59+00:00'
last_translated_at: '2026-03-14T01:23:00+09:00'
---

# Scripting Bridge

Apple event를 보내고 받아 scriptable 앱을 자동화합니다.

## 개요

Scripting Bridge는 표준 Objective-C 문법을 사용해 scriptable Apple 및 서드파티 애플리케이션을 제어할 수 있게 해 주는 기술입니다. OS X 10.5(Leopard)에서 도입된 Scripting Bridge 프레임워크는 OSA 규격을 준수하는 애플리케이션, 즉 스크립팅 인터페이스(보통 `sdef` 파일로 정의됨)를 가진 애플리케이션에 대해 Objective-C bridge를 동적으로 구현합니다. 이 구현의 일부로 프레임워크는 스크립팅 인터페이스에서 찾은 클래스에 대한 Objective-C 클래스 구현을 생성하며, 여기에는 속성, 요소, 명령 등을 나타내는 객체와 메서드가 포함됩니다. 이러한 객체는 Scripting Bridge 프레임워크에 정의된 클래스에서 파생됩니다.

:::topic-grid
## 클래스
- [SBApplication](https://developer.apple.com/documentation/scriptingbridge/sbapplication): 이 클래스는 Objective-C 프로그램이 scriptable 애플리케이션으로 Apple event를 보내고 응답으로 Apple event를 받을 수 있게 하는 메커니즘을 제공합니다. 이를 통해 해당 프로그램은 애플리케이션을 제어하고 데이터를 교환할 수 있습니다. Scripting Bridge는 Apple event descriptor와 Cocoa 객체 사이에서 데이터 타입을 bridge하는 방식으로 동작합니다.
- [SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbelementarray): 관련 객체 컬렉션을 관리하는 의 하위 클래스입니다. 예를 들어 Finder에 디스크 목록을 요청하거나 iTunes에 플레이리스트 목록을 요청하면, 해당 항목을 나타내는 Scripting Bridge 객체를 담은 형태로 결과를 돌려받습니다.
- [SBObject](https://developer.apple.com/documentation/scriptingbridge/sbobject): scriptable 애플리케이션의 어떤 객체에서든 호출할 수 있는 메서드를 선언하는 클래스입니다. 객체의 요소와 속성을 가져오는 메서드뿐 아니라, 주어진 객체를 새 값으로 설정하는 메서드도 정의합니다.
:::

:::topic-grid
## 프로토콜
- [SBApplicationDelegate](https://developer.apple.com/documentation/scriptingbridge/sbapplicationdelegate): 이 비공식 프로토콜은 대상 애플리케이션이 객체로 보낸 Apple event 오류를 처리하기 위한 delegation 메서드를 정의합니다.
:::
