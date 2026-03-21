---
route: /documentation/Spatial
source_url: https://developer.apple.com/documentation/Spatial
source_locale: en-US
section: docc
content_type: symbol
title: Spatial
original_title: Spatial
source_hash: e69dc423704ea0b67ad3c611d167ec0b623f5ad64c3cb6449f958cab0817d18b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:42:57+00:00'
last_translated_at: '2026-03-13T23:42:57+09:00'
---

# Spatial

3D 수학 기본 요소를 생성하고 조작합니다.

## 개요

Spatial 모듈은 3D 기본 요소를 다루기 위한 간단한 API를 제공하는 경량 3D 수학 라이브러리입니다. 많은 기능이 Core Graphics의 2D 기하 지원과 유사하지만, 이를 3차원으로 확장해 제공합니다.

:::topic-grid
## 데이터 구조
- [Vector3D](https://developer.apple.com/documentation/spatial/vector3d): 세 개의 요소를 가지는 벡터입니다.
- [Vector3DFloat](https://developer.apple.com/documentation/spatial/vector3dfloat): 세 개의 요소를 정의하는 단정밀도 벡터 구조체입니다.
- [Axis3D](https://developer.apple.com/documentation/spatial/axis3d): 축을 설명하는 상수입니다.
:::

:::topic-grid
## 2D 기본 요소
- [Angle2D](https://developer.apple.com/documentation/spatial/angle2d): 라디안 또는 도 단위로 값을 접근할 수 있는 기하학적 각도입니다.
- [Angle2DFloat](https://developer.apple.com/documentation/spatial/angle2dfloat): 라디안 또는 도 단위로 값을 접근할 수 있는 단정밀도 기하학적 각도입니다.
:::

:::topic-grid
## 3D 기본 요소
- [Point3D](https://developer.apple.com/documentation/spatial/point3d): 3D 좌표계의 점입니다.
- [Point3DFloat](https://developer.apple.com/documentation/spatial/point3dfloat): 3차원 좌표계의 점을 담는 단정밀도 구조체입니다.
- [Size3D](https://developer.apple.com/documentation/spatial/size3d): 3D 좌표계에서 너비, 높이, 깊이를 설명하는 크기입니다.
- [Size3DFloat](https://developer.apple.com/documentation/spatial/size3dfloat): 너비, 높이, 깊이 값을 담는 단정밀도 구조체입니다.
- [Rect3D](https://developer.apple.com/documentation/spatial/rect3d): 3D 좌표계의 직사각형입니다.
- [Rect3DFloat](https://developer.apple.com/documentation/spatial/rect3dfloat): 3D 직사각형의 위치와 크기를 담는 단정밀도 구조체입니다.
- [Rotation3D](https://developer.apple.com/documentation/spatial/rotation3d): 3차원 회전입니다.
- [Rotation3DFloat](https://developer.apple.com/documentation/spatial/rotation3dfloat): 3차원 회전을 나타내는 단정밀도 구조체입니다.
- [RotationAxis3D](https://developer.apple.com/documentation/spatial/rotationaxis3d): 3D 회전축입니다.
- [RotationAxis3DFloat](https://developer.apple.com/documentation/spatial/rotationaxis3dfloat): 3D 축을 나타내는 단정밀도 구조체입니다.
- [Pose3D](https://developer.apple.com/documentation/spatial/pose3d): 3D 위치와 3D 회전을 담는 구조체입니다.
- [Pose3DFloat](https://developer.apple.com/documentation/spatial/pose3dfloat): 위치와 회전을 담는 단정밀도 구조체입니다.
- [ScaledPose3D](https://developer.apple.com/documentation/spatial/scaledpose3d): 위치, 회전, 스케일을 함께 담는 구조체입니다.
- [ScaledPose3DFloat](https://developer.apple.com/documentation/spatial/scaledpose3dfloat): 위치, 회전, 스케일을 담는 단정밀도 구조체입니다.
- [SphericalCoordinates3D](https://developer.apple.com/documentation/spatial/sphericalcoordinates3d): 반지름, inclination, azimuthal 순서의 구면 좌표를 정의하는 구조체입니다.
- [SphericalCoordinates3DFloat](https://developer.apple.com/documentation/spatial/sphericalcoordinates3dfloat): 반지름, inclination, azimuthal 순서의 구면 좌표를 정의하는 단정밀도 구조체입니다.
- [Ray3D](https://developer.apple.com/documentation/spatial/ray3d): 3D 좌표계의 광선입니다.
- [Ray3DFloat](https://developer.apple.com/documentation/spatial/ray3dfloat): 3D 광선의 원점과 방향을 담는 단정밀도 구조체입니다.
:::

:::topic-grid
## Affine 및 projective 변환
- [AffineTransform3D](https://developer.apple.com/documentation/spatial/affinetransform3d): 3D affine 변환 행렬입니다.
- [AffineTransform3DFloat](https://developer.apple.com/documentation/spatial/affinetransform3dfloat)
- [ProjectiveTransform3D](https://developer.apple.com/documentation/spatial/projectivetransform3d): 3D projective 변환 행렬입니다.
- [ProjectiveTransform3DFloat](https://developer.apple.com/documentation/spatial/projectivetransform3dfloat): 단정밀도 3D projective 변환 행렬입니다.
:::

:::topic-grid
## 좌표 공간 간 변환
- [CoordinateSpace3D](https://developer.apple.com/documentation/spatial/coordinatespace3d): 다른 좌표 공간과 값 변환에 사용할 수 있는 좌표 공간을 나타내는 타입입니다.
- [CoordinateSpace3DFloat](https://developer.apple.com/documentation/spatial/coordinatespace3dfloat)
- [CoordinateSpaceValue3D](https://developer.apple.com/documentation/spatial/coordinatespacevalue3d): 구체적인 값으로 해석할 수 있는 불투명 값입니다.
- [ProjectiveTransformable3D](https://developer.apple.com/documentation/spatial/projectivetransformable3d)
- [ProjectiveTransformable3DFloat](https://developer.apple.com/documentation/spatial/projectivetransformable3dfloat)
- [WorldReferenceCoordinateSpace](https://developer.apple.com/documentation/spatial/worldreferencecoordinatespace): 세계 기준점을 나타내는 좌표 공간입니다.
:::

:::topic-grid
## 삼각 함수 적용
- [cos(_:)](https://developer.apple.com/documentation/spatial/cos(_:)-609v4)
- [cos(_:)](https://developer.apple.com/documentation/spatial/cos(_:)-79fxe)
- [cosh(_:)](https://developer.apple.com/documentation/spatial/cosh(_:)-6cg6v)
- [cosh(_:)](https://developer.apple.com/documentation/spatial/cosh(_:)-9mmhn)
- [sin(_:)](https://developer.apple.com/documentation/spatial/sin(_:)-46su7)
- [sin(_:)](https://developer.apple.com/documentation/spatial/sin(_:)-5tddt)
- [sinh(_:)](https://developer.apple.com/documentation/spatial/sinh(_:)-4m7ds)
- [sinh(_:)](https://developer.apple.com/documentation/spatial/sinh(_:)-8kigy)
- [tan(_:)](https://developer.apple.com/documentation/spatial/tan(_:)-1sjgu)
- [tan(_:)](https://developer.apple.com/documentation/spatial/tan(_:)-9x99s)
- [tanh(_:)](https://developer.apple.com/documentation/spatial/tanh(_:)-1f341)
- [tanh(_:)](https://developer.apple.com/documentation/spatial/tanh(_:)-5yozs)
:::

:::topic-grid
## 프로토콜
- [Primitive3D](https://developer.apple.com/documentation/spatial/primitive3d): Spatial 기본 요소 전반에 공통으로 쓰는 메서드 집합입니다.
- [Rotatable3D](https://developer.apple.com/documentation/spatial/rotatable3d): Spatial 엔터티를 회전시키기 위한 인터페이스를 정의하는 메서드 집합입니다.
- [Scalable3D](https://developer.apple.com/documentation/spatial/scalable3d): Spatial 엔터티를 스케일링하기 위한 인터페이스를 정의하는 메서드 집합입니다.
- [Shearable3D](https://developer.apple.com/documentation/spatial/shearable3d): Spatial 엔터티를 shear하기 위한 인터페이스를 정의하는 메서드 집합입니다.
- [Translatable3D](https://developer.apple.com/documentation/spatial/translatable3d): Spatial 엔터티를 이동시키기 위한 인터페이스를 정의하는 메서드 집합입니다.
- [Volumetric](https://developer.apple.com/documentation/spatial/volumetric): 부피를 가진 Spatial 기본 요소를 다루기 위한 메서드 집합입니다.
- [ClampableWithinRectProtocol](https://developer.apple.com/documentation/spatial/clampablewithinrectprotocol): volume 안으로 clamp할 수 있는 Spatial 엔터티용 인터페이스를 정의하는 메서드 집합입니다.
- [Primitive3DProtocol](https://developer.apple.com/documentation/spatial/primitive3dprotocol): Spatial 기본 요소에 공통적인 메서드 집합입니다.
- [Rotatable3DProtocol](https://developer.apple.com/documentation/spatial/rotatable3dprotocol): 회전 가능한 Spatial 엔터티를 위한 인터페이스를 정의하는 메서드 집합입니다.
- [Scalable3DProtocol](https://developer.apple.com/documentation/spatial/scalable3dprotocol): 스케일 가능한 Spatial 엔터티를 위한 인터페이스를 정의하는 메서드 집합입니다.
- [Shearable3DProtocol](https://developer.apple.com/documentation/spatial/shearable3dprotocol): shear 가능한 Spatial 엔터티를 위한 인터페이스를 정의하는 메서드 집합입니다.
- [SpatialTypeProtocol](https://developer.apple.com/documentation/spatial/spatialtypeprotocol)
- [Transform3DProtocol](https://developer.apple.com/documentation/spatial/transform3dprotocol): 변환 타입에 공통적인 메서드 집합입니다.
- [Translatable3DProtocol](https://developer.apple.com/documentation/spatial/translatable3dprotocol): 이동 가능한 Spatial 엔터티를 위한 인터페이스를 정의하는 메서드 집합입니다.
- [VolumetricProtocol](https://developer.apple.com/documentation/spatial/volumetricprotocol): 부피를 가진 Spatial 기본 요소를 다루기 위한 메서드 집합입니다.
:::

:::topic-grid
## 매크로
- [Macros & Global Variables](https://developer.apple.com/documentation/spatial/spatial-macros)
:::

:::topic-grid
## 구조체
- [EulerAnglesFloat](https://developer.apple.com/documentation/spatial/euleranglesfloat)
:::

:::topic-grid
## 열거형
- [AxisWithFactorsFloat](https://developer.apple.com/documentation/spatial/axiswithfactorsfloat): shear transform의 축입니다.
:::
