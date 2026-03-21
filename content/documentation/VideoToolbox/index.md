---
route: /documentation/VideoToolbox
source_url: https://developer.apple.com/documentation/VideoToolbox
source_locale: en-US
section: docc
content_type: symbol
title: Video Toolbox
original_title: Video Toolbox
source_hash: 6b7de9f4a3fbb5d94e9a1c22d6599d6ee4cf59061b4c4b6a9b4416dc0a50dd3d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:15:24+00:00'
last_translated_at: '2026-03-13T19:25:00+09:00'
---

# Video Toolbox

하드웨어 가속 비디오 인코딩 및 디코딩 기능을 직접 다룹니다.

## 개요

VideoToolbox는 하드웨어 인코더와 디코더에 직접 접근할 수 있게 해 주는 저수준 프레임워크입니다. 이 프레임워크는 비디오 압축과 압축 해제 서비스, 그리고 CoreVideo 픽셀 버퍼에 저장된 래스터 이미지 포맷 간 변환 서비스를 제공합니다. 이러한 서비스는 세션 객체(압축, 압축 해제, 픽셀 전송) 형태로 제공되며, Core Foundation(CF) 타입으로 노출됩니다. 하드웨어 인코더와 디코더에 직접 접근할 필요가 없는 앱이라면 일반적으로 VideoToolbox를 직접 사용할 필요가 없습니다.

:::topic-grid
## 프레임 처리
- [Frame processing](https://developer.apple.com/documentation/videotoolbox/frame-processing): 다양한 비디오 처리 기능에 접근하기 위한 인터페이스입니다.
:::

:::topic-grid
## 모션 추정
- [VTMotionEstimationSession](https://developer.apple.com/documentation/videotoolbox/vtmotionestimationsession)
:::

:::topic-grid
## 압축
- [Encoding video for low-latency conferencing](https://developer.apple.com/documentation/videotoolbox/encoding-video-for-low-latency-conferencing): 화상 회의 앱에 맞게 인코딩을 최적화하도록 압축 세션을 구성합니다.
- [Encoding video for live streaming](https://developer.apple.com/documentation/videotoolbox/encoding-video-for-live-streaming): 라이브 스트리밍용 비디오를 인코딩하도록 압축 세션을 구성합니다.
- [Encoding video for offline transcoding](https://developer.apple.com/documentation/videotoolbox/encoding-video-for-offline-transcoding): 오프라인 워크플로에서 비디오를 트랜스코딩하도록 압축 세션을 구성합니다.
- [VTCompressionSession](https://developer.apple.com/documentation/videotoolbox/vtcompressionsession-api-collection): 비디오 데이터를 압축하는 객체입니다.
- [VTDecompressionSession](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsession-api-collection): 비디오 데이터를 압축 해제하는 객체입니다.
- [VTFrameSilo](https://developer.apple.com/documentation/videotoolbox/vtframesilo-api-collection): 멀티패스 인코딩 세션의 sample buffer를 저장하는 객체입니다.
- [VTMultiPassStorage](https://developer.apple.com/documentation/videotoolbox/vtmultipassstorage-api-collection): 멀티패스 인코딩 세션의 비디오 인코딩 메타데이터를 저장하는 객체입니다.
:::

:::topic-grid
## 변환
- [VTPixelTransferSession](https://developer.apple.com/documentation/videotoolbox/vtpixeltransfersession-api-collection): 소스 픽셀 버퍼의 비디오 데이터를 대상 픽셀 버퍼로 변환하는 객체입니다.
- [VTPixelRotationSession](https://developer.apple.com/documentation/videotoolbox/vtpixelrotationsession-api-collection): 소스 픽셀 버퍼를 대상 픽셀 버퍼로 회전시키는 객체입니다.
:::

:::topic-grid
## RAW 처리
- [VTRAWProcessingSession](https://developer.apple.com/documentation/videotoolbox/vtrawprocessingsession): RAW나 Bayer 같은 카메라 네이티브 포맷의 프레임을 처리하는 객체입니다.
:::

:::topic-grid
## Media Extension
- [VTExtensionPropertiesKey](https://developer.apple.com/documentation/videotoolbox/vtextensionpropertieskey): Media Extension 확장 속성 dictionary의 키입니다.
:::

:::topic-grid
## HDR 메타데이터
- [VTHDRPerFrameMetadataGenerationSession](https://developer.apple.com/documentation/videotoolbox/vthdrperframemetadatagenerationsession): 프레임별 HDR 메타데이터를 생성하는 객체입니다.
:::

:::topic-grid
## 코덱 지원
- [VTIsHardwareDecodeSupported(_:)](https://developer.apple.com/documentation/videotoolbox/vtishardwaredecodesupported(_:)): 현재 시스템이 지정한 코덱에 대한 하드웨어 디코드를 지원하는지 나타내는 Boolean 값을 반환합니다.
- [VTRegisterProfessionalVideoWorkflowVideoEncoders()](https://developer.apple.com/documentation/videotoolbox/vtregisterprofessionalvideoworkflowvideoencoders()): 클라이언트의 전문 비디오 워크플로에 적합한 인코더를 로드합니다.
- [VTRegisterProfessionalVideoWorkflowVideoDecoders()](https://developer.apple.com/documentation/videotoolbox/vtregisterprofessionalvideoworkflowvideodecoders()): 클라이언트의 전문 비디오 워크플로에 적합한 디코더를 로드합니다.
- [VTRegisterSupplementalVideoDecoderIfAvailable(_:)](https://developer.apple.com/documentation/videotoolbox/vtregistersupplementalvideodecoderifavailable(_:)): 현재 시스템에 존재하는 경우 지정한 코덱 타입의 비디오 디코더를 등록합니다.
- [VTCopySupportedPropertyDictionaryForEncoder(width:height:codecType:encoderSpecification:encoderIDOut:supportedPropertiesOut:)](https://developer.apple.com/documentation/videotoolbox/vtcopysupportedpropertydictionaryforencoder(width:height:codectype:encoderspecification:encoderidout:supportedpropertiesout:)): 인코더에 대한 지원 프로퍼티 목록과 인코더 ID를 생성합니다.
- [VTCopyVideoEncoderList(_:_:)](https://developer.apple.com/documentation/videotoolbox/vtcopyvideoencoderlist(_:_:)): 사용 가능한 비디오 인코더 목록을 생성합니다.
- [Video Encoder List Keys](https://developer.apple.com/documentation/videotoolbox/video-encoder-list-keys): 비디오 인코더 정보를 가져오는 데 사용하는 dictionary 키 상수입니다.
:::

:::topic-grid
## 유틸리티
- [VTCreateCGImageFromCVPixelBuffer(_:options:imageOut:)](https://developer.apple.com/documentation/videotoolbox/vtcreatecgimagefromcvpixelbuffer(_:options:imageout:)): 제공된 픽셀 버퍼를 사용해 Core Graphics 비트맵 이미지 또는 이미지 마스크를 생성합니다.
:::

:::topic-grid
## 데이터 타입
- [VTSession](https://developer.apple.com/documentation/videotoolbox/vtsession-api-collection): VideoToolbox 세션 객체를 구성하는 공통 인터페이스를 제공하는 추상 객체입니다.
- [VTInt32Point](https://developer.apple.com/documentation/videotoolbox/vtint32point): 32비트 정수 점 값을 나타내는 구조체입니다.
- [VTInt32Size](https://developer.apple.com/documentation/videotoolbox/vtint32size): 32비트 정수 크기 값을 나타내는 구조체입니다.
:::

:::topic-grid
## 오류
- [Error Code Constants](https://developer.apple.com/documentation/videotoolbox/1490398-error-code-constants): Video Toolbox 작업 오류 코드용 상수입니다.
:::

:::topic-grid
## 참고 자료
- [VideoToolbox Reference](https://developer.apple.com/documentation/videotoolbox/videotoolbox-reference)
:::
