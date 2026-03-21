---
route: /documentation/CoreMediaIO
source_url: https://developer.apple.com/documentation/CoreMediaIO
source_locale: en-US
section: docc
content_type: symbol
title: Core Media I/O
original_title: Core Media I/O
source_hash: 4e284b9a7040e51eb9ab9590cf1a2c0e5be6cb116a734c40b83f7fb2b2a64bae
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:23:47+00:00'
last_translated_at: '2026-03-13T23:24:01+09:00'
---

# Core Media I/O

macOS에서 사용자 정의 카메라 기기를 안전하게 지원합니다.

## 개요

Core Media I/O 프레임워크를 사용하면 macOS에서 사용자 정의 카메라 기기를 지원할 수 있습니다. macOS 12.3부터 이 프레임워크는 [System Extensions](https://developer.apple.com/documentation/SystemExtensions)를 기반으로 동작하여, 시스템의 개인정보 보호와 보안 보호를 유지하면서도 사용자 정의 기기를 지원할 수 있게 합니다. 시스템은 앱이 자신의 프로세스 안으로 extension 코드를 로드하지 못하게 하여, macOS의 개인정보 보호를 우회하거나 자신의 정체를 숨기지 못하도록 합니다.

:::important Important
Apple은 기존 Device Abstraction Layer(DAL) plug-in을 Core Media I/O extension으로 교체할 것을 권장합니다.
:::

:::topic-grid
## Provider
- [Creating a camera extension with Core Media I/O](https://developer.apple.com/documentation/coremediaio/creating-a-camera-extension-with-core-media-i-o): 안전하고 배포가 쉬운 고성능 카메라 드라이버를 구축합니다.
- [Overriding the default USB video class extension](https://developer.apple.com/documentation/coremediaio/overriding-the-default-usb-video-class-extension): USB 기기에 대한 기본 드라이버 매칭 동작을 재정의하는 간단한 DriverKit extension을 만듭니다.
- [CMIOExtensionProvider](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider): provider의 기기 연결을 관리하는 객체입니다.
- [CMIOExtensionProviderSource](https://developer.apple.com/documentation/coremediaio/cmioextensionprovidersource): provider source 역할을 하는 객체를 위한 protocol입니다.
- [CMIOExtensionProviderProperties](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties): extension provider의 속성을 관리하는 객체입니다.
:::

:::topic-grid
## 기기
- [CMIOExtensionDevice](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice): 물리 또는 가상 기기를 나타내는 객체입니다.
- [CMIOExtensionDeviceSource](https://developer.apple.com/documentation/coremediaio/cmioextensiondevicesource): device source 역할을 하는 객체를 위한 protocol입니다.
- [CMIOExtensionDeviceProperties](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties): 기기의 속성을 정의하는 객체입니다.
:::

:::topic-grid
## 스트림
- [CMIOExtensionStream](https://developer.apple.com/documentation/coremediaio/cmioextensionstream): 미디어 데이터 스트림을 나타내는 객체입니다.
- [CMIOExtensionStreamSource](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource): stream source 역할을 하는 객체를 위한 protocol입니다.
- [CMIOExtensionStreamProperties](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties): extension stream의 속성을 설명하는 객체입니다.
- [CMIOExtensionClient](https://developer.apple.com/documentation/coremediaio/cmioextensionclient): extension의 client를 나타내는 객체입니다.
:::

:::topic-grid
## 속성
- [CMIOExtensionProperty](https://developer.apple.com/documentation/coremediaio/cmioextensionproperty): provider, device, stream이 지원하는 속성을 정의하는 구조체입니다.
- [CMIOExtensionPropertyState](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertystate): 속성의 상태를 설명하는 객체입니다.
- [CMIOExtensionPropertyAttributes](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertyattributes): 속성의 attribute를 설명하는 객체입니다.
- [CMIOExtensionInfoDictionaryKey](https://developer.apple.com/documentation/coremediaio/cmioextensioninfodictionarykey): extension 정보 dictionary를 지정하는 키입니다.
- [CMIOExtensionMachServiceNameKey](https://developer.apple.com/documentation/coremediaio/cmioextensionmachservicenamekey): mach service 이름을 지정하는 키입니다.
:::

:::topic-grid
## DAL Plug-In
- [Device Abstraction Layer (DAL) Plug-Ins](https://developer.apple.com/documentation/coremediaio/device-abstraction-layer-dal-plug-ins): 기존 DAL plug-in에 대한 API 참조입니다.
:::
