---
route: /documentation/Snapshots
source_url: https://developer.apple.com/documentation/Snapshots
source_locale: en-US
section: docc
content_type: symbol
title: Maps Web Snapshots
original_title: Maps Web Snapshots
source_hash: c7f2c67d73b621c08056921e8844b9f01153a9fc8c405c6f6fbe0e35e7b7e083
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:43:21+00:00'
last_translated_at: '2026-03-13T20:45:00+09:00'
---

# Maps Web Snapshots

URL로부터 지도의 정적 이미지를 생성합니다.

## 개요

Maps Web Snapshots 서비스를 사용해 URL로부터 정적 지도 이미지를 생성하십시오. Snapshots는 대화형 지도가 필요하지 않을 때 언제든 사용할 수 있으며, 일반적으로 이미지 URL을 쓰는 모든 곳에서 사용할 수 있습니다. 예를 들면 웹 페이지나, 이메일 클라이언트처럼 JavaScript를 사용할 수 없는 곳입니다.

![Maps Web Snapshots API를 사용해 생성한 지도의 스크린샷입니다.](https://developer.apple.com)

:::note 참고
웹에서 대화형 지도가 필요하다면 [MapKit JS](https://developer.apple.com/documentation/MapKitJS)를 참고하십시오. iOS, macOS, tvOS 앱에서 정적 지도 스냅샷을 생성하려면 [MKMapSnapshotter](https://developer.apple.com/documentation/MapKit/MKMapSnapshotter)를 참고하십시오.
:::

서명되고 검증된 snapshot URL을 구성하는 방법은 [Generating a URL and Signature to Create a Maps Web Snapshot](https://developer.apple.com/documentation/snapshots/generating-a-url-and-signature-to-create-a-maps-web-snapshot)을 참고하십시오. 필요한 서명은 Apple Developer 계정을 통해 얻은 자격 증명을 사용해 생성합니다. 이 자격 증명을 얻는 방법은 [Creating a Maps identifier and a private key](https://developer.apple.com/documentation/AppleMapsServerAPI/creating-a-maps-identifier-and-a-private-key)를 참고하십시오. 또한 [Create a Map](https://developer.apple.com/maps/create-a-map/)을 사용해 장소 정보를 보여 주는 HTML도 얻을 수 있습니다.

Maps Web Snapshots의 사용량 제한에 대한 자세한 내용은 Apple Developer의 [Maps on the Web](https://developer.apple.com/maps/web/) 페이지를 참고하십시오.

:::topic-grid
## 핵심 사항
- [Generating a URL and Signature to Create a Maps Web Snapshot](https://developer.apple.com/documentation/snapshots/generating-a-url-and-signature-to-create-a-maps-web-snapshot): Snapshot URL을 만들고 요청을 검증하기 위한 서명을 생성합니다.
- [Annotation](https://developer.apple.com/documentation/snapshots/annotation): annotation 특성을 설명하는 Snapshot URL용 객체입니다.
- [Overlay](https://developer.apple.com/documentation/snapshots/overlay): overlay의 점과 너비, 색상, 대시 패턴 같은 스타일을 포함해 overlay 형태 특성을 설명하는 Snapshot URL용 JSON 객체입니다.
- [OverlayStyle](https://developer.apple.com/documentation/snapshots/overlaystyle): overlay에 재사용 가능한 스타일을 설명하는 JSON 객체입니다.
- [Image](https://developer.apple.com/documentation/snapshots/image): 지도 annotation에 사용할 사용자 정의 이미지의 특성을 설명하는 Snapshot URL용 JSON 객체입니다.
:::

:::topic-grid
## Snapshot
- [Create a Maps Web Snapshot](https://developer.apple.com/documentation/snapshots/get-a-map-snapshot): 쿼리 매개변수로 제공한 특성을 가진 지도 이미지를 생성합니다.
:::
