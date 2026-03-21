---
route: /documentation/MetricKit
source_url: https://developer.apple.com/documentation/MetricKit
source_locale: en-US
section: docc
content_type: symbol
title: MetricKit
original_title: MetricKit
source_hash: f3d0490b2c049aeccfb4d2d5cdbd1f36c6976c8db196649e2b1f9634428c62af
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:11:26+00:00'
last_translated_at: '2026-03-13T23:11:40+09:00'
---

# MetricKit

예외 및 충돌 진단, 전력 및 성능 metric에 대한 기기별 보고서를 집계하고 분석합니다.

## 개요

MetricKit을 사용하면 시스템이 수집한 기기 내 앱 진단 정보와 전력 및 성능 metric을 받을 수 있습니다. 시스템은 등록된 앱에 대해 이전 24시간에 대한 metric 보고서를 하루에 최대 한 번 전달하며, 진단 보고서는 iOS 15 이상과 macOS 12 이상에서 즉시 전달합니다. 이 프레임워크는 visionOS에서 실행 중인 앱에 대해 충돌, 멈춤, 에너지, 디스크 쓰기 진단을 지원하지만, visionOS에서 실행 중인 앱에 대한 metric은 보고하지 않습니다. 여기에는 visionOS용으로 빌드한 앱과 visionOS에서 실행되는 호환 iPhone 및 iPad 앱이 모두 포함됩니다.

이 보고서의 데이터를 사용해 iOS 앱, macOS 앱, 또는 Mac Catalyst로 만든 Mac 앱의 성능을 개선할 수 있습니다. 이 프레임워크에는 다음이 포함되어 있습니다.

- 관리자 클래스와 subscriber protocol
- 보고된 데이터를 담는 payload 클래스
- metric 및 진단의 각 범주별 클래스
- 셀룰러 연결 막대 수 같은 측정 단위를 표현하는 클래스
- histogram처럼 누적 데이터를 표현하는 클래스
- 진단 정보에서 stack trace를 캡처하는 클래스

:::topic-grid
## 핵심
- [MXMetricManager](https://developer.apple.com/documentation/metrickit/mxmetricmanager): metric 수신을 등록하고, 사용자 정의 metric용 로그를 만들고, 과거 보고서에 접근할 수 있게 해 주는 공유 객체입니다.
- [MXMetricPayload](https://developer.apple.com/documentation/metrickit/mxmetricpayload): 일일 metric 보고서를 캡슐화하는 객체입니다.
- [MXDiagnosticPayload](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload): 진단 보고서를 캡슐화하는 객체입니다.
- [MXMetricManagerSubscriber](https://developer.apple.com/documentation/metrickit/mxmetricmanagersubscriber): 일일 metric 보고서를 수신하는 메서드를 정의하는 protocol입니다.
:::

:::topic-grid
## 성능 개선
- [Improving your app’s performance](https://developer.apple.com/documentation/Xcode/improving-your-app-s-performance): 지속적인 개선 사이클을 사용해 앱 성능을 모델링하고, 측정하고, 향상합니다.
:::

:::topic-grid
## 배터리 metric
- [MXCellularConditionMetric](https://developer.apple.com/documentation/metrickit/mxcellularconditionmetric): 셀룰러 네트워크 상태에 대한 metric을 나타내는 객체입니다.
- [MXCPUMetric](https://developer.apple.com/documentation/metrickit/mxcpumetric): CPU 사용량에 대한 metric을 나타내는 객체입니다.
- [MXDisplayMetric](https://developer.apple.com/documentation/metrickit/mxdisplaymetric): 화면에 앱을 표시하는 데 사용된 전력에 대한 metric을 나타내는 객체입니다.
- [MXGPUMetric](https://developer.apple.com/documentation/metrickit/mxgpumetric): GPU 사용량에 대한 metric을 나타내는 객체입니다.
- [MXLocationActivityMetric](https://developer.apple.com/documentation/metrickit/mxlocationactivitymetric): 기기의 위치 추적 기능 사용량에 대한 metric을 나타내는 객체입니다.
- [MXNetworkTransferMetric](https://developer.apple.com/documentation/metrickit/mxnetworktransfermetric): 네트워크 전송에 대한 metric을 나타내는 객체입니다.
- [MXCPUExceptionDiagnostic](https://developer.apple.com/documentation/metrickit/mxcpuexceptiondiagnostic): 치명적이거나 비치명적인 CPU 예외에 대한 진단 보고서를 나타내는 객체입니다.
:::

:::topic-grid
## 성능 metric
- [MXAppLaunchDiagnostic](https://developer.apple.com/documentation/metrickit/mxapplaunchdiagnostic): 앱 실행 진단 보고서를 캡슐화하는 진단 하위 클래스입니다.
- [MXAppExitMetric](https://developer.apple.com/documentation/metrickit/mxappexitmetric): 포그라운드 및 백그라운드 앱 종료 유형에 대한 metric을 나타내는 객체입니다.
- [MXAppRunTimeMetric](https://developer.apple.com/documentation/metrickit/mxappruntimemetric): 앱이 활성 상태였던 시간량에 대한 metric을 나타내는 객체입니다.
- [MXMemoryMetric](https://developer.apple.com/documentation/metrickit/mxmemorymetric): 앱의 메모리 사용량에 대한 metric을 나타내는 객체입니다.
- [MXCrashDiagnostic](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic): 앱 충돌에 대한 진단 보고서를 나타내는 객체입니다.
:::

:::topic-grid
## 반응성 metric
- [MXAnimationMetric](https://developer.apple.com/documentation/metrickit/mxanimationmetric): 앱의 애니메이션 반응성에 대한 metric을 나타내는 객체입니다.
- [MXAppLaunchMetric](https://developer.apple.com/documentation/metrickit/mxapplaunchmetric): 앱 실행 시간에 대한 metric을 나타내는 객체입니다.
- [MXAppResponsivenessMetric](https://developer.apple.com/documentation/metrickit/mxappresponsivenessmetric): 사용자 상호 작용에 대한 앱의 반응성에 대한 metric을 나타내는 객체입니다.
- [MXHangDiagnostic](https://developer.apple.com/documentation/metrickit/mxhangdiagnostic): 사용자 입력에 민첩하게 대응하지 못할 만큼 바쁜 앱에 대한 진단 보고서를 나타내는 객체입니다.
:::

:::topic-grid
## 디스크 사용 metric
- [MXDiskIOMetric](https://developer.apple.com/documentation/metrickit/mxdiskiometric): 디스크 사용량에 대한 metric을 나타내는 객체입니다.
- [MXDiskSpaceUsageMetric](https://developer.apple.com/documentation/metrickit/mxdiskspaceusagemetric): 앱의 디스크 공간 사용량에 대한 metric을 나타내는 객체입니다.
- [MXDiskWriteExceptionDiagnostic](https://developer.apple.com/documentation/metrickit/mxdiskwriteexceptiondiagnostic): 디스크 쓰기 예외에 대한 진단 보고서를 나타내는 객체입니다.
:::

:::topic-grid
## 사용자 정의 metric
- [MXSignpostMetric](https://developer.apple.com/documentation/metrickit/mxsignpostmetric): 사용자 정의 metric을 나타내는 객체입니다.
:::

:::topic-grid
## 데이터 타입
- [MXCallStackTree](https://developer.apple.com/documentation/metrickit/mxcallstacktree): 예외에 대한 call stack을 나타내는 객체입니다.
- [MXMetaData](https://developer.apple.com/documentation/metrickit/mxmetadata): 기기에 대한 시스템 수준 정보를 담는 객체입니다.
- [MXAverage](https://developer.apple.com/documentation/metrickit/mxaverage): 평균값을 위한 측정 단위입니다.
- [MXHistogram](https://developer.apple.com/documentation/metrickit/mxhistogram): 동일한 단위 타입을 가진 데이터 값의 histogram을 나타내는 객체입니다.
- [MXDiagnostic](https://developer.apple.com/documentation/metrickit/mxdiagnostic): 진단 정보를 위한 추상 데이터 클래스입니다.
- [MXMetric](https://developer.apple.com/documentation/metrickit/mxmetric): metric을 위한 추상 데이터 클래스입니다.
- [MXError.Code](https://developer.apple.com/documentation/metrickit/mxerror/code): 앱 metric에서 반환되는 오류 값의 오류 코드입니다.
- [MXErrorDomain](https://developer.apple.com/documentation/metrickit/mxerrordomain): 앱 metric 오류 값의 오류 도메인입니다.
- [MXError](https://developer.apple.com/documentation/metrickit/mxerror): 앱 metric 오류 처리를 위한 오류 타입입니다.
- [MXCrashDiagnosticObjectiveCExceptionReason](https://developer.apple.com/documentation/metrickit/mxcrashdiagnosticobjectivecexceptionreason): 처리되지 않은 ObjC 예외의 예외 사유를 나타내는 객체입니다.
- [MXSignpostRecord](https://developer.apple.com/documentation/metrickit/mxsignpostrecord): signpost interval 또는 event에 대한 기록을 나타내는 객체입니다.
:::
