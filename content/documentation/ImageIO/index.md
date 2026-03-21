---
route: /documentation/ImageIO
source_url: https://developer.apple.com/documentation/ImageIO
source_locale: en-US
section: docc
content_type: symbol
title: Image I/O
original_title: Image I/O
source_hash: d8b7f5dbcf09a20aa4c89c369172d6921e0ec2232b1d5e66f61ae971433596cc
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:36:26+00:00'
last_translated_at: '2026-03-14T01:03:00+09:00'
---

# Image I/O

대부분의 이미지 파일 형식을 읽고 쓰며, 이미지의 metadata에 접근합니다.

## 개요

Image I/O 프레임워크는 앱이 대부분의 이미지 파일 형식을 읽고 쓸 수 있게 합니다. 이 프레임워크는 높은 효율성, 색상 관리, 이미지 metadata 접근 기능을 제공합니다.

자세한 내용은 [Image I/O Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageIOGuide/imageio_intro/ikpg_intro.html#//apple_ref/doc/uid/TP40005462)를 참고하십시오.

:::topic-grid
## 이미지 관리
- [CGImageSource](https://developer.apple.com/documentation/imageio/cgimagesource): URL, data object, data consumer에서 이미지 데이터를 읽을 때 사용하는 opaque type입니다.
- [CGImageDestination](https://developer.apple.com/documentation/imageio/cgimagedestination): URL, data object, data consumer에 이미지 데이터를 쓸 때 사용하는 opaque type입니다.
:::

:::topic-grid
## XMP Metadata
- [CGImageMetadata](https://developer.apple.com/documentation/imageio/cgimagemetadata): 이미지와 연결된 XMP metadata를 담는 불변 객체입니다.
- [CGMutableImageMetadata](https://developer.apple.com/documentation/imageio/cgmutableimagemetadata): 이미지 metadata를 추가하거나 수정하기 위한 opaque type입니다.
- [CGImageMetadataTag](https://developer.apple.com/documentation/imageio/cgimagemetadatatag): 하나의 이미지 metadata 정보를 담는 불변 타입입니다.
- [XMP Namespaces and Prefixes](https://developer.apple.com/documentation/imageio/xmp-namespaces-and-prefixes): XMP metadata tag에 존재하는 공개 namespace와 prefix를 알아봅니다.
- [kCFErrorDomainCGImageMetadata](https://developer.apple.com/documentation/imageio/kcferrordomaincgimagemetadata): Image I/O 프레임워크에서 발생한 metadata 관련 오류의 도메인입니다.
- [CGImageMetadataErrors](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors): metadata 정보를 가져오거나 설정할 때 발생하는 오류 상수입니다.
:::

:::topic-grid
## 공통 이미지 속성
- [Image Properties](https://developer.apple.com/documentation/imageio/image-properties): 컨테이너 전체에 적용되는 속성으로, 반드시 컨테이너 안의 개별 이미지에만 한정되지는 않습니다.
- [EXIF Dictionary Keys](https://developer.apple.com/documentation/imageio/exif-dictionary-keys): Exchangeable Image File Format(EXIF) 데이터용 metadata 키입니다.
- [IPTC Dictionary Keys](https://developer.apple.com/documentation/imageio/iptc-dictionary-keys): International Press Telecommunications Council(IPTC) 데이터용 metadata 키입니다.
- [GPS Dictionary Keys](https://developer.apple.com/documentation/imageio/gps-dictionary-keys): Global Positioning System(GPS) 정보용 키입니다.
- [WebP Data](https://developer.apple.com/documentation/imageio/webp-data): WebP metadata용 키입니다.
:::

:::topic-grid
## 형식별 속성
- [CIFF Image Properties](https://developer.apple.com/documentation/imageio/ciff-image-properties): Camera Image File Format(CIFF) 이미지 형식용 metadata 키입니다.
- [DNG Image Properties](https://developer.apple.com/documentation/imageio/dng-image-properties): Digital Negative(DNG) 보관 형식용 metadata 키입니다.
- [GIF Image Properties](https://developer.apple.com/documentation/imageio/gif-image-properties): Graphics Interchange Format(GIF)용 metadata 키입니다.
- [HEIC Image Properties](https://developer.apple.com/documentation/imageio/heic-image-properties): High Efficiency Image Container(HEIC) 형식용 metadata 키입니다.
- [JFIF Image Properties](https://developer.apple.com/documentation/imageio/jfif-image-properties): JPEG File Interchange Format(JFIF)용 metadata 키입니다.
- [PNG Image Properties](https://developer.apple.com/documentation/imageio/png-image-properties): Portable Network Graphics(PNG) 형식용 metadata 키입니다.
- [TGA Image Properties](https://developer.apple.com/documentation/imageio/tga-image-properties): Truevision Graphics Adapter(TGA) 형식용 metadata 키입니다.
- [TIFF Image Properties](https://developer.apple.com/documentation/imageio/tiff-image-properties): Tagged Image File Format(TIFF)용 metadata 키입니다.
- [8BIM Image Properties](https://developer.apple.com/documentation/imageio/8bim-image-properties): Adobe Photoshop 이미지 형식용 metadata 키입니다.
:::

:::topic-grid
## 제조사별 속성
- [Nikon Camera Dictionary Keys](https://developer.apple.com/documentation/imageio/nikon-camera-dictionary-keys): Nikon 카메라 이미지용 metadata 키입니다.
- [Canon Camera Dictionary Keys](https://developer.apple.com/documentation/imageio/canon-camera-dictionary-keys): Canon 카메라 이미지용 metadata 키입니다.
- [kCGImagePropertyMakerAppleDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerappledictionary): Apple 카메라 이미지용 키-값 쌍 dictionary입니다.
- [kCGImagePropertyMakerMinoltaDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerminoltadictionary): Minolta 카메라 이미지용 키-값 쌍 dictionary입니다.
- [kCGImagePropertyMakerFujiDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerfujidictionary): Fuji 카메라 이미지용 키-값 쌍 dictionary입니다.
- [kCGImagePropertyMakerOlympusDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerolympusdictionary): Olympus 카메라 이미지용 키-값 쌍 dictionary입니다.
- [kCGImagePropertyMakerPentaxDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerpentaxdictionary): Pentax 카메라 이미지용 키-값 쌍 dictionary입니다.
- [kCGImagePropertyRawDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertyrawdictionary): 최소한으로 처리된 raw 데이터를 담는 이미지용 키-값 쌍 dictionary입니다.
:::

:::topic-grid
## Spatial photo
- [Writing spatial photos](https://developer.apple.com/documentation/imageio/writing-spatial-photos): 관련 spatial metadata가 포함된 stereo HEIC 파일로 좌우안 이미지 한 쌍을 패키징해 visionOS용 spatial photo를 만듭니다.
- [Creating spatial photos and videos with spatial metadata](https://developer.apple.com/documentation/imageio/creating-spatial-photos-and-videos-with-spatial-metadata): stereo 사진과 비디오에 spatial metadata를 추가해 Apple Vision Pro에서 볼 수 있는 spatial media를 만듭니다.
:::

:::topic-grid
## 애니메이션
- [CGAnimateImageAtURLWithBlock(_:_:_:)](https://developer.apple.com/documentation/imageio/cganimateimageaturlwithblock(_:_:_:)): 지정한 URL의 Graphics Interchange Format(GIF) 또는 Animated Portable Network Graphics(APNG) 파일에 들어 있는 이미지 시퀀스를 애니메이션으로 재생합니다.
- [CGAnimateImageDataWithBlock(_:_:_:)](https://developer.apple.com/documentation/imageio/cganimateimagedatawithblock(_:_:_:)): Graphics Interchange Format(GIF) 또는 Animated Portable Network Graphics(APNG) 파일의 데이터를 사용해 이미지 시퀀스를 애니메이션으로 재생합니다.
- [CGImageSourceAnimationBlock](https://developer.apple.com/documentation/imageio/cgimagesourceanimationblock): 이미지 애니메이션의 각 프레임마다 실행할 block입니다.
- [kCGImageAnimationStartIndex](https://developer.apple.com/documentation/imageio/kcgimageanimationstartindex): 애니메이션 첫 프레임의 인덱스를 지정하는 속성입니다.
- [kCGImageAnimationDelayTime](https://developer.apple.com/documentation/imageio/kcgimageanimationdelaytime): 애니메이션 시퀀스에서 다음 이미지를 표시하기 전에 기다릴 초 수입니다.
- [kCGImageAnimationLoopCount](https://developer.apple.com/documentation/imageio/kcgimageanimationloopcount): 애니메이션 시퀀스를 반복할 횟수입니다.
- [CGImageAnimationStatus](https://developer.apple.com/documentation/imageio/cgimageanimationstatus): 이미지 시퀀스 애니메이션 결과를 나타내는 상수입니다.
:::

:::topic-grid
## 참고 자료
- [Image I/O Constants](https://developer.apple.com/documentation/imageio/image-i-o-constants)
- [Image I/O Functions](https://developer.apple.com/documentation/imageio/image-i-o-functions)
- [Image I/O Macros](https://developer.apple.com/documentation/imageio/image-i-o-macros)
:::

:::topic-grid
## 변수
- [kCGComputeHDRStats](https://developer.apple.com/documentation/imageio/kcgcomputehdrstats)
- [kCGImageDestinationEncodeAlternateColorSpace](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodealternatecolorspace)
- [kCGImageDestinationEncodeBaseColorSpace](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodebasecolorspace)
- [kCGImageDestinationEncodeBaseIsSDR](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodebaseissdr)
- [kCGImageDestinationEncodeBasePixelFormatRequest](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodebasepixelformatrequest)
- [kCGImageDestinationEncodeGainMapPixelFormatRequest](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodegainmappixelformatrequest)
- [kCGImageDestinationEncodeGainMapSubsampleFactor](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodegainmapsubsamplefactor)
- [kCGImageDestinationEncodeGenerateGainMapWithBaseImage](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodegenerategainmapwithbaseimage)
- [kCGImageDestinationEncodeIsBaseImage](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodeisbaseimage)
- [kCGImageDestinationEncodeRequest](https://developer.apple.com/documentation/imageio/kcgimagedestinationencoderequest)
- [kCGImageDestinationEncodeRequestOptions](https://developer.apple.com/documentation/imageio/kcgimagedestinationencoderequestoptions)
- [kCGImageDestinationEncodeToISOGainmap](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodetoisogainmap)
- [kCGImageDestinationEncodeToISOHDR](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodetoisohdr)
- [kCGImageDestinationEncodeToSDR](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodetosdr)
- [kCGImageDestinationEncodeTonemapMode](https://developer.apple.com/documentation/imageio/kcgimagedestinationencodetonemapmode)
- [kCGImagePropertyASTCBlockSize](https://developer.apple.com/documentation/imageio/kcgimagepropertyastcblocksize)
- [kCGImagePropertyASTCBlockSize4x4](https://developer.apple.com/documentation/imageio/kcgimagepropertyastcblocksize4x4)
- [kCGImagePropertyASTCBlockSize8x8](https://developer.apple.com/documentation/imageio/kcgimagepropertyastcblocksize8x8)
- [kCGImagePropertyASTCEncoder](https://developer.apple.com/documentation/imageio/kcgimagepropertyastcencoder)
- [kCGImagePropertyBCEncoder](https://developer.apple.com/documentation/imageio/kcgimagepropertybcencoder)
- [kCGImagePropertyBCFormat](https://developer.apple.com/documentation/imageio/kcgimagepropertybcformat)
- [kCGImagePropertyEncoder](https://developer.apple.com/documentation/imageio/kcgimagepropertyencoder)
- [kCGImagePropertyOpenEXRCompression](https://developer.apple.com/documentation/imageio/kcgimagepropertyopenexrcompression)
- [kCGImagePropertyPVREncoder](https://developer.apple.com/documentation/imageio/kcgimagepropertypvrencoder)
- [kCGImageProviderPreferredTileHeight](https://developer.apple.com/documentation/imageio/kcgimageproviderpreferredtileheight)
- [kCGImageProviderPreferredTileWidth](https://developer.apple.com/documentation/imageio/kcgimageproviderpreferredtilewidth)
- [kCGImageSourceGenerateImageSpecificLumaScaling](https://developer.apple.com/documentation/imageio/kcgimagesourcegenerateimagespecificlumascaling)
:::
