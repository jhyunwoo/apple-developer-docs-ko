---
route: /documentation/DataDetection
source_url: https://developer.apple.com/documentation/DataDetection
source_locale: en-US
section: docc
content_type: symbol
title: DataDetection
original_title: DataDetection
source_hash: 09452485503a51de5e016c97bbb89f8b9bd89cac06b06b8dc9b34be3f64ffd46
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:31:22+00:00'
last_translated_at: '2026-03-13T23:34:00+09:00'
---

# DataDetection

데이터 감지 시스템이 매칭한 일반적인 데이터 유형에 접근하고 활용합니다.

## 개요

다른 프레임워크의 데이터 감지 메서드는 텍스트 안에 표현된 일반적인 데이터 유형을 감지하고, 일치 항목에 의미론적 의미를 제공하는 DataDetection 프레임워크 클래스를 반환합니다. 다음 유형의 매칭 결과에서 관련 있는 도메인별 정보를 얻을 수 있습니다.

- 캘린더 이벤트
- 이메일 주소
- 항공편 번호
- 웹 링크
- 통화가 포함된 금액
- 전화번호
- 우편 주소
- 배송 추적 번호

[UIPasteboard](https://developer.apple.com/documentation/UIKit/UIPasteboard)의 메서드처럼, 특정 맥락에서 지정한 데이터 유형을 감지하는 함수를 사용합니다. 예를 들어 다음 예시처럼 [detectValues(for:completionHandler:)](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectValues(for:completionHandler:)-6adre)를 사용해 pasteboard에서 이메일 주소를 찾을 수 있습니다.

```swift
UIPasteboard.general.detectValues(for: [\.emailAddresses]) { [self] result in
    switch result {
    case .success(let detectedValues):
        guard let firstEmailAddressMatch = detectedValues.emailAddresses.first else {
            return
        }
        let newEmailAddress = firstEmailAddressMatch.emailAddress
        let newLabel = firstEmailAddressMatch.label
        addNewEmail(for: contact, address: newEmailAddress, label: newLabel)
    case .failure(let error):
        print("Error detecting email addresses: \(error.localizedDescription)")
    }
}
```

그런 다음 데이터 감지 시스템이 반환한 객체에서 데이터를 검사하고 활용합니다.

:::topic-grid
## 매칭된 문자열
- [DDMatch](https://developer.apple.com/documentation/datadetection/ddmatch): 데이터 감지 시스템이 매칭하는 일반적인 데이터 유형을 위한 기본 클래스입니다.
- [DataDetector](https://developer.apple.com/documentation/datadetection/datadetector): 이메일 주소, 전화번호, URL, 항공편 정보 같은 의미 있는 엔터티를 문자열에서 스캔하는 string protocol 확장입니다.
:::

:::topic-grid
## 매칭된 데이터 유형
- [DDMatchCalendarEvent](https://developer.apple.com/documentation/datadetection/ddmatchcalendarevent): 데이터 감지 시스템이 매칭한 캘린더 날짜 또는 날짜 범위를 나타내는 객체입니다.
- [DDMatchEmailAddress](https://developer.apple.com/documentation/datadetection/ddmatchemailaddress): 데이터 감지 시스템이 매칭한 이메일 주소를 담는 객체입니다.
- [DDMatchFlightNumber](https://developer.apple.com/documentation/datadetection/ddmatchflightnumber): 데이터 감지 시스템이 매칭한 항공편 번호를 담는 객체입니다.
- [DDMatchLink](https://developer.apple.com/documentation/datadetection/ddmatchlink): 데이터 감지 시스템이 매칭한 웹 링크를 담는 객체입니다.
- [DDMatchMoneyAmount](https://developer.apple.com/documentation/datadetection/ddmatchmoneyamount): 데이터 감지 시스템이 매칭한 금액 정보를 담는 객체입니다.
- [DDMatchPhoneNumber](https://developer.apple.com/documentation/datadetection/ddmatchphonenumber): 데이터 감지 시스템이 매칭한 전화번호를 담는 객체입니다.
- [DDMatchPostalAddress](https://developer.apple.com/documentation/datadetection/ddmatchpostaladdress): 데이터 감지 시스템이 매칭한 우편 주소를 담는 객체입니다.
- [DDMatchShipmentTrackingNumber](https://developer.apple.com/documentation/datadetection/ddmatchshipmenttrackingnumber): 데이터 감지 시스템이 매칭한 소포 추적 정보를 담는 객체입니다.
:::

:::topic-grid
## Pasteboard detector
- [detectPatterns(for:completionHandler:)](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectPatterns(for:completionHandler:)-23vwn): 데이터 감지 시스템이 pasteboard에서 지정한 패턴을 식별하고, 매칭된 패턴을 클로저로 전달하도록 요청합니다.
- [detectedPatterns(for:)](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectedPatterns(for:)): 데이터 감지 시스템이 pasteboard에서 지정한 패턴을 비동기적으로 식별하고, 매칭된 패턴을 반환하도록 요청합니다.
- [detectPatterns(for:inItemSet:completionHandler:)](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectPatterns(for:inItemSet:completionHandler:)-7ubl1): 데이터 감지 시스템이 pasteboard 항목에서 지정한 패턴을 식별하고, 매칭된 패턴을 클로저로 전달하도록 요청합니다.
- [detectedPatterns(for:inItemSet:)](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectedPatterns(for:inItemSet:)): 데이터 감지 시스템이 pasteboard 항목에서 지정한 패턴을 비동기적으로 식별하고, 매칭된 패턴을 반환하도록 요청합니다.
- [detectValues(for:completionHandler:)](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectValues(for:completionHandler:)-6adre): 데이터 감지 시스템이 pasteboard에서 지정한 데이터 유형을 식별하고, 매칭된 값을 클로저로 전달하도록 요청합니다.
- [detectedValues(for:)](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectedValues(for:)): 데이터 감지 시스템이 pasteboard에서 지정한 값 유형을 비동기적으로 식별하고, 매칭된 값을 반환하도록 요청합니다.
- [detectValues(for:inItemSet:completionHandler:)](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectValues(for:inItemSet:completionHandler:)-pm9l): 데이터 감지 시스템이 pasteboard 항목에서 지정한 데이터 유형을 식별하고, 매칭된 값을 클로저로 전달하도록 요청합니다.
- [detectedValues(for:inItemSet:)](https://developer.apple.com/documentation/UIKit/UIPasteboard/detectedValues(for:inItemSet:)): 데이터 감지 시스템이 pasteboard 항목에서 지정한 값 유형을 비동기적으로 식별하고, 각 pasteboard에 대해 매칭된 값을 반환하도록 요청합니다.
:::
