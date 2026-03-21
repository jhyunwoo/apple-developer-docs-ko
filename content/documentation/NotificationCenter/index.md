---
route: /documentation/NotificationCenter
source_url: https://developer.apple.com/documentation/NotificationCenter
source_locale: en-US
section: docc
content_type: symbol
title: Notification Center
original_title: Notification Center
source_hash: 69eee8d9bbbb0af08bff6120a2af4e0917d05097f766ba2a00a1df811870a069
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:21:33+00:00'
last_translated_at: '2026-03-13T23:21:47+09:00'
---

# Notification Center

Today 보기용 위젯을 만들고 관리합니다.

## 개요

Notification Center 프레임워크는 Today 위젯을 구현하는 앱 extension을 만들고 관리할 수 있게 도와줍니다. 이 프레임워크는 Today 위젯에 표시할 콘텐츠가 있는지 지정하고, 위젯의 모양과 동작 일부를 사용자화하는 데 사용할 수 있는 API를 제공합니다. macOS에서는 위젯 안의 편집 및 검색 경험을 사용자화하는 방법도 제공합니다.

![iOS와 macOS의 Today 보기에서 날씨 정보를 보여 주는 위젯입니다.](https://developer.apple.com)

:::topic-grid
## 핵심 위젯
- [NCWidgetProviding](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding): Today 위젯의 모양과 동작을 사용자화하기 위한 인터페이스입니다.
- [NCWidgetController](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller): Today 위젯에 표시할 콘텐츠가 있는지 지정할 때 사용하는 객체입니다.
:::

:::topic-grid
## 검색 보기
- [NCWidgetSearchViewController](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller): macOS Today 위젯 안에서 기본 검색 뷰를 제공하는 객체입니다.
- [NCWidgetSearchViewDelegate](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate): macOS Today 위젯의 search view controller 안에서 사용자 검색을 활성화하는 인터페이스입니다.
:::

:::topic-grid
## 목록 보기
- [NCWidgetListViewController](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller): macOS Today 위젯 안에 콘텐츠를 표시하는 목록 뷰를 제공하는 객체입니다.
:::
