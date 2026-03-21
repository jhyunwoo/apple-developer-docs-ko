---
route: /documentation/WiFiInfrastructure
source_url: https://developer.apple.com/documentation/WiFiInfrastructure
source_locale: en-US
section: docc
content_type: symbol
title: Wi-Fi Infrastructure
original_title: Wi-Fi Infrastructure
source_hash: 3f08c9f06c7fdf46ced78eb48e3ad7058ac92d754f303f9c4c38b8eb145e7fa9
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:54:04+00:00'
last_translated_at: '2026-03-14T02:30:00+09:00'
---

# Wi-Fi Infrastructure

기기와 연결된 액세서리 사이에서 Wi-Fi 네트워크 자격 증명을 안전하게 공유합니다.

## 개요

[AccessorySetupKit](https://developer.apple.com/documentation/accessorysetupkit/)으로 액세서리를 페어링한 companion app은 Wi-Fi Infrastructure 프레임워크를 사용해 로컬 Bluetooth 4.2 Secure 연결을 통해 페어링된 액세서리와 네트워크를 공유할 수 있습니다.

Wi-Fi Infrastructure 프레임워크는 앱이 iOS 기기에서 페어링된 액세서리로 Wi-Fi 네트워크 자격 증명을 자동으로 안전하게 공유할 수 있게 합니다. 이 프레임워크를 사용하면 smartwatch, Internet of Things(IoT) 기기, 또는 서로 다른 네트워크를 따라 이동하는 기타 연결 하드웨어처럼 입력 기능이 제한된 액세서리에서 네트워크 암호를 수동으로 입력할 필요를 줄일 수 있습니다.

이 프레임워크는 개인 정보 보호와 사용자 선택을 존중하는 안전한 암호화 공유 메커니즘을 제공합니다. 사람들은 자동 네트워크 공유부터 네트워크별 수동 승인까지 여러 수준의 공유 권한을 부여할 수 있습니다. 모든 네트워크 공유는 액세서리가 Bluetooth를 통해 연결되었을 때만 발생하므로, 사용자가 공유하는 자격 증명은 기기들이 실제로 함께 있을 때에만 공유됩니다.

Wi-Fi Infrastructure 프레임워크를 사용하면 다음 작업을 수행할 수 있습니다.

- 페어링된 액세서리와 Wi-Fi 네트워크를 공유하기 위한 권한 요청
- iOS 기기가 네트워크에 연결될 때 자동으로 네트워크 공유
- 특정 네트워크를 액세서리와 공유하도록 앱을 통해 사용자에게 요청
- app extension에서 공유된 네트워크 자격 증명 수신
- 시스템이 제공하는 네트워크 선택기 인터페이스 표시
- 네트워크 공유 실패 처리 및 대체 네트워크로 재시도

:::important Important
Wi-Fi Infrastructure 앱은 모든 지역의 기기에서 개발하고 테스트할 수 있습니다. 하지만 앱 사용자는 유럽 연합(EU)에 등록된 계정을 가지고 있어야 하며, 해당 기기도 EU 내에 있어야 합니다.
:::

:::topic-grid
## 기초
- [com.apple.developer.wifi-infrastructure](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.wifi-infrastructure): 앱이 Wi-Fi Infrastructure 프레임워크를 사용하기 위해 시스템이 요구하는 entitlement입니다.
- [Sharing Wi-Fi network credentials](https://developer.apple.com/documentation/wifiinfrastructure/sharing-wi-fi-network-credentials): Bluetooth 연결을 설정한 뒤 Wi-Fi Infrastructure를 사용해 Wi-Fi 네트워크 자격 증명을 자동으로 공유합니다.
:::

:::topic-grid
## 네트워크 공유
- [WINetworkSharingController](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingcontroller): container app이 연결된 액세서리와의 네트워크 공유 기능을 제어할 수 있게 하는 controller입니다.
- [WINetworkSharingProvider](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider): 업데이트된 Wi-Fi 네트워크 정보를 app extension에 전달하는 provider입니다.
- [WINetworkSharingAskToShareState](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingasktosharestate): 현재 Wi-Fi 네트워크를 액세서리와 공유하기 위한 권한 상태입니다.
:::

:::topic-grid
## 공통 데이터
- [WISSID](https://developer.apple.com/documentation/wifiinfrastructure/wissid): 애플리케이션이 사람이 읽을 수 있는 네트워크 이름을 파생하는 데 사용하는 Wi-Fi 네트워크의 Service Set Identifier(SSID)입니다.
- [WIChannel](https://developer.apple.com/documentation/wifiinfrastructure/wichannel): WiFi 채널입니다.
- [WIMACAddress](https://developer.apple.com/documentation/wifiinfrastructure/wimacaddress): Wi-Fi MAC 주소입니다.
:::

:::topic-grid
## 오류
- [WINetworkSharingError](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingerror): Wi-Fi 네트워크 공유 기능에 대한 오류 코드입니다.
:::
