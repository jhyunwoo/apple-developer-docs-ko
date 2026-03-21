---
route: /documentation/RegexBuilder
source_url: https://developer.apple.com/documentation/RegexBuilder
source_locale: en-US
section: docc
content_type: symbol
title: RegexBuilder
original_title: RegexBuilder
source_hash: 333e72d43fd04a695a27746d1d08114a044f387752123ac622f668d1d25189f5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:33:48+00:00'
last_translated_at: '2026-03-14T00:58:00+09:00'
---

# RegexBuilder

표현력이 높은 domain-specific language를 사용해 정규 표현식을 만들고, 텍스트 검색이나 치환 같은 작업을 수행합니다.

## 개요

정규 표현식(regex)은 텍스트 안의 패턴을 일치시키는 강력한 도구입니다. Swift는 문자열, 리터럴, 그리고 이 DSL을 포함해 정규 표현식을 만드는 여러 방법을 지원합니다. 예를 들면 다음과 같습니다.

```swift
let word = OneOrMore(.word)
let emailPattern = Regex {
    Capture {
        ZeroOrMore {
            word
            "."
        }
        word
    }
    "@"
    Capture {
        word
        OneOrMore {
            "."
            word
        }
    }
}

let text = "My email is my.name@example.com."
if let match = text.firstMatch(of: emailPattern) {
    let (wholeMatch, name, domain) = match.output
    // wholeMatch is "my.name@example.com"
    // name is "my.name"
    // domain is "example.com"
}
```

:::topic-grid
## 구성 요소
- [CharacterClass](https://developer.apple.com/documentation/regexbuilder/characterclass): regex에서 일치하는 문자 클래스입니다.
- [Anchor](https://developer.apple.com/documentation/regexbuilder/anchor): 입력 문자열의 특정 위치에서 특정 조건이 일치하는 regex 구성 요소입니다.
- [Lookahead](https://developer.apple.com/documentation/regexbuilder/lookahead): 지정된 위치에서 그 내용이 일치할 때만 일치를 계속할 수 있게 하는 regex 구성 요소입니다.
- [NegativeLookahead](https://developer.apple.com/documentation/regexbuilder/negativelookahead): 지정된 위치에서 그 내용이 일치하지 않을 때만 일치를 계속할 수 있게 하는 regex 구성 요소입니다.
- [ChoiceOf](https://developer.apple.com/documentation/regexbuilder/choiceof): 일치 과정에서 구성 요소 중 정확히 하나를 선택하는 regex 구성 요소입니다.
:::

:::topic-grid
## 수량자
- [One](https://developer.apple.com/documentation/regexbuilder/one): 기본 구성 요소가 정확히 한 번 나타나는 경우와 일치하는 regex 구성 요소입니다.
- [Optionally](https://developer.apple.com/documentation/regexbuilder/optionally): 기본 구성 요소가 0번 또는 1번 나타나는 경우와 일치하는 regex 구성 요소입니다.
- [ZeroOrMore](https://developer.apple.com/documentation/regexbuilder/zeroormore): 기본 구성 요소가 0번 이상 나타나는 경우와 일치하는 regex 구성 요소입니다.
- [OneOrMore](https://developer.apple.com/documentation/regexbuilder/oneormore): 기본 구성 요소가 1번 이상 나타나는 경우와 일치하는 regex 구성 요소입니다.
- [Repeat](https://developer.apple.com/documentation/regexbuilder/repeat): 기본 구성 요소의 출현 횟수를 선택해 일치시키는 regex 구성 요소입니다.
- [Local](https://developer.apple.com/documentation/regexbuilder/local): atomic group을 나타내는 regex 구성 요소입니다.
:::

:::topic-grid
## Capture
- [Capture](https://developer.apple.com/documentation/regexbuilder/capture): 일치한 부분 문자열이나 변환된 결과를 저장해 regex 일치 결과에서 접근할 수 있게 하는 regex 구성 요소입니다.
- [TryCapture](https://developer.apple.com/documentation/regexbuilder/trycapture): 일치한 부분 문자열을 변환하려고 시도하고, 성공하면 결과를 저장하고 실패하면 backtracking하는 regex 구성 요소입니다.
- [Reference](https://developer.apple.com/documentation/regexbuilder/reference): 정규 표현식에서 capture된 부분에 대한 참조입니다.
:::

:::topic-grid
## Builder
- [RegexComponentBuilder](https://developer.apple.com/documentation/regexbuilder/regexcomponentbuilder): closure에서 정규 표현식을 구성하는 사용자 정의 parameter attribute입니다.
- [AlternationBuilder](https://developer.apple.com/documentation/regexbuilder/alternationbuilder): closure에서 정규 표현식 alternation을 구성하는 사용자 정의 parameter attribute입니다.
:::

:::topic-grid
## 연산자
- [...(_:_:)](https://developer.apple.com/documentation/regexbuilder/'...(_:_:)-16g2a): 주어진 범위의 문자를 포함하는 문자 클래스를 반환합니다.
- [...(_:_:)](https://developer.apple.com/documentation/regexbuilder/'...(_:_:)-629xh): 주어진 범위의 Unicode scalar를 포함하는 문자 클래스를 반환합니다.
:::
