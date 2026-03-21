---
route: /documentation/analytics-reports
source_url: https://developer.apple.com/documentation/analytics-reports
source_locale: en-US
section: docc
content_type: article
title: Analytics Reports
original_title: Analytics Reports
source_hash: 3233348217caa8925281bd4542d11633340fb94b6b89892e137ec6ba83d97bd5
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:04:56+00:00'
last_translated_at: '2026-03-13T08:20:00+00:00'
---

# Analytics Reports

앱 개발 리포트 목록과 각 리포트의 필드 설명, 용어집을 제공합니다.

## 개요

Analytics Report API를 사용하면 Apple 플랫폼의 앱에 대한 데이터를 분석할 수 있습니다. 이 페이지에서는 리포트 다운로드 방법, 리포트 변경 사항, 사용 가능한 리포트 목록을 안내합니다. 각 리포트 페이지에서는 리포트 필드 설명, 값 용어집, 핵심 용어 정의, 플랫폼별 지원 범위를 확인할 수 있습니다.

다음 API 키 역할 중 하나가 있으면 이 리포트들을 검토할 수 있습니다.

- `ADMIN`
- `SALES_AND_REPORTS`
- `FINANCE`

:::note Note
개발자 계정의 API 키를 제3자에게 공유하여 리포트를 분석하거나 처리하게 할 경우, 새 키를 만들 때 `SALES_AND_REPORTS` 역할을 선택하세요. 이 역할은 [Download Sales and Trends Reports](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-salesReports)에는 접근할 수 있지만 [Download Finance Reports](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-financeReports) 엔드포인트에는 접근할 수 없습니다.
:::

### 리포트 다운로드 및 처리

리포트를 받기 시작하려면 App Store Connect API의 [Request reports](https://developer.apple.com/documentation/AppStoreConnectAPI/POST-v1-analyticsReportRequests) 엔드포인트를 사용하세요. 자세한 내용은 [Downloading Analytics Reports](https://developer.apple.com/documentation/AppStoreConnectAPI/downloading-analytics-reports)를 참고하세요. 요청을 만든 뒤에는 [Read report request information](https://developer.apple.com/documentation/AppStoreConnectAPI/GET-v1-analyticsReportRequests-_id_)을 사용해 리포트 인스턴스 목록을 폴링하고, 새 인스턴스를 다운로드할 수 있는지 확인합니다. 유효한 Analytics Report Request를 생성하기 전에는 Apple이 리포트를 생성하지 않습니다.

각 리포트 *인스턴스*는 새로운 데이터 세트를 나타냅니다. 각 인스턴스는 여러 개의 *세그먼트*로 구성될 수 있으며, 세그먼트는 하나의 인스턴스를 물리적으로 나눈 파티션입니다. 따라서 전체 데이터를 얻으려면 해당 인스턴스의 모든 세그먼트를 다운로드해야 합니다.

각 리포트 인스턴스는 일간, 주간, 월간 중 하나의 세분화 단위를 가집니다. *일간* 인스턴스는 하루 또는 여러 날의 데이터를 포함할 수 있습니다. 리포트 내용의 Date 열은 이벤트가 발생한 날짜를 나타냅니다. *주간* 인스턴스는 월요일부터 일요일까지의 데이터를 포함합니다. *월간* 인스턴스는 한 달 전체의 데이터를 포함합니다. 자세한 내용은 [Data Completeness and Corrections](https://developer.apple.com/documentation/analytics-reports/data-completeness-corrections)를 참고하세요.

:::note Note
주간 및 월간 리포트 인스턴스에서 `Date` 열은 각각 해당 주와 해당 월의 첫째 날을 나타냅니다.
:::

### 누락된 리포트 다시 가져오기

리포트 인스턴스를 생성하면 35일 동안 사용할 수 있습니다. 이 기간이 지나면 시스템이 리포트 인스턴스를 자동으로 삭제합니다. 이 경우 App Store Connect API의 [Request reports](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-analyticsreportrequests) 엔드포인트를 사용해 새 일회성 스냅샷 요청을 시작하여, 일간 생성 리포트에서 더 이상 उपलब्ध하지 않은 데이터를 다시 가져올 수 있습니다. 이 요청은 사용 가능한 모든 과거 리포트를 포괄하는 데이터 모음을 생성합니다. 이 스냅샷 요청은 한 달에 한 번만 만들 수 있습니다.

### 향후 리포트 변경 사항 모니터링

리포트 열의 위치는 시간이 지나면서 바뀔 수 있습니다. 스키마 업그레이드를 더 원활히 처리하려면 리포트 파일에서 열 위치가 아니라 열 이름을 기준으로 처리하세요. 리포트 값은 대소문자를 구분하지 않습니다.

:::topic-grid
## 필수 항목
- [데이터 완전성과 수정](https://developer.apple.com/documentation/analytics-reports/data-completeness-corrections): Analytics Reports API가 완전한 데이터 세트를 제공하는 방식을 이해합니다.
- [리포트 데이터에서 사용자 개인정보 보호하기](https://developer.apple.com/documentation/analytics-reports/privacy): 사용자 개인정보를 보호하는 데 도움이 되는 조치를 이해합니다.
:::

:::topic-grid
## App Store 참여
- [App Store 탐색 및 참여](https://developer.apple.com/documentation/analytics-reports/app-store-discovery-and-engagement): 사용자가 App Store에서 앱과 상호 작용하는 방식을 분석합니다.
- [App Store 웹 미리보기](https://developer.apple.com/documentation/analytics-reports/app-store-web-preview): 웹 브라우저에서 사람들이 앱의 제품 페이지와 앱 내 이벤트에 어떻게 참여하는지 분석합니다.
:::

:::topic-grid
## App Store 상거래
- [App Store 다운로드](https://developer.apple.com/documentation/analytics-reports/app-download): App Store에서 사용자가 앱을 몇 번 다운로드하는지 분석합니다.
- [App Store 사전 주문](https://developer.apple.com/documentation/analytics-reports/app-store-pre-order): App Store에서 사용자가 앱을 얼마나 사전 주문하고 취소하는지에 대한 세부 정보를 분석합니다.
- [App Store 구매](https://developer.apple.com/documentation/analytics-reports/app-store-purchase): App Store에서 앱이 생성한 총수익을 분석합니다.
:::

:::topic-grid
## 앱 사용
- [App Clip 사용량](https://developer.apple.com/documentation/analytics-reports/app-clip-usage): 사용자가 App Clip과 상호 작용하는 방식을 분석합니다.
- [앱 충돌](https://developer.apple.com/documentation/analytics-reports/app-crashes): 앱 버전과 기기 유형별로 App Store 앱의 충돌을 검토합니다.
- [App Store 설치 및 삭제](https://developer.apple.com/documentation/analytics-reports/app-installs): 사용자가 앱을 설치하고 삭제한 횟수에 대한 세부 정보를 분석합니다.
- [App Store 데이터 공유 옵트인](https://developer.apple.com/documentation/analytics-reports/app-store-opt-in): 앱을 처음 다운로드한 사용자 중 여러분과 데이터를 공유하기로 선택한 비율을 분석합니다.
- [앱 세션](https://developer.apple.com/documentation/analytics-reports/app-sessions): 사람들이 App Store 앱을 얼마나 자주 열고 평균 세션 시간이 얼마나 되는지 분석합니다.
- [CarPlay 앱 사용량](https://developer.apple.com/documentation/analytics-reports/carplay-app-usage): 사람들이 앱에서 CarPlay를 사용하는 방식을 검토합니다.
- [플랫폼별 앱 설치](https://developer.apple.com/documentation/analytics-reports/platform-app-installs): 날짜, 설치 유형, 채널, 기기, 플랫폼 버전, 지역별로 앱 설치 데이터를 분석합니다.
- [단축어 앱 사용량](https://developer.apple.com/documentation/analytics-reports/shortcut-app-usage): 사람들이 앱의 단축어 동작을 얼마나 자주 사용하는지 분석합니다.
- [단축어 동작 사용량](https://developer.apple.com/documentation/analytics-reports/shortcuts-actions-usage): 사람들이 앱의 동작을 사용하는 단축어를 얼마나 자주 실행하는지 분석합니다.
:::

:::topic-grid
## 프레임워크 사용량
- [AccessorySetupKit 액세서리 선택기 세션](https://developer.apple.com/documentation/analytics-reports/accessorysetupkit-accessory-picker-sessions): 사람들이 AccessorySetupKit을 사용해 앱으로 액세서리를 설정하는 횟수를 분석합니다.
- [AccessorySetupKit 사용량](https://developer.apple.com/documentation/analytics-reports/accessorysetupkit-usage): 앱이 AccessorySetupKit을 얼마나 자주 사용하는지 분석합니다.
- [AirPlay 탐색 세션](https://developer.apple.com/documentation/analytics-reports/airplay-discovery-sessions): AirPlay 탐색 세션 정보를 검토합니다.
- [Animoji 스티커 전송 수](https://developer.apple.com/documentation/analytics-reports/animoji-stickers-sent): 사람들이 앱에서 Memoji 스티커를 사용하는 횟수를 분석합니다.
- [집중 모드에 추가된 앱](https://developer.apple.com/documentation/analytics-reports/app-added-to-focus): 앱과 집중 모드의 관계에 대한 정보를 검토합니다.
- [앱 디스크 공간 사용량](https://developer.apple.com/documentation/analytics-reports/app-disk-space-usage): 앱의 디스크 공간 사용량을 분석합니다.
- [앱 확장 실행 사용량](https://developer.apple.com/documentation/analytics-reports/app-extended-launch-usage): 앱의 확장 실행 사용 방식을 이해합니다.
- [App HangTracer 사용량](https://developer.apple.com/documentation/analytics-reports/app-hangtracer-usage): 앱이 HangTracer Framework를 통해 전경 UI 응답성을 모니터링하는 데 소비하는 시간을 분석합니다.
- [앱 런타임 사용량](https://developer.apple.com/documentation/analytics-reports/app-runtime-usage): 앱이 서로 다른 동적 라이브러리의 특정 심볼을 얼마나 자주 실행하는지 분석합니다.
- [앱 세션 컨텍스트](https://developer.apple.com/documentation/analytics-reports/app-sessions-context): 얼마나 많은 사람이 앱을 사용하고 얼마나 오래 사용하는지 분석합니다.
- [앱 선호 언어 설정](https://developer.apple.com/documentation/analytics-reports/application-preferred-language-settings): 사람들이 앱에서 언어 기본 설정을 사용하는 방식을 검토합니다.
- [ARKit ARSession 지속 시간](https://developer.apple.com/documentation/analytics-reports/arkit-arsession-duration): ARKit ARSession 지속 시간에 대한 정보를 검토합니다.
- [ARKit ARSession 실패](https://developer.apple.com/documentation/analytics-reports/arkit-arsession-failures): ARKit ARSession 실패에 대한 세부 정보를 분석합니다.
- [ARKit 캡처 프레임 속도 스로틀링](https://developer.apple.com/documentation/analytics-reports/arkit-capture-frame-rate-throttling): ARKit이 카메라 프레임 속도를 제한하는 데 걸리는 시간을 분석합니다.
- [ARKit 협업 세션 기능](https://developer.apple.com/documentation/analytics-reports/arkit-collaborative-session-features): 앱이 ARKit 협업 세션 기능을 사용하는 방식을 검토합니다.
- [ARKit 얼굴 추적](https://developer.apple.com/documentation/analytics-reports/arkit-face-tracking): 앱이 ARKit 얼굴 추적을 얼마나 자주 사용하는지 분석합니다.
- [ARKit 비디오 포맷](https://developer.apple.com/documentation/analytics-reports/arkit-video-formats): ARKit 비디오 포맷과 고해상도 프레임 정보를 검토합니다.
- [ARKit 월드 트래킹](https://developer.apple.com/documentation/analytics-reports/arkit-world-tracking): 앱의 월드 트래킹 구성 설정을 검토합니다.
- [ARKit 월드 트래킹 이미지 감지](https://developer.apple.com/documentation/analytics-reports/arkit-world-tracking-image-detection): ARKit 월드 트래킹에서 감지된 이미지 수를 분석합니다.
- [오디오 입력 음소거](https://developer.apple.com/documentation/analytics-reports/audio-input-muting): 회의 앱 통화 중 오디오 입력 음소거 및 음소거 해제 제스처에 대한 세부 정보를 분석합니다.
- [오디오 입력 경로, 지속 시간 및 통화 모드](https://developer.apple.com/documentation/analytics-reports/audio-input-route-and-duration-and-call-mode): 앱이 오디오 세션 입력을 사용하는 방식을 검토합니다.
- [오디오 세션 오디오 유닛 사용량](https://developer.apple.com/documentation/analytics-reports/audio-session-audio-unit-usage): 앱의 오디오 유닛 사용량을 분석합니다.
- [오디오 볼륨 수준 및 지속 시간](https://developer.apple.com/documentation/analytics-reports/audio-volume-levels-and-duration): 앱이 출력 오디오의 볼륨과 재생 시간을 사용하는 방식을 검토합니다.
- [자동 음성 인식 사용량](https://developer.apple.com/documentation/analytics-reports/automatic-speech-recognition-usage): 사람들이 앱에서 받아쓰기나 Siri를 얼마나 자주 사용하는지 분석합니다.
- [Bluetooth LE 광고](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-advertising): 앱이 Bluetooth Low Energy(LE) 광고를 사용하는 방식을 검토합니다.
- [Bluetooth LE 연결 결과](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-connection-results): 앱이 Low Energy(LE) 연결을 얼마나 자주 사용하며 연결 결과가 어떤지 분석합니다.
- [앱별 Bluetooth LE 연결 수](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-connections-per-app): 앱에서 완료된 Bluetooth Low Energy(LE) 연결 수를 분석합니다.
- [Bluetooth LE 연결 해제 결과](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-disconnection-results): 앱의 Low Energy(LE) 연결 해제를 검토합니다.
- [Bluetooth LE 스캔](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-scans): 앱이 Bluetooth Low Energy(LE) 스캔을 사용하는 방식을 검토합니다.
- [Bluetooth LE 세션](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-sessions): 앱이 Bluetooth Low Energy(LE) 연결을 얼마나 자주 사용하는지 분석합니다.
- [브라우저 선택 화면 참여도(iOS 18.2 미만)](https://developer.apple.com/documentation/analytics-reports/browser-choice-screen-engagement): iOS의 브라우저 선택 화면에서 웹 브라우저 앱이 기본 브라우저로 선택되는 빈도를 측정합니다.
- [브라우저 선택 화면 선택 결과](https://developer.apple.com/documentation/analytics-reports/browser-choice-screen-selection): 브라우저 선택 화면에서 웹 브라우저 앱이 기본값으로 선택된 기기 비율을 보여 주는 리포트입니다.
- [통화 서비스 및 통화 성능](https://developer.apple.com/documentation/analytics-reports/call-services-and-call-performance): 앱의 통화 서비스 사용과 통화 성능을 검토합니다.
- [CarPlay 내비게이션](https://developer.apple.com/documentation/analytics-reports/carplay-navigation): 사람들이 앱에서 경로 안내 세션을 시작하는 빈도를 분석합니다.
- [협업 메시지 사용량](https://developer.apple.com/documentation/analytics-reports/collaboration-message-usage): 사람들이 앱에서 협업 메시지를 얼마나 자주 사용하는지 분석합니다.
- [Core Location 권한 승인 결과](https://developer.apple.com/documentation/analytics-reports/core-location-authorization-results): 앱의 요청 결과로 사람들이 부여하는 권한을 검토합니다.
- [Core Location 지오펜싱](https://developer.apple.com/documentation/analytics-reports/core-location-geofencing): 앱이 지오펜스를 사용하는 방식을 검토합니다.
- [CRABS 기반 비디오 재생 사용량](https://developer.apple.com/documentation/analytics-reports/crabs-based-video-playback-usage): 앱이 CRABS 비디오 재생 또는 CRABS 프로토콜을 사용하는 비디오 재생을 얼마나 자주 사용하는지 분석합니다.
- [맞춤 언어 모델 빌드 시작 수](https://developer.apple.com/documentation/analytics-reports/custom-language-model-builds-started): 앱이 맞춤 언어 모델 재빌드를 얼마나 자주 트리거하는지 분석합니다.
- [맞춤형 전사 요청](https://developer.apple.com/documentation/analytics-reports/customized-transcription-requests): 맞춤 언어 모델을 사용하는 전사 요청 사용량을 분석합니다.
- [기본 브라우저 사용 비율](https://developer.apple.com/documentation/analytics-reports/default-browser-usage-rate): 브라우저 앱이 기본 웹 브라우저로 설정된 기기 비율을 검토합니다.
- [DockKit 앱 사용량](https://developer.apple.com/documentation/analytics-reports/dockkit-app-usage): 앱이 DockKit 액세서리를 사용하는 방식을 검토합니다.
- [Dynamic Island 레이아웃 변경](https://developer.apple.com/documentation/analytics-reports/dynamic-island-layout-changes): Dynamic Island 레이아웃 상태의 변화를 분석합니다.
- [얼굴 기반 자동 노출 및 자동 초점 사용량](https://developer.apple.com/documentation/analytics-reports/face-driven-auto-exposure-and-auto-focus-usage): 사람들이 앱에서 얼굴 기반 자동 노출(AE)과 자동 초점(AF)을 사용하는 방식을 분석합니다.
- [파일 기반 비디오 재생 사용량](https://developer.apple.com/documentation/analytics-reports/file-based-video-playback-usage): 앱이 파일 재생 또는 로컬 파일 시스템에서 일어나는 재생을 얼마나 자주 사용하는지 분석합니다.
- [파일 시스템 이벤트 API 사용량](https://developer.apple.com/documentation/analytics-reports/file-system-events-api-usage): 앱이 사용하는 파일 시스템 이벤트 리소스 수를 분석합니다.
- [플래시라이트 사용량](https://developer.apple.com/documentation/analytics-reports/flashlight-usage): 플래시라이트 상태 정보를 검토합니다.
- [게임 컨트롤러 햅틱 엔진 생성](https://developer.apple.com/documentation/analytics-reports/game-controller-haptics-engine-creation): 앱이 햅틱 위치성을 사용하는 방식과 사용하는 컨트롤러를 분석합니다.
- [게임 컨트롤러 세션](https://developer.apple.com/documentation/analytics-reports/game-controller-sessions): 사람들이 앱에서 게임 컨트롤러 세션을 얼마나 자주, 얼마나 오래 사용하는지 분석합니다.
- [햅틱 엔진 사용량](https://developer.apple.com/documentation/analytics-reports/haptics-engine-usage): 앱이 햅틱을 재생하는 빈도를 검토합니다.
- [홈 화면 위젯 설치](https://developer.apple.com/documentation/analytics-reports/home-screen-widget-installs): 사람들이 홈 화면에 위젯을 추가하는 빈도를 분석합니다.
- [홈 화면 위젯 회전](https://developer.apple.com/documentation/analytics-reports/home-screen-widget-rotations): 앱의 위젯이 Smart Stack의 전면으로 회전해 오는 빈도를 분석합니다.
- [홈 화면 위젯 사용량](https://developer.apple.com/documentation/analytics-reports/home-screen-widget-usage): 얼마나 많은 사람이 위젯과 상호 작용하는지 분석합니다.
- [홈 화면 위젯](https://developer.apple.com/documentation/analytics-reports/home-screen-widgets): 시스템이 홈 화면의 기본 Smart Stack에 앱 위젯을 추가하는 시점을 분석합니다.
- [HTTP Live Streaming 재생 횟수](https://developer.apple.com/documentation/analytics-reports/http-live-streaming-playback-count): AVFoundation API에서 앱이 HTTP Live Streaming(HLS) 자산을 사용하는 방식을 검토합니다.
- [HTTP Live Streaming 비디오 재생 사용량](https://developer.apple.com/documentation/analytics-reports/http-live-streaming-video-playback-usage): 앱이 HTTP Live Streaming(HLS) 비디오 재생 또는 HLS 프로토콜을 사용하는 비디오 재생을 사용하는 방식에 대한 정보를 검토합니다.
- [iBeacon 영역 추가 사용량](https://developer.apple.com/documentation/analytics-reports/ibeacon-add-region-usage): 앱이 iBeacon Add Region API를 사용하는 방식을 분석합니다.
- [iBeacon 거리 측정 사용량](https://developer.apple.com/documentation/analytics-reports/ibeacon-ranging-usage): 앱이 iBeacon Ranging API를 사용하는 방식에 대한 정보를 검토합니다.
- [iBeacon 영역 모니터링 중지 사용량](https://developer.apple.com/documentation/analytics-reports/ibeacon-stop-monitoring-for-region-usage): 앱이 iBeacon Stop Monitoring for Region API를 사용하는 빈도를 분석합니다.
- [키보드 받아쓰기 사용량](https://developer.apple.com/documentation/analytics-reports/keyboard-dictation-usage): 사람들이 앱에서 키보드 받아쓰기를 사용하는 방식을 분석합니다.
- [실시간 현황 사용](https://developer.apple.com/documentation/analytics-reports/live-activity-use): 앱이 Live Activity를 사용하는 방식을 검토합니다.
- [CoreML 모델 로드 메트릭](https://developer.apple.com/documentation/analytics-reports/load-coreml-models-metrics): 앱의 Core ML 모델 사용을 검토합니다.
- [로컬 네트워크 개인정보 보호](https://developer.apple.com/documentation/analytics-reports/local-network-privacy): 로컬 네트워크 개인정보 보호 프롬프트의 결과를 분석합니다.
- [위치 세션](https://developer.apple.com/documentation/analytics-reports/location-sessions): 앱이 Core Location API를 사용하는 방식을 검토합니다.
- [잠금 화면 위젯 구성](https://developer.apple.com/documentation/analytics-reports/lock-screen-widget-configuration): 사람들이 잠금 화면에서 위젯을 구성하는 빈도를 분석합니다.
- [Metal 명령 큐](https://developer.apple.com/documentation/analytics-reports/metal-command-queues): 앱의 Metal Command Queue 사용을 검토합니다.
- [모드 활동 알림](https://developer.apple.com/documentation/analytics-reports/mode-activity-notifications): 사용자가 앱의 알림을 어떻게 해결하는지에 대한 정보를 검토합니다.
- [다중 게임 컨트롤러 사용량](https://developer.apple.com/documentation/analytics-reports/multiple-game-controllers-usage): 앱을 사용하는 사람들이 여러 게임 컨트롤러를 사용하는 방식을 검토합니다.
- [Nearby Interaction 세션](https://developer.apple.com/documentation/analytics-reports/nearby-interaction-sessions): 앱이 Nearby Interaction을 통해 Ultra Wideband(UWB) 거리 측정 세션을 시작하는 빈도를 분석합니다.
- [알림 요약 참여도](https://developer.apple.com/documentation/analytics-reports/notification-summary-engagement): 사람들이 앱의 알림 요약과 상호 작용하는 빈도를 분석합니다.
- [사진 촬영 사용량](https://developer.apple.com/documentation/analytics-reports/photo-capture-usage): 앱이 사진에서 Photo capture를 사용하는 방식을 분석합니다.
- [Photogrammetry ObjectCaptureSession API 사용량](https://developer.apple.com/documentation/analytics-reports/photogrammetry-objectcapturesession-api-usage): 앱이 포토그래메트리용 객체 캡처를 얼마나 자주 사용하는지 검토합니다.
- [PhotogrammetrySession API 사용량](https://developer.apple.com/documentation/analytics-reports/photogrammetrysession-api-usage): 앱이 포토그래메트리용 객체 모델링을 얼마나 자주 사용하는지 검토합니다.
- [PhotoKit 가져오기](https://developer.apple.com/documentation/analytics-reports/photokit-imports): 앱이 PhotoKit 자산을 가져오는 방식을 검토합니다.
- [사진 라이브러리 접근](https://developer.apple.com/documentation/analytics-reports/photos-library-access): 사람들이 앱에서 어떤 형태의 사진 라이브러리 접근 권한을 부여하는지 검토합니다.
- [사진 선택기](https://developer.apple.com/documentation/analytics-reports/photos-picker): 사람들이 앱에서 Photos를 사용하는 방식을 분석합니다.
- [사진 공유](https://developer.apple.com/documentation/analytics-reports/photos-sharing): 사람들이 앱에서 Photos를 얼마나 자주 공유하는지 분석합니다.
- [ProRes 비디오 사용량](https://developer.apple.com/documentation/analytics-reports/prores-video-usage): 사람들이 앱에서 ProRes 비디오를 사용하는 방식을 검토합니다.
- [미리 알림 사용량](https://developer.apple.com/documentation/analytics-reports/reminders-usage): 앱이 시스템 미리 알림과 상호 작용하는 빈도를 분석합니다.
- [RoomPlan 사용량](https://developer.apple.com/documentation/analytics-reports/roomplan-usage): 사람들이 앱에서 RoomPlan을 사용하는 방식을 검토합니다.
- [Safari 확장 활성화](https://developer.apple.com/documentation/analytics-reports/safari-extensions-enablement): 사람들이 Safari 확장을 활성화하는 빈도를 분석합니다.
- [Safari 확장 사용량](https://developer.apple.com/documentation/analytics-reports/safari-extensions-usage): 사람들이 Safari 확장을 사용하는 방식을 검토합니다.
- [Shared With You 콘텐츠 참여도](https://developer.apple.com/documentation/analytics-reports/shared-with-you-content-engagement): 사람들이 앱에서 Shared with You 콘텐츠와 상호 작용하는 정보를 검토합니다.
- [활동 유형별 SharePlay 사용량](https://developer.apple.com/documentation/analytics-reports/shareplay-usage-by-activity-type): 사람들이 앱에서 SharePlay를 사용하는 방식을 검토합니다.
- [ShazamKit 사용량](https://developer.apple.com/documentation/analytics-reports/shazamkit-usage): 앱이 ShazamKit을 활용하는 방식을 분석합니다.
- [공간 음향 사용량](https://developer.apple.com/documentation/analytics-reports/spatial-audio-usage): 공간 음향 모드의 변화를 분석합니다.
- [Speech 프레임워크 전사 요청 오디오 길이](https://developer.apple.com/documentation/analytics-reports/speech-framework-transcription-request-audio-duration): 앱의 전사 요청에 대한 오디오 길이 분포를 분석합니다.
- [Speech 프레임워크 전사 요청](https://developer.apple.com/documentation/analytics-reports/speech-framework-transcription-requests): 앱의 전사 요청을 검토합니다.
- [텍스트 입력 동작](https://developer.apple.com/documentation/analytics-reports/text-input-actions): 텍스트 입력 동작에 대한 정보를 검토합니다.
- [번역 요청 사용량](https://developer.apple.com/documentation/analytics-reports/translation-request-usage): 사람들이 앱에서 음성-텍스트 번역을 사용하는 방식에 대한 정보를 검토합니다.
- [Verify With Wallet 문서 요청 사용 가능성](https://developer.apple.com/documentation/analytics-reports/verify-with-wallet-document-request-availability): 앱이 신원 및 인증 API를 사용해 문서 요청 가능 여부를 확인하는 방식을 검토합니다.
- [Verify with Wallet 문서 요청](https://developer.apple.com/documentation/analytics-reports/verify-with-wallet-document-requests): 앱이 신원 및 인증 API를 사용하는 방식을 검토합니다.
- [비디오 길이 정보](https://developer.apple.com/documentation/analytics-reports/video-duration-information): 비디오 길이에 대한 정보를 검토합니다.
- [비디오 PiP 지속 시간](https://developer.apple.com/documentation/analytics-reports/video-pip-duration): 앱이 Picture in Picture(PiP)를 사용하는 시간을 검토합니다.
- [비디오 스트리밍 지속 시간](https://developer.apple.com/documentation/analytics-reports/video-streaming-duration): 사람들이 앱에서 비디오 스트리밍을 사용하는 방식을 검토합니다.
- [VisionKit 데이터 감지기](https://developer.apple.com/documentation/analytics-reports/visionkit-data-detectors): 앱이 VisionKit에서 데이터 감지기 호출을 사용하는 방식을 검토합니다.
- [VisionKit 이미지 분석](https://developer.apple.com/documentation/analytics-reports/visionkit-image-analysis): 이미지에 대한 VisionKit 분석 요청을 분석합니다.
- [VisionKit Live Text 사용량](https://developer.apple.com/documentation/analytics-reports/visionkit-live-text-usage): 사람들이 Live Text와 상호 작용하는 방식에 대한 정보를 검토합니다.
- [VisionKit 세션](https://developer.apple.com/documentation/analytics-reports/visionkit-sessions): 앱의 VisionKit 세션을 검토합니다.
- [Wi-Fi 알려진 네트워크 수정](https://developer.apple.com/documentation/analytics-reports/wi-fi-known-network-modifications): 앱의 Wi-Fi 관리자 사용으로 알려진 네트워크를 추가하거나 제거하는 사용자의 동작을 분석합니다.
:::

:::topic-grid
## 성능
- [AirPlay 오류](https://developer.apple.com/documentation/analytics-reports/airplay-errors): 앱에서 발생하는 AirPlay 오류를 분석합니다.
- [AirPlay 성능](https://developer.apple.com/documentation/analytics-reports/airplay-performance): 앱의 AirPlay 성능을 검토합니다.
- [확장 앱 충돌](https://developer.apple.com/documentation/analytics-reports/app-crashes-expanded): 앱이 충돌하는 비율을 분석합니다.
- [앱 설치 성능](https://developer.apple.com/documentation/analytics-reports/app-installs-performance): 앱 설치 성공률과 실패율에 대한 세부 정보를 분석합니다.
- [앱 뉴럴 풋프린트](https://developer.apple.com/documentation/analytics-reports/app-neural-footprint): 프로세스를 대신해 Apple Neural Engine이 고정하는 메모리 양을 분석합니다.
- [앱 저장소 읽기 및 쓰기](https://developer.apple.com/documentation/analytics-reports/app-storage-reads-and-writes): 앱이 디스크 읽기와 쓰기를 얼마나 자주 사용하는지 분석합니다.
- [오디오 과부하](https://developer.apple.com/documentation/analytics-reports/audio-overloads): 사람들이 앱에서 겪는 오디오 끊김 수를 분석합니다.
- [Bluetooth LE 세션 지속 시간](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-session-duration): 앱이 Bluetooth Low Energy(LE) 연결을 사용하는 시간을 분석합니다.
- [Bluetooth 시스템 깨우기](https://developer.apple.com/documentation/analytics-reports/bluetooth-system-wakes): 앱이 유발하는 Bluetooth 시스템 깨우기에 대한 세부 정보를 분석합니다.
- [CAMetalLayer 성능](https://developer.apple.com/documentation/analytics-reports/cametallayer-performance): 앱의 CAMetalLayer 메타데이터와 성능을 검토합니다.
- [셀룰러 요금제 프로비저닝](https://developer.apple.com/documentation/analytics-reports/cellular-plan-provisioning): 사람들이 앱을 사용해 eSIM을 설치하는 빈도와 성공률을 분석합니다.
- [맞춤 언어 모델 빌드 실패](https://developer.apple.com/documentation/analytics-reports/custom-language-model-builds-failed): 앱이 트리거한 맞춤 언어 모델 재빌드가 실패한 빈도를 분석합니다.
- [디스플레이 전력 정보](https://developer.apple.com/documentation/analytics-reports/display-power-information): 앱이 디스플레이 픽셀 속성에 미치는 영향을 검토합니다.
- [임베딩 생성](https://developer.apple.com/documentation/analytics-reports/embedding-generation): 앱의 임베딩 생성 처리량에 대한 세부 정보를 분석합니다.
- [HTTP Live Streaming 재생 오류](https://developer.apple.com/documentation/analytics-reports/http-live-streaming-playback-errors): 앱이 수신하는 재생 오류를 분석합니다.
- [메모리 한도를 초과한 실행 이미지](https://developer.apple.com/documentation/analytics-reports/launch-image-over-memory-limit): 메모리 한도를 초과해 앱이 로드에 실패하는 빈도를 분석합니다.
- [네트워킹 연결 활동](https://developer.apple.com/documentation/analytics-reports/networking-connection-activity): 앱이 네트워크 연결을 사용하는 방식을 검토합니다.
- [Spotlight 쿼리 성능](https://developer.apple.com/documentation/analytics-reports/spotlight-query-performance): 앱이 Spotlight 쿼리를 사용하는 방식을 검토합니다.
- [스트리밍 다운로드 성능](https://developer.apple.com/documentation/analytics-reports/streaming-downloads-performance): 앱에서 AVAssetDownloadTask API를 사용할 때의 다운로드 성능을 검토합니다.
- [스트리밍 재생 성능](https://developer.apple.com/documentation/analytics-reports/streaming-playback-performance): 앱에서 AVPlayerItem API를 사용할 때의 재생 성능을 검토합니다.
:::
