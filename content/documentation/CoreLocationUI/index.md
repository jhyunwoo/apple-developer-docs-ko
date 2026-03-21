---
route: /documentation/CoreLocationUI
source_url: https://developer.apple.com/documentation/CoreLocationUI
source_locale: en-US
section: docc
content_type: symbol
title: CoreLocationUI
original_title: CoreLocationUI
source_hash: 8599b5266000c1d5313e6978a653e659b869248be45c8b8380b3c6c4ec8cab7d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:25:15+00:00'
last_translated_at: '2026-03-13T23:12:00+09:00'
---

# CoreLocationUI

표준화되고 안전한 UI를 통해 사용자의 위치 데이터 접근을 간소화합니다.

## 개요

CoreLocationUI 프레임워크에는 위치 데이터 접근 권한을 요청하기 위해 [Core Location](https://developer.apple.com/documentation/CoreLocation)과 안전하게 상호 작용하는 표준화된 UI가 포함되어 있습니다.

CoreLocationUI는 SwiftUI 앱을 위한 [LocationButton](https://developer.apple.com/documentation/corelocationui/locationbutton)과 UIKit 앱을 위한 [CLLocationButton](https://developer.apple.com/documentation/corelocationui/cllocationbutton)을 제공합니다. 사용자가 앱이 자신의 위치를 가져오기 위한 일회성 권한을 부여하길 원할 때 이 버튼들을 UI에 추가합니다. 버튼 스타일은 표준 Core Location 디자인 언어와 일관되므로, 사용자는 상호 작용할 때 친숙함과 신뢰감을 느낄 수 있습니다.

:::note Note
위치 버튼은 Mac Catalyst로 빌드한 Mac 앱과 visionOS에서 실행되는 호환 iPad 및 iPhone 앱에서는 사용자 입력을 무시합니다.
:::

:::topic-grid
## 위치 권한 부여
- [Sharing Your Location to Find a Park](https://developer.apple.com/documentation/corelocationui/sharing-your-location-to-find-a-park): 사용자화 가능한 위치 버튼을 사용해 위치 접근 권한을 요청합니다.
- [LocationButton](https://developer.apple.com/documentation/corelocationui/locationbutton): 일회성 위치 권한을 부여하는 SwiftUI 버튼입니다.
- [CLLocationButton](https://developer.apple.com/documentation/corelocationui/cllocationbutton): 일회성 위치 권한을 부여하는 버튼입니다.
:::

:::topic-grid
## 버튼 사용자화
- [CLLocationButtonIcon](https://developer.apple.com/documentation/corelocationui/cllocationbuttonicon): 버튼의 위치 화살표 아이콘 스타일을 지정하는 상수입니다.
- [CLLocationButtonLabel](https://developer.apple.com/documentation/corelocationui/cllocationbuttonlabel): 버튼 레이블의 텍스트를 지정하는 상수입니다.
:::
