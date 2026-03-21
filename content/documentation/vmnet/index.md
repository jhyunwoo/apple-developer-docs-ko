---
route: /documentation/vmnet
source_url: https://developer.apple.com/documentation/vmnet
source_locale: en-US
section: docc
content_type: symbol
title: vmnet
original_title: vmnet
source_hash: 85ea32bc395d4738ed76c59ae8872c5161f4d291f41b4054ba4c05f8836064df
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:07:37+00:00'
last_translated_at: '2026-03-14T03:28:00+09:00'
---

# vmnet

guest 운영 체제에서 packet을 읽고 쓰기 위해 네트워크 인터페이스에 연결합니다.

## 개요

vmnet 프레임워크는 가상 머신이 packet을 읽고 쓰기 위한 API입니다.

이 API를 사용하면 Guest OS 인터페이스를 host mode 또는 shared mode로 둘 수 있습니다. host mode의 인터페이스는 기본 host 시스템 및 host mode로 실행 중인 다른 인터페이스와 통신할 수 있습니다. shared mode에서는 네트워크 인터페이스가 인터넷, 기본 host, 그리고 shared mode로 실행 중인 다른 인터페이스와 packet을 송수신할 수 있습니다.

:::note Note
가상화 기술에 대한 자세한 내용은 [Hypervisor](https://developer.apple.com/documentation/Hypervisor) 프레임워크를 참고하십시오.
:::

### 요구 사항

vmnet 프레임워크에는 다음 요구 사항이 있습니다.

#### entitlement

sandboxed user space process가 vmnet API를 사용하려면 `com.apple.vm.networking` entitlement를 가지고 있어야 합니다.

### 아키텍처

![](https://developer.apple.com)

VM Network API는 guest 운영 체제의 인터페이스를 지원합니다. 이 API는 guest OS 인터페이스에 구성해야 하는 MAC 주소와 MTU를 제공합니다. 인터페이스는 DHCP를 통해 private IPv4 주소를 받습니다. guest 운영 체제에서 시작하는 IPv4 트래픽은 이 private IPv4 주소를 사용해야 합니다. 다른 IPv4 주소에서 보낸 packet은 시스템이 버립니다.

최대 32개의 인터페이스를 만들 수 있으며 guest 운영 체제당 최대 4개까지 허용됩니다. 각 read/write 호출은 최대 256KB까지 최대 200개 packet의 읽기 또는 쓰기를 허용합니다. 쓰는 각 packet은 완전한 ethernet frame이어야 합니다.

:::topic-grid
## 기초
- [com.apple.vm.networking](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.vm.networking): 앱이 root 사용자 권한 상승 없이 가상 네트워크 인터페이스를 관리하는지를 나타내는 Boolean입니다.
:::

:::topic-grid
## 인터페이스 시작 및 중지
- [vmnet_start_interface(_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_start_interface(_:_:_:)): 지정한 구성을 사용해 인터페이스에서 host mode 또는 shared mode를 시작합니다.
- [vmnet_interface_set_event_callback(_:_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_interface_set_event_callback(_:_:_:_:)): 지정한 인터페이스의 이벤트를 수신할 때 실행할 callback을 예약합니다.
- [vmnet_stop_interface(_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_stop_interface(_:_:_:)): 인터페이스를 중지합니다.
:::

:::topic-grid
## packet 읽기 및 쓰기
- [vmnet_read(_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_read(_:_:_:)): 인터페이스에서 지정한 수의 packet을 읽으려고 시도합니다.
- [vmnet_write(_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_write(_:_:_:)): 지정한 packet을 인터페이스에 쓰려고 시도합니다.
:::

:::topic-grid
## 데이터 타입
- [vmnet_return_t](https://developer.apple.com/documentation/vmnet/vmnet_return_t): vmnet 프레임워크 함수가 반환하는 값입니다.
- [vmpktdesc](https://developer.apple.com/documentation/vmnet/vmpktdesc): packet을 설명합니다.
- [interface_ref](https://developer.apple.com/documentation/vmnet/interface_ref): 가상 네트워크 인터페이스입니다.
- [interface_event_t](https://developer.apple.com/documentation/vmnet/interface_event_t): 인터페이스 이벤트 타입입니다.
- [operating_modes_t](https://developer.apple.com/documentation/vmnet/operating_modes_t): 인터페이스의 operating mode입니다.
:::

:::topic-grid
## 상수
- [interface_desc XPC Dictionary Keys](https://developer.apple.com/documentation/vmnet/interface_desc_xpc_dictionary_keys): 네트워크 인터페이스 매개변수를 설명하기 위해 함수에 전달하는 parameter가 지원하는 XPC dictionary key입니다.
- [interface_param XPC Dictionary Keys](https://developer.apple.com/documentation/vmnet/interface_param_xpc_dictionary_keys): completion handler가 반환한 인수가 네트워크 인터페이스 구성에 사용해야 할 매개변수를 설명할 때 사용하는 XPC dictionary key입니다.
- [event XPC Dictionary](https://developer.apple.com/documentation/vmnet/event_xpc_dictionary): callback 이벤트에 대한 정보를 제공하는 함수가 callback에서 클라이언트에 반환하는 값에 사용하는 XPC dictionary key입니다.
:::

:::topic-grid
## 참고 자료
- [vmnet Constants](https://developer.apple.com/documentation/vmnet/vmnet_constants)
- [vmnet Functions](https://developer.apple.com/documentation/vmnet/vmnet_functions)
- [vmnet Data Types](https://developer.apple.com/documentation/vmnet/vmnet_data_types)
:::

:::topic-grid
## 변수
- [vmnet_enable_virtio_header_key](https://developer.apple.com/documentation/vmnet/vmnet_enable_virtio_header_key-swift.var)
- [vmnet_read_max_packets_key](https://developer.apple.com/documentation/vmnet/vmnet_read_max_packets_key)
- [vmnet_write_max_packets_key](https://developer.apple.com/documentation/vmnet/vmnet_write_max_packets_key)
:::

:::topic-grid
## 함수
- [vmnet_interface_start_with_network(_:_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_interface_start_with_network(_:_:_:_:))
- [vmnet_network_configuration_add_dhcp_reservation(_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_add_dhcp_reservation(_:_:_:))
- [vmnet_network_configuration_add_port_forwarding_rule(_:_:_:_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_add_port_forwarding_rule(_:_:_:_:_:_:))
- [vmnet_network_configuration_create(_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_create(_:_:))
- [vmnet_network_configuration_disable_dhcp(_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_disable_dhcp(_:))
- [vmnet_network_configuration_disable_dns_proxy(_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_disable_dns_proxy(_:))
- [vmnet_network_configuration_disable_nat44(_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_disable_nat44(_:))
- [vmnet_network_configuration_disable_nat66(_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_disable_nat66(_:))
- [vmnet_network_configuration_disable_router_advertisement(_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_disable_router_advertisement(_:))
- [vmnet_network_configuration_set_external_interface(_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_set_external_interface(_:_:))
- [vmnet_network_configuration_set_ipv4_subnet(_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_set_ipv4_subnet(_:_:_:))
- [vmnet_network_configuration_set_ipv6_prefix(_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_set_ipv6_prefix(_:_:_:))
- [vmnet_network_configuration_set_mtu(_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_set_mtu(_:_:))
- [vmnet_network_copy_serialization(_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_copy_serialization(_:_:))
- [vmnet_network_create(_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_create(_:_:))
- [vmnet_network_create_with_serialization(_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_create_with_serialization(_:_:))
- [vmnet_network_get_ipv4_subnet(_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_get_ipv4_subnet(_:_:_:))
- [vmnet_network_get_ipv6_prefix(_:_:_:)](https://developer.apple.com/documentation/vmnet/vmnet_network_get_ipv6_prefix(_:_:_:))
:::

:::topic-grid
## 타입 별칭
- [vmnet_mode_t](https://developer.apple.com/documentation/vmnet/vmnet_mode_t)
- [vmnet_network_configuration_ref](https://developer.apple.com/documentation/vmnet/vmnet_network_configuration_ref)
- [vmnet_network_ref](https://developer.apple.com/documentation/vmnet/vmnet_network_ref)
:::
