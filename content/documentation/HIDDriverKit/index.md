---
route: /documentation/HIDDriverKit
source_url: https://developer.apple.com/documentation/HIDDriverKit
source_locale: en-US
section: docc
content_type: symbol
title: HIDDriverKit
original_title: HIDDriverKit
source_hash: 501d1f0c0dad9ad934edddeab0060a0733158e24a59894355f9dc95e6fe05c66
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:27:46+00:00'
last_translated_at: '2026-03-13T23:24:00+09:00'
---

# HIDDriverKit

키보드, 포인팅 장치, 펜과 터치 패드 같은 digitizer를 포함한 human-interface device용 드라이버를 개발합니다.

## 개요

HIDDriverKit 프레임워크는 human interface device용 드라이버를 개발하기 위한 C++ 클래스를 제공합니다. HIDDriverKit은 [DriverKit](https://developer.apple.com/documentation/DriverKit)에 정의된 핵심 타입을 사용하며, human interface device 개발에 특화된 기능을 추가합니다.

DriverKit과 HIDDriverKit으로 드라이버를 개발한 뒤, 이를 [System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용해 사용자의 Mac에 드라이버를 설치하고 업그레이드하는 앱에 패키징합니다.

:::note Note
HIDDriverKit은 macOS에서 사용할 수 있습니다.
:::

:::topic-grid
## 핵심 항목
- [com.apple.developer.driverkit.transport.hid](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.transport.hid): 드라이버가 human interface device와 통신하는지를 나타내는 Boolean 값입니다.
- [Handling Keyboard Events from a Human Interface Device](https://developer.apple.com/documentation/hiddriverkit/handling-keyboard-events-from-a-human-interface-device): human interface device의 키보드 관련 데이터를 처리하고 시스템으로 이벤트를 전달합니다.
- [Handling Stylus Input from a Human Interface Device](https://developer.apple.com/documentation/hiddriverkit/handling-stylus-input-from-a-human-interface-device): human interface device의 스타일러스 관련 입력을 처리하고 시스템으로 이벤트를 전달합니다.
:::

:::topic-grid
## 샘플
- [DriverKit sample code](https://developer.apple.com/documentation/DriverKit/driverkit-sample-code): DriverKit 계열 프레임워크로 macOS device driver를 작성하는 방법을 보여 주는 프로젝트를 살펴봅니다.
:::

:::topic-grid
## 드라이버 인터페이스
- [com.apple.developer.driverkit.family.hid.eventservice](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.eventservice): 드라이버가 시스템에 HID 관련 이벤트 서비스를 제공하는지를 나타내는 Boolean 값입니다.
- [IOUserHIDEventDriver](https://developer.apple.com/documentation/hiddriverkit/iouserhideventdriver): HID device에서 발생하는 키보드, digitizer, scrolling, pointer 이벤트를 시스템으로 전달하는 완전한 드라이버 객체입니다.
- [IOUserHIDEventService](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice): HID report 데이터를 파싱해 이벤트 전달에 사용할 수 있는 요소로 변환하는 서비스입니다.
- [IOHIDEventService](https://developer.apple.com/documentation/hiddriverkit/iohideventservice): 시스템으로 이벤트를 전달하는 device 또는 operating system 서비스를 구현하기 위한 기본 클래스입니다.
:::

:::topic-grid
## 제공자
- [com.apple.developer.driverkit.family.hid.device](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.device): 드라이버가 시스템에 HID 관련 서비스를 제공하는지를 나타내는 Boolean 값입니다.
- [IOHIDInterface](https://developer.apple.com/documentation/hiddriverkit/iohidinterface): HID device 인터페이스를 위한 provider 객체입니다.
- [IOUserUSBHostHIDDevice](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice): HID 상호 작용을 지원하는 USB device용 provider 객체입니다.
- [IOUserHIDDevice](https://developer.apple.com/documentation/hiddriverkit/iouserhiddevice): 사용자와의 상호 작용을 지원하는 device용 provider 객체입니다.
- [IOHIDDevice](https://developer.apple.com/documentation/hiddriverkit/iohiddevice): 모든 HID device provider의 저수준 동작을 담는 객체입니다.
:::

:::topic-grid
## 이벤트
- [IOHIDDigitizerStylusData](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizerstylusdata): digitizer stylus 데이터를 담는 구조체입니다.
- [IOHIDDigitizerTouchData](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizertouchdata): 현재 digitizer touch 데이터를 담는 구조체입니다.
:::

:::topic-grid
## HID Usage Tables
- [HID Usage Tables](https://developer.apple.com/documentation/hiddriverkit/hid-usage-tables): HID device가 드라이버에 보고할 수 있는 데이터 타입을 식별합니다.
- [Match Criteria](https://developer.apple.com/documentation/hiddriverkit/match-criteria): 시스템이 드라이버를 device와 매칭할 때 사용하는 기준을 지정합니다.
:::

:::topic-grid
## HID device 데이터
- [IOHIDElement](https://developer.apple.com/documentation/hiddriverkit/iohidelement): HID 입력 report에서 파싱한 정보를 담는 객체입니다.
- [IOHIDDigitizerCollection](https://developer.apple.com/documentation/hiddriverkit/iohiddigitizercollection): digitizer 관련 데이터를 담는 요소 컬렉션입니다.
- [com.apple.developer.hid.virtual.device](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.hid.virtual.device): 드라이버가 가상 HID device를 생성하는지를 나타내는 Boolean 값입니다.
- [Low-Level Information](https://developer.apple.com/documentation/hiddriverkit/low-level-information): HID 드라이버를 지원하는 기반 구조를 이해합니다.
:::

:::topic-grid
## 참고 자료
- [HIDDriverKit Macros](https://developer.apple.com/documentation/hiddriverkit/hiddriverkit-macros)
:::

:::topic-grid
## 매크로
- [kIOHIDDeviceApprovedCarPlayDeviceKey](https://developer.apple.com/documentation/hiddriverkit/kiohiddeviceapprovedcarplaydevicekey)
- [kIOHIDDeviceCarPlayDeviceKey](https://developer.apple.com/documentation/hiddriverkit/kiohiddevicecarplaydevicekey)
- [kIOHIDEventServiceSensorControlOptionsKey](https://developer.apple.com/documentation/hiddriverkit/kiohideventservicesensorcontroloptionskey)
- [kIOHIDSupportedEventMaskKey](https://developer.apple.com/documentation/hiddriverkit/kiohidsupportedeventmaskkey)
- [kIOHIDSupportedKeyboardUsagePairsKey](https://developer.apple.com/documentation/hiddriverkit/kiohidsupportedkeyboardusagepairskey)
- [kIOHIDSupportedVendorUsagePairsKey](https://developer.apple.com/documentation/hiddriverkit/kiohidsupportedvendorusagepairskey)
:::

:::topic-grid
## 열거형 케이스
- [kHIDUsage_GenDevControls_BatteryStrength](https://developer.apple.com/documentation/hiddriverkit/khidusage_gendevcontrols_batterystrength)
- [kHIDUsage_LED_BlueLEDChannel](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_blueledchannel)
- [kHIDUsage_LED_GoodStatus](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_goodstatus)
- [kHIDUsage_LED_GreenLEDChannel](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_greenledchannel)
- [kHIDUsage_LED_IndicatorBlue](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_indicatorblue)
- [kHIDUsage_LED_IndicatorOrange](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_indicatororange)
- [kHIDUsage_LED_LEDIntensity](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_ledintensity)
- [kHIDUsage_LED_RGB_LED](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_rgb_led)
- [kHIDUsage_LED_RedLEDChannel](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_redledchannel)
- [kHIDUsage_LED_SystemMicrophoneMute](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_systemmicrophonemute)
- [kHIDUsage_LED_WarningStatus](https://developer.apple.com/documentation/hiddriverkit/khidusage_led_warningstatus)
- [kHIDUsage_Snsr_Biometric_HeartRate](https://developer.apple.com/documentation/hiddriverkit/khidusage_snsr_biometric_heartrate)
- [kHIDUsage_Snsr_Data_Biometric_HeartRate](https://developer.apple.com/documentation/hiddriverkit/khidusage_snsr_data_biometric_heartrate)
- [kHIDUsage_Snsr_Motion_GravityVector](https://developer.apple.com/documentation/hiddriverkit/khidusage_snsr_motion_gravityvector)
- [kHIDUsage_Snsr_Motion_LinearAccelerometer](https://developer.apple.com/documentation/hiddriverkit/khidusage_snsr_motion_linearaccelerometer)
:::

:::topic-grid
## 열거형
- [IOHIDServiceSensorControlOptions](https://developer.apple.com/documentation/hiddriverkit/iohidservicesensorcontroloptions)
:::
