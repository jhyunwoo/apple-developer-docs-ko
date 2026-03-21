---
route: /documentation/applicationservices
source_url: https://developer.apple.com/documentation/applicationservices
source_locale: en-US
section: docc
content_type: symbol
title: Application Services
original_title: Application Services
source_hash: 9e43c77ff6286c8dcf3a5ec249158794559d2e9661fb2e0d2f72d2e358bd3068
canonical_source: manual-translation
last_crawled_at: '2026-03-13T02:52:08+00:00'
last_translated_at: '2026-03-13T02:52:08+00:00'
---

# Application Services

일반적인 애플리케이션 작업을 수행합니다.

## 개요

이 문서 모음은 Carbon 애플리케이션에 필수적인 여러 서비스를 포함하는 Application Services 프레임워크의 API 레퍼런스를 제공합니다. Application Services 프레임워크에는 QuickDraw와 Font Manager 같은 여러 레거시 기술에 대한 지원도 포함되어 있으며, 이러한 기술은 Quartz 2D와 ATSUI 같은 더 새로운 기술로 대체되었습니다.

:::topic-grid
## 관리자
- [Apple Event Manager](https://developer.apple.com/documentation/applicationservices/apple_event_manager)
- [ColorSync Manager](https://developer.apple.com/documentation/applicationservices/colorsync_manager)
- [Speech Synthesis Manager](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager)
:::

:::topic-grid
## 레퍼런스
- [Carbon Accessibility](https://developer.apple.com/documentation/applicationservices/carbon_accessibility)
- [Core Printing](https://developer.apple.com/documentation/applicationservices/core_printing)
- [AXActionConstants.h](https://developer.apple.com/documentation/applicationservices/axactionconstants_h): 많은 UIElement는 수행할 수 있는 동작 집합을 가집니다. 동작은 단순하게 설계됩니다. 동작은 대체로 UIElement를 마우스로 한 번 클릭해서 할 수 있는 일에 대응합니다. 예를 들어 버튼과 메뉴 항목은 각각 push 또는 pick이라는 단일 동작을 가지며, 스크롤 막대는 page up, page down, up one line, down one line처럼 여러 동작을 가집니다.
- [AXAttributeConstants.h](https://developer.apple.com/documentation/applicationservices/axattributeconstants_h)
- [AXError.h](https://developer.apple.com/documentation/applicationservices/axerror_h): 이러한 오류 코드는 AXUIElement.h에 정의된 손쉬운 사용 함수에서 반환될 수 있습니다.
- [AXNotificationConstants.h](https://developer.apple.com/documentation/applicationservices/axnotificationconstants_h)
- [AXRoleConstants.h](https://developer.apple.com/documentation/applicationservices/axroleconstants_h)
- [AXTextAttributedString.h](https://developer.apple.com/documentation/applicationservices/axtextattributedstring_h): 이 헤더 파일은 attributed string을 나타내는 손쉬운 사용 객체와 함께 사용하는 상수 정의를 포함합니다. attributed string은 문자 범위와 색상, 글꼴 같은 속성의 연관 관계입니다. 손쉬운 사용 객체가 attributed string을 나타내는 경우, 해당 속성의 값은 이 헤더 파일에 정의된 상수를 사용해 속성을 정의하는 attributed string 객체입니다.
- [AXUIElement.h](https://developer.apple.com/documentation/applicationservices/axuielement_h)
- [AXValue.h](https://developer.apple.com/documentation/applicationservices/axvalue_h): 이 헤더는 AXValueType 래퍼와 함께 동작하기 위한 함수와 데이터 타입을 포함합니다.
- [AXValueConstants.h](https://developer.apple.com/documentation/applicationservices/axvalueconstants_h)
- [UniversalAccess.h](https://developer.apple.com/documentation/applicationservices/universalaccess_h): 이 헤더 파일은 애플리케이션이 확대 초점을 제어할 수 있게 하는 함수를 포함합니다. 이러한 함수를 사용하면 애플리케이션은 macOS Universal Access 확대 기능에 사용자 인터페이스의 어느 부분에 초점을 맞춰야 하는지 알려 줄 수 있습니다.
- [ApplicationServices Structures](https://developer.apple.com/documentation/applicationservices/applicationservices_structures)
- [ApplicationServices Enumerations](https://developer.apple.com/documentation/applicationservices/applicationservices_enumerations)
- [ApplicationServices Constants](https://developer.apple.com/documentation/applicationservices/applicationservices_constants)
- [ApplicationServices Functions](https://developer.apple.com/documentation/applicationservices/applicationservices_functions)
- [ApplicationServices Data Types](https://developer.apple.com/documentation/applicationservices/applicationservices_data_types)
:::

:::topic-grid
## 클래스
- [ColorSyncCMM](https://developer.apple.com/documentation/colorsync/colorsynccmm)
- [ColorSyncMutableProfile](https://developer.apple.com/documentation/colorsync/colorsyncmutableprofile)
- [ColorSyncProfile](https://developer.apple.com/documentation/coregraphics/colorsyncprofile)
- [ColorSyncTransform](https://developer.apple.com/documentation/colorsync/colorsynctransform)
- [HIMutableShape](https://developer.apple.com/documentation/applicationservices/himutableshape)
- [HIShape](https://developer.apple.com/documentation/applicationservices/hishape)
- [Pasteboard](https://developer.apple.com/documentation/applicationservices/pasteboard)
- [Translation](https://developer.apple.com/documentation/applicationservices/translation)
- [AXTextMarker](https://developer.apple.com/documentation/applicationservices/axtextmarker)
- [AXTextMarkerRange](https://developer.apple.com/documentation/applicationservices/axtextmarkerrange)
:::

:::topic-grid
## 프로토콜
- [PDEPanel](https://developer.apple.com/documentation/applicationservices/pdepanel)
- [PDEPlugIn](https://developer.apple.com/documentation/applicationservices/pdeplugin)
- [PDEPlugInCallbackProtocol](https://developer.apple.com/documentation/applicationservices/pdeplugincallbackprotocol)
:::
