---
route: /documentation/QuartzCore
source_url: https://developer.apple.com/documentation/QuartzCore
source_locale: en-US
section: docc
content_type: symbol
title: Core Animation
original_title: Core Animation
source_hash: 921159408c17c77916a22b684632f6eb164c6e56821fa12975e0b180c4aa6871
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:04:19+00:00'
last_translated_at: '2026-03-13T21:56:00+09:00'
---

# Core Animation

시각 요소를 렌더링하고, 합성하고, 애니메이션합니다.

## 개요

Core Animation은 CPU에 부담을 주거나 앱을 느리게 하지 않으면서 높은 프레임률과 부드러운 애니메이션을 제공합니다. Core Animation은 애니메이션의 각 프레임을 그리는 작업 대부분을 대신 수행합니다. 개발자는 시작점과 끝점 같은 애니메이션 매개변수를 구성하면 되고, 나머지는 Core Animation이 처리합니다. 또한 전용 그래픽 하드웨어에 대부분의 작업을 넘겨 렌더링을 가속합니다. 자세한 내용은 [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)를 참고하십시오.

:::topic-grid
## 레이어 기초
- [CALayer](https://developer.apple.com/documentation/quartzcore/calayer): 이미지 기반 콘텐츠를 관리하고 해당 콘텐츠에 애니메이션을 수행할 수 있게 해 주는 객체입니다.
- [CALayerDelegate](https://developer.apple.com/documentation/quartzcore/calayerdelegate): 레이어 관련 이벤트에 응답하기 위해 앱이 구현할 수 있는 메서드입니다.
- [CAConstraint](https://developer.apple.com/documentation/quartzcore/caconstraint): 두 레이어 사이의 단일 레이아웃 제약을 나타내는 표현입니다.
- [CALayoutManager](https://developer.apple.com/documentation/quartzcore/calayoutmanager): 객체가 레이어와 그 하위 레이어의 레이아웃을 관리할 수 있게 해 주는 메서드입니다.
- [CAConstraintLayoutManager](https://developer.apple.com/documentation/quartzcore/caconstraintlayoutmanager): 제약 기반 레이아웃 관리자를 제공하는 객체입니다.
- [CAAction](https://developer.apple.com/documentation/quartzcore/caaction): Core Animation 레이어 변경에 의해 트리거되는 action에 인스턴스가 응답할 수 있게 해 주는 인터페이스입니다.
:::

:::topic-grid
## 텍스트, 도형, 그라디언트
- [CATextLayer](https://developer.apple.com/documentation/quartzcore/catextlayer): 일반 문자열 또는 속성 문자열의 단순한 텍스트 레이아웃과 렌더링을 제공하는 레이어입니다.
- [CAShapeLayer](https://developer.apple.com/documentation/quartzcore/cashapelayer): 자신의 좌표 공간에 cubic Bezier spline을 그리는 레이어입니다.
- [CAGradientLayer](https://developer.apple.com/documentation/quartzcore/cagradientlayer): 배경색 위에 색상 그라디언트를 그려 레이어의 형태를 채우는 레이어입니다.
:::

:::topic-grid
## 애니메이션
- [CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation): Core Animation의 애니메이션을 위한 추상 superclass입니다.
- [CAAnimationDelegate](https://developer.apple.com/documentation/quartzcore/caanimationdelegate): 애니메이션이 시작되고 멈출 때 앱이 응답할 수 있도록 구현하는 메서드입니다.
- [CAPropertyAnimation](https://developer.apple.com/documentation/quartzcore/capropertyanimation): 레이어 프로퍼티 값을 조작하는 애니메이션을 만들기 위한 추상 subclass입니다.
- [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation): 레이어 프로퍼티에 대해 기본적인 단일 keyframe 애니메이션 기능을 제공하는 객체입니다.
- [CAKeyframeAnimation](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation): 레이어 객체에 대한 keyframe 애니메이션 기능을 제공하는 객체입니다.
- [CASpringAnimation](https://developer.apple.com/documentation/quartzcore/caspringanimation): 레이어 프로퍼티에 스프링 같은 힘을 적용하는 애니메이션입니다.
- [CATransition](https://developer.apple.com/documentation/quartzcore/catransition): 레이어 상태 사이의 애니메이션 전환을 제공하는 객체입니다.
- [CAValueFunction](https://developer.apple.com/documentation/quartzcore/cavaluefunction): 애니메이션 변환을 유연하게 정의하는 방법을 제공하는 객체입니다.
:::

:::topic-grid
## 애니메이션 그룹
- [CAAnimationGroup](https://developer.apple.com/documentation/quartzcore/caanimationgroup): 여러 애니메이션을 그룹으로 묶어 동시에 실행할 수 있게 하는 객체입니다.
- [CATransaction](https://developer.apple.com/documentation/quartzcore/catransaction): 여러 레이어 트리 연산을 렌더 트리에 대한 원자적 업데이트로 묶는 메커니즘입니다.
:::

:::topic-grid
## 애니메이션 타이밍
- [CACurrentMediaTime()](https://developer.apple.com/documentation/quartzcore/cacurrentmediatime()): 현재 절대 시간을 초 단위로 반환합니다.
- [CAMediaTimingFunction](https://developer.apple.com/documentation/quartzcore/camediatimingfunction): 타이밍 곡선으로 애니메이션의 진행 속도를 정의하는 함수입니다.
- [CAMediaTiming](https://developer.apple.com/documentation/quartzcore/camediatiming): 객체가 부모 시간과 로컬 시간 사이를 매핑할 수 있도록 하는 계층적 타이밍 시스템을 모델링하는 메서드입니다.
- [CADisplayLink](https://developer.apple.com/documentation/quartzcore/cadisplaylink): 앱이 디스플레이의 refresh rate에 맞춰 그리기를 동기화할 수 있게 해 주는 timer 객체입니다.
- [CAMetalDisplayLink](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink): Metal 앱이 디스플레이와 애니메이션을 동기화하기 위한 callback을 등록할 때 사용하는 클래스입니다.
- [CAMetalDisplayLink.Update](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update): Metal display link 인스턴스의 단일 업데이트에 대한 정보를 저장합니다.
- [CAMetalDisplayLinkDelegate](https://developer.apple.com/documentation/quartzcore/cametaldisplaylinkdelegate): Metal display link에 대한 Core Animation callback에 응답하기 위해 앱이 구현하는 프로토콜입니다.
:::

:::topic-grid
## 파티클 시스템
- [CAEmitterLayer](https://developer.apple.com/documentation/quartzcore/caemitterlayer): 파티클 시스템을 방출하고, 애니메이션하며, 렌더링하는 레이어입니다.
- [CAEmitterCell](https://developer.apple.com/documentation/quartzcore/caemittercell): 파티클 레이어가 방출하는 파티클의 정의입니다.
:::

:::topic-grid
## 고급 레이어 옵션
- [CAScrollLayer](https://developer.apple.com/documentation/quartzcore/cascrolllayer): 자신의 bounds보다 큰 스크롤 가능한 콘텐츠를 표시하는 레이어입니다.
- [CATiledLayer](https://developer.apple.com/documentation/quartzcore/catiledlayer): 여러 수준의 세부 묘사로 잠재적으로 캐시되는 레이어 콘텐츠의 tile을 비동기적으로 제공하는 방법을 제공하는 레이어입니다.
- [CATransformLayer](https://developer.apple.com/documentation/quartzcore/catransformlayer): 다른 레이어 타입이 사용하는 평면화된 계층 렌더링 모델이 아니라, 진정한 3D 레이어 계층을 생성하는 데 사용하는 객체입니다.
- [CAReplicatorLayer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer): 기하학적, 시간적, 색상 변환이 다른 지정된 수의 하위 레이어 복사본을 생성하는 레이어입니다.
:::

:::topic-grid
## Metal 및 OpenGL
- [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer): Metal이 렌더링할 수 있고 일반적으로 화면에 표시되는 Core Animation 레이어입니다.
- [CAMetalDrawable](https://developer.apple.com/documentation/quartzcore/cametaldrawable): Core Animation 레이어와 연관된 Metal drawable입니다.
- [CAEAGLLayer](https://developer.apple.com/documentation/quartzcore/caeagllayer): iOS와 tvOS 앱에서 OpenGL 콘텐츠를 그릴 수 있게 지원하는 레이어입니다.
- [CAEDRMetadata](https://developer.apple.com/documentation/quartzcore/caedrmetadata): extended dynamic range(EDR) 값이 tone mapping되어야 하는 방식을 설명하는 metadata입니다.
- [CAOpenGLLayer](https://developer.apple.com/documentation/quartzcore/caopengllayer): OpenGL 콘텐츠 렌더링에 적합한 레이어를 제공하는 레이어입니다.
- [CARenderer](https://developer.apple.com/documentation/quartzcore/carenderer): 앱이 레이어 트리를 Core OpenGL context로 렌더링할 수 있게 해 주는 레이어입니다.
:::

:::topic-grid
## ProMotion
- [Optimizing iPhone and iPad apps to support ProMotion displays](https://developer.apple.com/documentation/quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays): 선호 refresh rate를 요청하고 애니메이션을 시스템과 동기화해 앱의 시각 품질을 높이고 전력을 절약합니다.
:::

:::topic-grid
## 레이어 콘텐츠의 원격 표시
- [CARemoteLayerClient](https://developer.apple.com/documentation/quartzcore/caremotelayerclient): 프로세스 간 렌더링을 위한 레거시 클래스입니다.
- [CARemoteLayerServer](https://developer.apple.com/documentation/quartzcore/caremotelayerserver): 프로세스 간 렌더링을 위한 레거시 클래스입니다.
:::

:::topic-grid
## 변환
- [Transforms](https://developer.apple.com/documentation/quartzcore/transforms): Core Animation의 레이어에 affine transformation을 적용할 수 있도록 transform matrix를 정의합니다.
:::

:::topic-grid
## Quartz Composer
- [QCCompositionLayer](https://developer.apple.com/documentation/Quartz/QCCompositionLayer): Core Animation 레이어 계층 안에서 Quartz Composer composition을 로드하고, 재생하고, 제어하는 레이어입니다.
:::

:::topic-grid
## 참고 자료
- [Core Animation Structures](https://developer.apple.com/documentation/quartzcore/core-animation-structures)
- [Core Animation Constants](https://developer.apple.com/documentation/quartzcore/core-animation-constants)
- [QuartzCore Functions](https://developer.apple.com/documentation/quartzcore/quartzcore-functions)
- [Core Animation Data Types](https://developer.apple.com/documentation/quartzcore/core-animation-data-types)
:::
