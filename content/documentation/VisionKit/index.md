---
route: /documentation/VisionKit
source_url: https://developer.apple.com/documentation/VisionKit
source_locale: en-US
section: docc
content_type: symbol
title: VisionKit
original_title: VisionKit
source_hash: d5689a2c71ee3d8141e9036550945bdb29a61725e34de87ddf3a911d96988b13
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:59:24+00:00'
last_translated_at: '2026-03-14T02:52:00+09:00'
---

# VisionKit

기기의 카메라를 사용하거나 앱이 표시하는 이미지 안에서 환경의 정보를 식별하고 추출합니다.

## 개요

VisionKit은 pixel 정보를 분석해 특정 언어의 텍스트, URL, 도로 주소, 전화번호, 배송 추적 번호, 항공편 번호, 날짜, 시간, 기간, 다양한 형식의 바코드 같은 중요한 데이터를 분리해 냅니다. 이 프레임워크는 앱이 표시하는 사용자 인터페이스를 통해 이 분석 결과를 앱에 제공하며, 사용자는 여기서 분석된 데이터([ImageAnalyzer.AnalysisTypes](https://developer.apple.com/documentation/visionkit/imageanalyzer/analysistypes))와 상호 작용하고 필요한 데이터를 앱으로 다시 전달할 수 있습니다. 이 인터페이스에서 사람들은 데이터를 강조 표시하고, 탭해 초점을 맞추고, clipboard로 복사 및 추출하거나, 앱이 정의한 작업을 실행하는 메뉴 옵션을 호출할 수 있습니다. VisionKit은 다음과 같은 사용자 인터페이스를 제공합니다.

[DataScannerViewController](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller)는 카메라 passthrough view를 표시하여 사용자가 환경 안에 보이는 모든 인식 콘텐츠 유형([DataScannerViewController.RecognizedDataType](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/recognizeddatatype))과 상호 작용할 수 있게 하며, 캡처된 정보를 앱에 제공해 처리할 수 있게 합니다.

이미지 분석 인터페이스([ImageAnalysisInteraction](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction)는 iOS에서, [ImageAnalysisOverlayView](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview)는 macOS에서 사용)는 이미지 위에 표시되며, 프레임워크가 이미지에서 인식한 콘텐츠 유형([ImageAnalysisInteraction.InteractionTypes](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/interactiontypes))과 사용자가 상호 작용할 수 있게 합니다. 예를 들어 Live Text 인터페이스를 사용하면 이미지에 있는 텍스트를 선택([textSelection](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/interactiontypes/textselection))하거나 URL을 실행([dataDetectors](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/interactiontypes/datadetectors))할 수 있습니다. 또한 텍스트 선택 UI는 선택한 텍스트를 복사하거나 더 많은 정보를 위해 웹에서 주제를 조회할 수 있는 프레임워크 표준 버튼을 제공합니다.

![Live Text 버튼과 강조된 텍스트 및 그 작업 메뉴를 보여 주는 iPhone 화면 모형입니다.](https://developer.apple.com)

VisionKit의 Document Camera view controller([VNDocumentCameraViewController](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller))는 사용자가 실제 문서를 스캔할 수 있게 해 주는 카메라 passthrough 경험입니다. 사용자는 이 view 안의 카메라 인터페이스를 탭해 문서를 페이지별로 스캔하고, 스캔이 끝나면 앱은 페이지 번호별 결과 이미지를 받습니다. 이 스캔 이미지 모음을 사용하면 앱은 예를 들어 스캔 이미지를 PDF로 내보내는 방식으로 실제 문서의 디지털 버전을 만들 수 있습니다.

## 이미지 안의 피사체와 상호 작용하기

iOS 17 및 macOS 14 이후 버전에서 VisionKit은 이미지 안의 피사체를 식별합니다([ImageAnalysisInteraction.Subject](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/subject) 참고). *피사체*는 사진의 중심이 되는 객체처럼 이미지의 초점이 되는 대상일 수 있습니다. 또는 프레임워크가 이미지 안에서 인식한 여러 객체를 식별할 수도 있습니다. VisionKit은 앱이 배경이 제거된 별도 이미지로 피사체를 추출하거나, 즉 *들어 올리거나*([image](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/subject/image)), 피사체에 대한 더 많은 정보를 제공하는 버튼([visualLookUp](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/interactiontypes/visuallookup))을 표시할 수 있게 합니다.

:::note Note
macOS 14 및 이후 버전에서는 Mac Catalyst로 빌드한 macOS 앱이 [ImageAnalyzer](https://developer.apple.com/documentation/visionkit/imageanalyzer)와 [ImageAnalysisInteraction](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction) 클래스를 지원합니다.
:::

:::topic-grid
## 이미지 안의 콘텐츠 인식 및 상호 작용
- [Enabling Live Text interactions with images](https://developer.apple.com/documentation/visionkit/enabling-live-text-interactions-with-images): 이미지에 나타나는 텍스트와 QR 코드에 대해 사용자가 동작을 수행할 수 있게 하는 Live Text 인터페이스를 추가합니다.
- [ImageAnalyzer](https://developer.apple.com/documentation/visionkit/imageanalyzer): 피사체, 텍스트, QR 코드처럼 사용자가 상호 작용할 수 있는 항목을 이미지에서 찾는 객체입니다.
- [ImageAnalysis](https://developer.apple.com/documentation/visionkit/imageanalysis): 이미지 분석 결과를 나타내며 Live Text 인터페이스 객체의 입력을 제공하는 객체입니다.
- [ImageAnalysisInteraction](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction): 이미지 안의 인식된 텍스트, 바코드, 기타 객체와 사용자가 상호 작용할 수 있게 하는 인터페이스입니다.
- [ImageAnalysisInteractionDelegate](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate): 상호 작용 객체에 대한 이미지 분석 및 사용자 상호 작용 callback을 처리하는 delegate입니다.
- [ImageAnalysisOverlayView](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayview): 이미지 안의 인식된 텍스트, 바코드, 기타 객체와 사용자가 상호 작용할 수 있게 하는 view입니다.
- [ImageAnalysisOverlayViewDelegate](https://developer.apple.com/documentation/visionkit/imageanalysisoverlayviewdelegate): overlay view에 대한 이미지 분석 및 사용자 상호 작용 callback을 처리하는 delegate입니다.
- [CameraRegionView](https://developer.apple.com/documentation/visionkit/cameraregionview): 사용자의 시야 안에서 안정화된 관심 영역을 표시하고 선택된 그 영역에 대한 passthrough 카메라 피드를 제공하는 view입니다.
:::

:::topic-grid
## 카메라를 통한 바코드 및 텍스트 스캔
- [Scanning data with the camera](https://developer.apple.com/documentation/visionkit/scanning-data-with-the-camera): 카메라 viewfinder에 나타나는 텍스트와 코드를 Live Text 데이터 스캔으로 처리할 수 있게 합니다.
- [DataScannerViewController](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller): 카메라 live video에서 텍스트, 텍스트 속 데이터, 기계 판독 코드를 스캔하는 객체입니다.
- [DataScannerViewControllerDelegate](https://developer.apple.com/documentation/visionkit/datascannerviewcontrollerdelegate): data scanner가 인식한 항목과 사용자가 상호 작용할 때 응답하는 delegate 객체입니다.
- [RecognizedItem](https://developer.apple.com/documentation/visionkit/recognizeditem): data scanner가 카메라 live video 안에서 인식한 항목입니다.
:::

:::topic-grid
## 카메라를 통한 문서 스캔
- [Structuring Recognized Text on a Document](https://developer.apple.com/documentation/visionkit/structuring_recognized_text_on_a_document): Vision 및 VisionKit을 사용해 명함이나 영수증 위의 텍스트를 감지, 인식, 구조화합니다.
- [VNDocumentCameraViewController](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller): 사람들이 실제 문서를 스캔할 수 있도록 도와주는 카메라 passthrough UI를 표시하는 객체입니다.
- [VNDocumentCameraViewControllerDelegate](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontrollerdelegate): document camera가 스캔 결과를 반환할 때 사용하는 delegate protocol입니다.
- [VNDocumentCameraScan](https://developer.apple.com/documentation/visionkit/vndocumentcamerascan): document camera에서 스캔한 단일 문서입니다.
:::
