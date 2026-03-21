---
route: /documentation/CoreText
source_url: https://developer.apple.com/documentation/CoreText
source_locale: en-US
section: docc
content_type: symbol
title: Core Text
original_title: Core Text
source_hash: 5da62f23935323f19183d2db2ed2f7e8251ac4fcc1b3f673b980bc4bc434f1f6
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:54:44+00:00'
last_translated_at: '2026-03-14T00:13:00+09:00'
---

# Core Text

텍스트 레이아웃을 만들고, 글꼴 처리를 최적화하며, 글꼴 메트릭과 glyph 데이터에 접근합니다.

## 개요

Core Text는 텍스트 레이아웃과 글꼴 처리를 위한 저수준 프로그래밍 인터페이스를 제공합니다. Core Text 레이아웃 엔진은 높은 성능, 사용 편의성, 그리고 [Core Foundation](https://developer.apple.com/documentation/CoreFoundation)과의 긴밀한 통합을 목표로 설계되었습니다. 텍스트 레이아웃 API는 문자에서 glyph로의 변환, ligature, kerning 등을 포함하는 고품질 조판 기능을 제공합니다. 이에 대응하는 Core Text의 글꼴 기술은 자동 글꼴 대체(cascading), 글꼴 descriptor와 collection, 글꼴 메트릭과 glyph 데이터에 대한 쉬운 접근, 그리고 그 밖의 다양한 기능을 제공합니다.

:::note 참고
Core Text의 개별 함수는 모두 thread-safe합니다. 글꼴 객체([CTFont](https://developer.apple.com/documentation/coretext/ctfont), [CTFontDescriptor](https://developer.apple.com/documentation/coretext/ctfontdescriptor), 그리고 관련 객체)는 여러 operation, work queue, thread에서 동시에 사용할 수 있습니다. 하지만 layout 객체([CTTypesetter](https://developer.apple.com/documentation/coretext/cttypesetter), [CTFramesetter](https://developer.apple.com/documentation/coretext/ctframesetter), [CTRun](https://developer.apple.com/documentation/coretext/ctrun), [CTLine](https://developer.apple.com/documentation/coretext/ctline), [CTFrame](https://developer.apple.com/documentation/coretext/ctframe), 그리고 관련 객체)는 단일 operation, work queue, 또는 thread에서 사용해야 합니다.
:::

:::topic-grid
## 불투명 타입
- [CTFont](https://developer.apple.com/documentation/coretext/ctfont): 글꼴 객체입니다.
- [CTFontCollection](https://developer.apple.com/documentation/coretext/ctfontcollection): 글꼴 collection입니다.
- [CTFontDescriptor](https://developer.apple.com/documentation/coretext/ctfontdescriptor): 글꼴 descriptor입니다.
- [CTFrame](https://developer.apple.com/documentation/coretext/ctframe): frame입니다.
- [CTFramesetter](https://developer.apple.com/documentation/coretext/ctframesetter): 텍스트 frame을 생성합니다.
- [CTGlyphInfo](https://developer.apple.com/documentation/coretext/ctglyphinfo): Unicode에서 glyph ID로의 글꼴 매핑을 재정의합니다.
- [CTLine](https://developer.apple.com/documentation/coretext/ctline): 한 줄의 텍스트입니다.
- [CTParagraphStyle](https://developer.apple.com/documentation/coretext/ctparagraphstyle): attributed string 안의 문단 또는 눈금자 속성입니다.
- [CTRun](https://developer.apple.com/documentation/coretext/ctrun): glyph run입니다.
- [CTRunDelegate](https://developer.apple.com/documentation/coretext/ctrundelegate): run delegate입니다.
- [CTTextTab](https://developer.apple.com/documentation/coretext/cttexttab): 정렬 유형과 위치를 저장하는 문단 스타일의 tab입니다.
- [CTTypesetter](https://developer.apple.com/documentation/coretext/cttypesetter): 줄 레이아웃을 수행하는 typesetter입니다.
:::

:::topic-grid
## 참고 자료
- [Styling Attributed Strings](https://developer.apple.com/documentation/coretext/styling-attributed-strings): 객체 안에 배치했을 때 Core Text가 반응하는 속성입니다.
- [Core Text Structures](https://developer.apple.com/documentation/coretext/core-text-structures)
- [Core Text Enumerations](https://developer.apple.com/documentation/coretext/core-text-enumerations)
- [Core Text Constants](https://developer.apple.com/documentation/coretext/core-text-constants)
- [Core Text Functions](https://developer.apple.com/documentation/coretext/core-text-functions)
- [Core Text Data Types](https://developer.apple.com/documentation/coretext/core-text-data-types)
- [SFNT Support](https://developer.apple.com/documentation/coretext/sfnt-support)
:::

:::topic-grid
## 매크로
- [Macros](https://developer.apple.com/documentation/coretext/coretext-macros)
:::

:::topic-grid
## 클래스
- [CTRubyAnnotation](https://developer.apple.com/documentation/coretext/ctrubyannotation)
:::

:::topic-grid
## 프로토콜
- [CTAdaptiveImageProviding](https://developer.apple.com/documentation/coretext/ctadaptiveimageproviding)
:::

:::topic-grid
## 변수
- [kCTFontDescriptorLanguageAttribute](https://developer.apple.com/documentation/coretext/kctfontdescriptorlanguageattribute)
:::

:::topic-grid
## 함수
- [CTFontGetUIFontType(_:)](https://developer.apple.com/documentation/coretext/ctfontgetuifonttype(_:))
:::
