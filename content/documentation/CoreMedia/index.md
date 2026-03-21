---
route: /documentation/CoreMedia
source_url: https://developer.apple.com/documentation/CoreMedia
source_locale: en-US
section: docc
content_type: symbol
title: Core Media
original_title: Core Media
source_hash: b166b055f8ef3592b90eb31f8a904eb852917c67c732026bcd5474aa0b9571c8
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:17:57+00:00'
last_translated_at: '2026-03-13T23:18:11+09:00'
---

# Core Media

기본 데이터 타입으로 시간 기반 오디오 및 비주얼 자산을 표현합니다.

## 개요

Core Media 프레임워크는 AVFoundation과 Apple 플랫폼의 다른 고수준 미디어 프레임워크가 사용하는 미디어 파이프라인을 정의합니다. Core Media의 저수준 데이터 타입과 인터페이스를 사용해 미디어 샘플을 효율적으로 처리하고 미디어 데이터 큐를 관리할 수 있습니다.

:::topic-grid
## 샘플 처리
- [CMSampleBuffer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer-api): 동일한 미디어 타입의 미디어 샘플을 0개 이상 담는 객체입니다.
- [CMBlockBuffer](https://developer.apple.com/documentation/coremedia/cmblockbuffer-api): 시스템이 처리 시스템 안에서 메모리 블록을 이동할 때 사용하는 객체입니다.
- [CMTaggedBufferGroup](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroup): Core Media tagged buffer group을 다루기 위한 Objective-C 타입과 인터페이스입니다.
- [CMFormatDescription](https://developer.apple.com/documentation/coremedia/cmformatdescription-api): sample buffer 안의 샘플을 설명하는 미디어 포맷 설명자입니다.
- [CMAttachment](https://developer.apple.com/documentation/coremedia/cmattachment-api): sample buffer에 보조 메타데이터를 추가합니다.
- [CMTaggedBuffer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffer): 메타데이터 태그를 포함한 미디어 버퍼 인스턴스입니다.
- [CMMutableDataBlockBuffer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer): 바이트 범위에 대해 읽기/쓰기를 제공하는 block buffer입니다.
- [CMReadOnlyDataBlockBuffer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer): 바이트 범위에 대해 읽기 전용 접근을 제공하는 block buffer입니다.
- [CMReadySampleBuffer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer): 즉시 사용할 수 있는 미디어 데이터 샘플을 담는 buffer입니다.
- [CMSampleDataReference](https://developer.apple.com/documentation/coremedia/cmsampledatareference): URL 위치의 샘플 데이터를 참조합니다.
- [CMTaggedDynamicBuffer](https://developer.apple.com/documentation/coremedia/cmtaggeddynamicbuffer): 읽기 전용 미디어 버퍼와 연결된 태그 모음을 담습니다.
:::

:::topic-grid
## 시간 표현
- [CMTime](https://developer.apple.com/documentation/coremedia/cmtime-api): 시간을 표현하는 구조체입니다.
- [CMTimeRange](https://developer.apple.com/documentation/coremedia/cmtimerange-api): 시간 범위를 표현하는 구조체입니다.
- [CMTimeMapping](https://developer.apple.com/documentation/coremedia/cmtimemapping-api): 원본 시간 범위의 한 구간을 대상 시간 범위에 매핑하는 구조체입니다.
:::

:::topic-grid
## 미디어 동기화
- [CMClock](https://developer.apple.com/documentation/coremedia/cmclock-api): 앱과 기기를 동기화할 때 사용하는 기준 clock입니다.
- [CMAudioClock](https://developer.apple.com/documentation/coremedia/cmaudioclock-api): 오디오 소스와 동기화되는 특수한 기준 clock입니다.
- [CMTimebase](https://developer.apple.com/documentation/coremedia/cmtimebase-api): 앱이 제어하는 타임라인 모델입니다.
:::

:::topic-grid
## 텍스트 마크업
- [CMTextMarkup](https://developer.apple.com/documentation/coremedia/cmtextmarkup): 읽을 수 있는 미디어의 텍스트 마크업을 지정하는 attribute입니다.
:::

:::topic-grid
## 메타데이터
- [CMMetadata](https://developer.apple.com/documentation/coremedia/cmmetadata): 프레임워크의 Metadata Identifier Services와 Metadata Data Type Registry를 다루는 API입니다.
- [CMTag](https://developer.apple.com/documentation/coremedia/cmtag-api): Core Media tag를 다루는 타입과 인터페이스입니다.
- [CMTag](https://developer.apple.com/documentation/coremedia/cmtag-swift.class): 미디어 버퍼에 추가 메타데이터를 설정하는 tag입니다.
- [CMTypedTag](https://developer.apple.com/documentation/coremedia/cmtypedtag): 값에 대응하는 Swift 타입을 함께 가지는 tag입니다.
- [CMTagCollection](https://developer.apple.com/documentation/coremedia/cmtagcollection): Core Media tag collection을 다루는 Objective-C 타입과 인터페이스입니다.
- [CMProjectionType](https://developer.apple.com/documentation/coremedia/cmprojectiontype): 3D 비디오 버퍼 또는 채널의 투영 표면 정보를 설명하는 상수입니다.
- [CMStereoViewComponents](https://developer.apple.com/documentation/coremedia/cmstereoviewcomponents): 버퍼 또는 채널에 포함된 스테레오 뷰를 설명하는 상수입니다.
- [CMStereoViewInterpretationOptions](https://developer.apple.com/documentation/coremedia/cmstereoviewinterpretationoptions): 상수로부터 스테레오 뷰 해석 옵션 집합을 만듭니다.
- [CMPackingType](https://developer.apple.com/documentation/coremedia/cmpackingtype): 각 비디오 프레임 안의 패킹 유형입니다.
:::

:::topic-grid
## 큐
- [CMSimpleQueue](https://developer.apple.com/documentation/coremedia/cmsimplequeue-api): 단순한 lockless FIFO 요소 큐입니다.
- [CMBufferQueue](https://developer.apple.com/documentation/coremedia/cmbufferqueue-api): 시간 정보를 가진 buffer 큐입니다.
- [CMMemoryPool](https://developer.apple.com/documentation/coremedia/cmmemorypool-api): 큰 메모리 블록을 다룰 때 메모리 할당을 최적화하는 객체입니다.
:::

:::topic-grid
## 참고 자료
- [Core Media Constants](https://developer.apple.com/documentation/coremedia/core-media-constants)
- [Core Media Functions](https://developer.apple.com/documentation/coremedia/core-media-functions)
- [Core Media Type Aliases](https://developer.apple.com/documentation/coremedia/core-media-type-aliases)
:::
