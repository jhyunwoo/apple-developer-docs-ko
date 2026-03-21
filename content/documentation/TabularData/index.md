---
route: /documentation/TabularData
source_url: https://developer.apple.com/documentation/TabularData
source_locale: en-US
section: docc
content_type: symbol
title: TabularData
original_title: TabularData
source_hash: 365dd4660f09121787d3db20b4f2504efe4aa732a8413819c2b0e4e02ba7a48b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:24:09+00:00'
last_translated_at: '2026-03-14T01:12:00+09:00'
---

# TabularData

머신 러닝 모델을 학습시키기 위한 데이터 테이블을 가져오고, 정리하고, 준비합니다.

:::topic-grid
## 데이터 테이블
- [DataFrame](https://developer.apple.com/documentation/tabulardata/dataframe): 데이터를 행과 열로 배치하는 컬렉션입니다.
- [DataFrameProtocol](https://developer.apple.com/documentation/tabulardata/dataframeprotocol): 데이터 프레임을 나타내는 타입입니다.
:::

:::topic-grid
## 타입이 지정된 열
- [Column](https://developer.apple.com/documentation/tabulardata/column): 데이터 프레임의 열입니다.
- [ColumnSlice](https://developer.apple.com/documentation/tabulardata/columnslice): 타입이 지정된 열에서 연속된 요소 선택을 나타내는 컬렉션입니다.
- [FilledColumn](https://developer.apple.com/documentation/tabulardata/filledcolumn): 누락된 요소를 기본값으로 대체한 열의 view입니다.
- [DiscontiguousColumnSlice](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice): 타입이 지정된 열에서, 중간에 간격이 있을 수 있는 요소 선택을 나타내는 컬렉션입니다.
- [ColumnProtocol](https://developer.apple.com/documentation/tabulardata/columnprotocol): 열을 나타내는 타입입니다.
- [OptionalColumnProtocol](https://developer.apple.com/documentation/tabulardata/optionalcolumnprotocol): 누락값을 포함할 수 있는 열을 나타내는 타입입니다.
:::

:::topic-grid
## 타입 소거 열
- [AnyColumn](https://developer.apple.com/documentation/tabulardata/anycolumn): 타입이 소거된 열입니다.
- [AnyColumnSlice](https://developer.apple.com/documentation/tabulardata/anycolumnslice): 타입이 소거된 열 슬라이스입니다.
- [AnyColumnProtocol](https://developer.apple.com/documentation/tabulardata/anycolumnprotocol): 타입이 소거된 열을 나타내는 타입입니다.
- [AnyColumnPrototype](https://developer.apple.com/documentation/tabulardata/anycolumnprototype): 타입이 소거된 열을 생성하는 프로토타입입니다.
:::

:::topic-grid
## 통계 요약
- [NumericSummary](https://developer.apple.com/documentation/tabulardata/numericsummary): 수치형 열의 요약입니다.
- [CategoricalSummary](https://developer.apple.com/documentation/tabulardata/categoricalsummary): 컬렉션 요소에 대한 범주형 요약입니다.
- [AnyCategoricalSummary](https://developer.apple.com/documentation/tabulardata/anycategoricalsummary): 타입이 소거된 범주형 요약입니다.
:::

:::topic-grid
## 오류
- [JSONReadingError](https://developer.apple.com/documentation/tabulardata/jsonreadingerror): JSON 읽기 오류입니다.
- [CSVReadingError](https://developer.apple.com/documentation/tabulardata/csvreadingerror): CSV 읽기 오류입니다.
- [CSVWritingError](https://developer.apple.com/documentation/tabulardata/csvwritingerror): CSV 쓰기 오류입니다.
- [ColumnDecodingError](https://developer.apple.com/documentation/tabulardata/columndecodingerror): 열 디코딩 오류입니다.
- [ColumnEncodingError](https://developer.apple.com/documentation/tabulardata/columnencodingerror): 열 인코딩 오류입니다.
- [SFrameReadingError](https://developer.apple.com/documentation/tabulardata/sframereadingerror): Turi Create scalable data frame을 읽을 때 발생하는 오류입니다.
:::

:::topic-grid
## 지원 타입
- [Order](https://developer.apple.com/documentation/tabulardata/order): 정렬 순서를 나타내는 타입입니다.
- [ColumnID](https://developer.apple.com/documentation/tabulardata/columnid): 열 이름과 그 요소 타입을 저장하는 열 식별자입니다.
- [FormattingOptions](https://developer.apple.com/documentation/tabulardata/formattingoptions): 데이터 프레임 또는 열 타입의 내용을 출력 가능한 문자열로 표현하는 방법을 나타내는 매개변수 집합입니다.
:::

:::topic-grid
## 구조체
- [JSONWritingOptions](https://developer.apple.com/documentation/tabulardata/jsonwritingoptions): JSON 파일 읽기 옵션 집합입니다.
:::
