---
route: /documentation/WeatherKit
source_url: https://developer.apple.com/documentation/WeatherKit
source_locale: en-US
section: docc
content_type: symbol
title: WeatherKit
original_title: WeatherKit
source_hash: 77e1dbe70420a621b9cf583f02f2047f989294b90a9c500da767583103eea33d
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:41:40+00:00'
last_translated_at: '2026-03-13T23:51:00+09:00'
---

# WeatherKit

사용자에게 날씨 상태와 경보를 제공합니다.

## 개요

WeatherKit은 현재 상태, 분 단위 강수, 시간별 및 일별 예보를 포함한 시의적절한 날씨 정보를 제공합니다. 또한 악천후 경보도 제공합니다.

:::topic-grid
## 기초
- [Fetching weather forecasts with WeatherKit](https://developer.apple.com/documentation/weatherkit/fetching_weather_forecasts_with_weatherkit): 비행 계획 앱에서 목적지 공항의 날씨 데이터를 요청하고 표시합니다.
- [Weather](https://developer.apple.com/documentation/weatherkit/weather): 호출자가 요청한 집계 날씨 데이터를 나타내는 모델입니다.
- [WeatherService](https://developer.apple.com/documentation/weatherkit/weatherservice): 날씨 데이터를 얻기 위한 인터페이스를 제공합니다.
:::

:::topic-grid
## 요청
- [WeatherQuery](https://developer.apple.com/documentation/weatherkit/weatherquery): 일반적인 날씨 데이터 집합 요청을 캡슐화하는 구조체입니다.
- [CurrentWeather](https://developer.apple.com/documentation/weatherkit/currentweather): 특정 위치에서 관측된 현재 상태를 설명하는 구조체입니다.
- [WeatherAttribution](https://developer.apple.com/documentation/weatherkit/weatherattribution): 날씨 데이터 제공자에 대한 attribution에 필요한 정보를 정의하는 구조체입니다.
- [WeatherMetadata](https://developer.apple.com/documentation/weatherkit/weathermetadata): 추가 날씨 정보를 제공하는 구조체입니다.
- [WeatherSeverity](https://developer.apple.com/documentation/weatherkit/weatherseverity): 악천후 이벤트의 심각도를 설명합니다.
:::

:::topic-grid
## 특성
- [Precipitation](https://developer.apple.com/documentation/weatherkit/precipitation): 강수의 형태입니다.
- [PressureTrend](https://developer.apple.com/documentation/weatherkit/pressuretrend): 시간에 따른 기압 변화입니다.
- [UVIndex](https://developer.apple.com/documentation/weatherkit/uvindex): 태양 자외선의 예상 강도입니다.
- [Wind](https://developer.apple.com/documentation/weatherkit/wind): 풍속, 풍향, 돌풍 데이터를 포함합니다.
- [WeatherCondition](https://developer.apple.com/documentation/weatherkit/weathercondition): 현재 날씨 상태에 대한 설명입니다.
:::

:::topic-grid
## 경보 및 예보
- [WeatherAlert](https://developer.apple.com/documentation/weatherkit/weatheralert): 요청된 위치에 대해 정부 기관이 발령한 날씨 경보입니다.
- [WeatherAvailability](https://developer.apple.com/documentation/weatherkit/weatheravailability): 요청된 위치에서 데이터 사용 가능 여부를 나타내는 구조체입니다.
- [Forecast](https://developer.apple.com/documentation/weatherkit/forecast): 분별, 시간별, 일별 예보를 위한 예보 컬렉션입니다.
- [MinuteWeather](https://developer.apple.com/documentation/weatherkit/minuteweather): 다음 한 시간의 분 단위 예보를 나타내는 구조체입니다.
- [HourWeather](https://developer.apple.com/documentation/weatherkit/hourweather): 해당 시간의 날씨 상태를 나타내는 구조체입니다.
- [DayWeather](https://developer.apple.com/documentation/weatherkit/dayweather): 해당 날짜의 날씨 상태를 나타내는 구조체입니다.
:::

:::topic-grid
## 천체 정보
- [SunEvents](https://developer.apple.com/documentation/weatherkit/sunevents): 일출, 일몰, 새벽, 황혼을 포함한 태양 이벤트 날짜를 나타내는 열거형입니다.
- [MoonEvents](https://developer.apple.com/documentation/weatherkit/moonevents): 달 관련 이벤트를 나타내는 구조체입니다.
- [MoonPhase](https://developer.apple.com/documentation/weatherkit/moonphase): 달의 위상 종류를 지정하는 열거형입니다.
:::

:::topic-grid
## 오류
- [WeatherError](https://developer.apple.com/documentation/weatherkit/weathererror): WeatherKit이 반환하는 오류입니다.
:::

:::topic-grid
## 구조체
- [CloudCoverByAltitude](https://developer.apple.com/documentation/weatherkit/cloudcoverbyaltitude): 저고도, 중고도, 고고도 구름이 하늘을 덮는 비율을 포함합니다.
- [DailyWeatherStatistics](https://developer.apple.com/documentation/weatherkit/dailyweatherstatistics): 일별 날씨 통계 데이터 컬렉션을 담는 구조체입니다.
- [DailyWeatherStatisticsQuery](https://developer.apple.com/documentation/weatherkit/dailyweatherstatisticsquery): 일반적인 일별 날씨 통계 데이터 집합 요청을 캡슐화하는 구조체입니다.
- [DailyWeatherSummary](https://developer.apple.com/documentation/weatherkit/dailyweathersummary): 일별 날씨 요약 컬렉션을 담는 구조체입니다.
- [DailyWeatherSummaryQuery](https://developer.apple.com/documentation/weatherkit/dailyweathersummaryquery): 일반적인 일별 날씨 요약 데이터 집합 요청을 캡슐화하는 구조체입니다.
- [DayPartForecast](https://developer.apple.com/documentation/weatherkit/daypartforecast): 하루 중 특정 구간의 날씨 예보를 나타내는 구조체입니다.
- [DayPrecipitationStatistics](https://developer.apple.com/documentation/weatherkit/dayprecipitationstatistics): 하루의 강수 통계를 설명하는 구조체입니다.
- [DayPrecipitationSummary](https://developer.apple.com/documentation/weatherkit/dayprecipitationsummary): 하루의 강수 요약을 설명하는 구조체입니다.
- [DayTemperatureStatistics](https://developer.apple.com/documentation/weatherkit/daytemperaturestatistics): 하루의 기온 통계를 설명하는 구조체입니다.
- [DayTemperatureSummary](https://developer.apple.com/documentation/weatherkit/daytemperaturesummary): 하루의 기온 요약을 설명하는 구조체입니다.
- [HistoricalComparisons](https://developer.apple.com/documentation/weatherkit/historicalcomparisons): 특정 위치의 날씨 상태 비교를 나타내는 구조체입니다. 현재 관측값과 과거 평균 간 비교 목록이며, 편차의 중요도 순서로 정렬됩니다.
- [HourTemperatureStatistics](https://developer.apple.com/documentation/weatherkit/hourtemperaturestatistics): 특정 시간의 기온 통계를 설명하는 구조체입니다.
- [HourlyWeatherStatistics](https://developer.apple.com/documentation/weatherkit/hourlyweatherstatistics): 시간별 날씨 통계 데이터 컬렉션을 담는 구조체입니다.
- [HourlyWeatherStatisticsQuery](https://developer.apple.com/documentation/weatherkit/hourlyweatherstatisticsquery): 일반적인 시간별 날씨 통계 데이터 집합 요청을 캡슐화하는 구조체입니다.
- [MonthPrecipitationStatistics](https://developer.apple.com/documentation/weatherkit/monthprecipitationstatistics): 특정 월의 강수 통계를 설명하는 구조체입니다.
- [MonthTemperatureStatistics](https://developer.apple.com/documentation/weatherkit/monthtemperaturestatistics): 특정 월의 기온 통계를 설명하는 구조체입니다.
- [MonthlyWeatherStatistics](https://developer.apple.com/documentation/weatherkit/monthlyweatherstatistics): 월별 날씨 통계 데이터 컬렉션을 담는 구조체입니다.
- [MonthlyWeatherStatisticsQuery](https://developer.apple.com/documentation/weatherkit/monthlyweatherstatisticsquery): 일반적인 월별 날씨 통계 데이터 집합 요청을 캡슐화하는 구조체입니다.
- [Percentiles](https://developer.apple.com/documentation/weatherkit/percentiles): 측정 가능한 날씨 조건의 확률 분포를 설명하는 구조체입니다.
- [PrecipitationAmountByType](https://developer.apple.com/documentation/weatherkit/precipitationamountbytype): 일정 기간 동안 발생할 것으로 예상되는 모든 형태의 강수량을 유형별로 나누어 제공하는 구조체입니다.
- [SnowfallAmount](https://developer.apple.com/documentation/weatherkit/snowfallamount): 일정 기간 동안의 적설량을 설명하는 구조체입니다.
- [Trend](https://developer.apple.com/documentation/weatherkit/trend): 특정 위치의 특정 조건에 대한 날씨 데이터에서 관측된 패턴을 설명하는 구조체입니다.
- [TrendBaseline](https://developer.apple.com/documentation/weatherkit/trendbaseline): trend baseline이 무엇인지에 대한 모든 정보를 캡슐화하는 타입입니다.
- [WeatherChange](https://developer.apple.com/documentation/weatherkit/weatherchange): 특정 측정 가능한 날씨 측면이 이전과 비교해 어떻게 변할 것으로 예상되는지를 알려 주는 구조체입니다.
- [WeatherChanges](https://developer.apple.com/documentation/weatherkit/weatherchanges): Weather Change 예보를 나타내는 구조체입니다. 다가오는 날씨가 이전 조건과 비교해 유의미하게 다른지를 정성적으로 평가합니다.
:::

:::topic-grid
## 열거형
- [Deviation](https://developer.apple.com/documentation/weatherkit/deviation): trend에서 두 값 간의 비교를 설명합니다.
- [HistoricalComparison](https://developer.apple.com/documentation/weatherkit/historicalcomparison): 위치의 과거 날씨 데이터 통계 분석에서 인식된 비교를 나타내는 enum입니다.
:::
