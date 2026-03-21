---
route: /documentation/LightweightCodeRequirements
source_url: https://developer.apple.com/documentation/LightweightCodeRequirements
source_locale: en-US
section: docc
content_type: symbol
title: LightweightCodeRequirements
original_title: LightweightCodeRequirements
source_hash: a69d919c70319eb9ae509434abb389903ced56b1592af7df3dfaf4b1e81c2cf9
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:54:05+00:00'
last_translated_at: '2026-03-14T02:30:00+09:00'
---

# LightweightCodeRequirements

디스크에 있는 실행 코드와 실행 중인 프로세스의 정체성을 테스트합니다.

## 개요

암호학적으로 서명된 코드는 code signature 안에 그 정체성에 대한 위변조 방지 진술을 담고 있습니다. lightweight code requirement domain-specific language(DSL)를 사용해 서로 다른 코드 파일을 구분하는 테스트를 구성하십시오. 이 테스트를 사용하면 디스크 위의 코드 파일, 실행 중인 프로세스, 운영체제가 실행하는 프로세스를 구분할 수 있습니다. 디스크 위의 코드 파일에는 다음이 포함됩니다.

- 실행 가능한 binary
- dynamic 또는 static library
- framework
- loadable bundle

## 서명된 코드 속성 테스트 정의하기

lightweight code requirement DSL에서 코드 속성을 테스트하는 데 사용하는 키워드는 다음과 같습니다.

:::term-list
[CodeDirectoryHash](https://developer.apple.com/documentation/lightweightcoderequirements/codedirectoryhash): 코드의 code directory hash가 특정 값과 일치하는지, 또는 허용된 값 목록 안에 있는지를 테스트합니다. code directory hash에 대한 자세한 내용은 [TN3126: Inside Code Signing: Hashes](https://developer.apple.com/documentation/Technotes/tn3126-inside-code-signing-hashes)를 참고하십시오.
[ProcessCodeSigningFlags](https://developer.apple.com/documentation/lightweightcoderequirements/processcodesigningflags): 실행 중인 프로세스의 실행 파일이 [ProcessCodeSigningFlags.ValueSet](https://developer.apple.com/documentation/lightweightcoderequirements/processcodesigningflags/valueset)에 정의된 특정 flag를 code signature 안에 설정하고 있는지를 테스트합니다.
[OnDiskCodeSigningFlags](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags): 디스크 위 코드가 [OnDiskCodeSigningFlags.ValueSet](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags/valueset)에 정의된 특정 flag를 code signature 안에 설정하고 있는지를 테스트합니다.
[EntitlementsQuery](https://developer.apple.com/documentation/lightweightcoderequirements/entitlementsquery): 실행 파일이 특정 entitlement를 가지는지, 필요하면 특정 값과 함께 가지는지를 테스트합니다.
[InfoPlistHash](https://developer.apple.com/documentation/lightweightcoderequirements/infoplisthash): 실행 파일의 `Info.plist` 파일 해시(명령줄 도구의 경우 포함된 `Info.plist`)가 특정 값과 일치하는지, 또는 허용된 값 목록 안에 있는지를 테스트합니다. code signature 버전에 따라 이 해시는 SHA-1 또는 SHA-256 알고리즘을 사용합니다. 두 버전을 모두 포함하는 목록 안에 해당 해시가 있는지 테스트하십시오.
[IsInitProcess](https://developer.apple.com/documentation/lightweightcoderequirements/isinitprocess): 프로세스가 운영체제의 초기 프로세스, 즉 `launchd`인지 테스트합니다.
[IsMainBinary](https://developer.apple.com/documentation/lightweightcoderequirements/ismainbinary): 실행 파일이 main binary인지 테스트합니다. main binary는 code signature 버전이 최소 `0x20400`이고, `CS_EXECSEG_MAIN_BINARY` flag가 설정된 executable segment를 가집니다.
[IsSIPProtected](https://developer.apple.com/documentation/lightweightcoderequirements/issipprotected): 코드가 System Integrity Protection(SIP)이 적용되는 volume 위에 있는지를 테스트합니다.
[PlatformType](https://developer.apple.com/documentation/lightweightcoderequirements/platformtype): 코드가 특정 플랫폼, 예를 들어 iOS를 대상으로 하는지를 테스트합니다. 허용 값 목록은 [PlatformType.Value](https://developer.apple.com/documentation/lightweightcoderequirements/platformtype/value)에 정의되어 있습니다.
[SigningIdentifier](https://developer.apple.com/documentation/lightweightcoderequirements/signingidentifier): 코드의 signing identifier가 특정 값과 일치하는지, 또는 허용된 값 목록 안에 있는지를 테스트합니다. signing identifier는 일반적으로 앱 같은 코드 번들의 bundle identifier인 문자열이며, 명령줄 도구 같은 다른 코드에도 유사한 구조를 가집니다.
[TeamIdentifier](https://developer.apple.com/documentation/lightweightcoderequirements/teamidentifier): 코드를 서명한 개발자 팀의 team identifier가 특정 값과 일치하는지, 또는 허용된 값 목록 안에 있는지를 테스트합니다.
[TeamIdentifierMatchesCurrentProcess](https://developer.apple.com/documentation/lightweightcoderequirements/teamidentifiermatchescurrentprocess): 실행 중인 프로세스의 코드를 서명한 개발자 팀의 team identifier가 현재 프로세스의 team identifier와 일치하는지를 테스트합니다.
[ValidationCategory](https://developer.apple.com/documentation/lightweightcoderequirements/validationcategory): 코드가 특정 category로 서명되었는지, 또는 허용된 category 목록 안에 있는지를 테스트합니다. 값 목록은 [ValidationCategory.Value](https://developer.apple.com/documentation/lightweightcoderequirements/validationcategory/value)에 정의되어 있습니다.
:::

Apple 이외의 조직이나 개인이 서명한 코드의 경우, 코드의 정체성은 `SigningIdentifier`, `TeamIdentifier`, `ValidationCategory`로 지정됩니다.

## 테스트를 requirement로 결합하기

lightweight code requirement DSL은 개별 테스트를 조합해 복잡한 requirement를 구축하는 데 사용하는 연산자를 제공합니다. 예를 들어 디스크 위 코드 requirement를 구성하는 연산자는 다음과 같습니다.

:::term-list
[anyOf(requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcoderequirement/anyof(requirement:)): 전달된 인수 중 하나 이상이 `true`면 `true`, 모든 인수가 `false`면 `false`입니다.
[allOf(requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcoderequirement/allof(requirement:)): 전달된 인수 각각이 `true`면 `true`, 하나라도 `false`면 `false`입니다.
:::

[ProcessCodeRequirement](https://developer.apple.com/documentation/lightweightcoderequirements/processcoderequirement)과 [LaunchCodeRequirement](https://developer.apple.com/documentation/lightweightcoderequirements/launchcoderequirement)은 프로세스 코드 requirement와 launch requirement를 구축하는 유사한 연산자를 제공합니다.

`anyOf(requirement:)` 및 `allOf(requirement:)` 연산자는 입력을 다음과 같이 단순화합니다.

- 인수로 단일 제약만 받는 연산자는 자신을 제거하고 해당 제약의 직접 평가 결과로 대체합니다.
- `anyOf(requirement:)` 연산자의 인수 중 일부가 다시 `anyOf(requirement:)` 연산자라면, 둘의 인수는 상위 `anyOf(requirement:)` 연산자가 평가하는 하나의 제약 집합으로 병합됩니다.
- `allOf(requirement:)` 연산자의 인수 중 일부가 다시 `allOf(requirement:)` 연산자라면, 둘의 인수는 상위 `allOf(requirement:)` 연산자가 평가하는 하나의 제약 집합으로 병합됩니다.

`allOf(requirement:)`와 `anyOf(requirement:)`는 모두 단순화 결과 같은 제약이 한 연산자의 인수 안에 두 번 나타나면 오류를 던집니다. 예를 들어 `anyOf(requirement:)` 연산자 안에 [InfoPlistHash](https://developer.apple.com/documentation/lightweightcoderequirements/infoplisthash) 제약 테스트가 두 개 들어 있는 경우가 그렇습니다. 이 단순화 규칙의 예외는 여러 [EntitlementsQuery](https://developer.apple.com/documentation/lightweightcoderequirements/entitlementsquery) 테스트가 한 연산자의 인수 안에 함께 나타날 수 있다는 점입니다.

## 실행 중인 프로세스가 lightweight code requirement를 만족하는지 테스트하기

DSL을 사용해 [ProcessCodeRequirement](https://developer.apple.com/documentation/lightweightcoderequirements/processcoderequirement)을 만들고, 실행 중인 프로세스를 나타내는 [SecTask](https://developer.apple.com/documentation/Security/SecTask)와 함께 [SecTaskValidateForRequirement(task:requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/sectaskvalidateforrequirement(task:requirement:))에 전달합니다. task의 코드가 lightweight code requirement를 만족하면 함수는 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

## 디스크 위 코드가 lightweight code requirement를 만족하는지 테스트하기

DSL을 사용해 [OnDiskCodeRequirement](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcoderequirement)을 만들고, 코드 표현에 [SecStaticCode](https://developer.apple.com/documentation/Security/SecStaticCode) 또는 [SecCode](https://developer.apple.com/documentation/Security/SecCode) 중 무엇을 구성했는지에 따라 [SecStaticCodeCheckValidityWithOnDiskRequirement(code:flags:requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/secstaticcodecheckvaliditywithondiskrequirement(code:flags:requirement:)) 또는 [SecCodeCheckValidityWithOnDiskRequirement(code:flags:requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/seccodecheckvaliditywithondiskrequirement(code:flags:requirement:))에 전달합니다. 두 함수 모두 코드가 유효한 signature를 가지는지, requirement를 만족하는지, 어떤 오류가 발생했는지를 나타내는 [ValidationResult](https://developer.apple.com/documentation/lightweightcoderequirements/validationresult)를 반환합니다.

## 새 프로세스로 실행할 수 있는 실행 파일 제한하기

DSL을 사용해 [LaunchCodeRequirement](https://developer.apple.com/documentation/lightweightcoderequirements/launchcoderequirement)을 만들고, [run()](https://developer.apple.com/documentation/Foundation/Process/run())을 호출하기 전에 [Process](https://developer.apple.com/documentation/Foundation/Process) 인스턴스의 [launchRequirement](https://developer.apple.com/documentation/Foundation/Process/launchRequirement)에 설정합니다. 프로세스의 [executableURL](https://developer.apple.com/documentation/Foundation/Process/executableURL)에 지정된 실행 파일이 launch requirement를 만족하면 kernel이 프로세스를 실행하고, 그렇지 않으면 `run()`이 오류를 던집니다. 또한 requirement를 실행 파일의 code signature 안에 포함하는 property list 파일의 launch constraint로 인코딩해, 어떤 프로세스가 실행 파일을 실행할 수 있는지와 프로세스가 어떤 dynamic library를 로드할 수 있는지를 제한할 수도 있습니다. 자세한 내용은 [Applying launch environment and library constraints](https://developer.apple.com/documentation/Security/applying-launch-environment-and-library-constraints)를 참고하십시오.

:::topic-grid
## 실행 중인 프로세스의 코드 requirement 확인
- [SecTaskValidateForRequirement(task:requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/sectaskvalidateforrequirement(task:requirement:)): task의 실행 파일이 lightweight code requirement를 만족하는지 테스트합니다.
- [ProcessCodeRequirement](https://developer.apple.com/documentation/lightweightcoderequirements/processcoderequirement): 실행 중인 프로세스를 평가할 때 사용하는 lightweight code requirement입니다.
- [allOf(requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/allof(requirement:)-4k3ay): 실행 중인 프로세스의 실행 파일이 제공된 모든 제약을 만족하도록 요구하는 제약을 만듭니다.
- [anyOf(requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/anyof(requirement:)-vwhn): 실행 중인 프로세스의 실행 파일이 제공된 제약 중 어느 하나라도 만족하도록 요구하는 제약을 만듭니다.
- [ProcessConstraint](https://developer.apple.com/documentation/lightweightcoderequirements/processconstraint): process code requirement에서 사용할 수 있는 lightweight code requirement 제약이 준수하는 protocol입니다.
- [ProcessCodeSigningFlags](https://developer.apple.com/documentation/lightweightcoderequirements/processcodesigningflags): 프로세스의 현재 code-signing flag와 일치하는 제약입니다.
- [ProcessConstraintBuilder](https://developer.apple.com/documentation/lightweightcoderequirements/processconstraintbuilder): closure로부터 process 제약을 구성하는 사용자 정의 parameter attribute입니다.
- [TeamIdentifierMatchesCurrentProcess](https://developer.apple.com/documentation/lightweightcoderequirements/teamidentifiermatchescurrentprocess): 프로세스가 호출한 현재 프로세스와 같은 team identifier를 가질 때 일치하는 제약입니다.
:::

:::topic-grid
## 시작 프로세스의 코드 requirement 확인
- [SecCodeCheckValidityWithProcessRequirement(code:flags:requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/seccodecheckvaliditywithprocessrequirement(code:flags:requirement:)): 실행 중인 프로세스와 연결된 코드가 lightweight code requirement를 만족하는지 확인합니다.
- [launchRequirement](https://developer.apple.com/documentation/Foundation/Process/launchRequirement)
- [LaunchCodeRequirement](https://developer.apple.com/documentation/lightweightcoderequirements/launchcoderequirement): 시작 중인 프로세스의 실행 파일을 평가할 때 사용하는 lightweight code requirement입니다.
- [allOf(requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/allof(requirement:)-4gf5f): 시작 중인 프로세스의 실행 파일이 제공된 모든 제약을 만족하도록 요구하는 제약을 만듭니다.
- [anyOf(requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/anyof(requirement:)-6nicx): 시작 중인 프로세스의 실행 파일이 제공된 제약 중 하나라도 만족하도록 요구하는 제약을 만듭니다.
- [LaunchConstraint](https://developer.apple.com/documentation/lightweightcoderequirements/launchconstraint): launch code requirement에서 사용할 수 있는 lightweight code requirement 제약이 준수하는 protocol입니다.
- [LaunchConstraintBuilder](https://developer.apple.com/documentation/lightweightcoderequirements/launchconstraintbuilder): closure로부터 launch 제약을 구성하는 사용자 정의 parameter attribute입니다.
:::

:::topic-grid
## 디스크 위 코드 파일의 requirement 확인
- [SecStaticCodeCheckValidityWithOnDiskRequirement(code:flags:requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/secstaticcodecheckvaliditywithondiskrequirement(code:flags:requirement:)): 디스크 위 static code가 lightweight code requirement를 만족하는지 확인합니다.
- [SecCodeCheckValidityWithOnDiskRequirement(code:flags:requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/seccodecheckvaliditywithondiskrequirement(code:flags:requirement:)): 디스크 위 코드가 lightweight code requirement를 만족하는지 확인합니다.
- [ValidationResult](https://developer.apple.com/documentation/lightweightcoderequirements/validationresult): lightweight code requirement 테스트 결과를 나타내는 구조체입니다.
- [OnDiskCodeRequirement](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcoderequirement): 디스크 위 코드 파일을 평가할 때 사용하는 lightweight code requirement입니다.
- [allOf(requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/allof(requirement:)-2ocwl): 디스크 위 코드가 제공된 모든 제약을 만족하도록 요구하는 제약을 만듭니다.
- [anyOf(requirement:)](https://developer.apple.com/documentation/lightweightcoderequirements/anyof(requirement:)-71pff): 디스크 위 코드가 제공된 제약 중 어느 하나라도 만족하도록 요구하는 제약을 만듭니다.
- [OnDiskConstraint](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskconstraint): on-disk code requirement에서 사용할 수 있는 lightweight code requirement 제약이 준수하는 protocol입니다.
- [OnDiskCodeSigningFlags](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskcodesigningflags): 디스크 위 코드 파일의 code-signing flag를 테스트하는 제약입니다.
- [OnDiskConstraintBuilder](https://developer.apple.com/documentation/lightweightcoderequirements/ondiskconstraintbuilder): closure로부터 on-disk 제약을 구성하는 사용자 정의 parameter attribute입니다.
:::

:::topic-grid
## 실행 코드 속성 테스트
- [CodeDirectoryHash](https://developer.apple.com/documentation/lightweightcoderequirements/codedirectoryhash): 코드 파일 또는 실행 중이거나 시작 중인 프로세스의 code directory hash와 일치하는 제약입니다.
- [EntitlementsQuery](https://developer.apple.com/documentation/lightweightcoderequirements/entitlementsquery): 프로세스 또는 코드 파일과 연관된 entitlements dictionary의 값을 테스트하는 제약입니다.
- [InfoPlistHash](https://developer.apple.com/documentation/lightweightcoderequirements/infoplisthash): 프로세스나 코드 파일의 code signature에 저장된 Information property list hash와 지정된 hash를 비교하는 제약입니다.
- [IsInitProcess](https://developer.apple.com/documentation/lightweightcoderequirements/isinitprocess): 프로세스가 운영체제의 초기 프로세스인지 테스트하는 제약입니다.
- [IsMainBinary](https://developer.apple.com/documentation/lightweightcoderequirements/ismainbinary): 코드 파일이 main binary인지 테스트하는 제약입니다.
- [IsSIPProtected](https://developer.apple.com/documentation/lightweightcoderequirements/issipprotected): 코드 파일 또는 프로세스가 System Integrity Protection(SIP)으로 보호되는 volume 위에 있는지를 테스트하는 제약입니다.
- [PlatformType](https://developer.apple.com/documentation/lightweightcoderequirements/platformtype): 코드 파일 또는 실행 중인 프로세스가 지정된 플랫폼을 대상으로 하는지 테스트하는 제약입니다.
- [SigningIdentifier](https://developer.apple.com/documentation/lightweightcoderequirements/signingidentifier): 제공된 signing identifier가 코드에 부착된 signature와 일치하는지 테스트하는 제약입니다.
- [TeamIdentifier](https://developer.apple.com/documentation/lightweightcoderequirements/teamidentifier): 제공된 team identifier가 code signature에 식별된 team과 일치하는지 테스트하는 제약입니다.
- [ValidationCategory](https://developer.apple.com/documentation/lightweightcoderequirements/validationcategory): 코드 파일 또는 실행 중인 프로세스가 지정된 validation category에 맞게 서명되었는지 테스트하는 제약입니다.
:::

:::topic-grid
## 오류 처리
- [ConstraintError](https://developer.apple.com/documentation/lightweightcoderequirements/constrainterror): lightweight code requirement 루틴에서 던질 수 있는 오류 유형입니다.
:::
