---
route: /documentation/CoreFoundation
source_url: https://developer.apple.com/documentation/CoreFoundation
source_locale: en-US
section: docc
content_type: symbol
title: Core Foundation
original_title: Core Foundation
source_hash: cb38af9d877c4974a8d87b55c65fbb9e34c48ef01eb6502697136465572a47e1
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:22:11+00:00'
last_translated_at: '2026-03-13T22:52:00+09:00'
---

# Core Foundation

Foundation 프레임워크와 자연스럽게 브리지되는 저수준 함수, 원시 데이터 타입, 다양한 컬렉션 타입에 접근합니다.

## 개요

Core Foundation은 애플리케이션 서비스, 애플리케이션 환경, 그리고 애플리케이션 자체에 유용한 기본 소프트웨어 서비스를 제공하는 프레임워크입니다. 또한 일반적인 데이터 타입을 위한 추상화를 제공하고, Unicode 문자열 저장을 통해 국제화를 쉽게 하며, plug-in 지원, XML property list, URL 리소스 접근, 환경설정 같은 유틸리티 모음을 제공합니다.

Core Foundation에 대해 더 알아보려면 [Core Foundation Design Concepts](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/CFDesignConcepts.html#//apple_ref/doc/uid/10000122i)를 참고하십시오.

:::topic-grid
## 유틸리티
- [Base Utilities](https://developer.apple.com/documentation/corefoundation/base-utilities)
- [Byte-Order Utilities](https://developer.apple.com/documentation/corefoundation/byte-order-utilities)
- [Core Foundation URL Access Utilities](https://developer.apple.com/documentation/corefoundation/core-foundation-url-access-utilities)
- [Preferences Utilities](https://developer.apple.com/documentation/corefoundation/preferences-utilities)
- [Socket Name Server Utilities](https://developer.apple.com/documentation/corefoundation/socket-name-server-utilities)
- [Time Utilities](https://developer.apple.com/documentation/corefoundation/time-utilities)
:::

:::topic-grid
## opaque 타입
- [CFAllocator](https://developer.apple.com/documentation/corefoundation/cfallocator)
- [CFArray](https://developer.apple.com/documentation/corefoundation/cfarray)
- [CFAttributedString](https://developer.apple.com/documentation/corefoundation/cfattributedstring)
- [CFBag](https://developer.apple.com/documentation/corefoundation/cfbag)
- [CFBinaryHeap](https://developer.apple.com/documentation/corefoundation/cfbinaryheap)
- [CFBitVector](https://developer.apple.com/documentation/corefoundation/cfbitvector)
- [CFBoolean](https://developer.apple.com/documentation/corefoundation/cfboolean)
- [CFBundle](https://developer.apple.com/documentation/corefoundation/cfbundle)
- [CFCalendar](https://developer.apple.com/documentation/corefoundation/cfcalendar)
- [CFCharacterSet](https://developer.apple.com/documentation/corefoundation/cfcharacterset)
- [CFData](https://developer.apple.com/documentation/corefoundation/cfdata)
- [CFDate](https://developer.apple.com/documentation/corefoundation/cfdate)
- [CFDateFormatter](https://developer.apple.com/documentation/corefoundation/cfdateformatter)
- [CFDictionary](https://developer.apple.com/documentation/corefoundation/cfdictionary)
- [CFError](https://developer.apple.com/documentation/corefoundation/cferror)
- [CFFileDescriptor](https://developer.apple.com/documentation/corefoundation/cffiledescriptor)
- [CFFileSecurity](https://developer.apple.com/documentation/corefoundation/cffilesecurity): 파일 시스템 객체의 보안 정보를 Core Foundation 객체에 캡슐화합니다.
- [CFLocale](https://developer.apple.com/documentation/corefoundation/cflocale)
- [CFMachPort](https://developer.apple.com/documentation/corefoundation/cfmachport)
- [CFMessagePort](https://developer.apple.com/documentation/corefoundation/cfmessageport)
- [CFMutableArray](https://developer.apple.com/documentation/corefoundation/cfmutablearray)
- [CFMutableAttributedString](https://developer.apple.com/documentation/corefoundation/cfmutableattributedstring)
- [CFMutableBag](https://developer.apple.com/documentation/corefoundation/cfmutablebag)
- [CFMutableBitVector](https://developer.apple.com/documentation/corefoundation/cfmutablebitvector)
- [CFMutableCharacterSet](https://developer.apple.com/documentation/corefoundation/cfmutablecharacterset)
- [CFMutableData](https://developer.apple.com/documentation/corefoundation/cfmutabledata)
- [CFMutableDictionary](https://developer.apple.com/documentation/corefoundation/cfmutabledictionary)
- [CFMutableSet](https://developer.apple.com/documentation/corefoundation/cfmutableset)
- [CFMutableString](https://developer.apple.com/documentation/corefoundation/cfmutablestring)
- [CFNotificationCenter](https://developer.apple.com/documentation/corefoundation/cfnotificationcenter)
- [CFNull](https://developer.apple.com/documentation/corefoundation/cfnull)
- [CFNumber](https://developer.apple.com/documentation/corefoundation/cfnumber)
- [CFNumberFormatter](https://developer.apple.com/documentation/corefoundation/cfnumberformatter)
- [CFPlugIn](https://developer.apple.com/documentation/corefoundation/cfplugin)
- [CFPlugInInstance](https://developer.apple.com/documentation/corefoundation/cfplugininstance)
- [CFPropertyList](https://developer.apple.com/documentation/corefoundation/cfpropertylist)
- [CFReadStream](https://developer.apple.com/documentation/corefoundation/cfreadstream)
- [CFRunLoop](https://developer.apple.com/documentation/corefoundation/cfrunloop)
- [CFRunLoopObserver](https://developer.apple.com/documentation/corefoundation/cfrunloopobserver)
- [CFRunLoopSource](https://developer.apple.com/documentation/corefoundation/cfrunloopsource)
- [CFRunLoopTimer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimer)
- [CFSet](https://developer.apple.com/documentation/corefoundation/cfset)
- [CFSocket](https://developer.apple.com/documentation/corefoundation/cfsocket)
- [CFString](https://developer.apple.com/documentation/corefoundation/cfstring)
- [CFStringTokenizer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizer)
- [CFTimeZone](https://developer.apple.com/documentation/corefoundation/cftimezone)
- [CFTree](https://developer.apple.com/documentation/corefoundation/cftree)
- [CFURL](https://developer.apple.com/documentation/corefoundation/cfurl)
- [CFUserNotification](https://developer.apple.com/documentation/corefoundation/cfusernotification)
- [CFURLEnumerator](https://developer.apple.com/documentation/corefoundation/cfurlenumerator): 객체에 대한 참조입니다.
- [CFUUID](https://developer.apple.com/documentation/corefoundation/cfuuid)
- [CFWriteStream](https://developer.apple.com/documentation/corefoundation/cfwritestream)
- [CFXMLNode](https://developer.apple.com/documentation/corefoundation/cfxmlnode)
- [CFXMLParser](https://developer.apple.com/documentation/corefoundation/cfxmlparser)
- [CFXMLTree](https://developer.apple.com/documentation/corefoundation/cfxmltree)
:::

:::topic-grid
## 참고 자료
- [CFStream](https://developer.apple.com/documentation/corefoundation/cfstream)
- [Core Foundation Structures](https://developer.apple.com/documentation/corefoundation/core-foundation-structures)
- [Core Foundation Enumerations](https://developer.apple.com/documentation/corefoundation/core-foundation-enumerations)
- [Core Foundation Constants](https://developer.apple.com/documentation/corefoundation/core-foundation-constants)
- [Core Foundation Functions](https://developer.apple.com/documentation/corefoundation/core-foundation-functions)
- [Core Foundation Data Types](https://developer.apple.com/documentation/corefoundation/core-foundation-data-types)
- [Core Foundation Macros](https://developer.apple.com/documentation/corefoundation/corefoundation-macros)
:::

:::topic-grid
## 변수
- [kCFURLUbiquitousItemIsSyncPausedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemissyncpausedkey)
- [kCFURLUbiquitousItemSupportedSyncControlsKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitemsupportedsynccontrolskey)
:::

:::topic-grid
## 함수
- [CFAttributedStringGetStatisticalWritingDirections(_:_:_:_:_:)](https://developer.apple.com/documentation/corefoundation/cfattributedstringgetstatisticalwritingdirections(_:_:_:_:_:))
:::
