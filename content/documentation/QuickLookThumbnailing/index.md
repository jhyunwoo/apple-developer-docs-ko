---
route: /documentation/QuickLookThumbnailing
source_url: https://developer.apple.com/documentation/QuickLookThumbnailing
source_locale: en-US
section: docc
content_type: symbol
title: Quick Look Thumbnailing
original_title: Quick Look Thumbnailing
source_hash: 8f137979b00954375cdfbc8c6e36bc34d5fd802a1372e3ae5977c6ec9b3e908e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:08:26+00:00'
last_translated_at: '2026-03-14T00:28:00+09:00'
---

# Quick Look Thumbnailing

일반적인 파일 유형의 썸네일을 생성하고, 다른 앱도 사용자 정의 파일의 썸네일을 만들 수 있도록 앱에 Thumbnail Extension을 추가합니다.

## 개요

앱 안에서 파일과 그 내용을 표시하기 위해 파일의 축소 표현, 즉 *thumbnail*을 만들고 싶을 수 있습니다. QuickLookThumbnailing 프레임워크는 [QLThumbnailGenerator](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator) 객체를 사용해 썸네일을 생성하는 API를 제공합니다. 이 프레임워크는 다음을 포함한 일반적인 파일 유형의 썸네일을 생성할 수 있습니다.

- 이미지
- Live Photos
- 텍스트 파일
- PDF
- 오디오 및 비디오 파일
- `usdz` 파일 형식을 사용하는 증강 현실 객체(iOS 및 iPadOS 전용)

많은 앱이 데이터를 저장하기 위해 사용자 정의 파일 유형을 사용합니다. macOS의 Finder와 Spotlight, 운영 체제의 다른 기능, 그리고 다른 앱은 이런 파일에 대해 썸네일 대신 일반적인 파일 아이콘을 표시하는 경우가 많습니다. 하지만 설치된 앱이 해당 사용자 정의 파일 유형을 지원하는 Thumbnail Extension을 구현하면, 운영 체제와 다른 앱은 [QLThumbnailGenerator](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator) 객체를 통해 그 확장을 활용하여 사용자 정의 파일 유형의 풍부한 썸네일을 표시할 수 있습니다. 운영 체제 전체와 타사 앱 전반에서 사용자 정의 파일 유형의 풍부한 썸네일을 사용자에게 제공하려면 앱에 Thumbnail Extension을 추가하십시오.

:::topic-grid
## 썸네일 생성
- [Creating Quick Look Thumbnails to Preview Files in Your App](https://developer.apple.com/documentation/quicklookthumbnailing/creating-quick-look-thumbnails-to-preview-files-in-your-app): 이미지, 텍스트 파일, PDF, 오디오 파일, 비디오 등 다양한 콘텐츠의 썸네일을 생성합니다.
- [QLThumbnailGenerator](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator): 제공된 요구 사항에 따라 썸네일 이미지를 생성하는 객체입니다.
- [QLThumbnailRepresentation](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailrepresentation): thumbnail generator가 반환하는 썸네일에 대한 정보입니다.
:::

:::topic-grid
## 사용자 정의 파일 유형의 썸네일
- [Providing Thumbnails of Your Custom File Types](https://developer.apple.com/documentation/quicklookthumbnailing/providing-thumbnails-of-your-custom-file-types): Thumbnail Extension을 구현해 운영 체제와 다른 앱이 사용자 정의 파일의 썸네일을 표시할 수 있게 합니다.
- [QLThumbnailProvider](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailprovider): 사용자 정의 파일 유형의 썸네일을 만들기 위한 추상 기반 클래스입니다.
- [QLFileThumbnailRequest](https://developer.apple.com/documentation/quicklookthumbnailing/qlfilethumbnailrequest): 사용자 정의 파일 유형의 썸네일 생성을 요청합니다.
- [QLThumbnailReply](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailreply): 사용자 정의 파일 유형의 썸네일을 제공하는 객체입니다.
:::

:::topic-grid
## 오류 정보
- [QLThumbnailErrorDomain](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerrordomain): QuickLookThumbnailing 프레임워크의 오류 도메인입니다.
- [QLThumbnailError](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct): 썸네일 생성 중 반환될 수 있는 오류 정보입니다.
- [QLThumbnailError.Code](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/code): 썸네일 생성 중 반환될 수 있는 오류 코드입니다.
:::
