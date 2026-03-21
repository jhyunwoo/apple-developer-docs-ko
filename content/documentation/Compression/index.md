---
route: /documentation/Compression
source_url: https://developer.apple.com/documentation/Compression
source_locale: en-US
section: docc
content_type: symbol
title: Compression
original_title: Compression
source_hash: e0ed51c275fc54b3af852a02d5c8c98aac110fce1ba2b41a8e360adc441c6b8d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:55:49+00:00'
last_translated_at: '2026-03-13T16:05:00+09:00'
---

# Compression

무손실 데이터 압축을 위해 널리 쓰이는 압축 알고리즘을 활용합니다.

## 개요

Compression 프레임워크를 사용하면 파일과 데이터를 저장하거나 공유할 때 앱에서 무손실 압축을 제공할 수 있습니다. 압축은 데이터를 압축(인코딩)하고 압축 해제(디코딩)하는 과정입니다. 예를 들어 텍스트 편집기는 파일을 압축된 형식으로 저장하고, 사용자가 파일을 열면 저장된 파일을 자동으로 압축 해제할 수 있습니다.

![압축 및 압축 해제 과정을 보여 주는 흐름도입니다. 인코더는 원본 데이터를 인코딩된(압축된) 데이터로 압축합니다. 디코더는 인코딩된 데이터를 압축 해제된 데이터로 복원합니다.](https://developer.apple.com)

이 프레임워크는 두 가지 압축 방식을 제공합니다.

- *버퍼 압축*은 파일을 한 단계로 압축하는 방식을 사용하므로, 8MB 미만의 비압축 파일이나 1MB 미만의 압축 파일에 적합합니다.
- *스트림 압축*은 파일을 여러 단계에 걸쳐 압축하는 방식을 사용하므로, 더 큰 파일이나 들어오는 오디오 신호 또는 다운로드 중인 파일 같은 스트리밍 데이터 압축에 적합합니다.

버퍼 압축을 사용하려면 해당 함수 한 번 호출로 입력 데이터를 압축하거나 압축 해제합니다. 문자열을 인코딩하고 디코딩하는 데 사용하는 코드를 단계별로 설명한 내용을 포함해 버퍼 압축에 대해 자세히 알아보려면 [Compressing and decompressing data with buffer compression](https://developer.apple.com/documentation/Accelerate/compressing-and-decompressing-data-with-buffer-compression)을 참고하십시오.

스트림 압축을 사용하려면 원본 버퍼의 데이터를 대상 버퍼로 압축하거나 압축 해제하기 위해 압축 함수 또는 압축 해제 함수를 반복해서 호출합니다. 각 호출 사이에서 압축기 또는 압축 해제기는 처리된 데이터를 원본 버퍼에서 이동시키고 새로운 데이터를 대상 버퍼에 채웁니다. 스트림 압축에 대해 자세히 알아보려면 샘플 코드 프로젝트 [Compressing and decompressing files with stream compression](https://developer.apple.com/documentation/Accelerate/compressing-and-decompressing-files-with-stream-compression)을 참고하십시오.

:::topic-grid
## 여러 단계 압축을 단순화하는 객체
- [Compressing and decompressing data with input and output filters](https://developer.apple.com/documentation/Accelerate/compressing-and-decompressing-data-with-input-and-output-filters): 입력 및 출력 필터를 사용해 스트리밍 데이터 또는 메모리 내 데이터를 압축하고 압축 해제합니다.
- [Compressing and decompressing files with stream compression](https://developer.apple.com/documentation/Accelerate/compressing-and-decompressing-files-with-stream-compression): 모든 파일에 대해 압축을 수행하고, 지원되는 확장자 유형의 파일에 대해 압축 해제를 수행합니다.
- [InputFilter](https://developer.apple.com/documentation/compression/inputfilter): 스트림에서 입력 데이터를 읽는 인코더-디코더입니다.
- [OutputFilter](https://developer.apple.com/documentation/compression/outputfilter): 스트림에 출력 데이터를 기록하는 인코더-디코더입니다.
- [Algorithm](https://developer.apple.com/documentation/compression/algorithm): 압축 또는 압축 해제에 사용하는 알고리즘입니다.
- [FilterError](https://developer.apple.com/documentation/compression/filtererror): 압축 중에 발생하는 오류입니다.
- [FilterOperation](https://developer.apple.com/documentation/compression/filteroperation): 입력 및 출력 필터가 데이터를 압축할지 압축 해제할지 정의하는 연산입니다.
:::

:::topic-grid
## 여러 단계 압축
- [compression_stream](https://developer.apple.com/documentation/compression/compression_stream): 압축 스트림을 나타내는 구조체입니다.
- [compression_stream_init(_:_:_:)](https://developer.apple.com/documentation/compression/compression_stream_init(_:_:_:)): 압축 또는 압축 해제를 위한 압축 스트림을 초기화합니다.
- [compression_stream_process(_:_:)](https://developer.apple.com/documentation/compression/compression_stream_process(_:_:)): 초기화된 압축 스트림 구조체를 사용해 압축 또는 압축 해제를 수행합니다.
- [compression_stream_destroy(_:)](https://developer.apple.com/documentation/compression/compression_stream_destroy(_:)): 스트림 초기화 함수가 할당한 메모리를 해제합니다.
- [compression_status](https://developer.apple.com/documentation/compression/compression_status): 스트림 압축 상태를 나타내는 값 집합입니다.
- [compression_stream_flags](https://developer.apple.com/documentation/compression/compression_stream_flags): 스트림 압축 플래그를 나타내는 값 집합입니다.
- [compression_stream_operation](https://developer.apple.com/documentation/compression/compression_stream_operation): 스트림 압축 작업을 나타내는 값 집합입니다.
- [compression_algorithm](https://developer.apple.com/documentation/compression/compression_algorithm): 압축 알고리즘을 나타내는 값용 구조체입니다.
:::

:::topic-grid
## 단일 단계 압축
- [Compressing and decompressing data with buffer compression](https://developer.apple.com/documentation/Accelerate/compressing-and-decompressing-data-with-buffer-compression): 문자열을 압축하고 파일 시스템에 기록한 뒤, 같은 파일을 버퍼 압축으로 압축 해제합니다.
- [compression_encode_scratch_buffer_size(_:)](https://developer.apple.com/documentation/compression/compression_encode_scratch_buffer_size(_:)): 선택한 알고리즘에 필요한 압축 scratch buffer 크기를 반환합니다.
- [compression_encode_buffer(_:_:_:_:_:_:)](https://developer.apple.com/documentation/compression/compression_encode_buffer(_:_:_:_:_:_:)): 원본 버퍼의 내용을 대상 버퍼로 압축합니다.
- [compression_decode_scratch_buffer_size(_:)](https://developer.apple.com/documentation/compression/compression_decode_scratch_buffer_size(_:)): 선택한 알고리즘에 필요한 압축 해제 scratch buffer 크기를 반환합니다.
- [compression_decode_buffer(_:_:_:_:_:_:)](https://developer.apple.com/documentation/compression/compression_decode_buffer(_:_:_:_:_:_:)): 원본 버퍼의 내용을 대상 버퍼로 압축 해제합니다.
- [compression_algorithm](https://developer.apple.com/documentation/compression/compression_algorithm): 압축 알고리즘을 나타내는 값용 구조체입니다.
:::
