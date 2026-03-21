---
route: /documentation/Hypervisor
source_url: https://developer.apple.com/documentation/Hypervisor
source_locale: en-US
section: docc
content_type: symbol
title: Hypervisor
original_title: Hypervisor
source_hash: f71c9f94821603541c06b2652a0183d480e94b1cc3001b029400ed71d84fbc4d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T02:55:31+00:00'
last_translated_at: '2026-03-13T02:55:31+00:00'
---

# Hypervisor

서드파티 커널 확장 없이 가벼운 하이퍼바이저 위에서 가상화 솔루션을 구축합니다.

## 개요

Hypervisor는 커널 확장(KEXT)을 작성하지 않고도 사용자 공간에서 가상화 기술과 상호작용할 수 있도록 C API를 제공합니다. 그 결과 이 프레임워크를 사용해 만드는 앱은 [Mac App Store](https://www.appstore.com/)를 통해 배포하기에 적합합니다.

이 프레임워크를 사용하면 권한이 부여된 샌드박스 사용자 공간 프로세스에서 하드웨어 지원 가상 머신과 가상 프로세서(VM 및 vCPU)를 생성하고 제어할 수 있습니다. Hypervisor는 가상 머신을 프로세스로, 가상 프로세서를 스레드로 추상화합니다.

### 요구 사항

Hypervisor 프레임워크에는 다음 요구 사항이 있습니다:

:::term-list
지원되는 하드웨어: Hypervisor 프레임워크는 하드웨어 리소스를 가상화하기 위한 하드웨어 지원을 요구합니다. Apple silicon에서는 여기에 Virtualization Extensions가 포함됩니다. Intel 기반 Mac 컴퓨터에서는 이 프레임워크가 Extended Page Tables(EPT)와 Unrestricted Mode를 포함하는 Intel VT-x 기능 집합을 갖춘 시스템을 지원합니다.
:::

실행 시에는 `kern.hv_support`를 인수로 전달하는 sysctl 명령을 사용해 특정 시스템에서 Hypervisor API를 사용할 수 있는지 판단합니다.

:::term-list
권한: Hypervisor API를 사용하려면 모든 프로세스가 [com.apple.security.hypervisor](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hypervisor) entitlement를 가져야 합니다.
:::

### 가상 리소스 매핑

게스트는 가상 하드웨어 위에서 실행되는 운영 체제입니다. 가상화된 하드웨어를 실행하는 운영 체제와 프로세스를 함께 호스트라고 부릅니다. 게스트의 가상 하드웨어는 호스트의 특정 리소스에 매핑됩니다.

각 가상 머신은 호스트의 하나의 프로세스에 대응합니다. 프로세스당 한 번에 하나의 가상 머신만 존재할 수 있으며, 가상 머신은 [hv_vm_create(_:)](https://developer.apple.com/documentation/hypervisor/hv_vm_create(_:))로 생성합니다.

가상 머신의 가상 CPU(vCPU)는 POSIX 스레드에 매핑됩니다. 현재 스레드에 대해 새 vCPU를 만들려면 [hv_vcpu_create(_:_:_:)](https://developer.apple.com/documentation/hypervisor/hv_vcpu_create(_:_:))를 사용합니다. 스레드가 [hv_vcpu_run(_:)](https://developer.apple.com/documentation/hypervisor/hv_vcpu_run(_:))를 호출하면 vCPU가 실행됩니다.

Hypervisor는 게스트의 물리 메모리를 호스트 프로세스의 가상 메모리에 매핑합니다. 새 메모리 매핑은 [hv_vm_map(_:_:_:_:)](https://developer.apple.com/documentation/hypervisor/hv_vm_map(_:_:_:_:))으로 생성합니다. 매핑된 범위 밖의 메모리에 접근하면 [hv_vcpu_run(_:)](https://developer.apple.com/documentation/hypervisor/hv_vcpu_run(_:))가 종료됩니다. 종료 시 메모리 접근을 에뮬레이션하고 [hv_vcpu_run(_:)](https://developer.apple.com/documentation/hypervisor/hv_vcpu_run(_:))로 게스트에 다시 진입함으로써 메모리 매핑 하드웨어를 에뮬레이션할 수 있습니다.

### 예제 VM 생명 주기

다음 그림은 Hypervisor API를 사용해 하나 이상의 가상 CPU를 가진 가상 머신을 생성하고 실행하는 단순화된 생명 주기를 보여 줍니다.

![가상 머신의 생명 주기를 나타내는 흐름도입니다.](https://developer.apple.com)

작업의 시작 시점에는 다음을 수행합니다:

- [hv_vm_create(_:)](https://developer.apple.com/documentation/hypervisor/hv_vm_create(_:))로 VM을 생성합니다.
- [hv_vm_map(_:_:_:_:)](https://developer.apple.com/documentation/hypervisor/hv_vm_map(_:_:_:_:))으로 현재 작업의 가상 주소 공간에 있는 영역을 VM의 게스트 물리 주소 공간에 매핑합니다.
- `pthread_create(_:_:_:_:)`로 하나 이상의 POSIX 스레드를 생성합니다.

각 스레드에서는 다음을 수행합니다:

- [hv_vcpu_create(_:_:_:)](https://developer.apple.com/documentation/hypervisor/hv_vcpu_create(_:_:))로 가상 CPU를 생성합니다.
- [hv_vcpu_run(_:)](https://developer.apple.com/documentation/hypervisor/hv_vcpu_run(_:))를 호출해 vCPU를 실행합니다.

스레드가 종료 이벤트를 수신하면 다음을 수행합니다:

- 이벤트를 처리합니다.
- [hv_vcpu_run(_:)](https://developer.apple.com/documentation/hypervisor/hv_vcpu_run(_:))로 게스트에 다시 진입하거나, [hv_vcpu_destroy(_:)](https://developer.apple.com/documentation/hypervisor/hv_vcpu_destroy(_:))로 vCPU를 제거합니다.

모든 스레드가 끝난 뒤에는 다음을 수행합니다:

- [hv_vm_unmap(_:_:)](https://developer.apple.com/documentation/hypervisor/hv_vm_unmap(_:_:))로 메모리 영역의 매핑을 해제합니다.
- [hv_vm_destroy()](https://developer.apple.com/documentation/hypervisor/hv_vm_destroy())로 VM을 제거합니다.

:::topic-grid
## 플랫폼
- [Apple Silicon](https://developer.apple.com/documentation/hypervisor/apple-silicon): Apple silicon에서 가상 머신을 생성하고 실행합니다.
- [Intel-based Mac](https://developer.apple.com/documentation/hypervisor/intel-based-mac): Intel 기반 Mac 컴퓨터에서 가상 머신을 생성하고 실행합니다.
:::

:::topic-grid
## 권한
- [com.apple.security.hypervisor](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hypervisor): 앱이 가상 머신을 생성하고 관리하는지를 나타내는 Boolean 값입니다.
- [com.apple.vm.hypervisor](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.vm.hypervisor): 앱이 가상 머신을 생성하고 관리하는지를 나타내는 Boolean 값입니다.
- [com.apple.vm.networking](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.vm.networking): 루트 사용자로 권한을 상승하지 않고 앱이 가상 네트워크 인터페이스를 관리하는지를 나타내는 Boolean 값입니다.
- [com.apple.vm.device-access](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.vm.device-access): 앱이 USB 기기를 캡처하여 게스트 운영 체제에서 사용하는지를 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 레퍼런스
- [Hypervisor Structures](https://developer.apple.com/documentation/hypervisor/hypervisor-structures)
- [Hypervisor Constants](https://developer.apple.com/documentation/hypervisor/hypervisor-constants)
- [Hypervisor Functions](https://developer.apple.com/documentation/hypervisor/hypervisor-functions)
- [Hypervisor Data Types](https://developer.apple.com/documentation/hypervisor/hypervisor-data-types)
:::

:::topic-grid
## 구조체
- [hv_ipa_granule_t](https://developer.apple.com/documentation/hypervisor/hv_ipa_granule_t)
:::

:::topic-grid
## 변수
- [HV_IPA_GRANULE_16KB](https://developer.apple.com/documentation/hypervisor/hv_ipa_granule_16kb)
- [HV_IPA_GRANULE_4KB](https://developer.apple.com/documentation/hypervisor/hv_ipa_granule_4kb)
:::

:::topic-grid
## 함수
- [hv_vm_config_get_default_ipa_granule(_:)](https://developer.apple.com/documentation/hypervisor/hv_vm_config_get_default_ipa_granule(_:))
- [hv_vm_config_get_ipa_granule(_:_:)](https://developer.apple.com/documentation/hypervisor/hv_vm_config_get_ipa_granule(_:_:))
- [hv_vm_config_set_ipa_granule(_:_:)](https://developer.apple.com/documentation/hypervisor/hv_vm_config_set_ipa_granule(_:_:))
:::
