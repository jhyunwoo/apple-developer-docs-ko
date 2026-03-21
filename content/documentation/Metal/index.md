---
route: /documentation/Metal
source_url: https://developer.apple.com/documentation/Metal
source_locale: en-US
section: docc
content_type: symbol
title: Metal
original_title: Metal
source_hash: fb93acac4480fa65ebe1808f4437fba937fe4b4e69b77245bf0a4007238fad50
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:33:47+00:00'
last_translated_at: '2026-03-14T00:58:00+09:00'
---

# Metal

그래픽 프로세서를 사용해 고급 3D 그래픽을 렌더링하고 데이터를 병렬로 계산합니다.

## 개요

Metal 프레임워크는 앱이 기기의 그래픽 처리 장치(GPU)에 직접 접근할 수 있게 해 줍니다. Metal을 사용하면 앱이 GPU를 활용해 복잡한 장면을 빠르게 렌더링하고 계산 작업을 병렬로 실행할 수 있습니다. 예를 들어 다음과 같은 범주의 앱은 성능을 극대화하기 위해 Metal을 사용합니다.

- 정교한 2D 또는 3D 환경을 렌더링하는 게임
- Final Cut Pro 같은 비디오 처리 앱
- 대규모 데이터 세트를 분석하고 처리하는 과학 연구 앱
- 완전 몰입형 visionOS 앱

Metal은 그 기능을 보완하는 다른 프레임워크와 긴밀하게 함께 동작합니다. 예를 들어 [MetalFX](https://developer.apple.com/documentation/MetalFX)는 렌더링을 네이티브 해상도로 직접 그리는 것보다 더 짧은 시간에 업스케일하고, [MetalKit](https://developer.apple.com/documentation/MetalKit)은 Metal 콘텐츠를 화면에 표시하는 작업을 단순화합니다. [Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders) 프레임워크는 각 GPU의 고유한 하드웨어를 활용하는 최적화된 compute 및 rendering shader의 대규모 라이브러리를 제공합니다. visionOS에서는 [Compositor Services](https://developer.apple.com/documentation/CompositorServices) 프레임워크의 도움을 받아 완전 몰입형 입체 콘텐츠를 만들 수 있습니다.

[RealityKit](https://developer.apple.com/documentation/RealityKit), [SpriteKit](https://developer.apple.com/documentation/SpriteKit), [Core Image](https://developer.apple.com/documentation/CoreImage)를 포함한 많은 상위 수준 Apple 프레임워크도 Metal의 성능을 활용합니다. 이런 상위 수준 프레임워크는 GPU 프로그래밍 세부 사항을 대신 구현해 줍니다. 하지만 일반적으로는 사용자 정의 Metal 코드와 shader 코드를 직접 작성할 때 더 나은 성능을 얻을 수 있습니다. shader 구현 세부 사항은 [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf)을 참고하십시오.

:::topic-grid
## 핵심 사항
- [Understanding the Metal 4 core API](https://developer.apple.com/documentation/metal/understanding-the-metal-4-core-api): Metal 4 기반 API의 기능과 특징을 살펴봅니다.
- [Drawing a triangle with Metal 4](https://developer.apple.com/documentation/metal/drawing-a-triangle-with-metal-4): GPU의 render pipeline으로 draw 명령을 실행해 색상이 있는 회전 2D 삼각형을 렌더링합니다.
- [Performing calculations on a GPU](https://developer.apple.com/documentation/metal/performing-calculations-on-a-gpu): Metal을 사용해 GPU를 찾고 그 위에서 계산을 수행합니다.
- [Using Metal to draw a view’s contents](https://developer.apple.com/documentation/metal/using-metal-to-draw-a-view's-contents): MetalKit view와 render pass를 만들어 view의 콘텐츠를 그립니다.
:::

:::topic-grid
## 샘플
- [Metal sample code library](https://developer.apple.com/documentation/metal/metal-sample-code-library): Metal 샘플 전체 모음을 살펴봅니다.
:::

:::topic-grid
## GPU 기기
- [GPU devices and work submission](https://developer.apple.com/documentation/metal/gpu-devices-and-work-submission): 사용 가능한 GPU를 찾고, command buffer로 작업을 제출하며, 작업을 중단하고, 여러 GPU 간 작업을 조정합니다.
:::

:::topic-grid
## Command encoder
- [Render passes](https://developer.apple.com/documentation/metal/render-passes): 이미지에 그래픽을 그리기 위한 render pass를 encode합니다.
- [Compute passes](https://developer.apple.com/documentation/metal/compute-passes): thread grid에서 계산을 병렬로 실행하며 GPU의 여러 코어에서 Metal 리소스 데이터를 처리하고 조작하는 compute pass를 encode합니다.
- [Machine learning passes](https://developer.apple.com/documentation/metal/machine-learning-passes): Metal 앱의 GPU 워크플로에 머신 러닝 모델 추론을 추가합니다.
- [Blit passes](https://developer.apple.com/documentation/metal/blit-passes): buffer와 texture 같은 GPU 리소스로 데이터를 조정하고 복사하는 block information transfer pass를 encode합니다.
- [Indirect command encoding](https://developer.apple.com/documentation/metal/indirect-command-encoding): draw 명령을 Metal buffer에 저장하고 나중에 GPU에서 한 번 또는 반복적으로 실행합니다.
- [Ray tracing with acceleration structures](https://developer.apple.com/documentation/metal/ray-tracing-with-acceleration-structures): 삼각형과 bounding volume을 사용해 장면 기하 구조를 표현하고, 광선을 장면 전체에 빠르게 추적합니다.
:::

:::topic-grid
## 리소스
- [Resource fundamentals](https://developer.apple.com/documentation/metal/resource-fundamentals): buffer와 texture를 포함한 모든 Metal 메모리 리소스의 공통 속성과 기본 메모리 구성 방법을 제어합니다.
- [Buffers](https://developer.apple.com/documentation/metal/buffers): 앱이 shader 함수와 정보를 교환할 때 사용하는 비정형 데이터를 생성하고 관리합니다.
- [Textures](https://developer.apple.com/documentation/metal/textures): 앱이 shader 함수와 정보를 교환할 때 사용하는 정형 데이터를 생성하고 관리합니다.
- [Memory heaps](https://developer.apple.com/documentation/metal/memory-heaps): 여러 buffer, texture, 기타 리소스를 위한 큰 메모리 할당을 생성해 앱의 GPU 메모리 관리를 직접 제어합니다.
- [Resource loading](https://developer.apple.com/documentation/metal/resource-loading): 전용 입출력 큐를 GPU 작업과 함께 실행해 게임과 앱의 asset을 빠르게 로드합니다.
- [Resource synchronization](https://developer.apple.com/documentation/metal/resource-synchronization): barrier, fence, event를 사용해 동일한 리소스에 동시에 접근할 수 있는 여러 명령의 읽기와 쓰기를 조정합니다.
:::

:::topic-grid
## Shader 컴파일 및 라이브러리
- [Using the Metal 4 compilation API](https://developer.apple.com/documentation/metal/using-the-metal-4-compilation-api): 앱의 shader를 언제 어떻게 컴파일할지 제어합니다.
- [Shader libraries](https://developer.apple.com/documentation/metal/shader-libraries): 앱의 Metal shader를 관리하고 로드합니다.
- [Using function specialization to build pipeline variants](https://developer.apple.com/documentation/metal/using-function-specialization-to-build-pipeline-variants): 공통 shader 소스에서 다양한 세부 수준용 pipeline을 만듭니다.
:::

:::topic-grid
## 표시
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos): Metal 콘텐츠를 최적으로 표시할 수 있도록 window와 view를 설정합니다.
- [Managing your Metal app window in iPadOS](https://developer.apple.com/documentation/metal/managing-your-metal-app-window-in-ipados): Metal 콘텐츠의 동적 크기 조절을 처리하는 window를 설정합니다.
- [Adapting your game interface for smaller screens](https://developer.apple.com/documentation/metal/adapting-your-game-interface-for-smaller-screens): 플레이어가 어떤 기기에서 게임을 실행하든 텍스트가 읽기 쉽도록 만듭니다.
- [Onscreen presentation](https://developer.apple.com/documentation/metal/onscreen-presentation): GPU의 렌더링 pass 출력을 앱 안에서 사용자에게 표시합니다.
- [HDR content](https://developer.apple.com/documentation/metal/hdr-content): 더 생생한 색을 표현하기 위해 high dynamic range를 활용합니다.
:::

:::topic-grid
## 개발자 도구
- [Supporting Simulator in a Metal app](https://developer.apple.com/documentation/metal/supporting-simulator-in-a-metal-app): Simulator에서 앱을 실행할 수 있도록 Metal 앱에 대체 render 경로를 구성합니다.
- [Capturing Metal commands programmatically](https://developer.apple.com/documentation/metal/capturing-metal-commands-programmatically): 앱에서 Metal frame capture를 호출한 뒤 결과 GPU trace를 파일로 저장하거나 Xcode에서 확인합니다.
- [Logging shader debug messages](https://developer.apple.com/documentation/metal/logging-shader-debug-messages): shader logging을 사용해 shader가 생성한 디버깅 메시지를 출력합니다.
- [Developing Metal apps that run in Simulator](https://developer.apple.com/documentation/metal/developing-metal-apps-that-run-in-simulator): Simulator에서 Metal 앱을 프로토타이핑하고 테스트합니다.
- [Improving your game’s graphics performance and settings](https://developer.apple.com/documentation/metal/improving-your-games-graphics-performance-and-settings): 강력한 Metal 개발 도구 모음을 사용해 성능 문제를 해결하고 Apple 플랫폼에서 부드러운 경험을 위한 기본 설정을 개발합니다.
- [Metal debugger](https://developer.apple.com/documentation/Xcode/Metal-debugger): GPU trace로 Metal workload를 디버그하고 프로파일링합니다.
- [Metal developer workflows](https://developer.apple.com/documentation/Xcode/Metal-developer-workflows): 앱의 Metal API 및 GPU 함수 사용과 관련된 문제를 찾고 수정합니다.
- [GPU counters and counter sample buffers](https://developer.apple.com/documentation/metal/gpu-counters-and-counter-sample-buffers): 하나 이상의 counter를 샘플링해 GPU 기기의 런타임 데이터를 가져옵니다.
- [Metal debugging types](https://developer.apple.com/documentation/metal/metal-debugging-types): capture manager와 capture scope를 만들고, command buffer 실행 후 GPU 기기 로그를 검토합니다.
:::

:::topic-grid
## Apple silicon
- [Porting your Metal code to Apple silicon](https://developer.apple.com/documentation/Apple-Silicon/porting-your-metal-code-to-apple-silicon): Apple silicon과 Intel 기반 Mac 모두에서 실행되는 Metal 앱 버전을 만듭니다.
- [Tailor your apps for Apple GPUs and tile-based deferred rendering](https://developer.apple.com/documentation/metal/tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering): imageblock, tile shader, raster order group을 포함한 Apple GPU의 특징적인 기능을 알아봅니다.
:::

:::topic-grid
## 참고 자료
- [Metal structures](https://developer.apple.com/documentation/metal/metal-structures)
- [Metal enumerations](https://developer.apple.com/documentation/metal/metal-enumerations)
- [Metal constants](https://developer.apple.com/documentation/metal/metal-constants)
- [Metal data types](https://developer.apple.com/documentation/metal/metal-data-types)
- [Metal variables](https://developer.apple.com/documentation/metal/metal-variables)
:::

:::topic-grid
## 구조체
- [MTLDeviceError](https://developer.apple.com/documentation/metal/mtldeviceerror-swift.struct)
:::

:::topic-grid
## 변수
- [MTLDeviceErrorDomain](https://developer.apple.com/documentation/metal/mtldeviceerrordomain)
:::

:::asset-list
- `https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf` -> `https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf` (pending)
:::
