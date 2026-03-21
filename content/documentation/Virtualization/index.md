---
route: /documentation/Virtualization
source_url: https://developer.apple.com/documentation/Virtualization
source_locale: en-US
section: docc
content_type: symbol
title: Virtualization
original_title: Virtualization
source_hash: 1c0d0fd64b0b68f700cd0c79afc471e1fc0e9c71ce079b97c2558a429237df61
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:49:10+00:00'
last_translated_at: '2026-03-14T02:20:00+09:00'
---

# Virtualization

가상 머신을 생성하고 macOS 및 Linux 기반 운영 체제를 실행합니다.

## 개요

Virtualization 프레임워크는 Apple silicon 및 Intel 기반 Mac 컴퓨터에서 가상 머신(VM)을 생성하고 관리하기 위한 고수준 API를 제공합니다. 이 프레임워크를 사용하면 직접 정의한 사용자 환경에서 macOS 또는 Linux 기반 운영 체제를 부팅하고 실행할 수 있습니다. 이 프레임워크는 네트워크, 소켓, 직렬 포트, 저장소, 엔트로피, 메모리 balloon 장치를 포함한 다양한 장치 유형의 표준 인터페이스를 정의하는 [Virtual I/O Device (VIRTIO)](https://docs.oasis-open.org/virtio/virtio/v1.1/csprd01/virtio-v1.1-csprd01.html) 사양을 지원합니다.

VM을 설정하려면 [VZVirtualMachineConfiguration](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration)을 구성합니다. macOS guest를 생성하는 경우 [VZMacPlatformConfiguration](https://developer.apple.com/documentation/virtualization/vzmacplatformconfiguration)도 구성한 다음 guest 운영 체제에 노출할 장치를 추가합니다. 그런 다음 구성 데이터로 [VZVirtualMachineConfiguration](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration) 객체를 만들고, 이 VM 객체를 사용해 VM 환경을 시작, 일시 정지, 재개합니다. guest와 상호 작용하려면 [VZVirtualMachine](https://developer.apple.com/documentation/virtualization/vzvirtualmachine) 객체로 [VZVirtualMachineView](https://developer.apple.com/documentation/virtualization/vzvirtualmachineview)를 생성해 창 안에 그래픽 콘텐츠를 표시하고 상호 작용합니다.

:::topic-grid
## 기초
- [Adding the Virtualization Entitlement to Your Project](https://developer.apple.com/documentation/virtualization/adding-the-virtualization-entitlement-to-your-project): 프로젝트가 Virtualization 프레임워크를 사용할 수 있도록 구성합니다.
- [com.apple.security.virtualization](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.virtualization): 앱이 Virtualization 프레임워크를 사용할 수 있는지를 나타내는 Boolean 값입니다.
- [Using iCloud with macOS virtual machines](https://developer.apple.com/documentation/virtualization/using-icloud-with-macos-virtual-machines): macOS guest 가상 머신에서 iCloud에 접근합니다.
:::

:::topic-grid
## 가상 머신 설정
- [Running macOS in a virtual machine on Apple silicon](https://developer.apple.com/documentation/virtualization/running-macos-in-a-virtual-machine-on-apple-silicon): Virtualization 프레임워크를 사용해 가상 머신에 macOS를 설치하고 실행합니다.
- [Running Linux in a Virtual Machine](https://developer.apple.com/documentation/virtualization/running-linux-in-a-virtual-machine): Virtualization 프레임워크를 사용해 Mac에서 Linux 운영 체제를 실행합니다.
- [Running GUI Linux in a virtual machine on a Mac](https://developer.apple.com/documentation/virtualization/running-gui-linux-in-a-virtual-machine-on-a-mac): Virtualization 프레임워크를 사용해 Mac의 가상 머신에 GUI Linux를 설치하고 실행합니다.
- [Installing macOS on a Virtual Machine](https://developer.apple.com/documentation/virtualization/installing-macos-on-a-virtual-machine): macOS 복원 이미지를 다운로드해 새 VM에 설치합니다.
- [Creating and Running a Linux Virtual Machine](https://developer.apple.com/documentation/virtualization/creating-and-running-a-linux-virtual-machine): Apple silicon 또는 Intel 기반 Mac 컴퓨터에서 사용자 정의 Linux guest를 설계하고 실행합니다.
- [Virtualize macOS on a Mac](https://developer.apple.com/documentation/virtualization/virtualize-macos-on-a-mac): Apple silicon에서 macOS guest를 구성하고 실행합니다.
- [Virtualize Linux on a Mac](https://developer.apple.com/documentation/virtualization/virtualize-linux-on-a-mac): Apple silicon 및 Intel 기반 Mac 컴퓨터에서 Linux guest를 구성하고 실행합니다.
- [Running Intel Binaries in Linux VMs with Rosetta](https://developer.apple.com/documentation/virtualization/running-intel-binaries-in-linux-vms-with-rosetta): Apple silicon에서 ARM Linux 아래에서 x86_64 Linux 바이너리를 실행합니다.
- [Accelerating the performance of Rosetta](https://developer.apple.com/documentation/virtualization/accelerating-the-performance-of-rosetta): Linux kernel에 total store ordering (TSO) 메모리 모델 지원을 추가해 Rosetta 성능을 향상합니다.
:::

:::topic-grid
## 런타임
- [VZVirtualMachine](https://developer.apple.com/documentation/virtualization/vzvirtualmachine): VM의 전체 상태와 구성을 관리하는 객체입니다.
- [VZVirtualMachineView](https://developer.apple.com/documentation/virtualization/vzvirtualmachineview): 사용자가 VM과 상호 작용할 수 있게 하는 view입니다.
- [VZLinuxRosettaDirectoryShare](https://developer.apple.com/documentation/virtualization/vzlinuxrosettadirectoryshare): Rosetta를 위한 Linux 디렉터리 공유입니다.
:::

:::topic-grid
## 장치
- [Audio](https://developer.apple.com/documentation/virtualization/audio): guest 운영 체제가 host의 오디오 장치를 통해 오디오 재생과 캡처를 수행할 수 있게 하는 오디오 장치를 구성합니다.
- [Graphics](https://developer.apple.com/documentation/virtualization/graphics): guest가 사용자 인터페이스를 표시할 수 있도록 장치를 구성합니다.
- [Keyboards and pointing devices](https://developer.apple.com/documentation/virtualization/keyboards-and-pointing-devices): guest 시스템에 마우스와 키보드를 연결하는 장치를 구성합니다.
- [Memory](https://developer.apple.com/documentation/virtualization/memory): guest 시스템에 할당된 메모리를 변경하는 memory balloon 장치를 구성합니다.
- [Network](https://developer.apple.com/documentation/virtualization/network): guest 시스템을 네트워크에 연결하는 장치를 구성합니다.
- [Randomization](https://developer.apple.com/documentation/virtualization/randomization): guest 시스템이 난수를 생성할 때 사용하는 장치를 구성합니다.
- [Serial ports](https://developer.apple.com/documentation/virtualization/serial-ports): guest 시스템과 통신하는 데 사용하는 직렬 장치를 구성합니다.
- [Shared directories](https://developer.apple.com/documentation/virtualization/shared-directories): host의 디렉터리를 guest 시스템에 공유하는 장치를 구성합니다.
- [Sockets](https://developer.apple.com/documentation/virtualization/sockets): guest 시스템과의 포트 기반 통신을 관리하는 장치를 구성합니다.
- [Storage](https://developer.apple.com/documentation/virtualization/storage): guest 시스템의 디스크를 나타내는 block-storage 장치를 구성합니다.
- [Consoles](https://developer.apple.com/documentation/virtualization/consoles): guest 시스템과의 다중 포트 콘솔 통신을 관리하는 장치를 구성합니다.
- [Clipboard sharing](https://developer.apple.com/documentation/virtualization/clipboard-sharing): host와 guest 시스템 사이에서 pasteboard를 공유합니다.
- [USB Devices](https://developer.apple.com/documentation/virtualization/usb-devices)
:::

:::topic-grid
## 열거형
- [Virtualization enumerations](https://developer.apple.com/documentation/virtualization/virtualization-enumerations): VM의 캐시 모드, 디스크 동기화, macOS auxiliary storage 옵션을 제어합니다.
:::

:::topic-grid
## 오류
- [VZErrorDomain](https://developer.apple.com/documentation/virtualization/vzerrordomain): Virtualization 프레임워크의 오류 도메인입니다.
- [VZError](https://developer.apple.com/documentation/virtualization/vzerror): VM을 구성하거나 사용할 때 마주칠 수 있는 오류입니다.
:::
