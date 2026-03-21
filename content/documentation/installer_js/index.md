---
route: /documentation/installer_js
source_url: https://developer.apple.com/documentation/installer_js
source_locale: en-US
section: docc
content_type: symbol
title: Installer JS
original_title: Installer JS
source_hash: c81ae4d04aaeddb5967baa517694d687cef360f96aad8c3fe21fb3128f25b944
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:17:42+00:00'
last_translated_at: '2026-03-13T08:34:00+00:00'
---

# Installer JS

설치 및 배포 경험을 관리하고 사용자화합니다.

## 개요

배포 정의 파일은 제품의 설치 경험을 정의합니다. Installer 애플리케이션은 배포 정의 파일을 열고 해석하여, 사용자가 제품 설치를 실행하고 사용자화하기 위해 조작하는 사용자 인터페이스를 생성합니다.

배포 정의 파일에는 XML 코드와 JavaScript 코드가 포함됩니다. XML 코드는 배포의 구조를 정의하고, JavaScript 코드는 설치 옵션 같은 설치 시점 속성을 정의하고 관리합니다. [Distribution Definition XML Schema Reference](https://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/DistributionDefinitionRef/Chapters/Introduction.html#//apple_ref/doc/uid/TP40005370)는 배포 구조를 정의하는 데 사용하는 XML 스키마를 설명합니다.

이 문서는 배포 정의 파일의 JavaScript 코드가 사용자 입력과 시스템 속성을 관리하는 데 사용할 수 있는 객체 모델을 설명합니다.

:::topic-grid
## 클래스
- [Applications](https://developer.apple.com/documentation/installer_js/applications): 실행 중인 애플리케이션 정보를 얻기 위한 메서드를 제공하는 객체입니다.
- [Choice](https://developer.apple.com/documentation/installer_js/choice): 단일 설치 선택 항목입니다.
- [Files](https://developer.apple.com/documentation/installer_js/files): 파일에 접근하기 위한 메서드를 제공하는 객체입니다.
- [IORegistry](https://developer.apple.com/documentation/installer_js/ioregistry): IOKit 레지스트리에 접근할 수 있게 해 주는 객체입니다.
- [ProcessInformation](https://developer.apple.com/documentation/installer_js/processinformation): 애플리케이션을 설명하는 사전(연관 배열)입니다.
- [Result](https://developer.apple.com/documentation/installer_js/result): Installation Check 또는 Volume Check 스크립트의 결과 정보를 얻기 위한 메서드를 제공하는 객체입니다.
- [System](https://developer.apple.com/documentation/installer_js/system): 대상 호스트의 정보에 접근할 수 있게 해 주는 객체입니다.
- [Target](https://developer.apple.com/documentation/installer_js/target): 설치 볼륨 정보를 얻기 위한 메서드를 제공하는 객체입니다.
:::
