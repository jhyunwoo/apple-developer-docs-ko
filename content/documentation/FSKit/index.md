---
route: /documentation/FSKit
source_url: https://developer.apple.com/documentation/FSKit
source_locale: en-US
section: docc
content_type: symbol
title: FSKit
original_title: FSKit
source_hash: baeaaa703a317a6f1df10fed94ed1b3d7c73a55032cba37abcfe97b4689a56af
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:12:35+00:00'
last_translated_at: '2026-03-14T00:45:00+09:00'
---

# FSKit

사용자 공간에서 실행되는 파일 시스템을 구현합니다.

## 개요

FSKit을 사용하면 새로운 유형의 파일 시스템에 대한 접근을 활성화하여 macOS를 확장할 수 있습니다. 이를 위해 사용자 공간에서 실행되고 Mac App Store 배포와 호환되는 app extension 형태의 FSKit module(`FSModule`)을 개발합니다. FSKit은 사용자의 module을 [Disk Arbitration](https://developer.apple.com/documentation/DiskArbitration), NetFS, `mount(8)` 명령 같은 시스템의 기존 프레임워크와 도구에 연결합니다.

### FSKit module

FSKit module은 두 가지 주요 부분으로 이루어집니다.

- Module의 `Info.plist` 파일에 정의하는 *module attributes* 집합입니다. 이러한 attribute는 기능 지원 여부를 나타내는 Boolean 키나, 명령줄 인터페이스 접근을 설명하는 dictionary 같은 메타데이터를 제공합니다.
- 파일 시스템 기능을 구현하는 코드입니다. 앱 extension은 아래에서 설명하는 설계 흐름에 따라 두 프로토콜 중 하나를 준수합니다.

FSKit 프레임워크는 `FSModule`이 지원하는 세 가지 핵심 파일 저장 개념을 정의합니다.

:::term-list
**Volume**: 파일과 폴더를 위한 디렉터리 구조입니다.
**Resource**: 블록 저장 장치나 URL로 식별하는 네트워크 리소스 같은 데이터 소스입니다.
**Container**: 하나 이상의 resource를 사용해 하나 이상의 volume을 제공하는 추상 객체로, APFS container와 유사합니다. 일반적으로 container는 하나의 resource만 사용하지만, Xsan(Apple의 클러스터 파일 시스템) 같은 일부 형식은 하나의 volume에 대한 콘텐츠를 저장하기 위해 여러 디스크를 사용합니다.
:::

### 설계 흐름

FSKit은 기능과 복잡성의 균형이 다른 두 가지 설계 흐름을 제공합니다.

- [FSFileSystem](https://developer.apple.com/documentation/fskit/fsfilesystem)은 여러 resource를 사용할 수 있고 여러 volume을 제공할 수 있는 전통적인 완전 기능 파일 시스템입니다.
- [FSUnaryFileSystem](https://developer.apple.com/documentation/fskit/fsunaryfilesystem)은 container가 하나의 resource만 사용하고 하나의 volume만 제공하는 더 단순한 파일 시스템입니다. macOS에 포함된 대부분의 파일 시스템(`HFS`, `msdosfs`, `ExFAT`, `ntfs` 등)이 이 패턴에 맞습니다.

:::note 참고
현재 FSKit 버전은 `FSUnaryFileSystem`만 지원합니다.
:::

설계 흐름을 선택했다면, 선택한 흐름에 따라 `FileSystemExtension` 또는 [UnaryFileSystemExtension](https://developer.apple.com/documentation/fskit/unaryfilesystemextension)을 준수하는 app extension을 작성합니다. 이 프로토콜들은 extension이 생성하여 반환하는 `fileSystem` delegate 객체를 선언합니다. 이 delegate 객체는 적절하게 `FSFileSystem` 또는 `FSUnaryFileSystem`을 subclass하고, `FSFileSystemOperations` 또는 [FSUnaryFileSystemOperations](https://developer.apple.com/documentation/fskit/fsunaryfilesystemoperations) 프로토콜을 준수합니다. 이 프로토콜들은 `loadResource` 메서드를 정의하며, FSKit은 이를 사용해 module이 resource를 사용할 수 있게 만듭니다.

:::topic-grid
## 핵심 사항
- [Building a passthrough file system](https://developer.apple.com/documentation/fskit/building-a-passthrough-file-system): FSKit 프레임워크를 사용해 기존 경로를 자체 파일 시스템으로 노출합니다.
:::

:::topic-grid
## App extensions
- [UnaryFileSystemExtension](https://developer.apple.com/documentation/fskit/unaryfilesystemextension): 최소한의 파일 시스템을 app extension으로 구현하기 위한 프로토콜입니다.
:::

:::topic-grid
## 파일 시스템
- [FSUnaryFileSystem](https://developer.apple.com/documentation/fskit/fsunaryfilesystem): 최소한의 파일 시스템을 구현하기 위한 추상 기반 클래스입니다.
- [FSFileSystemBase](https://developer.apple.com/documentation/fskit/fsfilesystembase): FSKit이 파일 시스템 구현에 제공하는 기능을 담는 프로토콜입니다.
- [FSFileName](https://developer.apple.com/documentation/fskit/fsfilename): 데이터 버퍼로 표현한 파일 이름입니다.
:::

:::topic-grid
## Container
- [FSContainerIdentifier](https://developer.apple.com/documentation/fskit/fscontaineridentifier): container를 식별하는 타입입니다.
- [FSContainerStatus](https://developer.apple.com/documentation/fskit/fscontainerstatus): container 상태를 나타내는 타입입니다.
:::

:::topic-grid
## Resource
- [FSResource](https://developer.apple.com/documentation/fskit/fsresource): 파일 시스템이 volume에 데이터를 제공할 때 사용하는 추상 resource입니다.
- [FSBlockDeviceResource](https://developer.apple.com/documentation/fskit/fsblockdeviceresource): 블록 저장 디스크 파티션을 나타내는 resource입니다.
- [FSPathURLResource](https://developer.apple.com/documentation/fskit/fspathurlresource): 시스템 파일 공간 안의 경로를 나타내는 resource입니다.
- [FSGenericURLResource](https://developer.apple.com/documentation/fskit/fsgenericurlresource): 추상 URL을 나타내는 resource입니다.
:::

:::topic-grid
## Volume
- [FSVolume](https://developer.apple.com/documentation/fskit/fsvolume): 파일과 폴더를 위한 디렉터리 구조입니다.
:::

:::topic-grid
## 항목
- [FSItem](https://developer.apple.com/documentation/fskit/fsitem): 파일, 디렉터리, symlink, socket 등 파일 계층 안의 개별 객체입니다.
:::

:::topic-grid
## 유지 보수 및 관리
- [FSManageableResourceMaintenanceOperations](https://developer.apple.com/documentation/fskit/fsmanageableresourcemaintenanceoperations): 파일 시스템 resource를 위한 유지 보수 작업입니다.
:::

:::topic-grid
## 연산
- [FSOperationID](https://developer.apple.com/documentation/fskit/fsoperationid): 연산의 고유 식별자입니다.
:::

:::topic-grid
## 작업
- [FSTask](https://developer.apple.com/documentation/fskit/fstask): 파일 시스템 module이 로그 메시지와 완료 알림을 client에 전달할 수 있게 하는 클래스입니다.
- [FSTaskOptions](https://developer.apple.com/documentation/fskit/fstaskoptions): 선택적으로 security-scoped URL을 제공하면서 명령 옵션을 task에 전달하는 클래스입니다.
:::

:::topic-grid
## 오류 및 로깅
- [fs_errorForCocoaError(_:)](https://developer.apple.com/documentation/fskit/fs_errorforcocoaerror(_:)): 지정한 Cocoa 오류 코드에 대한 오류 객체를 생성합니다.
- [fs_errorForMachError(_:)](https://developer.apple.com/documentation/fskit/fs_errorformacherror(_:)): 지정한 Mach 오류 코드에 대한 오류 객체를 생성합니다.
- [fs_errorForPOSIXError(_:)](https://developer.apple.com/documentation/fskit/fs_errorforposixerror(_:)): 지정한 POSIX 오류 코드에 대한 오류 객체를 생성합니다.
- [FSError](https://developer.apple.com/documentation/fskit/fserror): FSKit 연산을 수행하는 동안 발생한 오류입니다.
- [FSError.Code](https://developer.apple.com/documentation/fskit/fserror/code): 특정 FSKit 오류를 나타내는 코드입니다.
- [FSKitErrorDomain](https://developer.apple.com/documentation/fskit/fskiterrordomain): FSKit 오류를 위한 오류 도메인입니다.
:::

:::topic-grid
## FSKit 상호 작용
- [FSClient](https://developer.apple.com/documentation/fskit/fsclient): 앱과 데몬이 FSKit과 상호 작용하기 위한 인터페이스입니다.
:::

:::topic-grid
## 지원 타입
- [FSBlockmapFlags](https://developer.apple.com/documentation/fskit/fsblockmapflags): blockmap 연산의 동작을 설명하는 플래그입니다.
- [FSCompleteIOFlags](https://developer.apple.com/documentation/fskit/fscompleteioflags): I/O 완료 연산의 동작을 설명하는 플래그입니다.
- [FSEntityIdentifier](https://developer.apple.com/documentation/fskit/fsentityidentifier): container와 volume을 식별하는 기본 타입입니다.
- [FSExtentPacker](https://developer.apple.com/documentation/fskit/fsextentpacker): 이 파일 시스템이 관리하는 특정 파일에 대해 커널이 디스크 공간을 매핑하도록 지시하는 타입입니다.
- [FSExtentType](https://developer.apple.com/documentation/fskit/fsextenttype): extent 유형을 나타내는 열거형입니다.
- [FSMatchResult](https://developer.apple.com/documentation/fskit/fsmatchresult): 탐지된 resource의 인식 가능성과 사용 가능성을 나타내는 타입입니다.
- [FSMetadataRange](https://developer.apple.com/documentation/fskit/fsmetadatarange): 디스크 위의 연속된 메타데이터 세그먼트를 설명하는 범위입니다.
- [FSProbeResult](https://developer.apple.com/documentation/fskit/fsproberesult): 특정 probe의 결과를 나타내는 객체입니다.
:::
