---
route: /documentation/MLCompute
source_url: https://developer.apple.com/documentation/MLCompute
source_locale: en-US
section: docc
content_type: symbol
title: ML Compute
original_title: ML Compute
source_hash: e2cd0769750f2764c8e8f38680be201ed6381755dd1e10abfa753a70d1806fad
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:22:15+00:00'
last_translated_at: '2026-03-13T16:55:00+09:00'
---

# ML Compute

CPU와 하나 이상의 GPU 전반에서 신경망의 학습과 검증을 가속합니다.

## 개요

ML Compute는 CPU용으로 Accelerate 프레임워크의 고성능 [BNNS](https://developer.apple.com/documentation/Accelerate/BNNS) 프리미티브를 사용하고, GPU용으로 [Metal Performance Shaders](https://developer.apple.com/documentation/MetalPerformanceShaders)를 사용합니다.

:::topic-grid
## 구성 요소
- [MLCTensor](https://developer.apple.com/documentation/mlcompute/mlctensor): 프레임워크 전체에서 사용하는 데이터 객체입니다.
- [MLCPlatform](https://developer.apple.com/documentation/mlcompute/mlcplatform): 프레임워크의 전역 프로퍼티를 설정하는 유틸리티 클래스입니다.
- [Layers](https://developer.apple.com/documentation/mlcompute/layers): tensor를 입력받고 처리하고 출력하기 위한 연산과 구성 세부 사항을 캡슐화하는 layer를 생성하고 검사합니다.
- [Training and Validation](https://developer.apple.com/documentation/mlcompute/training-and-validation): 허용 가능한 예측 결과를 만들기 위해 graph를 생성하고 학습하고 검증합니다.
:::
