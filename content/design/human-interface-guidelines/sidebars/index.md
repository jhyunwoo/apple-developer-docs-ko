---
route: /design/human-interface-guidelines/sidebars
source_url: https://developer.apple.com/design/human-interface-guidelines/sidebars
source_locale: ko-KR
section: hig
content_type: article
title: 사이드바
original_title: Sidebars
source_hash: 0c0a4ce7d99a1d7b8af54b9794356c1bf8e854c2abf1c79220f553bd6e2c9c36
canonical_source: official-ko
last_crawled_at: '2026-03-13T15:06:55+00:00'
last_translated_at: '2026-03-14T00:06:53+09:00'
---

# 사이드바

사이드바는 보기의 앞쪽에 나타나며 이를 사용하여 앱 또는 게임에서 섹션을 탐색할 수 있습니다.

![제목, 섹션 및 일부 폴더를 표시하는 윈도우 사이드바 상단 부분의 스타일화된 모양이 표시되어 있음. 여섯 가지 색상으로 된 기존 Apple 로고의 빨간색을 은은하게 반영하는 빨간색 색조가 이미지에 적용됨.](https://developer.apple.com)

사이드바는 보기의 가장자리에 고정되지 않고 콘텐츠 위에 떠 있는 형태로 표시됩니다. 이는 앱의 정보 계층을 넓고 평평하게 보여주어 사람들이 여러 동등한 콘텐츠 영역이나 모드에 동시에 접근할 수 있습니다.

사이드바에는 세로 및 가로 공간이 많이 필요합니다. 공간이 제한되어 있거나, 화면의 더 많은 부분을 다른 정보나 기능에 할애하려는 경우에는 [탭 막대](https://developer.apple.com/kr/design/human-interface-guidelines/tab-bars)와 같이 좀 더 콤팩트한 제어기가 더 나은 탐색 경험을 제공할 수 있습니다. 지침을 보려면 [레이아웃](https://developer.apple.com/kr/design/human-interface-guidelines/layout)의 내용을 참조하십시오.

## 모범 사례

**사이드바 아래로 콘텐츠를 확장하십시오.** iOS, iPadOS 및 macOS에서는 도구 막대와 탭 막대 등의 다른 제어기와 마찬가지로, 사이드바가 [머티리얼](https://developer.apple.com/kr/design/human-interface-guidelines/materials#Liquid-Glass) 레이어에서 콘텐츠 위에 떠 있는 형태로 표시됩니다. 사이드바가 분리되어 떠 있는 느낌을 강화하려면 콘텐츠를 가로로 스크롤되도록 하거나 배경 확장 보기를 적용하여 사이드바 아래로 콘텐츠를 확장하십시오. 이때 배경 확장 보기는 인접한 콘텐츠를 반영하여 콘텐츠가 사이드바 아래까지 이어지는 듯한 인상을 줍니다. 개발자 지침을 보려면 [backgroundExtensionEffect()](https://developer.apple.com/documentation/SwiftUI/View/backgroundExtensionEffect())의 내용을 참조하십시오.

**가능할 경우, 사람들이 사이드바의 콘텐츠를 사용자화하도록 하십시오.** 사이드바를 통해 사람들이 앱에서 중요한 영역으로 이동할 수 있기 때문에 사람들이 가장 중요한 영역과 나타나는 순서를 결정할 수 있을 때 유용하게 사용할 수 있습니다.

**앱에 콘텐츠가 많은 경우 펼침 제어기로 계층을 그룹화하십시오.** [펼침 제어기](https://developer.apple.com/kr/design/human-interface-guidelines/disclosure-controls)를 사용하면 사이드바의 세로 공간을 적절한 수준으로 유지하는 데 도움이 됩니다.

**익숙한 기호를 사용하여 사이드바의 항목을 나타내는 것을 고려하십시오.** [SF Symbols](https://developer.apple.com/kr/design/human-interface-guidelines/sf-symbols)는 앱에서 항목을 나타내는 데 사용할 수 있는 다양한 범위의 사용자화할 수 있는 기호를 제공합니다. 사용자 설정 아이콘을 사용해야 하는 경우에는 비트맵 이미지를 사용하는 대신 [SF Symbols](https://developer.apple.com/kr/design/human-interface-guidelines/sf-symbols#Custom-symbols)를 만드는 것을 고려하십시오. [Apple Design Resources](https://developer.apple.com/design/resources/#sf-symbols)에서 SF Symbols 앱을 다운로드하십시오.

**사람들이 사이드바를 가리도록 허용하는 것을 고려하십시오.** 사람들은 때때로 콘텐츠 세부사항을 위한 더 넓은 공간을 확보하거나 방해 요인을 줄이기 위해 사이드바를 가리려고 합니다. 가능할 경우, 사람들이 이미 알고 있는 플랫폼별 상호작용 기능을 사용하여 사이드바를 가리거나 표시하도록 하십시오. 예를 들어, iPadOS에서 사람들은 내장 가장자리 쓸어넘기기 제스처를 사용할 것으로 기대합니다. macOS에서는 보기/가리기 버튼을 포함하거나 앱의 보기 메뉴에 사이드바 보기 및 사이드바 가리기 명령을 추가할 수 있습니다. visionOS에서 윈도우는 일반적으로 사이드바에 부합하도록 확장되기 때문에 사람들이 사이드바를 가릴 필요가 거의 없습니다. 쉽게 찾을 수 있도록 유지하려면 기본적으로 사이드바를 가리지 마십시오.

**일반적으로 사이드바에서 두 단계 이하의 계층을 표시하십시오.** 데이터 계층이 두 단계를 초과하면 사이드바 항목과 세부사항 보기 사이에 콘텐츠 목록을 포함하는 Split View 인터페이스를 사용하는 것을 고려하십시오.

**사이드바에 두 단계의 계층을 포함해야 하는 경우, 간결한 설명 레이블을 사용하여 각 그룹의 제목을 지정하십시오.** 레이블을 짧게 유지하려면 불필요한 단어를 생략하십시오.

## 플랫폼 고려 사항

*tvOS에 대한 추가 고려 사항은 없습니다. watchOS에서는 지원되지 않습니다.*

### iOS

**사이드바는 가급적 사용하지 마십시오.** 사이드바는 가로 방향에서 많은 공간을 차지하며 세로 방향에서는 사용할 수 없습니다. 그 대신 [탭 막대](https://developer.apple.com/kr/design/human-interface-guidelines/tab-bars)를 사용하는 것을 고려하십시오. 탭 막대는 공간을 더 적게 차지하며 두 방향 모두에서 표시됩니다.

### iPadOS

탭 보기의 [sidebarAdaptable](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable) 스타일을 사용하여 사이드바를 제공하면 앱이 열릴 때 사이드바 또는 탭 막대를 표시할지 선택하게 됩니다. 두 유형 모두에는 서로 전환할 수 있는 버튼이 포함되어 있습니다. 이 스타일은 회전 및 윈도우 크기 조절에도 자동으로 반응하여, 보기의 너비에 적합한 제어기 버전을 제공합니다.

:::note 개발자 참고 사항
사이드바만 표시하려면 [NavigationSplitView](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView)를 사용하여 Split View의 기본 패널에 사이드바를 표시하거나 [UISplitViewController](https://developer.apple.com/documentation/UIKit/UISplitViewController)를 사용하십시오.
:::

**먼저 탭 막대를 사용하는 것을 고려하십시오.** 탭 막대는 콘텐츠를 더 넓게 보여줄 수 있으며, 여러 앱의 주요 영역 간에 탐색할 수 있는 충분한 유연성을 제공합니다. 탭 막대 크기보다 더 많은 영역을 표시해야 하는 경우, 탭 막대의 변환 가능한 사이드바 스타일 모양을 사용하여 자주 쓰지 않는 콘텐츠에 접근할 수 있도록 할 수 있습니다. 지침을 보려면 [탭 막대](https://developer.apple.com/kr/design/human-interface-guidelines/tab-bars)의 내용을 참조하십시오.

**필요한 경우, 사이드바에 올바른 모양을 적용하십시오.** SwiftUI를 사용하여 사이드바를 생성하지 않는 경우, 모음 보기 목록 레이아웃의 [UICollectionLayoutListConfiguration.Appearance.sidebar](https://developer.apple.com/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct/Appearance-swift.enum/sidebar) 모양을 사용할 수 있습니다. 개발자 지침을 보려면 [UICollectionLayoutListConfiguration.Appearance](https://developer.apple.com/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct/Appearance-swift.enum)의 내용을 참조하십시오.

### macOS

사이드바의 행 높이, 텍스트 및 글리프 크기는 전체 크기에 따라 달라지며, 소형, 중형 또는 대형일 수 있습니다. 크기를 프로그램적으로 설정할 수 있지만, 사람들은 일반 설정에서 다양한 사이드바 아이콘 크기를 선택하여 변경할 수도 있습니다.

**모든 사이드바 아이콘에 고정 색상을 지정하여 앱을 스타일화하지 마십시오.** 기본적으로 사이드바 아이콘은 현재 [accent color](https://developer.apple.com/kr/design/human-interface-guidelines/color#App-accent-colors)을 사용하며 사람들은 사용 중인 모든 앱에서 직접 선택한 강조 색상을 보기를 기대합니다. 고정 색상은 아이콘의 의미를 명확하게 하는 데 도움이 될 수 있지만, 대부분의 사이드바 아이콘은 사람들이 선택하는 색상을 표시해야 합니다.

**컨테이너 윈도우의 크기를 조절할 때 사이드바를 자동으로 가리거나 표시하는 것을 고려하십시오.** 예를 들어, Mail 뷰어 윈도우의 크기를 줄이면 사이드바가 자동으로 축소되어 메시지 콘텐츠를 위한 더 넓은 공간을 확보할 수 있습니다.

**사이드바 하단에 중요한 정보 또는 동작을 넣지 마십시오.** 사람들은 주로 윈도우의 하단 가장자리는 가리는 방식으로 윈도우를 재배치합니다.

### visionOS

**앱의 계층이 많은 경우, 탭 막대에서 탭 내에 사이드바를 사용하는 것을 고려하십시오.** 이 경우, 사이드바가 탭 내에서 보조 탐색을 지원할 수 있습니다. 이렇게 할 경우, 사이드바의 선택 항목이 현재 열려 있는 탭을 변경하지 못하도록 하십시오.

![visionOS에서 음악 앱의 부분적인 스크린샷. 앱의 윈도우에는 음악 보관함을 탐색하기 위한 사이드바가 포함되어 있고, 보조 패널에는 플레이리스트 그리드가 포함되어 있음.](https://developer.apple.com)

## 리소스

#### 관련 콘텐츠

[Split View](https://developer.apple.com/kr/design/human-interface-guidelines/split-views)

[탭 막대](https://developer.apple.com/kr/design/human-interface-guidelines/tab-bars)

[레이아웃](https://developer.apple.com/kr/design/human-interface-guidelines/layout)

#### Developer 문서

[sidebarAdaptable](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable) — SwiftUI

[NavigationSplitView](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) — SwiftUI

[sidebar](https://developer.apple.com/documentation/SwiftUI/ListStyle/sidebar) — SwiftUI

[UICollectionLayoutListConfiguration](https://developer.apple.com/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct) — UIKit

[NSSplitViewController](https://developer.apple.com/documentation/AppKit/NSSplitViewController) — AppKit

#### 비디오

## 변경 기록

| 날짜 | 변경 사항 |
| --- | --- |
| 2025년 6월 9일 | 사이드바 아래로 콘텐츠를 확장하는 지침이 추가됨. |
| 2024년 8월 6일 | SwiftUI 적응형 사이드바 스타일을 포함하도록 지침이 업데이트됨. |
| 2023년 12월 5일 | iPadOS용 아트워크가 추가됨. |
| 2023년 6월 21일 | visionOS 지침을 포함하기 위해 업데이트됨. |
