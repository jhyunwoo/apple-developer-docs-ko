---
route: /documentation/ParavirtualizedGraphics
source_url: https://developer.apple.com/documentation/ParavirtualizedGraphics
source_locale: en-US
section: docc
content_type: symbol
title: Paravirtualized Graphics
original_title: Paravirtualized Graphics
source_hash: 07c303fcef5357bb7bb0764cf18a336e5ddbd2c840306c2b5064953c1ad23d78
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:47:40+00:00'
last_translated_at: '2026-03-13T15:35:00+09:00'
---

# Paravirtualized Graphics

게스트 드라이버 스택에 그래픽 가속을 추가합니다.

## 개요

하드웨어 수준 가상화를 구현하는 앱에서는 가상 머신 내부 성능, 특히 그래픽 성능이 중요합니다. ParavirtualizedGraphics 프레임워크는 가상 머신에서 실행되는 macOS, 즉 여기서 말하는 게스트를 위해 하드웨어 가속 그래픽을 구현합니다. 운영 체제는 게스트 내부에서 실행되는 그래픽 드라이버를 제공하며, 이 드라이버는 호스트 운영 체제의 프레임워크와 통신하여 Metal 가속 그래픽을 활용합니다.

가상화 솔루션 내부에서 가속 그래픽을 구현하려면 각 가상 머신에 대해 다음 단계를 수행해야 합니다.

1. macOS가 올바른 드라이버를 설치할 수 있도록 가상 머신 하드웨어에서 가상 그래픽 카드를 광고합니다.
2. [PGDeviceDescriptor](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevicedescriptor)를 생성하고, 가상 머신 구현을 ParavirtualizedGraphics 프레임워크에 연결하는 데 필요한 블록을 제공합니다. 이 descriptor를 사용해 [PGDevice](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice) 객체를 생성하고, 가상 머신이 활성 상태인 동안 이를 유지합니다. ParavirtualizedGraphics 프레임워크는 메모리를 할당하거나 그 밖의 관련 작업을 수행해야 할 때 이러한 블록을 호출합니다.
3. 기기에 연결할 각 가상 디스플레이에 대해 [PGDisplayDescriptor](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaydescriptor)를 생성하고, 디스플레이 속성과 프레임워크가 디스플레이 이벤트에 대해 호출할 블록을 지정합니다. 이 descriptor를 사용해 [PGDisplay](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay) 객체를 생성합니다. 프레임워크가 제공하는 그래픽 데이터를 표시할 수 있도록 적절한 디스플레이 이벤트를 처리합니다.

:::topic-grid
## PCI 기기 특성
- [PG_PCI_DEVICE_ID](https://developer.apple.com/documentation/paravirtualizedgraphics/pg_pci_device_id): 가상 머신 내부에서 그래픽 스택을 광고할 때 사용하는 PCI 기기 식별자입니다.
- [PG_PCI_VENDOR_ID](https://developer.apple.com/documentation/paravirtualizedgraphics/pg_pci_vendor_id): 가상 머신 내부에서 그래픽 스택을 광고할 때 사용하는 공급업체 식별자입니다.
- [PG_PCI_BAR_MMIO](https://developer.apple.com/documentation/paravirtualizedgraphics/pg_pci_bar_mmio): 가상 머신 내부에서 그래픽 스택을 광고할 때 사용하는 base address register입니다.
- [PG_PCI_MAX_MSI_VECTORS](https://developer.apple.com/documentation/paravirtualizedgraphics/pg_pci_max_msi_vectors): 그래픽 구성을 위해 할당해야 하는 MSI 벡터 수입니다.
- [PGCopyOptionROMURL()](https://developer.apple.com/documentation/paravirtualizedgraphics/pgcopyoptionromurl()): 게스트 그래픽 기기에서 사용할 ROM 이미지의 URL을 복사합니다.
:::

:::topic-grid
## 기기
- [PGNewDeviceWithDescriptor(_:)](https://developer.apple.com/documentation/paravirtualizedgraphics/pgnewdevicewithdescriptor(_:)): 새로운 반가상화 그래픽 기기를 생성합니다.
- [PGDeviceDescriptor](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevicedescriptor): 생성할 반가상화 그래픽 기기에 대한 설명입니다.
- [PGDevice](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice): 반가상화 GPU 기기 객체입니다.
:::

:::topic-grid
## 디스플레이
- [PGDisplayDescriptor](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaydescriptor): 가상 디스플레이를 위한 descriptor입니다.
- [PGDisplay](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay): 호스트 측 가상 머신 앱이 가로챌 수 있는 방식으로 게스트 운영 체제에 디스플레이 기능을 제공하는 객체입니다.
- [PGDisplayMode](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaymode): 지원되는 디스플레이 모드를 설명합니다.
- [PGDisplayCoord_t](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaycoord_t): 2차원 픽셀 배열 내 크기나 오프셋을 설명하는 좌표입니다.
:::

:::topic-grid
## 레퍼런스
- [ParavirtualizedGraphics Constants](https://developer.apple.com/documentation/paravirtualizedgraphics/paravirtualizedgraphics-constants)
- [ParavirtualizedGraphics Functions](https://developer.apple.com/documentation/paravirtualizedgraphics/paravirtualizedgraphics-functions)
- [ParavirtualizedGraphics Data Types](https://developer.apple.com/documentation/paravirtualizedgraphics/paravirtualizedgraphics-data-types)
:::

:::topic-grid
## 변수
- [HAS_NS_BITMAP_HEADER](https://developer.apple.com/documentation/paravirtualizedgraphics/has_ns_bitmap_header)
- [PG_SUPPORT_CREATE_DEVICE](https://developer.apple.com/documentation/paravirtualizedgraphics/pg_support_create_device)
:::

:::topic-grid
## 함수
- [PGCreateDeviceWithDescriptor(_:)](https://developer.apple.com/documentation/paravirtualizedgraphics/pgcreatedevicewithdescriptor(_:))
:::
