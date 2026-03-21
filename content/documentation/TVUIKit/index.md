---
route: /documentation/TVUIKit
source_url: https://developer.apple.com/documentation/TVUIKit
source_locale: en-US
section: docc
content_type: symbol
title: TVUIKit
original_title: TVUIKit
source_hash: 9348681ae1627f992086fca6ce23f192360606d297e51e427787f8fead579182
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:22:48+00:00'
last_translated_at: '2026-03-13T09:02:00+00:00'
---

# TVUIKit

네이티브 앱에서 Apple TV의 공통 사용자 인터페이스 요소를 표시합니다.

## 개요

[UIKit](https://developer.apple.com/documentation/UIKit)으로 tvOS 앱을 빌드할 때 [TVUIKit](https://developer.apple.com/documentation/tvuikit)을 사용하면 TV 환경에 맞게 콘텐츠 표시를 더 정교하게 다듬을 수 있습니다. 앱과 Apple TV 사이의 더 깊은 통합을 제공하려면 [TV Services](https://developer.apple.com/documentation/TVServices) 프레임워크를 사용하세요.

Apple 기술을 조합해 훌륭한 Apple TV 경험을 구축하는 방법에 대한 자세한 내용은 [Planning your tvOS app](https://developer.apple.com/tvos/planning/#build-the-data-structures-youll-use-in-your-app)을 참고하세요.

![육각형 모양의 UIKit 프레임워크 아이콘, 오른쪽을 가리키는 화살표, TVUIKit 라벨이 있는 육각형, 다시 오른쪽을 가리키는 화살표, 그리고 TV 화면이 포함된 그림입니다. TV 화면에는 중앙의 야자수 이미지와 좌우로 일부가 보이는 다른 이미지들이 표시됩니다.](https://developer.apple.com)

:::topic-grid
## 콘텐츠 컬렉션
- [전체 화면 레이아웃으로 몰입형 경험 만들기](https://developer.apple.com/documentation/tvuikit/creating-immersive-experiences-using-a-full-screen-layout): tvOS 경험을 극대화하는 collection view로 콘텐츠를 표시합니다.
- [TVCollectionViewFullScreenLayout](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayout): 항목을 탐색 가능한 전체 화면 표시 형식으로 구성하는 collection view 레이아웃입니다.
- [TVCollectionViewDelegateFullScreenLayout](https://developer.apple.com/documentation/tvuikit/tvcollectionviewdelegatefullscreenlayout): 셀 전환 중 발생하는 이벤트 알림을 보내는 메서드입니다.
- [TVCollectionViewFullScreenCell](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell): 전체 화면 표시 형식에서 사용하는 전체 화면 셀입니다.
- [TVCollectionViewFullScreenLayoutAttributes](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayoutattributes): collection view 레이아웃의 모양을 관리하는 속성입니다.
:::

:::topic-grid
## 콘텐츠 뷰
- [TVMediaItemContentView](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentview): 영화나 TV 프로그램 같은 미디어 콘텐츠를 나타내는 뷰입니다.
- [TVMonogramContentView](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview): 사람의 원형 이미지나 이니셜을 담는 뷰입니다.
:::

:::topic-grid
## 숫자 입력
- [TVDigitEntryViewController](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller): 앱에서 암호처럼 숫자를 입력할 수 있게 해 주는 뷰 컨트롤러입니다.
:::

:::topic-grid
## Lockup 뷰
- [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview): 영화 포스터 같은 मुख्य 콘텐츠와 선택적 헤더 및 푸터를 보여 주는 포커스 가능한 뷰입니다.
- [TVLockupViewComponent](https://developer.apple.com/documentation/tvuikit/tvlockupviewcomponent): lockup view 상태 변경에 응답하는 프로토콜입니다.
- [TVLockupHeaderFooterView](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview): 헤더 및 푸터 정보를 담는 뷰입니다.
- [TVCardView](https://developer.apple.com/documentation/tvuikit/tvcardview): 모든 하위 뷰에 적용하는 모션 효과로 포커스 상호 작용에 반응하는 뷰입니다.
- [TVPosterView](https://developer.apple.com/documentation/tvuikit/tvposterview): 이미지, 헤더, 푸터를 표시하도록 최적화된 뷰입니다.
- [TVCaptionButtonView](https://developer.apple.com/documentation/tvuikit/tvcaptionbuttonview): 사용자 상호 작용에 반응하는 버튼 형태의 뷰입니다.
- [TVMonogramView](https://developer.apple.com/documentation/tvuikit/tvmonogramview): 사람의 원형 이미지나 이니셜과 함께 푸터 뷰를 포함하는 특수 lockup 뷰입니다.
:::
