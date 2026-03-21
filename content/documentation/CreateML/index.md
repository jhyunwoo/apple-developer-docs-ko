---
route: /documentation/CreateML
source_url: https://developer.apple.com/documentation/CreateML
source_locale: en-US
section: docc
content_type: symbol
title: Create ML
original_title: Create ML
source_hash: 901c5b124096556b5966c4efb3e1d95a437d8f2361216c67d9b43c1d10cd95f5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:29:46+00:00'
last_translated_at: '2026-03-13T20:10:00+09:00'
---

# Create ML

앱에서 사용할 머신 러닝 모델을 만듭니다.

## 개요

Swift와 macOS playground 같은 익숙한 도구와 함께 Create ML을 사용해 Mac에서 사용자 정의 머신 러닝 모델을 만들고 훈련하십시오. 이미지 인식, 텍스트 의미 추출, 수치 값 간 관계 찾기 같은 작업을 수행하도록 모델을 훈련할 수 있습니다.

![이미지, 텍스트, 기타 구조화된 데이터를 Create ML과 함께 사용해 Core ML 모델을 훈련하는 방식을 보여 주는 다이어그램입니다.](https://developer.apple.com)

대표적인 샘플을 보여 주어 모델이 패턴을 인식하도록 훈련합니다. 예를 들어 서로 다른 개의 이미지를 많이 보여 주어 개를 인식하는 모델을 훈련할 수 있습니다. 모델을 훈련한 후에는 이전에 본 적 없는 데이터로 테스트하고, 작업을 얼마나 잘 수행했는지 평가합니다. 모델이 충분히 잘 동작하면 [Core ML](https://developer.apple.com/documentation/CoreML)을 사용해 앱에 통합할 준비가 된 것입니다.

![Create ML 워크플로를 보여 주는 다이어그램입니다. 데이터 수집, 모델 훈련, 훈련된 모델 평가의 흐름을 나타냅니다.](https://developer.apple.com)

Create ML은 Photos와 Siri 같은 Apple 제품에 내장된 머신 러닝 인프라를 활용합니다. 이는 이미지 분류와 자연어 모델의 크기가 더 작고 훈련 시간도 훨씬 짧다는 뜻입니다.

:::topic-grid
## 이미지 모델
- [Creating an Image Classifier Model](https://developer.apple.com/documentation/createml/creating-an-image-classifier-model): 이미지를 분류하는 머신 러닝 모델을 훈련하고 Core ML 앱에 추가합니다.
- [MLImageClassifier](https://developer.apple.com/documentation/createml/mlimageclassifier): 이미지를 분류하도록 훈련하는 모델입니다.
- [MLObjectDetector](https://developer.apple.com/documentation/createml/mlobjectdetector): 이미지 안의 하나 이상의 객체를 분류하도록 훈련하는 모델입니다.
- [MLHandPoseClassifier](https://developer.apple.com/documentation/createml/mlhandposeclassifier): 제공한 사람 손 이미지로 훈련하여 손 자세 분류 모델을 만드는 작업입니다.
:::

:::topic-grid
## 비디오 모델
- [Creating an Action Classifier Model](https://developer.apple.com/documentation/createml/creating-an-action-classifier-model): 사람의 몸 움직임을 인식하는 머신 러닝 모델을 훈련합니다.
- [Detecting human actions in a live video feed](https://developer.apple.com/documentation/CreateML/detecting-human-actions-in-a-live-video-feed): 일련의 비디오 프레임에서 사람의 자세 데이터를 action classification 모델로 보내 몸 움직임을 식별합니다.
- [MLActionClassifier](https://developer.apple.com/documentation/createml/mlactionclassifier): 비디오로 훈련하여 사람의 몸 움직임을 분류하는 모델입니다.
- [MLHandActionClassifier](https://developer.apple.com/documentation/createml/mlhandactionclassifier): 제공한 사람 손 움직임 비디오로 훈련하여 손 동작 분류 모델을 만드는 작업입니다.
- [MLStyleTransfer](https://developer.apple.com/documentation/createml/mlstyletransfer): 한 이미지의 스타일을 다른 이미지나 비디오에 적용하도록 훈련하는 모델입니다.
:::

:::topic-grid
## 텍스트 모델
- [Creating a text classifier model](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model): 자연어 텍스트를 분류하는 머신 러닝 모델을 훈련합니다.
- [Creating a word tagger model](https://developer.apple.com/documentation/createml/creating-a-word-tagger-model): 자연어 텍스트의 개별 단어에 태그를 붙이는 머신 러닝 모델을 훈련합니다.
- [MLTextClassifier](https://developer.apple.com/documentation/createml/mltextclassifier): 자연어 텍스트를 분류하도록 훈련하는 모델입니다.
- [MLWordTagger](https://developer.apple.com/documentation/createml/mlwordtagger): 자연어 텍스트를 단어 수준에서 분류하도록 훈련하는 단어 태깅 모델입니다.
- [MLGazetteer](https://developer.apple.com/documentation/createml/mlgazetteer): 자연어 텍스트를 분석하는 태거를 보강하는 용어와 라벨의 모음입니다.
- [MLWordEmbedding](https://developer.apple.com/documentation/createml/mlwordembedding): 문자열 이웃을 살펴 유사한 문자열을 찾을 수 있게 하는 벡터 공간상의 문자열 맵입니다.
:::

:::topic-grid
## 사운드 모델
- [MLSoundClassifier](https://developer.apple.com/documentation/createml/mlsoundclassifier): 오디오 파일로 훈련하여 기기에서 소리를 인식하고 식별하는 머신 러닝 모델입니다.
:::

:::topic-grid
## 모션 모델
- [MLActivityClassifier](https://developer.apple.com/documentation/createml/mlactivityclassifier): 모션 센서 데이터를 분류하도록 훈련하는 모델입니다.
:::

:::topic-grid
## 표 형식 모델
- [Creating a model from tabular data](https://developer.apple.com/documentation/CreateML/creating-a-model-from-tabular-data): Core ML을 사용해 표 형식 데이터를 가져오고 관리하며 머신 러닝 모델을 훈련합니다.
- [MLClassifier](https://developer.apple.com/documentation/createml/mlclassifier): 데이터를 이산적인 범주로 분류하도록 훈련하는 모델입니다.
- [MLRegressor](https://developer.apple.com/documentation/createml/mlregressor): 연속 값을 추정하도록 훈련하는 모델입니다.
- [MLRecommender](https://developer.apple.com/documentation/createml/mlrecommender): 항목 유사성, 그룹화, 선택적으로 항목 평점을 바탕으로 추천을 하도록 훈련하는 모델입니다.
:::

:::topic-grid
## 표 형식 데이터
- [MLDataTable](https://developer.apple.com/documentation/createml/mldatatable): 머신 러닝 모델의 훈련 또는 평가를 위한 데이터 테이블입니다.
- [MLDataValue](https://developer.apple.com/documentation/createml/mldatavalue): 데이터 테이블 셀의 값입니다.
- [Data visualizations](https://developer.apple.com/documentation/createml/data-visualizations): playground에서 데이터 테이블과 열의 이미지를 렌더링합니다.
:::

:::topic-grid
## 모델 정확도
- [Improving Your Model’s Accuracy](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy): 지표를 사용해 머신 러닝 모델의 성능을 조정합니다.
- [MLClassifierMetrics](https://developer.apple.com/documentation/createml/mlclassifiermetrics): 분류기 성능을 평가하는 데 사용하는 지표입니다.
- [MLRegressorMetrics](https://developer.apple.com/documentation/createml/mlregressormetrics): 회귀기 성능을 평가하는 데 사용하는 지표입니다.
- [MLWordTaggerMetrics](https://developer.apple.com/documentation/createml/mlwordtaggermetrics): 단어 태거 성능을 평가하는 데 사용하는 지표입니다.
- [MLRecommenderMetrics](https://developer.apple.com/documentation/createml/mlrecommendermetrics): 추천기 성능을 평가하는 데 사용하는 지표입니다.
- [MLObjectDetectorMetrics](https://developer.apple.com/documentation/createml/mlobjectdetectormetrics): 객체 탐지기 성능을 평가하는 데 사용하는 지표입니다.
:::

:::topic-grid
## 모델 훈련 제어
- [MLJob](https://developer.apple.com/documentation/createml/mljob): 진행 상황을 모니터링하거나 실행을 종료하는 데 사용하는 모델의 비동기 훈련 세션 표현입니다.
- [MLTrainingSession](https://developer.apple.com/documentation/createml/mltrainingsession): 모델의 비동기 훈련 세션의 현재 상태입니다.
- [MLTrainingSessionParameters](https://developer.apple.com/documentation/createml/mltrainingsessionparameters): 훈련 세션의 구성 설정입니다.
- [MLCheckpoint](https://developer.apple.com/documentation/createml/mlcheckpoint): 특징 추출 또는 훈련 단계 중 특정 시점에서의 모델 비동기 훈련 세션 상태입니다.
:::

:::topic-grid
## 지원 타입
- [MLCreateError](https://developer.apple.com/documentation/createml/mlcreateerror): 모델 훈련, 예측 생성, 파일 시스템에 모델 쓰기 등 다양한 작업 수행 중 Create ML이 발생시키는 오류입니다.
- [MLModelMetadata](https://developer.apple.com/documentation/createml/mlmodelmetadata): Core ML 모델 파일에 저장되는 모델 정보입니다.
- [MLSplitStrategy](https://developer.apple.com/documentation/createml/mlsplitstrategy): 일반적으로 훈련 데이터셋에서 검증 데이터셋을 만드는 데 사용하는 데이터 분할 방식입니다.
:::

:::topic-grid
## 글
- [Data visualizations](https://developer.apple.com/documentation/createml/create-ml-utilties): playground에서 데이터 테이블과 열의 이미지를 렌더링합니다.
- [Detecting human actions in a live video feed](https://developer.apple.com/documentation/createml/detecting-human-actions-in-a-live-video-feed): 일련의 비디오 프레임에서 사람의 자세 데이터를 action classification 모델로 보내 몸 움직임을 식별합니다.
- [Gathering Training Videos for an Action Classifier](https://developer.apple.com/documentation/createml/recording-or-choosing-training-videos): action classifier를 효과적으로 훈련하는 품질 좋은 예제 비디오를 수집합니다.
:::

:::topic-grid
## 함수
- [show(_:)](https://developer.apple.com/documentation/createml/show(_:)): 타입이 지정되지 않은 열의 스트리밍 시각화를 생성합니다.
- [show(_:_:)](https://developer.apple.com/documentation/createml/show(_:_:)): 두 개의 타입이 지정되지 않은 열에 대한 스트리밍 플롯 시각화를 생성합니다.
:::

:::topic-grid
## 열거형
- [MLBoundingBoxAnchor](https://developer.apple.com/documentation/createml/mlboundingboxanchor): annotation 좌표가 기준점으로 사용하는 bounding box 내부 위치입니다.
- [MLBoundingBoxCoordinatesOrigin](https://developer.apple.com/documentation/createml/mlboundingboxcoordinatesorigin): annotation 좌표가 원점으로 사용하는 이미지 내부 위치입니다.
- [MLBoundingBoxUnits](https://developer.apple.com/documentation/createml/mlboundingboxunits): bounding box annotation이 위치와 크기를 정의할 때 사용하는 단위입니다.
:::
