---
route: /documentation/OpenGLES
source_url: https://developer.apple.com/documentation/OpenGLES
source_locale: en-US
section: docc
content_type: symbol
title: OpenGL ES
original_title: OpenGL ES
source_hash: 8a5eb3734caaccba6b54b0cf186c8db854d0159933567241c16e06c0b36730e2
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:33+00:00'
last_translated_at: '2026-03-13T17:20:00+09:00'
---

# OpenGL ES

이 작고 효율적인 OpenGL 부분집합으로 3D 및 2D 그래픽 효과를 만듭니다.

## 개요

OpenGL ES는 하드웨어 가속 2D 및 3D 그래픽 렌더링을 위한 C 기반 인터페이스를 제공합니다. iOS의 OpenGL ES 프레임워크(`OpenGLES.framework`)는 OpenGL ES 사양 1.1, 2.0, 3.0 버전에 대한 구현을 제공합니다.

이 문서 모음은 EAGL이라고도 하는 iOS 기기의 OpenGL ES용 플랫폼별 API를 설명합니다. EAGL은 모든 OpenGL ES 상태를 캡슐화하는 그래픽 컨텍스트와, Core Animation 레이어를 OpenGL ES 그리기 명령의 대상지로 구성하는 기능을 제공합니다. 또한 EAGL은 texture, renderbuffer, framebuffer 같은 OpenGL ES 객체를 둘 이상의 그래픽 컨텍스트 간에 공유할 수 있게 합니다.

Khronos Group은 크로스플랫폼 OpenGL ES API용 OpenGL ES 사양과 레퍼런스를 유지 관리합니다.

- [OpenGL ES API Registry](http://www.khronos.org/registry/gles/)는 Khronos Group이 제공하는 OpenGL ES 사양 및 확장 문서의 공식 저장소입니다.
- 사용할 OpenGL ES 버전에 대한 API 및 OpenGL ES Shading Language 전체 레퍼런스는 다음 문서 모음을 참고하십시오.
- [OpenGL ES 1.1 Reference Pages](http://www.khronos.org/opengles/sdk/1.1/docs/man/)
- [OpenGL ES 2.0 Reference Pages](http://www.khronos.org/opengles/sdk/docs/man/)
- [OpenGL ES 3.0 Reference Pages](http://www.khronos.org/opengles/sdk/docs/man3/)

:::topic-grid
## 클래스
- [EAGLContext](https://developer.apple.com/documentation/opengles/eaglcontext): OpenGL ES를 사용해 그리는 데 필요한 상태 정보, 명령, 리소스를 관리하는 객체입니다. OpenGL ES 명령을 실행하려면 현재 렌더링 컨텍스트가 필요합니다.
- [EAGLSharegroup](https://developer.apple.com/documentation/opengles/eaglsharegroup): 하나 이상의 객체와 연결된 OpenGL ES 리소스를 관리하는 객체입니다. 객체가 초기화될 때 생성되며 이를 참조하는 마지막 객체가 해제될 때 함께 정리됩니다. opaque 객체이므로 개발자가 접근할 수 있는 API는 없습니다.
:::

:::topic-grid
## 프로토콜
- [EAGLDrawable](https://developer.apple.com/documentation/opengles/eagldrawable): 이 프로토콜을 구현하는 iOS 객체는 렌더링 표면으로 사용될 수 있으며 객체에 의해 화면에 표시될 수 있습니다. iOS 2.0에서는 이 프로토콜을 `CAEAGLLayer` 클래스만 구현하지만, 앞으로는 다른 클래스도 이를 구현할 수 있습니다. 이 프로토콜은 iOS 외부 객체가 구현하도록 의도된 것은 아닙니다.
:::

:::topic-grid
## 레퍼런스
- [EAGL Functions](https://developer.apple.com/documentation/opengles/eagl-functions): OpenGL ES 프레임워크의 함수를 설명합니다.
- [OpenGL ES Enumerations](https://developer.apple.com/documentation/opengles/opengl-es-enumerations)
- [OpenGL ES Constants](https://developer.apple.com/documentation/opengles/opengl-es-constants)
- [OpenGL ES Functions](https://developer.apple.com/documentation/opengles/opengl-es-functions)
- [OpenGL ES Data Types](https://developer.apple.com/documentation/opengles/opengl-es-data-types)
:::

:::topic-grid
## 변수
- [GL_SAMPLER_2D_SHADOW](https://developer.apple.com/documentation/opengles/gl_sampler_2d_shadow)
- [GL_TEXTURE_ENV_COLOR](https://developer.apple.com/documentation/opengles/gl_texture_env_color)
- [GL_TEXTURE_ENV_MODE](https://developer.apple.com/documentation/opengles/gl_texture_env_mode)
- [GL_TIMEOUT_IGNORED](https://developer.apple.com/documentation/opengles/gl_timeout_ignored)
:::

:::topic-grid
## 함수
- [glFramebufferTextureLayer(_:_:_:_:_:)](https://developer.apple.com/documentation/opengles/glframebuffertexturelayer(_:_:_:_:_:))
:::
