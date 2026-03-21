---
route: /documentation/CoreHID
source_url: https://developer.apple.com/documentation/CoreHID
source_locale: en-US
section: docc
content_type: symbol
title: Core HID
original_title: Core HID
source_hash: b5a203ddc47dbf41ad17f3703085e96390d8f1e52f01c17b3e5fc542601dff44
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:11:05+00:00'
last_translated_at: '2026-03-13T22:16:00+09:00'
---

# Core HID

키보드, 마우스, 기타 human interface device와 상호 작용합니다.

## 개요

CoreHID 프레임워크는 키보드, 마우스, 기타 장치 같은 human interface device(HID)와의 상호 작용을 쉽게 해 줍니다. 이러한 상호 작용에는 키 입력이나 마우스 클릭처럼 장치가 생성하는 데이터를 받는 작업이 포함됩니다. CoreHID는 LED를 켜 달라는 요청처럼 장치에 요청을 보내는 기능도 제공합니다. 또한 가상 game controller처럼 시스템에 연결된 장치를 에뮬레이션하고, 물리 하드웨어 없이 다른 앱으로 입력을 보낼 수도 있습니다.

![왼쪽에 Swift 로고가 있고, 그 로고에서 세 개의 화살표가 오른쪽으로 뻗어 나갑니다. 첫 번째 화살표는 game controller를, 두 번째는 mouse를, 세 번째는 keyboard를 가리키는 이미지입니다.](https://developer.apple.com)

HID 장치에 대해 더 알아보려면 [USB standards website](https://www.usb.org/hid)를 참고하십시오.

:::topic-grid
## 검색
- [Discovering HID devices from Terminal](https://developer.apple.com/documentation/corehid/discoveringhiddevicesfromterminal): command line에서 Mac에 연결된 장치를 식별합니다.
- [HIDDeviceManager](https://developer.apple.com/documentation/corehid/hiddevicemanager): 시스템에 연결된 human interface device(HID)를 검색하는 도우미입니다.
- [HIDDeviceManager.DeviceMatchingCriteria](https://developer.apple.com/documentation/corehid/hiddevicemanager/devicematchingcriteria): HID 장치를 필터링할 때 사용하는 매칭 기준입니다.
:::

:::topic-grid
## 상호 작용
- [Communicating with human interface devices](https://developer.apple.com/documentation/corehid/communicatingwithhiddevices): 키보드와 마우스 같은 장치와 상호 작용하고 데이터를 얻습니다.
- [HIDDeviceClient](https://developer.apple.com/documentation/corehid/hiddeviceclient): 물리적 또는 가상 HID 호환 주변 장치의 클라이언트입니다.
- [HIDElement](https://developer.apple.com/documentation/corehid/hidelement): HID 장치의 report descriptor 안에 있는 항목 하나를 표현합니다.
- [HIDElementCollection](https://developer.apple.com/documentation/corehid/hidelementcollection): HID 장치의 report descriptor에서 가져온 항목 모음입니다.
- [HIDElement.Value](https://developer.apple.com/documentation/corehid/hidelement/value): HID element와 연관된 데이터입니다.
- [HIDElementUpdate](https://developer.apple.com/documentation/corehid/hidelementupdate): element update 타입을 위한 기본 프로토콜입니다.
- [HIDReportType](https://developer.apple.com/documentation/corehid/hidreporttype): HID report의 타입입니다.
- [HIDReportID](https://developer.apple.com/documentation/corehid/hidreportid): HID report의 report ID를 나타내는 타입입니다.
- [HIDUsage](https://developer.apple.com/documentation/corehid/hidusage): HID usage page를 표현하는 타입입니다.
- [HIDDeviceError](https://developer.apple.com/documentation/corehid/hiddeviceerror): 프레임워크가 던질 수 있는 오류입니다.
- [HIDDeviceTransport](https://developer.apple.com/documentation/corehid/hiddevicetransport): HID 장치로 데이터를 보내거나 장치에서 데이터를 받는 공통 전송 방식입니다.
- [HIDDeviceLocalizationCode](https://developer.apple.com/documentation/corehid/hiddevicelocalizationcode): 일부 HID 장치가 특정 형식이나 언어 준수를 명시하기 위해 선언하는 현지화 코드입니다.
:::

:::topic-grid
## 시뮬레이션
- [Creating virtual devices](https://developer.apple.com/documentation/corehid/creatingvirtualdevices): 테스트와 개발을 위해 가상 human interface device를 사용하고 상호 작용합니다.
- [HIDVirtualDevice](https://developer.apple.com/documentation/corehid/hidvirtualdevice): 시스템에 연결된 HID 장치를 에뮬레이션하는 가상 서비스입니다.
- [HIDVirtualDeviceDelegate](https://developer.apple.com/documentation/corehid/hidvirtualdevicedelegate): 가상 HID 장치에 대한 알림을 받는 delegate입니다.
- [HIDVirtualDevice.Properties](https://developer.apple.com/documentation/corehid/hidvirtualdevice/properties): 가상 HID 장치의 속성입니다.
:::
