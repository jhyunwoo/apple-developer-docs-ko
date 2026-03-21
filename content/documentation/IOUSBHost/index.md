---
route: /documentation/IOUSBHost
source_url: https://developer.apple.com/documentation/IOUSBHost
source_locale: en-US
section: docc
content_type: symbol
title: IOUSBHost
original_title: IOUSBHost
source_hash: df5ac930692420dbde5822ffde970abbe38d661de437ddac62252d7dbcf4b9ed
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:56+00:00'
last_translated_at: '2026-03-13T18:25:00+09:00'
---

# IOUSBHost

USB 기기를 위한 host-mode 사용자 공간 드라이버를 생성합니다.

## 개요

[IOUSBHost](https://developer.apple.com/documentation/iousbhost) 프레임워크를 사용하면 앱 내부에서 사용자 정의 USB 기기와 클래스 규격을 따르지 않는 USB 기기에 접근할 수 있습니다. 이 프레임워크를 사용해 카메라, 오디오 기기, 스캐너, 프린터, 키보드, 마우스 기기, MIDI 키보드, USB 허브에 연결할 수 있습니다.

이 프레임워크는 USB Implementers Forum(USB-IF)의 *Universal Serial Bus 3.2 Specification*, Revision 1.0, September 22, 2017을 참조합니다. 이 사양은 [http://www.usb.org/](http://www.usb.org/)에서 볼 수 있습니다.

:::topic-grid
## 기능 드라이버
- [IOUSBHostInterface](https://developer.apple.com/documentation/iousbhost/iousbhostinterface): USB 관련 서비스에 접근하는 클래스입니다.
- [IOUSBHostPipe](https://developer.apple.com/documentation/iousbhost/iousbhostpipe): 기능 드라이버를 위해 제어, 벌크, 인터럽트, 등시성 입출력 요청을 전송하고 스트림 기능을 관리하는 클래스입니다.
- [IOUSBHostStream](https://developer.apple.com/documentation/iousbhost/iousbhoststream): 기능 드라이버를 위한 스트림 데이터를 전송하는 책임을 맡는 클래스입니다.
:::

:::topic-grid
## 기기 드라이버
- [IOUSBHostDevice](https://developer.apple.com/documentation/iousbhost/iousbhostdevice): 기기를 점유하고 구성하며 descriptor를 가져오고 기기 요청을 보내는 클래스입니다.
:::

:::topic-grid
## 기본 클래스
- [IOUSBHostObject](https://developer.apple.com/documentation/iousbhost/iousbhostobject): 기기 요청 전송과 descriptor 조회를 위한 기본 기능을 제공하는 클래스입니다.
- [IOUSBHostIOSource](https://developer.apple.com/documentation/iousbhost/iousbhostiosource): pipe와 stream 클래스를 파생시키기 위한 기본 기능을 제공하는 클래스입니다.
:::

:::topic-grid
## IOServicePlane 프로퍼티
- [IOUSBHostInterfacePropertyKey](https://developer.apple.com/documentation/iousbhost/iousbhostinterfacepropertykey): 상태를 설명하는 USB 인터페이스의 프로퍼티입니다.
- [IOUSBHostDevicePropertyKey](https://developer.apple.com/documentation/iousbhost/iousbhostdevicepropertykey): 상태를 설명하는 USB 기기의 프로퍼티입니다.
- [IOUSBHostMatchingPropertyKey](https://developer.apple.com/documentation/iousbhost/iousbhostmatchingpropertykey): 매칭 서비스를 구현하기 위한 프로퍼티입니다.
- [IOUSBHostPropertyKey](https://developer.apple.com/documentation/iousbhost/iousbhostpropertykey): USB host 기기 클래스와 인터페이스 클래스가 공유하는 프로퍼티입니다.
:::

:::topic-grid
## 오류 도메인
- [IOUSBHostErrorDomain](https://developer.apple.com/documentation/iousbhost/iousbhosterrordomain): 프레임워크의 오류 도메인입니다.
:::

:::topic-grid
## 클래스
- [IOUSBHostCIControllerStateMachine](https://developer.apple.com/documentation/iousbhost/iousbhostcicontrollerstatemachine)
- [IOUSBHostCIDeviceStateMachine](https://developer.apple.com/documentation/iousbhost/iousbhostcidevicestatemachine)
- [IOUSBHostCIEndpointStateMachine](https://developer.apple.com/documentation/iousbhost/iousbhostciendpointstatemachine)
- [IOUSBHostCIPortStateMachine](https://developer.apple.com/documentation/iousbhost/iousbhostciportstatemachine)
- [IOUSBHostControllerInterface](https://developer.apple.com/documentation/iousbhost/iousbhostcontrollerinterface)
:::

:::topic-grid
## 참고 자료
- [IOUSBHost Structures](https://developer.apple.com/documentation/iousbhost/iousbhost-structures)
- [IOUSBHost Enumerations](https://developer.apple.com/documentation/iousbhost/iousbhost-enumerations)
- [IOUSBHost Constants](https://developer.apple.com/documentation/iousbhost/iousbhost-constants)
- [IOUSBHost Functions](https://developer.apple.com/documentation/iousbhost/iousbhost-functions)
- [IOUSBHost Data Types](https://developer.apple.com/documentation/iousbhost/iousbhost-data-types)
:::

:::topic-grid
## 변수
- [IOUSBHostCIDeviceSpeedOther](https://developer.apple.com/documentation/iousbhost/iousbhostcidevicespeedother)
:::
