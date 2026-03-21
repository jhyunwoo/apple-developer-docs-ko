---
route: /documentation/PCIDriverKit
source_url: https://developer.apple.com/documentation/PCIDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: PCIDriverKit
original_title: PCIDriverKit
source_hash: 23e17b1aaa0398a451d4b6d2e8cc4ce8f6762e1fdad37ad2131f6344182cf4d7
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:50:57+00:00'
last_translated_at: '2026-03-13T21:20:00+09:00'
---

# PCIDriverKit

PCI(Peripheral Component Interconnect) 액세서리를 위한 device driver를 개발합니다.

## 개요

PCIDriverKit 프레임워크를 사용하면 PCI 및 PCI-Express 하드웨어의 custom 기능을 관리하는 드라이버를 개발할 수 있습니다. 시스템이 custom PCI 드라이버를 로드하면 [IOPCIDevice](https://developer.apple.com/documentation/pcidriverkit/iopcidevice) 객체를 provider로 드라이버에 전달합니다. 이 객체를 사용해 PCI 하드웨어의 구성과 메모리를 읽고 쓸 수 있습니다.

macOS에서는 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용해 드라이버를 설치하고 업그레이드하십시오. iPadOS에서는 시스템이 호스트 앱과 함께 드라이버를 자동으로 발견하고 업그레이드합니다.

:::note 참고
PCIDriverKit은 macOS에서는 Intel 및 Apple Silicon 기기에서 사용할 수 있고, iPadOS에서는 M 시리즈 칩을 탑재한 기기에서 사용할 수 있습니다.
:::

:::topic-grid
## entitlement
- [com.apple.developer.driverkit.transport.pci](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.transport.pci): custom 드라이버가 지원하는 PCI device descriptor 배열입니다.
:::

:::topic-grid
## 샘플
- [DriverKit sample code](https://developer.apple.com/documentation/DriverKit/driverkit-sample-code): DriverKit 계열 프레임워크를 사용해 macOS device driver를 작성하는 방법을 보여주는 프로젝트를 살펴봅니다.
- [Connecting a network driver](https://developer.apple.com/documentation/pcidriverkit/connecting-a-network-driver): 시스템의 네트워크 프로토콜 스택과 상호 작용하는 Ethernet 드라이버를 만듭니다.
:::

:::topic-grid
## 디바이스 인터페이스
- [Creating Custom PCIe Drivers for Thunderbolt Devices](https://developer.apple.com/documentation/pcidriverkit/creating-custom-pcie-drivers-for-thunderbolt-devices): Thunderbolt 기기의 custom 기능을 지원하는 DriverKit extension을 만듭니다.
- [IOPCIDevice](https://developer.apple.com/documentation/pcidriverkit/iopcidevice): custom PCI 하드웨어에 대한 접근을 관리하는 DriverKit provider 객체입니다.
:::

:::topic-grid
## 참고 자료
- [PCIDriverKit Enumerations](https://developer.apple.com/documentation/pcidriverkit/pcidriverkit-enumerations)
- [PCIDriverKit Data Types](https://developer.apple.com/documentation/pcidriverkit/pcidriverkit-data-types)
- [PCIDriverKit Macros](https://developer.apple.com/documentation/pcidriverkit/pcidriverkit-macros)
:::

:::topic-grid
## 매크로
- [kIOPCIACSCapabilitiesKey](https://developer.apple.com/documentation/pcidriverkit/kiopciacscapabilitieskey)
- [kIOPCIAERCapabilitiesKey](https://developer.apple.com/documentation/pcidriverkit/kiopciaercapabilitieskey)
- [kIOPCIExpressDeviceCapabilities2Key](https://developer.apple.com/documentation/pcidriverkit/kiopciexpressdevicecapabilities2key)
- [kIOPCIExpressDeviceCapabilitiesKey](https://developer.apple.com/documentation/pcidriverkit/kiopciexpressdevicecapabilitieskey)
- [kIOPCIExpressLinkCapabilities2Key](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresslinkcapabilities2key)
- [kIOPCIExpressRootCapabilitiesKey](https://developer.apple.com/documentation/pcidriverkit/kiopciexpressrootcapabilitieskey)
- [kIOPCIExpressSlotCapabilities2Key](https://developer.apple.com/documentation/pcidriverkit/kiopciexpressslotcapabilities2key)
- [kIOPCIFPBCapabilitiesKey](https://developer.apple.com/documentation/pcidriverkit/kiopcifpbcapabilitieskey)
- [kIOPCIL1PMCapabilitiesKey](https://developer.apple.com/documentation/pcidriverkit/kiopcil1pmcapabilitieskey)
- [kIOPCIMSIMessageControlKey](https://developer.apple.com/documentation/pcidriverkit/kiopcimsimessagecontrolkey)
- [kIOPCIMSIXMessageControlKey](https://developer.apple.com/documentation/pcidriverkit/kiopcimsixmessagecontrolkey)
- [kIOPCIPTMCapabilitiesKey](https://developer.apple.com/documentation/pcidriverkit/kiopciptmcapabilitieskey)
- [kIOPCIPowerManagementCapabilitiesKey](https://developer.apple.com/documentation/pcidriverkit/kiopcipowermanagementcapabilitieskey)
:::

:::topic-grid
## 열거형 케이스
- [kIOPCICapabilityIDAF](https://developer.apple.com/documentation/pcidriverkit/kiopcicapabilityidaf)
- [kIOPCICapabilityIDEnhancedAllocation](https://developer.apple.com/documentation/pcidriverkit/kiopcicapabilityidenhancedallocation)
- [kIOPCICapabilityIDSATAConfiguration](https://developer.apple.com/documentation/pcidriverkit/kiopcicapabilityidsataconfiguration)
- [kIOPCIExpressCapabilityIDAMD](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidamd)
- [kIOPCIExpressCapabilityIDATS](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidats)
- [kIOPCIExpressCapabilityIDAlternateProtocol](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidalternateprotocol)
- [kIOPCIExpressCapabilityIDCAC](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidcac)
- [kIOPCIExpressCapabilityIDDPA](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityiddpa)
- [kIOPCIExpressCapabilityIDDPC](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityiddpc)
- [kIOPCIExpressCapabilityIDDVSEC](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityiddvsec)
- [kIOPCIExpressCapabilityIDDataLinkFeature](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityiddatalinkfeature)
- [kIOPCIExpressCapabilityIDFRSQueueing](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidfrsqueueing)
- [kIOPCIExpressCapabilityIDHierarchyID](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidhierarchyid)
- [kIOPCIExpressCapabilityIDLNR](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidlnr)
- [kIOPCIExpressCapabilityIDLaneMarginingRx](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidlanemarginingrx)
- [kIOPCIExpressCapabilityIDMFVC](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidmfvc)
- [kIOPCIExpressCapabilityIDMPCIe](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidmpcie)
- [kIOPCIExpressCapabilityIDMRIOV](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidmriov)
- [kIOPCIExpressCapabilityIDMulticast](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidmulticast)
- [kIOPCIExpressCapabilityIDNPEM](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidnpem)
- [kIOPCIExpressCapabilityIDPASID](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidpasid)
- [kIOPCIExpressCapabilityIDPL16GTs](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidpl16gts)
- [kIOPCIExpressCapabilityIDPL32GTs](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidpl32gts)
- [kIOPCIExpressCapabilityIDPMUX](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidpmux)
- [kIOPCIExpressCapabilityIDPRI](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidpri)
- [kIOPCIExpressCapabilityIDRCECEndpointAssociation](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidrcecendpointassociation)
- [kIOPCIExpressCapabilityIDRCInternalLinkCtrl](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidrcinternallinkctrl)
- [kIOPCIExpressCapabilityIDRCLinkDeclaration](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidrclinkdeclaration)
- [kIOPCIExpressCapabilityIDReadinessTimeReporting](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidreadinesstimereporting)
- [kIOPCIExpressCapabilityIDResizableBAR](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidresizablebar)
- [kIOPCIExpressCapabilityIDRootComplexRegBlock](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidrootcomplexregblock)
- [kIOPCIExpressCapabilityIDSFI](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidsfi)
- [kIOPCIExpressCapabilityIDSPCIe](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidspcie)
- [kIOPCIExpressCapabilityIDSRIOV](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidsriov)
- [kIOPCIExpressCapabilityIDTPHRequester](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidtphrequester)
- [kIOPCIExpressCapabilityIDVC_MFVCPresent](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidvc_mfvcpresent)
- [kIOPCIExpressCapabilityIDVFResizableBAR](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidvfresizablebar)
- [kIOPCIExpressCapabilityIDVSEC](https://developer.apple.com/documentation/pcidriverkit/kiopciexpresscapabilityidvsec)
- [kIOPCISlotStatusAttentionButtonPressed](https://developer.apple.com/documentation/pcidriverkit/kiopcislotstatusattentionbuttonpressed)
- [kIOPCISlotStatusCommandCompleted](https://developer.apple.com/documentation/pcidriverkit/kiopcislotstatuscommandcompleted)
- [kIOPCISlotStatusDataLinkLayerStateChanged](https://developer.apple.com/documentation/pcidriverkit/kiopcislotstatusdatalinklayerstatechanged)
- [kIOPCISlotStatusElectromechanicalInterlockState](https://developer.apple.com/documentation/pcidriverkit/kiopcislotstatuselectromechanicalinterlockstate)
- [kIOPCISlotStatusMRLSensorChanged](https://developer.apple.com/documentation/pcidriverkit/kiopcislotstatusmrlsensorchanged)
- [kIOPCISlotStatusMRLSensorState](https://developer.apple.com/documentation/pcidriverkit/kiopcislotstatusmrlsensorstate)
- [kIOPCISlotStatusPowerFaultDetected](https://developer.apple.com/documentation/pcidriverkit/kiopcislotstatuspowerfaultdetected)
- [kIOPCISlotStatusPresenceDetectChanged](https://developer.apple.com/documentation/pcidriverkit/kiopcislotstatuspresencedetectchanged)
- [kIOPCISlotStatusPresenceDetectState](https://developer.apple.com/documentation/pcidriverkit/kiopcislotstatuspresencedetectstate)
:::
