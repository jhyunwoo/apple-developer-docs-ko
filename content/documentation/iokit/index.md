---
route: /documentation/iokit
source_url: https://developer.apple.com/documentation/iokit
source_locale: en-US
section: docc
content_type: symbol
title: IOKit
original_title: IOKit
source_hash: ff7818ff6ed1210b77d55ffe3e924fd5845a294bc363b0e939280eca4b48d8ee
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:15:06+00:00'
last_translated_at: '2026-03-14T00:54:00+09:00'
---

# IOKit

앱과 서비스에서 하드웨어 기기와 드라이버에 접근합니다.

## 개요

IOKit 프레임워크는 device-interface 메커니즘을 통해 드라이버와 nub 같은 IOKit 객체에 대해 커널 외부 접근을 구현합니다.

:::important 참고
macOS 11 이상에서 지원되는 기기는 [DriverKit](https://developer.apple.com/documentation/driverkit)이 필요합니다. 앱과 서비스 안에서는 IOKit을 사용해 기기를 발견하고 활용하십시오.
:::

:::topic-grid
## 직렬 포트
- [Communicating with a Modem on a Serial Port](https://developer.apple.com/documentation/iokit/communicating_with_a_modem_on_a_serial_port): IOKit을 사용해 직렬 포트에 연결된 모뎀을 찾고 연결합니다.
:::

:::topic-grid
## 참고 자료
- [IODataQueueClient.h](https://developer.apple.com/documentation/iokit/iodataqueueclient_h)
- [IOKitLib.h](https://developer.apple.com/documentation/iokit/iokitlib_h)
- [IOTypes.h User-Space](https://developer.apple.com/documentation/iokit/iotypes_h_user-space)
- [IOKit Structures](https://developer.apple.com/documentation/iokit/iokit_structures)
- [IOKit Enumerations](https://developer.apple.com/documentation/iokit/iokit_enumerations)
- [IOKit Constants](https://developer.apple.com/documentation/iokit/iokit_constants)
- [IOKit Functions](https://developer.apple.com/documentation/iokit/iokit_functions)
- [IOKit Data Types](https://developer.apple.com/documentation/iokit/iokit_data_types)
:::
