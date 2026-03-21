---
route: /documentation/SoundAnalysis
source_url: https://developer.apple.com/documentation/SoundAnalysis
source_locale: en-US
section: docc
content_type: symbol
title: Sound Analysis
original_title: Sound Analysis
source_hash: 6476bfb33f9f88964d83bc63869fc7b7d1ca073d1f8cca8e7614578bb72f75c9
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:54:28+00:00'
last_translated_at: '2026-03-13T21:38:00+09:00'
---

# Sound Analysis

오디오 파일이나 스트림을 분석해 다양한 소리를 분류합니다.

## 개요

오디오 파일이나 스트림을 분석하는 [SNClassifySoundRequest](https://developer.apple.com/documentation/soundanalysis/snclassifysoundrequest)를 생성하면 웃음소리나 박수 같은 특정 소리를 앱에서 식별할 수 있습니다. sound request는 300개가 넘는 소리를 식별할 수 있습니다. 또는 custom Core ML 모델을 sound request에 제공하여 사용자 정의 소리 집합을 식별할 수도 있습니다. [Create ML](https://developer.apple.com/documentation/CreateML)의 오디오 데이터를 사용해 [MLSoundClassifier](https://developer.apple.com/documentation/CreateML/MLSoundClassifier)를 생성하면 custom sound classification 모델을 학습시킬 수 있습니다.

:::topic-grid
## 오디오 분석기
- [Classifying Sounds in an Audio File](https://developer.apple.com/documentation/soundanalysis/classifying-sounds-in-an-audio-file): 오디오 파일 분석기를 사용해 녹음 같은 파일 안의 개별 소리를 식별합니다.
- [SNAudioFileAnalyzer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer): 오디오 파일에 대해 sound classification request를 실행하는 분석기입니다.
- [Classifying Sounds in an Audio Stream](https://developer.apple.com/documentation/soundanalysis/classifying-sounds-in-an-audio-stream): 오디오 스트림 분석기를 사용해 마이크 같은 오디오 데이터 스트림 안의 개별 소리를 식별합니다.
- [SNAudioStreamAnalyzer](https://developer.apple.com/documentation/soundanalysis/snaudiostreamanalyzer): 오디오 데이터 스트림을 분석하고 결과를 앱에 제공하기 위해 생성하는 객체입니다.
:::

:::topic-grid
## 소리 분류 요청
- [Classifying Live Audio Input with a Built-in Sound Classifier](https://developer.apple.com/documentation/soundanalysis/classifying-live-audio-input-with-a-built-in-sound-classifier): 학습된 classifier를 사용해 수백 가지 소리를 감지하고 식별합니다.
- [SNClassifySoundRequest](https://developer.apple.com/documentation/soundanalysis/snclassifysoundrequest): Core ML 모델을 사용해 소리를 분류하는 요청입니다.
- [SNClassificationResult](https://developer.apple.com/documentation/soundanalysis/snclassificationresult): 시간 범위 안에서 가장 높은 순위를 기록한 분류 결과를 담는 결과입니다.
:::

:::topic-grid
## 오류
- [SNError](https://developer.apple.com/documentation/soundanalysis/snerror): Sound Analysis 프레임워크의 오류입니다.
- [SNError.Code](https://developer.apple.com/documentation/soundanalysis/snerror/code): Sound Analysis 프레임워크가 생성하는 열거형 오류 코드입니다.
- [SNErrorDomain](https://developer.apple.com/documentation/soundanalysis/snerrordomain): Sound Analysis 오류 도메인을 식별하는 문자열입니다.
:::
