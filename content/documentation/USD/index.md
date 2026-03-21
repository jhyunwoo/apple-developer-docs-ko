---
route: /documentation/USD
source_url: https://developer.apple.com/documentation/USD
source_locale: en-US
section: docc
content_type: article
title: USD
original_title: USD
source_hash: e8023f3e6d1e1ca42a6da8dbc7cbffcb9d116e6fce407d350150cafcb5de99bd
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:01:50+00:00'
last_translated_at: '2026-03-14T03:05:00+09:00'
---

# USD

3D 장면을 표현하기 위한 효율적이고 확장 가능한 방법입니다.

## 개요

[Universal Scene Description](https://openusd.org/release/index.html)(*OpenUSD*이지만 일반적으로는 *USD*라고 부릅니다)는 그래픽 데이터를 작성하고, 읽고, 스트리밍하기 위한 효율적이고 확장 가능한 시스템입니다. 원래 Pixar의 장편 영화 제작을 위해 개발되었고, 지금은 [Alliance for OpenUSD (AOUSD)](https://aousd.org)가 추진하는 개방형 표준 제안입니다. Apple과 Pixar는 모두 AOUSD의 창립 멤버입니다.

USD는 증강 현실용 3D 콘텐츠를 포함한 Apple의 3D 콘텐츠 선택 형식이기도 합니다. RealityKit 및 ARKit 앱에서 USD 파일을 로드하거나 Reality Composer Pro 프로젝트로 가져올 수 있습니다. AR Quick Look을 사용해 앱이나 웹사이트에 USD 콘텐츠를 포함할 수도 있습니다. 또한 USD는 확장 가능한 형식이므로, 이를 사용하는 앱은 사용자 정의 기능 지원에 필요한 데이터를 저장하고 로드하기 위한 custom schema를 만들 수 있습니다. 예를 들어 anchoring 같은 AR 기능을 지원하도록 USD를 확장하기 위해 Apple이 Pixar와 함께 만든 제안인 [OpenUSD schemas for AR](https://developer.apple.com/documentation/usd/usd-schemas-for-ar)를 참고하십시오.

다른 interchange specification과 달리 USD는 임의의 수의 asset을 virtual set, scene, shot, world로 조합하는 것을 지원하며, 단일하고 일관된 API와 하나의 scenegraph 안에 저장되는 비파괴 편집을 허용합니다. 개별 3D model에 대해 별도의 USD 파일을 만드는 것이 일반적이지만, USD 파일은 다른 USD 파일을 참조할 수 있고 참조한 파일의 내용을 override할 수도 있으므로 완전히 비파괴적인 workflow를 구성할 수 있습니다.

:::note Note
Apple 플랫폼은 USD 지원을 내장하고 제공하지만, 새롭거나 아직 개발 중인 기능과 도구를 시험하려면 [source code](https://github.com/PixarAnimationStudios/OpenUSD)에서 USD를 직접 컴파일할 수도 있습니다.
:::

:::topic-grid
## 기초
- [OpenUSD schemas for AR](https://developer.apple.com/documentation/usd/usd-schemas-for-ar): USD schema를 사용해 3D 콘텐츠에 증강 현실 기능을 추가합니다.
- [Schema definitions for third-party DCCs](https://developer.apple.com/documentation/usd/schema-definitions-for-third-party-dccs): 로컬 USD library를 업데이트해 인터랙티브 및 증강 현실 기능을 추가합니다.
- [Creating USD files for Apple devices](https://developer.apple.com/documentation/usd/creating-usd-files-for-apple-devices): 기대한 대로 렌더링되는 3D asset을 생성합니다.
- [Validating feature support for USD files](https://developer.apple.com/documentation/usd/validating-usd-files): USD asset을 표시하는 renderer가 해당 기능을 지원하는지 확인합니다.
- [Placing a prim in the real world](https://developer.apple.com/documentation/usd/placing-a-prim-in-the-real-world): runtime이 물리 환경에서 인식하는 실제 객체에 prim을 anchor합니다.
- [Previewing a Model with AR Quick Look](https://developer.apple.com/documentation/ARKit/previewing-a-model-with-ar-quick-look): 사용자가 이동, 크기 조정, 공유할 수 있는 model 또는 scene을 표시합니다.
:::
