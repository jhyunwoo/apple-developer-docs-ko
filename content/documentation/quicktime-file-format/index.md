---
route: /documentation/quicktime-file-format
source_url: https://developer.apple.com/documentation/quicktime-file-format
source_locale: en-US
section: docc
content_type: symbol
title: QuickTime File Format
original_title: QuickTime File Format
source_hash: 1b5a1e47b1f07c8c128ae45682aa5f2c60cdbcb3aad471bbfc60588c0773dd9a
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:23:49+00:00'
last_translated_at: '2026-03-13T23:24:01+09:00'
---

# QuickTime File Format

기기, 애플리케이션, 운영체제 사이에서 디지털 미디어를 저장하고 교환하기 위한 객체 지향 파일 포맷입니다.

## 개요

QuickTime File Format(QTFF)은 여러 종류의 디지털 멀티미디어 데이터를 저장하고 접근하는 일을 수용합니다. QTFF는 거의 모든 미디어 구조를 설명하는 데 사용할 수 있기 때문에, 기기, 애플리케이션, 운영체제 사이에서 디지털 미디어를 교환하기에 이상적인 포맷입니다.

이 파일 포맷은 객체 지향 방식이며, 쉽게 파싱할 수 있는 유연한 객체 모음으로 이루어져 있습니다. 포맷 설계상 파서는 알 수 없는 객체를 건너뛰거나 무시할 수 있으므로 확장이 쉽고, 새로운 객체 타입에 대해서도 상당한 수준의 순방향 호환성을 제공합니다.

QuickTime은 실제 파일 포맷을 이해하지 않아도 QuickTime 파일을 만들고 조작할 수 있는 여러 고수준 함수를 제공합니다. 이 함수는 개발자가 저수준 동작 세부 사항에 직접 노출되지 않도록 해 줍니다. 이 문서는 기본 유형을 넘어서는 QuickTime 파일을 만들 때 사용하십시오.

:::important Important
QuickTime File Format은 국제표준화기구(ISO)가 개발한 MPEG-4 표준과 JPEG-2000 표준의 기반입니다. 이들 파일 유형은 구조가 비슷하고 기능적으로 동일한 요소를 많이 포함하지만, 서로 구별되는 파일 유형입니다.
:::

QuickTime 파일은 QuickTime 영화뿐 아니라 다른 데이터도 저장하는 데 사용됩니다. QuickTime 파일을 파싱하는 앱을 작성하는 경우, 파일 안에 영화가 아닌 데이터가 들어 있을 수 있다는 점을 인식해야 합니다.

:::topic-grid
## 핵심
- [Storing and sharing media with QuickTime files](https://developer.apple.com/documentation/quicktime-file-format/storing_and_sharing_media_with_quicktime_files): atom, QT atom, atom container를 사용해 QuickTime 파일을 구성합니다.
:::

:::topic-grid
## 영화
- [Movie atoms](https://developer.apple.com/documentation/quicktime-file-format/movie_atoms): 영화 데이터 정보를 설명하는 container 역할을 하는 atom입니다.
- [Track atoms](https://developer.apple.com/documentation/quicktime-file-format/track_atoms): 영화의 단일 track을 정의하는 atom입니다.
- [Media atoms](https://developer.apple.com/documentation/quicktime-file-format/media_atoms): track의 미디어 타입과 sample 데이터를 설명하고 정의하는 atom입니다.
- [Sample atoms](https://developer.apple.com/documentation/quicktime-file-format/sample_atoms): 시간 순서가 있는 데이터 시퀀스의 단일 요소인 sample을 설명하는 atom입니다.
- [Structuring movie data and features](https://developer.apple.com/documentation/quicktime-file-format/structuring_movie_data_and_features): 압축 데이터나 참조 데이터로 영화를 구성하고, 효과 설명이나 대체 자막 track 같은 기능을 추가합니다.
:::

:::topic-grid
## 메타데이터
- [Metadata atoms and types](https://developer.apple.com/documentation/quicktime-file-format/metadata_atoms_and_types): QuickTime Movie 파일에 메타데이터를 저장합니다.
:::

:::topic-grid
## 미디어 데이터
- [Media data atom types](https://developer.apple.com/documentation/quicktime-file-format/media_data_atom_types): 비디오, 사운드, 자막 등 다양한 유형의 미디어 데이터를 저장합니다.
:::

:::topic-grid
## 데이터 타입
- [Basic QuickTime data types](https://developer.apple.com/documentation/quicktime-file-format/basic_data_types): 공통 데이터 타입으로 QuickTime 파일 안의 값을 표현합니다.
:::

:::topic-grid
## 변경 로그
- [QuickTime File Format change log](https://developer.apple.com/documentation/quicktime-file-format/revision_history): QuickTime File Format의 변경 사항입니다.
:::

:::topic-grid
## 지원 중단
- [Deprecated atoms](https://developer.apple.com/documentation/quicktime-file-format/deprecated_atoms): 더 이상 지원하지 않는 atom을 검토합니다.
:::
