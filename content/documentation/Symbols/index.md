---
route: /documentation/Symbols
source_url: https://developer.apple.com/documentation/Symbols
source_locale: en-US
section: docc
content_type: symbol
title: Symbols
original_title: Symbols
source_hash: de7e98090e9d88525a8edbfa5f869ec6d872ed16575ed21559019b011609c737
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:01:46+00:00'
last_translated_at: '2026-03-14T03:05:00+09:00'
---

# Symbols

symbol 기반 이미지에 범용 애니메이션을 적용합니다.

## 개요

Symbols 프레임워크는 AppKit, UIKit, SwiftUI 앱에서 [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)를 애니메이션하기 위해 사용할 수 있는 symbol effect에 접근할 수 있게 합니다. 이러한 애니메이션은 서로 다른 동작을 보입니다.

:::term-list
Discrete: 시작부터 끝까지 실행되는 효과입니다.
Indefinite: 제거하거나 비활성화할 때까지 지속되는 효과입니다.
Transition: symbol이 보이거나 사라지도록 애니메이션하는 효과입니다.
Content Transition: 하나의 symbol을 다른 symbol로, 또는 자기 자신의 다른 구성으로 바꾸는 효과입니다.
:::

하나의 symbol effect는 여러 유형의 동작을 동시에 가질 수 있습니다. 예를 들어 pulse effect에 유한한 횟수만 반복되도록 옵션을 추가하면 discrete 동작이 됩니다. 반대로 영원히 반복되도록 옵션을 추가하면 indefinite 동작이 됩니다.

```swift
// Add an effect in SwiftUI.
Image(systemName: "globe")
    // Add effect with discrete behavior to image view.
    .symbolEffect(.pulse, options: .repeat(3))

Image(systemName: "globe")
    // Add effect with indefinite behavior to image view.
    .symbolEffect(.pulse)
```

이미지 view에 표시하는 symbol 기반 이미지에 범용 애니메이션 효과를 적용할 수 있습니다. Symbols 프레임워크는 어떤 UI 프레임워크나 언어를 선택하든 일관된 효과 집합을 제공합니다.

예를 들어 시스템이 Wi-Fi 네트워크를 검색하는 동안 Wi-Fi symbol에 variable color effect를 표시하는 SwiftUI 앱을 생각해 보십시오.

```swift
// Add an effect in SwiftUI.
Image(systemName: "wifi")
    .symbolEffect(.variableColor.reversing)
```

이제 같은 앱의 AppKit 또는 UIKit 버전을 생각해 보십시오. 동일한 효과를 적용해 Wi-Fi 네트워크 검색 애니메이션을 만들 수 있습니다.

:::topic-grid
## symbol effect
- [appear](https://developer.apple.com/documentation/symbols/symboleffect/appear): symbol 기반 이미지의 layer를 개별적으로 또는 전체적으로 나타나게 하는 애니메이션입니다.
- [bounce](https://developer.apple.com/documentation/symbols/symboleffect/bounce): symbol 기반 이미지의 layer에 일시적인 스케일 효과, 즉 bounce를 개별적으로 또는 전체적으로 적용하는 애니메이션입니다.
- [disappear](https://developer.apple.com/documentation/symbols/symboleffect/disappear): symbol 기반 이미지의 layer를 개별적으로 또는 전체적으로 사라지게 하는 애니메이션입니다.
- [pulse](https://developer.apple.com/documentation/symbols/symboleffect/pulse): symbol 기반 이미지의 일부 또는 모든 layer의 opacity를 서서히 바꾸는 애니메이션입니다.
- [scale](https://developer.apple.com/documentation/symbols/symboleffect/scale): symbol 기반 이미지의 layer를 개별적으로 또는 전체적으로 확대 또는 축소하는 애니메이션입니다.
- [variableColor](https://developer.apple.com/documentation/symbols/symboleffect/variablecolor): symbol 기반 이미지의 variable layer opacity를 반복 가능한 순서로 바꾸는 애니메이션입니다.
:::

:::topic-grid
## symbol content transition
- [replace](https://developer.apple.com/documentation/symbols/symboleffect/replace): 한 symbol 기반 이미지의 layer를 다른 symbol의 layer로 바꾸는 애니메이션입니다.
- [automatic](https://developer.apple.com/documentation/symbols/symboleffect/automatic): 문맥에 맞게 기본 애니메이션을 symbol 기반 이미지에 적용하는 transition입니다.
:::

:::topic-grid
## symbol effect 타입
- [AppearSymbolEffect](https://developer.apple.com/documentation/symbols/appearsymboleffect): symbol 기반 이미지의 layer를 개별적으로 또는 전체적으로 나타나게 하는 타입입니다.
- [AutomaticSymbolEffect](https://developer.apple.com/documentation/symbols/automaticsymboleffect): 문맥에 맞게 기본 애니메이션을 symbol 기반 이미지에 적용하는 타입입니다.
- [BounceSymbolEffect](https://developer.apple.com/documentation/symbols/bouncesymboleffect): symbol 기반 이미지의 layer에 일시적인 스케일 효과, 즉 bounce를 개별적으로 또는 전체적으로 적용하는 타입입니다.
- [DisappearSymbolEffect](https://developer.apple.com/documentation/symbols/disappearsymboleffect): symbol 기반 이미지의 layer를 개별적으로 또는 전체적으로 사라지게 하는 타입입니다.
- [PulseSymbolEffect](https://developer.apple.com/documentation/symbols/pulsesymboleffect): symbol 기반 이미지의 일부 또는 모든 layer의 opacity를 서서히 바꾸는 타입입니다.
- [ReplaceSymbolEffect](https://developer.apple.com/documentation/symbols/replacesymboleffect): 한 symbol 기반 이미지의 layer를 다른 symbol의 layer로 바꾸는 타입입니다.
- [ScaleSymbolEffect](https://developer.apple.com/documentation/symbols/scalesymboleffect): symbol 기반 이미지의 layer를 개별적으로 또는 전체적으로 확대 또는 축소하는 타입입니다.
- [VariableColorSymbolEffect](https://developer.apple.com/documentation/symbols/variablecolorsymboleffect): symbol 기반 이미지의 variable layer opacity를 반복 가능한 순서로 바꾸는 타입입니다.
- [BreatheSymbolEffect](https://developer.apple.com/documentation/symbols/breathesymboleffect): symbol 이미지에 Breathe 애니메이션을 적용하는 symbol effect입니다.
- [RotateSymbolEffect](https://developer.apple.com/documentation/symbols/rotatesymboleffect): symbol 이미지에 Rotate 애니메이션을 적용하는 symbol effect입니다.
- [WiggleSymbolEffect](https://developer.apple.com/documentation/symbols/wigglesymboleffect): symbol 이미지에 Wiggle 애니메이션을 적용하는 symbol effect입니다.
:::

:::topic-grid
## symbol effect 옵션
- [SymbolEffectOptions](https://developer.apple.com/documentation/symbols/symboleffectoptions): effect가 symbol 기반 이미지에 어떻게 적용될지 구성하는 옵션입니다.
:::

:::topic-grid
## symbol effect protocol
- [SymbolEffect](https://developer.apple.com/documentation/symbols/symboleffect): symbol 기반 이미지에 적용하는 presentation effect입니다.
- [DiscreteSymbolEffect](https://developer.apple.com/documentation/symbols/discretesymboleffect): 일시적 애니메이션을 수행하는 effect입니다.
- [IndefiniteSymbolEffect](https://developer.apple.com/documentation/symbols/indefinitesymboleffect): 비활성화하거나 제거할 때까지 symbol에 계속 영향을 주는 애니메이션입니다.
- [ContentTransitionSymbolEffect](https://developer.apple.com/documentation/symbols/contenttransitionsymboleffect): symbol 사이 또는 동일 symbol의 서로 다른 구성 사이를 애니메이션하는 effect입니다.
- [TransitionSymbolEffect](https://developer.apple.com/documentation/symbols/transitionsymboleffect): symbol이 나타나거나 사라지도록 애니메이션하는 effect입니다.
:::

:::topic-grid
## 구조체
- [DrawOffSymbolEffect](https://developer.apple.com/documentation/symbols/drawoffsymboleffect): symbol 이미지에 DrawOff 애니메이션을 적용하는 symbol effect입니다.
- [DrawOnSymbolEffect](https://developer.apple.com/documentation/symbols/drawonsymboleffect): symbol 이미지에 DrawOn 애니메이션을 적용하는 symbol effect입니다.
:::
