---
route: /documentation/IOSurface
source_url: https://developer.apple.com/documentation/IOSurface
source_locale: en-US
section: docc
content_type: symbol
title: IOSurface
original_title: IOSurface
source_hash: 5273ccddeb6b4f246c083cc076feb826b60ccf0ee2912f4da3293636d00f1eb0
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:44:32+00:00'
last_translated_at: '2026-03-14T00:03:00+09:00'
---

# IOSurface

하드웨어 가속 버퍼 데이터(framebuffer와 texture)를 여러 프로세스 간에 공유합니다. 이미지 메모리를 더 효율적으로 관리합니다.

## 개요

IOSurface 프레임워크는 프로세스 경계를 넘어 공유하기에 적합한 framebuffer 객체를 제공합니다. 보안을 강화하기 위해 애플리케이션이 복잡한 이미지 압축 해제와 드로잉 로직을 별도 프로세스로 옮길 수 있도록 하는 데 흔히 사용됩니다.

:::topic-grid
## 클래스
- [IOSurface](https://developer.apple.com/documentation/iosurface/iosurface): IOSurface 불투명 객체를 나타내는 데이터 타입입니다.
- [IOSurfaceRef](https://developer.apple.com/documentation/iosurface/iosurfaceref): IOSurface 불투명 객체를 나타내는 데이터 타입입니다.
:::

:::topic-grid
## 구조체
- [IOSurfaceLockOptions](https://developer.apple.com/documentation/iosurface/iosurfacelockoptions)
- [IOSurfacePropertyKey](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey)
- [IOSurfacePurgeabilityState](https://developer.apple.com/documentation/iosurface/iosurfacepurgeabilitystate)
:::

:::topic-grid
## 참고 자료
- [IOSurface Structures](https://developer.apple.com/documentation/iosurface/iosurface-structures)
- [IOSurface Constants](https://developer.apple.com/documentation/iosurface/iosurface-constants)
- [IOSurface Functions](https://developer.apple.com/documentation/iosurface/iosurface-functions)
:::

:::topic-grid
## 변수
- [kIOSurfaceContentHeadroom](https://developer.apple.com/documentation/iosurface/kiosurfacecontentheadroom)
- [kIOSurfaceCopybackCache](https://developer.apple.com/documentation/iosurface/kiosurfacecopybackcache)
- [kIOSurfaceCopybackInnerCache](https://developer.apple.com/documentation/iosurface/kiosurfacecopybackinnercache)
- [kIOSurfaceDefaultCache](https://developer.apple.com/documentation/iosurface/kiosurfacedefaultcache)
- [kIOSurfaceInhibitCache](https://developer.apple.com/documentation/iosurface/kiosurfaceinhibitcache)
- [kIOSurfaceMapCacheShift](https://developer.apple.com/documentation/iosurface/kiosurfacemapcacheshift)
- [kIOSurfaceMapCopybackCache](https://developer.apple.com/documentation/iosurface/kiosurfacemapcopybackcache)
- [kIOSurfaceMapCopybackInnerCache](https://developer.apple.com/documentation/iosurface/kiosurfacemapcopybackinnercache)
- [kIOSurfaceMapDefaultCache](https://developer.apple.com/documentation/iosurface/kiosurfacemapdefaultcache)
- [kIOSurfaceMapInhibitCache](https://developer.apple.com/documentation/iosurface/kiosurfacemapinhibitcache)
- [kIOSurfaceMapWriteCombineCache](https://developer.apple.com/documentation/iosurface/kiosurfacemapwritecombinecache)
- [kIOSurfaceMapWriteThruCache](https://developer.apple.com/documentation/iosurface/kiosurfacemapwritethrucache)
- [kIOSurfaceWriteCombineCache](https://developer.apple.com/documentation/iosurface/kiosurfacewritecombinecache)
- [kIOSurfaceWriteThruCache](https://developer.apple.com/documentation/iosurface/kiosurfacewritethrucache)
:::
