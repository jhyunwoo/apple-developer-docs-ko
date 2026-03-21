---
route: /documentation/CoreWLAN
source_url: https://developer.apple.com/documentation/CoreWLAN
source_locale: en-US
section: docc
content_type: symbol
title: Core WLAN
original_title: Core WLAN
source_hash: 76b89a0cc124e0bc80a69f3cdb7d7b1180d9ee0be758353b31a8fd71de5b421c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:12:33+00:00'
last_translated_at: '2026-03-14T00:45:00+09:00'
---

# Core WLAN

AirPort 인터페이스를 조회하고 무선 네트워크를 선택합니다.

## 개요

CoreWLAN 프레임워크는 AirPort 인터페이스를 조회하고 네트워크를 선택하기 위한 API를 제공합니다.

[CWWiFiClient](https://developer.apple.com/documentation/corewlan/cwwificlient) 인스턴스를 사용해 Wi-Fi 하위 시스템에 접근합니다. 이 client 객체는 [CWInterface](https://developer.apple.com/documentation/corewlan/cwinterface) 객체로 표현되는 시스템의 모든 Wi-Fi 인터페이스에 대한 핸들을 얻는 메서드를 제공합니다. 또한 client를 사용해 Wi-Fi 이벤트 알림 수신을 등록할 수도 있습니다. 이러한 알림을 처리하려면 [CWEventDelegate](https://developer.apple.com/documentation/corewlan/cweventdelegate) 프로토콜을 준수하는 delegate를 지정합니다.

Client 객체를 생성하는 작업은 리소스를 많이 사용하므로, 일반적으로 앱 수명 주기 동안 짧게 살아 있는 인스턴스를 여러 개 만드는 대신 하나의 객체만 사용하는 편이 좋습니다. 편의를 위해 client 클래스는 이런 용도로 사용할 수 있는 공유 singleton 인스턴스를 정의합니다.

App Sandbox를 채택한 앱에서도 client 인스턴스가 제공하는 interface 객체를 사용하는 한 별도의 예외 없이 CoreWLAN 프레임워크를 사용할 수 있습니다. Interface 객체를 직접 초기화하면 sandbox 안전하다고 간주되지 않는 저수준 시스템 socket 접근이 발생합니다. App Sandbox에 대한 자세한 내용은 [App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)를 참고하십시오.

:::topic-grid
## 클래스
- [CWChannel](https://developer.apple.com/documentation/corewlan/cwchannel): IEEE 802.11 채널을 캡슐화합니다.
- [CWConfiguration](https://developer.apple.com/documentation/corewlan/cwconfiguration): AirPort WLAN 인터페이스를 위한 불변 구성을 캡슐화합니다.
- [CWInterface](https://developer.apple.com/documentation/corewlan/cwinterface): IEEE 802.11 인터페이스를 캡슐화합니다.
- [CWMutableConfiguration](https://developer.apple.com/documentation/corewlan/cwmutableconfiguration): AirPort WLAN 인터페이스를 위한 가변 구성을 캡슐화합니다.
- [CWMutableNetworkProfile](https://developer.apple.com/documentation/corewlan/cwmutablenetworkprofile): 가변 네트워크 프로필 항목을 캡슐화합니다.
- [CWNetwork](https://developer.apple.com/documentation/corewlan/cwnetwork): IEEE 802.11 네트워크를 캡슐화하며, 네트워크의 여러 속성에 대한 읽기 전용 접근자를 제공합니다.
- [CWNetworkProfile](https://developer.apple.com/documentation/corewlan/cwnetworkprofile): 불변 네트워크 프로필 항목을 캡슐화합니다.
- [CWWiFiClient](https://developer.apple.com/documentation/corewlan/cwwificlient): 인터페이스 접근과 이벤트 알림 설정에 사용하는 전체 Wi-Fi 하위 시스템용 래퍼입니다.
:::

:::topic-grid
## 프로토콜
- [CWEventDelegate](https://developer.apple.com/documentation/corewlan/cweventdelegate): Wi-Fi client 객체가 Wi-Fi 이벤트를 delegate에 알릴 때 사용하는 인터페이스입니다.
:::

:::topic-grid
## 참고 자료
- [CoreWLANConstants.h](https://developer.apple.com/documentation/corewlan/corewlanconstants-h)
- [CoreWLANTypes.h](https://developer.apple.com/documentation/corewlan/corewlantypes-h)
- [CoreWLANUtil.h](https://developer.apple.com/documentation/corewlan/corewlanutil-h)
- [CoreWLAN Enumerations](https://developer.apple.com/documentation/corewlan/corewlan-enumerations)
- [CoreWLAN Functions](https://developer.apple.com/documentation/corewlan/corewlan-functions)
:::

:::topic-grid
## 구조체
- [CWCipherKeyFlags](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags): cipher key 플래그입니다.
:::
