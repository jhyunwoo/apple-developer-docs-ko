---
route: /documentation/Accelerate
source_url: https://developer.apple.com/documentation/Accelerate
source_locale: en-US
section: docc
content_type: symbol
title: Accelerate
original_title: Accelerate
source_hash: 85f66727047d3140d81fe2ca456b90f05d4f4ba6c643cb683ce74c7d9ad94a92
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:16:23+00:00'
last_translated_at: '2026-03-13T08:35:00+00:00'
---

# Accelerate

대규모 수학 계산과 이미지 계산을 고성능, 저전력으로 최적화하여 수행합니다.

## 개요

Accelerate는 CPU의 벡터 처리 기능을 활용해 고성능이면서 에너지 효율적인 계산을 제공합니다. 다음 Accelerate 라이브러리는 이 기능을 추상화하므로, 이들을 대상으로 작성한 코드는 런타임에 사용 가능한 프로세서에 맞는 적절한 명령을 실행합니다.

:::term-list
[BNNS](https://developer.apple.com/documentation/accelerate/bnns-library): 학습과 추론 모두를 위한 신경망을 구성하고 실행하는 서브루틴입니다.
[vImage](https://developer.apple.com/documentation/accelerate/vimage-library): Core Graphics 및 Core Video 상호 운용, 포맷 변환, 이미지 조작을 포함하는 폭넓은 이미지 처리 함수 모음입니다.
[vDSP](https://developer.apple.com/documentation/accelerate/vdsp-library): 1D 및 2D 고속 푸리에 변환, 2차 필터링, 벡터 및 행렬 연산, 컨볼루션, 타입 변환을 포함하는 디지털 신호 처리 함수입니다.
[vForce](https://developer.apple.com/documentation/accelerate/vforce-library): 벡터에 대해 산술 함수와 초월 함수를 수행하는 함수입니다.
[Sparse Solvers](https://developer.apple.com/documentation/accelerate/sparse-solvers-library), [BLAS](https://developer.apple.com/documentation/accelerate/blas-library), and LAPACK: 희소 행렬과 밀집 행렬에 대해 선형대수를 수행하는 라이브러리입니다.
:::

Accelerate 프레임워크의 일부는 아니지만, 다음 라이브러리도 밀접하게 관련되어 있습니다.

:::term-list
[Apple Archive](https://developer.apple.com/documentation/AppleArchive): 디렉터리, 파일, 데이터를 멀티스레드 무손실 압축하는 프레임워크입니다.
[Compression](https://developer.apple.com/documentation/Compression): LZFSE, LZ4, LZMA, ZLIB 알고리즘을 지원하는 무손실 데이터 압축 알고리즘입니다.
[simd](https://developer.apple.com/documentation/accelerate/simd-library): 작은 벡터와 행렬에 대한 계산을 수행하는 모듈입니다.
[Spatial](https://developer.apple.com/documentation/Spatial): 3D 기본 요소를 다루기 위한 간단한 API를 제공하는 가벼운 3D 수학 라이브러리입니다.
:::

:::topic-grid
## 신경망
- [숫자를 인식하는 신경망 학습하기](https://developer.apple.com/documentation/accelerate/training-a-neural-network-to-recognize-digits): 단순한 신경망을 구축하고 무작위로 생성한 숫자를 인식하도록 학습시킵니다.
- [BNNS](https://developer.apple.com/documentation/accelerate/bnns-library): 학습과 추론을 위한 신경망을 구현하고 실행합니다.
:::

:::topic-grid
## 디렉터리, 파일 및 데이터 아카이브
- [단일 파일 압축하기](https://developer.apple.com/documentation/accelerate/compressing-single-files): 단일 파일을 압축하고 그 결과를 파일 시스템에 저장합니다.
- [단일 파일 압축 해제하기](https://developer.apple.com/documentation/accelerate/decompressing-single-files): 압축 파일로부터 단일 파일을 다시 생성합니다.
- [파일 시스템 디렉터리 압축하기](https://developer.apple.com/documentation/accelerate/compressing-file-system-directories): 전체 디렉터리의 내용을 압축하고 그 결과를 파일 시스템에 저장합니다.
- [보관된 디렉터리 압축 해제 및 추출하기](https://developer.apple.com/documentation/accelerate/decompressing-and-extracting-an-archived-directory): 아카이브 파일로부터 전체 파일 시스템 디렉터리를 다시 생성합니다.
- [문자열을 압축해 파일 시스템에 저장하기](https://developer.apple.com/documentation/accelerate/compressing-and-saving-a-string-to-the-file-system): Unicode 문자열의 내용을 압축하고 그 결과를 파일 시스템에 저장합니다.
- [보관된 문자열 압축 해제 및 파싱하기](https://developer.apple.com/documentation/accelerate/decompressing-and-parsing-an-archived-string): 아카이브 파일로부터 문자열을 다시 생성합니다.
:::

:::topic-grid
## 압축
- [스트림 압축으로 파일 압축 및 압축 해제하기](https://developer.apple.com/documentation/accelerate/compressing-and-decompressing-files-with-stream-compression): 모든 파일에 대해 압축을 수행하고, 지원되는 확장자 유형의 파일에 대해 압축 해제를 수행합니다.
- [버퍼 압축으로 데이터 압축 및 압축 해제하기](https://developer.apple.com/documentation/accelerate/compressing-and-decompressing-data-with-buffer-compression): 문자열을 압축하고 파일 시스템에 기록한 다음, 버퍼 압축을 사용해 같은 파일을 압축 해제합니다.
- [입력 및 출력 필터로 데이터 압축 및 압축 해제하기](https://developer.apple.com/documentation/accelerate/compressing-and-decompressing-data-with-input-and-output-filters): 입력 및 출력 필터를 사용해 스트림 데이터나 메모리 상의 데이터를 압축하고 압축 해제합니다.
:::

:::topic-grid
## 이미지 처리 필수 항목
- [Core Graphics 이미지와 vImage 버퍼 사이에서 비트맵 데이터 변환하기](https://developer.apple.com/documentation/accelerate/converting-bitmap-data-between-core-graphics-images-and-vimage-buffers): Core Graphics와 vImage 사이에서 이미지 데이터를 주고받아 이미지를 생성하고 조작합니다.
- [Core Graphics 이미지로부터 버퍼 생성 및 채우기](https://developer.apple.com/documentation/accelerate/creating-and-populating-buffers-from-core-graphics-images): Core Graphics 이미지로부터 vImage 버퍼를 초기화합니다.
- [vImage 버퍼로부터 Core Graphics 이미지 만들기](https://developer.apple.com/documentation/accelerate/creating-a-core-graphics-image-from-a-vimage-buffer): vImage 버퍼의 표시 가능한 표현을 생성합니다.
- [기본 이미지 처리 워크플로 구축하기](https://developer.apple.com/documentation/accelerate/building-a-basic-image-processing-workflow): vImage로 이미지를 리사이즈합니다.
- [이미지에 기하 변환 적용하기](https://developer.apple.com/documentation/accelerate/applying-geometric-transforms-to-images): vImage를 사용해 이미지 버퍼를 반사, 전단, 회전, 크기 조절합니다.
- [알파 블렌딩으로 이미지 합성하기](https://developer.apple.com/documentation/accelerate/compositing-images-with-alpha-blending): 알파 블렌딩을 사용해 두 이미지를 하나의 출력으로 결합합니다.
- [vImage 블렌드 모드로 이미지 합성하기](https://developer.apple.com/documentation/accelerate/compositing-images-with-vimage-blend-modes): 블렌드 모드를 사용해 두 이미지를 하나의 출력으로 결합합니다.
- [관심 영역에만 vImage 연산 적용하기](https://developer.apple.com/documentation/accelerate/applying-vimage-operations-to-regions-of-interest): vImage 연산의 효과를 직사각형 관심 영역으로 제한합니다.
- [이미지 처리 성능 최적화하기](https://developer.apple.com/documentation/accelerate/optimizing-image-processing-performance): 이미지 버퍼 포맷을 interleaved에서 planar로 변환해 앱 성능을 향상합니다.
- [vImage](https://developer.apple.com/documentation/accelerate/vimage-library): CPU의 벡터 프로세서를 사용해 대형 이미지를 조작합니다.
:::

:::topic-grid
## 신호 처리 필수 항목
- [stride로 vDSP 연산 제어하기](https://developer.apple.com/documentation/accelerate/controlling-vdsp-operations-with-stride): 일정 간격으로 벡터의 요소를 선택적으로 처리합니다.
- [선형 보간으로 새로운 데이터 포인트 구성하기](https://developer.apple.com/documentation/accelerate/using-linear-interpolation-to-construct-new-data-points): 선형 보간을 사용해 수치 데이터 배열의 빈틈을 채웁니다.
- [벡터 기반 산술에 vDSP 사용하기](https://developer.apple.com/documentation/accelerate/using-vdsp-for-vector-based-arithmetic): vDSP의 벡터-벡터 및 벡터-스칼라 연산으로 일반적인 수학 작업의 성능을 높입니다.
- [데시메이션으로 신호 리샘플링하기](https://developer.apple.com/documentation/accelerate/resampling-a-signal-with-decimation): 데시메이션 계수를 지정하고 사용자 정의 anti-aliasing 필터를 적용해 신호의 샘플링 비율을 낮춥니다.
- [vDSP](https://developer.apple.com/documentation/accelerate/vdsp-library): 큰 벡터에 대해 기본 산술 연산과 공통 디지털 신호 처리(DSP) 루틴을 수행합니다.
:::

:::topic-grid
## 푸리에 및 코사인 변환
- [푸리에 변환을 위한 데이터 패킹 이해하기](https://developer.apple.com/documentation/accelerate/understanding-data-packing-for-fourier-transforms): vDSP 푸리에 함수에 맞게 소스 데이터를 포맷하고 결과를 해석합니다.
- [합성 사인파의 구성 주파수 찾기](https://developer.apple.com/documentation/accelerate/finding-the-component-frequencies-in-a-composite-sine-wave): 1D 고속 푸리에 변환을 사용해 신호의 주파수 성분을 계산합니다.
- [interleaved-complex 데이터에 푸리에 변환 수행하기](https://developer.apple.com/documentation/accelerate/performing-fourier-transforms-on-interleaved-complex-data): vDSP interleaved DFT 루틴으로 이산 푸리에 변환(DFT) 성능을 최적화합니다.
- [윈도잉으로 스펙트럼 누설 줄이기](https://developer.apple.com/documentation/accelerate/reducing-spectral-leakage-with-windowing): 정수 주기가 아닌 신호를 변환할 때 윈도우 시퀀스 값을 신호 데이터에 곱합니다.
- [잡음에서 신호 추출하기](https://developer.apple.com/documentation/accelerate/signal-extraction-from-noise): Accelerate의 이산 코사인 변환을 사용해 신호에서 잡음을 제거합니다.
- [여러 신호에 푸리에 변환 수행하기](https://developer.apple.com/documentation/accelerate/performing-fourier-transforms-on-multiple-signals): Accelerate의 다중 신호 고속 푸리에 변환(FFT) 함수로 한 번의 함수 호출로 여러 신호를 변환합니다.
- [2D 고속 푸리에 변환을 사용한 하프톤 디스크리닝](https://developer.apple.com/documentation/accelerate/halftone-descreening-with-2d-fast-fourier-transform): 이미지에서 주기적 아티팩트를 줄이거나 제거합니다.
- [고속 푸리에 변환](https://developer.apple.com/documentation/accelerate/fast-fourier-transforms): 시간 및 공간 영역의 복소수 값을 담은 벡터와 행렬을 주파수 영역으로 변환하고, 그 반대 변환도 수행합니다.
- [이산 푸리에 변환](https://developer.apple.com/documentation/accelerate/discrete-fourier-transforms): 시간 및 공간 영역의 복소수 값을 담은 벡터를 주파수 영역으로 변환하고, 그 반대 변환도 수행합니다.
- [이산 코사인 변환](https://developer.apple.com/documentation/accelerate/discrete-cosine-transforms): 시간 및 공간 영역의 실수 값을 담은 벡터를 주파수 영역으로 변환하고, 그 반대 변환도 수행합니다.
:::

:::topic-grid
## Core Video 상호 운용
- [vImage 픽셀 버퍼로 비디오 효과 생성하기](https://developer.apple.com/documentation/accelerate/using-vimage-pixel-buffers-to-generate-video-effects): vImage Pixel Buffer로 실시간 비디오 효과를 렌더링합니다.
- [Core Image 워크플로에 vImage 픽셀 버퍼 통합하기](https://developer.apple.com/documentation/accelerate/integrating-vimage-pixel-buffers-into-a-core-image-workflow): Core Video 픽셀 버퍼와 vImage 버퍼 사이에서 이미지 데이터를 공유해 vImage 연산을 Core Image 워크플로에 통합합니다.
- [비디오 샘플 버퍼에 vImage 연산 적용하기](https://developer.apple.com/documentation/accelerate/applying-vimage-operations-to-video-sample-buffers): vImage의 convert-any-to-any 기능을 사용해 기기 카메라에서 스트리밍되는 비디오 프레임에 실시간 이미지 처리를 수행합니다.
- [디더링으로 양자화 이미지 품질 향상하기](https://developer.apple.com/documentation/accelerate/improving-the-quality-of-quantized-images-with-dithering): 낮은 비트 깊이에서 사용할 수 없는 색을 시뮬레이션하기 위해 디더링을 적용합니다.
- [Core Video 상호 운용성](https://developer.apple.com/documentation/accelerate/core-video-interoperability): Core Video와 vImage 사이에서 이미지 데이터를 주고받습니다.
:::

:::topic-grid
## 벡터, 행렬 및 쿼터니언
- [벡터 다루기](https://developer.apple.com/documentation/accelerate/working-with-vectors): 벡터를 사용해 기하학적 값을 계산하고, 내적과 외적을 계산하며, 값 사이를 보간합니다.
- [행렬 다루기](https://developer.apple.com/documentation/accelerate/working-with-matrices): 연립방정식을 풀고 공간에서 점을 변환합니다.
- [쿼터니언 다루기](https://developer.apple.com/documentation/accelerate/working-with-quaternions): 구의 표면을 따라 점을 회전시키고 점들 사이를 보간합니다.
- [꼭짓점 변환으로 큐브 회전하기](https://developer.apple.com/documentation/accelerate/rotating-a-cube-by-transforming-its-vertices): 쿼터니언 보간을 사용해 일련의 키프레임을 거쳐 큐브를 회전시킵니다.
- [simd](https://developer.apple.com/documentation/accelerate/simd-library): 작은 벡터와 행렬에 대한 계산을 수행합니다.
- [vForce](https://developer.apple.com/documentation/accelerate/vforce-library): 길이에 상관없이 벡터에 대해 초월 함수와 삼각 함수를 수행합니다.
:::

:::topic-grid
## 오디오 처리
- [오디오 스펙트로그램으로 소리 시각화하기](https://developer.apple.com/documentation/accelerate/visualizing-sound-as-an-audio-spectrogram): vDSP와 vImage 사이에서 이미지 데이터를 공유해 기기 마이크가 캡처한 오디오를 시각화합니다.
- [음악 루프에 2차 필터 적용하기](https://developer.apple.com/documentation/accelerate/applying-biquadratic-filters-to-a-music-loop): 계단식 2차 필터를 사용해 오디오 신호의 주파수 응답을 변경합니다.
- [이산 코사인 변환(DCT)으로 오디오 이퀄라이징하기](https://developer.apple.com/documentation/accelerate/equalizing-audio-with-discrete-cosine-transforms-dcts): 주파수 영역 데이터를 조작해 오디오 신호의 주파수 응답을 변경합니다.
- [2차 IIR 필터](https://developer.apple.com/documentation/accelerate/biquadratic-iir-filters): 단일 채널 및 다중 채널 데이터에 2차 필터를 적용합니다.
- [이산 코사인 변환](https://developer.apple.com/documentation/accelerate/discrete-cosine-transforms): 시간 및 공간 영역의 실수 값을 담은 벡터를 주파수 영역으로 변환하고, 그 반대 변환도 수행합니다.
:::

:::topic-grid
## 이미지 포맷 간 변환
- [기본 이미지 변환 워크플로 구축하기](https://developer.apple.com/documentation/accelerate/building-a-basic-image-conversion-workflow): CMYK 이미지를 RGB 이미지로 변환하며 convert-any-to-any 함수의 기본 개념을 익힙니다.
- [컬러 이미지를 그레이스케일로 변환하기](https://developer.apple.com/documentation/accelerate/converting-color-images-to-grayscale): 행렬 곱셈을 사용해 RGB 이미지를 그레이스케일로 변환합니다.
- [다차원 조회 테이블로 이미지에 색상 변환 적용하기](https://developer.apple.com/documentation/accelerate/applying-color-transforms-to-images-with-a-multidimensional-lookup-table): 색 공간 변환과 기타 점별 연산을 최적화하기 위해 변환 값을 미리 계산합니다.
- [기본 이미지 변환 워크플로 구축하기](https://developer.apple.com/documentation/accelerate/building-a-basic-image-conversion-workflow): CMYK 이미지를 RGB 이미지로 변환하며 convert-any-to-any 함수의 기본 개념을 익힙니다.
- [휘도 및 색차 평면을 ARGB 이미지로 변환하기](https://developer.apple.com/documentation/accelerate/converting-luminance-and-chrominance-planes-to-an-argb-image): 기기 카메라의 휘도와 색차 정보를 사용해 표시 가능한 ARGB 이미지를 생성합니다.
- [Conversion](https://developer.apple.com/documentation/accelerate/conversion): 이미지를 다른 포맷으로 변환합니다.
:::

:::topic-grid
## 이미지 리샘플링
- [vImage에서 리샘플링](https://developer.apple.com/documentation/accelerate/resampling-in-vimage): 기하 연산 동안 vImage가 이미지 데이터를 리샘플링하는 방식을 알아봅니다.
- [사용자 정의 리샘플링 필터로 아티팩트 줄이기](https://developer.apple.com/documentation/accelerate/reducing-artifacts-with-custom-resampling-filters): 기본 Lanczos 알고리즘으로 이미지를 스케일링할 때 발생하는 링잉 효과를 막기 위해 사용자 정의 선형 보간을 구현합니다.
- [이미지 전단](https://developer.apple.com/documentation/accelerate/image-shearing): 이미지를 가로 및 세로 방향으로 전단합니다.
:::

:::topic-grid
## 컨볼루션과 형태학
- [이미지 블러 처리하기](https://developer.apple.com/documentation/accelerate/blurring-an-image): 사용자 정의 및 고속 커널로 컨볼루션을 수행해 이미지를 필터링합니다.
- [이미지에 보케 효과 추가하기](https://developer.apple.com/documentation/accelerate/adding-a-bokeh-effect-to-images): 팽창 연산을 적용해 보케 효과를 시뮬레이션합니다.
- [Convolution](https://developer.apple.com/documentation/accelerate/convolution): 이미지에 컨볼루션 커널을 적용합니다.
- [Morphology](https://developer.apple.com/documentation/accelerate/morphology): 이미지를 팽창 및 침식합니다.
:::

:::topic-grid
## 색상 및 톤 조정
- [이미지의 밝기와 대비 조정하기](https://developer.apple.com/documentation/accelerate/adjusting-the-brightness-and-contrast-of-an-image): 감마 함수를 사용해 선형 또는 지수 곡선을 적용합니다.
- [채도 조정 및 톤 매핑 적용하기](https://developer.apple.com/documentation/accelerate/adjusting-saturation-and-applying-tone-mapping): RGB 이미지를 개별 휘도 및 색차 채널로 변환하고 색상 및 대비 처리를 적용합니다.
- [이미지에 톤 곡선 조정 적용하기](https://developer.apple.com/documentation/accelerate/applying-tone-curve-adjustments-to-images): vImage 라이브러리의 다항식 변환을 사용해 이미지에 톤 곡선 조정을 적용합니다.
- [이미지의 색조 조정하기](https://developer.apple.com/documentation/accelerate/adjusting-the-hue-of-an-image): 이미지를 L*a*b* 색 공간으로 변환하고 색조 조정을 적용합니다.
- [vImage로 히스토그램 지정하기](https://developer.apple.com/documentation/accelerate/specifying-histograms-with-vimage): 한 이미지의 히스토그램을 계산하고 이를 두 번째 이미지에 적용합니다.
- [히스토그램 조작으로 이미지 대비 향상하기](https://developer.apple.com/documentation/accelerate/enhancing-image-contrast-with-histogram-manipulation): 히스토그램 균등화와 대비 확장을 사용해 이미지의 대비를 향상하고 조정합니다.
- [Histogram](https://developer.apple.com/documentation/accelerate/histogram): 이미지의 히스토그램을 계산하거나 조작합니다.
:::

:::topic-grid
## vImage / vDSP 상호 운용성
- [캡처한 이미지 시퀀스에서 가장 선명한 이미지 찾기](https://developer.apple.com/documentation/accelerate/finding-the-sharpest-image-in-a-sequence-of-captured-images): vDSP와 vImage 사이에서 이미지 데이터를 공유해 브래킷 촬영된 사진 시퀀스 중 가장 선명한 이미지를 계산합니다.
- [오디오 스펙트로그램으로 소리 시각화하기](https://developer.apple.com/documentation/accelerate/visualizing-sound-as-an-audio-spectrogram): vDSP와 vImage 사이에서 이미지 데이터를 공유해 기기 마이크가 캡처한 오디오를 시각화합니다.
:::

:::topic-grid
## 희소 행렬
- [희소 행렬 생성하기](https://developer.apple.com/documentation/accelerate/creating-sparse-matrices): 분해와 시스템 해를 위해 희소 행렬을 생성합니다.
- [직접 해법으로 시스템 풀기](https://developer.apple.com/documentation/accelerate/solving-systems-using-direct-methods): 계수 행렬이 희소한 연립방정식을 직접 해법으로 풉니다.
- [반복 해법으로 시스템 풀기](https://developer.apple.com/documentation/accelerate/solving-systems-using-iterative-methods): 계수 행렬이 희소한 연립방정식을 반복 해법으로 풉니다.
- [좌표 포맷 배열로부터 희소 행렬 생성하기](https://developer.apple.com/documentation/accelerate/creating-a-sparse-matrix-from-coordinate-format-arrays): 분리된 좌표 포맷 배열을 사용해 희소 행렬을 생성합니다.
- [Sparse Solvers](https://developer.apple.com/documentation/accelerate/sparse-solvers-library): 계수 행렬이 희소한 연립방정식을 풉니다.
:::

:::topic-grid
## 산술 및 초월 함수
- [vecLib](https://developer.apple.com/documentation/accelerate/veclib): 큰 벡터에 대한 계산을 수행합니다.
:::

:::topic-grid
## 선형대수
- [LAPACK으로 선형 연립방정식 풀기](https://developer.apple.com/documentation/accelerate/solving-systems-of-linear-equations-with-lapack): 선형 연립방정식을 풀기 위한 최적의 LAPACK 루틴을 선택합니다.
- [Vandermonde 방법으로 보간 다항식 찾기](https://developer.apple.com/documentation/accelerate/finding-an-interpolating-polynomial-using-the-vandermonde-method): LAPACK을 사용해 선형 시스템을 풀고, 알려진 데이터 포인트들 사이에 새 점을 구성할 보간 다항식을 찾습니다.
- [선형대수로 이미지 압축하기](https://developer.apple.com/documentation/accelerate/compressing-an-image-using-linear-algebra): 특이값 분해(SVD)를 사용해 이미지의 저장 크기를 줄입니다.
- [BLAS](https://developer.apple.com/documentation/accelerate/blas-library): Apple의 Basic Linear Algebra Subprograms(BLAS) 구현으로 공통 선형대수 연산을 수행합니다.
:::

:::topic-grid
## 정적분
- [Quadrature](https://developer.apple.com/documentation/accelerate/quadrature): 유한 또는 무한 구간에서 함수의 정적분을 근사합니다.
:::

:::topic-grid
## 매크로
- [Macros](https://developer.apple.com/documentation/accelerate/macros)
:::
