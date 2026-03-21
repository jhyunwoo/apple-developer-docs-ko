---
route: /documentation/MetalPerformanceShaders
source_url: https://developer.apple.com/documentation/MetalPerformanceShaders
source_locale: en-US
section: docc
content_type: symbol
title: Metal Performance Shaders
original_title: Metal Performance Shaders
source_hash: 8f1680dd3342b5682ec85272aeb7c6a4caeccf86b16d186a417f7e2856b1d1ea
canonical_source: manual-translation
last_crawled_at: '2026-03-13T05:22:18+00:00'
last_translated_at: '2026-03-13T05:22:18+00:00'
---

# Metal Performance Shaders

각 Metal GPU 제품군의 고유한 특성에 맞게 세밀하게 조정된 커널로 그래픽 및 연산 성능을 최적화합니다.

## 개요

Metal Performance Shaders 프레임워크에는 여러분의 Metal 앱에 쉽고 효율적으로 통합되도록 설계된 고도로 최적화된 연산 및 그래픽 셰이더 모음이 포함되어 있습니다. 이러한 데이터 병렬 프리미티브는 각 GPU 제품군의 고유한 하드웨어 특성을 활용하도록 특별히 조정되어 최적의 성능을 보장합니다.

Metal Performance Shaders 프레임워크를 채택한 앱은 각 GPU 제품군마다 손수 작성한 셰이더를 만들고 유지하지 않고도 뛰어난 성능을 얻을 수 있습니다. Metal Performance Shaders는 앱의 기존 Metal 리소스([MTLCommandBuffer](https://developer.apple.com/documentation/Metal/MTLCommandBuffer), [MTLTexture](https://developer.apple.com/documentation/Metal/MTLTexture), [MTLBuffer](https://developer.apple.com/documentation/Metal/MTLBuffer) 객체 등) 및 셰이더와 함께 사용할 수 있습니다.

Metal Performance Shaders 프레임워크는 다음 기능을 지원합니다:

- 이미지에 고성능 필터를 적용하고, 통계 데이터와 히스토그램 데이터를 추출합니다.
- 머신 러닝 학습과 추론을 위한 신경망을 구현하고 실행합니다.
- 연립 방정식을 풀고, 행렬을 분해하고, 행렬과 벡터를 곱합니다.
- 고성능 광선-기하 교차 테스트로 레이 트레이싱을 가속합니다.

:::topic-grid
## 기초
- [The MPSKernel Class](https://developer.apple.com/documentation/metalperformanceshaders/the-mpskernel-class)
- [Tuning Hints](https://developer.apple.com/documentation/metalperformanceshaders/tuning-hints)
:::

:::topic-grid
## 기기 지원
- [MPSSupportsMTLDevice(_:)](https://developer.apple.com/documentation/metalperformanceshaders/mpssupportsmtldevice(_:)): Metal Performance Shaders 프레임워크가 특정 Metal 기기를 지원하는지 판단합니다.
:::

:::topic-grid
## 이미지 필터
- [Image Filters](https://developer.apple.com/documentation/metalperformanceshaders/image-filters): 이미지에 고성능 필터를 적용하고, 통계 데이터와 히스토그램 데이터를 추출합니다.
:::

:::topic-grid
## 신경망
- [Training a Neural Network with Metal Performance Shaders](https://developer.apple.com/documentation/metalperformanceshaders/training-a-neural-network-with-metal-performance-shaders): MPS 신경망 그래프를 사용해 간단한 숫자 분류기 신경망을 학습합니다.
- [MPSImage](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage): 합성곱 신경망에서 사용하기 위해 4개보다 많은 채널을 가질 수 있는 텍스처입니다.
- [MPSTemporaryImage](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage): 합성곱 신경망에서 사용되며 일시적인 데이터를 저장했다가 곧바로 버리는 텍스처입니다.
- [Objects that Simplify the Creation of Neural Networks](https://developer.apple.com/documentation/metalperformanceshaders/objects-that-simplify-the-creation-of-neural-networks): 필터, 이미지, 상태 노드의 네트워크를 사용해 신경망 생성을 단순화합니다.
- [Convolutional Neural Network Kernels](https://developer.apple.com/documentation/metalperformanceshaders/convolutional-neural-network-kernels): 레이어를 사용해 신경망을 구축합니다.
- [Recurrent Neural Networks](https://developer.apple.com/documentation/metalperformanceshaders/recurrent-neural-networks): 순환 신경망을 생성합니다.
:::

:::topic-grid
## 행렬과 벡터
- [Matrices and Vectors](https://developer.apple.com/documentation/metalperformanceshaders/matrices-and-vectors): 연립 방정식을 풀고, 행렬을 분해하고, 행렬과 벡터를 곱합니다.
:::

:::topic-grid
## 커널 기본 클래스
- [MPSKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel): Metal Performance Shaders 커널을 위한 표준 인터페이스입니다.
:::

:::topic-grid
## 키 지정 아카이버
- [NSKeyedArchiver](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver): 키를 기준으로 객체의 데이터를 아카이브에 저장하는 인코더입니다.
- [MPSKeyedUnarchiver](https://developer.apple.com/documentation/metalperformanceshaders/mpskeyedunarchiver): Metal Performance Shaders 커널 디코딩을 지원하는 keyed archiver입니다.
- [MPSDeviceProvider](https://developer.apple.com/documentation/metalperformanceshaders/mpsdeviceprovider): 아카이브 해제된 객체에 Metal 기기를 설정할 수 있게 하는 인터페이스입니다.
:::

:::topic-grid
## 레이 트레이싱
- [Accelerating ray tracing and motion blur using Metal](https://developer.apple.com/documentation/Metal/accelerating-ray-tracing-and-motion-blur-using-metal): GPU 기반 병렬 처리를 사용해 모션 블러가 있는 레이 트레이스 이미지를 생성합니다.
- [MPSRayIntersector](https://developer.apple.com/documentation/metalperformanceshaders/mpsrayintersector): 광선과 기하 구조 사이의 교차 테스트를 수행하는 커널입니다.
- [MPSAccelerationStructureGroup](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructuregroup): 가속 구조체 그룹입니다.
- [MPSInstanceAccelerationStructure](https://developer.apple.com/documentation/metalperformanceshaders/mpsinstanceaccelerationstructure): 다른 가속 구조체의 인스턴스 위에 구축된 가속 구조체입니다.
- [MPSTriangleAccelerationStructure](https://developer.apple.com/documentation/metalperformanceshaders/mpstriangleaccelerationstructure): 삼각형 위에 구축된 가속 구조체입니다.
- [MPSAccelerationStructure](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructure): 기하 구조 위에 구축되어 레이 트레이싱을 가속하는 데 사용하는 데이터 구조의 기본 클래스입니다.
:::

:::topic-grid
## 문서
- [MetalPerformanceShaders Constants](https://developer.apple.com/documentation/metalperformanceshaders/metalperformanceshaders-constants)
- [MetalPerformanceShaders Data Types](https://developer.apple.com/documentation/metalperformanceshaders/metalperformanceshaders-data-types)
- [MetalPerformanceShaders Enumerations](https://developer.apple.com/documentation/metalperformanceshaders/metalperformanceshaders-enumerations)
- [MetalPerformanceShaders Functions](https://developer.apple.com/documentation/metalperformanceshaders/metalperformanceshaders-functions)
- [MetalPerformanceShaders Structures](https://developer.apple.com/documentation/metalperformanceshaders/metalperformanceshaders-structures)
:::

:::topic-grid
## 클래스
- [MPSCNNConvolutionTransposeGradient](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontransposegradient)
- [MPSCNNConvolutionTransposeGradientNode](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontransposegradientnode)
- [MPSCNNConvolutionTransposeGradientState](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontransposegradientstate)
- [MPSCNNConvolutionTransposeGradientStateNode](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiontransposegradientstatenode)
- [MPSCNNFullyConnectedGradientNode](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnectedgradientnode)
- [MPSCNNGroupNormalization](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalization)
- [MPSCNNGroupNormalizationGradient](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalizationgradient)
- [MPSCNNGroupNormalizationGradientNode](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalizationgradientnode)
- [MPSCNNGroupNormalizationGradientState](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalizationgradientstate)
- [MPSCNNGroupNormalizationNode](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalizationnode)
- [MPSCNNMultiaryKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnmultiarykernel)
- [MPSCNNNeuronGeLUNode](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneurongelunode)
- [MPSCommandBuffer](https://developer.apple.com/documentation/metalperformanceshaders/mpscommandbuffer)
- [MPSImageCanny](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagecanny)
- [MPSImageEDLines](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedlines)
- [MPSImageNormalizedHistogram](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagenormalizedhistogram): 이미지의 정규화된 히스토그램을 계산하는 필터입니다.
- [MPSMatrixRandom](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandom)
- [MPSMatrixRandomDistributionDescriptor](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandomdistributiondescriptor)
- [MPSMatrixRandomMTGP32](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandommtgp32)
- [MPSMatrixRandomPhilox](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixrandomphilox)
- [MPSNDArray](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray)
- [MPSNDArrayAffineInt4Dequantize](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayaffineint4dequantize)
- [MPSNDArrayAffineQuantizationDescriptor](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayaffinequantizationdescriptor)
- [MPSNDArrayBinaryKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinarykernel)
- [MPSNDArrayBinaryPrimaryGradientKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinaryprimarygradientkernel)
- [MPSNDArrayBinarySecondaryGradientKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraybinarysecondarygradientkernel)
- [MPSNDArrayDescriptor](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraydescriptor)
- [MPSNDArrayGather](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraygather)
- [MPSNDArrayGatherGradient](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraygathergradient)
- [MPSNDArrayGatherGradientState](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraygathergradientstate)
- [MPSNDArrayGradientState](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraygradientstate)
- [MPSNDArrayIdentity](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayidentity)
- [MPSNDArrayLUTDequantize](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraylutdequantize)
- [MPSNDArrayLUTQuantizationDescriptor](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraylutquantizationdescriptor)
- [MPSNDArrayMatrixMultiplication](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymatrixmultiplication)
- [MPSNDArrayMultiaryBase](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarybase)
- [MPSNDArrayMultiaryGradientKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarygradientkernel)
- [MPSNDArrayMultiaryKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarykernel)
- [MPSNDArrayQuantizationDescriptor](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayquantizationdescriptor)
- [MPSNDArrayQuantizedMatrixMultiplication](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayquantizedmatrixmultiplication)
- [MPSNDArrayStridedSlice](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraystridedslice)
- [MPSNDArrayStridedSliceGradient](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraystridedslicegradient)
- [MPSNDArrayUnaryGradientKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarygradientkernel)
- [MPSNDArrayUnaryKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarykernel)
- [MPSNDArrayVectorLUTDequantize](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayvectorlutdequantize)
- [MPSNNCompare](https://developer.apple.com/documentation/metalperformanceshaders/mpsnncompare)
- [MPSNNComparisonNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnncomparisonnode)
- [MPSNNCropAndResizeBilinear](https://developer.apple.com/documentation/metalperformanceshaders/mpsnncropandresizebilinear): 크롭과 양선형 크기 조정을 수행하는 필터입니다.
- [MPSNNForwardLoss](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardloss)
- [MPSNNForwardLossNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnforwardlossnode)
- [MPSNNGramMatrixCalculation](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngrammatrixcalculation)
- [MPSNNGramMatrixCalculationGradient](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngrammatrixcalculationgradient)
- [MPSNNGramMatrixCalculationGradientNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngrammatrixcalculationgradientnode)
- [MPSNNGramMatrixCalculationNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngrammatrixcalculationnode)
- [MPSNNGridSample](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngridsample)
- [MPSNNInitialGradient](https://developer.apple.com/documentation/metalperformanceshaders/mpsnninitialgradient)
- [MPSNNInitialGradientNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnninitialgradientnode)
- [MPSNNLocalCorrelation](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlocalcorrelation)
- [MPSNNLossGradient](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlossgradient)
- [MPSNNLossGradientNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlossgradientnode)
- [MPSNNMultiaryGradientState](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnmultiarygradientstate)
- [MPSNNMultiaryGradientStateNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnmultiarygradientstatenode)
- [MPSNNPad](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpad)
- [MPSNNPadGradient](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpadgradient)
- [MPSNNPadGradientNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpadgradientnode)
- [MPSNNPadNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpadnode)
- [MPSNNReductionColumnMaxNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductioncolumnmaxnode)
- [MPSNNReductionColumnMeanNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductioncolumnmeannode)
- [MPSNNReductionColumnMinNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductioncolumnminnode)
- [MPSNNReductionColumnSumNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductioncolumnsumnode)
- [MPSNNReductionFeatureChannelsArgumentMaxNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionfeaturechannelsargumentmaxnode)
- [MPSNNReductionFeatureChannelsArgumentMinNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionfeaturechannelsargumentminnode)
- [MPSNNReductionFeatureChannelsMaxNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionfeaturechannelsmaxnode)
- [MPSNNReductionFeatureChannelsMeanNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionfeaturechannelsmeannode)
- [MPSNNReductionFeatureChannelsMinNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionfeaturechannelsminnode)
- [MPSNNReductionFeatureChannelsSumNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionfeaturechannelssumnode)
- [MPSNNReductionRowMaxNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionrowmaxnode)
- [MPSNNReductionRowMeanNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionrowmeannode)
- [MPSNNReductionRowMinNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionrowminnode)
- [MPSNNReductionRowSumNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionrowsumnode)
- [MPSNNReductionSpatialMeanGradientNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionspatialmeangradientnode)
- [MPSNNReductionSpatialMeanNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreductionspatialmeannode)
- [MPSNNReshapeGradient](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreshapegradient)
- [MPSNNReshapeGradientNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreshapegradientnode)
- [MPSNNReshapeNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreshapenode)
- [MPSNNResizeBilinear](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnresizebilinear): 양선형 크기 조정 필터입니다.
- [MPSNNUnaryReductionNode](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnunaryreductionnode)
- [MPSPolygonAccelerationStructure](https://developer.apple.com/documentation/metalperformanceshaders/mpspolygonaccelerationstructure)
- [MPSPolygonBuffer](https://developer.apple.com/documentation/metalperformanceshaders/mpspolygonbuffer)
- [MPSPredicate](https://developer.apple.com/documentation/metalperformanceshaders/mpspredicate)
- [MPSQuadrilateralAccelerationStructure](https://developer.apple.com/documentation/metalperformanceshaders/mpsquadrilateralaccelerationstructure)
- [MPSSVGF](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgf)
- [MPSSVGFDefaultTextureAllocator](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgfdefaulttextureallocator)
- [MPSSVGFDenoiser](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgfdenoiser)
- [MPSStateResourceList](https://developer.apple.com/documentation/metalperformanceshaders/mpsstateresourcelist): Metal Performance Shaders 상태 컨테이너를 위한 리소스를 정의하는 객체용 인터페이스입니다.
- [MPSTemporalAA](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporalaa)
- [MPSTemporaryNDArray](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryndarray)
:::

:::topic-grid
## 프로토콜
- [MPSCNNGroupNormalizationDataSource](https://developer.apple.com/documentation/metalperformanceshaders/mpscnngroupnormalizationdatasource)
- [MPSHeapProvider](https://developer.apple.com/documentation/metalperformanceshaders/mpsheapprovider)
- [MPSNDArrayAllocator](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayallocator)
- [MPSNNGramMatrixCallback](https://developer.apple.com/documentation/metalperformanceshaders/mpsnngrammatrixcallback)
- [MPSNNLossCallback](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnlosscallback)
- [MPSSVGFTextureAllocator](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgftextureallocator)
:::

:::topic-grid
## 구조체
- [MPSOrigin](https://developer.apple.com/documentation/metalperformanceshaders/mpsorigin): 소스 원점으로 사용하는 이미지 내 위치입니다.
- [MPSSize](https://developer.apple.com/documentation/metalperformanceshaders/mpssize): 이미지 안 영역의 크기입니다.
:::

:::topic-grid
## 변수
- [MPSCustomKernelIndexDestIndex](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelindexdestindex)
- [MPSCustomKernelIndexSrc0Index](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelindexsrc0index)
- [MPSCustomKernelIndexSrc1Index](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelindexsrc1index)
- [MPSCustomKernelIndexSrc2Index](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelindexsrc2index)
- [MPSCustomKernelIndexSrc3Index](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelindexsrc3index)
- [MPSCustomKernelIndexSrc4Index](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelindexsrc4index)
- [MPSCustomKernelIndexUserDataIndex](https://developer.apple.com/documentation/metalperformanceshaders/mpscustomkernelindexuserdataindex)
- [MPSDeviceCapsLast](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicecapslast)
- [MPSDeviceCapsNull](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicecapsnull)
- [MPSDeviceIsAppleDevice](https://developer.apple.com/documentation/metalperformanceshaders/mpsdeviceisappledevice)
- [MPSDeviceSupportsBFloat16Arithmetic](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportsbfloat16arithmetic)
- [MPSDeviceSupportsFloat16BicubicFiltering](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportsfloat16bicubicfiltering)
- [MPSDeviceSupportsFloat32Filtering](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportsfloat32filtering)
- [MPSDeviceSupportsNorm16BicubicFiltering](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportsnorm16bicubicfiltering)
- [MPSDeviceSupportsQuadShuffle](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportsquadshuffle)
- [MPSDeviceSupportsReadWriteTextures](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportsreadwritetextures)
- [MPSDeviceSupportsReadableArrayOfTextures](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportsreadablearrayoftextures)
- [MPSDeviceSupportsSimdReduction](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportssimdreduction)
- [MPSDeviceSupportsSimdShuffle](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportssimdshuffle)
- [MPSDeviceSupportsSimdShuffleAndFill](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportssimdshuffleandfill)
- [MPSDeviceSupportsSimdgroupBarrier](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportssimdgroupbarrier)
- [MPSDeviceSupportsWritableArrayOfTextures](https://developer.apple.com/documentation/metalperformanceshaders/mpsdevicesupportswritablearrayoftextures)
- [MPSImageType2d](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype2d)
- [MPSImageType2d_array](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype2d_array)
- [MPSImageType2d_array_noAlpha](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype2d_array_noalpha)
- [MPSImageType2d_noAlpha](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype2d_noalpha)
- [MPSImageTypeArray2d](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetypearray2d)
- [MPSImageTypeArray2d_array](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetypearray2d_array)
- [MPSImageTypeArray2d_array_noAlpha](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetypearray2d_array_noalpha)
- [MPSImageTypeArray2d_noAlpha](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetypearray2d_noalpha)
- [MPSImageType_ArrayMask](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_arraymask)
- [MPSImageType_BatchMask](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_batchmask)
- [MPSImageType_bitCount](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_bitcount)
- [MPSImageType_mask](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_mask)
- [MPSImageType_noAlpha](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_noalpha)
- [MPSImageType_texelFormatBFloat16](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_texelformatbfloat16)
- [MPSImageType_texelFormatFloat16](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_texelformatfloat16)
- [MPSImageType_texelFormatMask](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_texelformatmask)
- [MPSImageType_texelFormatShift](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_texelformatshift)
- [MPSImageType_texelFormatStandard](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_texelformatstandard)
- [MPSImageType_texelFormatUnorm8](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_texelformatunorm8)
- [MPSImageType_typeMask](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetype_typemask)
:::

:::topic-grid
## 타입 별칭
- [MPSPackedFloat3](https://developer.apple.com/documentation/metalperformanceshaders/mpspackedfloat3-swift.typealias): 패킹된 3요소 벡터입니다.
:::
