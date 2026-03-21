---
route: /documentation/iWorkDocumentExportingAPI
source_url: https://developer.apple.com/documentation/iWorkDocumentExportingAPI
source_locale: en-US
section: docc
content_type: symbol
title: iWork Document Exporting API
original_title: iWork Document Exporting API
source_hash: 51dafcf529e284ecd37546601fb44a439df0a012538cf3691064551fe0f200cf
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:07:38+00:00'
last_translated_at: '2026-03-14T03:28:00+09:00'
---

# iWork Document Exporting API

iWork 문서를 웹 API를 사용해 Portable Document Format(PDF) 파일로 변환합니다.

## 개요

iWork API를 사용하면 Numbers, Pages, Keynote 같은 앱의 iWork 문서를 Preview 앱이나 다른 PDF reader 애플리케이션으로 볼 수 있는 PDF 문서로 변환할 수 있습니다.

서비스가 iWork 문서를 PDF 형식으로 내보내면 앱은 PDF를 사용해 iWork 문서의 inline preview를 표시할 수 있습니다. 표준 도구를 사용해 PDF 문서에서 텍스트와 preview 이미지를 추출할 수 있습니다.

변환 서비스는 다음 조건을 충족하는 파일을 지원합니다.

- 최대 파일 크기 1GB
- 비밀번호로 보호되지 않은 문서

:::important Important
업로드 workflow의 일부로, 변환 목적으로 서비스가 iWork 문서를 Apple 서버에 일시적으로 저장한다는 점을 사용자에게 알려야 합니다. iWork preview 기능을 켜고 끌 수 있는 옵션을 제공하고, “When using iWork online previews, your files will be temporarily stored on Apple servers.” 같은 privacy notice를 표시하십시오.
:::

iWork document-exporting 서비스를 사용해 iWork 문서를 PDF 파일로 변환하려면, 서비스가 요구하는 key와 service identifier를 생성해 등록해야 합니다. 이 과정은 아래 설명한 순서대로 수행해야 하는 여러 단계로 이루어져 있습니다.

### 개발자 포털 로그인

Apple Developer ID를 사용해 [developer.apple.com](https://developer.apple.com)에 접근하여 개발자 포털에 로그인합니다. 로그인한 뒤 Certificates, IDs & Profiles 섹션의 Identifiers 항목을 클릭합니다.

창 오른쪽 위 계정 이름 아래에 있는 개발자 team ID를 적어 두십시오. 서비스 API 호출 시 이 값이 필요합니다.

### 새 identifier 생성

새 identifier를 만들려면 다음 단계를 수행합니다.

1. `+` 버튼을 클릭해 새 identifier를 만듭니다.
2. Register a new identifier 페이지에서 Services IDs를 클릭한 뒤 Continue를 클릭합니다.
3. 새 service ID에 대한 설명과 고유 identifier를 입력합니다. `com.example.myAppName` 같은 reverse domain 스타일 문자열을 사용하고 Continue를 클릭합니다.
4. Register를 클릭해 새 service ID를 저장합니다. 그러면 개발자 포털이 사용 가능한 identifier 목록을 표시합니다.
5. 방금 만든 identifier를 클릭합니다.
6. iWork Document Export를 활성화하고 Continue를 클릭한 다음 Save를 클릭합니다.

### 새 key 생성 및 다운로드

새 key를 만들려면 다음 단계를 수행합니다.

1. 사이드바에서 Keys를 클릭합니다.
2. 새 key에 대해 고유한 이름을 입력합니다.
3. key type 목록에서 iWork Document Exporting을 선택합니다.
4. Continue를 클릭해 새 key를 구성합니다.
5. 드롭다운 메뉴에서 앞서 만든 identifier의 이름을 선택합니다.
6. Save를 클릭해 service 이름을 key에 바인딩합니다.
7. Download를 클릭해 새 key를 저장합니다. 이 key는 다시 다운로드할 수 없으므로, 분실되거나 손상되면 revoke하고 새 key를 생성해야 합니다. key 사본은 안전한 장소에 보관하십시오.

:::topic-grid
## Endpoint
- [Export a PDF document from an iWork file](https://developer.apple.com/documentation/iworkdocumentexportingapi/create-an-export-job-(v2)): JSON Web Token(JWT) 인증을 사용해 iWork 문서의 PDF preview를 생성합니다.
:::
