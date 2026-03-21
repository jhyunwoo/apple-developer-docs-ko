---
route: /documentation/ScreenSaver
source_url: https://developer.apple.com/documentation/ScreenSaver
source_locale: en-US
section: docc
content_type: symbol
title: Screen Saver
original_title: Screen Saver
source_hash: 689ecd8e6e7c533f947bb0289a2393e8268c368d798aef0950b858bc841af723
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:14:20+00:00'
last_translated_at: '2026-03-13T23:14:51+09:00'
---

# Screen Saver

화면 보호기를 애니메이션하고, 화면 보호기 인프라와 상호 작용합니다.

## 개요

Screen Saver 프레임워크는 사용자 정의 모듈이 Screen Effects 사용자 인터페이스 기능과 상호 작용하기 위한 인터페이스를 정의합니다. 화면 보호기는 Objective-C로 작성하고, 모듈의 사용자 인터페이스는 Cocoa로 구현합니다. 제공되는 함수를 사용해 난수를 만들고 사각형을 가운데 정렬할 수 있습니다.

화면 보호기를 만들려면 `.saver` 접미사를 가진 bundle 디렉터리를 만든 뒤, 시스템의 `Library/Screen Savers` 디렉터리 중 하나에 설치합니다. bundle의 실행 파일에는 [ScreenSaverView](https://developer.apple.com/documentation/screensaver/screensaverview) 하위 클래스를 포함해야 합니다. 이 뷰가 화면 보호기 콘텐츠를 생성할 때 사용하는 인터페이스를 정의합니다. 화면 보호기가 환경설정 정보를 저장해야 한다면 일반적인 [UserDefaults](https://developer.apple.com/documentation/Foundation/UserDefaults) 대신 [ScreenSaverDefaults](https://developer.apple.com/documentation/screensaver/screensaverdefaults) 클래스를 사용하십시오.

화면 보호기는 screen saver engine용 plug-in이므로, 화면 보호기 바이너리는 실행 중인 engine과 동일한 하드웨어 아키텍처를 지원해야 합니다. 일반 앱과 마찬가지로 screen saver engine은 호스트 컴퓨터의 네이티브 아키텍처를 사용합니다. 완전한 호환성을 위해 화면 보호기가 `x86_64`와 `arm64` 아키텍처를 모두 지원하도록 하십시오.

### 시스템이 화면 보호기를 실행하는 방식

macOS가 화면 보호기를 시작하면 시스템은 다음과 같이 동작합니다.

1. 화면을 검게 페이드합니다.
2. [ScreenSaverView](https://developer.apple.com/documentation/screensaver/screensaverview) 하위 클래스를 인스턴스화하고 [init(frame:isPreview:)](https://developer.apple.com/documentation/screensaver/screensaverview/init(frame:ispreview:)) 메서드를 호출합니다.
3. 윈도우를 만들고 그 안에 [ScreenSaverView](https://developer.apple.com/documentation/screensaver/screensaverview) 하위 클래스를 설치합니다.
4. 윈도우를 활성화하고 순서를 설정합니다.
5. 뷰의 [draw(_:)](https://developer.apple.com/documentation/screensaver/screensaverview/draw(_:)) 메서드를 호출해 초기 상태를 그리게 합니다.
6. 화면을 다시 페이드 인하여 앞쪽에 있는 윈도우를 보이게 합니다.
7. 뷰의 [startAnimation()](https://developer.apple.com/documentation/screensaver/screensaverview/startanimation()) 메서드를 호출하며, 이 메서드에서 애니메이션 관련 상태를 설정합니다.
8. 뷰의 [animateOneFrame()](https://developer.apple.com/documentation/screensaver/screensaverview/animateoneframe()) 메서드를 반복적으로 호출합니다.

사용자가 어떤 동작을 하면 시스템은 뷰의 [stopAnimation()](https://developer.apple.com/documentation/screensaver/screensaverview/stopanimation()) 메서드를 호출해 화면 보호기를 중지합니다. 이 메서드에서는 [startAnimation()](https://developer.apple.com/documentation/screensaver/screensaverview/startanimation())에서 설정한 상태 정보를 정리하십시오.

:::note Note
[stopAnimation()](https://developer.apple.com/documentation/screensaver/screensaverview/stopanimation())이나 [startAnimation()](https://developer.apple.com/documentation/screensaver/screensaverview/startanimation())은 애니메이션을 즉시 시작하거나 중지하지 않습니다. 시스템은 [stopAnimation()](https://developer.apple.com/documentation/screensaver/screensaverview/stopanimation())을 호출한 뒤에도 계속 [animateOneFrame()](https://developer.apple.com/documentation/screensaver/screensaverview/animateoneframe())을 호출할 수 있습니다.
:::

:::topic-grid
## 인터페이스
- [ScreenSaverView](https://developer.apple.com/documentation/screensaver/screensaverview): 하위 클래스가 화면 보호기 인프라와 상호 작용하기 위한 인터페이스를 정의하는 추상 클래스입니다.
- [ScreenSaverDefaults](https://developer.apple.com/documentation/screensaver/screensaverdefaults): 화면 보호기용 사용자 기본값을 저장하고 복원하는 메서드 집합을 정의하는 클래스입니다.
:::

:::topic-grid
## 유틸리티
- [SSRandomIntBetween(_:_:)](https://developer.apple.com/documentation/screensaver/ssrandomintbetween(_:_:)): 무작위 정수 값을 반환합니다.
- [SSRandomFloatBetween(_:_:)](https://developer.apple.com/documentation/screensaver/ssrandomfloatbetween(_:_:)): 무작위 부동소수점 값을 반환합니다.
- [SSRandomPointForSizeWithinRect(_:_:)](https://developer.apple.com/documentation/screensaver/ssrandompointforsizewithinrect(_:_:)): 무작위 점을 반환합니다.
- [SSCenteredRectInRect(_:_:)](https://developer.apple.com/documentation/screensaver/sscenteredrectinrect(_:_:)): 가운데 정렬된 사각형을 반환합니다.
:::
