---
route: /documentation/Vision
source_url: https://developer.apple.com/documentation/Vision
source_locale: en-US
section: docc
content_type: symbol
title: Vision
original_title: Vision
source_hash: d8de9cf9637afb9f21ee563a779f27bcf0d655052c7b2226cc80e7c1408788db
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:44:32+00:00'
last_translated_at: '2026-03-14T00:03:00+09:00'
---

# Vision

객체 감지, 텍스트 인식, 이미지 분할을 위한 컴퓨터 비전 알고리즘을 사용해 앱의 이미지와 비디오 콘텐츠를 분석합니다.

## 개요

Vision 프레임워크는 컴퓨터 비전 작업을 위한 사전 학습된 머신 러닝 모델을 제공합니다. Vision을 사용하면 정지 이미지와 비디오를 다양한 목적으로 분석할 수 있습니다. 예를 들면 다음과 같습니다.

- 일상 사물, 문서, 사진에서 26개 언어의 텍스트 인식
- 바코드와 QR 코드 감지
- 얼굴 감지 및 얼굴 특징 분석
- subject lifting으로 사람과 전경 객체 분리
- 동작 및 제스처 인식을 위한 사람과 동물의 신체 자세 추적
- 분류 및 검색을 위한 이미지 분류
- 이미지 품질 측정 및 시각적 유사도 비교

![subject lifting으로 배경에서 분리된 개입니다.](https://developer.apple.com)

모든 Vision 분석 작업은 같은 단계를 따릅니다. 요청을 만들고, 이미지나 비디오 프레임에 대해 수행한 뒤, 결과 observation을 읽습니다. 예를 들어 이미지에서 텍스트를 감지하려면 수행하려는 분석 유형에 대한 요청을 생성합니다. 각 요청은 [VisionRequest](https://developer.apple.com/documentation/vision/visionrequest) 프로토콜을 준수합니다.

```swift
let request = RecognizeTextRequest()
let observations = try await request.perform(on: imageData)

// 앱에서 사용할 수 있도록 observation을 저장합니다.
var scannedText: [String] = []

for observation in observations {
    scannedText.append(observation.transcript)
}
```

요청은 이미지 분석 결과를 담고 있는 observation 객체 배열을 반환합니다. 각 observation 타입은 인식된 텍스트, 신뢰도 점수, 경계 상자 위치 같은 분석 결과의 구체적인 세부 정보를 제공합니다.

얼굴 경계 상자나 텍스트 영역처럼 이미지 위치를 설명하는 observation의 경우, Vision은 값 범위가 `0.0`에서 `1.0`이고 원점이 왼쪽 아래 모서리에 있는 정규화 좌표계를 사용합니다. 좌표 타입과 변환 helper에 대한 자세한 내용은 [Image locations and regions](https://developer.apple.com/documentation/vision#Image-locations-and-regions)를 참고합니다.

동일한 이미지에 대해 여러 요청을 수행할 수도 있습니다. 자세한 내용은 Request handlers 섹션의 [ImageRequestHandler](https://developer.apple.com/documentation/vision/imagerequesthandler)를 참고합니다.

이 패턴은 얼굴 감지, 움직임 추적, 이미지 품질 분석, Core ML 모델을 사용한 사용자 정의 분석 등 모든 Vision 요청에 적용됩니다. 각 요청 타입은 해당 분석 작업에 특화된 observation을 반환합니다.

:::note Note
iOS 18.0부터 Vision 프레임워크는 새로운 Swift 전용 API를 제공합니다. 원래 API를 보려면 [Original Objective-C and Swift API](https://developer.apple.com/documentation/vision/original-objective-c-and-swift-api)를 참고합니다.
:::

:::topic-grid
## 텍스트 및 문서 분석
- [Locating and displaying recognized text](https://developer.apple.com/documentation/vision/locating-and-displaying-recognized-text): Vision 프레임워크의 텍스트 인식 요청을 사용해 사진에서 텍스트 인식을 수행합니다.
- [Recognizing tables within a document](https://developer.apple.com/documentation/vision/recognize-tables-within-a-document): 표가 포함된 문서를 스캔하고 그 내용을 서식 있는 방식으로 추출합니다.
- [DetectBarcodesRequest](https://developer.apple.com/documentation/vision/detectbarcodesrequest): 이미지에서 바코드를 감지하는 요청입니다.
- [DetectDocumentSegmentationRequest](https://developer.apple.com/documentation/vision/detectdocumentsegmentationrequest): 입력 이미지에서 텍스트를 포함한 직사각형 영역을 감지하는 요청입니다.
- [DetectTextRectanglesRequest](https://developer.apple.com/documentation/vision/detecttextrectanglesrequest): 이미지에서 눈에 보이는 텍스트 영역을 찾는 이미지 분석 요청입니다.
- [RecognizeDocumentsRequest](https://developer.apple.com/documentation/vision/recognizedocumentsrequest): 문서 이미지를 스캔하고 구조 정보를 제공하는 이미지 분석 요청입니다.
- [RecognizeTextRequest](https://developer.apple.com/documentation/vision/recognizetextrequest): 이미지에서 텍스트를 인식하는 이미지 분석 요청입니다.
:::

:::topic-grid
## 얼굴 분석
- [Analyzing a selfie and visualizing its content](https://developer.apple.com/documentation/vision/analyzing-a-selfie-and-visualizing-its-content): Vision 프레임워크를 사용해 이미지 모음의 얼굴 캡처 품질을 계산하고 얼굴 특징을 시각화합니다.
- [DetectFaceCaptureQualityRequest](https://developer.apple.com/documentation/vision/detectfacecapturequalityrequest): 사진 속 얼굴의 캡처 품질을 나타내는 부동소수점 수를 생성하는 요청입니다.
- [DetectFaceLandmarksRequest](https://developer.apple.com/documentation/vision/detectfacelandmarksrequest): 이미지에서 눈, 입 같은 얼굴 특징을 찾는 이미지 분석 요청입니다.
- [DetectFaceRectanglesRequest](https://developer.apple.com/documentation/vision/detectfacerectanglesrequest): 이미지 안의 얼굴을 찾는 요청입니다.
:::

:::topic-grid
## 이미지 분할 및 subject lifting
- [GenerateForegroundInstanceMaskRequest](https://developer.apple.com/documentation/vision/generateforegroundinstancemaskrequest): 배경에서 분리할 눈에 띄는 객체의 instance mask를 생성하는 요청입니다.
- [GeneratePersonInstanceMaskRequest](https://developer.apple.com/documentation/vision/generatepersoninstancemaskrequest): 입력 이미지에서 찾은 개별 사람의 마스크를 생성하는 요청입니다.
- [GeneratePersonSegmentationRequest](https://developer.apple.com/documentation/vision/generatepersonsegmentationrequest): 입력 이미지에서 찾은 사람에 대한 matte 이미지를 생성하는 요청입니다.
:::

:::topic-grid
## 자세 분석
- [DetectAnimalBodyPoseRequest](https://developer.apple.com/documentation/vision/detectanimalbodyposerequest): 동물의 신체 자세를 감지하는 요청입니다.
- [DetectHumanBodyPose3DRequest](https://developer.apple.com/documentation/vision/detecthumanbodypose3drequest): 카메라를 기준으로 3D 공간 안의 사람 신체 포인트를 감지하는 요청입니다.
- [DetectHumanBodyPoseRequest](https://developer.apple.com/documentation/vision/detecthumanbodyposerequest): 사람의 신체 자세를 감지하는 요청입니다.
- [DetectHumanHandPoseRequest](https://developer.apple.com/documentation/vision/detecthumanhandposerequest): 사람 손의 자세를 감지하는 요청입니다.
- [Supporting Pose Types](https://developer.apple.com/documentation/vision/supporting-pose-types): 자세 분석 작업 시 사용하는 타입입니다.
:::

:::topic-grid
## 이미지 분류 및 인식
- [Classifying images for categorization and search](https://developer.apple.com/documentation/vision/classifying-images-for-categorization-and-search): Vision 분류 요청을 사용해 이미지를 분석하고 라벨을 붙입니다.
- [ClassifyImageRequest](https://developer.apple.com/documentation/vision/classifyimagerequest): 이미지를 분류하기 위한 요청입니다.
- [DetectHumanRectanglesRequest](https://developer.apple.com/documentation/vision/detecthumanrectanglesrequest): 이미지에서 사람을 포함한 직사각형 영역을 찾는 요청입니다.
- [RecognizeAnimalsRequest](https://developer.apple.com/documentation/vision/recognizeanimalsrequest): 이미지에서 동물을 인식하는 요청입니다.
:::

:::topic-grid
## 형태 및 가장자리 감지
- [DetectContoursRequest](https://developer.apple.com/documentation/vision/detectcontoursrequest): 이미지 가장자리의 contour를 감지하는 요청입니다.
- [DetectHorizonRequest](https://developer.apple.com/documentation/vision/detecthorizonrequest): 이미지의 수평선 각도를 판별하는 이미지 분석 요청입니다.
- [DetectRectanglesRequest](https://developer.apple.com/documentation/vision/detectrectanglesrequest): 이미지에서 투영된 직사각형 영역을 찾는 이미지 분석 요청입니다.
:::

:::topic-grid
## 이미지 품질 및 saliency 분석
- [Generating high-quality thumbnails from videos](https://developer.apple.com/documentation/vision/generating-thumbnails-from-videos): image-aesthetics score 요청을 사용해 비디오에서 가장 보기 좋은 프레임을 식별합니다.
- [CalculateImageAestheticsScoresRequest](https://developer.apple.com/documentation/vision/calculateimageaestheticsscoresrequest): 이미지의 미적 속성을 분석하는 요청입니다.
- [DetectLensSmudgeRequest](https://developer.apple.com/documentation/vision/detectlenssmudgerequest): 이미지나 비디오 프레임 캡처에서 렌즈 얼룩을 감지하는 요청입니다.
- [GenerateAttentionBasedSaliencyImageRequest](https://developer.apple.com/documentation/vision/generateattentionbasedsaliencyimagerequest): 이미지에서 가장 주의를 끌 가능성이 높은 부분을 식별하는 heat map을 생성하는 객체입니다.
- [GenerateObjectnessBasedSaliencyImageRequest](https://developer.apple.com/documentation/vision/generateobjectnessbasedsaliencyimagerequest): 이미지에서 객체를 나타낼 가능성이 가장 높은 부분을 식별하는 heat map을 생성하는 요청입니다.
:::

:::topic-grid
## 움직임 및 객체 추적
- [DetectTrajectoriesRequest](https://developer.apple.com/documentation/vision/detecttrajectoriesrequest): 포물선 경로를 따라 움직이는 형태의 궤적을 감지하는 요청입니다.
- [TrackObjectRequest](https://developer.apple.com/documentation/vision/trackobjectrequest): 여러 이미지나 비디오 프레임에 걸쳐 이전에 식별한 객체의 움직임을 추적하는 이미지 분석 요청입니다.
- [TrackOpticalFlowRequest](https://developer.apple.com/documentation/vision/trackopticalflowrequest): 이전 이미지에서 현재 이미지로 각 픽셀 벡터의 방향 변화를 판별하는 요청입니다.
- [TrackRectangleRequest](https://developer.apple.com/documentation/vision/trackrectanglerequest): 여러 이미지나 비디오 프레임에 걸쳐 이전에 식별한 직사각형 객체의 움직임을 추적하는 이미지 분석 요청입니다.
:::

:::topic-grid
## 이미지 정합 및 비교
- [GenerateImageFeaturePrintRequest](https://developer.apple.com/documentation/vision/generateimagefeatureprintrequest): 이미지에서 feature print를 생성하는 이미지 기반 요청입니다.
- [TrackHomographicImageRegistrationRequest](https://developer.apple.com/documentation/vision/trackhomographicimageregistrationrequest): 시간에 따라 추적해 두 이미지의 콘텐츠를 정렬하는 데 필요한 perspective warp matrix를 판별하는 이미지 분석 요청입니다.
- [TrackTranslationalImageRegistrationRequest](https://developer.apple.com/documentation/vision/tracktranslationalimageregistrationrequest): 시간에 따라 추적해 두 이미지의 콘텐츠를 정렬하는 데 필요한 affine transform을 판별하는 이미지 분석 요청입니다.
:::

:::topic-grid
## 사용자 정의 Core ML 통합
- [CoreMLRequest](https://developer.apple.com/documentation/vision/coremlrequest): Core ML 모델을 사용해 이미지를 처리하는 이미지 분석 요청입니다.
:::

:::topic-grid
## 프로토콜
- [ImageProcessingRequest](https://developer.apple.com/documentation/vision/imageprocessingrequest): 이미지의 특정 부분에 초점을 맞추는 이미지 분석 요청용 타입입니다.
- [PoseProviding](https://developer.apple.com/documentation/vision/poseproviding): 자세를 구성하는 joint 컬렉션을 제공하는 observation입니다.
- [StatefulRequest](https://developer.apple.com/documentation/vision/statefulrequest): 시간 경과에 따라 조건의 증거를 축적하는 타입용 프로토콜입니다.
- [TargetedRequest](https://developer.apple.com/documentation/vision/targetedrequest): 두 이미지를 함께 분석하기 위한 타입입니다.
- [VisionObservation](https://developer.apple.com/documentation/vision/visionobservation): 이미지 분석 요청이 생성하는 객체용 타입입니다.
- [VisionRequest](https://developer.apple.com/documentation/vision/visionrequest): 이미지 분석 요청용 타입입니다.
:::

:::topic-grid
## 요청 핸들러
- [ImageRequestHandler](https://developer.apple.com/documentation/vision/imagerequesthandler): 단일 이미지에 대한 하나 이상의 이미지 분석 요청을 처리하는 객체입니다.
- [TargetedImageRequestHandler](https://developer.apple.com/documentation/vision/targetedimagerequesthandler): 두 이미지에 대해 이미지 분석 요청을 수행하는 객체입니다.
- [VideoProcessor](https://developer.apple.com/documentation/vision/videoprocessor): 비디오 콘텐츠의 오프라인 분석을 수행하는 객체입니다.
:::

:::topic-grid
## 이미지 위치 및 영역
- [NormalizedPoint](https://developer.apple.com/documentation/vision/normalizedpoint): 2D 좌표계의 한 점입니다.
- [NormalizedRect](https://developer.apple.com/documentation/vision/normalizedrect): 사각형의 위치와 크기입니다.
- [NormalizedRegion](https://developer.apple.com/documentation/vision/normalizedregion): 정규화된 점들로 구성된 다각형입니다.
- [NormalizedCircle](https://developer.apple.com/documentation/vision/normalizedcircle): 2D 원의 중심점과 반지름입니다.
- [BoundingBoxProviding](https://developer.apple.com/documentation/vision/boundingboxproviding): bounding box를 가진 객체용 프로토콜입니다.
- [BoundingRegionProviding](https://developer.apple.com/documentation/vision/boundingregionproviding): 이미지 안에 정의된 경계를 가진 객체용 프로토콜입니다.
- [QuadrilateralProviding](https://developer.apple.com/documentation/vision/quadrilateralproviding): bounding quadrilateral을 가진 객체용 프로토콜입니다.
- [CoordinateOrigin](https://developer.apple.com/documentation/vision/coordinateorigin): 이미지에 대한 좌표계 원점입니다.
:::

:::topic-grid
## 오류
- [VisionError](https://developer.apple.com/documentation/vision/visionerror): 프레임워크가 생성하는 오류입니다.
:::

:::topic-grid
## 레거시 API
- [Original Objective-C and Swift API](https://developer.apple.com/documentation/vision/original-objective-c-and-swift-api)
:::
