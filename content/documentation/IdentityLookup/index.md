---
route: /documentation/IdentityLookup
source_url: https://developer.apple.com/documentation/IdentityLookup
source_locale: en-US
section: docc
content_type: symbol
title: SMS and Call Reporting
original_title: SMS and Call Reporting
source_hash: 8b45cc040cdb36b531cbda689b60436fb511fdb69b2d8fb7df884ce0ecd735ce
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:17:41+00:00'
last_translated_at: '2026-03-13T08:36:00+00:00'
---

# SMS and Call Reporting

원치 않는 SMS 메시지와 스팸 전화를 관리하고 신고하는 앱 확장을 생성합니다.

## 개요

SMS and Call Reporting은 원치 않는 통신을 관리하기 위한 앱 확장을 제공합니다.

:::term-list
**Message Filter app extension**: 원치 않는 SMS 및 MMS 메시지를 식별하고 필터링합니다.
**Unwanted Communication app extension**: 사용자가 원치 않는 SMS 메시지와 전화를 스팸으로 신고할 수 있게 합니다.
**Live Caller ID Lookup app extension**: 최신 발신 정보와 차단 정보를 제공합니다.
:::

:::topic-grid
## 메시지 필터링
- [SMS 및 MMS 메시지 필터링](https://developer.apple.com/documentation/identitylookup/sms-and-mms-message-filtering): 사용자 개인정보를 보호하면서 원치 않는 SMS 및 MMS 메시지를 식별하고 필터링하는 앱 확장을 생성합니다.
:::

:::topic-grid
## 스팸 신고
- [SMS 및 통화 스팸 신고](https://developer.apple.com/documentation/identitylookup/sms-and-call-spam-reporting): 사용자가 원치 않는 SMS 메시지와 전화를 정크로 신고할 수 있는 앱 확장을 생성합니다.
:::

:::topic-grid
## Live Caller ID Lookup
- [Live Caller ID Lookup이 개인정보를 보호하는 방식 이해하기](https://developer.apple.com/documentation/identitylookup/understanding-how-live-caller-id-lookup-preserves-privacy): 클라이언트의 IP 주소를 숨기고, 익명 인증을 사용하며, 수신 전화번호를 숨겨 사용자 개인정보를 보호하는 Live Caller ID Lookup을 사용합니다.
- [차단 및 신원 정보용 데이터 포맷 지정하기](https://developer.apple.com/documentation/identitylookup/formatting-data-for-blocking-and-identity-information): 통화 차단과 신원 정보에 사용할 PIR payload를 설정합니다.
- [Live Caller ID Lookup용 HTTP 엔드포인트 설정하기](https://developer.apple.com/documentation/identitylookup/setting-up-the-http-endpoints-for-live-caller-id-lookup): 기기 내 시스템을 서버에 연결합니다.
- [앱에 대한 최신 발신 및 차단 정보 가져오기](https://developer.apple.com/documentation/identitylookup/getting-up-to-date-calling-and-blocking-information-for-your-app): Live Caller ID Lookup 앱 확장을 구현해 통화 차단 및 신원 서비스를 제공합니다.
- [LiveCallerIDLookupProtocol](https://developer.apple.com/documentation/identitylookup/livecalleridlookupprotocol): 시스템이 컨텍스트를 얻기 위해 앱 확장에 질의할 때 사용하는 정보입니다.
- [LiveCallerIDLookupExtensionConfiguration](https://developer.apple.com/documentation/identitylookup/livecalleridlookupextensionconfiguration): 시스템이 앱 확장에 질의할 수 있게 해 주는 객체입니다.
- [LiveCallerIDLookupExtensionContext](https://developer.apple.com/documentation/identitylookup/livecalleridlookupextensioncontext): 시스템이 구성에 사용하는 정보입니다.
- [CallLookupExtensionStatus](https://developer.apple.com/documentation/identitylookup/calllookupextensionstatus): 앱 확장의 현재 상태 값을 반환합니다.
- [LiveCallerIDLookupManager](https://developer.apple.com/documentation/identitylookup/livecalleridlookupmanager): Live Caller ID Lookup 앱 확장의 상태를 관리하는 데 도움이 되는 함수 모음에 접근하는 진입점입니다.
:::

:::topic-grid
## 매크로
- [Macros](https://developer.apple.com/documentation/identitylookup/macros)
:::

:::topic-grid
## 타입 별칭
- [BlockingInfoCoreDataPropertiesSet](https://developer.apple.com/documentation/identitylookup/blockinginfocoredatapropertiesset)
- [IdentityInfoCoreDataPropertiesSet](https://developer.apple.com/documentation/identitylookup/identityinfocoredatapropertiesset)
- [LiveLookupDBExtensionCoreDataPropertiesSet](https://developer.apple.com/documentation/identitylookup/livelookupdbextensioncoredatapropertiesset)
- [LiveLookupStoreCoreDataFrameworkManagedObject](https://developer.apple.com/documentation/identitylookup/livelookupstorecoredataframeworkmanagedobject)
- [LiveLookupStoreFoundationFrameworkSet](https://developer.apple.com/documentation/identitylookup/livelookupstorefoundationframeworkset)
:::
