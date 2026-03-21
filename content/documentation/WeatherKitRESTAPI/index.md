---
route: /documentation/WeatherKitRESTAPI
source_url: https://developer.apple.com/documentation/WeatherKitRESTAPI
source_locale: en-US
section: docc
content_type: symbol
title: WeatherKit REST API
original_title: WeatherKit REST API
source_hash: e387f7b6230fb008391af05922649e37e3d0733ee8c8577fd9b8bb72aff1190c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:42:59+00:00'
last_translated_at: '2026-03-13T18:25:00+09:00'
---

# WeatherKit REST API

앱이나 서비스에서 과거, 현재, 예측 날씨 정보를 가져옵니다.

## 개요

WeatherKit REST API 웹 서비스를 사용하면 사용자에게 현재 날씨와 예보 날씨 정보를 모두 제공하는 앱과 서비스에 날씨 데이터를 제공할 수 있습니다.

웹 앱이나 Android 같은 다른 플랫폼에 날씨 정보를 제공하려면 WeatherKit REST API를 사용하십시오. 네이티브 iOS, macOS, tvOS, watchOS 앱에서는 [WeatherKit](https://developer.apple.com/documentation/WeatherKit)을 사용하십시오.

:::important 중요
이 API를 사용하려면 출처 표기가 필요합니다. 자세한 내용은 [WeatherKit - Data Sources](https://developer.apple.com/weatherkit/data-source-attribution/)를 참고하십시오.
:::

:::topic-grid
## 기본 사항
- [Request authentication for WeatherKit REST API](https://developer.apple.com/documentation/weatherkitrestapi/request-authentication-for-weatherkit-rest-api): 날씨 데이터에 접근하기 위한 developer token을 생성합니다.
:::

:::topic-grid
## 위치의 날씨 정보 가져오기
- [GET /api/v1/availability/{latitude}/{longitude}](https://developer.apple.com/documentation/weatherkitrestapi/get-api-v1-availability-_latitude_-_longitude_): 지정된 위치에서 사용할 수 있는 데이터 세트를 확인합니다.
- [GET /api/v1/weather/{language}/{latitude}/{longitude}](https://developer.apple.com/documentation/weatherkitrestapi/get-api-v1-weather-_language_-_latitude_-_longitude_): 지정된 위치의 날씨 데이터를 가져옵니다.
- [Weather](https://developer.apple.com/documentation/weatherkitrestapi/weather): 요청한 모든 날씨 데이터의 모음입니다.
- [Latitude](https://developer.apple.com/documentation/weatherkitrestapi/latitude): 좌표의 위도를 나타내는 숫자 값입니다. 값 범위는 과 사이입니다.
- [Longitude](https://developer.apple.com/documentation/weatherkitrestapi/longitude): 좌표의 경도를 나타내는 숫자 값입니다. 값 범위는 과 사이입니다.
- [DataSet](https://developer.apple.com/documentation/weatherkitrestapi/dataset): 위치에 대한 날씨 정보의 모음입니다.
:::

:::topic-grid
## 현재 날씨 정보 가져오기
- [CurrentWeather](https://developer.apple.com/documentation/weatherkitrestapi/currentweather): 지정된 위치의 현재 날씨 상태입니다.
- [Metadata](https://developer.apple.com/documentation/weatherkitrestapi/metadata): 날씨 데이터에 대한 설명 정보입니다.
- [ProductData](https://developer.apple.com/documentation/weatherkitrestapi/productdata): 모든 날씨 데이터의 기본 타입입니다.
:::

:::topic-grid
## 분 단위 예보 날씨 가져오기
- [ForecastPeriodSummary](https://developer.apple.com/documentation/weatherkitrestapi/forecastperiodsummary): 분 단위 예보에서 지정된 기간에 대한 요약입니다.
- [ForecastMinute](https://developer.apple.com/documentation/weatherkitrestapi/forecastminute): 지정된 분에 대한 강수 예보입니다.
:::

:::topic-grid
## 시간별 날씨 정보 가져오기
- [HourWeatherConditions](https://developer.apple.com/documentation/weatherkitrestapi/hourweatherconditions): 지정된 시간에 대한 과거 또는 예보 날씨 상태입니다.
- [HourlyForecast](https://developer.apple.com/documentation/weatherkitrestapi/hourlyforecast): 지정한 시간 범위에 대한 시간별 예보 모음입니다.
- [NextHourForecast](https://developer.apple.com/documentation/weatherkitrestapi/nexthourforecast): 다음 1시간에 대한 분 단위 예보입니다.
:::

:::topic-grid
## 일별 날씨 정보 가져오기
- [DayWeatherConditions](https://developer.apple.com/documentation/weatherkitrestapi/dayweatherconditions): 지정된 날짜에 대한 과거 또는 예보 날씨 상태입니다.
- [DayPartForecast](https://developer.apple.com/documentation/weatherkitrestapi/daypartforecast): 낮 시간 또는 야간 시간대에 대한 요약 예보입니다.
- [DailyForecast](https://developer.apple.com/documentation/weatherkitrestapi/dailyforecast): 지정한 날짜 범위에 대한 일별 예보 모음입니다.
:::

:::topic-grid
## 기상 경보 가져오기
- [GET /api/v1/weatherAlert/{language}/{id}](https://developer.apple.com/documentation/weatherkitrestapi/get-api-v1-weatheralert-_language_-_id_): 활성 기상 경보를 수신합니다.
- [WeatherAlert](https://developer.apple.com/documentation/weatherkitrestapi/weatheralert): 보고 기관이 발행한 악천후 공식 메시지입니다.
- [WeatherAlertCollection](https://developer.apple.com/documentation/weatherkitrestapi/weatheralertcollection): 지정된 위치에 대한 악천후 경보 모음입니다.
- [WeatherAlertSummary](https://developer.apple.com/documentation/weatherkitrestapi/weatheralertsummary): 기상 경보에 대한 상세 정보입니다.
- [ResponseType](https://developer.apple.com/documentation/weatherkitrestapi/responsetype): 보고 기관이 권장하는 조치입니다.
- [Severity](https://developer.apple.com/documentation/weatherkitrestapi/severity): 생명과 재산에 대한 위험 수준입니다.
- [Urgency](https://developer.apple.com/documentation/weatherkitrestapi/urgency): 보고 기관이 제시하는 조치의 긴급도를 나타냅니다.
:::

:::topic-grid
## 기상 현상 식별
- [UnitsSystem](https://developer.apple.com/documentation/weatherkitrestapi/unitssystem): 날씨 데이터가 보고되는 단위 체계입니다.
- [MoonPhase](https://developer.apple.com/documentation/weatherkitrestapi/moonphase): 특정 시점에 지상 관측자가 보게 되는 달의 모양입니다.
- [PrecipitationType](https://developer.apple.com/documentation/weatherkitrestapi/precipitationtype): 하루 동안 발생할 것으로 예보된 강수 유형입니다.
- [PressureTrend](https://developer.apple.com/documentation/weatherkitrestapi/pressuretrend): 해면 기압 변화의 방향입니다.
:::

:::topic-grid
## 이벤트 정보 가져오기
- [EventText](https://developer.apple.com/documentation/weatherkitrestapi/eventtext): 기관이 제공하는 악천후 이벤트의 공식 설명 텍스트입니다.
- [Certainty](https://developer.apple.com/documentation/weatherkitrestapi/certainty): 해당 이벤트가 발생할 가능성입니다.
:::

:::topic-grid
## 출처 표기 수행
- [GET /attribution/{language}](https://developer.apple.com/documentation/weatherkitrestapi/get-attribution-_language_): 출처 표기 정보를 수신합니다.
- [Attribution](https://developer.apple.com/documentation/weatherkitrestapi/attribution): 출처 표기를 위한 이미지 자산 URL 목록입니다.
:::
