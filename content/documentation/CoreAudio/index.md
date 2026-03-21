---
route: /documentation/CoreAudio
source_url: https://developer.apple.com/documentation/CoreAudio
source_locale: en-US
section: docc
content_type: symbol
title: Core Audio
original_title: Core Audio
source_hash: aa0a895b9e6364b711132f05a830138683654b4ab59f2c373dfde9e979d529d3
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:24:09+00:00'
last_translated_at: '2026-03-13T09:10:00+00:00'
---

# Core Audio

Core Audio 프레임워크를 사용해 기기의 오디오 하드웨어와 상호 작용합니다.

:::topic-grid
## 드라이버
- [오디오 서버 드라이버 플러그인 생성하기](https://developer.apple.com/documentation/coreaudio/creating-an-audio-server-driver-plug-in): 사용자 정의 드라이버 플러그인을 만들어 가상 오디오 기기를 빌드합니다.
- [오디오 서버 플러그인과 드라이버 확장 빌드하기](https://developer.apple.com/documentation/coreaudio/building-an-audio-server-plug-in-and-driver-extension): macOS에서 오디오 기기를 지원하기 위한 플러그인과 드라이버 확장을 생성합니다.
- [Core Audio tap으로 시스템 오디오 캡처하기](https://developer.apple.com/documentation/coreaudio/capturing-system-audio-with-core-audio-taps): Core Audio tap을 사용해 프로세스 또는 프로세스 그룹에서 나가는 오디오를 캡처합니다.
:::

:::topic-grid
## 참고 자료
- [Core Audio Structures](https://developer.apple.com/documentation/coreaudio/core-audio-structures)
- [Core Audio Data Types](https://developer.apple.com/documentation/coreaudio/core-audio-data-types)
- [Core Audio Functions](https://developer.apple.com/documentation/coreaudio/core-audio-functions)
- [Core Audio Constants](https://developer.apple.com/documentation/coreaudio/core-audio-constants)
- [Core Audio Enumerations](https://developer.apple.com/documentation/coreaudio/core-audio-enumerations)
:::

:::topic-grid
## 클래스
- [AudioHardwareAggregateDevice](https://developer.apple.com/documentation/coreaudio/audiohardwareaggregatedevice): 여러 실제 기기나 tap의 입력 및 출력 스트림을 결합하는 가상 기기인 단일 오디오 aggregate device를 캡슐화하는 클래스입니다. 또한 I/O를 실행할 때 하위 기기와 하위 tap의 클록을 동기화해 스트림이 정렬되도록 합니다.
- [AudioHardwareBox](https://developer.apple.com/documentation/coreaudio/audiohardwarebox): 단일 오디오 박스를 캡슐화하는 클래스입니다. 오디오 박스는 다른 객체(보통 기기 객체)를 담는 컨테이너입니다. 박스는 자신을 식별하는 정보를 공개하며 활성화 또는 비활성화할 수 있습니다. 박스의 내용은 박스가 활성화되어 있을 때만 시스템에서 사용할 수 있습니다.
- [AudioHardwareClock](https://developer.apple.com/documentation/coreaudio/audiohardwareclock): 개별 오디오 클록을 캡슐화하는 클래스입니다. 모든 오디오 기기는 이 오디오 클록 클래스를 상속하며, 이 클래스는 여러 기본 속성을 제공하고 컨트롤 객체 목록을 포함합니다. 클록 객체는 aggregate device에서 시간 소스로 사용할 수 있지만 I/O 스트림은 포함하지 않습니다.
- [AudioHardwareControl](https://developer.apple.com/documentation/coreaudio/audiohardwarecontrol): 단일 오디오 컨트롤을 캡슐화하는 클래스입니다. gain, mute, 데이터 소스 선택 등 소유 객체의 특정 측면을 설명하거나 조작하는 속성을 제공합니다.
- [AudioHardwareDevice](https://developer.apple.com/documentation/coreaudio/audiohardwaredevice): 개별 오디오 기기를 캡슐화하는 클래스입니다. 오디오 기기는 I/O의 기본 단위 역할을 합니다. AudioHardwareDevice는 기기 상태에 접근하고 이를 조작하며 I/O를 실행하기 위한 속성과 메서드를 제공합니다.
- [AudioHardwareObject](https://developer.apple.com/documentation/coreaudio/audiohardwareobject): 오디오 HAL은 애플리케이션이 오디오 하드웨어에 접근할 수 있도록 추상화를 제공합니다. 이를 위해 HAL은 시스템의 여러 부분에 접근할 수 있는 소수의 오디오 객체를 제공합니다. 오디오 객체는 모두 상태를 설명하고 조작하는 속성 집합을 가집니다. AudioHardwareObject는 다른 모든 오디오 객체의 기반 클래스이므로, 모든 클래스가 이 속성 집합을 상속합니다.
- [AudioHardwarePlugin](https://developer.apple.com/documentation/coreaudio/audiohardwareplugin): 단일 오디오 HAL 플러그인을 캡슐화하는 클래스입니다. 이 플러그인은 HAL이 드라이버로 로드하는 CFBundle이며, 기기별 속성과 루틴을 구현합니다.
- [AudioHardwareProcess](https://developer.apple.com/documentation/coreaudio/audiohardwareprocess): 단일 오디오 프로세스를 캡슐화하는 클래스입니다. HAL에 연결된 클라이언트 프로세스 정보를 담고 있습니다.
- [AudioHardwareStream](https://developer.apple.com/documentation/coreaudio/audiohardwarestream): 단일 오디오 스트림을 캡슐화하는 클래스입니다. 이는 사용자/커널 경계를 넘어 데이터를 전송하기 위한 단일 버퍼를 나타냅니다. 따라서 AudioStream은 포맷 정보의 관문 역할을 하며, 각각 자신의 포맷과 사용 가능한 포맷 목록을 가집니다.
- [AudioHardwareSystem](https://developer.apple.com/documentation/coreaudio/audiohardwaresystem): HAL의 오디오 객체는 포함 관계 계층 구조로 정리됩니다. 이 계층 구조의 루트는 하나뿐인 시스템 클래스 인스턴스입니다. AudioHardwareSystem의 속성은 여러 기본 기기 같은 프로세스 전역 설정을 설명합니다. 시스템 객체는 또한 사용 가능한 모든 기기를 포함합니다.
- [AudioHardwareTap](https://developer.apple.com/documentation/coreaudio/audiohardwaretap): 단일 오디오 tap을 캡슐화하는 클래스입니다. 이는 프로세스 또는 프로세스 그룹에서 나가는 오디오를 캡처하고, aggregate device에서 입력 스트림 소스로 사용할 수 있습니다.
- [CATapDescription](https://developer.apple.com/documentation/coreaudio/catapdescription)
:::

:::topic-grid
## 프로토콜
- [PropertyListenerDelegate](https://developer.apple.com/documentation/coreaudio/propertylistenerdelegate): `AudioHardwareObject.addPropertyListener`에 등록된 속성이 변경될 때 알림을 받기 위한 delegate 프로토콜입니다.
:::

:::topic-grid
## 구조체
- [AudioHardwareError](https://developer.apple.com/documentation/coreaudio/audiohardwareerror): HAL이 반환하는 오류를 나타냅니다.
- [ManagedAudioChannelLayout](https://developer.apple.com/documentation/coreaudio/managedaudiochannellayout): 파일과 하드웨어에서 채널 레이아웃을 지정하는 데 사용하는 구조체입니다.
:::

:::topic-grid
## 변수
- [kAudioDevicePropertyWantsControlsRestored](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertywantscontrolsrestored)
- [kAudioDevicePropertyWantsStreamFormatsRestored](https://developer.apple.com/documentation/coreaudio/kaudiodevicepropertywantsstreamformatsrestored)
:::
