---
route: /documentation/CoreVideo
source_url: https://developer.apple.com/documentation/CoreVideo
source_locale: en-US
section: docc
content_type: symbol
title: Core Video
original_title: Core Video
source_hash: 4e20f34c1c1b70d12580adfb5df7985e43c900181c6b0f99182c05599169be0c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:14:57+00:00'
last_translated_at: '2026-03-13T16:55:00+09:00'
---

# Core Video

파이프라인 기반 API와 Metal 및 OpenGL 지원을 사용해 개별 프레임 조작을 포함한 디지털 비디오를 처리합니다.

## 개요

Core Video는 디지털 비디오를 위한 파이프라인 모델을 제공합니다. 과정을 개별 단계로 분할하여 비디오 작업을 단순화합니다. 덕분에 개발자는 데이터 타입 간 변환이나 디스플레이 동기화 문제를 걱정하지 않고 개별 프레임에 더 쉽게 접근하고 이를 조작할 수 있습니다. 개별 비디오 프레임을 조작할 필요가 없는 앱은 Core Video를 직접 사용할 필요가 없습니다.

:::topic-grid
## 데이터 처리
- [CVBuffer](https://developer.apple.com/documentation/corevideo/cvbuffer-nfm): 데이터 버퍼와 상호 작용하는 방법을 정의하는 추상 기본 클래스입니다.
- [CVImageBuffer](https://developer.apple.com/documentation/corevideo/cvimagebuffer-q40): 다양한 유형의 이미지 데이터를 관리하기 위한 인터페이스입니다.
- [CVPixelBuffer](https://developer.apple.com/documentation/corevideo/cvpixelbuffer-q2e): 메인 메모리에 픽셀을 보관하는 이미지 버퍼입니다.
- [CVPixelBufferPool](https://developer.apple.com/documentation/corevideo/cvpixelbufferpool-77o): 재사용 가능한 pixel buffer 객체 집합을 관리하는 유틸리티 객체입니다.
- [CVPixelFormatDescription](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription-42p): 사용자 정의 픽셀 포맷을 정의하기 위한 함수와 타입을 제공하는 API입니다.
:::

:::topic-grid
## 시간 관리
- [CVTime](https://developer.apple.com/documentation/corevideo/cvtime-q1e): Core Video 시간 값을 저장하는 데 사용하는 구조체입니다.
- [CVDisplayLink](https://developer.apple.com/documentation/corevideo/cvdisplaylink-k0k): 특정 디스플레이가 각 프레임을 필요로 할 시점을 앱에 알려 주는 고우선순위 스레드입니다.
:::

:::topic-grid
## Metal
- [CVMetalTextureCache](https://developer.apple.com/documentation/corevideo/cvmetaltexturecache-q3j): Metal texture 객체를 생성하고 관리하는 데 사용하는 캐시입니다.
- [CVMetalTexture](https://developer.apple.com/documentation/corevideo/cvmetaltexture-q3g): Metal 프레임워크에서 사용할 소스 이미지 데이터를 제공하는 texture 기반 이미지 버퍼입니다.
:::

:::topic-grid
## OpenGL
- [CVOpenGLTextureCache](https://developer.apple.com/documentation/corevideo/cvopengltexturecache-780): OpenGL texture 객체를 생성하고 관리하는 데 사용하는 캐시입니다.
- [CVOpenGLTexture](https://developer.apple.com/documentation/corevideo/cvopengltexture-782): OpenGL에 소스 이미지 데이터를 제공하는 texture 기반 이미지 버퍼입니다.
- [CVOpenGLBuffer](https://developer.apple.com/documentation/corevideo/cvopenglbuffer-77s): 비디오 메모리에 이미지 데이터를 저장하는 데 사용하는 이미지 버퍼입니다.
- [CVOpenGLBufferPool](https://developer.apple.com/documentation/corevideo/cvopenglbufferpool-77j): 재사용 가능한 OpenGL buffer 객체 집합을 관리하는 유틸리티 객체입니다.
:::

:::topic-grid
## OpenGL ES
- [CVOpenGLESTextureCache](https://developer.apple.com/documentation/corevideo/cvopenglestexturecache-q2r): OpenGL ES texture 객체를 생성하고 관리하는 데 사용하는 캐시입니다.
- [CVOpenGLESTexture](https://developer.apple.com/documentation/corevideo/cvopenglestexture-q2s): OpenGL ES에 소스 이미지 데이터를 제공하는 texture 기반 이미지 버퍼입니다.
:::

:::topic-grid
## Core Video 오류 상수
- [Result Codes](https://developer.apple.com/documentation/corevideo/result-codes): Core Video 작업이 생성하는 결과 코드를 설명합니다.
- [Data Types](https://developer.apple.com/documentation/corevideo/data-types): Core Video 프레임워크에서 사용하는 공통 데이터 타입입니다.
:::

:::topic-grid
## 레퍼런스
- [Core Video Enumerations](https://developer.apple.com/documentation/corevideo/core-video-enumerations)
- [Core Video Constants](https://developer.apple.com/documentation/corevideo/core-video-constants)
- [Core Video Functions](https://developer.apple.com/documentation/corevideo/core-video-functions)
:::

:::topic-grid
## 클래스
- [CVMetalBufferCache](https://developer.apple.com/documentation/corevideo/cvmetalbuffercache)
- [CVReadOnlyPixelBuffer](https://developer.apple.com/documentation/corevideo/cvreadonlypixelbuffer): pixel buffer가 보유한 픽셀 데이터에 대한 불변 뷰를 제공합니다.
:::

:::topic-grid
## 프로토콜
- [CVBufferRepresentable](https://developer.apple.com/documentation/corevideo/cvbufferrepresentable): CoreVideo 프레임워크의 타입들이 구현하도록 의도된 sealed protocol입니다. CVBuffer 타입 값을 감싸는 Swift 타입을 돕습니다.
- [CVImageBufferRepresentable](https://developer.apple.com/documentation/corevideo/cvimagebufferrepresentable): CoreVideo 프레임워크의 타입들이 구현하도록 의도된 sealed protocol입니다. CVImageBuffer 타입 값을 감싸는 Swift 타입을 돕습니다.
- [CVPixelBufferRepresentable](https://developer.apple.com/documentation/corevideo/cvpixelbufferrepresentable): CoreVideo 프레임워크의 타입들이 구현하도록 의도된 sealed protocol입니다. CVPixelBuffer 타입 값을 감싸는 Swift 타입을 돕습니다.
:::

:::topic-grid
## 구조체
- [CVError](https://developer.apple.com/documentation/corevideo/cverror): 값을 Swift `Error` 값으로 제시하기 위해 감쌉니다. 이 타입은 CoreVideo 프레임워크에서 던져지는 모든 오류에 사용되며, 모든 값은 정적 상수로 제공됩니다.
- [CVImageSize](https://developer.apple.com/documentation/corevideo/cvimagesize): 픽셀 수로 표현한 이미지 버퍼의 크기입니다.
- [CVMutablePixelBuffer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer): 픽셀 데이터와 attachment에 대한 읽기-쓰기를 제공합니다.
- [CVPixelBufferAttributes](https://developer.apple.com/documentation/corevideo/cvpixelbufferattributes): pixel buffer 생성 속성의 부분 집합입니다. 클라이언트에 pixel buffer의 부분 요구 사항을 전달하는 데 유용하며, 모든 프로퍼티를 optional로 만듭니다.
- [CVPixelBufferCreationAttributes](https://developer.apple.com/documentation/corevideo/cvpixelbuffercreationattributes): pixel buffer를 생성하는 데 필요한 속성입니다.
- [CVPixelBufferPadding](https://developer.apple.com/documentation/corevideo/cvpixelbufferpadding): `CVPixelBuffer` 주변의 padding 픽셀입니다.
- [CVPixelBufferPlaneProperties](https://developer.apple.com/documentation/corevideo/cvpixelbufferplaneproperties): pixel buffer 안 개별 plane의 속성입니다.
- [CVPixelFormatType](https://developer.apple.com/documentation/corevideo/cvpixelformattype): 픽셀 포맷 타입의 식별자입니다.
:::

:::topic-grid
## 변수
- [kCVImageBufferDisplayMaskRectangleKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectanglekey): 이미지 안에서 직사각형 표시 영역을 지정합니다.
- [kCVImageBufferDisplayMaskRectangleStereoLeftKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectanglestereoleftkey): 같은 키 집합을 사용해 스테레오 이미지의 왼쪽 눈 뷰 안 직사각형 표시 영역을 지정합니다.
- [kCVImageBufferDisplayMaskRectangleStereoRightKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferdisplaymaskrectanglestereorightkey): 같은 키 집합을 사용해 스테레오 이미지의 오른쪽 눈 뷰 안 직사각형 표시 영역을 지정합니다.
- [kCVImageBufferLogTransferFunction_AppleLog2](https://developer.apple.com/documentation/corevideo/kcvimagebufferlogtransferfunction_applelog2)
- [kCVImageBufferPostDecodeProcessingFrameMetadataKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferpostdecodeprocessingframemetadatakey)
- [kCVImageBufferPostDecodeProcessingSequenceMetadataKey](https://developer.apple.com/documentation/corevideo/kcvimagebufferpostdecodeprocessingsequencemetadatakey)
- [kCVImageBufferSceneIlluminationKey](https://developer.apple.com/documentation/corevideo/kcvimagebuffersceneilluminationkey)
- [kCVMetalBufferCacheMaximumBufferAgeKey](https://developer.apple.com/documentation/corevideo/kcvmetalbuffercachemaximumbufferagekey)
- [kCVPixelBufferIOSurfacePurgeableKey](https://developer.apple.com/documentation/corevideo/kcvpixelbufferiosurfacepurgeablekey)
- [kCVPixelFormatBitsPerComponent](https://developer.apple.com/documentation/corevideo/kcvpixelformatbitspercomponent)
- [kCVPixelFormatType_30RGBLE_8A_BiPlanar](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_30rgble_8a_biplanar)
- [kCVPixelFormatType_30RGB_r210](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_30rgb_r210)
- [kCVPixelFormatType_96VersatileBayerPacked12](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_96versatilebayerpacked12)
- [kCVPixelFormatType_Lossless_30RGBLEPackedWideGamut](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_lossless_30rgblepackedwidegamut)
- [kCVPixelFormatType_Lossless_30RGBLE_8A_BiPlanar](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_lossless_30rgble_8a_biplanar)
- [kCVPixelFormatType_Lossless_420YpCbCr10PackedBiPlanarFullRange](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_lossless_420ypcbcr10packedbiplanarfullrange)
- [kCVPixelFormatType_Lossless_64RGBAHalf](https://developer.apple.com/documentation/corevideo/kcvpixelformattype_lossless_64rgbahalf)
:::

:::topic-grid
## 함수
- [CVMetalBufferCacheCreate(_:_:_:_:)](https://developer.apple.com/documentation/corevideo/cvmetalbuffercachecreate(_:_:_:_:))
- [CVMetalBufferCacheCreateBufferFromImage(_:_:_:_:)](https://developer.apple.com/documentation/corevideo/cvmetalbuffercachecreatebufferfromimage(_:_:_:_:))
- [CVMetalBufferCacheFlush(_:_:)](https://developer.apple.com/documentation/corevideo/cvmetalbuffercacheflush(_:_:))
- [CVMetalBufferCacheGetTypeID()](https://developer.apple.com/documentation/corevideo/cvmetalbuffercachegettypeid())
- [CVMetalBufferGetBuffer(_:)](https://developer.apple.com/documentation/corevideo/cvmetalbuffergetbuffer(_:))
- [CVMetalBufferGetTypeID()](https://developer.apple.com/documentation/corevideo/cvmetalbuffergettypeid())
- [CVPixelBufferIsCompatibleWithAttributes(_:_:)](https://developer.apple.com/documentation/corevideo/cvpixelbufferiscompatiblewithattributes(_:_:))
- [CVPixelFormatTypeCopyFourCharCodeString(_:)](https://developer.apple.com/documentation/corevideo/cvpixelformattypecopyfourcharcodestring(_:))
:::

:::topic-grid
## 타입 별칭
- [CVMetalBuffer](https://developer.apple.com/documentation/corevideo/cvmetalbuffer)
:::

:::topic-grid
## 열거형
- [CVImageBufferOriginPosition](https://developer.apple.com/documentation/corevideo/cvimagebufferoriginposition)
:::
