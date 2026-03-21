---
route: /documentation/Cinematic
source_url: https://developer.apple.com/documentation/Cinematic
source_locale: en-US
section: docc
content_type: symbol
title: Cinematic
original_title: Cinematic
source_hash: 96c63402fbb5469fc2532cea9e4ff7e184cc6ea430ed568c3fcf9dea6c566aec
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:03:23+00:00'
last_translated_at: '2026-03-13T16:25:00+09:00'
---

# Cinematic

Cinematic 모드로 촬영한 자산의 재생 및 편집 기능을 앱에 통합합니다.

## 개요

Cinematic 프레임워크를 사용하면 Camera 앱의 Cinematic 모드로 촬영한 동영상에 대해 전문가 수준의 편집 및 재생 기능을 앱에 추가할 수 있습니다. 이는 Final Cut Pro, Photos, iMovie 같은 앱에서 사용하는 것과 동일한 기능입니다. 예를 들어 촬영 후에도 동영상에서 초점 거리와 조리개를 변경해 보케 효과를 만들 수 있습니다.

:::topic-grid
## 핵심 사항
- [Playing and editing Cinematic mode video](https://developer.apple.com/documentation/cinematic/playing-and-editing-cinematic-mode-video): 조정 가능한 피사계 심도와 초점 지점을 사용해 Cinematic 모드 비디오를 재생하고 편집합니다.
- [CNScript](https://developer.apple.com/documentation/cinematic/cnscript-1ispe): Cinematic 모드로 촬영한 동영상과 관련된 초점 결정, 초점 전환, 감지, 감지 트랙의 모음과 이를 변경하는 메서드입니다.
:::

:::topic-grid
## 읽기와 렌더링
- [CNAssetInfo](https://developer.apple.com/documentation/cinematic/cnassetinfo-2ata2): 트랙을 포함해 자산의 Cinematic 관련 정보를 제공하는 객체입니다.
- [CNCompositionInfo](https://developer.apple.com/documentation/cinematic/cncompositioninfo-7eunn): Cinematic 자산에 적절한 수의 트랙을 추가할 수 있게 해 주는 객체입니다.
- [CNRenderingSession](https://developer.apple.com/documentation/cinematic/cnrenderingsession-1hzh8): 렌더링이 일어나는 컨텍스트를 나타내는 객체입니다.
:::

:::topic-grid
## 편집
- [Editing Spatial Audio with an audio mix](https://developer.apple.com/documentation/cinematic/editing-spatial-audio-with-an-audio-mix): Cinematic 프레임워크의 Audio Mix API를 사용해 Spatial Audio 편집 기능을 추가합니다.
- [CNDetection](https://developer.apple.com/documentation/cinematic/cndetection-swift.struct): 특정 시점에 감지된 피사체, 얼굴, 몸통, 반려동물을 나타내는 구조체입니다.
- [CNDecision](https://developer.apple.com/documentation/cinematic/cndecision-swift.struct): 특정 시점에 특정 감지 대상 또는 감지 대상 그룹에 초점을 맞추기로 한 결정을 나타내는 객체입니다.
- [CNDetectionTrack](https://developer.apple.com/documentation/cinematic/cndetectiontrack-2bxtd): 시간에 따라 동일한 피사체를 감지한 연속 기록을 나타내는 객체입니다.
- [CNFixedDetectionTrack](https://developer.apple.com/documentation/cinematic/cnfixeddetectiontrack-93rrw): 고정 감지 트랙을 나타내는 객체입니다.
- [CNCustomDetectionTrack](https://developer.apple.com/documentation/cinematic/cncustomdetectiontrack-9a2zo): 개별 감지로 구성된 이산 감지 트랙을 나타내는 객체입니다.
- [CNDetectionType](https://developer.apple.com/documentation/cinematic/cndetectiontype): 얼굴, 몸통, 고양이, 개 등 감지된 객체의 타입입니다.
:::

:::topic-grid
## 사용자 정의 객체 추적
- [CNBoundsPrediction](https://developer.apple.com/documentation/cinematic/cnboundsprediction-swift.struct): 예측된 피사체의 경계를 나타내는 구조체입니다.
- [CNObjectTracker](https://developer.apple.com/documentation/cinematic/cnobjecttracker-1n598): 정규화된 점 또는 사각형을 시간이 흐르며 객체를 추적하는 감지 트랙으로 변환하는 객체입니다.
:::

:::topic-grid
## 구조체
- [CNCinematicError](https://developer.apple.com/documentation/cinematic/cncinematicerror)
:::

:::topic-grid
## 레퍼런스
- [Cinematic Enumerations](https://developer.apple.com/documentation/cinematic/cinematic-enumerations)
- [Cinematic Constants](https://developer.apple.com/documentation/cinematic/cinematic-constants)
- [Cinematic Data Types](https://developer.apple.com/documentation/cinematic/cinematic-data-types)
:::

:::topic-grid
## 클래스
- [CNAssetSpatialAudioInfo](https://developer.apple.com/documentation/cinematic/cnassetspatialaudioinfo-7hdev)
:::

:::topic-grid
## 열거형
- [CNSpatialAudioContentType](https://developer.apple.com/documentation/cinematic/cnspatialaudiocontenttype)
- [CNSpatialAudioRenderingStyle](https://developer.apple.com/documentation/cinematic/cnspatialaudiorenderingstyle)
:::
