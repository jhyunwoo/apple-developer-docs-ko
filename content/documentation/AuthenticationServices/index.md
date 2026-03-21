---
route: /documentation/AuthenticationServices
source_url: https://developer.apple.com/documentation/AuthenticationServices
source_locale: en-US
section: docc
content_type: symbol
title: Authentication Services
original_title: Authentication Services
source_hash: a4f5aa0bc6534b46372339e85a942792782b0fc88bba0b29aff137c24dd8a729
canonical_source: manual-translation
last_crawled_at: '2026-03-13T12:54:44+00:00'
last_translated_at: '2026-03-14T00:13:00+09:00'
---

# Authentication Services

사용자가 앱과 서비스에 로그인하기 쉽게 만듭니다.

## 개요

Authentication Services 프레임워크를 사용하면 사용자가 자신의 신원을 확인하기 위해 자격 증명을 입력할 때의 경험을 개선할 수 있습니다.

- 사용자가 Apple ID로 서비스에 로그인할 수 있게 합니다.
- 앱의 로그인 흐름 안에서 저장된 암호를 찾아볼 수 있게 합니다.
- iCloud 키체인이나 물리적 보안 키를 사용해 앱과 웹사이트에 대한 암호 없는 등록 및 인증 흐름을 제공합니다.
- 약한 암호에서 강한 암호로의 자동 보안 업그레이드나 Sign in with Apple 사용으로의 업그레이드를 수행합니다.
- OAuth 같은 기술을 사용해 앱과 웹 브라우저 사이에 데이터를 공유하여, 기존 웹 기반 로그인을 앱 안에서 활용합니다.
- 엔터프라이즈 앱에서 single sign-on(SSO) 경험을 만듭니다.

단순하고 직관적인 가입 및 로그인 흐름은 사용자가 암호를 기억해야 하는 부담을 줄여 주며, 이는 보안을 향상하는 데 도움이 될 수 있습니다.

:::topic-grid
## 인증 요청
- [ASAuthorizationController](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller): provider가 생성한 인증 요청을 관리하는 controller입니다.
- [AuthorizationController](https://developer.apple.com/documentation/authenticationservices/authorizationcontroller): view가 인증 요청을 수행할 때 사용하는 SwiftUI environment 값입니다.
- [ASAuthorizationResult](https://developer.apple.com/documentation/authenticationservices/asauthorizationresult): 인증 요청이 성공했을 때의 결과를 설명합니다.
:::

:::topic-grid
## Sign In with Apple
- [Implementing User Authentication with Sign in with Apple](https://developer.apple.com/documentation/authenticationservices/implementing-user-authentication-with-sign-in-with-apple): 사용자가 앱에서 계정을 만들고 서비스를 시작할 수 있는 방법을 제공합니다.
- [Simplifying User Authentication in a tvOS App](https://developer.apple.com/documentation/authenticationservices/simplifying-user-authentication-in-a-tvos-app): AuthenticationServices를 사용해 tvOS 앱에 부드러운 로그인 경험을 구축합니다.
- [SignInWithAppleButton](https://developer.apple.com/documentation/authenticationservices/signinwithapplebutton): 표시용 Sign in with Apple 버튼을 만드는 SwiftUI view입니다.
- [Sign in with Apple Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.applesignin): 앱이 Sign in with Apple을 사용할 수 있게 하는 entitlement입니다.
- [ASAuthorizationAppleIDProvider](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidprovider): Apple ID를 기반으로 사용자를 인증하는 요청을 생성하는 메커니즘입니다.
- [ASAuthorizationAppleIDCredential](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidcredential): Apple ID 인증이 성공했을 때 얻는 credential입니다.
:::

:::topic-grid
## 암호
- [Password AutoFill](https://developer.apple.com/documentation/Security/password-autofill): 앱의 로그인 및 온보딩 절차를 간소화합니다.
- [ASAuthorizationPasswordProvider](https://developer.apple.com/documentation/authenticationservices/asauthorizationpasswordprovider): 키체인 자격 증명 공유를 수행하기 위한 요청을 생성하는 메커니즘입니다.
- [ASPasswordCredential](https://developer.apple.com/documentation/authenticationservices/aspasswordcredential): 암호 credential입니다.
- [Password use in web browsers](https://developer.apple.com/documentation/authenticationservices/password-use-in-web-browsers): 암호를 사용해 웹사이트 사용자를 등록하고 인증합니다.
:::

:::topic-grid
## 패스키
- [Public-Private Key Authentication](https://developer.apple.com/documentation/authenticationservices/public-private-key-authentication): 암호 없이 passkey와 보안 키를 사용해 사용자를 등록하고 인증합니다.
- [Passkey use in web browsers](https://developer.apple.com/documentation/authenticationservices/passkey-use-in-web-browsers): passkey를 사용해 웹사이트 사용자를 등록하고 인증합니다.
- [Performing fast account creation with passkeys](https://developer.apple.com/documentation/authenticationservices/performing-fast-account-creation-with-passkeys): passkey와 연관 도메인을 사용해 사용자가 빠르게 계정을 만들 수 있게 합니다.
- [Connecting to a service with passkeys](https://developer.apple.com/documentation/authenticationservices/connecting-to-a-service-with-passkeys): 사용자가 암호를 입력하지 않고 서비스에 로그인할 수 있게 합니다.
:::

:::topic-grid
## 웹 인증 세션
- [Authenticating a User Through a Web Service](https://developer.apple.com/documentation/authenticationservices/authenticating-a-user-through-a-web-service): web authentication session을 사용해 앱에서 사용자를 인증합니다.
- [Securing Logins with iCloud Keychain Verification Codes](https://developer.apple.com/documentation/authenticationservices/securing-logins-with-icloud-keychain-verification-codes): 기기에서 생성된 시간 기반 코드를 사용해 안전한 인증 경험을 제공합니다.
- [ASWebAuthenticationSession](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession): 앱이 웹 서비스를 통해 사용자를 인증할 때 사용하는 세션입니다.
- [WebAuthenticationSession](https://developer.apple.com/documentation/authenticationservices/webauthenticationsession): view가 웹 서비스를 사용해 누군가를 인증할 때 사용하는 SwiftUI environment 값입니다.
- [Supporting Single Sign-On in a Web Browser App](https://developer.apple.com/documentation/authenticationservices/supporting-single-sign-on-in-a-web-browser-app): 다른 앱에서 오는 웹 인증 요청을 처리하도록 웹 브라우저 앱을 확장합니다.
- [ASWebAuthenticationSessionWebBrowserSessionManager](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionwebbrowsersessionmanager): 앱과 웹 브라우저 사이의 데이터 공유를 중재하는 세션 관리자입니다.
- [ASWebAuthenticationSessionWebBrowserSupportCapabilities](https://developer.apple.com/documentation/BundleResources/Information-Property-List/ASWebAuthenticationSessionWebBrowserSupportCapabilities): 브라우저 앱이 다른 앱의 인증 요청을 처리할 수 있는 능력을 선언할 때 사용하는 키 모음입니다.
:::

:::topic-grid
## AutoFill 자격 증명
- [Providing one-time passcodes to AutoFill](https://developer.apple.com/documentation/authenticationservices/providing-one-time-passcodes-to-autofill): 사용자가 다중 요소 인증을 효율적으로 수행할 수 있도록 돕습니다.
- [AutoFill Credential Provider Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.authentication-services.autofill-credential-provider): 사용자 허가가 있을 때 Safari와 다른 앱에서 AutoFill용 사용자 이름과 암호를 제공할 수 있는지를 나타내는 Boolean 값입니다.
- [ASCredentialProviderViewController](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller): 자격 증명 관리자 앱이 AutoFill을 확장할 때 사용하는 view controller입니다.
:::

:::topic-grid
## 자격 증명 마이그레이션
- [ASCredentialExportManager](https://developer.apple.com/documentation/authenticationservices/ascredentialexportmanager): 자격 증명 내보내기를 관리하는 클래스입니다.
- [ASCredentialImportManager](https://developer.apple.com/documentation/authenticationservices/ascredentialimportmanager): 자격 증명 가져오기를 관리하는 클래스입니다.
:::

:::topic-grid
## Single sign-on (SSO)
- [Enterprise single sign-on (SSO)](https://developer.apple.com/documentation/authenticationservices/enterprise-single-sign-on-sso)
- [Platform single sign-on (SSO)](https://developer.apple.com/documentation/authenticationservices/platform-single-sign-on-sso): macOS 로그인 자격 증명을 사용해 identity provider와 single sign-on을 수행합니다.
:::

:::topic-grid
## Apple TV 인증
- [customAuthorizationMethods](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/customauthorizationmethods): 사용자가 선택할 수 있는 사용자 정의 인증 방법 배열입니다.
- [authorizationController(_:didCompleteWithCustomMethod:)](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:)): 인증이 완료되었을 때 delegate에 알리고, 사용자가 선택한 사용자 정의 방법을 지정합니다.
- [ASAuthorizationCustomMethod](https://developer.apple.com/documentation/authenticationservices/asauthorizationcustommethod): 사용자 정의 인증 방법입니다.
:::

:::topic-grid
## 자동 보안 업그레이드
- [Upgrading Account Security With an Account Authentication Modification Extension](https://developer.apple.com/documentation/authenticationservices/upgrading-account-security-with-an-account-authentication-modification-extension): 더 나은 보안을 위해 계정을 Sign in with Apple 또는 강한 암호 사용으로 자동이며 투명하게 전환합니다.
- [ASAccountAuthenticationModificationController](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontroller): 계정의 인증 속성을 수정하는 요청을 수행하는 객체입니다.
- [ASAccountAuthenticationModificationViewController](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationviewcontroller): 사용자 암호를 강한 암호로 업그레이드하거나 계정을 Sign in with Apple로 전환할 수 있는 view controller입니다.
- [ASAccountAuthenticationModificationExtensionContext](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationextensioncontext): 계정의 암호를 변경하거나 Sign in with Apple로 업그레이드할 때 상호 작용하는 객체입니다.
:::

:::topic-grid
## 자격 증명 관리자 업데이트
- [ASCredentialUpdater](https://developer.apple.com/documentation/authenticationservices/ascredentialupdater): 시스템에서 활성화된 credential manager에 자격 증명 업데이트 이벤트를 전달하는 클래스입니다.
:::

:::topic-grid
## 참고 자료
- [AuthenticationServices Enumerations](https://developer.apple.com/documentation/authenticationservices/authenticationservices-enumerations)
- [AuthenticationServices Data Types](https://developer.apple.com/documentation/authenticationservices/authenticationservices-data-types)
:::

:::topic-grid
## 클래스
- [ASAuthorizationAccountCreationPlatformPublicKeyCredential](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationplatformpublickeycredential)
- [ASAuthorizationAccountCreationPlatformPublicKeyCredentialRequest](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationplatformpublickeycredentialrequest)
- [ASAuthorizationAccountCreationProvider](https://developer.apple.com/documentation/authenticationservices/asauthorizationaccountcreationprovider)
- [ASAuthorizationProviderExtensionUserLoginConfiguration](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionuserloginconfiguration)
- [ASCredentialDataManager](https://developer.apple.com/documentation/authenticationservices/ascredentialdatamanager): 시스템에서 활성화된 credential manager에 자격 증명과 이벤트를 제출할 수 있게 하는 클래스입니다.
- [ASGeneratePasswordsRequest](https://developer.apple.com/documentation/authenticationservices/asgeneratepasswordsrequest)
- [ASGeneratedPassword](https://developer.apple.com/documentation/authenticationservices/asgeneratedpassword)
- [ASOneTimeCodeCredentialIdentity](https://developer.apple.com/documentation/authenticationservices/asonetimecodecredentialidentity)
- [ASSavePasswordRequest](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest)
:::

:::topic-grid
## 구조체
- [ASAuthorizationProviderExtensionEncryptionAlgorithm](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionencryptionalgorithm)
- [ASAuthorizationProviderExtensionSigningAlgorithm](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionsigningalgorithm)
- [ASAutoFillURLScope](https://developer.apple.com/documentation/authenticationservices/asautofillurlscope): 자격 증명 AutoFill에 대해 지원되는 URL 구성 요소의 하위 집합을 나타내는 구조체입니다.
- [ASEmailIdentifier](https://developer.apple.com/documentation/authenticationservices/asemailidentifier)
- [ASImportableCredentialScope](https://developer.apple.com/documentation/authenticationservices/asimportablecredentialscope): 자격 증명이 사용 가능해야 하는 위치의 범위입니다.
- [ASImportableEditableField](https://developer.apple.com/documentation/authenticationservices/asimportableeditablefield): 자격 증명 안에서 사용자가 수정할 수 있는 필드입니다.
- [ASImportableFIDO2Extensions](https://developer.apple.com/documentation/authenticationservices/asimportablefido2extensions): CXF에 정의된 FIDO2 확장을 표현합니다.
- [ASImportableFIDO2HMACCredential](https://developer.apple.com/documentation/authenticationservices/asimportablefido2hmaccredential): CXF에 정의된 FIDO2 HMAC 자격 증명을 표현합니다.
- [ASImportableFIDO2LargeBlob](https://developer.apple.com/documentation/authenticationservices/asimportablefido2largeblob): CXF에 정의된 FIDO2 LargeBlob 확장을 표현합니다.
- [ASPhoneNumberIdentifier](https://developer.apple.com/documentation/authenticationservices/asphonenumberidentifier)
- [ASPublicKeyCredentialClientData](https://developer.apple.com/documentation/authenticationservices/aspublickeycredentialclientdata-swift.struct)
- [CredentialDataManager](https://developer.apple.com/documentation/authenticationservices/credentialdatamanager)
:::

:::topic-grid
## 변수
- [ASCredentialExchangeActivity](https://developer.apple.com/documentation/authenticationservices/ascredentialexchangeactivity): 가져오기 앱에 전송되는 user activity 객체에서 사용하는 activity type입니다.
- [ASCredentialImportToken](https://developer.apple.com/documentation/authenticationservices/ascredentialimporttoken): 가져오기 앱에 전송되는 user activity의 user info dictionary에서 token에 해당하는 키입니다.
:::

:::topic-grid
## 열거형
- [ASContactIdentifier](https://developer.apple.com/documentation/authenticationservices/ascontactidentifier)
- [ASContactIdentifierRequest](https://developer.apple.com/documentation/authenticationservices/ascontactidentifierrequest)
- [ASImportableExtension](https://developer.apple.com/documentation/authenticationservices/asimportableextension): CXF 확장을 표현합니다.
:::
