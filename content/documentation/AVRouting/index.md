---
route: /documentation/AVRouting
source_url: https://developer.apple.com/documentation/AVRouting
source_locale: en-US
section: docc
content_type: symbol
title: AVRouting
original_title: AVRouting
source_hash: c0f9f952c2530454eca54441c2e5bae7744de3e6188d1daed8ce686bd22f56f3
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:17:18+00:00'
last_translated_at: '2026-03-13T22:37:00+09:00'
---

# AVRouting

시스템 route picker에서 미디어를 스트리밍할 사용자 정의 목적지를 표시합니다.

## 개요

AVRouting 프레임워크를 사용하면 [AVRoutePickerView](https://developer.apple.com/documentation/AVKit/AVRoutePickerView)에 third-party 장치와 프로토콜을 추가할 수 있습니다. 이를 통해 사용자는 AirPlay와 같은 시스템 메뉴를 사용해 third-party 프로토콜을 통해 AV 콘텐츠를 스트리밍할 수 있습니다.

사용자가 view를 탭하면 시스템이 사용 가능한 미디어 수신기 목록을 표시하는 popover를 제공합니다. 앱 번들에 [Media Device Discovery Extension](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.media-device-discovery-extension) entitlement가 포함된 extension이 있으면, 장치가 근처에 있을 때 시스템이 그 extension을 실행하고 관련 third-party 프로토콜을 picker에 추가합니다.

![항목 목록이 있는 popover 스크린샷입니다. 맨 위 항목은 오른쪽에 체크 표시가 있는 iPad 아이콘이며, 그 아래에는 Speakers and TVs 제목과 여섯 개의 하위 항목이 표시됩니다. 첫 번째 하위 항목은 Third-party device이며, 이어서 AirPlay와 Third-party protocol이 표시됩니다. 나머지 하위 항목은 왼쪽에 Apple TV 아이콘이 있는 Sunset Beach, 왼쪽에 지구본 아이콘이 있는 Link with TV code, 그리고 Show more입니다.](https://developer.apple.com)

### 시스템 장치 선택기 view에 사용자 정의 route 추가

앱이 근처 third-party 미디어 수신기를 검색하려는 의도를 표시하려면 view에 사용자 정의 routing controller([AVCustomRoutingController](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller))를 설정하십시오.

```swift
struct DevicePickerView: UIViewRepresentable {
    func makeUIView(context: Context) -> UIView {
        let routePickerView = AVRoutePickerView()
        routePickerView.delegate = context.coordinator
        routePickerView.customRoutingController = RouteManager.shared.customRoutingController
```

그다음 view에 앱이 추가하려는 특정 장치를 알려 주십시오. 각 장치는 `Info.plist` 파일의 uniform type identifier를 통해 자신을 구별하는 고유한 device discovery extension을 필요로 합니다. [type](https://developer.apple.com/documentation/avrouting/avcustomroutingactionitem/type)을 해당 identifier로 설정한 사용자 정의 routing action([AVCustomRoutingActionItem](https://developer.apple.com/documentation/avrouting/avcustomroutingactionitem))을 추가하고, 이를 controller의 [customActionItems](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller/customactionitems)에 전달합니다.

```swift
func routePickerViewWillBeginPresentingRoutes(_ routePickerView: AVRoutePickerView) {
    if let type = UTType("com.example.apple-DataAccessDemo.menu") {
        let customRow1 = AVCustomRoutingActionItem()
        customRow1.type = type
        RouteManager.shared.customRoutingController?.customActionItems = [customRow1]
    }
}
```

extension이 런타임에 장치를 찾으면, 그 장치를 시스템에 전달해 picker에 표시합니다. 사용자 정의 프로토콜로 미디어를 라우팅하는 완전한 샘플 코드 프로젝트는 [Discovering a third-party media-streaming device](https://developer.apple.com/documentation/DeviceDiscoveryExtension/discovering-a-third-party-media-streaming-device)를 참고하십시오.

:::topic-grid
## 미디어 라우팅
- [AVCustomRoutingController](https://developer.apple.com/documentation/avrouting/avcustomroutingcontroller): 장치와 목적지 사이의 연결을 관리하는 객체입니다.
- [AVCustomRoutingControllerDelegate](https://developer.apple.com/documentation/avrouting/avcustomroutingcontrollerdelegate): 사용자 정의 routing controller의 delegate를 위한 프로토콜입니다.
- [AVCustomRoutingEvent](https://developer.apple.com/documentation/avrouting/avcustomroutingevent): route에서 발생하는 이벤트를 표현하는 객체입니다.
- [AVCustomRoutingActionItem](https://developer.apple.com/documentation/avrouting/avcustomroutingactionitem): 장치 route picker에 표시할 사용자 정의 action 항목을 표현하는 객체입니다.
:::

:::topic-grid
## 재생 중재
- [AVRoutingPlaybackArbiter](https://developer.apple.com/documentation/avrouting/avroutingplaybackarbiter): 재생 라우팅 환경설정을 관리하는 객체입니다.
- [AVRoutingPlaybackParticipant](https://developer.apple.com/documentation/avrouting/avroutingplaybackparticipant): 재생 라우팅 중재에 참여하는 객체를 위한 프로토콜입니다.
:::
