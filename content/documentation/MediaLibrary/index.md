---
route: /documentation/MediaLibrary
source_url: https://developer.apple.com/documentation/MediaLibrary
source_locale: en-US
section: docc
content_type: symbol
title: Media Library
original_title: Media Library
source_hash: 2548cdd17b92600a770a8fe03c76b4407b7319f30bb51610a69c10d7aee59c88
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:36:24+00:00'
last_translated_at: '2026-03-14T01:03:00+09:00'
---

# Media Library

사용자의 멀티미디어 콘텐츠를 읽기 전용 컬렉션으로 접근합니다.

## 개요

Media Library 프레임워크는 사용자의 이미지, 오디오, 비디오 컬렉션을 표현하는 읽기 전용 Objective-C 데이터 모델을 제공합니다. Media Library 프레임워크의 초기 진입점은 [MLMediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmedialibrary)이며, 이 객체는 사용자의 미디어를 media source, group, object로 구성된 계층 구조로 로드합니다.

가장 상위 수준에서 media library 인스턴스 안의 모든 콘텐츠는 media source별로 분류됩니다. 개념적으로 media source는 iTunes나 Aperture 같은 단일 앱을 나타냅니다. 각 source는 루트 group에서 시작하는 media group 계층을 포함합니다. 이 group은 사진, 노래, 영화처럼 하나의 미디어 조각을 담고 있는 개별 파일인 media object로 이루어집니다. 각 object는 media library 인스턴스 안에 하나만 존재하지만, 하나의 source 안에서 여러 group이 같은 object를 참조할 수 있습니다. group 계층 구조는 media source마다 다릅니다.

![](https://developer.apple.com)

:::topic-grid
## 클래스
- [MLMediaGroup](https://developer.apple.com/documentation/medialibrary/mlmediagroup): iTunes나 Aperture처럼 하나의 media source에서 온 media object의 그룹화를 제공하는 클래스입니다. 사진, 노래, 영화 같은 하나의 미디어 조각을 담는 개별 파일인 media object는 각 media source 안에서 하나 이상의 group이 참조합니다. 이러한 그룹화는 filter 역할을 하며 각 source 안의 object 컬렉션에 계층 구조를 제공합니다.
- [MLMediaLibrary](https://developer.apple.com/documentation/medialibrary/mlmedialibrary): 여러 source의 media object 컬렉션에 접근하는 인터페이스를 제공하는 클래스입니다. Media Library 프레임워크의 초기 진입점 역할을 합니다.
- [MLMediaObject](https://developer.apple.com/documentation/medialibrary/mlmediaobject): 사진, 노래, 영화 같은 단일 media file을 설명하는 클래스입니다. 각 media object는 이름, media type, URL 등 기본 metadata를 포함합니다. 각 object에 대한 추가 정보는 attribute 목록에 저장됩니다. 가능한 object attribute key 목록은 를 참고하십시오.
- [MLMediaSource](https://developer.apple.com/documentation/medialibrary/mlmediasource): 특정 media provider를 식별하는 클래스입니다. 개념적으로 media source는 iTunes나 Aperture 같은 단일 앱을 나타냅니다. 각 media source는 사진, 노래, 영화 같은 하나의 미디어 조각을 담는 개별 파일인 media object의 여러 group을 포함합니다.
:::

:::topic-grid
## 참고 자료
- [MediaLibrary Constants](https://developer.apple.com/documentation/medialibrary/medialibrary-constants)
:::
