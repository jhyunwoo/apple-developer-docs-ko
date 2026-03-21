---
route: /documentation/TouchController
source_url: https://developer.apple.com/documentation/TouchController
source_locale: en-US
section: docc
content_type: symbol
title: Touch Controller
original_title: Touch Controller
source_hash: 2016baa4dc85f0799d713e8500452474b853b8cc4ffefac27a0666acf11e1451
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:21:35+00:00'
last_translated_at: '2026-03-13T23:21:47+09:00'
---

# Touch Controller

Metal 기반 게임에 화면상의 터치 컨트롤을 통합합니다.

## 개요

Touch Controller를 사용하면 게임에 맞춘 사용자 정의형 대화형 터치 컨트롤을 추가할 수 있습니다. 이 프레임워크는 버튼, 방향 패드, thumbstick, throttle control, touchpad처럼 다양한 조작 체계를 지원하는 컨트롤 모음을 제공합니다. Game Controller 프레임워크는 각 컨트롤을 지원하며, 이를 [GCController](https://developer.apple.com/documentation/GameController/GCController) 인스턴스를 통해 노출합니다.

[TCTouchController](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller) 클래스를 터치 컨트롤을 관리하고 렌더링하는 중심 지점으로 사용하십시오. 컨트롤의 시각적 모양을 구성하려면 [TCControlContents](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents)와 [TCControlImage](https://developer.apple.com/documentation/touchcontroller/tccontrolimage)를 사용합니다. [TCControlContents](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents)를 사용하면 시스템이 제공하는 자산을 바탕으로 일관된 모양과 느낌을 만들 수 있습니다.

:::topic-grid
## 핵심
- [TCTouchController](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller): Metal을 사용하는 게임용 화면상 터치 컨트롤을 만들고 사용자화할 수 있게 하는 객체입니다.
:::

:::topic-grid
## 컨트롤
- [TCControl](https://developer.apple.com/documentation/touchcontroller/tccontrol): 모든 터치 컨트롤의 기본 속성과 메서드를 정의하는 protocol입니다.
- [TCButton](https://developer.apple.com/documentation/touchcontroller/tcbutton): 단일 화면상 버튼을 나타내는 컨트롤입니다.
- [TCDirectionPad](https://developer.apple.com/documentation/touchcontroller/tcdirectionpad): 방향 패드를 나타내는 객체입니다.
- [TCSwitch](https://developer.apple.com/documentation/touchcontroller/tcswitch): 단일 화면상 스위치를 나타내는 컨트롤입니다.
- [TCThumbstick](https://developer.apple.com/documentation/touchcontroller/tcthumbstick): 단일 화면상 thumbstick을 나타냅니다.
- [TCThrottle](https://developer.apple.com/documentation/touchcontroller/tcthrottle): 단일 축 입력을 가지는 화면상 throttle을 나타냅니다.
- [TCTouchpad](https://developer.apple.com/documentation/touchcontroller/tctouchpad): 절대 좌표 또는 delta movement를 보고하는 단일 화면상 touchpad를 나타냅니다.
:::

:::topic-grid
## 시각 요소
- [TCControlContents](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents): 터치 컨트롤의 시각적 콘텐츠를 나타냅니다.
- [TCControlImage](https://developer.apple.com/documentation/touchcontroller/tccontrolimage): Metal로 렌더링할 이미지를 나타냅니다.
- [TCControlLayout](https://developer.apple.com/documentation/touchcontroller/tccontrollayout): 컨트롤의 `controlLayout` 속성을 정의하는 protocol입니다.
:::

:::topic-grid
## 시스템 콘텐츠
- [TCControlContents.ButtonShape](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/buttonshape): 버튼의 시각적 형태를 정의합니다.
- [TCControlContents.DpadDirection](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/dpaddirection): 방향 패드 시각 요소의 방향을 정의합니다.
- [TCControlContents.DpadElementStyle](https://developer.apple.com/documentation/touchcontroller/tccontrolcontents/dpadelementstyle): 방향 패드의 각 위/아래/왼쪽/오른쪽 요소에 대한 시각 스타일을 정의합니다.
:::
