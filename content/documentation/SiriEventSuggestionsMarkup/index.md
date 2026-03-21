---
route: /documentation/SiriEventSuggestionsMarkup
source_url: https://developer.apple.com/documentation/SiriEventSuggestionsMarkup
source_locale: en-US
section: docc
content_type: symbol
title: Siri Event Suggestions Markup
original_title: Siri Event Suggestions Markup
source_hash: 02ab95916b7a3aa1075eea48c3a0cec54095c371d82b4ad12b5b7fbf3209fc20
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:29+00:00'
last_translated_at: '2026-03-13T17:10:00+09:00'
---

# Siri Event Suggestions Markup

이메일과 웹 페이지에 포함된 예약 데이터로 사용자의 캘린더를 업데이트하고 Siri의 제안을 강화합니다.

## 개요

Siri Event Suggestions Markup 데이터 형식을 사용하면 웹 페이지와 이메일에 이벤트 세부 정보를 제공할 수 있습니다. Siri는 여행 일정, 공연, 식당 예약, 소셜 이벤트를 해석하여 예정된 이벤트로 가는 운전 경로 또는 차량 호출을 제안하고 공연 시작 직전에 Do Not Disturb를 활성화하는 것처럼 관련 활동을 보강합니다.

Mail이 예약 마크업이 포함된 이메일을 수신하거나 Safari가 예약 마크업이 포함된 웹 페이지를 로드하면 Siri는 해당 이벤트를 사용자의 Siri Event Suggestions 캘린더에도 추가합니다. Mail과 Safari는 현재 보고 있는 콘텐츠에 예약 정보가 포함되어 있음을 사용자에게 알려 주기 때문에, 사용자는 현재 작업을 벗어나지 않고도 이벤트를 수락하거나 거부할 수 있습니다.

![예약 데이터 조각을 나타내는 그래픽에서 시작해 Siri 아이콘으로 화살표가 이어지고, 다시 캘린더, 길 안내 그래픽, “Time to check-in”, “Reservation found in Mail” 텍스트가 포함된 Siri Suggestion으로 이어지는 Siri Event Suggestions Markup 프로세스 다이어그램입니다.](https://developer.apple.com)

사용자에게 확정된 예약에 대해 알릴 때는 예약 마크업 데이터를 포함하십시오. 매번 일관된 [reservationId](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/reservationid)를 사용하면 시스템이 Safari와 Mail 사이, 그리고 사용자의 여러 기기 사이에서 중복을 관리할 수 있습니다.

이벤트 제안 처리를 위한 도메인 허용 목록에 포함되도록 하려면 [Siri Event Suggestions Markup Information](https://developer.apple.com/contact/request/siri-events/) 양식을 작성하십시오. 신청 전에 구현을 테스트하는 방법에 대한 자세한 내용은 [Checking Your Reservation Markup](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/checking-your-reservation-markup)을 참고하십시오.

:::tip Tip
앱이 있다면 앱에서도 예약 정보를 donate하십시오. 앱에서 이벤트 제안을 제공하는 방법에 대한 자세한 내용은 [Siri Event Suggestions](https://developer.apple.com/documentation/SiriKit/siri-event-suggestions)를 참고하십시오.
:::

### 예약 데이터 형식 지정

웹사이트에서 예약을 제공하거나 사용자에게 이메일로 예약 확인을 보낸다면 HTML 문서 안에 예약 정보를 JSON-LD 또는 Microdata 형식으로 포함할 수 있습니다. JSON-LD의 경우 다음 예처럼 [@context](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/@context)와 `@type,`을 지정하십시오.

```xml
<script type="application/ld+json">
{
  "@context": "http://schema.org", 
  "@type": "TrainReservation",
  "reservationId": "ASDF1234"
  /* more data goes here */    
}
</script>
```

Microdata의 경우 다음처럼 `itemtype` 속성에 해당 예약의 schema.org URL을 제공합니다.

```xml
<section itemscope itemtype="http://schema.org/TrainReservation">
Your reservation
<span itemprop="reservationId">ASDF1234</span>
is confirmed!
/* more data goes here */
</section>
```

:::topic-grid
## 핵심 사항
- [Providing Trusted Data](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/providing-trusted-data): 콘텐츠에 서명하고 불필요하거나 부정확한 정보를 보내지 않도록 합니다.
- [Checking Your Reservation Markup](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/checking-your-reservation-markup): 허용 목록에 도메인이 포함되기 전에 예약 이벤트 데이터를 미리 확인합니다.
:::

:::topic-grid
## 교통
- [FlightReservation](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/flightreservation): 항공편 예약입니다.
- [TrainReservation](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/trainreservation): 기차 여행 예약입니다.
- [BusReservation](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/busreservation): 버스 여행 예약입니다.
- [BoatReservation](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/boatreservation): 선박 여행 예약입니다.
- [RentalCarReservation](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/rentalcarreservation): 렌터카 예약입니다.
:::

:::topic-grid
## 음식, 숙박, 이벤트
- [EventReservation](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/eventreservation): 영화, 스포츠 이벤트, 라이브 쇼 또는 기타 예정된 이벤트에 대한 예약입니다.
- [FoodEstablishmentReservation](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/foodestablishmentreservation): 식당 예약입니다.
- [LodgingReservation](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/lodgingreservation): 호텔 예약 또는 기타 숙박 예약입니다.
:::

:::topic-grid
## 공통 예약 데이터
- [Person](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/person): 승객, 식사 손님, 숙박 손님 또는 행사 참석자입니다.
- [Ticket](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/ticket): 교통 또는 이벤트 티켓에 대한 세부 정보입니다.
- [Seat](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/seat): 승객을 위해 예약된 구체적인 좌석 위치입니다.
- [Organization](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/organization): 사업체, 운송 제공자 또는 이벤트 주최자입니다.
- [Place](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/place): 사업체, 교통 허브 또는 행사 장소입니다.
- [PostalAddress](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/postaladdress): 구체적인 지리적 위치입니다.
:::

:::topic-grid
## 기본 데이터 타입
- [@context](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/@context): 마크업 내용을 해석하기 위한 공개 표준 참조입니다.
- [dateTimeISO8601](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/datetimeiso8601): ISO-8601 형식의 날짜와 시간입니다.
- [reservationId](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/reservationid): 예약을 위한 안정적이고 고유한 식별자입니다.
- [reservationStatus](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/reservationstatus): 예약이 확인되었는지 취소되었는지를 나타내는 문자열입니다.
- [URL](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/url): 웹 페이지의 주소입니다.
- [telephone](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/telephone): 전화번호입니다.
:::
