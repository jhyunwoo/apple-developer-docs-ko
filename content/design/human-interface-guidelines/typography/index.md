---
route: /design/human-interface-guidelines/typography
source_url: https://developer.apple.com/design/human-interface-guidelines/typography
source_locale: ko-KR
section: hig
content_type: article
title: 타이포그래피
original_title: Typography
source_hash: 28a7a649feef0801d252e3ceb46a2dfe97c201f947b3ecbace90151bfeb59002
canonical_source: official-ko
last_crawled_at: '2026-03-13T14:54:51+00:00'
last_translated_at: '2026-03-13T23:54:36+09:00'
---

# 타이포그래피

타이포그래피 선택지는 가독성 있는 텍스트를 표시하고, 정보 계층을 명시하고, 중요한 콘텐츠를 전달하며, 브랜드 또는 스타일을 선보일 수 있습니다.

![타이포그래피를 사용하여 계층적 정보를 전달할 수 있음을 나타내는 대문자 A 왼쪽에 소문자 A가 있는 스케치. 이미지에 직사각형 및 원형 그리드 선이 겹쳐져 있고, 여섯 가지 색상으로 된 기존 Apple 로고의 노란색을 은은하게 반영하는 노란색 색조가 적용됨.](https://developer.apple.com)

## 가독성 보장하기

**대부분의 사람들이 쉽게 읽을 수 있는 서체 크기를 사용하십시오.** 사람들은 콘텐츠를 다양한 거리와 조건하에서 읽을 수 있어야 합니다. 사용자 설정 서체 및 시스템 서체의 경우, 각 플랫폼별로 기본 및 최소 텍스트 크기를 준수하여 모든 기기에서 텍스트를 읽을 수 있는지 확인하십시오. 서체 굵기는 텍스트의 가독성에 영향을 미칠 수도 있다는 점을 염두에 두십시오. 굵기가 얇은 사용자 설정 서체를 사용하는 경우, 가독성을 높이려면 권장 크기보다 큰 서체를 사용하십시오.

| 플랫폼 | 기본 크기 | 최소 크기 |
| --- | --- | --- |
| iOS, iPadOS | 17pt | 11pt |
| macOS | 13pt | 10pt |
| tvOS | 29pt | 23pt |
| visionOS | 17pt | 12pt |
| watchOS | 16pt | 12pt |

**다양한 맥락에서 가독성을 테스트하십시오.** 예를 들어, 게임이 실행되는 각 플랫폼에서 게임 텍스트의 가독성을 테스트해야 합니다. 테스트한 결과 텍스트가 읽기 힘들다면 더 큰 글자 크기를 사용하거나, 텍스트 또는 배경 색상을 수정하여 대비를 높이거나, 시스템 서체와 같이 최적화된 가독성을 위해 디자인된 글자체를 사용하십시오.

![가로 방향의 iPhone에서 실행되는 게임을 보여주는 스크린샷. 이름이 3개의 식물 위에 각각 나타나며 상태 메시지가 오른쪽 상단 모서리에 있는 모서리가 둥근 직사각형에 나타남. 모든 텍스트가 너무 작은 크기를 사용하며, 3개의 식물 이름에는 표시되는 배경이 없음.](https://developer.apple.com)

![가로 방향의 iPhone에서 실행되는 게임을 보여주는 스크린샷. 이름이 3개의 식물 위에 각각 음영이 있는 마름모 모양 안에 나타나며 상태 메시지가 오른쪽 상단 모서리에 있는 모서리가 둥근 직사각형에 나타남. 모든 텍스트가 권장되는 최소 크기를 사용함.](https://developer.apple.com)

**일반적으로 가는 서체는 사용하지 마십시오.** 예를 들어, 시스템 제공 서체를 사용 중인 경우, 일반체, 중간체, 세미볼드체 또는 볼드체를 가급적 사용하고 특히 텍스트가 작을 때 읽기 힘든 아주 가는체, 얇은체, 가는체는 사용하지 마십시오.

## 계층 전달하기

**필요한 대로 굵기, 크기, 색상을 조절하여 중요한 정보를 강조하고 계층을 시각화하십시오.** 사람들이 텍스트 크기를 조절할 때 상대적 계층과 텍스트 요소의 시각적 구분을 유지하십시오.

**많은 부분을 사용자화한 인터페이스에서도 사용하는 글자체의 수를 최소화하십시오.** 너무 많은 종류의 글자체를 함께 사용하면 인터페이스가 내부적으로 일관되지 않고 디자인이 잘못되었다고 느끼는 것 외에도 정보 계층이 모호해지고 가독성이 떨어질 수 있습니다.

**텍스트 크기 변경에 반응할 때는 중요한 콘텐츠를 우선시하십시오.** 모든 콘텐츠가 동등하게 중요한 건 아닙니다. 사람들은 더 큰 텍스트 크기를 선택할 때 일반적으로 중요한 콘텐츠를 더 읽기 쉽게 만들려고 합니다. 항상 화면의 모든 단어 크기를 늘리려고 하는 것은 아닙니다. 예를 들어, 사람들이 탭으로 구성된 윈도우에서 콘텐츠를 읽기 위해 텍스트 크기를 늘릴 때 탭 제목의 크기가 증가할 것이라고 생각하지 않습니다. 이와 비슷하게, 사람들은 종종 게임에서 일시적 히트 데미지 값보다 캐릭터의 대화에 더 관심이 많습니다.

## 시스템 서체 사용하기

Apple은 다양한 굵기, 크기, 스타일 및 언어를 지원하는 2가지 글자체 패밀리를 제공합니다.

**San Francisco(SF)**는 SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew 및 SF Mono 변형을 포함하는 산세리프체 글자체 패밀리입니다.

![‘The quick brown fox jumps over the lazy dog’ 문구가 San Francisco Pro 서체로 표시됨.](https://developer.apple.com)

또한 시스템은 부드럽거나 둥근 UI 요소의 모양과 텍스트가 어울리도록 조정하거나 대체 타이포그래피 음성을 제공하기 위해 사용할 수 있는 SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian 및 SF Hebrew의 둥근 변형을 제공합니다.

**New York(NY)**은 단독으로 또는 SF 서체와 동시에 사용하기 위해 디자인된 세리프체 글자체 패밀리입니다.

![‘The quick brown fox jumps over the lazy dog’ 문구가 New York 서체로 표시됨.](https://developer.apple.com)

[here](https://developer.apple.com/fonts/)에서 San Francisco 및 New York 서체를 다운로드할 수 있습니다.

시스템은 다양한 서체 스타일을 하나의 파일에 결합한 *변형* 서체 형식으로 SF 및 NY 서체를 제공하고 스타일 간 중간값 채우기를 지원하여 중간 서체를 생성합니다.

:::note 참고
변형 서체는 다양한 타이포그래피 디자인을 여러 크기에 맞춰 조절하는 *시각적 크기 조절*을 지원합니다. 모든 플랫폼에서 시스템 서체는 별개의 시각적 크기(텍스트 및 디스플레이)와 굵기를 하나의 연속적인 디자인으로 합치는 *다이나믹 시각적 크기 조절*을 지원하여 시스템이 각 글리프 또는 문자의 중간값을 채워서 포인트 크기에 정확히 적용된 구조를 생성할 수 있습니다. 다이나믹 시각적 크기가 있으면 변형 서체 형식의 모든 기능을 지원하지 않는 디자인 도구를 사용하지 않는 이상 별개의 시각적 크기를 사용할 필요가 없습니다.
:::

시각적 계층을 정의하고 다양한 크기 및 맥락에서 명확하고 가독성 있는 디자인을 생성할 수 있게 시스템 서체는 아주 가는체부터 블랙체까지 다양한 굵기 및 Condensed와 Expanded를 포함한 다양한 너비(SF의 경우)로 제공됩니다. SF Symbols는 동일한 굵기를 사용하기 때문에 선택한 크기나 스타일과 무관하게 기호와 주변 텍스트 간 굵기를 정확하게 일치시킬 수 있습니다.

![‘Text’ 단어가 SF Pro 서체로 표시되어 2행의 9열로 반복됨. 행에는 곧은체 및 이탤릭체 스타일이 표시되고 열에는 아주 가는체부터 블랙체까지 서체 굵기가 표시됨.](https://developer.apple.com)

:::note 참고
[SF Symbols](https://developer.apple.com/kr/design/human-interface-guidelines/sf-symbols)는 San Francisco 시스템 서체와 매끄럽게 통합되어 모든 가중치와 크기를 가진 텍스트에 자동으로 정렬되는 포괄적인 기호 라이브러리를 제공합니다. 특히 텍스트로 개념을 전달하거나 대상체를 묘사해야 할 때 기호 사용을 고려하십시오.
:::

시스템은 두 글자체 패밀리와 함께 작동하는 일련의 타이포그래피 속성(텍스트 스타일이라고 함)을 정의합니다. *텍스트 스타일*은 서체 굵기, 포인트 크기 및 각 텍스트 크기의 시작 값의 조합을 지정합니다. 예를 들어, *본문* 텍스트 스타일은 여러 줄의 텍스트를 편안하게 읽을 수 있는 값을 사용하고 *머리말* 스타일은 머리말을 주변 콘텐츠와 구분할 수 있는 서체 크기 및 굵기를 지정합니다. 함께 사용하면 텍스트 스타일은 콘텐츠에서 다양한 수준의 중요도를 표현하는 데 사용할 수 있는 타이포그래피 계층을 형성합니다. 또한 텍스트 스타일은 사람들이 시스템의 텍스트 크기를 변경하거나 손쉬운 사용 설정에서 ‘텍스트 크게’를 켜는 것처럼 손쉬운 사용 기능을 조절할 때 텍스트 크기를 비례적으로 조절할 수 있습니다.

**기본 텍스트 스타일을 사용해 보십시오.** 시스템 정의된 텍스트 타입은 서체 크기 및 굵기를 통해 정보 계층을 전달할 수 있는 편리하고 일관된 방법을 제공합니다. 시스템 서체로 텍스트 스타일을 사용하면 다이나믹 타입과 원하는 텍스트 크기를 선택할 수 있는 더 큰 손쉬운 사용 글자 크기(사용 가능한 경우)도 확실하게 지원합니다. 지침을 보려면 [타이포그래피](https://developer.apple.com/kr/design/human-interface-guidelines/typography#Supporting-Dynamic-Type)의 내용을 참조하십시오.

**필요한 경우 기본 텍스트 스타일을 수정하십시오.** 시스템 API는 *기호 특성*이라 불리는 서체 조절 정의하여 텍스트 스타일의 일부 측면을 수정할 수 있도록 합니다. 예를 들어, 볼드 특성은 텍스트를 두껍게 만들어서 또 다른 계층 레벨을 생성합니다. 또한 가독성을 높이거나 공간을 절약해야 하는 경우, 기호 특성을 사용하여 행간을 조절할 수 있습니다. 예를 들어, 텍스트를 넓은 열 또는 긴 문단으로 표시하면 줄 간 공간이 많을수록(*넓은 행간*) 사람들이 다음 줄로 넘어갈 때 현재 위치를 놓치지 않기 쉽습니다. 반대로 목록 행처럼 높이가 제한된 영역에 여러 줄의 텍스트를 표시해야 하는 경우, 줄 사이 간격을 줄여서(*좁은 행간*) 텍스트를 맞춰 넣을 수 있습니다. 3줄 이상의 텍스트를 표시해야 한다면 높이가 제한된 영역에서도 좁은 행간을 사용하지 마십시오. 개발자 지침을 보려면 [leading(_:)](https://developer.apple.com/documentation/SwiftUI/Font/leading(_:))의 내용을 참조하십시오.

:::note 개발자 참고 사항
[Font.Design](https://developer.apple.com/documentation/SwiftUI/Font/Design)에서 정의된 상수를 사용하여 모든 시스템 서체에 접근할 수 있습니다. 앱 또는 게임에 시스템 서체를 내장하지 마십시오. 예를 들어, 모든 플랫폼에서 시스템 서체를 사용하려면 [Font.Design.default](https://developer.apple.com/documentation/SwiftUI/Font/Design/default)를 사용하고 New York 서체를 사용하려면 [Font.Design.serif](https://developer.apple.com/documentation/SwiftUI/Font/Design/serif)를 사용하십시오.
:::

**필요한 경우 인터페이스 모형에서 자간을 조절하십시오.** 실행 중인 앱에서 시스템 서체는 모든 포인트 크기에서 자간을 동적으로 조절합니다. 변형 시스템 서체를 사용하는 인터페이스의 정확한 인터페이스 모형을 생성하려면 특정 포인트 크기에서 개별 시각적 크기를 선택할 필요가 없지만 자간은 조절해야 할 수 있습니다. 지침을 보려면 [타이포그래피](https://developer.apple.com/kr/design/human-interface-guidelines/typography#Tracking-values)의 내용을 참조하십시오.

## 사용자 설정 서체 사용하기

**사용자 설정 서체가 읽기 적합한지 확인하십시오.** 사람들은 사용자 설정 서체를 다양한 거리와 조건하에서 쉽게 읽을 수 있어야 합니다. 사용자 설정 서체를 사용하는 동안 [타이포그래피](https://developer.apple.com/kr/design/human-interface-guidelines/typography#Specifications)에서 다양한 스타일 및 굵기에 대해 권장되는 최소 서체 크기를 참고하십시오.

**사용자 설정 서체에 손쉬운 사용 기능을 적용하십시오.** 시스템 서체는 자동으로 다이나믹 타입을 지원(지원 가능한 경우)하고 볼드체 텍스트 등의 손쉬운 사용 기능을 켤 때 반응합니다. 사용자 설정 서체를 사용하는 경우, 동일한 동작을 구현하는지 확인하십시오. 개발자 지침을 보려면 [Applying custom fonts to text](https://developer.apple.com/documentation/SwiftUI/Applying-Custom-Fonts-to-Text)의 내용을 참조하십시오. Unity 기반 게임에서 [Apple’s Unity plug-ins](https://github.com/apple/unityplugins)를 사용하여 다이나믹 타입을 지원할 수 있습니다. 플러그인이 게임에 적합하지 않은 경우, 플레이어가 다른 방법으로 텍스트 크기를 조절할 수 있도록 하십시오.

## 다이나믹 타입 지원하기

다이나믹 타입은 iOS, iPadOS, tvOS, visionOS 및 watchOS의 시스템 수준 기능으로 가독성과 편의성을 보장하기 위해 기기에서 표시되는 텍스트의 크기를 조절할 수 있습니다. 관련된 지침을 보려면 [손쉬운 사용](https://developer.apple.com/kr/design/human-interface-guidelines/accessibility)의 내용을 참조하십시오.

사용 가능한 다이나믹 타입 크기의 목록은 [타이포그래피](https://developer.apple.com/kr/design/human-interface-guidelines/typography#Specifications)의 내용을 참조하십시오. [Apple Design Resources](https://developer.apple.com/design/resources/)에서 각 플랫폼에 대한 다이나믹 타입 크기 표를 다운로드할 수도 있습니다.

개발자 지침을 보려면 [Text input and output](https://developer.apple.com/documentation/SwiftUI/Text-input-and-output)의 내용을 참조하십시오. Unity 기반 게임에서 다이나믹 타입을 지원하려면 [Apple’s Unity plug-ins](https://github.com/apple/unityplugins)을 사용하십시오.

**앱의 레이아웃이 모든 서체 크기에 맞게 조정되는지 확인하십시오.** 디자인이 크기 조절되며 텍스트와 글리프를 모든 서체 크기에서 읽을 수 있는지 확인하십시오. iPhone 또는 iPad에서 설정 > 손쉬운 사용 > 디스플레이 및 텍스트 크기 > 더 큰 텍스트의 ‘글자 더 크게 조절’을 켜고 앱이 읽기 편한 상태로 유지되는지 확인하십시오.

**서체 크기가 증가할 때 의미 있는 인터페이스 아이콘의 크기도 증가시키십시오.** 인터페이스 아이콘을 사용하여 중요한 정보를 전달하는 경우, 큰 서체 크기에서도 해당 아이콘을 쉽게 볼 수 있도록 하십시오. [SF Symbols](https://developer.apple.com/kr/design/human-interface-guidelines/sf-symbols)를 사용하면 다이나믹 타입 크기가 변경될 때 자동으로 크기 조정되는 아이콘을 가져올 수 있습니다.

**서체 크기가 증가할 때 텍스트 잘림을 최소화하십시오.** 일반적으로 가장 큰 표준 서체 크기에서처럼 가장 큰 손쉬운 사용 서체 크기에서도 가능한 많은 유용한 텍스트를 표시하도록 노력하십시오. 별도의 보기를 열어 나머지 콘텐츠를 볼 수 있는 경우가 아니라면 스크롤 가능 영역에서 텍스트가 잘리는 일이 없도록 하십시오. 유용한 양의 텍스트를 표시하는 데 필요한 만큼 여러 줄을 사용하도록 레이블을 구성하여 레이블의 텍스트 잘림을 방지할 수 있습니다. 개발자 지침을 보려면 [numberOfLines](https://developer.apple.com/documentation/UIKit/UILabel/numberOfLines)의 내용을 참조하십시오.

**큰 서체 크기에서 레이아웃을 조절하는 것을 고려하십시오.** 수평적으로 공간이 제한된 상황에서 서체가 증가하면 인라인 항목(글리프 및 타임스탬프 등)과 컨테이너 경계가 텍스트를 가득 채워 텍스트가 잘리거나 겹칠 수 있습니다. 가독성을 높이려면 텍스트가 보조 항목 위에 표시되는 스택 레이아웃을 사용하는 것을 고려하십시오. 여러 열로 구성된 텍스트는 수평 공간 제한 때문에 큰 서체 크기에서 가독성이 떨어질 수 있습니다. 서체 크기가 증가할 때 열의 수를 줄여 텍스트 잘림을 막고 전체적인 가독성을 향상하십시오. 개발자 지침을 보려면 [isAccessibilityCategory](https://developer.apple.com/documentation/UIKit/UIContentSizeCategory/isAccessibilityCategory)의 내용을 참조하십시오.

**현재 서체 크기와 관계없이 일관된 정보 계층을 유지하십시오.** 예를 들어, 서체 크기가 매우 크더라도 주요 요소를 보기의 상단 쪽에 유지하여 이러한 요소를 찾을 수 있도록 하십시오.

## 플랫폼 고려 사항

### iOS, iPadOS

SF Pro는 iOS 및 iPadOS의 시스템 서체입니다. iOS 및 iPadOS 앱은 NY를 사용할 수도 있습니다.

### macOS

SF Pro는 macOS의 시스템 서체입니다. NY는 Mac Catalyst로 빌드된 Mac 앱에서 사용 가능합니다. macOS는 다이나믹 타입을 지원하지 않습니다.

**필요한 경우, 다이나믹 시스템 서체 변형을 사용하여 표준 제어기의 텍스트와 맞추십시오.** 다이나믹 시스템 서체 변형은 시스템 제공 제어기에 표시되는 텍스트와 동일한 모양과 느낌을 가진 텍스트를 제공합니다. 아래에 나열된 변형을 사용하여 플랫폼의 다른 앱과 일관된 스타일을 만드십시오.

| 다이나믹 서체 변형 | API |
| --- | --- |
| 제어기 콘텐츠 | [controlContentFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/controlContentFont(ofSize:)) |
| 레이블 | [labelFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/labelFont(ofSize:)) |
| 메뉴 | [menuFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/menuFont(ofSize:)) |
| 메뉴 막대 | [menuBarFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/menuBarFont(ofSize:)) |
| 메시지 | [messageFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/messageFont(ofSize:)) |
| 팔레트 | [paletteFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/paletteFont(ofSize:)) |
| 제목 | [titleBarFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/titleBarFont(ofSize:)) |
| 툴팁 | [toolTipsFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/toolTipsFont(ofSize:)) |
| 문서 텍스트(사용자) | [userFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/userFont(ofSize:)) |
| 고정폭 문서 텍스트(사용자 고정폭) | [userFixedPitchFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/userFixedPitchFont(ofSize:)) |
| 볼드체 시스템 서체 | [boldSystemFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/boldSystemFont(ofSize:)) |
| 시스템 서체 | [systemFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/systemFont(ofSize:)) |

### tvOS

SF Pro는 tvOS의 시스템 서체이며 앱은 NY를 사용할 수도 있습니다.

### visionOS

SF Pro는 visionOS의 시스템 서체입니다. NY를 사용하는 경우, 원하는 유형 스타일을 지정해야 합니다.

visionOS는 다이나믹 타입 본문 및 제목 스타일의 더 볼드한 버전을 사용하고 넓은 편집 스타일 레이아웃에서 매우 큰 제목 1 및 매우 큰 제목 2를 도입합니다. 생동감을 사용하여 텍스트 및 기호의 계층을 나타내는 방법에 관한 지침을 보려면 [머티리얼](https://developer.apple.com/kr/design/human-interface-guidelines/materials#visionOS)의 내용을 참조하십시오.

**일반적으로 2D 텍스트를 가급적 사용하십시오.** 텍스트 문자의 시각적 깊이가 클수록 가독성이 떨어질 수 있습니다. 소량의 3D 텍스트는 재미있는 시각적 요소로 사람들의 관심을 끌 수 있지만, 읽고 이해해야 하는 콘텐츠를 표시할 때는 시각적 깊이가 거의 없거나 전혀 없는 텍스트를 가급적 사용하십시오.

**텍스트를 확대/축소할 때 보기 좋게 표시되고 가독성이 있는지 확인하십시오.** 전체 크기에서 텍스트가 보기 좋게 표시되는 텍스트 스타일을 사용한 다음 다양한 크기에서 가독성을 테스트하십시오.

**텍스트와 컨테이너 배경 간에 대비를 최대화하십시오.** 기본적으로 시스템은 텍스트를 흰색으로 표시하는데 이는 흰색이 기본 시스템 배경 머티리얼과 강한 대비를 제공하여 텍스트를 더 쉽게 읽을 수 있기 때문입니다. 다른 텍스트 색상을 사용하고 싶은 경우, 다양한 맥락에서 테스트하십시오.

**배경이 없는 텍스트를 표시하려면 가독성을 높이기 위해 볼드체로 만드십시오.** 이러한 상황에서는 텍스트 대비를 높이기 위해 그림자를 추가하지 않는 것이 좋습니다. 현재 공간에는 정확한 그림자를 드리울 수 있는 시각적 표면이 없을 수도 있고 사용자의 현재 환경에서 잘 표시되는 그림자의 크기와 밀도를 예측할 수 없습니다.

**최대한 사람을 향해 텍스트를 배치하십시오.** 3D 대상체의 레이블처럼 공간의 한 지점과 연관된 텍스트를 표시하는 경우, 일반적으로 *빌보딩*을 사용하는 것이 좋습니다. 즉, 텍스트 또는 대상체의 움직임과 무관하게 해당 텍스트가 착용자를 향하도록 배치하는 것이 좋습니다. 계속 착용자를 향하도록 텍스트가 회전되지 않는 경우, 사람들이 측면이나 고도로 기울어진 각도에서 볼 수 있기 때문에 텍스트를 읽는 것이 불가능해질 수 있습니다. 예를 들어, 실제 책상 위에 있는 것처럼 보이고 바로 위에 레이블이 고정된 가상 램프를 떠올려 보십시오. 텍스트를 항상 읽을 수 있도록 사람들이 책상 주위를 이동할 때마다 레이블은 y축을 중심으로 회전해야 합니다. 즉, 텍스트의 기준선은 사람의 시선과 수직을 유지해야 합니다.

### watchOS

SF Compact는 watchOS의 시스템 서체이고 앱은 NY를 사용할 수도 있습니다. 컴플리케이션에서 watchOS는 SF Compact Rounded를 사용합니다.

## 명세

기호 특성을 사용하여 시스템 텍스트 스타일의 강조 버전을 표시할 수 있습니다. SwiftUI의 경우 UIKit은 [bold()](https://developer.apple.com/documentation/SwiftUI/Text/bold()) 보조 키를 사용하고; [UIFontDescriptor](https://developer.apple.com/documentation/UIKit/UIFontDescriptor) API는 [traitBold](https://developer.apple.com/documentation/UIKit/UIFontDescriptor/SymbolicTraits-swift.struct/traitBold)를 사용하십시오. 강조 굵기는 중간체, 세미볼드체, 볼드체 또는 진한 볼드체가 있습니다. 다음 명세에는 각 텍스트 스타일의 강조 굵기가 포함되어 있습니다.

### iOS, iPadOS 다이나믹 타입 크기

### iOS, iPadOS 더 큰 손쉬운 사용 글자 크기

### macOS 기본 텍스트 스타일

| 텍스트 스타일 | 굵기 | 크기(포인트) | 줄 높이(포인트) | 강조 굵기 |
| --- | --- | --- | --- | --- |
| 큰 제목 | 일반체 | 26 | 32 | 볼드체 |
| 제목 1 | 일반체 | 22 | 26 | 볼드체 |
| 제목 2 | 일반체 | 17 | 22 | 볼드체 |
| 제목 3 | 일반체 | 15 | 20 | 세미볼드체 |
| 머리말 | 볼드체 | 13 | 16 | 진한 볼드체 |
| 본문 | 일반체 | 13 | 16 | 세미볼드체 |
| 콜아웃 | 일반체 | 12 | 15 | 세미볼드체 |
| 부머리말 | 일반체 | 11 | 14 | 세미볼드체 |
| 각주 | 일반체 | 10 | 13 | 세미볼드체 |
| 캡션 1 | 일반체 | 10 | 13 | 중간체 |
| 캡션 2 | 중간체 | 10 | 13 | 세미볼드체 |

### tvOS 기본 텍스트 스타일

| 텍스트 스타일 | 굵기 | 크기(포인트) | 행간(포인트) | 강조 굵기 |
| --- | --- | --- | --- | --- |
| 제목 1 | 중간체 | 76 | 96 | 볼드체 |
| 제목 2 | 중간체 | 57 | 66 | 볼드체 |
| 제목 3 | 중간체 | 48 | 56 | 볼드체 |
| 머리말 | 중간체 | 38 | 46 | 볼드체 |
| 부제목 1 | 일반체 | 38 | 46 | 중간체 |
| 콜아웃 | 중간체 | 31 | 38 | 볼드체 |
| 본문 | 중간체 | 29 | 36 | 볼드체 |
| 캡션 1 | 중간체 | 25 | 32 | 볼드체 |
| 캡션 2 | 중간체 | 23 | 30 | 볼드체 |

### watchOS 다이나믹 타입 크기

### watchOS 더 큰 손쉬운 사용 글자 크기

### 자간 값

#### iOS, iPadOS, visionOS 자간 값

#### macOS 자간 값

| 크기(포인트) | 자간(1/1000em) | 자간(포인트) |
| --- | --- | --- |
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

#### tvOS 자간 값

| 크기(포인트) | 자간(1/1000em) | 자간(포인트) |
| --- | --- | --- |
| 6 | +41 | +0.24 |
| 7 | +34 | +0.23 |
| 8 | +26 | +0.21 |
| 9 | +19 | +0.17 |
| 10 | +12 | +0.12 |
| 11 | +6 | +0.06 |
| 12 | 0 | 0.0 |
| 13 | -6 | -0.08 |
| 14 | -11 | -0.15 |
| 15 | -16 | -0.23 |
| 16 | -20 | -0.31 |
| 17 | -26 | -0.43 |
| 18 | -25 | -0.44 |
| 19 | -24 | -0.45 |
| 20 | -23 | -0.45 |
| 21 | -18 | -0.36 |
| 22 | -12 | -0.26 |
| 23 | -4 | -0.10 |
| 24 | +3 | +0.07 |
| 25 | +6 | +0.15 |
| 26 | +8 | +0.22 |
| 27 | +11 | +0.29 |
| 28 | +14 | +0.38 |
| 29 | +14 | +0.40 |
| 30 | +14 | +0.40 |
| 31 | +13 | +0.39 |
| 32 | +13 | +0.41 |
| 33 | +12 | +0.40 |
| 34 | +12 | +0.40 |
| 35 | +11 | +0.38 |
| 36 | +10 | +0.37 |
| 37 | +10 | +0.36 |
| 38 | +10 | +0.37 |
| 39 | +10 | +0.38 |
| 40 | +10 | +0.37 |
| 41 | +9 | +0.36 |
| 42 | +9 | +0.37 |
| 43 | +9 | +0.38 |
| 44 | +8 | +0.37 |
| 45 | +8 | +0.35 |
| 46 | +8 | +0.36 |
| 47 | +8 | +0.37 |
| 48 | +8 | +0.35 |
| 49 | +7 | +0.33 |
| 50 | +7 | +0.34 |
| 51 | +7 | +0.35 |
| 52 | +6 | +0.31 |
| 53 | +6 | +0.33 |
| 54 | +6 | +0.32 |
| 56 | +6 | +0.30 |
| 58 | +5 | +0.28 |
| 60 | +4 | +0.26 |
| 62 | +4 | +0.24 |
| 64 | +4 | +0.22 |
| 66 | +3 | +0.19 |
| 68 | +2 | +0.17 |
| 70 | +2 | +0.14 |
| 72 | +2 | +0.14 |
| 76 | +1 | +0.07 |
| 80 | 0 | 0 |
| 84 | 0 | 0 |
| 88 | 0 | 0 |
| 92 | 0 | 0 |
| 96 | 0 | 0 |

#### watchOS 자간 값

## 리소스

#### 관련 콘텐츠

[here](https://developer.apple.com/fonts/)

[SF Symbols](https://developer.apple.com/kr/design/human-interface-guidelines/sf-symbols)

#### Developer 문서

[Text input and output](https://developer.apple.com/documentation/SwiftUI/Text-input-and-output) — SwiftUI

[Text display and fonts](https://developer.apple.com/documentation/UIKit/text-display-and-fonts) — UIKit

[Fonts](https://developer.apple.com/documentation/AppKit/fonts) — AppKit

#### 비디오

## 변경 기록

| 날짜 | 변경 사항 |
| --- | --- |
| 2025년 12월 16일 | 각 플랫폼의 다이나믹 타입 스타일 명세에 강조 굵기가 추가되었습니다. |
| 2025년 3월 7일 | 다이나믹 타입의 지침이 확장됨. |
| 2024년 6월 10일 | Apple의 Unity 플러그인을 사용하여 Unity 기반 게임에서 다이나믹 타입을 지원하는 것에 대한 지침이 추가되고 visionOS 앱 또는 게임에서 빌보딩에 대한 지침이 향상됨. |
| 2023년 9월 12일 | 시스템 서체 굵기 및 명시된 tvOS 명세 표 설명의 일러스트 아트워크가 추가됨. |
| 2023년 6월 21일 | visionOS 지침을 포함하기 위해 업데이트됨. |
