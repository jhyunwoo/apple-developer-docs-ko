---
route: /documentation/USBDriverKit
source_url: https://developer.apple.com/documentation/USBDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: USBDriverKit
original_title: USBDriverKit
source_hash: d32ea2f5b33111d7a36c2a210fdc6aed37667cb5c16a020b33b4f55936ba8a9f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:23:48+00:00'
last_translated_at: '2026-03-13T23:24:01+09:00'
---

# USBDriverKit

USB 기반 기기를 위한 드라이버를 개발합니다.

## 개요

[USBDriverKit](https://developer.apple.com/documentation/usbdriverkit) 프레임워크를 사용하면 macOS용 사용자 정의 USB 기기 또는 클래스 규격을 따르지 않는 USB 기기를 위한 드라이버를 개발할 수 있습니다. 이 프레임워크의 객체는 드라이버를 위한 provider 역할을 합니다. 이 객체를 그대로 사용해 USB 기기의 구성, 인터페이스, endpoint에 접근할 수 있습니다. 각 객체는 USB 기기에서 필요한 descriptor를 가져오고, 드라이버 고유 동작을 수행하기 위한 요청을 시작하는 메서드를 제공합니다.

드라이버는 [DriverKit](https://developer.apple.com/documentation/DriverKit) 프레임워크의 [IOService](https://developer.apple.com/documentation/DriverKit/IOService)를 하위 클래스화해 개발합니다. macOS에서는 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용해 드라이버를 설치하고 업그레이드합니다. iPadOS에서는 시스템이 호스트 앱과 함께 드라이버를 자동으로 발견하고 업그레이드합니다.

:::note Note
USBDriverKit은 Intel 및 Apple Silicon 기반 macOS 기기, 그리고 M 시리즈 칩을 탑재한 iPadOS 기기에서 사용할 수 있습니다.
:::

:::topic-grid
## 핵심
- [com.apple.developer.driverkit.transport.usb](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.transport.usb): 드라이버가 지원하는 USB 기기를 식별하는 dictionary 배열입니다.
:::

:::topic-grid
## 샘플
- [DriverKit sample code](https://developer.apple.com/documentation/DriverKit/driverkit-sample-code): DriverKit 계열 프레임워크로 macOS 기기 드라이버를 작성하는 방법을 보여 주는 프로젝트를 살펴봅니다.
:::

:::topic-grid
## Provider
- [IOUSBHostInterface](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface): USB 기기의 인터페이스와 상호 작용을 관리하는 provider 객체입니다.
- [IOUSBHostDevice](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice): USB 기기를 나타내는 provider 객체입니다.
:::

:::topic-grid
## Endpoint 통신
- [IOUSBHostPipe](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe): USB endpoint와 데이터를 주고받을 때 사용하는 객체입니다.
:::

:::topic-grid
## USB 사양
- [USB Device Descriptors](https://developer.apple.com/documentation/usbdriverkit/usb-device-descriptors): USB 사양의 descriptor를 사용해 기기의 capability와 구성을 판단합니다.
- [Additional Specifications](https://developer.apple.com/documentation/usbdriverkit/additional-specifications): 기기에서 정보를 요청하고 하드웨어 및 타이밍 정보를 얻습니다.
- [Registry Property Names](https://developer.apple.com/documentation/usbdriverkit/registry-property-names): 기기 registry 안에서 특정 키를 찾습니다.
- [Utilities](https://developer.apple.com/documentation/usbdriverkit/utilities): 비트 구조를 조작하고 정수를 기기 고유 형식과 플랫폼 기본 형식 사이에서 변환합니다.
:::

:::topic-grid
## 참고 자료
- [USBDriverKit Enumerations](https://developer.apple.com/documentation/usbdriverkit/usbdriverkit-enumerations)
- [USBDriverKit Functions](https://developer.apple.com/documentation/usbdriverkit/usbdriverkit-functions)
- [USBDriverKit Data Types](https://developer.apple.com/documentation/usbdriverkit/usbdriverkit-data-types)
- [USBDriverKit Macros](https://developer.apple.com/documentation/usbdriverkit/usbdriverkit-macros)
:::

:::topic-grid
## 매크로
- [IOUSBHOST_PROPERTY_DEPRECATED](https://developer.apple.com/documentation/usbdriverkit/iousbhost_property_deprecated)
- [kUSBHostBillboardDevicePropertyAltModeFailed](https://developer.apple.com/documentation/usbdriverkit/kusbhostbillboarddevicepropertyaltmodefailed)
- [kUSBHostBillboardDevicePropertyAltModePowerFailed](https://developer.apple.com/documentation/usbdriverkit/kusbhostbillboarddevicepropertyaltmodepowerfailed)
- [kUSBHostBillboardDevicePropertyCurrentMode](https://developer.apple.com/documentation/usbdriverkit/kusbhostbillboarddevicepropertycurrentmode)
- [kUSBHostBillboardDevicePropertyModeValueDisplayPort](https://developer.apple.com/documentation/usbdriverkit/kusbhostbillboarddevicepropertymodevaluedisplayport)
- [kUSBHostBillboardDevicePropertyModeValueThunderbolt](https://developer.apple.com/documentation/usbdriverkit/kusbhostbillboarddevicepropertymodevaluethunderbolt)
- [kUSBHostBillboardDevicePropertyModeValueUSB4](https://developer.apple.com/documentation/usbdriverkit/kusbhostbillboarddevicepropertymodevalueusb4)
- [kUSBHostBillboardDevicePropertyPreferredMode](https://developer.apple.com/documentation/usbdriverkit/kusbhostbillboarddevicepropertypreferredmode)
- [kUSBHostBillboardDevicePropertySupportedModes](https://developer.apple.com/documentation/usbdriverkit/kusbhostbillboarddevicepropertysupportedmodes)
- [kUSBHostBillboardDevicePropertyVersion](https://developer.apple.com/documentation/usbdriverkit/kusbhostbillboarddevicepropertyversion)
- [kUSBHostControllerPropertyProtocolRevision](https://developer.apple.com/documentation/usbdriverkit/kusbhostcontrollerpropertyprotocolrevision)
- [kUSBHostDevicePropertyIdlePolicy](https://developer.apple.com/documentation/usbdriverkit/kusbhostdevicepropertyidlepolicy)
- [kUSBHostDevicePropertyPowerSinkAllocation](https://developer.apple.com/documentation/usbdriverkit/kusbhostdevicepropertypowersinkallocation)
- [kUSBHostDevicePropertyUSB3Preferred](https://developer.apple.com/documentation/usbdriverkit/kusbhostdevicepropertyusb3preferred)
- [kUSBHostDevicePropertyUSB3Required](https://developer.apple.com/documentation/usbdriverkit/kusbhostdevicepropertyusb3required)
- [kUSBHostPortPropertyIOPortServicePath](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyioportservicepath)
- [kUSBHostPortPropertyProtocolCompanionRevision1](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyprotocolcompanionrevision1)
- [kUSBHostPortPropertyProtocolCompanionRevision2](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyprotocolcompanionrevision2)
- [kUSBHostPortPropertyProtocolCompanionRevision3](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyprotocolcompanionrevision3)
- [kUSBHostPortPropertyProtocolRevision1](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyprotocolrevision1)
- [kUSBHostPortPropertyProtocolRevision2](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyprotocolrevision2)
- [kUSBHostPortPropertyProtocolRevision3](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyprotocolrevision3)
- [kUSBHostPortPropertyProtocolRevision4](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyprotocolrevision4)
- [kUSBHostPortPropertyTransportState](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertytransportstate)
- [kUSBHostPortPropertyUSB2ExternalRemoteWake](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyusb2externalremotewake)
- [kUSBHostPortPropertyUSB2Repeater](https://developer.apple.com/documentation/usbdriverkit/kusbhostportpropertyusb2repeater)
- [kUSBHostPropertyLinkSpeed](https://developer.apple.com/documentation/usbdriverkit/kusbhostpropertylinkspeed)
:::

:::topic-grid
## 열거형 케이스
- [kIOUSBLinkSpeed10Gbps](https://developer.apple.com/documentation/usbdriverkit/kiousblinkspeed10gbps)
- [kIOUSBLinkSpeed20Gbps](https://developer.apple.com/documentation/usbdriverkit/kiousblinkspeed20gbps)
- [kIOUSBLinkSpeed40Gbps](https://developer.apple.com/documentation/usbdriverkit/kiousblinkspeed40gbps)
- [kIOUSBLinkSpeed5Gbps](https://developer.apple.com/documentation/usbdriverkit/kiousblinkspeed5gbps)
- [kIOUSBLinkSpeed80Gbps](https://developer.apple.com/documentation/usbdriverkit/kiousblinkspeed80gbps)
- [kIOUSBLinkSpeedFull](https://developer.apple.com/documentation/usbdriverkit/kiousblinkspeedfull)
- [kIOUSBLinkSpeedHigh](https://developer.apple.com/documentation/usbdriverkit/kiousblinkspeedhigh)
- [kIOUSBLinkSpeedLow](https://developer.apple.com/documentation/usbdriverkit/kiousblinkspeedlow)
:::

:::topic-grid
## 열거형
- [tIOUSB40LinkStateTimeout](https://developer.apple.com/documentation/usbdriverkit/tiousb40linkstatetimeout)
:::
