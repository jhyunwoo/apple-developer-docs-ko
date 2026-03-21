---
route: /documentation/MetalKit
source_url: https://developer.apple.com/documentation/MetalKit
source_locale: en-US
section: docc
content_type: symbol
title: MetalKit
original_title: MetalKit
source_hash: 5e0bc925e93a1a9a2c5b3b9134a613f7f207b7b6a4ffff553728fc4d1c2cc976
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:44:32+00:00'
last_translated_at: '2026-03-14T00:03:00+09:00'
---

# MetalKit

공통 유틸리티 클래스 집합을 사용해 Metal 앱을 더 빠르고 쉽게 빌드합니다.

:::topic-grid
## 뷰 관리
- [MTKView](https://developer.apple.com/documentation/metalkit/mtkview): Metal 객체를 생성, 구성, 표시하는 특수한 뷰입니다.
- [MTKViewDelegate](https://developer.apple.com/documentation/metalkit/mtkviewdelegate): MetalKit 뷰의 드로잉 및 크기 조절 이벤트에 응답하기 위한 메서드입니다.
:::

:::topic-grid
## 텍스처 로딩
- [MTKTextureLoader](https://developer.apple.com/documentation/metalkit/mtktextureloader): 일반적인 이미지 포맷의 기존 데이터에서 texture를 생성하는 객체입니다.
:::

:::topic-grid
## 모델 처리
- [MTKMesh](https://developer.apple.com/documentation/metalkit/mtkmesh): Model I/O mesh의 vertex 데이터를 담는 컨테이너로, Metal 앱에서 사용하기에 적합합니다.
- [MTKMeshBuffer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer): Model I/O mesh의 vertex 데이터를 뒷받침하는 buffer로, Metal 앱에서 사용하기에 적합합니다.
- [MTKMeshBufferAllocator](https://developer.apple.com/documentation/metalkit/mtkmeshbufferallocator): Model I/O mesh의 vertex 데이터를 뒷받침하는 MetalKit buffer를 할당하기 위한 인터페이스로, Metal 앱에서 사용하기에 적합합니다.
- [MTKSubmesh](https://developer.apple.com/documentation/metalkit/mtksubmesh): Model I/O submesh의 index 데이터를 담는 컨테이너로, Metal 앱에서 사용하기에 적합합니다.
- [Conversion Functions](https://developer.apple.com/documentation/metalkit/conversion-functions): Metal과 Model I/O의 vertex 표현 사이를 변환합니다.
- [Model Errors](https://developer.apple.com/documentation/metalkit/model-errors): 모델 처리 메서드가 던지는 오류를 알아봅니다.
:::

:::topic-grid
## 참고 자료
- [MetalKit Functions](https://developer.apple.com/documentation/metalkit/metalkit-functions): MetalKit 프레임워크는 Metal 및 Model I/O 프레임워크와 효율적으로 연동하기 위해 사용하는 helper 함수를 정의합니다.
:::
