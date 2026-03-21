---
route: /documentation/CreateMLComponents
source_url: https://developer.apple.com/documentation/CreateMLComponents
source_locale: en-US
section: docc
content_type: symbol
title: Create ML Components
original_title: Create ML Components
source_hash: a9d7df33fffd63826c5f192adc179904a59ecc10bce378064a6742e27f2320c1
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:26:30+00:00'
last_translated_at: '2026-03-14T00:42:00+09:00'
---

# Create ML Components

앱에서 더 세밀하게 맞춤화할 수 있는 머신 러닝 모델을 만듭니다.

## 개요

Create ML Components는 하나로 묶여 보이던 작업의 내부 구성 요소를 드러내는 핵심 기술입니다. 전체 흐름을 직접 제어하면서 더 높은 유연성을 위해 사용자 정의 파이프라인을 만들 수 있습니다.

![4개의 컴포넌트 사각형으로 표현된 작업을 보여 주는 흐름도입니다. 흐름은 왼쪽 아래의 사각형에서 시작하며, 이 사각형에는 입력 이미지를 나타내는 카메라 아이콘과 `Component 0`이라는 레이블이 있습니다. 이 사각형에서 두 개의 화살표가 나가는데, 하나는 아래 세 사각형 위에 있는 단일 사각형으로 향합니다. 위쪽 사각형에는 이미지 향상을 나타내는 마법 지팡이와 네 개의 별 아이콘이 있고 `Component 1`이라는 레이블이 있습니다. 두 번째 화살표는 아래 가운데 사각형으로 향하며, 이 사각형에는 이미지 크기 조절을 나타내는 화면 안의 화면 확대 아이콘과 `Component 2`라는 레이블이 있습니다. 이어서 위쪽 단일 사각형에서 아래 오른쪽 사각형으로 화살표가 내려가며, 이 사각형에는 완성된 이미지를 나타내는 사진 아이콘과 `Component n`이라는 레이블이 있습니다. 아래 가운데 사각형과 오른쪽 사각형은 점 세 개로 연결되어 있습니다.](https://developer.apple.com)

구성 요소를 사용하면 머신 러닝 작업을 세부 수준까지 나누어 구성할 수 있습니다. 이미지, 비디오, 표 형식 데이터에 맞는 분류기를 구체적으로 선택할 수 있습니다.

:::topic-grid
## 이미지 구성 요소
- [Augmenting images to expand your training data](https://developer.apple.com/documentation/createmlcomponents/augmenting-images-to-expand-your-training-data): 변형된 학습 이미지를 사용해 모델을 개선합니다.
- [Creating a multi-label image classifier](https://developer.apple.com/documentation/createmlcomponents/creating-a-multi-label-image-classifier): 하나의 이미지에 여러 레이블을 할당하는 머신 러닝 모델을 학습시킵니다.
- [ImageReader](https://developer.apple.com/documentation/createmlcomponents/imagereader): 이미지 파일 reader입니다.
- [ImageFeatureExtractor](https://developer.apple.com/documentation/createmlcomponents/imagefeatureextractor): 이미지를 받아 이미지 feature를 출력하는 transformer입니다.
- [ImageCropper](https://developer.apple.com/documentation/createmlcomponents/imagecropper): 이미지 crop transformer입니다.
- [ImageScaler](https://developer.apple.com/documentation/createmlcomponents/imagescaler): 이미지 크기 조절 transformer입니다.
- [ImageFeaturePrint](https://developer.apple.com/documentation/createmlcomponents/imagefeatureprint): ImageFeaturePrint 이미지 feature extractor입니다.
- [ImageBlur](https://developer.apple.com/documentation/createmlcomponents/imageblur): 이미지 블러 transformer입니다.
- [ImageColorTransformer](https://developer.apple.com/documentation/createmlcomponents/imagecolortransformer): 이미지 색상 transformer입니다.
- [ImageExposureAdjuster](https://developer.apple.com/documentation/createmlcomponents/imageexposureadjuster): 이미지 노출 조정 transformer입니다.
- [ImageFlipper](https://developer.apple.com/documentation/createmlcomponents/imageflipper): 이미지 뒤집기 transformer입니다.
- [ImageRotator](https://developer.apple.com/documentation/createmlcomponents/imagerotator): 이미지 회전 transformer입니다.
- [RandomImageNoiseGenerator](https://developer.apple.com/documentation/createmlcomponents/randomimagenoisegenerator): 이미지에 무작위 노이즈를 추가하는 transformer입니다.
- [MLModelImageFeatureExtractor](https://developer.apple.com/documentation/createmlcomponents/mlmodelimagefeatureextractor): `MLModel`이 제공하는 이미지 feature extractor입니다.
:::

:::topic-grid
## 자세 구성 요소
- [Counting human body action repetitions in a live video feed](https://developer.apple.com/documentation/createmlcomponents/counting-human-body-action-repetitions-in-a-live-video-feed): Create ML Components를 사용해 비디오 프레임 시퀀스를 분석하고 사람의 반복적 또는 주기적인 신체 움직임 횟수를 셉니다.
- [Pose](https://developer.apple.com/documentation/createmlcomponents/pose): 사람, 손, 또는 그 조합의 관절 keypoint를 담는 자세입니다.
- [JointKey](https://developer.apple.com/documentation/createmlcomponents/jointkey): 관절을 고유하게 식별하는 키입니다.
- [JointPoint](https://developer.apple.com/documentation/createmlcomponents/jointpoint): 위치와 점수 정보를 담는 자세 안의 관절입니다.
- [PoseSelector](https://developer.apple.com/documentation/createmlcomponents/poseselector): 자세 배열에서 하나의 자세를 선택하는 transformer입니다.
- [PoseSelectionStrategy](https://developer.apple.com/documentation/createmlcomponents/poseselectionstrategy): 자세 선택 전략입니다.
- [JointsSelector](https://developer.apple.com/documentation/createmlcomponents/jointsselector): 자세에서 관절을 선택하는 selector입니다.
- [HumanBodyPoseExtractor](https://developer.apple.com/documentation/createmlcomponents/humanbodyposeextractor): 사람 신체 자세 이미지 feature extractor입니다.
- [HumanHandPoseExtractor](https://developer.apple.com/documentation/createmlcomponents/humanhandposeextractor): 사람 손 자세 이미지 feature extractor입니다.
- [HumanBodyActionCounter](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter): 사람 신체 자세의 window를 받아 누적된 반복 동작 수를 생성하는 transformer입니다.
- [HumanBodyActionPeriodPredictor](https://developer.apple.com/documentation/createmlcomponents/humanbodyactionperiodpredictor): 자세의 window를 받아 예측 window를 생성하는 사람 신체 동작 주기 예측 transformer입니다.
:::

:::topic-grid
## 오디오 구성 요소
- [AudioReader](https://developer.apple.com/documentation/createmlcomponents/audioreader): 오디오 파일 reader입니다.
- [AudioFeaturePrint](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint): 오디오 버퍼에서 오디오 feature를 추출하는 stream transformer입니다.
- [AudioConvertingTransformer](https://developer.apple.com/documentation/createmlcomponents/audioconvertingtransformer): 오디오 변환용 transformer입니다.
:::

:::topic-grid
## 시계열 구성 요소
- [Creating a time-series classifier](https://developer.apple.com/documentation/createmlcomponents/creating-a-time-series-classifier): 시계열 신호의 클래스 레이블을 예측하는 머신 러닝 모델을 학습시킵니다.
- [Creating a time-series forecaster](https://developer.apple.com/documentation/createmlcomponents/creating-a-time-series-forecaster): 과거 데이터를 사용해 머신 러닝 모델을 학습시키고 미래 데이터 포인트를 예측합니다.
- [DateFeatures](https://developer.apple.com/documentation/createmlcomponents/datefeatures): 날짜 및 시간 feature 집합입니다.
- [DateFeatureExtractor](https://developer.apple.com/documentation/createmlcomponents/datefeatureextractor): 시간 및 날짜 feature extractor입니다.
- [LinearTimeSeriesForecaster](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster): 시계열 예측 estimator입니다.
- [LinearTimeSeriesForecasterConfiguration](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecasterconfiguration): 선형 시계열 forecaster의 구성입니다.
- [TimeSeriesForecasterBatches](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterbatches): 시계열 형태 배열에서 forecaster batch의 시퀀스입니다.
- [TimeSeriesForecasterAnnotatedWindows](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterannotatedwindows): 시계열 형태 배열에서 예측 window의 시퀀스입니다.
- [TemporalFeature](https://developer.apple.com/documentation/createmlcomponents/temporalfeature): 세그먼트 식별자와 feature 값을 담는 temporal feature입니다.
- [TemporalSequence](https://developer.apple.com/documentation/createmlcomponents/temporalsequence): temporal feature를 위한 async sequence입니다.
- [TemporalSegmentIdentifier](https://developer.apple.com/documentation/createmlcomponents/temporalsegmentidentifier): temporal sequence의 세그먼트를 고유하게 식별합니다.
- [SlidingWindows](https://developer.apple.com/documentation/createmlcomponents/slidingwindows): 시계열 형태 배열 위의 window 시퀀스입니다.
- [SlidingWindowTransformer](https://developer.apple.com/documentation/createmlcomponents/slidingwindowtransformer): 입력 요소를 그룹화하는 temporal transformer입니다.
- [Downsampler](https://developer.apple.com/documentation/createmlcomponents/downsampler): 입력 스트림을 다운샘플링하는 temporal transformer입니다.
- [VideoReader](https://developer.apple.com/documentation/createmlcomponents/videoreader): 비디오 파일 reader입니다.
- [TemporalFileSegment](https://developer.apple.com/documentation/createmlcomponents/temporalfilesegment): 시간 기반 파일의 특정 세그먼트를 식별하는 URL과 시간 범위입니다.
- [AnyTemporalIterator](https://developer.apple.com/documentation/createmlcomponents/anytemporaliterator): 타입이 지워진 async iterator입니다.
- [AnyTemporalSequence](https://developer.apple.com/documentation/createmlcomponents/anytemporalsequence): 타입이 지워진 temporal sequence입니다.
- [PreprocessedFeatureSequence](https://developer.apple.com/documentation/createmlcomponents/preprocessedfeaturesequence): eager하게 저장된 temporal feature의 비동기 시퀀스입니다.
:::

:::topic-grid
## 객체 감지 구성 요소
- [DetectedObject](https://developer.apple.com/documentation/createmlcomponents/detectedobject): 감지 결과 안의 항목입니다.
- [ObjectDetectionAnnotation](https://developer.apple.com/documentation/createmlcomponents/objectdetectionannotation): 객체 감지 annotation입니다.
- [ObjectDetectionMetrics](https://developer.apple.com/documentation/createmlcomponents/objectdetectionmetrics): 객체 감지 모델용 metric입니다.
:::

:::topic-grid
## 표 형식 구성 요소
- [TabularTransformer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformer): data frame을 변환하는 tabular transformer입니다.
- [TabularEstimator](https://developer.apple.com/documentation/createmlcomponents/tabularestimator): data frame의 데이터 세트에 맞춰 transformer를 생성하는 tabular estimator입니다.
- [SupervisedTabularEstimator](https://developer.apple.com/documentation/createmlcomponents/supervisedtabularestimator): data frame의 데이터 세트에 맞춰 transformer를 생성하는 감독형 tabular estimator입니다.
- [ColumnSelector](https://developer.apple.com/documentation/createmlcomponents/columnselector): 선택한 열 집합에 estimator를 적용하는 연산입니다.
- [ColumnSelectorTransformer](https://developer.apple.com/documentation/createmlcomponents/columnselectortransformer): data frame의 특정 열에 기본 transformer를 적용하는 transformer입니다.
- [ColumnSelection](https://developer.apple.com/documentation/createmlcomponents/columnselection): data frame에서 선택한 열 집합입니다.
- [ColumnConcatenator](https://developer.apple.com/documentation/createmlcomponents/columnconcatenator): data frame의 모든 수치형 열을 각 행마다 하나의 shaped array로 이어 붙이는 transformer입니다.
- [PreprocessingSupervisedTabularEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtabularestimator): 전처리 transformer와 감독형 tabular estimator를 조합하는 감독형 tabular estimator입니다.
- [PreprocessingTabularEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingtabularestimator): 전처리 transformer와 estimator를 조합하는 estimator입니다.
- [PreprocessingUpdatableSupervisedTabularEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtabularestimator): 전처리 transformer와 업데이트 가능한 감독형 estimator를 조합하는 업데이트 가능한 감독형 estimator입니다.
- [PreprocessingUpdatableTabularEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletabularestimator): 전처리 transformer와 업데이트 가능한 estimator를 조합하는 업데이트 가능한 estimator입니다.
:::

:::topic-grid
## 프로토콜
- [Transformer](https://developer.apple.com/documentation/createmlcomponents/transformer): 입력을 받아 출력을 생성하는 transformer입니다.
- [TemporalTransformer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer): temporal feature의 비동기 입력 시퀀스를 받아 비동기 출력 시퀀스를 생성하는 transformer입니다.
- [RandomTransformer](https://developer.apple.com/documentation/createmlcomponents/randomtransformer): 입력과 난수 생성기를 받아 무작위화된 출력을 생성하는 transformer입니다.
- [Estimator](https://developer.apple.com/documentation/createmlcomponents/estimator): 데이터 세트에 맞춰 transformer를 생성하는 estimator입니다.
- [TemporalEstimator](https://developer.apple.com/documentation/createmlcomponents/temporalestimator): temporal feature 시퀀스에 맞춰 transformer를 생성하는 estimator입니다.
- [SupervisedEstimator](https://developer.apple.com/documentation/createmlcomponents/supervisedestimator): 데이터 세트에 맞춰 transformer를 생성하는 감독형 estimator입니다.
- [SupervisedTemporalEstimator](https://developer.apple.com/documentation/createmlcomponents/supervisedtemporalestimator): annotation이 포함된 temporal feature 시퀀스에 맞춰 transformer를 생성하는 estimator입니다.
- [UpdatableEstimator](https://developer.apple.com/documentation/createmlcomponents/updatableestimator): 점진적으로 업데이트할 수 있는 estimator입니다.
- [UpdatableSupervisedEstimator](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimator): 점진적으로 업데이트할 수 있는 감독형 estimator입니다.
- [UpdatableSupervisedTemporalEstimator](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtemporalestimator): 점진적으로 업데이트할 수 있는 감독형 temporal estimator입니다.
- [UpdatableSupervisedTabularEstimator](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtabularestimator): 점진적으로 업데이트할 수 있는 감독형 tabular estimator입니다.
- [UpdatableTemporalEstimator](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimator): 점진적으로 업데이트할 수 있는 temporal estimator입니다.
- [UpdatableTabularEstimator](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimator): 점진적으로 업데이트할 수 있는 tabular estimator입니다.
:::

:::topic-grid
## Core ML 어댑터
- [MLModelTransformerAdaptor](https://developer.apple.com/documentation/createmlcomponents/mlmodeltransformeradaptor): Core ML 모델을 사용하는 transformer입니다.
- [MLModelClassifierAdaptor](https://developer.apple.com/documentation/createmlcomponents/mlmodelclassifieradaptor): Core ML 모델을 분류기로 사용하는 transformer입니다.
- [MLModelRegressorAdaptor](https://developer.apple.com/documentation/createmlcomponents/mlmodelregressoradaptor): Core ML 모델을 회귀기로 사용하는 transformer입니다.
- [ModelMetadata](https://developer.apple.com/documentation/createmlcomponents/modelmetadata): 모델에 대한 유용한 정보를 지정하는 user info key입니다.
:::

:::topic-grid
## Annotation
- [AnnotatedFiles](https://developer.apple.com/documentation/createmlcomponents/annotatedfiles): annotation이 지정된 파일 컬렉션입니다.
- [AnnotatedBatch](https://developer.apple.com/documentation/createmlcomponents/annotatedbatch): 감독형 estimator를 맞추기 위한 annotation 예제 batch입니다.
- [AnnotatedFeature](https://developer.apple.com/documentation/createmlcomponents/annotatedfeature): 감독형 estimator를 맞추기 위한 annotation 예제입니다.
- [AnnotatedFeatureProvider](https://developer.apple.com/documentation/createmlcomponents/annotatedfeatureprovider): 열에서 feature와 annotation을 선택하여 일반 estimator를 tabular estimator로 변환하는 adaptor입니다.
- [AnnotatedPrediction](https://developer.apple.com/documentation/createmlcomponents/annotatedprediction): annotation이 포함된 prediction입니다.
- [DataFrameTemporalAnnotationParameters](https://developer.apple.com/documentation/createmlcomponents/dataframetemporalannotationparameters): temporal annotation을 포함하는 data frame용 annotation 매개변수입니다.
:::

:::topic-grid
## 증강
- [ApplyEachRandomly](https://developer.apple.com/documentation/createmlcomponents/applyeachrandomly): 각 transformer를 확률에 따라 무작위로 적용합니다.
- [ApplyRandomly](https://developer.apple.com/documentation/createmlcomponents/applyrandomly): 주어진 확률에 따라 transformer를 무작위로 적용합니다.
- [AugmentationBuilder](https://developer.apple.com/documentation/createmlcomponents/augmentationbuilder): 증강 시퀀스입니다.
- [AugmentationSequence](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence): 증강된 요소의 async sequence입니다.
- [Augmenter](https://developer.apple.com/documentation/createmlcomponents/augmenter): augmenter입니다.
- [ChooseRandomly](https://developer.apple.com/documentation/createmlcomponents/chooserandomly): transformer 목록 중 하나를 무작위로 선택해 단일 변환을 적용합니다.
- [RandomImageCropper](https://developer.apple.com/documentation/createmlcomponents/randomimagecropper): 무작위 위치에서 이미지를 자릅니다.
- [ShuffleRandomly](https://developer.apple.com/documentation/createmlcomponents/shufflerandomly): 변환을 무작위 순서로 적용합니다.
- [UniformRandomFloatingPointParameter](https://developer.apple.com/documentation/createmlcomponents/uniformrandomfloatingpointparameter): 무작위로 생성된 부동소수점 입력 매개변수로 transformer를 적용합니다.
- [UniformRandomIntegerParameter](https://developer.apple.com/documentation/createmlcomponents/uniformrandomintegerparameter): 무작위로 생성된 정수 입력 매개변수로 transformer를 적용합니다.
- [UpsampledAugmentationSequence](https://developer.apple.com/documentation/createmlcomponents/upsampledaugmentationsequence): 증강된 요소의 async sequence입니다.
:::

:::topic-grid
## 이벤트 처리
- [Event](https://developer.apple.com/documentation/createmlcomponents/event): 파이프라인 상태를 유지합니다.
- [EventHandler](https://developer.apple.com/documentation/createmlcomponents/eventhandler): 처리 이벤트를 다루는 closure입니다.
- [MetricsKey](https://developer.apple.com/documentation/createmlcomponents/metricskey): metric을 고유하게 식별하는 키입니다.
:::

:::topic-grid
## 스케일러
- [StandardScaler](https://developer.apple.com/documentation/createmlcomponents/standardscaler): 평균을 제거하고 단위 분산으로 스케일링해 입력을 표준화하는 estimator입니다.
- [MaxAbsScaler](https://developer.apple.com/documentation/createmlcomponents/maxabsscaler): 최대 절대값이 1.0이 되도록 입력 값을 스케일링하는 estimator입니다.
- [MinMaxScaler](https://developer.apple.com/documentation/createmlcomponents/minmaxscaler): 모든 입력 값이 닫힌 범위 안에 들어가도록 스케일링하는 estimator입니다.
- [NormalizationScaler](https://developer.apple.com/documentation/createmlcomponents/normalizationscaler): 정규화 전략을 사용해 입력 값을 정규화하는 estimator입니다.
- [RobustScaler](https://developer.apple.com/documentation/createmlcomponents/robustscaler): 이상치에 강인한 통계를 사용해 입력을 스케일링하는 estimator입니다.
:::

:::topic-grid
## 전처리기
- [LinearTransformer](https://developer.apple.com/documentation/createmlcomponents/lineartransformer): 입력에 scale과 offset을 적용하는 transformer입니다.
- [ImputeTransformer](https://developer.apple.com/documentation/createmlcomponents/imputetransformer): 누락된 값을 미리 정의된 값으로 바꾸는 transformer입니다.
- [OneHotEncoder](https://developer.apple.com/documentation/createmlcomponents/onehotencoder): 범주형 값을 정수 배열로 인코딩하는 estimator입니다.
- [OrdinalEncoder](https://developer.apple.com/documentation/createmlcomponents/ordinalencoder): 범주형 값을 순서형 정수 값으로 인코딩하는 ordinal encoder estimator입니다.
- [NumericImputer](https://developer.apple.com/documentation/createmlcomponents/numericimputer): 숫자 입력의 누락된 값을 대체하는 estimator입니다.
- [Reshaper](https://developer.apple.com/documentation/createmlcomponents/reshaper): shaped array의 형태를 바꾸는 transformer입니다.
- [CategoricalImputer](https://developer.apple.com/documentation/createmlcomponents/categoricalimputer): 범주형 입력의 누락된 값을 대체하는 estimator입니다.
- [OptionalUnwrapper](https://developer.apple.com/documentation/createmlcomponents/optionalunwrapper): optional 요소의 래핑을 풀고 누락 값을 만나면 오류를 던지는 transformer입니다.
:::

:::topic-grid
## 회귀기
- [Regressor](https://developer.apple.com/documentation/createmlcomponents/regressor): 부동소수점 값을 예측하는 transformer입니다.
- [LinearRegressor](https://developer.apple.com/documentation/createmlcomponents/linearregressor): 선형 회귀기입니다.
- [LinearRegressorModel](https://developer.apple.com/documentation/createmlcomponents/linearregressormodel): 학습된 선형 회귀기 모델입니다.
- [MultivariateLinearRegressor](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor): 다변량 선형 회귀기입니다.
- [MultivariateLinearRegressorConfiguration](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressorconfiguration): 선형 회귀기 구성입니다.
- [MultivariateLinearRegressor.Model](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/model): 학습된 다변량 선형 회귀기 모델입니다.
- [FullyConnectedNetworkRegressor](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressor): 완전 연결 네트워크를 사용하는 회귀기입니다.
- [FullyConnectedNetworkRegressorModel](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressormodel): 완전 연결 네트워크를 사용하는 회귀기 모델입니다.
- [BoostedTreeRegressor](https://developer.apple.com/documentation/createmlcomponents/boostedtreeregressor): gradient boosted decision tree 회귀기입니다.
- [TreeRegressorModel](https://developer.apple.com/documentation/createmlcomponents/treeregressormodel): 학습된 tree 회귀기 모델입니다.
- [OptimizationStrategy](https://developer.apple.com/documentation/createmlcomponents/optimizationstrategy): 선형 최적화 전략입니다.
:::

:::topic-grid
## 직렬화
- [EstimatorDecoder](https://developer.apple.com/documentation/createmlcomponents/estimatordecoder): 모델 표현에서 값을 decode할 수 있는 타입입니다.
- [EstimatorEncoder](https://developer.apple.com/documentation/createmlcomponents/estimatorencoder): 값을 모델 표현으로 encode할 수 있는 타입입니다.
:::

:::topic-grid
## 분류기
- [Classifier](https://developer.apple.com/documentation/createmlcomponents/classifier): 분류 확률을 예측하는 estimator입니다.
- [LogisticRegressionClassifier](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier): 로지스틱 회귀 분류기입니다.
- [LogisticRegressionClassifierModel](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifiermodel): 학습된 로지스틱 회귀 분류기 모델입니다.
- [BoostedTreeClassifier](https://developer.apple.com/documentation/createmlcomponents/boostedtreeclassifier): gradient boosted decision tree 분류기입니다.
- [BoostedTreeConfiguration](https://developer.apple.com/documentation/createmlcomponents/boostedtreeconfiguration): boosted tree 구성입니다.
- [FullyConnectedNetworkClassifier](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier): 완전 연결 네트워크를 사용하는 분류기입니다.
- [FullyConnectedNetworkClassifierModel](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifiermodel): 완전 연결 네트워크를 사용하는 분류기 모델입니다.
- [FullyConnectedNetworkMultiLabelClassifier](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier): 다중 레이블 완전 연결 네트워크를 사용하는 분류기입니다.
- [FullyConnectedNetworkMultiLabelClassifierModel](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifiermodel): 다중 레이블 완전 연결 네트워크를 사용하는 분류기 모델입니다.
- [FullyConnectedNetworkConfiguration](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkconfiguration): 완전 연결 네트워크 구성입니다.
- [TreeClassifierModel](https://developer.apple.com/documentation/createmlcomponents/treeclassifiermodel): 학습된 tree 분류기 모델입니다.
- [TimeSeriesClassifier](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier)
- [TimeSeriesClassifierConfiguration](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifierconfiguration): 시계열 분류기 구성입니다.
:::

:::topic-grid
## 메트릭
- [Classification](https://developer.apple.com/documentation/createmlcomponents/classification): 분류 결과 안의 항목입니다.
- [ClassificationDistribution](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution): 각 분류 레이블의 확률을 담는 분류 분포입니다.
- [ClassificationMetrics](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics): 분류 metric입니다.
- [MultiLabelClassificationMetrics](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics): 다중 레이블 분류 metric입니다.
- [rootMeanSquaredError(_:)](https://developer.apple.com/documentation/createmlcomponents/rootmeansquarederror(_:)): 예측값과 실제값 사이의 root mean squared error를 계산합니다.
- [rootMeanSquaredError(_:_:)](https://developer.apple.com/documentation/createmlcomponents/rootmeansquarederror(_:_:)): 예측값과 실제값 사이의 root mean squared error를 계산합니다.
- [maximumAbsoluteError(_:)](https://developer.apple.com/documentation/createmlcomponents/maximumabsoluteerror(_:)): 예측값과 실제값 사이의 최대 절대 오차를 계산합니다.
- [maximumAbsoluteError(_:_:)](https://developer.apple.com/documentation/createmlcomponents/maximumabsoluteerror(_:_:)): 예측값과 실제값 사이의 최대 절대 오차를 계산합니다.
- [meanAbsoluteError(_:)](https://developer.apple.com/documentation/createmlcomponents/meanabsoluteerror(_:)): 예측값과 실제값 사이의 평균 절대 오차를 계산합니다.
- [meanAbsoluteError(_:_:)](https://developer.apple.com/documentation/createmlcomponents/meanabsoluteerror(_:_:)): 예측값과 실제값 사이의 평균 절대 오차를 계산합니다.
- [meanAbsolutePercentageError(_:)](https://developer.apple.com/documentation/createmlcomponents/meanabsolutepercentageerror(_:)): 예측값과 실제값 사이의 평균 절대 백분율 오차를 계산합니다.
- [meanSquaredError(_:)](https://developer.apple.com/documentation/createmlcomponents/meansquarederror(_:)): 예측값과 실제값 사이의 mean squared error를 계산합니다.
- [meanSquaredError(_:_:)](https://developer.apple.com/documentation/createmlcomponents/meansquarederror(_:_:)): 예측값과 실제값 사이의 mean squared error를 계산합니다.
:::

:::topic-grid
## Transformer 어댑터
- [TransformerToEstimatorAdaptor](https://developer.apple.com/documentation/createmlcomponents/transformertoestimatoradaptor): 미리 정의된 transformer를 항상 반환하는 estimator입니다.
- [TransformerToTemporalAdaptor](https://developer.apple.com/documentation/createmlcomponents/transformertotemporaladaptor): 일반 transformer를 temporal sequence의 각 값에 적용하는 temporal transformer입니다.
- [TransformerToUpdatableEstimatorAdaptor](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor): 미리 정의된 transformer를 항상 반환하는 업데이트 가능한 estimator입니다.
:::

:::topic-grid
## 업데이트 가능 어댑터
- [UpdatableEstimatorToTemporalAdaptor](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor): 업데이트 가능한 estimator를 감싼 업데이트 가능한 temporal estimator입니다.
- [UpdatableEstimatorToSupervisedAdaptor](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortosupervisedadaptor): 업데이트 가능한 estimator를 업데이트 가능한 감독형 estimator로 노출하는 adaptor입니다.
- [UpdatableSupervisedEstimatorToTemporalAdaptor](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimatortotemporaladaptor): 업데이트 가능한 감독형 estimator를 감싼 업데이트 가능한 감독형 temporal estimator입니다.
- [UpdatableTemporalEstimatorToSupervisedAdaptor](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimatortosupervisedadaptor): 업데이트 가능한 temporal estimator를 업데이트 가능한 감독형 temporal estimator로 노출하는 adaptor입니다.
:::

:::topic-grid
## Estimator 어댑터
- [EstimatorToSupervisedAdaptor](https://developer.apple.com/documentation/createmlcomponents/estimatortosupervisedadaptor): estimator를 감독형 estimator로 노출하는 adaptor입니다.
- [EstimatorToTemporalAdaptor](https://developer.apple.com/documentation/createmlcomponents/estimatortotemporaladaptor): estimator를 감싼 temporal estimator입니다.
- [SupervisedEstimatorToTemporalAdaptor](https://developer.apple.com/documentation/createmlcomponents/supervisedestimatortotemporaladaptor): 감독형 estimator를 감싼 감독형 temporal estimator입니다.
:::

:::topic-grid
## Tabular 어댑터
- [TabularEstimatorToSupervisedAdaptor](https://developer.apple.com/documentation/createmlcomponents/tabularestimatortosupervisedadaptor): tabular estimator를 tabular 감독형 estimator로 노출하는 adaptor입니다.
- [TabularTransformerToEstimatorAdaptor](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoestimatoradaptor): 미리 정의된 tabular transformer를 항상 반환하는 tabular estimator입니다.
- [TabularTransformerToUpdatableEstimatorAdaptor](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoupdatableestimatoradaptor): 미리 정의된 transformer를 항상 반환하는 업데이트 가능한 tabular estimator입니다.
- [UpdatableTabularEstimatorToSupervisedAdaptor](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimatortosupervisedadaptor): 업데이트 가능한 tabular estimator를 업데이트 가능한 감독형 tabular estimator로 노출하는 adaptor입니다.
:::

:::topic-grid
## Temporal 어댑터
- [TemporalAdaptor](https://developer.apple.com/documentation/createmlcomponents/temporaladaptor): 일반 transformer를 temporal sequence의 각 값에 적용하는 temporal transformer입니다.
- [TemporalTransformerToEstimatorAdaptor](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoestimatoradaptor): 미리 정의된 temporal transformer를 항상 반환하는 temporal estimator입니다.
- [TemporalEstimatorToSupervisedAdaptor](https://developer.apple.com/documentation/createmlcomponents/temporalestimatortosupervisedadaptor): temporal estimator를 감독형 temporal estimator로 노출하는 adaptor입니다.
- [TemporalTransformerToUpdatableEstimatorAdaptor](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoupdatableestimatoradaptor): 미리 정의된 temporal transformer를 항상 반환하는 temporal estimator입니다.
:::

:::topic-grid
## 전처리 조합
- [PreprocessingEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingestimator): 전처리 transformer와 estimator를 조합하는 estimator입니다.
- [PreprocessingTemporalEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingtemporalestimator): 전처리 transformer와 temporal estimator를 조합하는 temporal estimator입니다.
- [PreprocessingSupervisedEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedestimator): 전처리 transformer와 감독형 estimator를 조합하는 감독형 estimator입니다.
- [PreprocessingSupervisedTemporalEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtemporalestimator): 전처리 transformer와 감독형 temporal estimator를 조합하는 감독형 temporal estimator입니다.
- [PreprocessingUpdatableEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatableestimator): 전처리 transformer와 업데이트 가능한 estimator를 조합하는 업데이트 가능한 estimator입니다.
- [PreprocessingUpdatableTemporalEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletemporalestimator): 전처리 transformer와 업데이트 가능한 temporal estimator를 조합하는 업데이트 가능한 temporal estimator입니다.
- [PreprocessingUpdatableSupervisedEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedestimator): 전처리 transformer와 업데이트 가능한 감독형 estimator를 조합하는 업데이트 가능한 감독형 estimator입니다.
- [PreprocessingUpdatableSupervisedTemporalEstimator](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtemporalestimator): 전처리 transformer와 업데이트 가능한 감독형 temporal estimator를 조합하는 업데이트 가능한 감독형 temporal estimator입니다.
:::

:::topic-grid
## 조합
- [ComposedTransformer](https://developer.apple.com/documentation/createmlcomponents/composedtransformer): 두 transformer를 차례로 적용해 조합하는 transformer입니다.
- [ComposedTemporalTransformer](https://developer.apple.com/documentation/createmlcomponents/composedtemporaltransformer): 두 temporal transformer를 차례로 적용해 조합하는 temporal transformer입니다.
- [ComposedTabularTransformer](https://developer.apple.com/documentation/createmlcomponents/composedtabulartransformer): 두 tabular transformer를 차례로 적용해 조합하는 transformer입니다.
:::

:::topic-grid
## 오류
- [AudioPreprocessingError](https://developer.apple.com/documentation/createmlcomponents/audiopreprocessingerror): 오디오 전처리 오류입니다.
- [AudioReaderError](https://developer.apple.com/documentation/createmlcomponents/audioreadererror): 오디오 reader 오류입니다.
- [CompatibilityError](https://developer.apple.com/documentation/createmlcomponents/compatibilityerror): 호환성 오류입니다.
- [ConcatenationError](https://developer.apple.com/documentation/createmlcomponents/concatenationerror): 수치 값을 이어 붙일 때 발생하는 오류입니다.
- [DatasetError](https://developer.apple.com/documentation/createmlcomponents/dataseterror): 데이터 세트 처리 오류입니다.
- [EstimatorEncodingError](https://developer.apple.com/documentation/createmlcomponents/estimatorencodingerror): estimator encoding 오류입니다.
- [ModelCompatibilityError](https://developer.apple.com/documentation/createmlcomponents/modelcompatibilityerror): Core ML 모델 호환성과 관련된 오류입니다.
- [ModelUpdateError](https://developer.apple.com/documentation/createmlcomponents/modelupdateerror): 업데이트 가능한 모델 오류입니다.
- [OptimizationError](https://developer.apple.com/documentation/createmlcomponents/optimizationerror): 최적화 오류입니다.
- [PipelineDataError](https://developer.apple.com/documentation/createmlcomponents/pipelinedataerror): 파이프라인 데이터 affinity 문제와 관련된 오류입니다.
- [SerializationError](https://developer.apple.com/documentation/createmlcomponents/serializationerror): 직렬화 오류입니다.
- [TabularPipelineDataError](https://developer.apple.com/documentation/createmlcomponents/tabularpipelinedataerror): tabular 파이프라인 데이터 affinity 문제와 관련된 오류입니다.
- [VideoReaderError](https://developer.apple.com/documentation/createmlcomponents/videoreadererror): 비디오 loader 오류입니다.
:::
