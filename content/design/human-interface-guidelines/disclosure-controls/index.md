---
route: /design/human-interface-guidelines/disclosure-controls
source_url: https://developer.apple.com/design/human-interface-guidelines/disclosure-controls
source_locale: ko-KR
section: hig
content_type: article
title: 펼침 제어기
original_title: Disclosure controls
source_hash: dac2d5163abad77892a0bd23730cb2339290a84ee8c657159fde07d7730c55ad
canonical_source: official-ko
last_crawled_at: '2026-03-13T15:02:11+00:00'
last_translated_at: '2026-03-14T00:02:05+09:00'
---

# 펼침 제어기

펼침 제어기는 특정 제어기 또는 보기와 관련된 정보 및 기능을 표시하거나 가립니다.

![축소 및 확장된 펼침 버튼의 스타일화된 모양이 표시되어 있음. 여섯 가지 색상으로 된 기존 Apple 로고의 빨간색을 은은하게 반영하는 빨간색 색조가 이미지에 적용됨.](https://developer.apple.com)

## 모범 사례

**펼침 제어기를 사용하여 관련성이 있기 전에는 세부사항을 가리십시오.** 사람들이 사용할 가능성이 가장 높은 제어기를 펼침 계층의 상단에 배치하여 항상 표시되도록 하며, 기본적으로 고급 기능은 가려집니다. 이 구성을 사용하면 사람들이 너무 많은 세부 옵션으로 인해 부담을 느끼지 않고 가장 중요한 정보를 빠르게 찾을 수 있도록 도와줍니다.

## 펼침 삼각형

펼침 삼각형은 보기 또는 항목 목록과 관련된 정보 및 기능을 표시하거나 가립니다. 예를 들어, Keynote는 프레젠테이션을 내보낼 때 펼침 삼각형을 사용하여 고급 옵션을 표시하고, Finder는 목록 보기에서 폴더 구조를 탐색할 때 펼침 삼각형을 사용하여 계층을 점진적으로 표시합니다.

펼침 삼각형은 콘텐츠가 가려져 있을 때 앞쪽 가장자리에서 안쪽을 가리키고, 콘텐츠가 표시될 때 아래쪽을 가리킵니다. 펼침 삼각형을 클릭하거나 탭하면 이 두 상태 간에 전환되며, 보기가 콘텐츠에 맞게 확장되거나 축소됩니다.

**펼침 삼각형을 사용할 때 설명 레이블을 제공하십시오.** 레이블에 표시되거나 가려진 내용(예: ‘고급 옵션’)이 나타나는지 확인하십시오.

개발자 지침을 보려면 [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/disclosure)의 내용을 참조하십시오.

## 펼침 버튼

펼침 버튼은 특정 제어기와 관련된 기능을 표시하거나 가립니다. 예를 들어, macOS 저장 시트에는 ‘별도 저장’ 텍스트 필드 옆에 펼침 버튼이 표시됩니다. 사람들이 이 버튼을 클릭하거나 탭하면 저장 대화상자가 확장되어 문서의 출력 위치를 선택할 수 있는 고급 탐색 옵션이 제공됩니다.

펼침 버튼은 콘텐츠가 가려져 있을 때 아래쪽을 가리키고, 콘텐츠가 표시될 때 위쪽을 가리킵니다. 펼침 버튼을 클릭하거나 탭하면 이 두 상태 간에 전환되며, 보기가 콘텐츠에 맞게 확장되거나 축소됩니다.

**표시하거나 가리는 콘텐츠 근처에 펼침 버튼을 배치하십시오.** 사람이 버튼을 클릭하거나 탭할 때 나타나는 확장된 선택 항목과 제어기 간의 명확한 관계를 설정하십시오.

**단일 보기에서는 펼침 버튼을 한 개만 사용하십시오.** 펼침 버튼이 여러 개 있으면 더 복잡해지고 혼란스러울 수 있습니다.

개발자 지침을 보려면 [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/pushDisclosure)의 내용을 참조하십시오.

## 플랫폼 고려 사항

*macOS에 대한 추가 고려 사항은 없습니다. tvOS 또는 watchOS에서는 지원되지 않습니다.*

### iOS, iPadOS, visionOS

펼침 제어기는 SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/SwiftUI/DisclosureGroup) 보기를 통해 iOS, iPadOS 및 visionOS에서 사용할 수 있습니다.

## 리소스

#### 관련 콘텐츠

[개요 보기](https://developer.apple.com/kr/design/human-interface-guidelines/outline-views)

[목록 및 표](https://developer.apple.com/kr/design/human-interface-guidelines/lists-and-tables)

[버튼](https://developer.apple.com/kr/design/human-interface-guidelines/buttons)

#### Developer 문서

[DisclosureGroup](https://developer.apple.com/documentation/SwiftUI/DisclosureGroup) — SwiftUI

[NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/disclosure) — AppKit

[NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/pushDisclosure) — AppKit

#### 비디오
