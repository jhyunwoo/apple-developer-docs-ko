---
route: /documentation/CoreML
source_url: https://developer.apple.com/documentation/CoreML
source_locale: en-US
section: docc
content_type: symbol
title: Core ML
original_title: Core ML
source_hash: 271125d7676ced58dc8a0c0fdf40153d13d5debc826d1b32809d1ef1c9903d82
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:47:39+00:00'
last_translated_at: '2026-03-13T15:35:00+09:00'
---

# Core ML

기계 학습 모델을 앱에 통합합니다.

## 개요

[Core ML](https://developer.apple.com/documentation/coreml)을 사용해 기계 학습 모델을 앱에 통합합니다. [Core ML](https://developer.apple.com/documentation/coreml)은 모든 모델에 대해 통합된 표현을 제공합니다. 앱은 [Core ML](https://developer.apple.com/documentation/coreml) API와 사용자 데이터를 사용해 예측을 수행하고, 사용자의 기기에서 직접 모델을 학습하거나 미세 조정할 수 있습니다.

![왼쪽에서 오른쪽으로 이어지는 흐름도입니다. 왼쪽에는 Core ML 모델 파일 아이콘이 있고, 가운데에는 Core ML 프레임워크 아이콘, 오른쪽에는 “your app”이라고 표시된 일반적인 앱 아이콘이 있습니다.](https://developer.apple.com)

모델은 기계 학습 알고리즘을 학습 데이터 집합에 적용한 결과입니다. 모델은 새로운 입력 데이터를 바탕으로 예측을 수행하는 데 사용합니다. 모델은 코드로 작성하기 어렵거나 비현실적인 매우 다양한 작업을 수행할 수 있습니다. 예를 들어 사진을 분류하거나, 사진의 픽셀로부터 특정 객체를 직접 감지하도록 모델을 학습시킬 수 있습니다.

모델은 Xcode에 포함된 [Create ML app](https://developer.apple.com/machine-learning/create-ml/)으로 빌드하고 학습합니다. [Create ML](https://developer.apple.com/documentation/CreateML)로 학습한 모델은 [Core ML](https://developer.apple.com/documentation/coreml) 모델 포맷으로 생성되며 앱에서 바로 사용할 수 있습니다. 또는 다양한 다른 기계 학습 라이브러리를 사용한 뒤 [Core ML Tools](https://coremltools.readme.io)를 이용해 모델을 [Core ML](https://developer.apple.com/documentation/coreml) 포맷으로 변환할 수 있습니다. 모델이 사용자의 기기에 올라간 뒤에는 [Core ML](https://developer.apple.com/documentation/coreml)을 사용해 해당 사용자의 데이터로 기기 내에서 모델을 다시 학습하거나 미세 조정할 수 있습니다.

[Core ML](https://developer.apple.com/documentation/coreml)은 CPU, GPU, Neural Engine을 활용하면서 메모리 사용량과 전력 소비를 최소화해 온디바이스 성능을 최적화합니다. 모델을 전적으로 사용자의 기기에서 실행하면 네트워크 연결이 필요 없으므로, 사용자 데이터의 프라이버시를 유지하는 데 도움이 되고 앱의 반응성도 좋아집니다.

이 프레임워크는 도메인 특화 프레임워크와 기능의 기반이 됩니다. 이미지 분석을 위한 [Vision](https://developer.apple.com/documentation/Vision), 텍스트 처리를 위한 [Natural Language](https://developer.apple.com/documentation/NaturalLanguage), 오디오를 텍스트로 변환하는 [Speech](https://developer.apple.com/documentation/Speech), 오디오 속 소리를 식별하는 [Sound Analysis](https://developer.apple.com/documentation/SoundAnalysis)를 지원합니다. [Core ML](https://developer.apple.com/documentation/coreml) 자체도 [Accelerate](https://developer.apple.com/documentation/Accelerate)와 [BNNS](https://developer.apple.com/documentation/Accelerate/bnns-library), 그리고 [Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders) 같은 저수준 프리미티브 위에 구축됩니다.

![기계 학습 스택의 블록 다이어그램입니다. 최상단 계층은 전체 폭을 차지하는 “Your app” 단일 블록입니다. 두 번째 계층에는 “Vision”, “Natural Language”, “Speech”, “Sound Analysis”라는 네 개의 블록이 있습니다. 세 번째 계층은 전체 폭을 차지하는 “Core ML”입니다. 네 번째이자 마지막 계층에는 “Accelerate and BNNS”, “Metal Performance Shaders” 두 개의 블록이 있습니다.](https://developer.apple.com)

:::topic-grid
## Core ML 모델
- [Getting a Core ML Model](https://developer.apple.com/documentation/coreml/getting-a-core-ml-model): 앱에서 사용할 Core ML 모델을 확보합니다.
- [Updating a Model File to a Model Package](https://developer.apple.com/documentation/coreml/updating-a-model-file-to-a-model-package): Core ML 모델 파일을 Xcode에서 모델 패키지로 변환합니다.
- [Integrating a Core ML Model into Your App](https://developer.apple.com/documentation/coreml/integrating-a-core-ml-model-into-your-app): 간단한 모델을 앱에 추가하고, 모델에 입력 데이터를 전달한 뒤 예측 결과를 처리합니다.
- [MLModel](https://developer.apple.com/documentation/coreml/mlmodel): 기계 학습 모델의 모든 세부 사항을 캡슐화한 객체입니다.
- [Model Customization](https://developer.apple.com/documentation/coreml/model-customization): 새 레이어를 추가해 모델을 확장하고 수정합니다.
- [Model Personalization](https://developer.apple.com/documentation/coreml/model-personalization): 새 데이터에 적응하도록 모델을 업데이트합니다.
:::

:::topic-grid
## 모델 입력과 출력
- [Making Predictions with a Sequence of Inputs](https://developer.apple.com/documentation/coreml/making-predictions-with-a-sequence-of-inputs): 입력 시퀀스를 처리하는 순환 신경망 모델을 통합합니다.
- [MLFeatureValue](https://developer.apple.com/documentation/coreml/mlfeaturevalue): 기본 값과 해당 값의 타입을 감싸는 범용 래퍼입니다.
- [MLSendableFeatureValue](https://developer.apple.com/documentation/coreml/mlsendablefeaturevalue): sendable 특성 값을 나타냅니다.
- [MLFeatureProvider](https://developer.apple.com/documentation/coreml/mlfeatureprovider): 모델 입력 또는 출력에 대한 값 모음을 표현하는 인터페이스입니다.
- [MLDictionaryFeatureProvider](https://developer.apple.com/documentation/coreml/mldictionaryfeatureprovider): 주어진 데이터 딕셔너리를 위한 편의 래퍼입니다.
- [MLBatchProvider](https://developer.apple.com/documentation/coreml/mlbatchprovider): feature provider 모음을 표현하는 인터페이스입니다.
- [MLArrayBatchProvider](https://developer.apple.com/documentation/coreml/mlarraybatchprovider): feature provider 배치를 위한 편의 래퍼입니다.
- [MLModelAsset](https://developer.apple.com/documentation/coreml/mlmodelasset): 컴파일된 Core ML 모델 자산을 추상화한 객체입니다.
:::

:::topic-grid
## 앱 통합
- [Downloading and Compiling a Model on the User’s Device](https://developer.apple.com/documentation/coreml/downloading-and-compiling-a-model-on-the-user-s-device): 런타임에 사용자의 기기에 Core ML 모델을 동적으로 설치합니다.
- [Model Integration Samples](https://developer.apple.com/documentation/coreml/model-integration-samples): 표 형식 데이터, 이미지, 텍스트 분류 모델을 앱에 통합합니다.
:::

:::topic-grid
## 모델 암호화
- [Generating a Model Encryption Key](https://developer.apple.com/documentation/coreml/generating-a-model-encryption-key): 컴파일된 모델 또는 모델 아카이브를 암호화하는 모델 암호화 키를 생성합니다.
- [Encrypting a Model in Your App](https://developer.apple.com/documentation/coreml/encrypting-a-model-in-your-app): 컴파일러 플래그를 추가해 앱의 내장 모델을 컴파일 시점에 암호화합니다.
:::

:::topic-grid
## 계산 기기
- [MLComputeDevice](https://developer.apple.com/documentation/coreml/mlcomputedevice): 프레임워크 연산을 위한 계산 기기입니다.
- [MLCPUComputeDevice](https://developer.apple.com/documentation/coreml/mlcpucomputedevice): CPU 계산 기기를 표현하는 객체입니다.
- [MLGPUComputeDevice](https://developer.apple.com/documentation/coreml/mlgpucomputedevice): GPU 계산 기기를 표현하는 객체입니다.
- [MLNeuralEngineComputeDevice](https://developer.apple.com/documentation/coreml/mlneuralenginecomputedevice): Neural Engine 계산 기기를 표현하는 객체입니다.
- [MLComputeDeviceProtocol](https://developer.apple.com/documentation/coreml/mlcomputedeviceprotocol): 계산 기기 타입을 표현하는 인터페이스입니다.
:::

:::topic-grid
## 계산 계획
- [MLComputePlan](https://developer.apple.com/documentation/coreml/mlcomputeplan-1w21n): 모델의 계산 계획을 나타내는 클래스입니다.
- [MLModelStructure](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum): 모델의 구조를 나타내는 열거형입니다.
- [MLComputePolicy](https://developer.apple.com/documentation/coreml/mlcomputepolicy): ML 워크로드를 어떤 계산 기기 또는 계산 기기들에서 실행할지 결정하는 계산 정책입니다.
- [withMLTensorComputePolicy(_:_:)](https://developer.apple.com/documentation/coreml/withmltensorcomputepolicy(_:_:)-8stx9): 지정한 계산 정책을 사용해 task-local 컨텍스트 안에서 주어진 클로저를 호출하여 tensor 연산이 어떤 계산 기기에서 실행될지에 영향을 줍니다.
- [withMLTensorComputePolicy(_:_:)](https://developer.apple.com/documentation/coreml/withmltensorcomputepolicy(_:_:)-6z33x): 지정한 계산 정책을 사용해 task-local 컨텍스트 안에서 주어진 클로저를 호출하여 tensor 연산이 어떤 계산 기기에서 실행될지에 영향을 줍니다.
:::

:::topic-grid
## 모델 상태
- [MLState](https://developer.apple.com/documentation/coreml/mlstate): 상태 버퍼에 대한 핸들입니다.
- [MLStateConstraint](https://developer.apple.com/documentation/coreml/mlstateconstraint): 상태 feature value의 제약 조건입니다.
:::

:::topic-grid
## 모델 텐서
- [MLTensor](https://developer.apple.com/documentation/coreml/mltensor): ML 사용 사례에 맞게 설계된 숫자형 또는 Boolean 스칼라의 다차원 배열로, ML 계산 기기를 사용해 변환과 수학 연산을 효율적으로 수행하는 메서드를 포함합니다.
- [MLTensorScalar](https://developer.apple.com/documentation/coreml/mltensorscalar): 프레임워크가 지원하는 tensor scalar 타입을 나타내는 타입입니다. 이 타입을 직접 사용하지 마십시오.
- [MLTensorRangeExpression](https://developer.apple.com/documentation/coreml/mltensorrangeexpression): tensor의 한 차원을 슬라이스하는 데 사용할 수 있는 타입입니다. 이 타입을 직접 사용하지 마십시오.
- [pointwiseMin(_:_:)](https://developer.apple.com/documentation/coreml/pointwisemin(_:_:)): 두 tensor의 요소별 최소값을 계산합니다.
- [pointwiseMax(_:_:)](https://developer.apple.com/documentation/coreml/pointwisemax(_:_:)): 두 tensor 사이의 요소별 최소값을 계산합니다.
- [withMLTensorComputePolicy(_:_:)](https://developer.apple.com/documentation/coreml/withmltensorcomputepolicy(_:_:)): 지정한 계산 정책을 사용해 task-local 컨텍스트 안에서 주어진 클로저를 호출하여 tensor 연산이 어떤 계산 기기에서 실행될지에 영향을 줍니다.
:::

:::topic-grid
## 모델 구조
- [MLModelStructure](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum): 모델의 구조를 나타내는 열거형입니다.
:::

:::topic-grid
## 모델 오류
- [MLModelError](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct): Core ML 모델 오류에 대한 정보입니다.
- [MLModelError.Code](https://developer.apple.com/documentation/coreml/mlmodelerror-swift.struct/code): Core ML 모델 오류에 대한 정보입니다.
- [MLModelErrorDomain](https://developer.apple.com/documentation/coreml/mlmodelerrordomain): Core ML 오류의 도메인입니다.
:::

:::topic-grid
## 모델 배포
- [MLModelCollection](https://developer.apple.com/documentation/coreml/mlmodelcollection): 모델 배포에서 가져온 Core ML 모델 집합입니다.
:::

:::topic-grid
## 레퍼런스
- [CoreML Enumerations](https://developer.apple.com/documentation/coreml/coreml-enumerations)
:::
