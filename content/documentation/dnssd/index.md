---
route: /documentation/dnssd
source_url: https://developer.apple.com/documentation/dnssd
source_locale: en-US
section: docc
content_type: symbol
title: dnssd
original_title: dnssd
source_hash: 88ec04fe4ca159a7f13ca65c36f89413e40862134028d5f2ec46ddf8ec5229f4
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:42:57+00:00'
last_translated_at: '2026-03-13T23:42:57+09:00'
---

# dnssd

로컬 네트워크 또는 광역 네트워크에서 네트워크 서비스를 검색하고, 게시하고, 해석합니다.

## 개요

DNS Service Discovery API는 다음 세 가지 주요 작업을 수행하는 데 도움을 줍니다.

- 서비스를 등록하기
- 서비스를 탐색하기
- 서비스 이름을 호스트 이름으로 해석하기

이러한 핵심 작업을 지원하기 위해, 이 API는 다음 두 가지 보조 작업도 직접 지원합니다.

- 도메인 열거하기(권장 서비스 도메인 찾기)
- 등록 정보 업데이트하기(DNS 등록 데이터를 동적으로 변경하기)

대부분의 앱은 이 API를 직접 사용하지 말고, 대신 [NetService](https://developer.apple.com/documentation/Foundation/NetService) 같은 더 높은 수준의 서비스 검색 API를 사용해야 합니다. `dnssd`는 BSD 스타일 애플리케이션을 작성하거나, 상위 프레임워크와 연결할 필요가 없는 크로스 플랫폼 프로그램을 작성할 때 사용하십시오. 이 API가 노출하는 특정 저수준 기능이 필요할 때도 사용할 수 있습니다.

:::important Important
로컬 네트워크를 사용하는 앱은 `Info.plist` 파일에 [NSLocalNetworkUsageDescription](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription) 키와 함께 사용 목적 문자열을 제공해야 합니다. [bonjour](https://developer.apple.com/documentation/Foundation/bonjour)를 사용하는 앱은 [NSBonjourServices](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) 키를 사용해 탐색할 서비스를 선언해야 합니다.
:::

:::topic-grid
## 참고 자료
- [DNS Service Discovery C](https://developer.apple.com/documentation/dnssd/dns-service-discovery-c): 위 개요 절의 header 수준 문서를 참고하십시오.
- [dnssd Enumerations](https://developer.apple.com/documentation/dnssd/dnssd-enumerations)
- [dnssd Functions](https://developer.apple.com/documentation/dnssd/dnssd-functions)
- [dnssd Data Types](https://developer.apple.com/documentation/dnssd/dnssd-data-types)
- [dnssd Constants](https://developer.apple.com/documentation/dnssd/dnssd-constants)
:::

:::topic-grid
## 변수
- [kDNSServiceAAAAPolicyFallback](https://developer.apple.com/documentation/dnssd/kdnsserviceaaaapolicyfallback)
- [kDNSServiceAAAAPolicyNone](https://developer.apple.com/documentation/dnssd/kdnsserviceaaaapolicynone)
- [kDNSServiceClass_IN](https://developer.apple.com/documentation/dnssd/kdnsserviceclass_in)
- [kDNSServiceErr_AlreadyRegistered](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_alreadyregistered)
- [kDNSServiceErr_BadFlags](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_badflags)
- [kDNSServiceErr_BadInterfaceIndex](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_badinterfaceindex)
- [kDNSServiceErr_BadKey](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_badkey)
- [kDNSServiceErr_BadParam](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_badparam)
- [kDNSServiceErr_BadReference](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_badreference)
- [kDNSServiceErr_BadSig](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_badsig)
- [kDNSServiceErr_BadState](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_badstate)
- [kDNSServiceErr_BadTime](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_badtime)
- [kDNSServiceErr_DefunctConnection](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_defunctconnection)
- [kDNSServiceErr_DoubleNAT](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_doublenat)
- [kDNSServiceErr_Firewall](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_firewall)
- [kDNSServiceErr_Incompatible](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_incompatible)
- [kDNSServiceErr_Invalid](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_invalid)
- [kDNSServiceErr_NATPortMappingDisabled](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_natportmappingdisabled)
- [kDNSServiceErr_NATPortMappingUnsupported](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_natportmappingunsupported)
- [kDNSServiceErr_NATTraversal](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_nattraversal)
- [kDNSServiceErr_NameConflict](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_nameconflict)
- [kDNSServiceErr_NoAuth](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_noauth)
- [kDNSServiceErr_NoError](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_noerror)
- [kDNSServiceErr_NoMemory](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_nomemory)
- [kDNSServiceErr_NoRouter](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_norouter)
- [kDNSServiceErr_NoSuchKey](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_nosuchkey)
- [kDNSServiceErr_NoSuchName](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_nosuchname)
- [kDNSServiceErr_NoSuchRecord](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_nosuchrecord)
- [kDNSServiceErr_NotInitialized](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_notinitialized)
- [kDNSServiceErr_NotPermitted](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_notpermitted)
- [kDNSServiceErr_PolicyDenied](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_policydenied)
- [kDNSServiceErr_PollingMode](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_pollingmode)
- [kDNSServiceErr_Refused](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_refused)
- [kDNSServiceErr_ServiceNotRunning](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_servicenotrunning)
- [kDNSServiceErr_StaleData](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_staledata)
- [kDNSServiceErr_Timeout](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_timeout)
- [kDNSServiceErr_Transient](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_transient)
- [kDNSServiceErr_Unknown](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_unknown)
- [kDNSServiceErr_Unsupported](https://developer.apple.com/documentation/dnssd/kdnsserviceerr_unsupported)
- [kDNSServiceFlagAnsweredFromCache](https://developer.apple.com/documentation/dnssd/kdnsserviceflagansweredfromcache)
- [kDNSServiceFlagsAdd](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsadd)
- [kDNSServiceFlagsAllowExpiredAnswers](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsallowexpiredanswers)
- [kDNSServiceFlagsAllowRemoteQuery](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsallowremotequery)
- [kDNSServiceFlagsAutoTrigger](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsautotrigger)
- [kDNSServiceFlagsBackgroundTrafficClass](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsbackgroundtrafficclass)
- [kDNSServiceFlagsBogus](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsbogus)
- [kDNSServiceFlagsBrowseDomains](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsbrowsedomains)
- [kDNSServiceFlagsDefault](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsdefault)
- [kDNSServiceFlagsEnableDNSSEC](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsenablednssec)
- [kDNSServiceFlagsExpiredAnswer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsexpiredanswer)
- [kDNSServiceFlagsForce](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsforce)
- [kDNSServiceFlagsForceMulticast](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsforcemulticast)
- [kDNSServiceFlagsIncludeAWDL](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsincludeawdl)
- [kDNSServiceFlagsIncludeP2P](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsincludep2p)
- [kDNSServiceFlagsIndeterminate](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsindeterminate)
- [kDNSServiceFlagsInsecure](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsinsecure)
- [kDNSServiceFlagsKnownUnique](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsknownunique)
- [kDNSServiceFlagsLongLivedQuery](https://developer.apple.com/documentation/dnssd/kdnsserviceflagslonglivedquery)
- [kDNSServiceFlagsMoreComing](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsmorecoming)
- [kDNSServiceFlagsNoAutoRename](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsnoautorename)
- [kDNSServiceFlagsPrivateFive](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsprivatefive)
- [kDNSServiceFlagsPrivateFour](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsprivatefour)
- [kDNSServiceFlagsPrivateOne](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsprivateone)
- [kDNSServiceFlagsPrivateThree](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsprivatethree)
- [kDNSServiceFlagsPrivateTwo](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsprivatetwo)
- [kDNSServiceFlagsQueueRequest](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsqueuerequest)
- [kDNSServiceFlagsRegistrationDomains](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsregistrationdomains)
- [kDNSServiceFlagsReturnIntermediates](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsreturnintermediates)
- [kDNSServiceFlagsSecure](https://developer.apple.com/documentation/dnssd/kdnsserviceflagssecure)
- [kDNSServiceFlagsShareConnection](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsshareconnection)
- [kDNSServiceFlagsShared](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsshared)
- [kDNSServiceFlagsSuppressUnusable](https://developer.apple.com/documentation/dnssd/kdnsserviceflagssuppressunusable)
- [kDNSServiceFlagsThresholdFinder](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsthresholdfinder)
- [kDNSServiceFlagsThresholdOne](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsthresholdone)
- [kDNSServiceFlagsThresholdReached](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsthresholdreached)
- [kDNSServiceFlagsTimeout](https://developer.apple.com/documentation/dnssd/kdnsserviceflagstimeout)
- [kDNSServiceFlagsUnicastResponse](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsunicastresponse)
- [kDNSServiceFlagsUnique](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsunique)
- [kDNSServiceFlagsValidate](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsvalidate)
- [kDNSServiceFlagsValidateOptional](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsvalidateoptional)
- [kDNSServiceFlagsWakeOnResolve](https://developer.apple.com/documentation/dnssd/kdnsserviceflagswakeonresolve)
- [kDNSServiceFlagsWakeOnlyService](https://developer.apple.com/documentation/dnssd/kdnsserviceflagswakeonlyservice)
- [kDNSServiceProtocol_IPv4](https://developer.apple.com/documentation/dnssd/kdnsserviceprotocol_ipv4)
- [kDNSServiceProtocol_IPv6](https://developer.apple.com/documentation/dnssd/kdnsserviceprotocol_ipv6)
- [kDNSServiceProtocol_TCP](https://developer.apple.com/documentation/dnssd/kdnsserviceprotocol_tcp)
- [kDNSServiceProtocol_UDP](https://developer.apple.com/documentation/dnssd/kdnsserviceprotocol_udp)
- [kDNSServiceType_A](https://developer.apple.com/documentation/dnssd/kdnsservicetype_a)
- [kDNSServiceType_A6](https://developer.apple.com/documentation/dnssd/kdnsservicetype_a6)
- [kDNSServiceType_AAAA](https://developer.apple.com/documentation/dnssd/kdnsservicetype_aaaa)
- [kDNSServiceType_AFSDB](https://developer.apple.com/documentation/dnssd/kdnsservicetype_afsdb)
- [kDNSServiceType_ANY](https://developer.apple.com/documentation/dnssd/kdnsservicetype_any)
- [kDNSServiceType_APL](https://developer.apple.com/documentation/dnssd/kdnsservicetype_apl)
- [kDNSServiceType_ATMA](https://developer.apple.com/documentation/dnssd/kdnsservicetype_atma)
- [kDNSServiceType_AXFR](https://developer.apple.com/documentation/dnssd/kdnsservicetype_axfr)
- [kDNSServiceType_CERT](https://developer.apple.com/documentation/dnssd/kdnsservicetype_cert)
- [kDNSServiceType_CNAME](https://developer.apple.com/documentation/dnssd/kdnsservicetype_cname)
- [kDNSServiceType_DHCID](https://developer.apple.com/documentation/dnssd/kdnsservicetype_dhcid)
- [kDNSServiceType_DNAME](https://developer.apple.com/documentation/dnssd/kdnsservicetype_dname)
- [kDNSServiceType_DNSKEY](https://developer.apple.com/documentation/dnssd/kdnsservicetype_dnskey)
- [kDNSServiceType_DS](https://developer.apple.com/documentation/dnssd/kdnsservicetype_ds)
- [kDNSServiceType_EID](https://developer.apple.com/documentation/dnssd/kdnsservicetype_eid)
- [kDNSServiceType_GID](https://developer.apple.com/documentation/dnssd/kdnsservicetype_gid)
- [kDNSServiceType_GPOS](https://developer.apple.com/documentation/dnssd/kdnsservicetype_gpos)
- [kDNSServiceType_HINFO](https://developer.apple.com/documentation/dnssd/kdnsservicetype_hinfo)
- [kDNSServiceType_HIP](https://developer.apple.com/documentation/dnssd/kdnsservicetype_hip)
- [kDNSServiceType_HTTPS](https://developer.apple.com/documentation/dnssd/kdnsservicetype_https)
- [kDNSServiceType_IPSECKEY](https://developer.apple.com/documentation/dnssd/kdnsservicetype_ipseckey)
- [kDNSServiceType_ISDN](https://developer.apple.com/documentation/dnssd/kdnsservicetype_isdn)
- [kDNSServiceType_IXFR](https://developer.apple.com/documentation/dnssd/kdnsservicetype_ixfr)
- [kDNSServiceType_KEY](https://developer.apple.com/documentation/dnssd/kdnsservicetype_key)
- [kDNSServiceType_KX](https://developer.apple.com/documentation/dnssd/kdnsservicetype_kx)
- [kDNSServiceType_LOC](https://developer.apple.com/documentation/dnssd/kdnsservicetype_loc)
- [kDNSServiceType_MAILA](https://developer.apple.com/documentation/dnssd/kdnsservicetype_maila)
- [kDNSServiceType_MAILB](https://developer.apple.com/documentation/dnssd/kdnsservicetype_mailb)
- [kDNSServiceType_MB](https://developer.apple.com/documentation/dnssd/kdnsservicetype_mb)
- [kDNSServiceType_MD](https://developer.apple.com/documentation/dnssd/kdnsservicetype_md)
- [kDNSServiceType_MF](https://developer.apple.com/documentation/dnssd/kdnsservicetype_mf)
- [kDNSServiceType_MG](https://developer.apple.com/documentation/dnssd/kdnsservicetype_mg)
- [kDNSServiceType_MINFO](https://developer.apple.com/documentation/dnssd/kdnsservicetype_minfo)
- [kDNSServiceType_MR](https://developer.apple.com/documentation/dnssd/kdnsservicetype_mr)
- [kDNSServiceType_MX](https://developer.apple.com/documentation/dnssd/kdnsservicetype_mx)
- [kDNSServiceType_NAPTR](https://developer.apple.com/documentation/dnssd/kdnsservicetype_naptr)
- [kDNSServiceType_NIMLOC](https://developer.apple.com/documentation/dnssd/kdnsservicetype_nimloc)
- [kDNSServiceType_NS](https://developer.apple.com/documentation/dnssd/kdnsservicetype_ns)
- [kDNSServiceType_NSAP](https://developer.apple.com/documentation/dnssd/kdnsservicetype_nsap)
- [kDNSServiceType_NSAP_PTR](https://developer.apple.com/documentation/dnssd/kdnsservicetype_nsap_ptr)
- [kDNSServiceType_NSEC](https://developer.apple.com/documentation/dnssd/kdnsservicetype_nsec)
- [kDNSServiceType_NSEC3](https://developer.apple.com/documentation/dnssd/kdnsservicetype_nsec3)
- [kDNSServiceType_NSEC3PARAM](https://developer.apple.com/documentation/dnssd/kdnsservicetype_nsec3param)
- [kDNSServiceType_NULL](https://developer.apple.com/documentation/dnssd/kdnsservicetype_null)
- [kDNSServiceType_NXT](https://developer.apple.com/documentation/dnssd/kdnsservicetype_nxt)
- [kDNSServiceType_OPT](https://developer.apple.com/documentation/dnssd/kdnsservicetype_opt)
- [kDNSServiceType_PTR](https://developer.apple.com/documentation/dnssd/kdnsservicetype_ptr)
- [kDNSServiceType_PX](https://developer.apple.com/documentation/dnssd/kdnsservicetype_px)
- [kDNSServiceType_RP](https://developer.apple.com/documentation/dnssd/kdnsservicetype_rp)
- [kDNSServiceType_RRSIG](https://developer.apple.com/documentation/dnssd/kdnsservicetype_rrsig)
- [kDNSServiceType_RT](https://developer.apple.com/documentation/dnssd/kdnsservicetype_rt)
- [kDNSServiceType_SIG](https://developer.apple.com/documentation/dnssd/kdnsservicetype_sig)
- [kDNSServiceType_SINK](https://developer.apple.com/documentation/dnssd/kdnsservicetype_sink)
- [kDNSServiceType_SOA](https://developer.apple.com/documentation/dnssd/kdnsservicetype_soa)
- [kDNSServiceType_SPF](https://developer.apple.com/documentation/dnssd/kdnsservicetype_spf)
- [kDNSServiceType_SRV](https://developer.apple.com/documentation/dnssd/kdnsservicetype_srv)
- [kDNSServiceType_SSHFP](https://developer.apple.com/documentation/dnssd/kdnsservicetype_sshfp)
- [kDNSServiceType_SVCB](https://developer.apple.com/documentation/dnssd/kdnsservicetype_svcb)
- [kDNSServiceType_TKEY](https://developer.apple.com/documentation/dnssd/kdnsservicetype_tkey)
- [kDNSServiceType_TSIG](https://developer.apple.com/documentation/dnssd/kdnsservicetype_tsig)
- [kDNSServiceType_TXT](https://developer.apple.com/documentation/dnssd/kdnsservicetype_txt)
- [kDNSServiceType_UID](https://developer.apple.com/documentation/dnssd/kdnsservicetype_uid)
- [kDNSServiceType_UINFO](https://developer.apple.com/documentation/dnssd/kdnsservicetype_uinfo)
- [kDNSServiceType_UNSPEC](https://developer.apple.com/documentation/dnssd/kdnsservicetype_unspec)
- [kDNSServiceType_WKS](https://developer.apple.com/documentation/dnssd/kdnsservicetype_wks)
- [kDNSServiceType_X25](https://developer.apple.com/documentation/dnssd/kdnsservicetype_x25)
:::
