---
route: /documentation/ClockKit
source_url: https://developer.apple.com/documentation/ClockKit
source_locale: en-US
section: docc
content_type: symbol
title: ClockKit
original_title: ClockKit
source_hash: a9a1c7223d2f5cbab9c035f4783315f18977c97cc486737c33deaf0963f6aa28
canonical_source: manual-translation
last_crawled_at: '2026-03-13T05:18:25+00:00'
last_translated_at: '2026-03-13T05:18:25+00:00'
---

# ClockKit

시계 페이스에 앱별 데이터를 표시합니다.

## 개요

:::important Important
watchOS 10 이상에서는 ClockKit 기반 컴플리케이션이 지원 중단되었습니다. 컴플리케이션을 만들려면 [WidgetKit](https://developer.apple.com/documentation/WidgetKit)을 사용하세요. 자세한 내용은 [Migrating to WidgetKit](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource#Migrating-to-WidgetKit)를 참고하세요.
:::

ClockKit 프레임워크를 사용하여 앱용 컴플리케이션을 구현합니다. *컴플리케이션*은 시계 페이스에 표시되어 사람들이 자주 사용하는 데이터에 빠르게 접근할 수 있게 해 주는 작은 인터페이스 요소입니다. 앱은 컴플리케이션의 모양과 ClockKit이 표시하는 날짜에 대한 템플릿을 제공하는 타임라인 항목을 사용해 컴플리케이션을 정의합니다. 시스템은 이 타임라인을 바탕으로 컴플리케이션의 모양을 업데이트합니다.

ClockKit은 각 시계 페이스에서 컴플리케이션의 크기와 배치를 정의합니다. 다음 이미지는 큰 컴플리케이션 하나와 작은 컴플리케이션 네 개를 위한 공간이 있는 Modular 시계 페이스의 레이아웃을 보여 줍니다.

![Modular 시계 페이스에서 큰 컴플리케이션 하나와 작은 컴플리케이션 네 개를 위한 공간을 보여 주는 그림입니다.](https://developer.apple.com)

ClockKit은 컴플리케이션을 크기와 스타일에 따라 패밀리로 구성하고, 각 패밀리에 대해 다양한 템플릿을 제공합니다. 템플릿을 사용해 텍스트, 이미지, 그래픽 게이지를 표시하세요.

### 컴플리케이션으로 앱 개선하기

컴플리케이션은 사용자와 상호작용하는 독특한 방법을 제공합니다. watchOS 앱을 실행하는 용도로만 사용되더라도 컴플리케이션 생성을 고려해 보세요. 현재 활성화된 시계 페이스에 있는 컴플리케이션은 다음을 제공합니다:

- 사용자가 시계를 흘끗 볼 때 중요한 정보를 제공합니다.
- 사용자가 컴플리케이션을 탭하면 앱의 특정 화면을 빠르게 실행합니다.
- 백그라운드 작업을 수행하여 컴플리케이션과 앱을 최신 상태로 유지할 수 있게 합니다.

### 타임라인 항목

ClockKit은 타임라인 항목 컬렉션을 사용해 시계 페이스에 컴플리케이션을 그립니다. 각 타임라인 항목에는 날짜와 하나의 컴플리케이션 패밀리에 대한 템플릿이 포함됩니다.

:::topic-grid
시계 페이스를 그리기 위해 시스템은 컴플리케이션 데이터 소스의 [CLKComplicationDataSource](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource) 메서드를 호출합니다. 이 메서드는 가능한 컴플리케이션 패밀리, 현재 타임라인 항목, 미래 타임라인 항목, 사용자가 개인정보 보호를 활성화했을 때 표시할 템플릿을 제공합니다.
:::

:::topic-grid
## 핵심
- [Creating and updating a complication’s timeline](https://developer.apple.com/documentation/clockkit/creating-and-updating-a-complication-s-timeline): 타임라인 항목을 제공하여 시계 페이스에서 컴플리케이션의 데이터를 최신 상태로 유지합니다.
- [Adding your complication to the Smart Stack](https://developer.apple.com/documentation/clockkit/adding-your-complication-to-the-smart-stack): Smart Stack에 컴플리케이션이 나타날 수 있도록 구성합니다.
- [CLKComplicationDataSource](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource): 타임라인 데이터를 제공하고 컴플리케이션을 지원하는 클래스를 위한 프로토콜입니다.
:::

:::topic-grid
## 클래스
- [CLKComplicationServer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver): 활성 시계 페이스의 컴플리케이션을 관리하는 객체입니다.
- [CLKDateTextProvider](https://developer.apple.com/documentation/clockkit/clkdatetextprovider): 날짜를 표시하는 텍스트 제공자입니다.
:::
