---
route: /documentation/EndpointSecurity
source_url: https://developer.apple.com/documentation/EndpointSecurity
source_locale: en-US
section: docc
content_type: symbol
title: Endpoint Security
original_title: Endpoint Security
source_hash: 51fa097750abcde35e069d30036b917718252ba5d60237a4f90bd57a5c16e799
canonical_source: manual-translation
last_crawled_at: '2026-03-13T09:48:38+00:00'
last_translated_at: '2026-03-13T21:12:00+09:00'
---

# Endpoint Security

사용자 보안을 강화하는 system extension을 개발합니다.

## 개요

Endpoint Security는 잠재적으로 악의적인 활동을 탐지하기 위해 시스템 이벤트를 모니터링하는 C API입니다. 클라이언트는 네이티브 호출을 지원하는 어떤 언어로도 작성할 수 있습니다. 클라이언트는 Endpoint Security에 등록해 대기 중인 이벤트를 승인하거나, 이미 발생한 이벤트에 대한 알림을 받을 수 있습니다. 이러한 이벤트에는 프로세스 실행, 파일 시스템 마운트, 프로세스 fork, signal 발생 등이 포함됩니다.

[System Extensions](https://developer.apple.com/documentation/SystemExtensions) 프레임워크를 사용해 extension을 사용자의 Mac에 설치하고 업그레이드하는 앱에 Endpoint Security 기반 system extension을 패키징하십시오.

:::topic-grid
## 이벤트 모니터링
- [Client](https://developer.apple.com/documentation/endpointsecurity/client): Endpoint Security 클라이언트 상태를 유지하고 이 타입과 관련된 함수를 제공하는 opaque 타입입니다.
- [Message](https://developer.apple.com/documentation/endpointsecurity/message): 모니터링 중인 동작이 발생했을 때 Endpoint Security가 클라이언트에 알리기 위해 사용하는 타입입니다.
- [Event Types](https://developer.apple.com/documentation/endpointsecurity/event-types): 서로 다른 종류의 Endpoint Security 이벤트에 특화된 세부 정보를 message가 전달할 때 사용하는 타입입니다.
:::

:::topic-grid
## entitlement
- [com.apple.developer.endpoint-security.client](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.endpoint-security.client): 잠재적으로 악의적인 활동을 모니터링하기 위해 필요한 entitlement입니다.
:::

:::topic-grid
## 참고 자료
- [EndpointSecurity Constants](https://developer.apple.com/documentation/endpointsecurity/endpointsecurity-constants)
- [EndpointSecurity Data Types](https://developer.apple.com/documentation/endpointsecurity/endpointsecurity-data-types)
- [EndpointSecurity Functions](https://developer.apple.com/documentation/endpointsecurity/endpointsecurity-functions)
- [EndpointSecurity Structures](https://developer.apple.com/documentation/endpointsecurity/endpointsecurity-structures)
- [EndpointSecurity Enumerations](https://developer.apple.com/documentation/endpointsecurity/endpointsecurity-enumerations)
:::

:::topic-grid
## 구조체
- [es_cs_validation_category_t](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_t): es_cs_validation_category
- [es_event_tcc_modify_t](https://developer.apple.com/documentation/endpointsecurity/es_event_tcc_modify_t)
- [es_tcc_authorization_reason_t](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_t): ess_tcc_authorization_reason_t
- [es_tcc_authorization_right_t](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_right_t): ess_tcc_authorization_right_t
- [es_tcc_event_type_t](https://developer.apple.com/documentation/endpointsecurity/es_tcc_event_type_t)
- [es_tcc_identity_type_t](https://developer.apple.com/documentation/endpointsecurity/es_tcc_identity_type_t): es_tcc_identity_type_t
:::

:::topic-grid
## 변수
- [ES_CS_VALIDATION_CATEGORY_APP_STORE](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_app_store)
- [ES_CS_VALIDATION_CATEGORY_DEVELOPER_ID](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_developer_id)
- [ES_CS_VALIDATION_CATEGORY_DEVELOPMENT](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_development)
- [ES_CS_VALIDATION_CATEGORY_ENTERPRISE](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_enterprise)
- [ES_CS_VALIDATION_CATEGORY_INVALID](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_invalid)
- [ES_CS_VALIDATION_CATEGORY_LOCAL_SIGNING](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_local_signing)
- [ES_CS_VALIDATION_CATEGORY_NONE](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_none)
- [ES_CS_VALIDATION_CATEGORY_OOPJIT](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_oopjit)
- [ES_CS_VALIDATION_CATEGORY_PLATFORM](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_platform)
- [ES_CS_VALIDATION_CATEGORY_ROSETTA](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_rosetta)
- [ES_CS_VALIDATION_CATEGORY_TESTFLIGHT](https://developer.apple.com/documentation/endpointsecurity/es_cs_validation_category_testflight)
- [ES_EVENT_TYPE_NOTIFY_TCC_MODIFY](https://developer.apple.com/documentation/endpointsecurity/es_event_type_notify_tcc_modify)
- [ES_EVENT_TYPE_RESERVED_0](https://developer.apple.com/documentation/endpointsecurity/es_event_type_reserved_0)
- [ES_EVENT_TYPE_RESERVED_1](https://developer.apple.com/documentation/endpointsecurity/es_event_type_reserved_1)
- [ES_EVENT_TYPE_RESERVED_2](https://developer.apple.com/documentation/endpointsecurity/es_event_type_reserved_2)
- [ES_EVENT_TYPE_RESERVED_3](https://developer.apple.com/documentation/endpointsecurity/es_event_type_reserved_3)
- [ES_EVENT_TYPE_RESERVED_4](https://developer.apple.com/documentation/endpointsecurity/es_event_type_reserved_4)
- [ES_EVENT_TYPE_RESERVED_5](https://developer.apple.com/documentation/endpointsecurity/es_event_type_reserved_5)
- [ES_EVENT_TYPE_RESERVED_6](https://developer.apple.com/documentation/endpointsecurity/es_event_type_reserved_6)
- [ES_TCC_AUTHORIZATION_REASON_APP_TYPE_POLICY](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_app_type_policy): 시스템 프로세스가 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_ENTITLED](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_entitled): 시스템 프로세스가 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_ERROR](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_error)
- [ES_TCC_AUTHORIZATION_REASON_MDM_POLICY](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_mdm_policy): 시스템 프로세스가 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_MISSING_USAGE_STRING](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_missing_usage_string): 시스템 프로세스가 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_NONE](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_none)
- [ES_TCC_AUTHORIZATION_REASON_PREFLIGHT_UNKNOWN](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_preflight_unknown): 시스템 프로세스가 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_PROMPT_CANCEL](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_prompt_cancel): 시스템 프로세스가 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_PROMPT_TIMEOUT](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_prompt_timeout): 시스템 프로세스가 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_SERVICE_OVERRIDE_POLICY](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_service_override_policy): 시스템 프로세스가 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_SERVICE_POLICY](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_service_policy): 시스템 프로세스가 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_SYSTEM_SET](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_system_set): 사용자가 환경설정에서 권한 부여 권리를 변경했습니다.
- [ES_TCC_AUTHORIZATION_REASON_USER_CONSENT](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_user_consent)
- [ES_TCC_AUTHORIZATION_REASON_USER_SET](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_reason_user_set): 사용자가 프롬프트에 응답했습니다.
- [ES_TCC_AUTHORIZATION_RIGHT_ADD_MODIFY_ADDED](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_right_add_modify_added)
- [ES_TCC_AUTHORIZATION_RIGHT_ALLOWED](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_right_allowed)
- [ES_TCC_AUTHORIZATION_RIGHT_DENIED](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_right_denied)
- [ES_TCC_AUTHORIZATION_RIGHT_LEARN_MORE](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_right_learn_more)
- [ES_TCC_AUTHORIZATION_RIGHT_LIMITED](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_right_limited)
- [ES_TCC_AUTHORIZATION_RIGHT_SESSION_PID](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_right_session_pid)
- [ES_TCC_AUTHORIZATION_RIGHT_UNKNOWN](https://developer.apple.com/documentation/endpointsecurity/es_tcc_authorization_right_unknown)
- [ES_TCC_EVENT_TYPE_CREATE](https://developer.apple.com/documentation/endpointsecurity/es_tcc_event_type_create)
- [ES_TCC_EVENT_TYPE_DELETE](https://developer.apple.com/documentation/endpointsecurity/es_tcc_event_type_delete)
- [ES_TCC_EVENT_TYPE_MODIFY](https://developer.apple.com/documentation/endpointsecurity/es_tcc_event_type_modify)
- [ES_TCC_EVENT_TYPE_UNKNOWN](https://developer.apple.com/documentation/endpointsecurity/es_tcc_event_type_unknown)
- [ES_TCC_IDENTITY_TYPE_BUNDLE_ID](https://developer.apple.com/documentation/endpointsecurity/es_tcc_identity_type_bundle_id)
- [ES_TCC_IDENTITY_TYPE_EXECUTABLE_PATH](https://developer.apple.com/documentation/endpointsecurity/es_tcc_identity_type_executable_path)
- [ES_TCC_IDENTITY_TYPE_FILE_PROVIDER_DOMAIN_ID](https://developer.apple.com/documentation/endpointsecurity/es_tcc_identity_type_file_provider_domain_id)
- [ES_TCC_IDENTITY_TYPE_POLICY_ID](https://developer.apple.com/documentation/endpointsecurity/es_tcc_identity_type_policy_id)
:::

:::topic-grid
## 타입 별칭
- [es_statfs_t](https://developer.apple.com/documentation/endpointsecurity/es_statfs_t): 이 typedef는 더 이상 사용되지 않지만 API 하위 호환성을 위해 남아 있습니다.
:::
