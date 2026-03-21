---
route: /documentation/JavaScriptCore
source_url: https://developer.apple.com/documentation/JavaScriptCore
source_locale: en-US
section: docc
content_type: symbol
title: JavaScriptCore
original_title: JavaScriptCore
source_hash: 87dd8772474d1987d9b688e9884a44c9177d1b9c45d42cf4929d4dd7ced1df1f
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:26:32+00:00'
last_translated_at: '2026-03-14T00:42:00+09:00'
---

# JavaScriptCore

앱 내부에서 JavaScript 프로그램을 평가하고, 앱의 JavaScript 스크립팅을 지원합니다.

## 개요

JavaScriptCore 프레임워크는 Swift, Objective-C, C 기반 앱 안에서 JavaScript 프로그램을 평가하는 기능을 제공합니다. 또한 JavaScriptCore를 사용해 JavaScript 환경 안에 사용자 정의 객체를 삽입할 수도 있습니다.

:::topic-grid
## 실행 환경
- [JSVirtualMachine](https://developer.apple.com/documentation/javascriptcore/jsvirtualmachine): 독립적으로 완결된 JavaScript 실행 환경입니다.
- [JSContext](https://developer.apple.com/documentation/javascriptcore/jscontext): JavaScript 실행 환경입니다.
:::

:::topic-grid
## JavaScript 코드
- [JSValue](https://developer.apple.com/documentation/javascriptcore/jsvalue): JavaScript 값입니다.
- [JSManagedValue](https://developer.apple.com/documentation/javascriptcore/jsmanagedvalue): 자동 메모리 관리를 제공하기 위해 조건부 retain 동작을 사용하는 JavaScript 값입니다.
:::

:::topic-grid
## 네이티브 코드
- [JSExport](https://developer.apple.com/documentation/javascriptcore/jsexport): Objective-C 객체를 JavaScript로 내보내기 위한 프로토콜입니다.
:::

:::topic-grid
## C API
- [C JavaScriptCore API](https://developer.apple.com/documentation/javascriptcore/c-javascriptcore-api): JavaScriptCore의 대체 C 기반 API를 살펴봅니다.
:::

:::topic-grid
## 참고 자료
- [JavaScriptCore Constants](https://developer.apple.com/documentation/javascriptcore/javascriptcore-constants)
:::

:::topic-grid
## 변수
- [kJSTypeBigInt](https://developer.apple.com/documentation/javascriptcore/kjstypebigint)
:::

:::topic-grid
## 함수
- [JSBigIntCreateWithDouble(_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithdouble(_:_:_:))
- [JSBigIntCreateWithInt64(_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithint64(_:_:_:))
- [JSBigIntCreateWithString(_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithstring(_:_:_:))
- [JSBigIntCreateWithUInt64(_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsbigintcreatewithuint64(_:_:_:))
- [JSValueCompare(_:_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsvaluecompare(_:_:_:_:))
- [JSValueCompareDouble(_:_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsvaluecomparedouble(_:_:_:_:))
- [JSValueCompareInt64(_:_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsvaluecompareint64(_:_:_:_:))
- [JSValueCompareUInt64(_:_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsvaluecompareuint64(_:_:_:_:))
- [JSValueIsBigInt(_:_:)](https://developer.apple.com/documentation/javascriptcore/jsvalueisbigint(_:_:))
- [JSValueToInt32(_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsvaluetoint32(_:_:_:))
- [JSValueToInt64(_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsvaluetoint64(_:_:_:))
- [JSValueToUInt32(_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsvaluetouint32(_:_:_:))
- [JSValueToUInt64(_:_:_:)](https://developer.apple.com/documentation/javascriptcore/jsvaluetouint64(_:_:_:))
:::

:::topic-grid
## 열거형
- [JSRelationCondition](https://developer.apple.com/documentation/javascriptcore/jsrelationcondition)
:::
