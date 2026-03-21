---
route: /documentation/kernel
source_url: https://developer.apple.com/documentation/kernel
source_locale: en-US
section: docc
content_type: symbol
title: Kernel
original_title: Kernel
source_hash: eed300a9893ce3bf3f3018ec478cd908527d8f3cdfd1972e35deba658757120e
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:15:07+00:00'
last_translated_at: '2026-03-14T00:54:00+09:00'
---

# Kernel

커널 상주 장치 드라이버와 커널 확장을 개발합니다.

## 개요

Kernel 프레임워크는 커널 상주 장치 드라이버와 기타 커널 확장을 위한 API와 지원 기능을 제공합니다. 이 프레임워크는 I/O Kit 장치 드라이버의 기본 클래스([IOService](https://developer.apple.com/documentation/kernel/ioservice-5h)), 여러 도우미 클래스, 그리고 다양한 장치 유형을 지원하는 family를 정의합니다.

:::topic-grid
## 커널 확장
- [Implementing drivers, system extensions, and kexts](https://developer.apple.com/documentation/kernel/implementing_drivers_system_extensions_and_kexts): 하드웨어와 통신하고 저수준 서비스를 제공하기 위한 드라이버와 system extension을 만들고, 일부 작업에만 kernel extension을 사용합니다.
- [Installing a custom kernel extension](https://developer.apple.com/documentation/apple-silicon/installing-a-custom-kernel-extension): 사용자 정의 installer 패키지로 kernel extension을 설치하고, 사용자가 설치 과정을 이해하도록 돕습니다.
- [Debugging a custom kernel extension](https://developer.apple.com/documentation/apple-silicon/debugging-a-custom-kernel-extension): 두 번째 Mac에서 사용자 정의 kernel extension의 디버깅을 활성화하도록 시스템을 구성합니다.
- [Generating a Non-Maskable Interrupt](https://developer.apple.com/documentation/kernel/generating_a_non-maskable_interrupt): 대상 Mac의 kernel을 중단시키고 원격 debugger를 연결합니다.
:::

:::topic-grid
## IOKit 드라이버
- [IOKit Fundamentals](https://developer.apple.com/documentation/kernel/iokit_fundamentals): 타사 kernel extension을 사용해 사용자 정의 하드웨어용 드라이버를 구현합니다.
- [Hardware Families](https://developer.apple.com/documentation/kernel/hardware_families): USB 같은 특정 하드웨어 프로토콜과 표준 네트워크, 직렬, 오디오, 그래픽 인터페이스에 대한 지원을 추가합니다.
- [Driver Support](https://developer.apple.com/documentation/kernel/driver_support): device registry를 탐색하고 전원 관리 유틸리티와 기타 공유 드라이버 기능에 접근합니다.
- [libkern](https://developer.apple.com/documentation/kernel/libkern): kernel 라이브러리의 런타임 지원과 기본 클래스에 접근합니다.
:::

:::topic-grid
## BSD
- [architecture](https://developer.apple.com/documentation/kernel/architecture): 현재 플랫폼의 머신 수준 및 아키텍처 정보를 접근합니다.
- [bsm](https://developer.apple.com/documentation/kernel/bsm): 시스템의 리소스 사용량을 감사(audit)합니다.
- [hfs](https://developer.apple.com/documentation/kernel/hfs): HFS 파일 시스템 데이터 구조에 접근합니다.
- [kern](https://developer.apple.com/documentation/kernel/kern): clock, task, kernel extension, lock, compression 유틸리티를 포함한 kernel 수준 인터페이스에 접근합니다.
- [Math](https://developer.apple.com/documentation/kernel/math): 수학 연산을 수행하고 정수, float, double 값을 다룹니다.
- [miscfs](https://developer.apple.com/documentation/kernel/miscfs): device node와 기타 파일 시스템 엔티티에 접근합니다.
- [net](https://developer.apple.com/documentation/kernel/net): 네트워크 관련 유틸리티에 접근합니다.
- [Strings](https://developer.apple.com/documentation/kernel/strings): 문자열을 비교, 변환, 연결하고 그 결과 콘텐츠에 접근합니다.
- [sys](https://developer.apple.com/documentation/kernel/sys): 시간, 파일 시스템, 시스템 정보를 위한 일반 시스템 유틸리티에 접근합니다.
- [vfs](https://developer.apple.com/documentation/kernel/vfs): 가상 파일 시스템 인터페이스에 접근합니다.
- [vm](https://developer.apple.com/documentation/kernel/vm): 가상 메모리 시스템과 상호 작용합니다.
:::

:::topic-grid
## Mach
- [mach](https://developer.apple.com/documentation/kernel/mach): 프로세서, 메모리, 스레드, semaphore 지원을 포함한 Mach 인터페이스에 접근합니다.
- [mach-o](https://developer.apple.com/documentation/kernel/mach-o): Mach-O 런타임과 연관된 인터페이스에 접근합니다.
:::

:::topic-grid
## 유틸리티
- [Debugging](https://developer.apple.com/documentation/kernel/debugging): kernel debugger, assertion, exception, backtrace, logging을 사용해 kernel extension을 디버그합니다.
- [AppleDSP](https://developer.apple.com/documentation/kernel/appledsp): 데이터에 대해 디지털 신호 처리를 수행합니다.
:::

:::topic-grid
## Deprecated
- [Deprecated Symbols](https://developer.apple.com/documentation/kernel/deprecated_symbols): 더 이상 지원되지 않는 symbol과 그 대체 항목을 검토합니다.
:::

:::topic-grid
## 추가 참고 자료
- [Kernel Functions](https://developer.apple.com/documentation/kernel/kernel_functions)
- [Kernel Structures](https://developer.apple.com/documentation/kernel/kernel_structures)
- [Kernel Data Types](https://developer.apple.com/documentation/kernel/kernel_data_types)
- [Kernel Enumerations](https://developer.apple.com/documentation/kernel/kernel_enumerations)
- [Kernel Constants](https://developer.apple.com/documentation/kernel/kernel_constants)
:::

:::topic-grid
## 클래스
- [IOCatalogue](https://developer.apple.com/documentation/kernel/iocatalogue): IOKit 드라이버 personality를 위한 인커널 데이터베이스입니다.
- [IOEventLink](https://developer.apple.com/documentation/kernel/ioeventlink)
- [IOEventLinkInterface](https://developer.apple.com/documentation/kernel/ioeventlinkinterface)
- [IOGuardPageMemoryDescriptor](https://developer.apple.com/documentation/kernel/ioguardpagememorydescriptor)
- [IOHIDTranslationService](https://developer.apple.com/documentation/kernel/iohidtranslationservice)
- [IOServiceStateNotificationDispatchSource](https://developer.apple.com/documentation/driverkit/ioservicestatenotificationdispatchsource)
- [IOServiceStateNotificationDispatchSourceInterface](https://developer.apple.com/documentation/kernel/ioservicestatenotificationdispatchsourceinterface)
- [IOWorkGroup](https://developer.apple.com/documentation/kernel/ioworkgroup)
- [IOWorkGroupInterface](https://developer.apple.com/documentation/kernel/ioworkgroupinterface)
- [OSAction_IOHIDEventService__CopyEvent](https://developer.apple.com/documentation/kernel/osaction_iohideventservice_copyevent)
- [OSAction_IOHIDEventService__CopyEventInterface](https://developer.apple.com/documentation/kernel/osaction_iohideventservice_copyeventinterface)
- [OSAction_IOHIDEventService__SetLED](https://developer.apple.com/documentation/kernel/osaction_iohideventservice_setled)
- [OSAction_IOHIDEventService__SetLEDInterface](https://developer.apple.com/documentation/kernel/osaction_iohideventservice_setledinterface)
- [OSAction_IOHIDEventService__SetUserProperties](https://developer.apple.com/documentation/kernel/osaction_iohideventservice_setuserproperties)
- [OSAction_IOHIDEventService__SetUserPropertiesInterface](https://developer.apple.com/documentation/kernel/osaction_iohideventservice_setuserpropertiesinterface)
:::
