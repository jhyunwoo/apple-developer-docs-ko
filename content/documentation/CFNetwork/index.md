---
route: /documentation/CFNetwork
source_url: https://developer.apple.com/documentation/CFNetwork
source_locale: en-US
section: docc
content_type: symbol
title: CFNetwork
original_title: CFNetwork
source_hash: 4c8244b6ab86885c10b59b26d0e9686d27b7ea335f4c128486f3f630e8f8016a
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:14:18+00:00'
last_translated_at: '2026-03-13T23:14:51+09:00'
---

# CFNetwork

네트워크 서비스에 접근하고 네트워크 구성 변경을 처리합니다. 네트워크 프로토콜의 추상화를 기반으로 BSD 소켓 작업, HTTP 및 FTP 서버 관리, Bonjour 서비스 관리 같은 작업을 단순화합니다.

## 개요

CFNetwork는 Core Foundation 기반의 저수준 네트워킹 프레임워크입니다. 호스트 조회, 프록시 설정, HTTP 인증과 메시지 처리, FTP 리소스, 네트워크 진단, Bonjour 계열 네트워크 서비스, 스트림 기반 전송 같은 기능을 폭넓게 제공합니다. 이 문서는 이러한 기능을 이루는 C 기반 API와 상수, 스트림 속성 키를 한곳에 모아 둔 참조 허브입니다.

:::topic-grid
## 오류
- [CFNetworkErrors](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors): 오류 도메인 아래에서 반환되는 오류 코드를 담는 열거형입니다.
- [Error Dictionary Keys](https://developer.apple.com/documentation/cfnetwork/error-dictionary-keys): `NSError` 객체의 dictionary에서 사용할 수 있는 네트워킹 관련 키입니다.
- [Error Domains](https://developer.apple.com/documentation/cfnetwork/error-domains): 상위 수준의 오류 도메인입니다.
:::

:::topic-grid
## 호스트
- [CFHost](https://developer.apple.com/documentation/cfnetwork/cfhost): `CFHost` 객체를 나타내는 불투명 참조입니다.
- [CFHostInfoType](https://developer.apple.com/documentation/cfnetwork/cfhostinfotype): 해석할 데이터 타입 또는 해석된 데이터 타입을 나타내는 값입니다.
- [CFHostClientContext](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext): `CFHost` 객체를 위한 사용자 정의 데이터와 callback을 담는 구조체입니다.
- [CFHostCancelInfoResolution(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhostcancelinforesolution(_:_:)): 호스트 해석을 취소합니다.
- [CFHostCreateWithAddress(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhostcreatewithaddress(_:_:)): 주소를 사용해 호스트 객체 인스턴스를 생성합니다.
- [CFHostCreateWithName(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhostcreatewithname(_:_:)): 이름을 사용해 호스트 객체 인스턴스를 생성합니다.
- [CFHostGetAddressing(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhostgetaddressing(_:_:)): 호스트에서 주소 목록을 가져옵니다.
- [CFHostGetNames(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhostgetnames(_:_:)): `CFHost`에서 이름을 가져옵니다.
- [CFHostGetReachability(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhostgetreachability(_:_:)): 호스트의 reachability 정보를 가져옵니다.
- [CFHostScheduleWithRunLoop(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhostschedulewithrunloop(_:_:_:)): `CFHost`를 run loop에 등록합니다.
- [CFHostSetClient(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhostsetclient(_:_:_:)): `CFHost` 객체에 client context와 callback 함수를 연결하거나 해제합니다.
- [CFHostStartInfoResolution(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhoststartinforesolution(_:_:_:)): 호스트 객체의 정보 해석을 시작합니다.
:::

:::topic-grid
## 전역 프록시 구성
- [CFNetworkCopyProxiesForURL(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetworkcopyproxiesforurl(_:_:)): 지정한 URL을 내려받을 때 사용해야 하는 프록시 목록을 반환합니다.
- [CFNetworkCopyProxiesForAutoConfigurationScript(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetworkcopyproxiesforautoconfigurationscript(_:_:_:)): 프록시 자동 구성 스크립트를 실행해 지정한 URL에 가장 적합한 프록시를 결정합니다.
- [CFNetworkExecuteProxyAutoConfigurationScript(_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetworkexecuteproxyautoconfigurationscript(_:_:_:_:)): 프록시 자동 구성 스크립트를 내려받아 실행합니다.
- [CFNetworkExecuteProxyAutoConfigurationURL(_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetworkexecuteproxyautoconfigurationurl(_:_:_:_:)): 프록시 자동 구성 URL을 사용해 스크립트를 내려받아 실행합니다.
- [CFNetworkCopySystemProxySettings()](https://developer.apple.com/documentation/cfnetwork/cfnetworkcopysystemproxysettings()): 현재 시스템 전체 인터넷 프록시 설정을 담은 `CFDictionary`를 반환합니다.
- [CFProxyAutoConfigurationResultCallback](https://developer.apple.com/documentation/cfnetwork/cfproxyautoconfigurationresultcallback): 프록시 자동 구성 계산이 끝났을 때 호출되는 callback 함수입니다.
- [Property Keys](https://developer.apple.com/documentation/cfnetwork/property-keys): 속성 get/set 함수에서 사용하는 키입니다.
- [Proxy Types](https://developer.apple.com/documentation/cfnetwork/proxy-types): 프록시 유형을 지정하는 상수입니다.
- [Global Proxy Settings Constants](https://developer.apple.com/documentation/cfnetwork/global-proxy-settings-constants): 전역 프록시 설정 dictionary의 키로 사용하는 상수입니다.
:::

:::topic-grid
## HTTP 인증
- [CFHTTPAuthentication](https://developer.apple.com/documentation/cfnetwork/cfhttpauthentication): HTTP 인증 정보를 나타내는 불투명 참조입니다.
- [CFHTTPAuthenticationAppliesToRequest(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationappliestorequest(_:_:)): `CFHTTPAuthentication` 객체가 특정 `CFHTTPMessage` 요청과 연결되어 있는지 나타내는 Boolean 값을 반환합니다.
- [CFHTTPAuthenticationCopyDomains(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationcopydomains(_:)): 주어진 `CFHTTPAuthentication` 객체를 적용할 수 있는 도메인 URL 배열을 반환합니다.
- [CFHTTPAuthenticationCopyMethod(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationcopymethod(_:)): 인증을 요청에 적용할 때 사용될 가장 강력한 인증 방식을 가져옵니다.
- [CFHTTPAuthenticationCopyRealm(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationcopyrealm(_:)): 인증 정보의 namespace를 가져옵니다.
- [CFHTTPAuthenticationCreateFromResponse(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationcreatefromresponse(_:_:)): 인증 실패 응답으로부터 `CFHTTPAuthentication` 객체를 생성합니다.
- [CFHTTPAuthenticationIsValid(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationisvalid(_:_:)): `CFHTTPAuthentication` 객체가 유효한지 나타내는 Boolean 값을 반환합니다.
- [CFHTTPAuthenticationRequiresUserNameAndPassword(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpauthenticationrequiresusernameandpassword(_:)): 인증 방식에 사용자 이름과 암호가 필요한지 나타냅니다.
- [kCFHTTPAuthenticationSchemeBasic](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemebasic): HTTP Basic 인증 방식을 요청합니다.
- [kCFHTTPAuthenticationSchemeDigest](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemedigest): HTTP Digest 인증 방식을 요청합니다.
- [kCFHTTPAuthenticationSchemeKerberos](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschemekerberos): HTTP Kerberos 인증 방식을 요청합니다.
- [kCFHTTPAuthenticationSchemeNTLM](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationschementlm): HTTP NTLM 인증 방식을 요청합니다.
- [kCFHTTPAuthenticationUsername](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationusername): 인증에 사용할 사용자 이름입니다.
- [kCFHTTPAuthenticationPassword](https://developer.apple.com/documentation/cfnetwork/kcfhttpauthenticationpassword): 인증에 사용할 암호입니다.
:::

:::topic-grid
## HTTP 메시지
- [CFHTTPMessage](https://developer.apple.com/documentation/cfnetwork/cfhttpmessage): HTTP 메시지를 나타내는 불투명 참조입니다.
- [CFHTTPMessageAddAuthentication(_:_:_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageaddauthentication(_:_:_:_:_:_:)): 요청에 인증 정보를 추가합니다.
- [CFHTTPMessageAppendBytes(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageappendbytes(_:_:_:)): 객체에 데이터를 추가합니다.
- [CFHTTPMessageApplyCredentialDictionary(_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageapplycredentialdictionary(_:_:_:_:)): 인증 자격 증명을 담은 dictionary를 사용해 인증 방식을 수행합니다.
- [CFHTTPMessageApplyCredentials(_:_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageapplycredentials(_:_:_:_:_:)): 지정된 인증 방식을 수행합니다.
- [CFHTTPMessageCopyAllHeaderFields(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecopyallheaderfields(_:)): 객체의 모든 헤더 필드를 가져옵니다.
- [CFHTTPMessageCopyBody(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecopybody(_:)): 객체의 본문을 가져옵니다.
- [CFHTTPMessageCopyHeaderFieldValue(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecopyheaderfieldvalue(_:_:)): 헤더 필드 값을 가져옵니다.
- [CFHTTPMessageCopyRequestMethod(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecopyrequestmethod(_:)): 요청 메서드를 가져옵니다.
- [CFHTTPMessageCopyRequestURL(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecopyrequesturl(_:)): 요청 URL을 가져옵니다.
- [CFHTTPMessageCopyResponseStatusLine(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecopyresponsestatusline(_:)): 응답 상태 줄을 가져옵니다.
- [CFHTTPMessageCopySerializedMessage(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecopyserializedmessage(_:)): `CFHTTPMessage` 객체를 직렬화합니다.
- [CFHTTPMessageCreateRequest(_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecreaterequest(_:_:_:_:)): HTTP 요청용 객체를 생성합니다.
- [CFHTTPMessageCreateResponse(_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagecreateresponse(_:_:_:_:)): HTTP 응답용 객체를 생성합니다.
- [CFHTTPMessageGetResponseStatusCode(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagegetresponsestatuscode(_:)): HTTP 응답 객체의 상태 코드를 가져옵니다.
- [CFHTTPMessageIsHeaderComplete(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageisheadercomplete(_:)): 메시지 헤더가 완전한지 판단합니다.
- [CFHTTPMessageIsRequest(_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessageisrequest(_:)): 메시지가 요청인지 응답인지 나타내는 Boolean 값을 반환합니다.
- [CFHTTPMessageSetBody(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagesetbody(_:_:)): 객체의 본문을 설정합니다.
- [CFHTTPMessageSetHeaderFieldValue(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfhttpmessagesetheaderfieldvalue(_:_:_:)): HTTP 메시지의 헤더 필드 값을 설정합니다.
- [kCFHTTPVersion1_0](https://developer.apple.com/documentation/cfnetwork/kcfhttpversion1_0): HTTP 1.0 버전입니다.
- [kCFHTTPVersion1_1](https://developer.apple.com/documentation/cfnetwork/kcfhttpversion1_1): HTTP 1.1 버전입니다.
- [kCFHTTPVersion2_0](https://developer.apple.com/documentation/cfnetwork/kcfhttpversion2_0): HTTP 2.0 버전입니다.
:::

:::topic-grid
## FTP
- [CFFTPCreateParsedResourceListing(_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfftpcreateparsedresourcelisting(_:_:_:_:)): FTP 목록을 dictionary로 파싱합니다.
- [kCFFTPResourceGroup](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcegroup): FTP 리소스를 공유하는 그룹 이름을 담은 `CFString`을 가져오는 `CFDictionary` 키입니다.
- [kCFFTPResourceLink](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcelink): 심볼릭 링크 정보를 담은 `CFString`을 가져오는 `CFDictionary` 키입니다.
- [kCFFTPResourceModDate](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcemoddate): FTP 리소스가 마지막으로 수정된 날짜와 시간을 담은 `CFDate`를 가져오는 키입니다.
- [kCFFTPResourceMode](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcemode): FTP 리소스 접근 권한을 담은 `CFNumber`를 가져오는 키입니다.
- [kCFFTPResourceName](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcename): FTP 리소스 이름을 담은 `CFString`을 가져오는 키입니다.
- [kCFFTPResourceOwner](https://developer.apple.com/documentation/cfnetwork/kcfftpresourceowner): FTP 리소스 소유자 이름을 담은 `CFString`을 가져오는 키입니다.
- [kCFFTPResourceSize](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcesize): FTP 리소스 크기(바이트)를 담은 `CFNumber`를 가져오는 키입니다.
:::

:::topic-grid
## 네트워크 진단
- [CFNetDiagnostic](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnostic): `CFNetDiagnostic`을 나타내는 불투명 참조입니다.
- [CFNetDiagnosticStatusValues](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticstatusvalues): 진단 상태 값을 위한 상수입니다.
- [CFNetDiagnosticCopyNetworkStatusPassively(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticcopynetworkstatuspassively(_:_:)): 네트워크 상태 값을 가져옵니다.
- [CFNetDiagnosticCreateWithStreams(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticcreatewithstreams(_:_:_:)): `CFStream` 쌍으로부터 네트워크 진단 객체를 생성합니다.
- [CFNetDiagnosticCreateWithURL(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticcreatewithurl(_:_:)): `CFURLRef`로부터 `CFNetDiagnosticRef`를 생성합니다.
- [CFNetDiagnosticDiagnoseProblemInteractively(_:)](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticdiagnoseprobleminteractively(_:)): Network Diagnostics 창을 엽니다.
- [CFNetDiagnosticSetName(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetdiagnosticsetname(_:_:)): 표시할 앱 이름을 재정의합니다.
:::

:::topic-grid
## 네트워크 서비스
- [CFNetService](https://developer.apple.com/documentation/cfnetwork/cfnetservice): `CFNetService`를 나타내는 불투명 참조입니다.
- [CFNetServiceBrowser](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowser): `CFNetServiceBrowser`를 나타내는 불투명 참조입니다.
- [CFNetServiceMonitor](https://developer.apple.com/documentation/cfnetwork/cfnetservicemonitor): 서비스 모니터를 나타내는 불투명 참조입니다.
- [CFNetServiceBrowserSearchForDomains(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowsersearchfordomains(_:_:_:)): 도메인을 검색합니다.
- [CFNetServiceBrowserSearchForServices(_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetservicebrowsersearchforservices(_:_:_:_:)): 지정한 유형의 서비스를 도메인 안에서 검색합니다.
- [CFNetServiceCreate(_:_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetservicecreate(_:_:_:_:_:)): 네트워크 서비스 객체를 생성합니다.
- [CFNetServiceCreateDictionaryWithTXTData(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetservicecreatedictionarywithtxtdata(_:_:)): TXT 레코드 데이터로 dictionary를 생성합니다.
- [CFNetServiceCreateTXTDataWithDictionary(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetservicecreatetxtdatawithdictionary(_:_:)): key/value 쌍 집합을 `CFDataRef`로 평탄화합니다.
- [CFNetServiceGetAddressing(_:)](https://developer.apple.com/documentation/cfnetwork/cfnetservicegetaddressing(_:)): `CFNetService`의 IP 주소 정보를 가져옵니다.
- [CFNetServiceGetTXTData(_:)](https://developer.apple.com/documentation/cfnetwork/cfnetservicegettxtdata(_:)): 네트워크 서비스의 TXT 레코드 내용을 조회합니다.
- [CFNetServiceResolveWithTimeout(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetserviceresolvewithtimeout(_:_:_:)): `CFNetService`의 IP 주소를 해석합니다.
- [CFNetServiceSetTXTData(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfnetservicesettxtdata(_:_:)): `CFNetService`의 TXT 레코드를 설정합니다.
:::

:::topic-grid
## 스트림
- [CFReadStreamCreateForHTTPRequest(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfreadstreamcreateforhttprequest(_:_:)): `CFHTTP` 요청 메시지를 위한 read stream을 생성합니다.
- [CFReadStreamCreateForStreamedHTTPRequest(_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfreadstreamcreateforstreamedhttprequest(_:_:_:)): 본문이 메모리에 유지하기에는 너무 긴 `CFHTTP` 요청 메시지 객체용 read stream을 생성합니다.
- [kCFStreamPropertyHTTPFinalRequest](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpfinalrequest): 모든 수정이 끝난 뒤 최종적으로 전송된 `CFHTTPMessage`를 반환하는 HTTP Final Request 속성입니다.
- [kCFStreamPropertyHTTPFinalURL](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpfinalurl): 최종 HTTP URL을 담은 `CFURL`을 반환하는 HTTP Final URL 속성입니다.
- [kCFStreamPropertyHTTPResponseHeader](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpresponseheader): HTTP 응답 메시지의 헤더를 반환하는 HTTP Response Header 속성입니다.
- [kCFStreamPropertyHTTPShouldAutoredirect](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpshouldautoredirect): HTTP 자동 리다이렉션 활성화 여부를 제어하는 속성입니다.
- [CFWriteStreamCreateWithFTPURL(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfwritestreamcreatewithftpurl(_:_:)): FTP write stream을 생성합니다.
- [CFReadStreamCreateWithFTPURL(_:_:)](https://developer.apple.com/documentation/cfnetwork/cfreadstreamcreatewithftpurl(_:_:)): FTP read stream을 생성합니다.
- [kCFStreamPropertyFTPFileTransferOffset](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpfiletransferoffset): 전송을 시작할 파일 오프셋을 나타내는 FTP stream 속성입니다.
- [kCFStreamPropertyFTPPassword](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftppassword): 로그인 암호를 저장하는 FTP stream 속성입니다.
- [kCFStreamPropertyFTPProxy](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxy): 프록시 dictionary를 보관하는 FTP Proxy stream 속성입니다.
- [kCFStreamPropertyFTPUsePassiveMode](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpusepassivemode): 패시브 모드 활성화 여부를 제어하는 FTP Passive Mode stream 속성입니다.
- [kCFStreamPropertyFTPUserName](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpusername): 로그인 사용자 이름을 저장하는 FTP User Name stream 속성입니다.
- [CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfstreamcreatepairwithsockettocfhost(_:_:_:_:_:)): 지정한 객체에 연결된 읽기/쓰기 stream 쌍을 생성합니다.
- [CFStreamCreatePairWithSocketToNetService(_:_:_:_:)](https://developer.apple.com/documentation/cfnetwork/cfstreamcreatepairwithsockettonetservice(_:_:_:_:)): `CFNetService`용 stream 쌍을 생성합니다.
- [kCFStreamNetworkServiceTypeBackground](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypebackground): stream이 백그라운드 다운로드임을 지정합니다.
- [kCFStreamNetworkServiceTypeVideo](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevideo): stream이 대화형 비디오 데이터를 제공함을 지정합니다.
- [kCFStreamNetworkServiceTypeVoIP](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevoip): stream이 VoIP 서비스를 제공함을 지정합니다.
- [kCFStreamErrorDomainHTTP](https://developer.apple.com/documentation/cfnetwork/kcfstreamerrordomainhttp): 오류 코드가 HTTP 오류 코드임을 나타냅니다.
- [kCFStreamErrorDomainFTP](https://developer.apple.com/documentation/cfnetwork/kcfstreamerrordomainftp): 오류 코드가 FTP 오류 코드임을 나타냅니다.
- [kCFStreamPropertyConnectionIsCellular](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyconnectioniscellular): stream이 셀룰러(WWAN) 인터페이스를 통해 연결되어 있는지 나타내는 Boolean 값입니다.
- [kCFStreamPropertyNoCellular](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertynocellular): 연결을 셀룰러(WWAN) 연결 위에서 설정하지 않도록 지시하는 Boolean 값입니다.
- [kCFStreamPropertySSLSettings](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysslsettings): SSL 설정을 위한 속성 키입니다.
:::
