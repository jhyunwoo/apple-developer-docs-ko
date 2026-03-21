---
route: /documentation/InputMethodKit
source_url: https://developer.apple.com/documentation/InputMethodKit
source_locale: en-US
section: docc
content_type: symbol
title: InputMethodKit
original_title: InputMethodKit
source_hash: 28a52cef8a4775874f3a209e43f681935f187652d7d389b48a87c7a2ce794fef
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:16:25+00:00'
last_translated_at: '2026-03-13T08:28:00+00:00'
---

# InputMethodKit

입력기를 개발하고 클라이언트 애플리케이션, 후보 창, 입력기 모드와의 통신을 관리합니다.

## 개요

OS X v10.5에서 도입된 Input Method Kit는 기존 Mac 프로그래밍 인터페이스보다 훨씬 적은 코드로 입력기를 개발할 수 있게 해 주는 간결한 프로그래밍 인터페이스를 제공합니다. Text Services Manager와 완전히 통합되어 있으며, 32비트 애플리케이션이 64비트 애플리케이션과 함께 동작할 수 있도록 합니다.

Input Method Kit는 클라이언트 애플리케이션, 후보 창, 입력기 모드와의 통신을 관리하는 클래스와 프로토콜을 제공합니다. 입력기는 변환 엔진에서 텍스트를 제공하고(변환 엔진은 C, C++, Objective-C, Python 등 어떤 언어로도 작성할 수 있음), 키 바인딩과 선택적 이벤트 처리를 제공하며, 확장된 `Info.plist` 파일에 입력기 정보를 포함합니다. 또한 입력기 전용 명령이나 환경설정을 지원하는 메뉴 항목을 제공할 수도 있습니다.

:::topic-grid
## 클래스
- [IMKCandidates](https://developer.apple.com/documentation/inputmethodkit/imkcandidates): 사용자에게 후보를 표시하고, 사용자가 후보를 선택하면 적절한 객체에 이를 알리는 클래스입니다. 후보는 특정 입력 시퀀스에 대한 대체 문자입니다. 이 클래스는 입력기에서 후보 창을 사용하는 기능을 지원하며, 사용은 선택 사항입니다. 모든 입력기에 후보 창이 필요한 것은 아닙니다.
- [IMKInputController](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller): 사용자 정의 입력 컨트롤러 클래스의 기반 클래스를 제공하는 클래스입니다. 입력기의 `main` 함수에서 할당되는 이 클래스는 클라이언트 애플리케이션이 생성하는 각 입력 세션마다 입력 컨트롤러 객체를 만듭니다. 각 입력 세션마다 대응되는 객체가 하나씩 존재합니다.
- [IMKServer](https://developer.apple.com/documentation/inputmethodkit/imkserver): 입력기에 대한 클라이언트 연결을 관리하는 클래스입니다. 입력기의 `main` 함수를 작성할 때 이 객체를 생성합니다. 일반적으로 이 클래스를 재정의할 필요는 없습니다.
:::

:::topic-grid
## 프로토콜
- [IMKMouseHandling](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling): 입력기가 마우스 이벤트를 처리하기 위해 구현할 수 있는 메서드를 정의하는 프로토콜입니다.
- [IMKServerInput](https://developer.apple.com/documentation/inputmethodkit/imkserverinput): 텍스트 이벤트를 수신하기 위한 메서드를 정의하는 비공식 프로토콜입니다. 이벤트를 수신하는 방법이 세 가지 있기 때문에 의도적으로 정식 프로토콜로 만들지 않았습니다. 입력기는 다음 접근 방식 중 하나를 선택하고 그에 맞는 메서드를 구현합니다.
- [IMKStateSetting](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting): 입력기의 상태를 나타내는 값을 설정하거나 접근하기 위한 메서드를 정의하는 프로토콜입니다.
:::

:::topic-grid
## 참고 자료
- [InputMethodKit Enumerations](https://developer.apple.com/documentation/inputmethodkit/inputmethodkit-enumerations)
- [InputMethodKit Constants](https://developer.apple.com/documentation/inputmethodkit/inputmethodkit-constants)
- [InputMethodKit Data Types](https://developer.apple.com/documentation/inputmethodkit/inputmethodkit-data_types)
:::
