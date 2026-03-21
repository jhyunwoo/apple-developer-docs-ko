---
route: /documentation/Speech
source_url: https://developer.apple.com/documentation/Speech
source_locale: en-US
section: docc
content_type: symbol
title: Speech
original_title: Speech
source_hash: 4bcaa273909f24b119e03c6f16ce8798ec60c46e86d985b0f41c4b10b84db23b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T05:20:37+00:00'
last_translated_at: '2026-03-13T05:20:37+00:00'
---

# Speech

실시간 또는 사전 녹음된 오디오에서 음성 인식을 수행하고, 전사 결과, 대체 해석, 결과의 신뢰도 수준을 받습니다.

## 개요

Speech 프레임워크를 사용해 녹음된 오디오나 실시간 오디오에서 말한 단어를 인식하세요. 키보드의 받아쓰기 지원은 음성 인식을 사용해 오디오 콘텐츠를 텍스트로 변환합니다. 이 프레임워크는 비슷한 동작을 제공하지만, 키보드가 없어도 사용할 수 있다는 차이가 있습니다. 예를 들어 음성 인식을 사용해 음성 명령을 인식하거나 앱의 다른 부분에서 텍스트 받아쓰기를 처리할 수 있습니다.

[SpeechTranscriber](https://developer.apple.com/documentation/speech/speechtranscriber) 클래스와 다른 모듈 클래스는 구체적인 서비스를 제공합니다. [AssetInventory](https://developer.apple.com/documentation/speech/assetinventory) 클래스는 시스템이 이러한 클래스를 지원하는 데 필요한 에셋을 갖추도록 보장합니다. [SpeechAnalyzer](https://developer.apple.com/documentation/speech/speechanalyzer) 클래스는 이러한 클래스를 사용하는 분석 세션을 관리합니다.

이 클래스들을 함께 사용하는 방식에 대한 전반적인 이해는 [SpeechAnalyzer](https://developer.apple.com/documentation/speech/speechanalyzer)를 참고하세요.

:::topic-grid
## 핵심
- [Bringing advanced speech-to-text capabilities to your app](https://developer.apple.com/documentation/speech/bringing-advanced-speech-to-text-capabilities-to-your-app): SpeechAnalyzer를 사용해 실시간 음성-텍스트 전사를 앱에 통합하는 방법을 알아봅니다.
- [SpeechAnalyzer](https://developer.apple.com/documentation/speech/speechanalyzer): 다양한 방식으로 음성 오디오 콘텐츠를 분석하고 분석 세션을 관리합니다.
- [AssetInventory](https://developer.apple.com/documentation/speech/assetinventory): 전사 또는 기타 분석에 필요한 에셋을 관리합니다.
:::

:::topic-grid
## 모듈
- [SpeechTranscriber](https://developer.apple.com/documentation/speech/speechtranscriber): 일반적인 대화와 범용 목적에 적합한 음성-텍스트 전사 모듈입니다.
- [DictationTranscriber](https://developer.apple.com/documentation/speech/dictationtranscriber): 시스템 받아쓰기 기능과 유사하고 오래된 기기와도 호환되는 음성-텍스트 전사 모듈입니다.
- [SpeechDetector](https://developer.apple.com/documentation/speech/speechdetector): 음성 활동 감지(VAD) 분석을 수행하는 모듈입니다.
- [SpeechModule](https://developer.apple.com/documentation/speech/speechmodule): 모든 analyzer 모듈이 따르는 프로토콜입니다.
- [LocaleDependentSpeechModule](https://developer.apple.com/documentation/speech/localedependentspeechmodule): 로캘별 에셋이 필요한 모듈입니다.
:::

:::topic-grid
## 입력과 출력
- [AnalyzerInput](https://developer.apple.com/documentation/speech/analyzerinput): 시간 코드가 포함된 오디오 데이터입니다.
- [SpeechModuleResult](https://developer.apple.com/documentation/speech/speechmoduleresult): 모든 모듈 결과가 따르는 프로토콜입니다.
:::

:::topic-grid
## 사용자 정의 어휘
- [AnalysisContext](https://developer.apple.com/documentation/speech/analysiscontext): analyzer 간에 공유될 수 있는 문맥 정보입니다.
- [SFSpeechLanguageModel](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel): 사용자 정의 학습 데이터로 구축한 언어 모델입니다.
- [SFSpeechLanguageModel.Configuration](https://developer.apple.com/documentation/speech/sfspeechlanguagemodel/configuration): 사용자 정의 언어 모델과 특화된 어휘의 위치를 설명하는 객체입니다.
- [SFCustomLanguageModelData](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata): 사용자 정의 언어 모델 학습 데이터를 생성하고 내보내는 객체입니다.
:::

:::topic-grid
## 에셋 및 리소스 관리
- [AssetInstallationRequest](https://developer.apple.com/documentation/speech/assetinstallationrequest): 선택한 에셋을 설명하고, 다운로드하고, 설치하는 객체입니다.
- [SpeechModels](https://developer.apple.com/documentation/speech/speechmodels): 모델 관리와 관련된 메서드를 위한 네임스페이스입니다.
:::

:::topic-grid
## 레거시 API
- [Speech Recognition in Objective-C](https://developer.apple.com/documentation/speech/speech-recognition-in-objc): Objective-C 코드에서 음성 인식을 수행하려면 이 클래스들을 사용하세요.
:::
