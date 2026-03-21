---
route: /documentation/ContactProvider
source_url: https://developer.apple.com/documentation/ContactProvider
source_locale: en-US
section: docc
content_type: symbol
title: ContactProvider
original_title: ContactProvider
source_hash: b4a0e7614971dc962cf00150249dee42149823039d1635338dd5575a78823ff8
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:27+00:00'
last_translated_at: '2026-03-13T17:20:00+09:00'
---

# ContactProvider

앱이 관리하는 연락처를 시스템 전역 Contacts 생태계에 제공합니다.

## 개요

앱이 자체 연락처를 관리하고 있고 이를 [Contacts](https://developer.apple.com/documentation/Contacts) 프레임워크를 사용하는 다른 앱에서 사용할 수 있게 하려면 Contact Provider 프레임워크를 사용하십시오. 이렇게 하면 앱이 발신자나 보낸 사람을 알고 있을 때 Phone, Mail 같은 앱이 수신 전화나 메시지에 대해 개인 이름과 이미지를 제공할 수 있습니다. 앱은 Contacts 프레임워크로 연락처를 직접 추가하는 대신, 읽기 전용 연락처 항목을 제공하고 이를 업데이트할 수 있으며, 앱 사용자는 이러한 항목을 쉽게 활성화하거나 비활성화하거나 추가하거나 제거할 수 있습니다. 이를 통해 사용자는 앱에서 사용하는 연락처를 개인 연락처와 별도로 정리할 수 있습니다.

앱에서 연락처를 제공하려면 [ContactProviderExtension](https://developer.apple.com/documentation/contactprovider/contactproviderextension)을 확장하는 app extension을 추가하십시오. extension은 앱이 관리하는 연락처를 열거하는 역할을 합니다. 앱은 [ContactProviderManager](https://developer.apple.com/documentation/contactprovider/contactprovidermanager) 클래스로 extension을 관리합니다. manager를 사용해 extension domain을 활성화하거나 비활성화하는데, 일반적으로 기본 domain을 사용합니다. extension domain을 활성화한 뒤에는 extension이 실행되어 연락처를 동기화할 수 있고, 그러면 연락처가 [Contacts](https://developer.apple.com/documentation/Contacts) 프레임워크를 사용하는 다른 앱에서도 사용 가능해집니다.

:::tip Tip
기존 프로젝트에 Contact Provider 지원을 추가할 수 있도록 Xcode는 Contact Provider extension 템플릿을 제공합니다. Project navigator에서 프로젝트를 선택하고 Editor > Add Target을 선택하거나 Projects and Targets 목록에서 Add 버튼(`+`)을 클릭한 뒤 iOS 템플릿에서 Contact Provider Extension을 선택하십시오.
:::

extension은 여러 방식으로 실행되고 연락처를 업데이트할 수 있습니다. 앱은 manager의 [signalEnumerator(for:)](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/signalenumerator(for:))를 호출할 수 있으며, 이 호출은 extension을 로드하고 업데이트된 연락처 집합을 제공하도록 요청합니다. 예를 들어 앱이 서버에서 새 연락처를 사용할 수 있음을 알고 있을 때 이 호출을 사용할 수 있습니다. 그러면 앱은 이 연락처를 가져와 extension이 시스템 Contacts 데이터베이스에 제공하도록 할 수 있습니다. 또한 야간에 전원에 연결되어 있을 때 Contacts는 활성화된 모든 contact provider extension domain이 낮은 우선순위로 동기화할 시간을 예약합니다.

기기 사용자는 Settings 앱에서 provider를 보고 선택적으로 활성화하거나 비활성화할 수 있습니다. contact provider를 비활성화하면 해당 연락처는 다른 앱에서 사용할 수 없게 됩니다. 앱을 삭제하면 extension과 그 모든 연락처도 삭제됩니다.

:::topic-grid
## contact provider extension 생성
- [ContactProviderExtension](https://developer.apple.com/documentation/contactprovider/contactproviderextension): 앱 extension이 구현하는 프로토콜로, 시스템 전역 Contacts 생태계에 연락처 항목을 제공합니다.
:::

:::topic-grid
## 앱에서 extension 관리
- [ContactProviderManager](https://developer.apple.com/documentation/contactprovider/contactprovidermanager): 앱이 자신의 extension을 제어하기 위한 인터페이스입니다.
:::

:::topic-grid
## domain 작업
- [ContactProviderDomain](https://developer.apple.com/documentation/contactprovider/contactproviderdomain): 식별자와 표시 이름 같은 특성을 포함하며 extension을 구성할 때 사용하는 domain입니다.
- [DefaultContactProviderDomain](https://developer.apple.com/documentation/contactprovider/defaultcontactproviderdomain): extension이 사용하는 기본 domain입니다.
:::

:::topic-grid
## 연락처 제공
- [ContactItem](https://developer.apple.com/documentation/contactprovider/contactitem): 연락처 데이터베이스의 항목입니다.
- [ContactItemEnumerating](https://developer.apple.com/documentation/contactprovider/contactitemenumerating): 연락처 항목 컬렉션에 대한 enumerator를 제공하는 프로토콜입니다.
- [ContactItemEnumerator](https://developer.apple.com/documentation/contactprovider/contactitemenumerator): 모든 연락처 항목과 변경된 연락처 항목을 열거하는 기능을 제공하는 프로토콜입니다.
:::

:::topic-grid
## 연락처 수신
- [ContactItemContentObserver](https://developer.apple.com/documentation/contactprovider/contactitemcontentobserver): 모든 항목의 재개 가능한 enumeration을 수신하는 시스템 observer를 정의하는 프로토콜입니다.
- [ContactItemChangeObserver](https://developer.apple.com/documentation/contactprovider/contactitemchangeobserver): 변경된 연락처 항목의 재개 가능한 enumeration을 수신하는 시스템 observer를 정의하는 프로토콜입니다.
:::

:::topic-grid
## 지원 타입
- [ContactProviderError](https://developer.apple.com/documentation/contactprovider/contactprovidererror): Contact Provider 프레임워크가 던지는 오류입니다.
:::
