---
route: /documentation/AppleArchive
source_url: https://developer.apple.com/documentation/AppleArchive
source_locale: en-US
section: docc
content_type: symbol
title: Apple Archive
original_title: Apple Archive
source_hash: e47e31b8ae668de81d37bca8cc4a2d4c4977855602a0608e712b6b9c3dbb8eb3
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:31:23+00:00'
last_translated_at: '2026-03-13T23:34:00+09:00'
---

# Apple Archive

디렉터리, 파일, 데이터를 멀티스레드 무손실 압축으로 처리합니다.

## 개요

Apple Archive는 소유권, 권한, 플래그, 시간, 확장 속성, 오류 정정을 포함한 파일 속성과 함께 빠른 압축을 제공합니다. Apple Archive는 다음 기능을 제공합니다.

- 모든 코어를 활용하고 에너지 효율적이며 더 빠른 결과를 내는 멀티스레드 처리
- 파일과 그 속성을 전송할 수 있고, 사용 가능한 경우 파일 시스템 압축, full clone, sparse file 같은 Apple File System(APFS) 기능을 활용할 수 있는 능력
- 오류 정정, digest, manifest, 외부 데이터 저장 등에 아카이브를 사용할 수 있는 유연한 인코딩 형식
- 메모리 내 아카이브 처리, 스트리밍 접근, 임의 접근, 연속적인 아카이브 및 추출을 위한 API 지원

:::topic-grid
## Apple Archive 핵심 항목
- [Compressing single files](https://developer.apple.com/documentation/Accelerate/compressing-single-files): 단일 파일을 압축해 결과를 파일 시스템에 저장합니다.
- [Decompressing single files](https://developer.apple.com/documentation/Accelerate/decompressing-single-files): 압축 파일에서 단일 파일을 다시 생성합니다.
- [Compressing file system directories](https://developer.apple.com/documentation/Accelerate/compressing-file-system-directories): 전체 디렉터리의 내용을 압축해 결과를 파일 시스템에 저장합니다.
- [Decompressing and extracting an archived directory](https://developer.apple.com/documentation/Accelerate/decompressing-and-extracting-an-archived-directory): 아카이브 파일에서 전체 파일 시스템 디렉터리를 다시 생성합니다.
- [Compressing and saving a string to the file system](https://developer.apple.com/documentation/Accelerate/compressing-and-saving-a-string-to-the-file-system): Unicode 문자열의 내용을 압축해 결과를 파일 시스템에 저장합니다.
- [Decompressing and parsing an archived string](https://developer.apple.com/documentation/Accelerate/decompressing-and-parsing-an-archived-string): 아카이브 파일에서 문자열을 다시 생성합니다.
:::

:::topic-grid
## Apple Encrypted Archive 핵심 항목
- [Encrypting and Decrypting a String](https://developer.apple.com/documentation/applearchive/encrypting-and-decrypting-a-string): 문자열 내용을 암호화해 파일 시스템에 저장한 뒤, Apple Encrypted Archive를 사용해 아카이브 파일에서 이를 복호화하고 문자열을 다시 생성합니다.
- [Encrypting and Decrypting a Single File](https://developer.apple.com/documentation/applearchive/encrypting-and-decrypting-a-single-file): 단일 파일을 암호화해 파일 시스템에 저장한 뒤, Apple Encrypted Archive를 사용해 아카이브 파일에서 원본 파일을 복호화하고 다시 생성합니다.
- [Encrypting and Decrypting Directories](https://developer.apple.com/documentation/applearchive/encrypting-and-decrypting-directories): Apple Encrypted Archive를 사용해 전체 디렉터리의 내용을 압축 및 암호화하거나, 아카이브된 디렉터리를 압축 해제 및 복호화합니다.
- [ArchiveEncryptionContext](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext): 암호화와 복호화 스트림 모두를 위해 암호화된 아카이브를 여는 데 필요한 모든 매개변수, 키, 데이터를 캡슐화하는 객체입니다.
:::

:::topic-grid
## Apple Archive 헤더
- [ArchiveHeader](https://developer.apple.com/documentation/applearchive/archiveheader): AppleArchive 항목 헤더입니다.
:::

:::topic-grid
## Apple Archive 스트림
- [ArchiveStreamProtocol](https://developer.apple.com/documentation/applearchive/archivestreamprotocol): 데이터 blob에 읽기 및 쓰기를 수행하는 아카이브 스트림을 사용하는 인터페이스를 정의하는 메서드 집합입니다.
- [ArchiveStream](https://developer.apple.com/documentation/applearchive/archivestream): 데이터 blob에 읽기 및 쓰기를 수행하는 아카이브 스트림입니다.
- [ArchiveByteStreamProtocol](https://developer.apple.com/documentation/applearchive/archivebytestreamprotocol): 버퍼에 읽기 및 쓰기를 수행하는 아카이브 스트림을 사용하는 인터페이스를 정의하는 메서드 집합입니다.
- [ArchiveByteStream](https://developer.apple.com/documentation/applearchive/archivebytestream): 버퍼에 읽기 및 쓰기를 수행하는 아카이브 스트림입니다.
:::

:::topic-grid
## Apple Archive 오류
- [ArchiveError](https://developer.apple.com/documentation/applearchive/archiveerror): AppleArchive용 오류 코드입니다.
:::

:::topic-grid
## 상수
- [APPLE_ARCHIVE_API_VERSION](https://developer.apple.com/documentation/applearchive/apple_archive_api_version): 컴파일 시점의 프레임워크 버전입니다.
:::

:::topic-grid
## 참고 자료
- [Apple Archive structures](https://developer.apple.com/documentation/applearchive/apple-archive-structures)
:::
