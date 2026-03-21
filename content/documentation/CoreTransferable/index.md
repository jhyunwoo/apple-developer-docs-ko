---
route: /documentation/CoreTransferable
source_url: https://developer.apple.com/documentation/CoreTransferable
source_locale: en-US
section: docc
content_type: symbol
title: Core Transferable
original_title: Core Transferable
source_hash: 244bec17cd83f1b056c510e5d002e9b60014757320f99451dca03e3674934a94
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:14:17+00:00'
last_translated_at: '2026-03-13T23:14:51+09:00'
---

# Core Transferable

시스템 공유와 데이터 전송 작업에 참여할 수 있도록 모델 타입의 전송 표현을 선언합니다.

## 개요

Core Transferable은 데이터 전송과 공유 맥락에서 사용자 정의 타입을 사용할 수 있게 해 주는, 현대적이고 Swift 중심의 접근 방식을 제공합니다. Share 버튼, 드래그 앤 드롭, 복사 및 붙여넣기처럼 데이터를 이동하거나 공유하는 시스템 상호 작용에는 transferable 타입을 사용하십시오.

Core Transferable은 앱의 모델 타입이 채택하는 핵심 protocol인 [Transferable](https://developer.apple.com/documentation/coretransferable/transferable)을 정의합니다. 전송 표현은 프레임워크에 내장된 하나 이상의 [TransferRepresentation](https://developer.apple.com/documentation/coretransferable/transferrepresentation) 타입을 조합해 제공합니다. `Transferable` 타입은 [ShareLink](https://developer.apple.com/documentation/SwiftUI/ShareLink), [PasteButton](https://developer.apple.com/documentation/SwiftUI/PasteButton) 같은 타입을 포함한 SwiftUI와 함께 사용해 transferable 데이터를 공유하고 붙여넣을 수 있습니다. SwiftUI에는 `Transferable`을 이용한 드래그 앤 드롭 상호 작용을 지원하는 [draggable(_:)](https://developer.apple.com/documentation/SwiftUI/View/draggable(_:)) 및 [dropDestination(for:action:isTargeted:)](https://developer.apple.com/documentation/SwiftUI/View/dropDestination(for:action:isTargeted:)) 같은 view modifier도 포함되어 있습니다. [String](https://developer.apple.com/documentation/Swift/String), [Data](https://developer.apple.com/documentation/Foundation/Data), [URL](https://developer.apple.com/documentation/Foundation/URL), [Image](https://developer.apple.com/documentation/SwiftUI/Image) 같은 시스템 타입은 이미 `Transferable`을 준수합니다.

앱 내부, 여러 자사 앱 사이, 또는 알려진 데이터 형식을 가져오고 내보내는 방법에 대해 공통 이해를 가진 다른 앱과의 사이에서도 `Transferable` 항목을 주고받을 수 있습니다. 다음 예제는 `Transferable`을 준수하도록 확장한 `Note` 모델 타입을 보여 줍니다.

```swift
struct Note: Codable {
    var text: String
    var url: URL

    init(url: URL) {
        self.url = url
        self.text = ""
    }
}

extension Note: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        CodableRepresentation(contentType: .note)
        ProxyRepresentation(exporting: \.text)
        FileRepresentation(
            contentType: .utf8PlainText,
            exporting: { note in SentTransferredFile(note.url) },
            importing: { received in
                let destination = URL(fileURLWithPath: <# ... #>)
                try FileManager.default.copyItem(at: received.file, to: destination)
                return Self.init(url: destination) })
        }
}

extension UTType {
    static var note = UTType(exportedAs: "com.example.note")
}
```

Core Transferable을 [Uniform Type Identifiers](https://developer.apple.com/documentation/UniformTypeIdentifiers) 프레임워크의 공통 파일 및 데이터 전송 식별자 모음과 함께 사용하면, 표준 파일 타입이나 직접 정의한 사용자 지정 파일 타입을 이용해 데이터를 이동하고 공유하는 시스템 상호 작용을 활용할 수 있습니다.

:::topic-grid
## 핵심
- [Transferable](https://developer.apple.com/documentation/coretransferable/transferable): 드래그 앤 드롭이나 복사 및 붙여넣기 같은 전송 API와 타입이 어떻게 상호 작용하는지 설명하는 protocol입니다.
- [TransferRepresentation](https://developer.apple.com/documentation/coretransferable/transferrepresentation): transferable 항목을 가져오고 내보내는 과정을 선언적으로 설명합니다.
- [Choosing a transfer representation for a model type](https://developer.apple.com/documentation/coretransferable/choosing-a-transfer-representation-for-a-model-type): 내장 타입 조합을 사용해 데이터의 사용자 정의 표현을 정의합니다.
:::

:::topic-grid
## 데이터 전송
- [CodableRepresentation](https://developer.apple.com/documentation/coretransferable/codablerepresentation): Swift의 인코딩 및 디코딩 protocol에 참여하는 타입을 위한 전송 표현입니다.
- [DataRepresentation](https://developer.apple.com/documentation/coretransferable/datarepresentation): 바이너리 데이터 변환을 자체 제공하는 타입을 위한 전송 표현입니다.
:::

:::topic-grid
## 파일 전송
- [FileRepresentation](https://developer.apple.com/documentation/coretransferable/filerepresentation): 파일 URL로 전송되는 타입을 위한 전송 표현입니다.
- [SentTransferredFile](https://developer.apple.com/documentation/coretransferable/senttransferredfile): 보내는 쪽 관점에서 본 파일 설명입니다.
- [ReceivedTransferredFile](https://developer.apple.com/documentation/coretransferable/receivedtransferredfile): 받는 쪽 관점에서 본 파일 설명입니다.
:::

:::topic-grid
## 전송 사용자화
- [ProxyRepresentation](https://developer.apple.com/documentation/coretransferable/proxyrepresentation): 다른 타입의 전송 표현을 자신의 전송 표현으로 사용하는 타입입니다.
- [TransferRepresentationVisibility](https://developer.apple.com/documentation/coretransferable/transferrepresentationvisibility): 전송 중인 항목을 어떤 앱과 프로세스가 볼 수 있는지 지정하는 가시성 수준입니다.
:::

:::topic-grid
## 지원 타입
- [TransferRepresentationBuilder](https://developer.apple.com/documentation/coretransferable/transferrepresentationbuilder): 기존 전송 표현을 조합해 새 전송 표현을 만듭니다.
- [TupleTransferRepresentation](https://developer.apple.com/documentation/coretransferable/tupletransferrepresentation): 전송 표현을 담은 tuple을 감싸는 래퍼 타입입니다.
:::
