---
route: /documentation/DriverKit
source_url: https://developer.apple.com/documentation/DriverKit
source_locale: en-US
section: docc
content_type: symbol
title: DriverKit
original_title: DriverKit
source_hash: 395e5f8df51cbc2f7ce0ea53beb1d7886340a7a523cf7b2fce417ef3ffcee01c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:14:51+00:00'
last_translated_at: '2026-03-13T16:45:00+09:00'
---

# DriverKit

사용자 공간에서 실행되는 장치 드라이버를 개발합니다.

## 개요

DriverKit 프레임워크는 macOS와 iPadOS용 장치 드라이버의 기본 동작을 정의합니다. 이 프레임워크의 C++ 클래스는 드라이버의 기본 구조를 정의하고 이벤트 처리와 메모리 할당을 지원합니다. 또한 드라이버의 I/O 레지스트리 항목에 있는 숫자, 문자열, 기타 데이터 타입을 검사하는 데 적합한 타입도 제공합니다. [USBDriverKit](https://developer.apple.com/documentation/USBDriverKit), [HIDDriverKit](https://developer.apple.com/documentation/HIDDriverKit), [NetworkingDriverKit](https://developer.apple.com/documentation/NetworkingDriverKit), [PCIDriverKit](https://developer.apple.com/documentation/PCIDriverKit), [SerialDriverKit](https://developer.apple.com/documentation/SerialDriverKit), [AudioDriverKit](https://developer.apple.com/documentation/AudioDriverKit) 같은 다른 프레임워크는 다양한 종류의 장치를 지원하는 데 필요한 구체적인 동작을 제공합니다.

DriverKit으로 빌드한 드라이버는 kernel extension이 아니라 사용자 공간에서 실행되므로 시스템 안정성과 보안이 향상됩니다. 드라이버는 app extension으로 만들고 기존 앱 내부에 포함해 배포합니다.

macOS에서는 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용해 드라이버를 설치하고 업그레이드합니다. iPadOS에서는 시스템이 호스트 앱과 함께 드라이버를 자동으로 검색하고 업그레이드합니다.

:::note Note
기본 DriverKit 프레임워크는 Apple silicon과 Intel 기반 Mac의 macOS, 그리고 M 시리즈 칩이 탑재된 기기의 iPadOS에서 사용할 수 있습니다. [USBDriverKit](https://developer.apple.com/documentation/USBDriverKit), [AudioDriverKit](https://developer.apple.com/documentation/AudioDriverKit) 같은 family framework의 사용 가능 여부는 플랫폼마다 다릅니다.
:::

:::topic-grid
## 핵심 사항
- [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts): 하드웨어와 통신하고 저수준 서비스를 제공하는 드라이버와 system extension을 생성하고, kernel extension은 소수의 작업에만 사용합니다.
- [Creating drivers for iPadOS](https://developer.apple.com/documentation/driverkit/creating-drivers-for-ipados): 플랫폼의 DriverKit 지원을 사용해 드라이버를 iPadOS로 확장합니다.
:::

:::topic-grid
## entitlement
- [Requesting Entitlements for DriverKit Development](https://developer.apple.com/documentation/driverkit/requesting-entitlements-for-driverkit-development): DriverKit 개발용 entitlement와 드라이버가 특정 장치 및 인터페이스와 상호 작용하는 데 필요한 다른 entitlement를 요청합니다.
- [com.apple.developer.driverkit](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit): extension이 사용자 공간 드라이버로 실행될 권한이 있는지 나타내는 Boolean 값입니다.
- [com.apple.developer.driverkit.userclient-access](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.userclient-access): 다른 DriverKit 서비스와 통신할 수 있는 macOS 드라이버 extension을 나타내는 문자열 배열입니다.
- [com.apple.developer.driverkit.allow-any-userclient-access](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.allow-any-userclient-access): macOS 드라이버가 어떤 애플리케이션으로부터도 user client 연결을 받아들일지 결정하는 Boolean 값입니다.
- [Communicates with Drivers](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.communicates-with-drivers): iPadOS 앱이 드라이버와 통신할 수 있는지 나타내는 Boolean 값입니다.
- [DriverKit Allow Third Party User Clients](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.allow-third-party-userclients): iPadOS 드라이버가 서드파티 user client의 호출을 받아들일지 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 샘플
- [DriverKit sample code](https://developer.apple.com/documentation/driverkit/driverkit-sample-code): DriverKit 계열 프레임워크로 macOS 장치 드라이버를 작성하는 방법을 보여 주는 프로젝트를 살펴봅니다.
:::

:::topic-grid
## 서비스
- [Creating a Driver Using the DriverKit SDK](https://developer.apple.com/documentation/driverkit/creating-a-driver-using-the-driverkit-sdk): 회사 하드웨어 장치의 독점 기능을 지원하는 드라이버를 생성합니다.
- [Debugging and testing system extensions](https://developer.apple.com/documentation/driverkit/debugging-and-testing-system-extensions): macOS가 설치 과정에서 수행하는 보안 검사를 일시적으로 비활성화하여 system extension을 디버깅합니다.
- [IOService](https://developer.apple.com/documentation/driverkit/ioservice): 드라이버의 설정과 등록을 관리하는 기본 클래스입니다.
:::

:::topic-grid
## 이벤트 관리
- [IODispatchQueue](https://developer.apple.com/documentation/driverkit/iodispatchqueue): block의 직렬 실행을 관리하는 객체입니다.
- [IOInterruptDispatchSource](https://developer.apple.com/documentation/driverkit/iointerruptdispatchsource): 하드웨어 관련 인터럽트 이벤트를 드라이버에 보고하는 dispatch source입니다.
- [IOTimerDispatchSource](https://developer.apple.com/documentation/driverkit/iotimerdispatchsource): 특정 시점에 드라이버에 알림을 보내는 dispatch source입니다.
- [IODataQueueDispatchSource](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource): 공유 메모리 데이터 큐를 관리하는 dispatch source입니다.
- [IODispatchSource](https://developer.apple.com/documentation/driverkit/iodispatchsource): dispatch source의 공통 기본 클래스입니다.
- [OSAction](https://developer.apple.com/documentation/driverkit/osaction): 드라이버의 사용자 정의 동작을 실행하는 객체입니다.
:::

:::topic-grid
## 메모리 관리
- [IOBufferMemoryDescriptor](https://developer.apple.com/documentation/driverkit/iobuffermemorydescriptor): 호출자 주소 공간에 할당된 메모리 버퍼입니다.
- [IOMemoryDescriptor](https://developer.apple.com/documentation/driverkit/iomemorydescriptor): 메모리 내 위치를 설명하는 기본 클래스입니다.
- [IOMemoryMap](https://developer.apple.com/documentation/driverkit/iomemorymap): 현재 프로세스 또는 다른 프로세스의 기존 메모리 블록에 대한 참조입니다.
- [Memory Utilities](https://developer.apple.com/documentation/driverkit/memory-utilities): 메모리를 할당 및 해제하고 서로 다른 주소 공간의 메모리 포인터를 관리합니다.
:::

:::topic-grid
## 레지스트리 데이터 타입
- [OSArray](https://developer.apple.com/documentation/driverkit/osarray): 순서가 있고 임의 접근이 가능한 객체 컬렉션을 위한 컨테이너입니다.
- [OSDictionary](https://developer.apple.com/documentation/driverkit/osdictionary): 요소가 키-값 쌍인 컬렉션을 위한 컨테이너입니다.
- [OSBoolean](https://developer.apple.com/documentation/driverkit/osboolean): 참 또는 거짓 값을 위한 컨테이너입니다.
- [OSData](https://developer.apple.com/documentation/driverkit/osdata): 타입이 지정되지 않은 데이터를 위한 컨테이너입니다.
- [OSNumber](https://developer.apple.com/documentation/driverkit/osnumber): 정수 값을 위한 컨테이너입니다.
- [OSString](https://developer.apple.com/documentation/driverkit/osstring): 문자 배열을 관리하는 컨테이너입니다.
- [OSSerialization](https://developer.apple.com/documentation/driverkit/osserialization): 메시징에 적합한 바이너리 데이터 형식으로 직렬화된 하나 이상의 객체를 담는 컨테이너입니다.
- [OSCollection](https://developer.apple.com/documentation/driverkit/oscollection): DriverKit collection 객체의 기본 클래스입니다.
- [OSContainer](https://developer.apple.com/documentation/driverkit/oscontainer): DriverKit 데이터 객체의 기본 클래스입니다.
- [OSObject](https://developer.apple.com/documentation/driverkit/osobject): DriverKit 객체의 기본 클래스입니다.
- [OSSymbol](https://developer.apple.com/documentation/driverkit/ossymbol): 문자 배열을 관리하는 컨테이너입니다.
- [IOFixed](https://developer.apple.com/documentation/driverkit/iofixed): 고정 소수점 숫자입니다.
:::

:::topic-grid
## 외부 드라이버
- [IOUserClient](https://developer.apple.com/documentation/driverkit/iouserclient): 시스템이 관리하는 다른 서비스와의 연결입니다.
- [IOUserServer](https://developer.apple.com/documentation/driverkit/iouserserver): 시스템이 관리하는 서비스입니다.
- [com.apple.developer.driverkit.userclient-access](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.userclient-access): 다른 DriverKit 서비스와 통신할 수 있는 macOS 드라이버 extension을 나타내는 문자열 배열입니다.
- [Communicating between a DriverKit extension and a client app](https://developer.apple.com/documentation/driverkit/communicating-between-a-driverkit-extension-and-a-client-app): 입력을 검증해 다양한 종류의 데이터를 안전하게 송수신하고, callback을 저장 및 사용해 비동기적으로 통신합니다.
:::

:::topic-grid
## 런타임 지원
- [OSDynamicCast](https://developer.apple.com/documentation/driverkit/osdynamiccast): 가능하면 객체를 지정한 타입으로 안전하게 캐스팅합니다.
- [OSRequiredCast](https://developer.apple.com/documentation/driverkit/osrequiredcast): 객체가 올바른 타입이 아니면 프로세스를 중단하면서 지정한 타입으로 캐스팅합니다.
- [IMPL](https://developer.apple.com/documentation/driverkit/impl): 이 메서드의 superclass 구현이 kernel에서 실행된다는 것을 시스템에 알립니다.
- [TYPE](https://developer.apple.com/documentation/driverkit/type): 메서드 선언이 기존 메서드 시그니처를 따른다는 것을 표시합니다.
- [QUEUENAME](https://developer.apple.com/documentation/driverkit/queuename): 지정된 이름의 dispatch queue에서 메서드를 실행하라고 시스템에 알립니다.
- [SUPERDISPATCH](https://developer.apple.com/documentation/driverkit/superdispatch): 현재 메서드의 superclass 구현을 kernel에서 실행하라고 시스템에 알립니다.
- [IIG_KERNEL](https://developer.apple.com/documentation/driverkit/iig_kernel): 클래스 또는 메서드가 kernel 내부에서 실행된다는 것을 시스템에 알립니다.
- [LOCAL](https://developer.apple.com/documentation/driverkit/local): 메서드가 드라이버 extension의 프로세스 공간에서 로컬로 실행된다는 것을 시스템에 알립니다.
- [LOCALONLY](https://developer.apple.com/documentation/driverkit/localonly): 클래스 또는 메서드가 드라이버 extension의 프로세스 공간에서 로컬로 실행된다는 것을 시스템에 알립니다.
- [Error Codes](https://developer.apple.com/documentation/driverkit/error-codes): 작업이 실패한 이유를 확인합니다.
- [C++ Runtime Support](https://developer.apple.com/documentation/driverkit/c-runtime-support): DriverKit이 kernel 수준 작업을 지원하기 위해 사용하는 저수준 타입을 살펴봅니다.
:::

:::topic-grid
## 클래스
- [IOHistogramReporter](https://developer.apple.com/documentation/driverkit/iohistogramreporter)
- [IOReportLegend](https://developer.apple.com/documentation/driverkit/ioreportlegend)
- [IOReporter](https://developer.apple.com/documentation/driverkit/ioreporter)
- [IOServiceStateNotificationDispatchSource](https://developer.apple.com/documentation/driverkit/ioservicestatenotificationdispatchsource)
- [IOSimpleReporter](https://developer.apple.com/documentation/driverkit/iosimplereporter)
- [IOStateReporter](https://developer.apple.com/documentation/driverkit/iostatereporter)
- [OSBundle](https://developer.apple.com/documentation/driverkit/osbundle)
- [OSMappedFile](https://developer.apple.com/documentation/driverkit/osmappedfile)
:::

:::topic-grid
## 레퍼런스
- [DriverKit Structures](https://developer.apple.com/documentation/driverkit/driverkit-structures)
- [DriverKit Enumerations](https://developer.apple.com/documentation/driverkit/driverkit-enumerations)
- [DriverKit Constants](https://developer.apple.com/documentation/driverkit/driverkit-constants)
- [DriverKit Functions](https://developer.apple.com/documentation/driverkit/driverkit-functions)
- [DriverKit Data Types](https://developer.apple.com/documentation/driverkit/driverkit-data-types)
- [DriverKit Namespaces](https://developer.apple.com/documentation/driverkit/driverkit-namespaces)
:::

:::topic-grid
## 매크로
- [Macros](https://developer.apple.com/documentation/driverkit/driverkit-macros)
- [kIOPropertyHashTypeKey](https://developer.apple.com/documentation/driverkit/kiopropertyhashtypekey)
- [kIOPropertySHA3256Key](https://developer.apple.com/documentation/driverkit/kiopropertysha3256key)
- [kIOPropertySHA3384Key](https://developer.apple.com/documentation/driverkit/kiopropertysha3384key)
- [kIOPropertySHA3512Key](https://developer.apple.com/documentation/driverkit/kiopropertysha3512key)
- [kIOUserServrMaxExitReasonLength](https://developer.apple.com/documentation/driverkit/kiouserservrmaxexitreasonlength)
- [kIOUserServrMaxModulePathLength](https://developer.apple.com/documentation/driverkit/kiouserservrmaxmodulepathlength)
- [kIOUserServrMaxPanicReasonLength](https://developer.apple.com/documentation/driverkit/kiouserservrmaxpanicreasonlength)
- [queue_extend_first](https://developer.apple.com/documentation/driverkit/queue_extend_first)
- [queue_extend_last](https://developer.apple.com/documentation/driverkit/queue_extend_last)
:::

:::topic-grid
## 함수
- [IOSysCtlByName](https://developer.apple.com/documentation/driverkit/iosysctlbyname)
- [getpid](https://developer.apple.com/documentation/driverkit/getpid)
:::

:::topic-grid
## 열거형 케이스
- [kIOServicePMAssertionCPUBit](https://developer.apple.com/documentation/driverkit/kioservicepmassertioncpubit): `kIOServicePMAssertionCPUBit`가 설정되면 PM kernel은 잠자기 상태로 들어가는 대신 CPU와 코어 하드웨어를 “Dark Wake” 상태로 유지하려고 합니다.
- [kIOServicePMAssertionForceFullWakeupBit](https://developer.apple.com/documentation/driverkit/kioservicepmassertionforcefullwakeupbit): `kIOServicePMAssertionForceFullWakeupBit`가 설정되면 시스템은 잠든 직후 즉시 완전한 깨우기를 수행합니다.
- [kIOServicePowerCapabilityLPW](https://developer.apple.com/documentation/driverkit/kioservicepowercapabilitylpw)
- [kSCSICmd_ATA_PASS_THROUGH](https://developer.apple.com/documentation/driverkit/kscsicmd_ata_pass_through)
- [kSCSICmd_ATA_PASS_THROUGH_EXT](https://developer.apple.com/documentation/driverkit/kscsicmd_ata_pass_through_ext)
:::

:::topic-grid
## 타입 별칭
- [pid_t](https://developer.apple.com/documentation/driverkit/pid_t)
:::
