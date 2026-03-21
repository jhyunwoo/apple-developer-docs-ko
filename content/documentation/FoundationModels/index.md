---
route: /documentation/FoundationModels
source_url: https://developer.apple.com/documentation/FoundationModels
source_locale: en-US
section: docc
content_type: symbol
title: Foundation Models
original_title: Foundation Models
source_hash: e63d7fc38d2fc692a14ed74cf9f7373f23b9a27bf609c56b4993f4149e488a83
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:27:46+00:00'
last_translated_at: '2026-03-13T23:24:00+09:00'
---

# Foundation Models

언어 이해, 구조화된 출력, 도구 호출에 특화된 온디바이스 모델로 작업을 수행합니다.

## 개요

Foundation Models 프레임워크는 Apple Intelligence를 구동하는 Apple의 온디바이스 대규모 언어 모델에 접근할 수 있게 하여, 사용 사례에 맞는 지능형 작업을 수행하도록 도와줍니다. 텍스트 기반 온디바이스 모델은 요청에 적합한 새 텍스트를 생성할 수 있도록 패턴을 식별하며, 사용자가 작성한 코드를 호출해 특수한 작업을 수행하도록 결정할 수도 있습니다.

![foundation model을 나타내는 일러스트입니다.](https://developer.apple.com)

사용자가 만든 요청을 기반으로 텍스트 콘텐츠를 생성합니다. 온디바이스 모델은 요약, 엔터티 추출, 텍스트 이해, 다듬기, 게임용 대화 생성, 창의적인 콘텐츠 생성 등 다양한 텍스트 생성 작업에 뛰어납니다.

guided generation으로 전체 Swift 데이터 구조를 생성합니다. `@Generable` macro를 사용하면 사용자 정의 데이터 구조를 정의할 수 있고, 프레임워크는 모델이 해당 타입의 인스턴스를 생성하도록 강력한 보장을 제공합니다.

온디바이스 foundation model의 기능을 확장하려면 [Tool](https://developer.apple.com/documentation/foundationmodels/tool)을 사용해 모델이 요청 처리에 도움을 주기 위해 호출할 수 있는 사용자 정의 도구를 만듭니다. 예를 들어 모델은 로컬 또는 온라인 데이터베이스에서 정보를 검색하거나 앱의 서비스를 호출하는 도구를 사용할 수 있습니다.

온디바이스 언어 모델을 사용하려면 사용자가 자신의 기기에서 Apple Intelligence를 켜야 합니다. 지원되는 기기 목록은 [Apple Intelligence](https://www.apple.com/apple-intelligence/)를 참고합니다.

Foundation Models 프레임워크의 허용 가능한 사용에 대한 자세한 내용은 [Acceptable use requirements for the Foundation Models framework](https://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework)를 참고합니다.

### 관련 비디오

:::topic-grid
## 핵심 항목
- [Foundation Models updates](https://developer.apple.com/documentation/Updates/FoundationModels): Foundation Models의 중요한 변경 사항을 알아봅니다.
- [Generating content and performing tasks with Foundation Models](https://developer.apple.com/documentation/foundationmodels/generating-content-and-performing-tasks-with-foundation-models): 온디바이스 대규모 언어 모델을 프롬프트해 앱 경험을 향상합니다.
- [Adding intelligent app features with generative models](https://developer.apple.com/documentation/foundationmodels/adding-intelligent-app-features-with-generative-models): Foundation Models 프레임워크를 채택해 guided generation과 tool calling으로 견고한 앱을 빌드합니다.
- [SystemLanguageModel](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel): 텍스트 생성 작업을 수행할 수 있는 온디바이스 대규모 언어 모델입니다.
:::

:::topic-grid
## 프롬프팅
- [Prompting an on-device foundation model](https://developer.apple.com/documentation/foundationmodels/prompting-an-on-device-foundation-model): 온디바이스 모델에서 효과적인 결과를 얻기 위해 프롬프트를 조정합니다.
- [Updating prompts for new model versions](https://developer.apple.com/documentation/foundationmodels/updating-prompts-for-new-model-versions): 모델 개선을 최대한 활용할 수 있도록 앱이 사용하는 프롬프트를 버전 관리합니다.
- [Evaluating prompts to measure performance and improve model responses](https://developer.apple.com/documentation/foundationmodels/evaluating-prompts-to-measure-performance-and-improve-model-responses): 구조화된 평가를 사용해 프롬프트의 품질을 체계적으로 측정하고 개선합니다.
- [Analyzing the runtime performance of your Foundation Models app](https://developer.apple.com/documentation/foundationmodels/analyzing-the-runtime-performance-of-your-foundation-models-app): Instruments로 앱의 모델 사용을 프로파일링해 token 소비를 최적화하고 응답 시간을 개선합니다.
- [LanguageModelSession](https://developer.apple.com/documentation/foundationmodels/languagemodelsession): 언어 모델과 상호 작용하는 세션을 나타내는 객체입니다.
- [Instructions](https://developer.apple.com/documentation/foundationmodels/instructions): 프롬프트에 대해 모델의 의도된 동작을 정의하기 위해 제공하는 세부 사항입니다.
- [Prompt](https://developer.apple.com/documentation/foundationmodels/prompt): 사용자가 모델에 보내는 프롬프트입니다.
- [Transcript](https://developer.apple.com/documentation/foundationmodels/transcript): 세션과의 상호 작용을 반영하는 항목들의 선형 기록입니다.
- [GenerationOptions](https://developer.apple.com/documentation/foundationmodels/generationoptions): 모델이 프롬프트에 대한 응답을 생성하는 방식을 제어하는 옵션입니다.
:::

:::topic-grid
## Guided generation
- [Generating Swift data structures with guided generation](https://developer.apple.com/documentation/foundationmodels/generating-swift-data-structures-with-guided-generation): 원하는 출력을 프로그래밍 방식으로 설명해 견고한 앱을 만듭니다.
- [Generable](https://developer.apple.com/documentation/foundationmodels/generable): 모델이 프롬프트에 응답할 때 사용하는 타입입니다.
:::

:::topic-grid
## Tool calling
- [Expanding generation with tool calling](https://developer.apple.com/documentation/foundationmodels/expanding-generation-with-tool-calling): 모델이 사용 사례에 특화된 작업을 수행할 수 있게 하는 도구를 빌드합니다.
- [Generate dynamic game content with guided generation and tools](https://developer.apple.com/documentation/foundationmodels/generate-dynamic-game-content-with-guided-generation-and-tools): AI가 생성한 대화와 플레이어 맞춤형 조우를 통해 게임 플레이를 더 생동감 있게 만듭니다.
- [Tool](https://developer.apple.com/documentation/foundationmodels/tool): 런타임에 정보를 수집하거나 부수 효과를 수행하기 위해 모델이 호출할 수 있는 도구입니다.
:::

:::topic-grid
## 안전성
- [Improving the safety of generative model output](https://developer.apple.com/documentation/foundationmodels/improving-the-safety-of-generative-model-output): 민감한 입력을 적절히 처리하고 사용자를 존중하는 생성 경험을 만듭니다.
- [SystemLanguageModel.Guardrails](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/guardrails): Guardrail은 모델 입력과 출력에서 민감한 콘텐츠를 표시합니다.
:::

:::topic-grid
## 언어 및 로캘
- [Supporting languages and locales with Foundation Models](https://developer.apple.com/documentation/foundationmodels/supporting-languages-and-locales-with-foundation-models): 사용자가 앱과 상호 작용할 때 선호하는 언어로 콘텐츠를 생성합니다.
- [supportsLocale(_:)](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/supportslocale(_:)): 지정한 locale이 모델에서 지원되는지를 나타내는 Boolean을 반환합니다.
- [LanguageModelSession.GenerationError.unsupportedLanguageOrLocale(_:)](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/generationerror/unsupportedlanguageorlocale(_:)): 모델이 지원하지 않는 언어로 응답하도록 프롬프트되었을 때 발생하는 오류를 나타냅니다.
:::

:::topic-grid
## 사용 사례
- [Categorizing and organizing data with content tags](https://developer.apple.com/documentation/foundationmodels/categorizing-and-organizing-data-with-content-tags): 콘텐츠 태깅 모델로 입력 텍스트 안의 주제, 동작, 객체, 감정을 식별합니다.
- [SystemLanguageModel.UseCase](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/usecase): 프롬프트 용도를 나타내는 타입입니다.
:::

:::topic-grid
## 피드백
- [LanguageModelFeedback](https://developer.apple.com/documentation/foundationmodels/languagemodelfeedback): 로그로 남기거나 Feedback Assistant에 첨부하기에 적합한 피드백입니다.
- [logFeedbackAttachment(sentiment:issues:desiredOutput:)](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/logfeedbackattachment(sentiment:issues:desiredoutput:)): Apple에 피드백을 보고할 때 첨부하는 세션 정보를 포함한 데이터를 기록하고 직렬화합니다.
:::
