---
route: /documentation/WalletPasses
source_url: https://developer.apple.com/documentation/WalletPasses
source_locale: en-US
section: docc
content_type: symbol
title: Wallet Passes
original_title: Wallet Passes
source_hash: d4f01112a9e2b2f502314932300343a64442fdc85b16728167dd035eff303f02
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:04:57+00:00'
last_translated_at: '2026-03-13T07:05:46+00:00'
---

# Wallet Passes

지갑 앱용 패스를 생성하고, 배포하고, 업데이트합니다.

## 개요

*패스*는 이전에는 종이, 플라스틱, 또는 다른 물리적 매체로 배포되었을 정보를 디지털 형태로 표현한 것입니다. 패스를 사용하면 비행기에 탑승하거나, 이벤트에 참석하거나, 쿠폰을 사용하는 등 사람이 행동을 취할 수 있습니다. Wallet Passes 프레임워크를 사용하면 최신 상태를 유지하고 관련 정보를 제공하는 동적이고 상호작용 가능한 패스를 만들 수 있습니다.

이 프레임워크를 사용하면 다음을 할 수 있습니다.

- 탑승권, 이벤트 티켓, 스토어 카드, 쿠폰, 일반 패스를 생성합니다.
- 패스 내용을 실시간으로 업데이트합니다.
- 하나의 티켓에 여러 예정 이벤트를 표시합니다.
- Maps, 알림, Live Activities 같은 시스템 기능과 통합합니다.
- 탑승권에 대해 항공편 추적을 활용한 자동 패스 업데이트를 지원합니다.

![서로 다른 세 종류의 패스를 보여 주는 일러스트입니다. 하나는 비행기 탑승권이고, 다른 하나는 콘서트용 이벤트 패스이며, 나머지 하나는 멤버십 카드입니다.](https://developer.apple.com)

사용자가 패스를 설치할 수 있게 하려면 다음을 수행합니다.

- 패스의 소스를 만듭니다.
- 소스에서 배포 가능한 패스를 빌드합니다.
- 패스를 배포합니다.

또한 서버를 통해 개인화된 경험에 맞게 패스를 더 세밀하게 조정하고, 여러 종류의 패스에 대해 실시간 업데이트를 제공할 수 있습니다.

:::topic-grid
## 필수 항목
- [패스용 소스 만들기](https://developer.apple.com/documentation/walletpasses/creating-the-source-for-a-pass): 디렉터리 구조를 만들고 소스 파일과 이미지를 추가하여 패스를 정의합니다.
- [패스 빌드하기](https://developer.apple.com/documentation/walletpasses/building-a-pass): 배포 가능한 패스를 빌드합니다.
- [패스 배포 및 업데이트](https://developer.apple.com/documentation/walletpasses/distributing-and-updating-a-pass): 사용자에게 패스를 배포하거나 기존 패스를 업데이트합니다.
- [Pass](https://developer.apple.com/documentation/walletpasses/pass): 패스를 나타내는 객체입니다.
- [PassFields](https://developer.apple.com/documentation/walletpasses/passfields): 패스 앞면과 뒷면에 표시되는 정보 필드 그룹을 나타내는 객체입니다.
:::

:::topic-grid
## 탑승권
- [의미 태그를 사용하여 항공사 탑승권 만들기](https://developer.apple.com/documentation/walletpasses/creating-an-airline-boarding-pass-using-semantic-tags): 의미 태그를 업데이트하여 탑승권에 대한 실시간 대화형 승객 정보를 제공합니다.
- [Pass.BoardingPass](https://developer.apple.com/documentation/walletpasses/pass/boardingpass-data.dictionary): 탑승권에 표시되는 정보 필드 그룹을 나타내는 객체입니다.
- [SemanticTags](https://developer.apple.com/documentation/walletpasses/semantictags): 시스템이 패스를 제공하고 관련 동작을 제안하는 데 사용하는 기계 판독 가능 메타데이터를 담은 객체입니다.
- [SemanticTagType](https://developer.apple.com/documentation/walletpasses/semantictagtype): 의미 태그용 데이터 객체 타입 모음입니다.
:::

:::topic-grid
## 쿠폰 패스
- [쿠폰 패스 만들기](https://developer.apple.com/documentation/walletpasses/creating-a-coupon-pass): 할인 및 특별 제안을 위한 디지털 패스를 구성합니다.
- [Pass.Coupon](https://developer.apple.com/documentation/walletpasses/pass/coupon-data.dictionary): 쿠폰에 표시되는 정보 필드 그룹을 나타내는 객체입니다.
:::

:::topic-grid
## 이벤트 패스
- [의미 태그를 사용하여 이벤트 패스 만들기](https://developer.apple.com/documentation/walletpasses/creating-an-event-pass-using-semantic-tags): 의미 태그를 사용하여 이벤트 패스에 최신 정보를 제공합니다.
- [Pass.EventTicket](https://developer.apple.com/documentation/walletpasses/pass/eventticket-data.dictionary): 이벤트 티켓에 표시되는 정보 필드 그룹을 나타내는 객체입니다.
- [SemanticTags](https://developer.apple.com/documentation/walletpasses/semantictags): 시스템이 패스를 제공하고 관련 동작을 제안하는 데 사용하는 기계 판독 가능 메타데이터를 담은 객체입니다.
- [SemanticTagType](https://developer.apple.com/documentation/walletpasses/semantictagtype): 의미 태그용 데이터 객체 타입 모음입니다.
- [UpcomingPassInformationEntry](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentry): 모든 예정 패스 정보 항목의 순서 있는 목록을 나타내는 객체입니다.
- [UpcomingPassInformationEntryType](https://developer.apple.com/documentation/walletpasses/upcomingpassinformationentrytype): 특정 예정 이벤트에 대한 예정 패스 정보 항목을 나타내는 객체입니다.
:::

:::topic-grid
## 일반 패스
- [일반 패스 만들기](https://developer.apple.com/documentation/walletpasses/creating-a-generic-pass): 사람이 행동을 취할 수 있도록 정보를 담은 디지털 패스를 구성합니다.
- [Pass.Generic](https://developer.apple.com/documentation/walletpasses/pass/generic-data.dictionary): 일반 패스에 표시되는 정보 필드 그룹을 나타내는 객체입니다.
:::

:::topic-grid
## 스토어 카드 패스
- [스토어 카드 패스 만들기](https://developer.apple.com/documentation/walletpasses/creating-a-store-card-pass): 매장 로열티 카드와 기프트 카드를 위한 디지털 패스를 구성합니다.
- [Pass.StoreCard](https://developer.apple.com/documentation/walletpasses/pass/storecard-data.dictionary): 스토어 카드에 표시되는 정보 필드 그룹을 나타내는 객체입니다.
:::

:::topic-grid
## 패스 업데이트
- [패스 업데이트용 웹 서비스 추가하기](https://developer.apple.com/documentation/walletpasses/adding-a-web-service-to-update-passes): 기기에서 패스를 등록, 업데이트, 등록 해제하는 웹 서버를 구현합니다.
- [업데이트 알림용 패스 등록](https://developer.apple.com/documentation/walletpasses/register-a-pass-for-update-notifications): 기기에서 패스에 대한 변경 알림을 설정합니다.
- [업데이트 가능한 패스 목록 가져오기](https://developer.apple.com/documentation/walletpasses/get-the-list-of-updatable-passes): 업데이트된 패스의 일련 번호를 기기로 보냅니다.
- [업데이트된 패스 보내기](https://developer.apple.com/documentation/walletpasses/send-an-updated-pass): 업데이트된 패스를 생성하고 서명한 뒤 기기로 보냅니다.
- [업데이트 알림용 패스 등록 해제](https://developer.apple.com/documentation/walletpasses/unregister-a-pass-for-update-notifications): 기기에서 패스에 대한 업데이트 알림 전송을 중지합니다.
- [Log a Message](https://developer.apple.com/documentation/walletpasses/log-a-message): 서버에 메시지를 기록합니다.
- [PushToken](https://developer.apple.com/documentation/walletpasses/pushtoken): 기기에 등록된 패스의 푸시 알림 토큰을 담은 객체입니다.
- [SerialNumbers](https://developer.apple.com/documentation/walletpasses/serialnumbers): 기기에서 업데이트 가능한 패스의 일련 번호를 담은 객체입니다.
- [LogEntries](https://developer.apple.com/documentation/walletpasses/logentries): 메시지 배열을 담은 객체입니다.
:::

:::topic-grid
## 개인화된 패스
- [개인화된 패스 반환](https://developer.apple.com/documentation/walletpasses/return-a-personalized-pass): 개인화된 패스를 생성하고 서명한 뒤 기기로 보냅니다.
- [PersonalizationDictionary](https://developer.apple.com/documentation/walletpasses/personalizationdictionary): 패스를 개인화하는 데 사용하는 정보를 담은 객체입니다.
:::
