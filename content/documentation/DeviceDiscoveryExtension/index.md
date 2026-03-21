---
route: /documentation/DeviceDiscoveryExtension
source_url: https://developer.apple.com/documentation/DeviceDiscoveryExtension
source_locale: en-US
section: docc
content_type: symbol
title: DeviceDiscoveryExtension
original_title: DeviceDiscoveryExtension
source_hash: 5ee0dc2abcadf700cfaf908f757de0caed2c0dda175b2aa29ef7d116f326432d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:15:00+00:00'
last_translated_at: '2026-03-13T16:45:00+09:00'
---

# DeviceDiscoveryExtension

사용자가 시스템 메뉴에서 선택한 서드파티 장치로 미디어를 스트리밍합니다.

## 개요

DeviceDiscoveryExtension(DDE)을 사용하면 앱이 AV 콘텐츠를 스트리밍할 수 있는 서드파티 미디어 수신기를 검색할 수 있습니다.

사용자가 앱의 미디어 스트리밍 UI를 호출하면 route picker view([AVRoutePickerView](https://developer.apple.com/documentation/AVKit/AVRoutePickerView))에서 서드파티 장치, 로컬 네트워크 장치, Bluetooth 장치를 스트리밍 대상지로 제공할 수 있습니다. 아래 그림은 검색 과정에 참여하는 주체를 보여 줍니다. 그림의 System 섹션에서 보이듯이, view가 표시되면 앱의 device discovery extension이 로드됩니다.

![왼쪽에서 오른쪽으로 사용자, 앱, 시스템, 서드파티 장치가 있는 흐름도입니다. 각 상자 아래로 채널을 나타내는 선이 내려가고, 사용자가 기능을 호출한 시점부터 서드파티 장치가 미디어를 재생할 때까지의 검색 과정 여러 단계가 채널 사이를 오가는 화살표로 표시됩니다.](https://developer.apple.com)

extension이 로드되면 다음과 같이 동작합니다.

- extension은 시스템 프로세스 안에서 실행되며 로컬 네트워크와 Bluetooth 장치에서 특정 미디어 수신기를 검색합니다.
- extension이 장치를 찾으면 시스템에 해당 장치를 반환하고, 시스템은 이를 picker view에서 사용 가능한 옵션으로 표시합니다.
- 사용자가 장치를 선택하면 시스템이 선택된 장치를 앱에 전달하고, 앱은 그 장치로 미디어를 스트리밍할 수 있습니다.

DDE는 시스템 sandbox 안에서 실행되므로 extension이 로컬 네트워크나 Bluetooth 권한을 사용자에게 요청할 필요가 없습니다. picker view는 검색된 서드파티 장치와 프로토콜을 AirPlay와 같은 시스템 메뉴 안에 함께 표시하므로 통합된 장치 선택 경험을 제공합니다.

:::note Note
직접 제조하지 않은 서드파티 장치로 스트리밍하려면 제조사가 SDK의 일부로 제공하는 device discovery extension을 앱과 함께 번들로 포함하십시오.
:::

:::topic-grid
## 핵심 사항
- [Discovering a third-party media-streaming device](https://developer.apple.com/documentation/devicediscoveryextension/discovering-a-third-party-media-streaming-device): iOS 또는 macOS의 서버 앱으로 미디어를 스트리밍하는 extension을 빌드합니다.
- [Media Device Discovery Extension](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.media-device-discovery-extension): 특정 서드파티 미디어 수신기를 시스템 장치 picker UI에 추가하는 app extension용 entitlement입니다.
:::

:::topic-grid
## extension
- [DDDiscoveryExtension](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextension): 프레임워크가 extension의 검색 프로세스를 시작하고 중지할 수 있게 해 주는 명세입니다.
- [DDDiscoverySession](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoverysession): extension에서 시스템으로 장치 검색 이벤트를 전달하는 객체입니다.
- [DDDiscoveryExtensionConfigurationProtocol](https://developer.apple.com/documentation/devicediscoveryextension/dddiscoveryextensionconfigurationprotocol): extension과 프레임워크 사이에 통신 채널을 제공하는 명세입니다.
:::

:::topic-grid
## 생명주기
- [DDDeviceEvent](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceevent): 장치를 제공하거나 장치 상태 변화를 전달하는 객체입니다.
- [DDDeviceEvent.EventType](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceevent/eventtype-swift.enum): 장치 검색 생명주기에서 발생하는 이벤트 유형 식별자입니다.
- [DDEventTypeToString(_:)](https://developer.apple.com/documentation/devicediscoveryextension/ddeventtypetostring(_:)): 지정한 이벤트 식별자에 대한 사람이 읽을 수 있는 텍스트를 반환합니다.
- [DDEventHandler](https://developer.apple.com/documentation/devicediscoveryextension/ddeventhandler): extension이 이벤트를 알리기 위해 호출하는 함수입니다.
:::

:::topic-grid
## 장치 정보
- [DDDevice](https://developer.apple.com/documentation/devicediscoveryextension/dddevice): 관심 있는 검색 장치를 설명하는 객체입니다.
- [DDDevice.Category](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/category-swift.enum): picker UI에서 장치 아이콘을 결정하는 옵션입니다.
- [DDDeviceState](https://developer.apple.com/documentation/devicediscoveryextension/dddevicestate): 사용자가 장치와 상호 작용하는 수준을 나타내는 상태입니다.
- [DDDeviceCategoryToString(_:)](https://developer.apple.com/documentation/devicediscoveryextension/dddevicecategorytostring(_:)): 장치 카테고리를 설명하는 지정 식별자에 대한 사람이 읽을 수 있는 텍스트를 반환합니다.
- [DDDeviceStateToString(_:)](https://developer.apple.com/documentation/devicediscoveryextension/dddevicestatetostring(_:)): 장치 상태를 설명하는 지정 식별자에 대한 사람이 읽을 수 있는 텍스트를 반환합니다.
- [DDDevice.Protocol](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/protocol-swift.enum): 앱이 장치와 상호 작용하는 방식을 나타내는 식별자입니다.
- [DDDeviceProtocolToString(_:)](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceprotocoltostring(_:)): 지정한 프로토콜 식별자에 대한 사람이 읽을 수 있는 텍스트를 반환합니다.
- [DDDeviceProtocolString](https://developer.apple.com/documentation/devicediscoveryextension/dddeviceprotocolstring): 앱이 장치와 상호 작용하는 방식에 대한 문자열 값입니다.
- [DDDeviceMediaPlaybackStateToString(_:)](https://developer.apple.com/documentation/devicediscoveryextension/dddevicemediaplaybackstatetostring(_:)): 지정한 미디어 재생 상태에 대한 사람이 읽을 수 있는 텍스트를 반환합니다.
:::

:::topic-grid
## 오류
- [DDError](https://developer.apple.com/documentation/devicediscoveryextension/dderror): 프레임워크가 보고하는 오류입니다.
- [DDError.Code](https://developer.apple.com/documentation/devicediscoveryextension/dderror/code): 프레임워크 사용 중 발생할 수 있는 오류를 식별하는 코드입니다.
- [DDErrorHandler](https://developer.apple.com/documentation/devicediscoveryextension/dderrorhandler): 작업이 오류를 반환하거나 성공적으로 완료될 때 제공한 코드를 실행하는 함수입니다.
- [DDErrorOutType](https://developer.apple.com/documentation/devicediscoveryextension/dderrorouttype): 오류 참조를 반환하는 프레임워크 함수용 타입입니다.
- [DDErrorDomain](https://developer.apple.com/documentation/devicediscoveryextension/dderrordomain): 프레임워크 전용의 고유 오류 도메인입니다.
:::

:::topic-grid
## 레퍼런스
- [DeviceDiscoveryExtension Enumerations](https://developer.apple.com/documentation/devicediscoveryextension/devicediscoveryextension-enumerations)
:::
