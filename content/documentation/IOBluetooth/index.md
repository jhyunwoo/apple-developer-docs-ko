---
route: /documentation/IOBluetooth
source_url: https://developer.apple.com/documentation/IOBluetooth
source_locale: en-US
section: docc
content_type: symbol
title: IOBluetooth
original_title: IOBluetooth
source_hash: df85240f6972aff32c858ab77fa95cbc8cc1044f94d620cd82b1939f7721149c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:15:09+00:00'
last_translated_at: '2026-03-14T00:54:00+09:00'
---

# IOBluetooth

Bluetooth 장치에 대해 사용자 공간 접근을 얻습니다.

## 개요

Bluetooth 프레임워크는 C와 Objective-C API를 모두 포함하여 Bluetooth 장치에 대한 사용자 공간 접근을 지원합니다.

:::topic-grid
## 클래스
- [IOBluetoothDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice): 하나의 원격 Bluetooth 장치를 나타내는 인스턴스입니다.
- [IOBluetoothDeviceInquiry](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquiry): 컴퓨터 범위 안의 Bluetooth 장치를 찾고, 선택적으로 이름 정보를 가져오는 device inquiry를 나타내는 객체입니다.
- [IOBluetoothDevicePair](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepair): 원격 Bluetooth 장치에 대한 pairing 시도를 나타내는 인스턴스입니다.
- [IOBluetoothDeviceRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceref): Bluetooth I/O 장치를 나타내는 객체입니다.
- [IOBluetoothHandsFree](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfree): hands-free profile 클래스입니다.
- [IOBluetoothHandsFreeAudioGateway](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogateway): 연결된 Bluetooth hands-free 전화기 또는 헤드셋으로 데이터를 보내고, 그로부터 오는 명령을 처리하는 객체입니다.
- [IOBluetoothHandsFreeDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevice): 연결된 Bluetooth hands-free 전화기 또는 헤드셋의 통화를 관리할 때 사용하는 객체입니다.
- [IOBluetoothHostController](https://developer.apple.com/documentation/iobluetooth/iobluetoothhostcontroller): 로컬 컴퓨터에 존재하는 Bluetooth Host Controller Interface를 표현하는 클래스입니다. 외부로 연결되었거나 내부에 포함된 경우 모두 해당합니다.
- [IOBluetoothL2CAPChannel](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel): 단일로 열린 L2CAP 채널을 나타내는 인스턴스입니다.
- [IOBluetoothL2CAPChannelRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelref)
- [IOBluetoothOBEXSession](https://developer.apple.com/documentation/iobluetooth/iobluetoothobexsession): Bluetooth RFCOMM 채널을 전송 계층으로 사용하는 OBEX session입니다.
- [IOBluetoothObject](https://developer.apple.com/documentation/iobluetooth/iobluetoothobject)
- [IOBluetoothObjectRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothobjectref)
- [IOBluetoothRFCOMMChannel](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel): Bluetooth SDP 사양에 정의된 RFCOMM 채널을 나타내는 인스턴스입니다.
- [IOBluetoothRFCOMMChannelRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannelref)
- [IOBluetoothSDPDataElement](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelement): Bluetooth SDP 사양에 정의된 단일 SDP 데이터 요소를 나타내는 인스턴스입니다.
- [IOBluetoothSDPDataElementRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpdataelementref)
- [IOBluetoothSDPServiceAttribute](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpserviceattribute): 단일 SDP 서비스 attribute를 나타냅니다.
- [IOBluetoothSDPServiceRecord](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord): 단일 SDP 서비스 레코드를 나타내는 인스턴스입니다.
- [IOBluetoothSDPServiceRecordRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecordref)
- [IOBluetoothSDPUUID](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuid): Bluetooth SDP 사양에 정의된 UUID를 나타내는 `NSData` subclass입니다.
- [IOBluetoothSDPUUIDRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpuuidref)
- [IOBluetoothUserNotification](https://developer.apple.com/documentation/iobluetooth/iobluetoothusernotification): 등록된 알림을 나타냅니다.
- [IOBluetoothUserNotificationRef](https://developer.apple.com/documentation/iobluetooth/iobluetoothusernotificationref)
- [OBEXFileTransferServices](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices): 단순한 PUT 및 GET 외에 고급 OBEX 연산을 구현합니다.
- [OBEXSession](https://developer.apple.com/documentation/iobluetooth/obexsession): 원격 대상에 대한 OBEX 연결을 나타내는 객체입니다.
:::

:::topic-grid
## 프로토콜
- [IOBluetoothDeviceAsyncCallbacks](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceasynccallbacks)
- [IOBluetoothDeviceInquiryDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothdeviceinquirydelegate): `IOBluetoothDeviceInquiry` 객체를 위한 delegate 메서드를 설명하는 `NSObject` category입니다. 모든 메서드는 선택 사항이지만, 모두 구현하는 것을 강력히 권장합니다. inquiry 객체가 중지되기 전에는 발견된 `IOBluetoothDevice` 객체에 대해 원격 이름 요청을 호출하지 마십시오. 그렇게 하면 프로세스가 deadlock될 수 있습니다.
- [IOBluetoothDevicePairDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevicepairdelegate)
- [IOBluetoothHandsFreeAudioGatewayDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreeaudiogatewaydelegate): 연결된 Bluetooth hands-free 전화기 또는 헤드셋의 상태 변화에 대한 정보 수신에 사용하는 선택적 메서드 집합입니다.
- [IOBluetoothHandsFreeDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedelegate)
- [IOBluetoothHandsFreeDeviceDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothhandsfreedevicedelegate): 연결된 Bluetooth hands-free 전화기 또는 헤드셋의 상태 변경 업데이트와 정보를 수신하기 위한 선택적 메서드 집합입니다.
- [IOBluetoothL2CAPChannelDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchanneldelegate)
- [IOBluetoothRFCOMMChannelDelegate](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchanneldelegate)
:::

:::topic-grid
## 참고 자료
- [Bluetooth.h User-Space](https://developer.apple.com/documentation/iobluetooth/bluetooth-h-user-space): Bluetooth 무선 기술
- [IOBluetoothUserLib.h](https://developer.apple.com/documentation/iobluetooth/iobluetoothuserlib-h): Apple의 Bluetooth 기술 구현을 위한 공개 인터페이스입니다.
- [IOBluetoothUtilities.h](https://developer.apple.com/documentation/iobluetooth/iobluetoothutilities-h): 헤더 수준 문서는 위의 Overview 절을 참고하십시오.
- [OBEX.h](https://developer.apple.com/documentation/iobluetooth/obex-h): 공개 OBEX 기술 인터페이스입니다.
- [OBEXBluetooth.h](https://developer.apple.com/documentation/iobluetooth/obexbluetooth-h): Bluetooth를 통한 Object Exchange입니다.
- [OBEXFileTransferServices.h](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices-h)
- [IOBluetooth Structures](https://developer.apple.com/documentation/iobluetooth/iobluetooth-structures)
- [IOBluetooth Enumerations](https://developer.apple.com/documentation/iobluetooth/iobluetooth-enumerations)
- [IOBluetooth Constants](https://developer.apple.com/documentation/iobluetooth/iobluetooth-constants)
- [IOBluetooth Functions](https://developer.apple.com/documentation/iobluetooth/iobluetooth-functions)
- [IOBluetooth Data Types](https://developer.apple.com/documentation/iobluetooth/iobluetooth-data-types)
:::

:::topic-grid
## 변수
- [kBluetoothConnectionHandleSerialDeviceReserved](https://developer.apple.com/documentation/iobluetooth/kbluetoothconnectionhandleserialdevicereserved)
:::
