---
route: /documentation/PreferencePanes
source_url: https://developer.apple.com/documentation/PreferencePanes
source_locale: en-US
section: docc
content_type: symbol
title: Preference Panes
original_title: Preference Panes
source_hash: 81cfdad3d3069f8de838179a64c97a78021da3c8854cf6d4647953e6e42c0bbe
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:02:15+00:00'
last_translated_at: '2026-03-13T21:47:00+09:00'
---

# Preference Panes

앱의 사용자 정의 환경설정을 System Preferences 앱에 통합합니다.

## 개요

Preference Panes 프레임워크를 사용하면 시스템 수준의 사용자 정의 환경설정을 System Preferences 앱에 통합할 수 있습니다. 이 프레임워크를 사용해 사용자에게 표시할 사용자 정의 인터페이스가 들어 있는 preference pane bundle을 구현합니다. 그런 다음 사용자의 시스템에서 적절한 `Library/PreferencePanes` 디렉터리에 bundle을 설치합니다.

System Preferences는 bundle의 사용자 정의 [NSPreferencePane](https://developer.apple.com/documentation/preferencepanes/nspreferencepane) 객체와 함께 동작하여 사용자에게 사용자 정의 인터페이스를 표시하는 과정을 관리합니다. System Preferences는 bundle이 제공하는 view를 로드하고 lifecycle event를 preference pane 객체에 전달합니다. 이 객체를 사용해 인터페이스의 control 및 view와의 상호 작용에 응답하고, 설정 변경 사항을 사용자의 defaults 데이터베이스에 저장하십시오.

:::note 참고
preference pane bundle은 앱과 별도로 관리되어야 하는 설정에만 사용하십시오. 예를 들어 같은 suite 안의 여러 앱이 공유하는 설정을 관리할 때 사용합니다. 앱 전용 환경설정은 사용자 정의 preferences 인터페이스를 사용해 관리하십시오.
:::

:::topic-grid
## Preference Pane 인터페이스
- [NSPreferencePane](https://developer.apple.com/documentation/preferencepanes/nspreferencepane): System Preferences 또는 다른 앱에 preference pane을 제공하기 위한 인터페이스입니다.
:::

:::topic-grid
## 알림
- [NSPreferencePrefPaneIsAvailable](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSPreferencePrefPaneIsAvailable): 시스템 환경설정 앱이 사용자 설정을 표시할 수 있음을 observer에게 알립니다.
- [NSPreferencePaneDoUnselect](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSPreferencePaneDoUnselect): preference pane의 선택이 해제될 수 있음을 observer에게 알립니다.
- [NSPreferencePaneCancelUnselect](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSPreferencePaneCancelUnselect): preference pane의 선택을 해제하면 안 된다는 점을 observer에게 알립니다.
- [NSPreferencePaneSwitchToPane](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSPreferencePaneSwitchToPane): 사용자가 새로운 preference pane을 선택했음을 observer에게 알립니다.
- [NSPreferencePaneUpdateHelpMenu](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSPreferencePaneUpdateHelpMenu): 도움말 메뉴 콘텐츠가 변경되었음을 observer에게 알립니다.
:::

:::topic-grid
## 도움말 메뉴 키
- [NSPrefPaneHelpMenuInfoPListKey](https://developer.apple.com/documentation/preferencepanes/nsprefpanehelpmenuinfoplistkey): preference pane과 연관된 전역 도움말 메뉴 항목입니다.
- [NSPrefPaneHelpMenuTitleKey](https://developer.apple.com/documentation/preferencepanes/nsprefpanehelpmenutitlekey): preference pane 안의 도움말 메뉴 항목 제목입니다.
- [NSPrefPaneHelpMenuAnchorKey](https://developer.apple.com/documentation/preferencepanes/nsprefpanehelpmenuanchorkey): 표시할 help book anchor입니다.
:::

:::topic-grid
## 참고 자료
- [PreferencePanes Constants](https://developer.apple.com/documentation/preferencepanes/preferencepanes-constants)
:::
