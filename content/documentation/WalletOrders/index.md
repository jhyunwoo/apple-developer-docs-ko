---
route: /documentation/WalletOrders
source_url: https://developer.apple.com/documentation/WalletOrders
source_locale: en-US
section: docc
content_type: symbol
title: Wallet Orders
original_title: Wallet Orders
source_hash: 48e882f7a5057abdbed22ca5f5aae9e7f1cb41b4939f766cf87055e749e126e2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:24:08+00:00'
last_translated_at: '2026-03-13T09:10:00+00:00'
---

# Wallet Orders

Wallet에서 주문을 생성하고, 배포하고, 업데이트합니다.

## 개요

Wallet Orders를 사용하면 사용자가 Wallet에서 구매 내역을 추적하고 관리할 수 있습니다. 결제 승인 이후 Apple Pay를 통해 주문을 Wallet에 자연스럽게 기부할 수 있습니다.

사용자가 Wallet에서 주문을 추적할 수 있게 하려면 다음이 필요합니다.

- 결제 승인 결과에 주문 세부 정보를 추가합니다.
- 주문 패키지를 빌드하고 웹 서비스로 접근할 수 있게 제공합니다.
- 주문 상태가 변경되었을 때 주문을 업데이트합니다.

:::topic-grid
## 필수 항목
- [주문용 소스 만들기](https://developer.apple.com/documentation/walletorders/creating-the-source-for-an-order): 디렉터리 구조를 만들고 소스 파일과 이미지를 추가하여 주문을 정의합니다.
- [배포 가능한 주문 패키지 빌드하기](https://developer.apple.com/documentation/walletorders/building-a-distributable-order-package): 소스 파일을 빌드, 서명, 압축하여 주문을 배포할 수 있게 준비합니다.
- [기기의 등록 정보 가져오기](https://developer.apple.com/documentation/walletorders/retrieve-the-registrations-for-a-device): 기기가 등록한 주문의 식별자를 가져옵니다.
- [주문의 최신 버전 가져오기](https://developer.apple.com/documentation/walletorders/retrieve-the-latest-version-of-an-order): 서명되고 압축된 주문의 최신 버전을 가져옵니다.
- [Order](https://developer.apple.com/documentation/walletorders/order): 제공된 제품이나 서비스, 고객 서비스, 이행 정보 등을 포함한 주문 세부 정보입니다.
- [Example Order Packages](https://developer.apple.com/documentation/walletorders/example-order-packages): 예제 주문 패키지를 수정하고 빌드하여 Wallet에 추가합니다.
:::

:::topic-grid
## 알림
- [업데이트 알림용으로 기기 등록하기](https://developer.apple.com/documentation/walletorders/register-a-device-for-update-notifications): 주문에 대한 업데이트 알림을 받도록 기기를 등록합니다.
- [업데이트 알림에서 기기 등록 해제하기](https://developer.apple.com/documentation/walletorders/unregister-a-device-from-update-notifications): 주문에 대한 업데이트 알림 수신에서 기기를 등록 해제합니다.
- [PushToken](https://developer.apple.com/documentation/walletorders/pushtoken): APNS가 기기에 업데이트 알림을 보내기 위해 사용하는 push token입니다.
:::

:::topic-grid
## 메시지 로그
- [로그 메시지 수신하기](https://developer.apple.com/documentation/walletorders/receive-log-messages): 서버에 로그 메시지를 기록합니다.
- [LogEntries](https://developer.apple.com/documentation/walletorders/logentries): 로그 메시지 배열입니다.
:::
