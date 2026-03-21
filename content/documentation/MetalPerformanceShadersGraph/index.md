---
route: /documentation/MetalPerformanceShadersGraph
source_url: https://developer.apple.com/documentation/MetalPerformanceShadersGraph
source_locale: en-US
section: docc
content_type: symbol
title: Metal Performance Shaders Graph
original_title: Metal Performance Shaders Graph
source_hash: c2a00740277ee8bc40b0f969f80b4ab8fc7afd45db0fab3d37f2fcf1e71489de
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:54:45+00:00'
last_translated_at: '2026-03-14T00:13:00+09:00'
---

# Metal Performance Shaders Graph

GPU, CPU, Neural Engine를 포함한 플랫폼의 다양한 계산 장치를 활용하는 compute graph를 빌드하고, 컴파일하고, 실행합니다.

## 개요

Metal Performance Shaders Graph는 서로 다른 하드웨어 계산 블록을 활용하여 Apple 플랫폼에서 고성능이면서 에너지 효율적인 연산을 제공합니다. 이 프레임워크를 사용하면 연산의 symbolic compute graph를 만들 수 있으며, 각 연산은 graph의 edge로 사용되는 tensor 집합을 출력할 수 있습니다. 이러한 tensor는 [MTLBuffer](https://developer.apple.com/documentation/Metal/MTLBuffer)나 [MTLTexture](https://developer.apple.com/documentation/Metal/MTLTexture) 같은 객체가 backing storage로 사용할 수 있는 다차원 데이터를 나타냅니다. Graph를 구성한 뒤에는 성능 최적화를 위해 이를 실행 가능한 형태로 컴파일하고, 이후 입력 데이터에 대해 실행할 수 있습니다. 또한 이 프레임워크는 실행 파일을 직렬화하고, 직렬화된 `.mpsgraphpackage`에서 실행 파일을 다시 불러오는 기능도 제공합니다.

:::topic-grid
## 핵심 사항
- [Adding custom functions to a shader graph](https://developer.apple.com/documentation/metalperformanceshadersgraph/adding-custom-functions-to-a-shader-graph): 함수를 프로그래밍 방식으로 구성해 GPU에서 사용자 정의 graph 함수를 실행합니다.
- [Training a neural network using MPSGraph](https://developer.apple.com/documentation/metalperformanceshadersgraph/training-a-neural-network-using-mps-graph): 간단한 신경망 숫자 분류기를 학습합니다.
- [Filtering images with MPSGraph FFT operations](https://developer.apple.com/documentation/metalperformanceshadersgraph/filtering-images-with-mpsgraph-fft-operations): convolution theorem을 사용해 MPSGraph 고속 푸리에 변환으로 이미지를 필터링합니다.
:::

:::topic-grid
## 클래스
- [MPSGraph](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph): 연산과 tensor로 이루어진 compute graph의 최적화된 표현입니다.
- [MPSGraphCompilationDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcompilationdescriptor): graph 컴파일에 필요한 모든 제어 수단을 담는 클래스입니다.
- [MPSGraphConvolution2DOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor): 2D convolution operator의 속성을 설명하는 클래스입니다.
- [MPSGraphConvolution3DOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor): 3D convolution operator의 속성을 설명하는 클래스입니다.
- [MPSGraphCreateSparseOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcreatesparseopdescriptor): sparse 생성 연산의 속성을 설명하는 클래스입니다.
- [MPSGraphDepthwiseConvolution2DOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdepthwiseconvolution2dopdescriptor): 2D depthwise convolution 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphDepthwiseConvolution3DOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdepthwiseconvolution3dopdescriptor): 3D depthwise convolution 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphDevice](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdevice): 계산 장치를 설명하는 클래스입니다.
- [MPSGraphExecutable](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable): compute graph executable의 컴파일된 표현입니다.
- [MPSGraphExecutableExecutionDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutableexecutiondescriptor): executable 실행의 동기화와 스케줄링을 위한 제어 수단을 담는 클래스입니다.
- [MPSGraphExecutableSerializationDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutableserializationdescriptor): executable을 직렬화하기 위한 제어 수단을 담는 클래스입니다.
- [MPSGraphExecutionDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutiondescriptor): graph 실행의 동기화와 스케줄링을 위한 제어 수단을 담는 클래스입니다.
- [MPSGraphFFTDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphfftdescriptor): FFT(fast Fourier transform) 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphGRUDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphgrudescriptor): GRU(gated recurrent unit) 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphImToColOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphimtocolopdescriptor): image-to-column 또는 column-to-image 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphLSTMDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphlstmdescriptor): LSTM(long short-term memory) 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphObject](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphobject): 모든 Metal Performance Shaders Graph 객체의 공통 기반 클래스입니다.
- [MPSGraphOperation](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoperation): compute 연산의 symbolic 표현입니다.
- [MPSGraphPooling2DOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling2dopdescriptor): 2D pooling 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphPooling4DOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor): 4D pooling 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphRandomOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomopdescriptor): random 연산을 설명하는 클래스입니다.
- [MPSGraphShapedType](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphshapedtype): shape와 data type을 가진 tensor 타입을 위한 shaped type 클래스입니다.
- [MPSGraphSingleGateRNNDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsinglegaternndescriptor): single gate RNN 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphStencilOpDescriptor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphstencilopdescriptor): stencil 연산의 매개변수를 정의하는 클래스입니다.
- [MPSGraphTensor](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensor): compute 데이터 타입의 symbolic 표현입니다.
- [MPSGraphTensorData](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata): compute 데이터 타입의 표현입니다.
- [MPSGraphType](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtype): tensor 타입을 위한 기본 타입 클래스입니다.
- [MPSGraphVariableOp](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphvariableop): variable의 매개변수를 정의하는 클래스입니다.
:::

:::topic-grid
## 구조체
- [MPSGraphReducedPrecisionFastMath](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphreducedprecisionfastmath): 더 빠른 수학 연산을 제공하기 위해 reduced precision 경로를 사용할 수 있지만, 항상 보장되지는 않습니다.
:::

:::topic-grid
## 타입 별칭
- [MPSGraphCompilationCompletionHandler](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcompilationcompletionhandler): 컴파일이 끝났을 때 호출되는 알림입니다.
- [MPSGraphCompletionHandler](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcompletionhandler): graph 실행이 끝났을 때 호출되는 알림입니다.
- [MPSGraphControlFlowDependencyBlock](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphcontrolflowdependencyblock): 이 block 안에서 정의된 모든 연산에 control dependency 연산이 적용되는 범위입니다.
- [MPSGraphExecutableCompletionHandler](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutablecompletionhandler): graph executable 실행이 끝났을 때 호출되는 알림입니다.
- [MPSGraphExecutableScheduledHandler](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutablescheduledhandler): graph executable 실행이 스케줄되었을 때 호출되는 알림입니다.
- [MPSGraphForLoopBodyBlock](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphforloopbodyblock): for loop 본문에 해당하는 block입니다.
- [MPSGraphIfThenElseBlock](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphifthenelseblock): if 또는 else 조건 아래에서 실행되는 연산 block입니다.
- [MPSGraphScheduledHandler](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphscheduledhandler): graph 실행이 스케줄되었을 때 호출되는 알림입니다.
- [MPSGraphWhileAfterBlock](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphwhileafterblock): 각 반복에서 조건이 평가된 뒤 실행되는 block입니다.
- [MPSGraphWhileBeforeBlock](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphwhilebeforeblock): 각 반복에서 조건이 평가되기 전에 실행되는 block입니다.
:::

:::topic-grid
## 열거형
- [MPSGraphDeploymentPlatform](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdeploymentplatform): graph에 사용할 수 있는 플랫폼 옵션입니다.
- [MPSGraphDeviceType](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdevicetype): 장치 유형입니다.
- [MPSGraphExecutionStage](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutionstage): 공유 event와 함께 사용할 수 있는 실행 이벤트입니다.
- [MPSGraphFFTScalingMode](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphfftscalingmode): Fourier transform 연산의 scaling 모드입니다.
- [MPSGraphLossReductionType](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphlossreductiontype): graph가 loss 연산에서 적용하는 reduction 유형입니다.
- [MPSGraphNonMaximumSuppressionCoordinateMode](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphnonmaximumsuppressioncoordinatemode): non-maximum suppression의 좌표 모드입니다.
- [MPSGraphOptimization](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoptimization): 더 많은 패스를 실행해 런타임 성능을 높이는 대신 컴파일 시간과 교환하는 최적화 수준입니다.
- [MPSGraphOptimizationProfile](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoptimizationprofile): graph compiler가 네트워크를 최적화할 때 휴리스틱으로 사용하는 최적화 프로파일입니다.
- [MPSGraphOptions](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoptions): graph에 사용할 수 있는 옵션입니다.
- [MPSGraphPaddingMode](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpaddingmode): tensor padding 모드입니다.
- [MPSGraphPaddingStyle](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpaddingstyle): tensor padding 스타일입니다.
- [MPSGraphPoolingReturnIndicesMode](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpoolingreturnindicesmode): max-pooling에서 반환되는 index의 flattening 모드입니다.
- [MPSGraphRNNActivation](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrnnactivation): RNN 연산의 activation 모드입니다.
- [MPSGraphRandomDistribution](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomdistribution): random 연산이 지원하는 분포입니다.
- [MPSGraphRandomNormalSamplingMethod](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphrandomnormalsamplingmethod): 정규 분포 값 생성에 사용하는 sampling 방법입니다.
- [MPSGraphReductionMode](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphreductionmode): reduction 모드입니다.
- [MPSGraphResizeMode](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphresizemode): resize에 사용하는 모드입니다.
- [MPSGraphResizeNearestRoundingMode](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphresizenearestroundingmode): nearest resize 모드를 사용할 때 적용하는 반올림 모드입니다.
- [MPSGraphScatterMode](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphscattermode): scatter 모드입니다.
- [MPSGraphSparseStorageType](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphsparsestoragetype): Metal Performance Shaders Graph 프레임워크의 sparse storage 옵션입니다.
- [MPSGraphTensorNamedDataLayout](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensornameddatalayout): tensor 레이아웃입니다.
:::
