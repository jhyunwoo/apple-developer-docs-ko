---
route: /documentation/AdAttributionKit
source_url: https://developer.apple.com/documentation/AdAttributionKit
source_locale: en-US
section: docc
content_type: symbol
title: AdAttributionKit
original_title: AdAttributionKit
source_hash: ceb7944b2ac964819b6ddc38846bfa8860428aa28a1a2e8d46dd6c7d8ceea29b
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:33:49+00:00'
last_translated_at: '2026-03-14T00:58:00+09:00'
---

# AdAttributionKit

App Store와 대체 앱 마켓플레이스의 인앱 광고에 대해 postback을 표시하고, 처리하고, 등록합니다.

## 개요

AdAttributionKit은 광고주가 광고 캠페인의 성공을 측정하도록 도우면서도 사용자 개인 정보 보호를 유지하도록 돕습니다.

이 API에는 세 가지 참여자가 있습니다.

- 광고에 서명하고 광고가 전환으로 이어진 뒤 postback을 받는 광고 네트워크
- 광고 네트워크의 광고를 표시하는 publisher 앱
- 사용자가 앱과 상호 작용할 때 conversion value를 업데이트하는 광고 대상 앱

광고 네트워크는 광고 네트워크 ID를 발급받고 API를 사용하기 위해 Apple에 등록합니다. 개발자는 앱이 광고 네트워크의 attribution 가능 광고를 수락하고, 당첨된 postback의 사본을 받을 수 있도록 설정합니다. 설정 정보는 [Registering an ad network](https://developer.apple.com/documentation/adattributionkit/registering-an-ad-network), [Configuring a publisher app](https://developer.apple.com/documentation/adattributionkit/configuring-a-publisher-app), [Configuring an advertised app](https://developer.apple.com/documentation/adattributionkit/configuring-an-advertised-app)을 참고하십시오.

아래는 광고 attribution에서 승리하는 광고 노출의 경로입니다. 광고 네트워크가 광고를 제공하고 앱이 이를 표시합니다. 사용자가 광고를 탭하고 광고 대상 앱을 다운로드하거나 다시 참여합니다. ![광고 노출이 승리하는 경로를 보여 주는 흐름도입니다. 도표는 사각형이 들어 있는 두 개의 가로 구역으로 이루어져 있습니다. 위쪽 구역은 Server, 아래쪽은 Device로 표시됩니다. 흐름은 왼쪽 위의 `Ad network serves ad` 사각형에서 시작합니다. 여기서 화살표가 아래쪽 `App presents ad` 사각형으로 향하고, 다시 `Download or reengagement` 사각형으로 이어집니다. 세 번째 사각형 오른쪽에는 점선이 위쪽 구역의 `Apple ensures crowd anonymity` 사각형으로 연결되고, 그 바로 아래 화살표는 인접한 `Person interacts with advertised app` 사각형으로 이어집니다. `Apple ensures crowd anonymity` 사각형에서 아래쪽 `Person interacts with advertised app` 사각형으로는 `Postback data tier`라고 표시된 점선이 내려갑니다. 이어서 `Person interacts with advertised app` 사각형에서 오른쪽 `Multiple conversions` 사각형으로 화살표가 이어지며, 이 안에는 `Postback 1`, `Postback 2`, `Postback 3` 하위 사각형이 있습니다. 각 하위 사각형은 위쪽 구역의 `Ad Network (winning)`과 `Developer` 하위 사각형이 들어 있는 사각형으로 연결됩니다.](https://developer.apple.com)

Apple은 전환에 대한 postback data tier를 결정하고, 기기는 나중에 이 tier를 사용해 crowd anonymity를 보장할 수 있도록 postback에 어느 정도의 세부 정보를 포함할 수 있을지 결정합니다. postback 내용과 data tier에 대한 자세한 내용은 [Receiving postbacks in multiple conversion windows](https://developer.apple.com/documentation/adattributionkit/receiving-postbacks-in-multiple-conversion-windows)를 참고하십시오.

사용자가 attribution 시간 창 안에 앱을 실행하면 해당 광고 노출은 postback 대상이 됩니다. 사용자가 앱과 상호 작용함에 따라 앱은 conversion value를 업데이트합니다. 광고 네트워크가 전환 기준을 충족하면 시스템은 세 개의 conversion window를 제공합니다. 시스템은 광고 네트워크에 postback을 보내고, 개발자가 수신을 선택한 경우 앱 개발자에게도 이를 보냅니다.

기기는 광고에 서명한 여러 광고 네트워크로 postback을 보냅니다.

- 하나의 광고 네트워크는 광고 attribution에서 승리한 광고 노출에 대해 `did-win` 매개변수 값이 `true`인 postback을 여러 conversion window에 걸쳐 받습니다.
- 설치 전환의 경우 attribution 자격을 충족했지만 승리하지 못한 광고 노출이라면 최대 5개의 다른 광고 네트워크가 `did-win` 값이 `false`인 postback을 받습니다.
- 재참여 전환의 경우 하나의 광고 네트워크가 여러 conversion window에 걸쳐 승리한 postback을 받을 수 있습니다. 이 프레임워크는 재참여에 대해서는 runner-up postback을 생성하지 않습니다.

다음 그림은 광고 attribution 자격은 얻었지만 승리하지 못한 광고 노출의 경로를 보여 줍니다. 최대 5개의 광고 네트워크가 하나의 비승리 postback을 받습니다.

![광고 노출이 승리하지 못한 경로를 보여 주는 흐름도입니다. 도표는 사각형이 들어 있는 두 개의 가로 구역으로 이루어져 있습니다. 위쪽 구역은 Server, 아래쪽은 Device로 표시됩니다. 흐름은 왼쪽 위의 `Ad network serves ad` 사각형에서 시작합니다. 여기서 화살표가 아래쪽 `App presents ad` 사각형으로 향하고, 다시 `Download or reengagement` 사각형으로 이어집니다. 세 번째 사각형 오른쪽에는 점선이 위쪽 구역의 `Apple ensures crowd anonymity` 사각형으로 연결되고, 그 바로 아래 화살표는 인접한 `Person interacts with advertised app` 사각형으로 이어집니다. `Apple ensures crowd anonymity` 사각형에서 아래쪽 `Person interacts with advertised app` 사각형으로는 `Postback data tier`라고 표시된 점선이 내려갑니다. 이어서 `Person interacts with advertised app` 사각형에서 오른쪽 `Postback` 사각형으로 화살표가 이어지며, 이 안에는 `Nonwinning postbacks`라고 표시된 사각형 더미가 있습니다. 이 사각형들은 위쪽 구역의 `Ad Networks (nonwinning)`이라 표시된 여러 사각형 더미로 연결됩니다.](https://developer.apple.com)

시간 창 세부 사항, 설치 및 재참여 전환 정보, 기타 제약을 포함해 광고 attribution 수신에 대한 자세한 내용은 [Receiving ad attributions and postbacks](https://developer.apple.com/documentation/adattributionkit/receiving-ad-attributions-and-postbacks)를 참고하십시오. Apple이 암호학적으로 서명하는 postback 정보에는 사용자별 또는 기기별 데이터가 포함되지 않습니다. Apple이 정한 개인정보 보호 임계값을 충족하는 경우에는 광고 네트워크와 광고 대상 앱의 값이 포함될 수 있습니다. postback 값과 postback data tier에 대한 자세한 내용은 [Receiving postbacks in multiple conversion windows](https://developer.apple.com/documentation/adattributionkit/receiving-postbacks-in-multiple-conversion-windows)를 참고하십시오. postback 내용에 대한 자세한 내용은 [Verifying a postback](https://developer.apple.com/documentation/adattributionkit/verifying-a-postback)을 참고하십시오.

### 광고를 표시하고, conversion value를 업데이트하고, attribution을 수신하기

각 참여자는 광고를 표시하고 attribution을 수신하기 위해 API를 사용할 때 특정 책임을 집니다.

광고 네트워크의 책임은 다음과 같습니다.

- 등록하고 개발자에게 광고 네트워크 식별자를 제공합니다. [Registering an ad network](https://developer.apple.com/documentation/adattributionkit/registering-an-ad-network)를 참고하십시오.
- publisher 앱에 서명된 광고를 제공합니다. [Presenting ads in your app](https://developer.apple.com/documentation/adattributionkit/presenting-ads-in-your-app)을 참고하십시오.
- 등록 중 설정한 URL에서 postback을 수신합니다.
- postback을 검증합니다. [Verifying a postback](https://developer.apple.com/documentation/adattributionkit/verifying-a-postback)을 참고하십시오.

publisher 앱의 책임은 다음과 같습니다.

- 정보 property list에 광고 네트워크 식별자를 추가합니다. [Configuring a publisher app](https://developer.apple.com/documentation/adattributionkit/configuring-a-publisher-app)을 참고하십시오.
- 광고 네트워크가 서명한 광고를 표시합니다. [Presenting ads in your app](https://developer.apple.com/documentation/adattributionkit/presenting-ads-in-your-app)을 참고하십시오.

광고 대상 앱의 책임은 다음과 같습니다.

- 사용자가 앱을 처음 실행할 때 [updateConversionValue(_:lockPostback:)](https://developer.apple.com/documentation/adattributionkit/postback/updateconversionvalue(_:lockpostback:)) 같은 conversion 업데이트 메서드 중 하나를 호출해 conversion value를 갱신함으로써 전환을 등록합니다.
- 선택적으로, 사용자가 앱과 상호 작용하는 동안 [updateConversionValue(_:coarseConversionValue:lockPostback:)](https://developer.apple.com/documentation/adattributionkit/postback/updateconversionvalue(_:coarseconversionvalue:lockpostback:)) 같은 conversion 업데이트 메서드 중 하나를 호출해 conversion value를 계속 업데이트합니다.
- 선택적으로, 당첨된 postback 사본을 받기 위해 정보 property list에 서버 URL을 지정합니다. [Configuring an advertised app](https://developer.apple.com/documentation/adattributionkit/configuring-an-advertised-app)을 참고하십시오.

Apple은 사용자 개인 정보를 보호하도록 돕기 위해 광고 attribution API를 설계했습니다. 앱은 ad attribution API를 호출하기 전에 [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency)를 사용할 필요가 없으며, 추적 권한 상태와 관계없이 이 API를 호출할 수 있습니다. 개인정보 보호에 대한 자세한 내용은 [User privacy and data use](https://developer.apple.com/app-store/user-privacy-and-data-use/)를 참고하십시오.

:::topic-grid
## 핵심 사항
- [Understanding AdAttributionKit and SKAdNetwork interoperability](https://developer.apple.com/documentation/adattributionkit/adattributionkit-skadnetwork-interoperability): attribution API가 어떻게 상호 작용해 광고 노출을 전달하는지 알아봅니다.
- [Presenting ads in your app](https://developer.apple.com/documentation/adattributionkit/presenting-ads-in-your-app): 앱 안에서 서로 다른 광고 스타일을 렌더링합니다.
- [Receiving ad attributions and postbacks](https://developer.apple.com/documentation/adattributionkit/receiving-ad-attributions-and-postbacks): 광고 attribution으로 이어지는 광고 노출의 시간 범위와 우선순위, 그리고 노출이 postback 자격을 얻는 방식을 이해합니다.
- [Identifying conversion values with conversion tags](https://developer.apple.com/documentation/adattributionkit/conversion-tags): conversion window가 겹칠 때 특정 postback을 식별하고 업데이트하기 위해 conversion tag를 사용합니다.
:::

:::topic-grid
## 광고 네트워크 등록 및 구성
- [Registering an ad network](https://developer.apple.com/documentation/adattributionkit/registering-an-ad-network): 광고 네트워크를 Apple에 등록한 후 AdAttributionKit API를 광고 캠페인에 사용합니다.
- [Configuring a publisher app](https://developer.apple.com/documentation/adattributionkit/configuring-a-publisher-app): 광고 캠페인에 참여할 publisher 앱을 설정합니다.
- [Configuring an advertised app](https://developer.apple.com/documentation/adattributionkit/configuring-an-advertised-app): 광고 캠페인에 참여할 광고 대상 앱을 준비합니다.
- [Configuring attribution rules for your app](https://developer.apple.com/documentation/adattributionkit/configuring-attribution-rules-for-your-app): 노출 등록에 허용되는 시간과 앱이 받아들일 최소 전환 시간 등 attribution 흐름 요소를 조정합니다.
:::

:::topic-grid
## 광고 attribution 테스트
- [Testing ad attributions with Developer Mode](https://developer.apple.com/documentation/adattributionkit/testing-adattributionkit-with-developer-mode): 광고 attribution 시간 창을 줄이고 프록시를 사용해 테스트 중 postback을 검사합니다.
- [Creating postbacks in developer settings](https://developer.apple.com/documentation/adattributionkit/creating-postbacks-in-developer-settings): publisher 앱의 광고와 상호 작용하지 않고도 광고 대상 앱용 개발 postback을 테스트합니다.
- [Testing ad attributions with a downloaded profile](https://developer.apple.com/documentation/adattributionkit/testing-ad-attributions-with-a-downloaded-profile): 광고 attribution 시간 창을 줄이고 프록시를 사용해 테스트 중 postback을 검사합니다.
:::

:::topic-grid
## 서명
- [Generating JWS impressions](https://developer.apple.com/documentation/adattributionkit/generating-jws-impressions): AdAttributionKit의 앱 노출에 사용할 JSON Web Signature(JWS)를 생성합니다.
:::

:::topic-grid
## 앱 노출
- [AppImpression](https://developer.apple.com/documentation/adattributionkit/appimpression): 앱 안의 광고와 사용자가 상호 작용한 뒤 생성하는 attribution 가능한 노출을 나타내는 구조체입니다.
:::

:::topic-grid
## Postback
- [Postback](https://developer.apple.com/documentation/adattributionkit/postback): 광고 attribution의 conversion value를 업데이트할 때 사용하는 메서드를 제공하는 구조체입니다.
- [PostbackUpdate](https://developer.apple.com/documentation/adattributionkit/postbackupdate): conversion value 같은 postback 속성을 업데이트할 때 사용하는 값입니다.
- [CoarseConversionValue](https://developer.apple.com/documentation/adattributionkit/coarseconversionvalue): 개발자가 정의한 상대적 attribution conversion value를 설명하는 값입니다.
:::

:::topic-grid
## Postback 검증 및 매개변수 식별
- [Verifying a postback](https://developer.apple.com/documentation/adattributionkit/verifying-a-postback): 광고 전환 후 받은 postback의 암호 서명을 검증해 유효성을 확인합니다.
- [Identifying the parameters in a postback](https://developer.apple.com/documentation/adattributionkit/identifying-the-parameters-in-a-postback): attribution 보고서를 이해할 수 있도록 postback 속성을 해석합니다.
:::

:::topic-grid
## 오류
- [AdAttributionKitError](https://developer.apple.com/documentation/adattributionkit/adattributionkiterror): 광고 attribution 오류 조건을 설명하는 값입니다.
:::

:::topic-grid
## 문서
- [Receiving postbacks in multiple conversion windows](https://developer.apple.com/documentation/adattributionkit/receiving-postbacks-in-multiple-conversion-windows): 각 conversion window에서 postback이 포함할 수 있는 데이터를 알아봅니다.
:::
