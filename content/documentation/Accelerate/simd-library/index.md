---
route: /documentation/Accelerate/simd-library
source_url: https://developer.apple.com/documentation/Accelerate/simd-library
source_locale: en-US
section: docc
content_type: article
title: simd
original_title: simd
source_hash: ec22a65b434c83713975e2e33f948546899bf5ac0c13dc36d8e0de8aa7b7ff2c
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:28:05+00:00'
last_translated_at: '2026-03-13T09:26:00+00:00'
---

# simd

작은 벡터와 행렬에 대한 계산을 수행합니다.

## 개요

simd는 작은 벡터와 행렬 계산을 위한 타입과 함수를 제공합니다. 타입에는 정수 및 부동소수점 벡터와 행렬이 포함되며, 함수는 기본 산술 연산, 요소별 수학 연산, 기하 및 선형대수 연산을 제공합니다.

simd는 최대 16개 요소(단정밀도 값 기준) 또는 8개 요소(배정밀도 값 기준)를 담는 벡터와, 최대 4 x 4 크기의 행렬을 지원합니다. [vForce](https://developer.apple.com/documentation/Accelerate/vforce-library) 같은 다른 프레임워크를 사용하면 더 큰 벡터도 다룰 수 있습니다.

:::topic-grid
## 불리언 스칼라 데이터 타입
- [simd_bool](https://developer.apple.com/documentation/simd/simd_bool): 불리언 스칼라 값입니다.
:::

:::topic-grid
## 부호 있는 정수 벡터
- [8비트 부호 있는 정수 벡터](https://developer.apple.com/documentation/accelerate/8-bit-signed-integer-vectors): 부호 있는 8비트 정수 요소를 담는 벡터에 대해 연산을 수행합니다.
- [16비트 부호 있는 정수 벡터](https://developer.apple.com/documentation/accelerate/16-bit-signed-integer-vectors): 부호 있는 16비트 정수 요소를 담는 벡터에 대해 연산을 수행합니다.
- [32비트 부호 있는 정수 벡터](https://developer.apple.com/documentation/accelerate/32-bit-signed-integer-vectors): 부호 있는 32비트 정수 요소를 담는 벡터에 대해 연산을 수행합니다.
- [64비트 부호 있는 정수 벡터](https://developer.apple.com/documentation/accelerate/64-bit-signed-integer-vectors): 부호 있는 64비트 정수 요소를 담는 벡터에 대해 연산을 수행합니다.
:::

:::topic-grid
## 부호 없는 정수 벡터
- [8비트 부호 없는 정수 벡터](https://developer.apple.com/documentation/accelerate/8-bit-unsigned-integer-vectors): 부호 없는 8비트 정수 요소를 담는 벡터에 대해 연산을 수행합니다.
- [16비트 부호 없는 정수 벡터](https://developer.apple.com/documentation/accelerate/16-bit-unsigned-integer-vectors): 부호 없는 16비트 정수 요소를 담는 벡터에 대해 연산을 수행합니다.
- [32비트 부호 없는 정수 벡터](https://developer.apple.com/documentation/accelerate/32-bit-unsigned-integer-vectors): 부호 없는 32비트 정수 요소를 담는 벡터에 대해 연산을 수행합니다.
- [64비트 부호 없는 정수 벡터](https://developer.apple.com/documentation/accelerate/64-bit-unsigned-integer-vectors): 부호 없는 64비트 정수 요소를 담는 벡터에 대해 연산을 수행합니다.
:::

:::topic-grid
## 부동소수점 벡터
- [벡터 다루기](https://developer.apple.com/documentation/accelerate/working-with-vectors): 벡터를 사용해 기하학적 값을 계산하고, 내적과 외적을 계산하며, 값 사이를 보간합니다.
- [반정밀도 부동소수점 벡터](https://developer.apple.com/documentation/accelerate/half-precision-floating-point-vectors): 반정밀도 부동소수점 요소를 담는 벡터에 대해 연산을 수행합니다.
- [단정밀도 부동소수점 벡터](https://developer.apple.com/documentation/accelerate/single-precision-floating-point-vectors): 단정밀도 부동소수점 요소를 담는 벡터에 대해 연산을 수행합니다.
- [배정밀도 부동소수점 벡터](https://developer.apple.com/documentation/accelerate/double-precision-floating-point-vectors): 배정밀도 부동소수점 요소를 담는 벡터에 대해 연산을 수행합니다.
:::

:::topic-grid
## 행렬
- [행렬 다루기](https://developer.apple.com/documentation/accelerate/working-with-matrices): 연립방정식을 풀고 공간에서 점을 변환합니다.
- [반정밀도 부동소수점 행렬](https://developer.apple.com/documentation/accelerate/half-precision-floating-point-matrices): 반정밀도 부동소수점 요소를 담는 행렬에 대해 연산을 수행합니다.
- [단정밀도 부동소수점 행렬](https://developer.apple.com/documentation/accelerate/single-precision-floating-point-matrices): 단정밀도 부동소수점 요소를 담는 행렬에 대해 연산을 수행합니다.
- [배정밀도 부동소수점 행렬](https://developer.apple.com/documentation/accelerate/double-precision-floating-point-matrices): 배정밀도 부동소수점 요소를 담는 행렬에 대해 연산을 수행합니다.
:::

:::topic-grid
## 쿼터니언
- [쿼터니언 다루기](https://developer.apple.com/documentation/accelerate/working-with-quaternions): 구 표면을 따라 점을 회전시키고 점들 사이를 보간합니다.
- [꼭짓점 변환으로 큐브 회전하기](https://developer.apple.com/documentation/accelerate/rotating-a-cube-by-transforming-its-vertices): 쿼터니언 보간을 사용해 일련의 키프레임을 거쳐 큐브를 회전시킵니다.
- [simd_quatf](https://developer.apple.com/documentation/simd/simd_quatf): 단정밀도 쿼터니언입니다.
- [simd_quatd](https://developer.apple.com/documentation/simd/simd_quatd): 배정밀도 쿼터니언입니다.
:::

:::topic-grid
## 상수
- [SIMD_COMPILER_HAS_REQUIRED_FEATURES](https://developer.apple.com/documentation/simd/simd_compiler_has_required_features)
- [SIMD_LIBRARY_VERSION](https://developer.apple.com/documentation/simd/simd_library_version)
:::

:::topic-grid
## 매크로
- [simd Macros](https://developer.apple.com/documentation/accelerate/simd-macros)
:::
