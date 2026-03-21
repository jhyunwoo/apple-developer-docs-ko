---
route: /documentation/CoreImage
source_url: https://developer.apple.com/documentation/CoreImage
source_locale: en-US
section: docc
content_type: symbol
title: Core Image
original_title: Core Image
source_hash: 7e13e25195c4a0cd46faa24c5707ba85e11bf33fc3297d8e50e5e57b4c0138cc
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:38:45+00:00'
last_translated_at: '2026-03-13T23:38:45+09:00'
---

# Core Image

내장 필터 또는 사용자화 필터를 사용해 정지 이미지와 비디오 이미지를 처리합니다.

## 개요

Core Image는 정지 이미지와 비디오 이미지에 대해 고성능 처리를 제공하는 이미지 처리 및 분석 기술입니다. 다양한 내장 이미지 필터를 사용해 이미지를 처리하고, 필터를 연쇄적으로 연결해 복잡한 효과를 구축할 수 있습니다. 모든 내장 필터 목록은 [Filter Catalog](https://developer.apple.com/documentation/coreimage#Filter-Catalog)를 참고하십시오.

또한 사용자화 필터와 이미지 프로세서를 사용해 새로운 효과를 만들 수도 있습니다. 자세한 내용은 [Custom Filters](https://developer.apple.com/documentation/coreimage#Custom-Filters)를 참고하십시오.

:::topic-grid
## 핵심
- [내장 필터를 사용해 이미지 처리하기](https://developer.apple.com/documentation/coreimage/processing-an-image-using-built-in-filters): 세피아 톤, 하이라이트 강화, 크기 조정 같은 효과를 이미지에 적용합니다.
- [CIContext](https://developer.apple.com/documentation/coreimage/cicontext): Metal, OpenGL, OpenCL을 사용하는 Core Image 처리의 평가 컨텍스트를 제공하는 Core Image context 클래스입니다.
- [CIImage](https://developer.apple.com/documentation/coreimage/ciimage): Core Image 필터가 처리하거나 생성하는 이미지 표현입니다.
:::

:::topic-grid
## 필터
- [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter-swift.class): 하나 이상의 입력 이미지를 조작하거나 새 이미지 데이터를 생성해 이미지를 만들어 내는 이미지 프로세서입니다.
- [CIRAWFilter](https://developer.apple.com/documentation/coreimage/cirawfilter): 디지털 카메라나 스캐너의 RAW 이미지 센서 데이터를 조작해 이미지를 생성하는 필터 하위 클래스입니다.
- [CIColor](https://developer.apple.com/documentation/coreimage/cicolor): 색상 객체를 정의하는 Core Image 클래스입니다.
- [CIVector](https://developer.apple.com/documentation/coreimage/civector): 벡터 객체를 정의하는 Core Image 클래스입니다.
:::

:::topic-grid
## 필터 카탈로그
- [Blur Filters](https://developer.apple.com/documentation/coreimage/blur-filters): blur를 적용하고, motion 및 zoom 효과를 시뮬레이션하며, 노이즈를 줄이고, 이미지 영역을 침식하거나 팽창시킵니다.
- [Color Adjustment Filters](https://developer.apple.com/documentation/coreimage/color-adjustment-filters): 노출, hue, tint 조정을 포함한 색상 변환을 적용합니다.
- [Color Effect Filters](https://developer.apple.com/documentation/coreimage/color-effect-filters): 사진 효과, dithering, color map을 포함한 색상 효과를 적용합니다.
- [Composite Operations](https://developer.apple.com/documentation/coreimage/composite-operations): 다양한 blend mode와 compositing operator를 사용해 이미지를 합성합니다.
- [Convolution Filters](https://developer.apple.com/documentation/coreimage/convolution-filters): blur, sharpening, edge detection, translation, embossing 같은 효과를 생성합니다.
- [Distortion Filters](https://developer.apple.com/documentation/coreimage/distortion-filters): 이미지에 왜곡 효과를 적용합니다.
- [Generator Filters](https://developer.apple.com/documentation/coreimage/generator-filters): 바코드, 기하학적 이미지, 특수 효과 이미지를 생성합니다.
- [Geometry Adjustment Filters](https://developer.apple.com/documentation/coreimage/geometry-adjustment-filters): 2D와 3D에서 이미지를 이동, 확대/축소, 회전합니다.
- [Gradient Filters](https://developer.apple.com/documentation/coreimage/gradient-filters): 선형 및 방사형 gradient를 생성합니다.
- [Halftone Effect Filters](https://developer.apple.com/documentation/coreimage/halftone-effect-filters): 흑백 및 CMYK halftone screen을 시뮬레이션합니다.
- [Reduction Filters](https://developer.apple.com/documentation/coreimage/reduction-filters): 이미지에 대한 통계 정보를 생성합니다.
- [Sharpening Filters](https://developer.apple.com/documentation/coreimage/sharpening-filters): 이미지에 sharpening을 적용합니다.
- [Stylizing Filters](https://developer.apple.com/documentation/coreimage/stylizing-filters): pixelation, line overlay 등을 적용해 이미지를 스타일화한 버전으로 만듭니다.
- [Tile Effect Filters](https://developer.apple.com/documentation/coreimage/tile-effect-filters): 원본 이미지로부터 타일 형태 이미지를 생성합니다.
- [Transition Filters](https://developer.apple.com/documentation/coreimage/transition-filters): page curl, swipe 같은 효과를 사용해 두 이미지 사이를 전환합니다.
:::

:::topic-grid
## 필터 레시피
- [크로마 키 효과 적용하기](https://developer.apple.com/documentation/coreimage/applying-a-chroma-key-effect): 한 이미지의 특정 색상을 다른 이미지의 배경으로 바꿉니다.
- [이미지의 특정 영역에 선택적으로 초점 맞추기](https://developer.apple.com/documentation/coreimage/selectively-focusing-on-an-image): Gaussian blur와 gradient mask를 적용해 이미지의 일부에 초점을 맞춥니다.
- [이미지 전환 사용자화하기](https://developer.apple.com/documentation/coreimage/customizing-image-transitions): Core Image 필터를 사용해 이미지 간 전환을 창의적으로 구성합니다.
- [거친 아날로그 필름 질감 시뮬레이션하기](https://developer.apple.com/documentation/coreimage/simulating-scratchy-analog-film): 이미지 품질을 의도적으로 저하시켜 오래된 아날로그 필름처럼 보이게 만듭니다.
:::

:::topic-grid
## 사용자화 필터
- [사용자화 커널 작성하기](https://developer.apple.com/documentation/coreimage/writing-custom-kernels): Core Image Kernel Language 또는 Metal Shading Language로 사용자화 커널을 작성합니다.
- [CIKernel](https://developer.apple.com/documentation/coreimage/cikernel): 사용자화 Core Image 필터를 만드는 데 사용하는 GPU 기반 이미지 처리 루틴입니다.
- [CIColorKernel](https://developer.apple.com/documentation/coreimage/cicolorkernel): 이미지의 색상 정보만 처리하는 GPU 기반 이미지 처리 루틴으로, 사용자화 Core Image 필터를 만드는 데 사용합니다.
- [CIWarpKernel](https://developer.apple.com/documentation/coreimage/ciwarpkernel): 이미지의 기하 정보만 처리하는 GPU 기반 이미지 처리 루틴으로, 사용자화 Core Image 필터를 만드는 데 사용합니다.
- [CIBlendKernel](https://developer.apple.com/documentation/coreimage/ciblendkernel): 두 이미지를 혼합하는 데 최적화된 GPU 기반 이미지 처리 루틴입니다.
- [CISampler](https://developer.apple.com/documentation/coreimage/cisampler): 필터 커널이 처리할 pixel sample을 가져오는 객체입니다.
- [CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape): 필터의 경계 모양과 필터 연산 정의 영역을 설명합니다.
- [CIFormat](https://developer.apple.com/documentation/coreimage/ciformat): 이미지 입력, 출력, 처리에 사용하는 pixel 데이터 형식입니다.
:::

:::topic-grid
## 사용자화 이미지 프로세서
- [CIImageProcessorKernel](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel): Core Image 워크플로에 통합할 사용자화 이미지 프로세서를 만들 때 확장하는 추상 클래스입니다.
- [CIImageProcessorInput](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput): 사용자화 이미지 프로세서에서 사용할 이미지 데이터와 정보를 담는 컨테이너입니다.
- [CIImageProcessorOutput](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput): 사용자화 이미지 프로세서가 생성한 이미지 데이터와 정보를 기록하는 컨테이너입니다.
:::

:::topic-grid
## 사용자화 렌더 대상
- [Core Image Render Destination으로 애니메이션 생성하기](https://developer.apple.com/documentation/coreimage/generating-an-animation-with-a-core-image-render-destination): SwiftUI 앱에서 Core Image Render Destination을 사용해 필터가 적용된 이미지를 Metal view로 애니메이션합니다.
- [CIRenderDestination](https://developer.apple.com/documentation/coreimage/cirenderdestination): 렌더 작업의 대상 속성을 모두 구성하고 비동기 렌더 작업을 발행하기 위한 사양입니다.
- [CIRenderInfo](https://developer.apple.com/documentation/coreimage/cirenderinfo): 렌더 작업의 시간 정보, pass, 처리된 pixel 수를 캡슐화합니다.
- [CIRenderTask](https://developer.apple.com/documentation/coreimage/cirendertask): 단일 렌더 작업입니다.
- [CIRenderDestinationAlphaMode](https://developer.apple.com/documentation/coreimage/cirenderdestinationalphamode): alpha를 표현하는 여러 방법입니다.
:::

:::topic-grid
## 피드백 기반 처리
- [CIImageAccumulator](https://developer.apple.com/documentation/coreimage/ciimageaccumulator): 페인팅이나 유체 시뮬레이션 같은 작업을 위한 피드백 기반 이미지 처리를 관리하는 객체입니다.
:::

:::topic-grid
## 바코드 설명
- [CIBarcodeDescriptor](https://developer.apple.com/documentation/coreimage/cibarcodedescriptor): 기계 판독 코드의 속성을 나타내는 추상 기반 클래스입니다.
- [CIQRCodeDescriptor](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor): 정사각형 QR 코드 심볼을 나타내는 Core Image Barcode Descriptor의 구체적인 하위 클래스입니다.
- [CIAztecCodeDescriptor](https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor): Aztec 코드 심볼을 나타내는 Core Image Barcode Descriptor의 구체적인 하위 클래스입니다.
- [CIPDF417CodeDescriptor](https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor): PDF417 심볼을 나타내는 Core Image Barcode Descriptor의 구체적인 하위 클래스입니다.
- [CIDataMatrixCodeDescriptor](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor): Data Matrix 코드 심볼을 나타내는 Core Image Barcode Descriptor의 구체적인 하위 클래스입니다.
:::

:::topic-grid
## 이미지 특징 감지
- [CIDetector](https://developer.apple.com/documentation/coreimage/cidetector): 정지 이미지 또는 비디오에서 얼굴이나 바코드 같은 두드러진 특징을 식별하는 이미지 프로세서입니다.
- [CIFeature](https://developer.apple.com/documentation/coreimage/cifeature): 이미지에서 감지한 특징을 나타내는 객체의 추상 상위 클래스입니다.
- [CIFaceFeature](https://developer.apple.com/documentation/coreimage/cifacefeature): 정지 이미지 또는 비디오에서 감지한 얼굴에 대한 정보입니다.
- [CIRectangleFeature](https://developer.apple.com/documentation/coreimage/cirectanglefeature): 정지 이미지 또는 비디오에서 감지한 직사각형 영역에 대한 정보입니다.
- [CITextFeature](https://developer.apple.com/documentation/coreimage/citextfeature): 정지 이미지 또는 비디오에서 감지한 텍스트에 대한 정보입니다.
- [CIQRCodeFeature](https://developer.apple.com/documentation/coreimage/ciqrcodefeature): 정지 이미지 또는 비디오에서 감지한 QR 코드에 대한 정보입니다.
:::

:::topic-grid
## 이미지 유닛
- [CIPlugIn](https://developer.apple.com/documentation/coreimage/ciplugin): macOS에서 이미지 유닛을 로드하는 메커니즘입니다.
- [CIFilterGenerator](https://developer.apple.com/documentation/coreimage/cifiltergenerator): 개별 이미지 필터의 체인을 만들고 구성하는 객체입니다.
- [CIPlugInRegistration](https://developer.apple.com/documentation/coreimage/cipluginregistration): Core Image image unit을 로드하기 위한 인터페이스입니다.
- [CIFilterConstructor](https://developer.apple.com/documentation/coreimage/cifilterconstructor): 필터를 생성하는 객체를 위한 일반 인터페이스입니다.
:::

:::topic-grid
## 프로토콜
- [CIAreaBoundsRed](https://developer.apple.com/documentation/coreimage/ciareaboundsred)
- [CIMaximumScaleTransform](https://developer.apple.com/documentation/coreimage/cimaximumscaletransform)
- [CIToneMapHeadroom](https://developer.apple.com/documentation/coreimage/citonemapheadroom)
- [CIAreaAverageMaximumRed](https://developer.apple.com/documentation/coreimage/ciareaaveragemaximumred): Area Average and Maximum Red 필터용 프로토콜입니다.
- [CIBlurredRoundedRectangleGenerator](https://developer.apple.com/documentation/coreimage/ciblurredroundedrectanglegenerator): Blurred Rounded Rectangle Generator 필터용 프로토콜입니다.
- [CIDistanceGradientFromRedMask](https://developer.apple.com/documentation/coreimage/cidistancegradientfromredmask): Distance Gradient From Red Mask 필터용 프로토콜입니다.
- [CIRoundedQRCodeGenerator](https://developer.apple.com/documentation/coreimage/ciroundedqrcodegenerator): Rounded QR Code Generator 필터용 프로토콜입니다.
- [CISignedDistanceGradientFromRedMask](https://developer.apple.com/documentation/coreimage/cisigneddistancegradientfromredmask): Signed Distance Gradient From Red Mask 필터용 프로토콜입니다.
:::

:::topic-grid
## 참고 자료
- [Core Image Constants](https://developer.apple.com/documentation/coreimage/core-image-constants)
:::
