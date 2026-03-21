---
route: /documentation/MediaExtension
source_url: https://developer.apple.com/documentation/MediaExtension
source_locale: en-US
section: docc
content_type: symbol
title: MediaExtension
original_title: MediaExtension
source_hash: c0c3a2fa397111998aa038415aace77ca4d548c07b7b7b642b3e7acc404836ae
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:51:14+00:00'
last_translated_at: '2026-03-13T18:40:00+09:00'
---

# MediaExtension

이 프레임워크는 시스템이 기본적으로 지원하지 않는 미디어를 위해 개발자가 포맷 리더, 비디오 디코더, RAW 프로세서를 만들 수 있는 수단을 제공합니다.

## 개요

MediaExtension 포맷 리더는 시스템이 기본적으로 지원하지 않는 미디어 자산을 감싸서 시스템이 이를 인식할 수 있게 합니다. MediaExtension 비디오 디코더는 시스템이 기본적으로 지원하지 않는 비디오 포맷을 디코딩합니다. MediaExtension RAW 프로세서는 비디오 디코더와 함께 동작하여 RAW 디코딩 과정을 직접 제어할 수 있게 합니다. 개발자는 포맷 리더, 비디오 디코더, RAW 프로세서를 [ExtensionKit](https://developer.apple.com/documentation/ExtensionKit) 번들로 만들어 호스트 앱에 포함해야 합니다. 사용자가 호스트 앱을 설치하고 실행하면, 포함된 확장 기능은 사용자가 opt in한 시스템의 어떤 앱에서도 사용할 수 있게 됩니다.

:::topic-grid
## 포맷 리더
- [MEFormatReader](https://developer.apple.com/documentation/mediaextension/meformatreader): 단일 미디어 자산을 나타내는 포맷 리더의 요구 사항을 정의하는 프로토콜입니다.
- [MEFormatReaderExtension](https://developer.apple.com/documentation/mediaextension/meformatreaderextension): 바이트 소스로 새 포맷 리더를 생성하는 팩터리를 정의하는 프로토콜입니다.
- [MEFormatReaderInstantiationOptions](https://developer.apple.com/documentation/mediaextension/meformatreaderinstantiationoptions): 포맷 리더 확장에 전달할 옵션을 담은 객체입니다.
- [MEFileInfo](https://developer.apple.com/documentation/mediaextension/mefileinfo): 미디어 자산의 파일 속성을 포함하는 객체입니다.
- [Format reader property list dictionaries](https://developer.apple.com/documentation/mediaextension/format-reader-property-list-dictionaries): 포맷 리더를 설명하고 지원하는 포맷을 등록하기 위한 property list dictionary를 포함합니다.
- [Format reader entitlement](https://developer.apple.com/documentation/mediaextension/format-reader-entitlement): 확장이 MediaExtension 포맷 리더임을 나타내는 entitlement를 포함합니다.
:::

:::topic-grid
## 트랙 리더
- [METrackReader](https://developer.apple.com/documentation/mediaextension/metrackreader): 미디어 자산 내 트랙에 대해 제공해야 하는 정보를 정의하는 프로토콜입니다.
- [METrackInfo](https://developer.apple.com/documentation/mediaextension/metrackinfo): 미디어 자산에서 파싱한 트랙 속성을 포함하는 객체입니다.
:::

:::topic-grid
## 샘플 커서
- [MESampleCursor](https://developer.apple.com/documentation/mediaextension/mesamplecursor): 미디어 자산의 트랙 내 샘플에 대해 제공해야 하는 정보를 정의하고, 디코드 순서 또는 프레젠테이션 순서로 트랙의 샘플을 단계적으로 탐색할 수 있게 하는 프로토콜입니다.
- [MESampleLocation](https://developer.apple.com/documentation/mediaextension/mesamplelocation): 미디어 내 샘플 위치에 대한 정보를 제공하는 객체입니다.
- [MESampleCursorChunk](https://developer.apple.com/documentation/mediaextension/mesamplecursorchunk): 샘플 위치에 있는 미디어 청크에 대한 정보를 제공하는 객체입니다.
- [MEEstimatedSampleLocation](https://developer.apple.com/documentation/mediaextension/meestimatedsamplelocation): 미디어에서 추정된 샘플 위치 정보를 제공하는 객체입니다.
- [MEHEVCDependencyInfo](https://developer.apple.com/documentation/mediaextension/mehevcdependencyinfo): 샘플의 HEVC 종속성 속성에 대한 정보를 제공하는 객체입니다.
:::

:::topic-grid
## 바이트 소스
- [MEByteSource](https://developer.apple.com/documentation/mediaextension/mebytesource): 미디어 자산 파일의 데이터에 대한 읽기 접근을 제공합니다.
:::

:::topic-grid
## 비디오 디코더
- [MEVideoDecoder](https://developer.apple.com/documentation/mediaextension/mevideodecoder): 비디오 디코더의 요구 사항을 정의하는 프로토콜입니다.
- [MEVideoDecoderExtension](https://developer.apple.com/documentation/mediaextension/mevideodecoderextension): 확장이 구현하는 codec 타입에 대해 새로운 비디오 디코더를 생성하는 팩터리를 정의하는 프로토콜입니다.
- [MEDecodeFrameOptions](https://developer.apple.com/documentation/mediaextension/medecodeframeoptions): 프레임 단위로 비디오 디코더 동작을 안내하는 객체입니다.
- [MEVideoDecoderPixelBufferManager](https://developer.apple.com/documentation/mediaextension/mevideodecoderpixelbuffermanager): 픽셀 버퍼 요구 사항을 설명하고 새 픽셀 버퍼를 생성합니다.
- [Video decoder property list dictionary](https://developer.apple.com/documentation/mediaextension/video-decoder-property-list-dictionary): 비디오 디코더를 설명하기 위한 property list dictionary를 포함합니다.
- [Video decoder entitlement](https://developer.apple.com/documentation/mediaextension/video-decoder-entitlement): 확장이 MediaExtension 비디오 디코더임을 나타내는 entitlement를 포함합니다.
:::

:::topic-grid
## RAW 프로세서
- [MERAWProcessor](https://developer.apple.com/documentation/mediaextension/merawprocessor): RAW 프로세서의 요구 사항을 정의하는 프로토콜입니다.
- [MERAWProcessorExtension](https://developer.apple.com/documentation/mediaextension/merawprocessorextension): 확장이 구현하는 codec 타입에 대해 RAW 프로세서를 생성하는 팩터리를 정의하는 프로토콜입니다.
- [MERAWProcessorPixelBufferManager](https://developer.apple.com/documentation/mediaextension/merawprocessorpixelbuffermanager): 픽셀 버퍼 요구 사항을 설명하고 새 픽셀 버퍼를 생성합니다.
- [MERAWProcessingParameter](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter): 프로세서가 노출하는 각 처리 매개변수를 설명할 때 RAW 프로세서가 사용하는 객체입니다.
- [MERAWProcessorNotification](https://developer.apple.com/documentation/mediaextension/merawprocessornotification): RAW 프로세서 상태 변화가 있음을 나타내는 알림입니다.
- [RAW processor property list dictionary](https://developer.apple.com/documentation/mediaextension/raw-processor-property-list-dictionary): RAW 프로세서를 설명하기 위한 property list dictionary를 포함합니다.
- [RAW processor entitlement](https://developer.apple.com/documentation/mediaextension/raw-processor-entitlement): 확장이 MediaExtension RAW 프로세서임을 나타내는 entitlement를 포함합니다.
:::

:::topic-grid
## 오류
- [MediaExtensionErrorDomain](https://developer.apple.com/documentation/mediaextension/mediaextensionerrordomain): 오류의 도메인입니다.
- [MEError](https://developer.apple.com/documentation/mediaextension/meerror-swift.struct): MediaExtension 프레임워크 오류입니다.
- [MEError.Code](https://developer.apple.com/documentation/mediaextension/meerror-swift.struct/code): 미디어 확장 오류 코드를 모델링하는 열거형입니다.
:::

:::topic-grid
## 변수
- [kMERAWProcessorClassImplementationIDKey](https://developer.apple.com/documentation/mediaextension/kmerawprocessorclassimplementationidkey)
- [kMERAWProcessorCodecNameKey](https://developer.apple.com/documentation/mediaextension/kmerawprocessorcodecnamekey)
- [kMERAWProcessorCodecTypeKey](https://developer.apple.com/documentation/mediaextension/kmerawprocessorcodectypekey)
- [kMERAWProcessorObjectNameKey](https://developer.apple.com/documentation/mediaextension/kmerawprocessorobjectnamekey)
- [kMERAWProcessorProcessorInfoKey](https://developer.apple.com/documentation/mediaextension/kmerawprocessorprocessorinfokey)
:::
