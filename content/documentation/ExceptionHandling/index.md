---
route: /documentation/ExceptionHandling
source_url: https://developer.apple.com/documentation/ExceptionHandling
source_locale: en-US
section: docc
content_type: symbol
title: Exception Handling
original_title: Exception Handling
source_hash: 3a4538834cc5c7e7adeaef84c754b1ef184700a6e17ad8e9d4fce9a1d94f4d32
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:22:19+00:00'
last_translated_at: '2026-03-13T16:55:00+09:00'
---

# Exception Handling

코드에서 예외적인 상태를 모니터링하고 디버그합니다.

## 개요

이 문서 모음은 Exception Handling 프레임워크의 API 레퍼런스를 제공합니다. 이 프레임워크는 Objective-C 코드에서 예외적인 상태를 모니터링하고 디버깅하기 위한 기능을 제공합니다.

현재 이 문서 모음에는 하나의 클래스 레퍼런스만 포함되어 있습니다. `NSExceptionHandler.h`에 정의된 [NSExceptionHandler](https://developer.apple.com/documentation/exceptionhandling/nsexceptionhandler) 클래스 레퍼런스입니다.

:::topic-grid
## 클래스
- [NSExceptionHandler](https://developer.apple.com/documentation/exceptionhandling/nsexceptionhandler): Objective-C 프로그램에서 예외적인 상태를 모니터링하고 디버깅하는 기능을 제공하는 클래스입니다. 이 클래스는 특수한 uncaught exception handler를 함수로 설치하는 방식으로 동작합니다. 따라서 `NSExceptionHandler`의 서비스를 사용하려면 자체 사용자 정의 uncaught exception handler를 설치해서는 안 됩니다.
:::

:::topic-grid
## 프로토콜
- [NSExceptionHandlerDelegate](https://developer.apple.com/documentation/exceptionhandling/nsexceptionhandlerdelegate): 예외가 발생했을 때 객체가 delegate에 호출하는 메서드를 설명하는 비공식 프로토콜입니다. 객체는 delegate를 가질 필요는 없습니다. delegate가 있는 경우, 모니터링되는 각 객체에 대해 예외 처리와 로깅을 승인할지 묻기 위해 이 delegate 메서드를 호출합니다.
:::

:::topic-grid
## 레퍼런스
- [ExceptionHandling Enumerations](https://developer.apple.com/documentation/exceptionhandling/exceptionhandling-enumerations)
- [ExceptionHandling Constants](https://developer.apple.com/documentation/exceptionhandling/exceptionhandling-constants)
- [ExceptionHandling Functions](https://developer.apple.com/documentation/exceptionhandling/exceptionhandling-functions)
:::
