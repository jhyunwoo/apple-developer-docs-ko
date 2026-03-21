---
route: /documentation/TipKit
source_url: https://developer.apple.com/documentation/TipKit
source_locale: en-US
section: docc
content_type: symbol
title: TipKit
original_title: TipKit
source_hash: 5d380fb94850009afb963c4ae575708e0383d679a7fc259485cb149a0793d27b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:14:58+00:00'
last_translated_at: '2026-03-13T16:45:00+09:00'
---

# TipKit

사용자가 앱의 기능을 발견할 수 있도록 도와주는 팁을 표시합니다.

## 개요

TipKit을 사용하면 사용자가 아직 스스로 발견하지 못한 새롭거나 흥미롭거나 사용되지 않은 기능을 강조하는 맥락 기반 팁을 보여 줄 수 있습니다.

![일반적인 앱에 일반적인 팁이 추가된 모습을 보여 주는 개념 이미지입니다.](https://developer.apple.com)

[Tip](https://developer.apple.com/documentation/tipkit/tip) 프로토콜을 사용해 팁의 콘텐츠와 팁이 나타나는 조건을 정의합니다. 그런 다음 [TipView](https://developer.apple.com/documentation/tipkit/tipview)를 사용해 새 기능에 주의를 끌 수 있습니다.

앱의 팁을 설계할 때는 사용자를 압도하지 않도록 주의하십시오. 사용자가 아직 스스로 발견하지 못한 비직관적 기능을 강조할 때만 팁을 드물게 사용하십시오. 마찬가지로 사용자가 앱을 사용할 때마다 팁을 표시하는 것도 피해야 합니다. 불필요하게 팁이 나타나면 산만해질 수 있습니다. 팁을 사용해 앱을 단계별로 안내하거나 광고 및 프로모션 목적으로 사용하지 마십시오.

팁에 대한 디자인 지침은 [Human Interface Guidelines > Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help)를 참고하십시오.

:::note Related session from WWDC24
Session 10070: [Customize feature discovery with TipKit](https://developer.apple.com/videos/play/wwdc2024/10070/)
:::

:::note Related session from WWDC23
Session 10229: [Make features discoverable with TipKit](https://developer.apple.com/videos/play/wwdc2023/10229/)
:::

```swift
import SwiftUI
import TipKit

// Define your tip's content.
struct FavoriteLandmarkTip: Tip {
    var title: Text {
        Text("Save as a Favorite")
    }

    var message: Text? {
        Text("Your favorite landmarks always appear at the top of the list.")
    }

    var image: Image? {
        Image(systemName: "star")
    }
}

@main
struct LandmarkTips: App {
    // Create an instance of your tip.
    var favoriteLandmarkTip = FavoriteLandmarkTip()

    var body: some Scene {
        WindowGroup {
            VStack {
                // Place the tip view near the feature you want to highlight.
                TipView(favoriteLandmarkTip, arrowEdge: .bottom)

                Image(systemName: "star")
                    .imageScale(.large)
                Spacer()
            }
            .task {
                // Configure and load your tips at app launch.
                do {
                    try Tips.configure()
                } 
                catch {
                    // Handle TipKit errors
                    print("Error initializing TipKit \(error.localizedDescription)")
                }
            }
        }
    }
}
```

:::topic-grid
## 핵심 사항
- [Highlighting app features with TipKit](https://developer.apple.com/documentation/tipkit/highlightingappfeatureswithtipkit): 팁을 사용해 앱의 새 기능에 주의를 끕니다.
:::

:::topic-grid
## 콘텐츠
- [Tip](https://developer.apple.com/documentation/tipkit/tip): 팁의 콘텐츠와 표시 조건을 설정하는 타입입니다.
- [TipGroup](https://developer.apple.com/documentation/tipkit/tipgroup): 특정 순서를 사용하거나 표시 자격이 있는 첫 번째 팁을 기준으로 한 번에 하나씩 표시할 수 있는 팁 모음입니다.
:::

:::topic-grid
## 구성
- [configure(_:)](https://developer.apple.com/documentation/tipkit/tips/configure(_:)): 앱의 모든 팁에 대한 영구 상태를 로드하고 구성합니다.
- [cloudKitContainer(_:)](https://developer.apple.com/documentation/tipkit/tips/configurationoption/cloudkitcontainer(_:)): 팁 동기화에 사용하는 CloudKit 컨테이너를 설정합니다.
- [datastoreLocation(_:)](https://developer.apple.com/documentation/tipkit/tips/configurationoption/datastorelocation(_:)): 팁 datastore의 사용자 정의 위치를 지정합니다.
- [displayFrequency(_:)](https://developer.apple.com/documentation/tipkit/tips/configurationoption/displayfrequency(_:)): 다른 팁이 표시된 뒤 앱에서 새 팁을 얼마나 자주 제시할지 사용자화합니다.
:::

:::topic-grid
## 뷰
- [TipView](https://developer.apple.com/documentation/tipkit/tipview): 인라인 팁을 나타내는 사용자 인터페이스 요소입니다.
- [popoverTip(_:arrowEdge:action:)](https://developer.apple.com/documentation/SwiftUI/View/popoverTip(_:arrowEdge:action:)): 수정된 view에 popover tip을 표시합니다.
:::

:::topic-grid
## UIKit 뷰
- [TipUIView](https://developer.apple.com/documentation/tipkit/tipuiview): UIKit 앱에서 팁을 나타내는 사용자 인터페이스 요소입니다.
- [TipUIPopoverViewController](https://developer.apple.com/documentation/tipkit/tipuipopoverviewcontroller): UIKit 앱에서 popover tip을 표시하는 view controller입니다.
- [TipUICollectionViewCell](https://developer.apple.com/documentation/tipkit/tipuicollectionviewcell): 팁을 포함하는 collection view cell입니다.
- [TipUICollectionReusableView](https://developer.apple.com/documentation/tipkit/tipuicollectionreusableview): 팁을 나타내는 UICollectionReusableView 하위 클래스입니다.
:::

:::topic-grid
## AppKit 뷰
- [TipNSView](https://developer.apple.com/documentation/tipkit/tipnsview): AppKit 앱에서 팁을 나타내는 사용자 인터페이스 요소입니다.
- [TipNSPopover](https://developer.apple.com/documentation/tipkit/tipnspopover): AppKit 앱에서 popover tip을 표시하는 NSPopover 하위 클래스입니다.
:::

:::topic-grid
## 표시 규칙
- [Rule](https://developer.apple.com/documentation/tipkit/tips/rule): 팁을 표시하기 전에 충족해야 하는 조건입니다.
- [Parameter](https://developer.apple.com/documentation/tipkit/tips/parameter): 감싼 값의 상태를 모니터링해 값이 바뀔 때 의존하는 팁 규칙을 다시 평가하는 타입입니다.
- [Event](https://developer.apple.com/documentation/tipkit/tips/event): 반복 가능한 사용자 정의 동작입니다.
:::

:::topic-grid
## 뷰 스타일
- [tipViewStyle(_:)](https://developer.apple.com/documentation/SwiftUI/View/tipViewStyle(_:)): 뷰 계층 내 TipView에 지정한 스타일을 설정합니다.
- [TipViewStyle](https://developer.apple.com/documentation/tipkit/tipviewstyle): 뷰 계층 내 모든 팁에 사용자 정의 모양을 적용하는 타입입니다.
- [TipViewStyleConfiguration](https://developer.apple.com/documentation/tipkit/tipviewstyleconfiguration): 팁의 구성을 담는 컨테이너 타입입니다.
- [MiniTipViewStyle](https://developer.apple.com/documentation/tipkit/minitipviewstyle): TipView의 기본 스타일입니다.
:::

:::topic-grid
## 테스트
- [showAllTipsForTesting()](https://developer.apple.com/documentation/tipkit/tips/showalltipsfortesting()): 팁의 표시 규칙 자격이나 표시 빈도 상태와 관계없이 UI 테스트를 위해 모든 팁을 표시합니다.
- [showTipsForTesting(_:)](https://developer.apple.com/documentation/tipkit/tips/showtipsfortesting(_:)): 특정 팁의 UI 테스트를 위해 표시 규칙 자격이나 표시 빈도 상태와 관계없이 지정된 팁을 표시합니다.
- [hideAllTipsForTesting()](https://developer.apple.com/documentation/tipkit/tips/hidealltipsfortesting()): 팁 없는 UI 테스트를 위해 표시 규칙 자격과 관계없이 모든 팁을 숨깁니다.
- [hideTipsForTesting(_:)](https://developer.apple.com/documentation/tipkit/tips/hidetipsfortesting(_:)): 특정 팁 없는 UI 테스트를 위해 표시 규칙 자격과 관계없이 지정된 팁을 숨깁니다.
- [resetDatastore()](https://developer.apple.com/documentation/tipkit/tips/resetdatastore()): 팁의 datastore를 초기 상태로 재설정하여 팁 표시 규칙과 자격을 다시 테스트합니다.
:::

:::topic-grid
## 공통 타입
- [AnyTip](https://developer.apple.com/documentation/tipkit/anytip): 타입이 지워진 팁 값입니다.
- [TipKitError](https://developer.apple.com/documentation/tipkit/tipkiterror): localized tip kit 오류입니다.
- [Option](https://developer.apple.com/documentation/tipkit/tipoption): 팁 동작에 적용할 수 있는 다양한 사용자화를 나타내는 타입입니다.
:::

:::topic-grid
## 열거형
- [Tips](https://developer.apple.com/documentation/tipkit/tips): TipKit namespace입니다.
:::
