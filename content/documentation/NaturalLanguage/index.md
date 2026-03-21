---
route: /documentation/NaturalLanguage
source_url: https://developer.apple.com/documentation/NaturalLanguage
source_locale: en-US
section: docc
content_type: symbol
title: Natural Language
original_title: Natural Language
source_hash: 8ba2b5f1ff638f7b0dced2d5f8961c481a9d8d5c9869b425eb3c0f60d837a995
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:46:56+00:00'
last_translated_at: '2026-03-14T01:23:00+09:00'
---

# Natural Language

자연어 텍스트를 분석하고 해당 언어에 특화된 metadata를 추론합니다.

## 개요

Natural Language 프레임워크는 다양한 언어와 문자 체계를 지원하는 여러 자연어 처리(NLP) 기능을 제공합니다. 이 프레임워크를 사용해 자연어 텍스트를 문단, 문장, 또는 단어 단위로 분할하고, 품사, 어휘 클래스, lemma, 문자 체계, 언어와 같은 세그먼트 정보를 태그할 수 있습니다.

![Natural Language 프레임워크가 수행할 수 있는 분석 유형을 보여 주는 다이어그램입니다.](https://developer.apple.com)

이 프레임워크를 사용하면 다음과 같은 작업을 수행할 수 있습니다.

- *언어 식별*: 텍스트 조각의 언어를 자동으로 감지합니다.
- *토큰화*: 텍스트를 언어학적 단위 또는 token으로 분해합니다.
- *품사 태깅*: 개별 단어에 해당 품사를 표시합니다.
- *표제어 추출*: 형태소 분석을 바탕으로 단어의 어간을 추론합니다.
- *개체명 인식*: token이 사람, 장소, 조직의 이름인지 식별합니다.

또한 이 프레임워크를 Create ML과 함께 사용해 사용자 정의 자연어 모델을 학습하고 배포할 수 있습니다. 자세한 내용은 [Creating a text classifier model](https://developer.apple.com/documentation/CreateML/creating-a-text-classifier-model)과 doc:creating-a-word-tagger-model을 참고하십시오.

:::topic-grid
## 토큰화
- [Tokenizing natural language text](https://developer.apple.com/documentation/naturallanguage/tokenizing-natural-language-text): 문자열 안의 단어를 열거합니다.
- [NLTokenizer](https://developer.apple.com/documentation/naturallanguage/nltokenizer): 자연어 텍스트를 의미 단위로 분할하는 tokenizer입니다.
:::

:::topic-grid
## 언어 식별
- [Identifying the language in text](https://developer.apple.com/documentation/naturallanguage/identifying-the-language-in-text): 언어 인식기를 사용해 텍스트 조각의 언어를 감지합니다.
- [NLLanguageRecognizer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer): 텍스트 본문의 언어를 인식합니다.
- [NLLanguage](https://developer.apple.com/documentation/naturallanguage/nllanguage): Natural Language 프레임워크가 지원하는 언어입니다.
:::

:::topic-grid
## 언어학적 태그
- [Identifying parts of speech](https://developer.apple.com/documentation/naturallanguage/identifying-parts-of-speech): 문자열 안의 명사, 동사, 형용사 등 품사를 분류합니다.
- [Identifying people, places, and organizations](https://developer.apple.com/documentation/naturallanguage/identifying-people-places-and-organizations): 언어학적 tagger를 사용해 문자열에서 개체명 인식을 수행합니다.
- [NLTagger](https://developer.apple.com/documentation/naturallanguage/nltagger): 자연어 텍스트를 분석하는 tagger입니다.
:::

:::topic-grid
## 텍스트 임베딩
- [Finding similarities between pieces of text](https://developer.apple.com/documentation/naturallanguage/finding-similarities-between-pieces-of-text): 단어 또는 문장 사이의 의미적 거리를 계산합니다.
- [NLEmbedding](https://developer.apple.com/documentation/naturallanguage/nlembedding): 문자열을 벡터에 매핑해, 인접하고 유사한 문자열을 찾을 수 있게 하는 map입니다.
:::

:::topic-grid
## 문맥 임베딩
- [NLContextualEmbedding](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding): 자연어 발화에 대한 임베딩 벡터 시퀀스를 계산하는 모델입니다.
- [NLContextualEmbeddingKey](https://developer.apple.com/documentation/naturallanguage/nlcontextualembeddingkey): 문맥 임베딩을 필터링하거나 검색하는 데 사용할 수 있는 속성을 정의하는 클래스입니다.
- [NLScript](https://developer.apple.com/documentation/naturallanguage/nlscript): Natural Language 프레임워크가 지원하는 문자 체계입니다.
:::

:::topic-grid
## 자연어 모델
- [Creating a text classifier model](https://developer.apple.com/documentation/CreateML/creating-a-text-classifier-model): 자연어 텍스트를 분류하는 머신 러닝 모델을 학습시킵니다.
- [Creating a word tagger model](https://developer.apple.com/documentation/CreateML/creating-a-word-tagger-model): 자연어 텍스트의 개별 단어에 태그를 지정하는 머신 러닝 모델을 학습시킵니다.
- [NLModel](https://developer.apple.com/documentation/naturallanguage/nlmodel): 자연어 텍스트를 분류하거나 태그하기 위해 학습된 사용자 정의 모델입니다.
:::
