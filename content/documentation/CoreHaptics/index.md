---
route: /documentation/CoreHaptics
source_url: https://developer.apple.com/documentation/CoreHaptics
source_locale: en-US
section: docc
content_type: symbol
title: Core Haptics
original_title: Core Haptics
source_hash: 79475eea80e1aa29cff9db3e140c6c7c03ccce186145448e23d6644054246516
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:18+00:00'
last_translated_at: '2026-03-13T10:02:00+00:00'
---

# Core Haptics

iOS 앱의 햅틱 피드백을 사용자화하기 위해 햅틱 패턴을 구성하고 재생합니다.

## 개요

Core Haptics를 사용하면 앱에 사용자 정의 햅틱 및 오디오 피드백을 추가할 수 있습니다. 햅틱을 사용하면 사용자의 주의를 끌고 동작을 강화하는 촉각 및 오디오 피드백으로 물리적으로 사용자와 상호 작용할 수 있습니다. picker, switch, slider 같은 일부 시스템 제공 인터페이스 요소는 사용자가 상호 작용할 때 자동으로 햅틱 피드백을 제공합니다. Core Haptics를 사용하면 기본 패턴을 넘어 햅틱을 구성하고 결합하여 이 기능을 확장할 수 있습니다.

앱은 햅틱 이벤트([CHHapticEvent](https://developer.apple.com/documentation/corehaptics/chhapticevent))라고 하는 기본 구성 요소로 만든 사용자 정의 햅틱 패턴을 재생할 수 있습니다. 이벤트는 스위치를 토글할 때의 피드백처럼 일시적일 수도 있고, 벨소리의 진동이나 소리처럼 연속적일 수도 있습니다. 일시적 패턴과 연속적 패턴을 독립적으로 사용할 수도 있고, 둘을 정밀하게 조합해 패턴을 구성할 수도 있습니다. 또 다른 햅틱 이벤트 유형을 사용하면 패턴의 일부로 사용자 정의 오디오 콘텐츠를 재생할 수 있습니다.

:::topic-grid
## 필수 항목
- [앱이 햅틱을 재생하도록 준비하기](https://developer.apple.com/documentation/corehaptics/preparing-your-app-to-play-haptics): 앱이 햅틱을 재생할 수 있도록 설정합니다.
- [단일 탭 햅틱 패턴 재생하기](https://developer.apple.com/documentation/corehaptics/playing-a-single-tap-haptic-pattern): dictionary literal을 inline으로 사용해 일시적 햅틱 패턴을 만들고 재생합니다.
- [CHHapticEngine](https://developer.apple.com/documentation/corehaptics/chhapticengine): 햅틱 서버와의 연결을 나타내는 객체입니다.
- [CHHapticPattern](https://developer.apple.com/documentation/corehaptics/chhapticpattern): 햅틱 파형을 나타내는 객체입니다.
- [CHHapticPatternPlayer](https://developer.apple.com/documentation/corehaptics/chhapticpatternplayer): 고정 파라미터로 햅틱 패턴을 재생할 수 있는 표준 패턴 플레이어를 정의하는 프로토콜입니다.
- [CHHapticAdvancedPatternPlayer](https://developer.apple.com/documentation/corehaptics/chhapticadvancedpatternplayer): 루프, 탐색, 일시 정지, 재개가 가능한 고급 패턴 플레이어를 정의하는 프로토콜입니다.
:::

:::topic-grid
## 프로그래밍 방식 햅틱
- [햅틱으로 풍부한 앱 경험 제공하기](https://developer.apple.com/documentation/corehaptics/delivering-rich-app-experiences-with-haptics): 핵심 상호 작용 순간에 햅틱과 사운드 피드백을 도입해 앱 경험을 향상합니다.
- [충돌 기반 햅틱 패턴 재생하기](https://developer.apple.com/documentation/corehaptics/playing-collision-based-haptic-patterns): 물체의 충돌 속도에 따라 강도가 달라지는 사용자 정의 햅틱 패턴을 재생합니다.
- [연속 및 일시적 햅틱 파라미터를 실시간으로 업데이트하기](https://developer.apple.com/documentation/corehaptics/updating-continuous-and-transient-haptic-parameters-in-real-time): 사용자 터치에 반응해 연속적 및 일시적 햅틱 패턴을 생성합니다.
- [CHHapticEvent](https://developer.apple.com/documentation/corehaptics/chhapticevent): 단일 햅틱 또는 오디오 이벤트를 설명하는 객체입니다.
- [CHHapticEventParameter](https://developer.apple.com/documentation/corehaptics/chhapticeventparameter): 햅틱 패턴의 단일 속성을 나타내는 정적 파라미터 값입니다.
- [CHHapticDynamicParameter](https://developer.apple.com/documentation/corehaptics/chhapticdynamicparameter): 재생 중 속성 값을 변경하기 위해 햅틱 패턴 플레이어로 보내는 값입니다.
- [CHHapticParameterCurve](https://developer.apple.com/documentation/corehaptics/chhapticparametercurve): 재생 중 속성 값을 점진적으로 변경하기 위해 햅틱 패턴 플레이어로 보내는 곡선입니다.
:::

:::topic-grid
## 파일 기반 햅틱
- [파일에서 사용자 정의 햅틱 패턴 재생하기](https://developer.apple.com/documentation/corehaptics/playing-a-custom-haptic-pattern-from-a-file): 미리 설계된 Apple Haptic Audio Pattern 파일을 샘플링하고, 직접 만든 패턴을 재생하는 방법을 배웁니다.
- [AHAP 파일에서 햅틱 패턴 표현하기](https://developer.apple.com/documentation/corehaptics/representing-haptic-patterns-in-ahap-files): Apple Haptic and Audio Pattern(AHAP) 파일 형식을 이해합니다.
:::

:::topic-grid
## 게임 컨트롤러 햅틱
- [게임 컨트롤러에서 햅틱 재생하기](https://developer.apple.com/documentation/corehaptics/playing-haptics-on-game-controllers): Core Haptics를 사용해 지원되는 게임 컨트롤러에 햅틱 피드백을 추가합니다.
:::

:::topic-grid
## 햅틱 오류
- [CoreHapticsErrorDomain](https://developer.apple.com/documentation/corehaptics/corehapticserrordomain): 햅틱 오류 도메인의 문자열 표현입니다.
- [CHHapticError](https://developer.apple.com/documentation/corehaptics/chhapticerror): 프레임워크 오류를 나타내는 구조체입니다.
- [CHHapticError.Code](https://developer.apple.com/documentation/corehaptics/chhapticerror/code): 프레임워크 작업용 오류 코드입니다.
:::

:::topic-grid
## 변수
- [CHHapticAudioResourceKeyLoopEnabled](https://developer.apple.com/documentation/corehaptics/chhapticaudioresourcekeyloopenabled): 오디오 재생을 반복할지 나타내는 불리언 값용 키입니다.
- [CHHapticAudioResourceKeyUseVolumeEnvelope](https://developer.apple.com/documentation/corehaptics/chhapticaudioresourcekeyusevolumeenvelope): 오디오 파일 재생이 envelope를 사용해 fade in/out 할지 나타내는 불리언 값용 키입니다.
:::

:::topic-grid
## 타입 별칭
- [CHHapticAudioResourceKey](https://developer.apple.com/documentation/corehaptics/chhapticaudioresourcekey): 오디오 리소스의 재생 동작을 식별하는 키 타입 별칭입니다.
:::
