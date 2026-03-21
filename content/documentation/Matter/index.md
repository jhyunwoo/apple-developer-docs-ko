---
route: /documentation/Matter
source_url: https://developer.apple.com/documentation/Matter
source_locale: en-US
section: docc
content_type: symbol
title: Matter
original_title: Matter
source_hash: 6c6c063d26fc5bcc6da6a3969499e88b10cacf0319e0752a08a894374b453f67
canonical_source: manual-translation
last_crawled_at: '2026-03-13T07:44:22+00:00'
last_translated_at: '2026-03-13T15:20:00+09:00'
---

# Matter

다양한 제조업체의 스마트 홈 기기와 통신하고 이를 제어합니다.

## 개요

[Matter](https://csa-iot.org/all-solutions/matter/) 스마트 홈 연결 표준은 다양한 스마트 홈 기기와 생태계 간 상호 운용성을 가능하게 합니다. [MatterSupport](https://developer.apple.com/documentation/MatterSupport)를 사용해 액세서리를 로컬 네트워크에 연결한 다음, Matter를 사용해 해당 액세서리를 커미셔닝하고 제어하십시오.

![가정 내에서 Matter 기기와 비 Matter 기기 간 통신을 보여 주는 다이어그램입니다. 중앙에는 Matter를 지원하는 iOS 기기가 있으며, 왼쪽의 Matter 차고문 컨트롤러와 오른쪽의 Matter 조명 스위치에 연결됩니다. Matter 조명 스위치는 Matter 램프 컨트롤러에 연결됩니다. 다이어그램에는 비 Matter 기기인 콘센트 스위치, HomePod, Apple TV도 포함되어 있습니다.](https://developer.apple.com)

네트워크에서 Matter 액세서리에 접근하려면 먼저 이를 커미셔닝해야 합니다. 커미셔닝은 보안 통신을 가능하게 하는 자격 증명을 제공하고 초기 액세서리 구성을 수행합니다. 액세서리를 커미셔닝하면 이를 제어하는 데 사용하는 기능 영역인 cluster가 노출됩니다. 예를 들어 조명은 켜짐 여부를 제어하기 위해 On/Off cluster를 노출합니다. 밝기 조절이 가능한 조명은 밝기를 제어하기 위해 Level Control cluster도 함께 노출합니다.

:::topic-grid
## Matter device onboarding
- [Onboarding a Matter device](https://developer.apple.com/documentation/matter/onboarding-a-matter-device): Matter 기기를 검색하고 제어할 수 있도록 앱을 준비합니다.
:::

:::topic-grid
## Matter device interactions
- [Controller initialization](https://developer.apple.com/documentation/matter/controller-initialization): Matter 액세서리를 제어하는 객체를 초기화합니다.
- [Accessory commissioning](https://developer.apple.com/documentation/matter/accessory-commissioning): Matter 액세서리를 네트워크에 커미셔닝합니다.
- [Accessory control](https://developer.apple.com/documentation/matter/accessory-control): 커미셔닝된 Matter 액세서리와 통신합니다.
- [Clusters](https://developer.apple.com/documentation/matter/clusters): Matter 액세서리가 노출하는 관련 기능 그룹과 상호 작용합니다.
:::

:::topic-grid
## Reference
- [Other symbols](https://developer.apple.com/documentation/matter/other-symbols)
- [Matter Constants](https://developer.apple.com/documentation/matter/matter-constants)
- [Matter Functions](https://developer.apple.com/documentation/matter/matter-functions)
:::

:::topic-grid
## Classes
- [MTRAccessControlClusterAccessRestrictionEntryStruct](https://developer.apple.com/documentation/matter/mtraccesscontrolclusteraccessrestrictionentrystruct)
- [MTRAccessControlClusterAccessRestrictionStruct](https://developer.apple.com/documentation/matter/mtraccesscontrolclusteraccessrestrictionstruct)
- [MTRAccessControlClusterCommissioningAccessRestrictionEntryStruct](https://developer.apple.com/documentation/matter/mtraccesscontrolclustercommissioningaccessrestrictionentrystruct)
- [MTRAccessControlClusterFabricRestrictionReviewUpdateEvent](https://developer.apple.com/documentation/matter/mtraccesscontrolclusterfabricrestrictionreviewupdateevent)
- [MTRAccessControlClusterReviewFabricRestrictionsParams](https://developer.apple.com/documentation/matter/mtraccesscontrolclusterreviewfabricrestrictionsparams)
- [MTRAccessControlClusterReviewFabricRestrictionsResponseParams](https://developer.apple.com/documentation/matter/mtraccesscontrolclusterreviewfabricrestrictionsresponseparams)
- [MTRAccountLoginClusterLoggedOutEvent](https://developer.apple.com/documentation/matter/mtraccountloginclusterloggedoutevent)
- [MTRAttributeValueWaiter](https://developer.apple.com/documentation/matter/mtrattributevaluewaiter)
- [MTRBaseClusterCommissionerControl](https://developer.apple.com/documentation/matter/mtrbaseclustercommissionercontrol): Cluster Commissioner Control
- [MTRBaseClusterContentAppObserver](https://developer.apple.com/documentation/matter/mtrbaseclustercontentappobserver): Cluster Content App Observer
- [MTRBaseClusterDeviceEnergyManagement](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagement): Cluster Device Energy Management
- [MTRBaseClusterDeviceEnergyManagementMode](https://developer.apple.com/documentation/matter/mtrbaseclusterdeviceenergymanagementmode): Cluster Device Energy Management Mode
- [MTRBaseClusterDishwasherAlarm](https://developer.apple.com/documentation/matter/mtrbaseclusterdishwasheralarm): Cluster Dishwasher Alarm
- [MTRBaseClusterDishwasherMode](https://developer.apple.com/documentation/matter/mtrbaseclusterdishwashermode): Cluster Dishwasher Mode
- [MTRBaseClusterEnergyEVSE](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevse): Cluster Energy EVSE
- [MTRBaseClusterEnergyEVSEMode](https://developer.apple.com/documentation/matter/mtrbaseclusterenergyevsemode): Cluster Energy EVSE Mode
- [MTRBaseClusterICDManagement](https://developer.apple.com/documentation/matter/mtrbaseclustericdmanagement): Cluster ICD Management
- [MTRBaseClusterLaundryDryerControls](https://developer.apple.com/documentation/matter/mtrbaseclusterlaundrydryercontrols): Cluster Laundry Dryer Controls
- [MTRBaseClusterLaundryWasherControls](https://developer.apple.com/documentation/matter/mtrbaseclusterlaundrywashercontrols): Cluster Laundry Washer Controls
- [MTRBaseClusterLaundryWasherMode](https://developer.apple.com/documentation/matter/mtrbaseclusterlaundrywashermode): Cluster Laundry Washer Mode
- [MTRBaseClusterMessages](https://developer.apple.com/documentation/matter/mtrbaseclustermessages): Cluster Messages
- [MTRBaseClusterMicrowaveOvenControl](https://developer.apple.com/documentation/matter/mtrbaseclustermicrowaveovencontrol): Cluster Microwave Oven Control
- [MTRBaseClusterMicrowaveOvenMode](https://developer.apple.com/documentation/matter/mtrbaseclustermicrowaveovenmode): Cluster Microwave Oven Mode
- [MTRBaseClusterOvenCavityOperationalState](https://developer.apple.com/documentation/matter/mtrbaseclusterovencavityoperationalstate): Cluster Oven Cavity Operational State
- [MTRBaseClusterOvenMode](https://developer.apple.com/documentation/matter/mtrbaseclusterovenmode): Cluster Oven Mode
- [MTRBaseClusterPowerTopology](https://developer.apple.com/documentation/matter/mtrbaseclusterpowertopology): Cluster Power Topology
- [MTRBaseClusterRefrigeratorAlarm](https://developer.apple.com/documentation/matter/mtrbaseclusterrefrigeratoralarm): Cluster Refrigerator Alarm
- [MTRBaseClusterRefrigeratorAndTemperatureControlledCabinetMode](https://developer.apple.com/documentation/matter/mtrbaseclusterrefrigeratorandtemperaturecontrolledcabinetmode): Cluster Refrigerator And Temperature Controlled Cabinet Mode
- [MTRBaseClusterServiceArea](https://developer.apple.com/documentation/matter/mtrbaseclusterservicearea): Cluster Service Area
- [MTRBaseClusterTemperatureControl](https://developer.apple.com/documentation/matter/mtrbaseclustertemperaturecontrol): Cluster Temperature Control
- [MTRBaseClusterThreadBorderRouterManagement](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadborderroutermanagement): Cluster Thread Border Router Management
- [MTRBaseClusterThreadNetworkDirectory](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadnetworkdirectory): Cluster Thread Network Directory
- [MTRBaseClusterTimeSynchronization](https://developer.apple.com/documentation/matter/mtrbaseclustertimesynchronization): Cluster Time Synchronization
- [MTRBaseClusterWaterHeaterManagement](https://developer.apple.com/documentation/matter/mtrbaseclusterwaterheatermanagement): Cluster Water Heater Management
- [MTRBaseClusterWaterHeaterMode](https://developer.apple.com/documentation/matter/mtrbaseclusterwaterheatermode): Cluster Water Heater Mode
- [MTRBaseClusterWiFiNetworkManagement](https://developer.apple.com/documentation/matter/mtrbaseclusterwifinetworkmanagement): Cluster Wi-Fi Network Management
- [MTRBridgedDeviceBasicInformationClusterActiveChangedEvent](https://developer.apple.com/documentation/matter/mtrbridgeddevicebasicinformationclusteractivechangedevent)
- [MTRBridgedDeviceBasicInformationClusterKeepActiveParams](https://developer.apple.com/documentation/matter/mtrbridgeddevicebasicinformationclusterkeepactiveparams)
- [MTRChannelClusterCancelRecordProgramParams](https://developer.apple.com/documentation/matter/mtrchannelclustercancelrecordprogramparams)
- [MTRChannelClusterChannelPagingStruct](https://developer.apple.com/documentation/matter/mtrchannelclusterchannelpagingstruct)
- [MTRChannelClusterGetProgramGuideParams](https://developer.apple.com/documentation/matter/mtrchannelclustergetprogramguideparams)
- [MTRChannelClusterPageTokenStruct](https://developer.apple.com/documentation/matter/mtrchannelclusterpagetokenstruct)
- [MTRChannelClusterProgramCastStruct](https://developer.apple.com/documentation/matter/mtrchannelclusterprogramcaststruct)
- [MTRChannelClusterProgramCategoryStruct](https://developer.apple.com/documentation/matter/mtrchannelclusterprogramcategorystruct)
- [MTRChannelClusterProgramGuideResponseParams](https://developer.apple.com/documentation/matter/mtrchannelclusterprogramguideresponseparams)
- [MTRChannelClusterProgramStruct](https://developer.apple.com/documentation/matter/mtrchannelclusterprogramstruct)
- [MTRChannelClusterRecordProgramParams](https://developer.apple.com/documentation/matter/mtrchannelclusterrecordprogramparams)
- [MTRChannelClusterSeriesInfoStruct](https://developer.apple.com/documentation/matter/mtrchannelclusterseriesinfostruct)
- [MTRClusterCommissionerControl](https://developer.apple.com/documentation/matter/mtrclustercommissionercontrol): Cluster Commissioner Control. 클라이언트가 자신 또는 다른 노드를 클러스터 서버가 커미셔닝할 수 있는 fabric에 커미셔닝해 달라고 요청하는 기능을 지원합니다.
- [MTRClusterContentAppObserver](https://developer.apple.com/documentation/matter/mtrclustercontentappobserver): Cluster Content App Observer. 이 cluster는 Streaming Media Player, Smart TV, Smart Screen과 같은 Video Player 기기의 Content App Observer에 대상 지정 명령을 보내기 위한 인터페이스를 제공합니다. Content App Observer용 cluster server는 Casting Video Client와 같이 Content App과 통신하는 endpoint에서 구현됩니다. Content App Observer용 cluster client는 Content App endpoint에서 구현됩니다. Content App에 binding이 설정되면 Content App은 Observer의 NodeId를 전달받습니다. 그러면 Content App은 Observer(server cluster)로 ContentAppMessage를 보낼 수 있고, Observer는 ContentAppMessageResponse로 응답합니다.
- [MTRClusterDeviceEnergyManagement](https://developer.apple.com/documentation/matter/mtrclusterdeviceenergymanagement): Cluster Device Energy Management. 이 cluster를 사용하면 클라이언트가 기기의 전력 사용량을 관리할 수 있습니다. 이러한 클라이언트의 예로는 Energy Smart Appliance(ESA)를 제어하는 Energy Management System(EMS)이 있습니다.
- [MTRClusterDeviceEnergyManagementMode](https://developer.apple.com/documentation/matter/mtrclusterdeviceenergymanagementmode): Cluster Device Energy Management Mode. 지원되는 옵션 목록에서 모드를 선택하기 위한 attribute와 command를 제공합니다.
- [MTRClusterDishwasherAlarm](https://developer.apple.com/documentation/matter/mtrclusterdishwasheralarm): Cluster Dishwasher Alarm. 식기세척기 알람을 구성하기 위한 attribute와 command를 제공합니다.
- [MTRClusterDishwasherMode](https://developer.apple.com/documentation/matter/mtrclusterdishwashermode): Cluster Dishwasher Mode. 지원되는 옵션 목록에서 모드를 선택하기 위한 attribute와 command를 제공합니다.
- [MTRClusterEnergyEVSE](https://developer.apple.com/documentation/matter/mtrclusterenergyevse): Cluster Energy EVSE. Electric Vehicle Supply Equipment(EVSE)는 전기차(EV) 또는 플러그인 하이브리드 전기차를 충전하는 데 사용하는 장비입니다. 이 cluster는 Electric Vehicle Supply Equipment(EVSE) 관리 기능을 위한 인터페이스를 제공합니다.
- [MTRClusterEnergyEVSEMode](https://developer.apple.com/documentation/matter/mtrclusterenergyevsemode): Cluster Energy EVSE Mode. 지원되는 옵션 목록에서 모드를 선택하기 위한 attribute와 command를 제공합니다.
- [MTRClusterICDManagement](https://developer.apple.com/documentation/matter/mtrclustericdmanagement): Cluster ICD Management. 서버가 통신 가능해졌을 때 나열된 클라이언트에 알림이 전달되도록 보장할 수 있게 합니다.
- [MTRClusterLaundryDryerControls](https://developer.apple.com/documentation/matter/mtrclusterlaundrydryercontrols): Cluster Laundry Dryer Controls. 이 cluster는 의류 건조기 device type 동작과 관련된 옵션에 접근하는 방법을 제공합니다.
- [MTRClusterLaundryWasherControls](https://developer.apple.com/documentation/matter/mtrclusterlaundrywashercontrols): Cluster Laundry Washer Controls. 이 cluster는 세탁기와 같은 세탁 기기에서 제공되는 여러 기능 유형을 원격으로 모니터링하고 제어하는 기능을 지원합니다.
- [MTRClusterLaundryWasherMode](https://developer.apple.com/documentation/matter/mtrclusterlaundrywashermode): Cluster Laundry Washer Mode. 지원되는 옵션 목록에서 모드를 선택하기 위한 attribute와 command를 제공합니다.
- [MTRClusterMessages](https://developer.apple.com/documentation/matter/mtrclustermessages): Cluster Messages. 이 cluster는 기기가 표시할 메시지를 전달하기 위한 인터페이스를 제공합니다.
- [MTRClusterMicrowaveOvenControl](https://developer.apple.com/documentation/matter/mtrclustermicrowaveovencontrol): Cluster Microwave Oven Control. 전자레인지 제어를 구성하고 조리 통계를 보고하기 위한 attribute와 command를 제공합니다.
- [MTRClusterMicrowaveOvenMode](https://developer.apple.com/documentation/matter/mtrclustermicrowaveovenmode): Cluster Microwave Oven Mode. 지원되는 옵션 목록에서 모드를 선택하기 위한 attribute와 command를 제공합니다.
- [MTRClusterOvenCavityOperationalState](https://developer.apple.com/documentation/matter/mtrclusterovencavityoperationalstate): Cluster Oven Cavity Operational State. 이 cluster는 오븐의 작동 상태를 원격으로 모니터링하고, 지원되는 경우 해당 상태를 변경하는 기능을 지원합니다.
- [MTRClusterOvenMode](https://developer.apple.com/documentation/matter/mtrclusterovenmode): Cluster Oven Mode. 지원되는 옵션 목록에서 모드를 선택하기 위한 attribute와 command를 제공합니다.
- [MTRClusterPowerTopology](https://developer.apple.com/documentation/matter/mtrclusterpowertopology): Cluster Power Topology. Power Topology Cluster는 endpoint 간 전력이 어떻게 흐르는지 표현하는 메커니즘을 제공합니다.
- [MTRClusterRefrigeratorAlarm](https://developer.apple.com/documentation/matter/mtrclusterrefrigeratoralarm): Cluster Refrigerator Alarm. 냉장고 알람을 구성하기 위한 attribute와 command를 제공합니다.
- [MTRClusterRefrigeratorAndTemperatureControlledCabinetMode](https://developer.apple.com/documentation/matter/mtrclusterrefrigeratorandtemperaturecontrolledcabinetmode): Cluster Refrigerator And Temperature Controlled Cabinet Mode. 지원되는 옵션 목록에서 모드를 선택하기 위한 attribute와 command를 제공합니다.
- [MTRClusterServiceArea](https://developer.apple.com/documentation/matter/mtrclusterservicearea): Cluster Service Area. Service Area cluster는 기기가 동작해야 하는 영역을 제어하고, 현재 서비스 중인 영역을 질의하기 위한 인터페이스를 제공합니다.
- [MTRClusterTemperatureControl](https://developer.apple.com/documentation/matter/mtrclustertemperaturecontrol): Cluster Temperature Control. 온도 제어를 구성하고 온도를 보고하기 위한 attribute와 command를 제공합니다.
- [MTRClusterThreadBorderRouterManagement](https://developer.apple.com/documentation/matter/mtrclusterthreadborderroutermanagement): Cluster Thread Border Router Management. Thread Border Router의 Thread 네트워크를 관리합니다.
- [MTRClusterThreadNetworkDirectory](https://developer.apple.com/documentation/matter/mtrclusterthreadnetworkdirectory): Cluster Thread Network Directory. 사용자에게 표시되는 Thread 네트워크의 이름과 자격 증명을 관리합니다.
- [MTRClusterTimeSynchronization](https://developer.apple.com/documentation/matter/mtrclustertimesynchronization): Cluster Time Synchronization. 정확한 시간은 일정 관리, 표시, 보안 자료 검증 등 여러 이유로 필요합니다.
- [MTRClusterWaterHeaterManagement](https://developer.apple.com/documentation/matter/mtrclusterwaterheatermanagement): Cluster Water Heater Management. 이 cluster는 클라이언트가 온수 가열 기기의 동작을 제어해 에너지 관리와 함께 사용할 수 있도록 하기 위해 사용됩니다.
- [MTRClusterWaterHeaterMode](https://developer.apple.com/documentation/matter/mtrclusterwaterheatermode): Cluster Water Heater Mode. 지원되는 옵션 목록에서 모드를 선택하기 위한 attribute와 command를 제공합니다.
- [MTRClusterWiFiNetworkManagement](https://developer.apple.com/documentation/matter/mtrclusterwifinetworkmanagement): Cluster Wi-Fi Network Management. 관리되는 Wi-Fi 네트워크에 관한 운영 정보를 가져오는 기능입니다.
- [MTRCommandWithRequiredResponse](https://developer.apple.com/documentation/matter/mtrcommandwithrequiredresponse): 호출할 단일 command와, 해당 호출을 성공으로 간주하기 위해 필요한 response를 나타내는 객체입니다.
- [MTRCommissioneeInfo](https://developer.apple.com/documentation/matter/mtrcommissioneeinfo): 커미셔닝 중 commissionee 기기에서 읽어 온 정보입니다.
- [MTRCommissionerControlClusterCommissionNodeParams](https://developer.apple.com/documentation/matter/mtrcommissionercontrolclustercommissionnodeparams)
- [MTRCommissionerControlClusterCommissioningRequestResultEvent](https://developer.apple.com/documentation/matter/mtrcommissionercontrolclustercommissioningrequestresultevent)
- [MTRCommissionerControlClusterRequestCommissioningApprovalParams](https://developer.apple.com/documentation/matter/mtrcommissionercontrolclusterrequestcommissioningapprovalparams)
- [MTRCommissionerControlClusterReverseOpenCommissioningWindowParams](https://developer.apple.com/documentation/matter/mtrcommissionercontrolclusterreverseopencommissioningwindowparams)
- [MTRCommissioningOperation](https://developer.apple.com/documentation/matter/mtrcommissioningoperation)
- [MTRContentAppObserverClusterContentAppMessageParams](https://developer.apple.com/documentation/matter/mtrcontentappobserverclustercontentappmessageparams)
- [MTRContentAppObserverClusterContentAppMessageResponseParams](https://developer.apple.com/documentation/matter/mtrcontentappobserverclustercontentappmessageresponseparams)
- [MTRDataTypeAtomicAttributeStatusStruct](https://developer.apple.com/documentation/matter/mtrdatatypeatomicattributestatusstruct)
- [MTRDataTypeLocationDescriptorStruct](https://developer.apple.com/documentation/matter/mtrdatatypelocationdescriptorstruct)
- [MTRDeviceEnergyManagementClusterCancelPowerAdjustRequestParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclustercancelpoweradjustrequestparams)
- [MTRDeviceEnergyManagementClusterCancelRequestParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclustercancelrequestparams)
- [MTRDeviceEnergyManagementClusterConstraintsStruct](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterconstraintsstruct)
- [MTRDeviceEnergyManagementClusterCostStruct](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclustercoststruct)
- [MTRDeviceEnergyManagementClusterForecastStruct](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterforecaststruct)
- [MTRDeviceEnergyManagementClusterModifyForecastRequestParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclustermodifyforecastrequestparams)
- [MTRDeviceEnergyManagementClusterPauseRequestParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterpauserequestparams)
- [MTRDeviceEnergyManagementClusterPausedEvent](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterpausedevent)
- [MTRDeviceEnergyManagementClusterPowerAdjustCapabilityStruct](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterpoweradjustcapabilitystruct)
- [MTRDeviceEnergyManagementClusterPowerAdjustEndEvent](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterpoweradjustendevent)
- [MTRDeviceEnergyManagementClusterPowerAdjustRequestParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterpoweradjustrequestparams)
- [MTRDeviceEnergyManagementClusterPowerAdjustStartEvent](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterpoweradjuststartevent)
- [MTRDeviceEnergyManagementClusterPowerAdjustStruct](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterpoweradjuststruct)
- [MTRDeviceEnergyManagementClusterRequestConstraintBasedForecastParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterrequestconstraintbasedforecastparams)
- [MTRDeviceEnergyManagementClusterResumeRequestParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterresumerequestparams)
- [MTRDeviceEnergyManagementClusterResumedEvent](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterresumedevent)
- [MTRDeviceEnergyManagementClusterSlotAdjustmentStruct](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterslotadjustmentstruct)
- [MTRDeviceEnergyManagementClusterSlotStruct](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterslotstruct)
- [MTRDeviceEnergyManagementClusterStartTimeAdjustRequestParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementclusterstarttimeadjustrequestparams)
- [MTRDeviceEnergyManagementModeClusterChangeToModeParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementmodeclusterchangetomodeparams)
- [MTRDeviceEnergyManagementModeClusterChangeToModeResponseParams](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementmodeclusterchangetomoderesponseparams)
- [MTRDeviceEnergyManagementModeClusterModeOptionStruct](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementmodeclustermodeoptionstruct)
- [MTRDeviceEnergyManagementModeClusterModeTagStruct](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementmodeclustermodetagstruct)
- [MTRDeviceType](https://developer.apple.com/documentation/matter/mtrdevicetype): Matter specification에 정의된 device type에 대한 메타데이터입니다.
- [MTRDishwasherAlarmClusterModifyEnabledAlarmsParams](https://developer.apple.com/documentation/matter/mtrdishwasheralarmclustermodifyenabledalarmsparams)
- [MTRDishwasherAlarmClusterNotifyEvent](https://developer.apple.com/documentation/matter/mtrdishwasheralarmclusternotifyevent)
- [MTRDishwasherAlarmClusterResetParams](https://developer.apple.com/documentation/matter/mtrdishwasheralarmclusterresetparams)
- [MTRDishwasherModeClusterChangeToModeParams](https://developer.apple.com/documentation/matter/mtrdishwashermodeclusterchangetomodeparams)
- [MTRDishwasherModeClusterChangeToModeResponseParams](https://developer.apple.com/documentation/matter/mtrdishwashermodeclusterchangetomoderesponseparams)
- [MTRDishwasherModeClusterModeOptionStruct](https://developer.apple.com/documentation/matter/mtrdishwashermodeclustermodeoptionstruct)
- [MTRDishwasherModeClusterModeTagStruct](https://developer.apple.com/documentation/matter/mtrdishwashermodeclustermodetagstruct)
- [MTRDoorLockClusterClearAliroReaderConfigParams](https://developer.apple.com/documentation/matter/mtrdoorlockclusterclearaliroreaderconfigparams)
- [MTRDoorLockClusterSetAliroReaderConfigParams](https://developer.apple.com/documentation/matter/mtrdoorlockclustersetaliroreaderconfigparams)
- [MTRDoorLockClusterUnboltDoorParams](https://developer.apple.com/documentation/matter/mtrdoorlockclusterunboltdoorparams)
- [MTRElectricalEnergyMeasurementClusterMeasurementAccuracyRangeStruct](https://developer.apple.com/documentation/matter/mtrelectricalenergymeasurementclustermeasurementaccuracyrangestruct)
- [MTREndpointInfo](https://developer.apple.com/documentation/matter/mtrendpointinfo): Matter node의 endpoint에 대한 메타데이터입니다.
- [MTREnergyEVSEClusterChargingTargetScheduleStruct](https://developer.apple.com/documentation/matter/mtrenergyevseclusterchargingtargetschedulestruct)
- [MTREnergyEVSEClusterChargingTargetStruct](https://developer.apple.com/documentation/matter/mtrenergyevseclusterchargingtargetstruct)
- [MTREnergyEVSEClusterClearTargetsParams](https://developer.apple.com/documentation/matter/mtrenergyevseclustercleartargetsparams)
- [MTREnergyEVSEClusterDisableParams](https://developer.apple.com/documentation/matter/mtrenergyevseclusterdisableparams)
- [MTREnergyEVSEClusterEVConnectedEvent](https://developer.apple.com/documentation/matter/mtrenergyevseclusterevconnectedevent)
- [MTREnergyEVSEClusterEVNotDetectedEvent](https://developer.apple.com/documentation/matter/mtrenergyevseclusterevnotdetectedevent)
- [MTREnergyEVSEClusterEnableChargingParams](https://developer.apple.com/documentation/matter/mtrenergyevseclusterenablechargingparams)
- [MTREnergyEVSEClusterEnergyTransferStartedEvent](https://developer.apple.com/documentation/matter/mtrenergyevseclusterenergytransferstartedevent)
- [MTREnergyEVSEClusterEnergyTransferStoppedEvent](https://developer.apple.com/documentation/matter/mtrenergyevseclusterenergytransferstoppedevent)
- [MTREnergyEVSEClusterFaultEvent](https://developer.apple.com/documentation/matter/mtrenergyevseclusterfaultevent)
- [MTREnergyEVSEClusterGetTargetsParams](https://developer.apple.com/documentation/matter/mtrenergyevseclustergettargetsparams)
- [MTREnergyEVSEClusterGetTargetsResponseParams](https://developer.apple.com/documentation/matter/mtrenergyevseclustergettargetsresponseparams)
- [MTREnergyEVSEClusterRFIDEvent](https://developer.apple.com/documentation/matter/mtrenergyevseclusterrfidevent)
- [MTREnergyEVSEClusterSetTargetsParams](https://developer.apple.com/documentation/matter/mtrenergyevseclustersettargetsparams)
- [MTREnergyEVSEClusterStartDiagnosticsParams](https://developer.apple.com/documentation/matter/mtrenergyevseclusterstartdiagnosticsparams)
- [MTREnergyEVSEModeClusterChangeToModeParams](https://developer.apple.com/documentation/matter/mtrenergyevsemodeclusterchangetomodeparams)
- [MTREnergyEVSEModeClusterChangeToModeResponseParams](https://developer.apple.com/documentation/matter/mtrenergyevsemodeclusterchangetomoderesponseparams)
- [MTREnergyEVSEModeClusterModeOptionStruct](https://developer.apple.com/documentation/matter/mtrenergyevsemodeclustermodeoptionstruct)
- [MTREnergyEVSEModeClusterModeTagStruct](https://developer.apple.com/documentation/matter/mtrenergyevsemodeclustermodetagstruct)
- [MTRGeneralDiagnosticsClusterPayloadTestRequestParams](https://developer.apple.com/documentation/matter/mtrgeneraldiagnosticsclusterpayloadtestrequestparams)
- [MTRGeneralDiagnosticsClusterPayloadTestResponseParams](https://developer.apple.com/documentation/matter/mtrgeneraldiagnosticsclusterpayloadtestresponseparams)
- [MTRGeneralDiagnosticsClusterTimeSnapshotParams](https://developer.apple.com/documentation/matter/mtrgeneraldiagnosticsclustertimesnapshotparams)
- [MTRGeneralDiagnosticsClusterTimeSnapshotResponseParams](https://developer.apple.com/documentation/matter/mtrgeneraldiagnosticsclustertimesnapshotresponseparams)
- [MTRICDManagementClusterMonitoringRegistrationStruct](https://developer.apple.com/documentation/matter/mtricdmanagementclustermonitoringregistrationstruct)
- [MTRICDManagementClusterRegisterClientParams](https://developer.apple.com/documentation/matter/mtricdmanagementclusterregisterclientparams)
- [MTRICDManagementClusterRegisterClientResponseParams](https://developer.apple.com/documentation/matter/mtricdmanagementclusterregisterclientresponseparams)
- [MTRICDManagementClusterStayActiveRequestParams](https://developer.apple.com/documentation/matter/mtricdmanagementclusterstayactiverequestparams)
- [MTRICDManagementClusterStayActiveResponseParams](https://developer.apple.com/documentation/matter/mtricdmanagementclusterstayactiveresponseparams)
- [MTRICDManagementClusterUnregisterClientParams](https://developer.apple.com/documentation/matter/mtricdmanagementclusterunregisterclientparams)
- [MTRLaundryWasherModeClusterChangeToModeParams](https://developer.apple.com/documentation/matter/mtrlaundrywashermodeclusterchangetomodeparams)
- [MTRLaundryWasherModeClusterChangeToModeResponseParams](https://developer.apple.com/documentation/matter/mtrlaundrywashermodeclusterchangetomoderesponseparams)
- [MTRLaundryWasherModeClusterModeOptionStruct](https://developer.apple.com/documentation/matter/mtrlaundrywashermodeclustermodeoptionstruct)
- [MTRLaundryWasherModeClusterModeTagStruct](https://developer.apple.com/documentation/matter/mtrlaundrywashermodeclustermodetagstruct)
- [MTRMediaPlaybackClusterActivateAudioTrackParams](https://developer.apple.com/documentation/matter/mtrmediaplaybackclusteractivateaudiotrackparams)
- [MTRMediaPlaybackClusterActivateTextTrackParams](https://developer.apple.com/documentation/matter/mtrmediaplaybackclusteractivatetexttrackparams)
- [MTRMediaPlaybackClusterDeactivateTextTrackParams](https://developer.apple.com/documentation/matter/mtrmediaplaybackclusterdeactivatetexttrackparams)
- [MTRMediaPlaybackClusterStateChangedEvent](https://developer.apple.com/documentation/matter/mtrmediaplaybackclusterstatechangedevent)
- [MTRMessagesClusterCancelMessagesRequestParams](https://developer.apple.com/documentation/matter/mtrmessagesclustercancelmessagesrequestparams)
- [MTRMessagesClusterMessageCompleteEvent](https://developer.apple.com/documentation/matter/mtrmessagesclustermessagecompleteevent)
- [MTRMessagesClusterMessagePresentedEvent](https://developer.apple.com/documentation/matter/mtrmessagesclustermessagepresentedevent)
- [MTRMessagesClusterMessageQueuedEvent](https://developer.apple.com/documentation/matter/mtrmessagesclustermessagequeuedevent)
- [MTRMessagesClusterMessageResponseOptionStruct](https://developer.apple.com/documentation/matter/mtrmessagesclustermessageresponseoptionstruct)
- [MTRMessagesClusterMessageStruct](https://developer.apple.com/documentation/matter/mtrmessagesclustermessagestruct)
- [MTRMessagesClusterPresentMessagesRequestParams](https://developer.apple.com/documentation/matter/mtrmessagesclusterpresentmessagesrequestparams)
- [MTRMicrowaveOvenControlClusterAddMoreTimeParams](https://developer.apple.com/documentation/matter/mtrmicrowaveovencontrolclusteraddmoretimeparams)
- [MTRMicrowaveOvenControlClusterSetCookingParametersParams](https://developer.apple.com/documentation/matter/mtrmicrowaveovencontrolclustersetcookingparametersparams)
- [MTRMicrowaveOvenModeClusterModeOptionStruct](https://developer.apple.com/documentation/matter/mtrmicrowaveovenmodeclustermodeoptionstruct)
- [MTRMicrowaveOvenModeClusterModeTagStruct](https://developer.apple.com/documentation/matter/mtrmicrowaveovenmodeclustermodetagstruct)
- [MTROccupancySensingClusterHoldTimeLimitsStruct](https://developer.apple.com/documentation/matter/mtroccupancysensingclusterholdtimelimitsstruct)
- [MTROccupancySensingClusterOccupancyChangedEvent](https://developer.apple.com/documentation/matter/mtroccupancysensingclusteroccupancychangedevent)
- [MTROvenCavityOperationalStateClusterErrorStateStruct](https://developer.apple.com/documentation/matter/mtrovencavityoperationalstateclustererrorstatestruct)
- [MTROvenCavityOperationalStateClusterOperationCompletionEvent](https://developer.apple.com/documentation/matter/mtrovencavityoperationalstateclusteroperationcompletionevent)
- [MTROvenCavityOperationalStateClusterOperationalCommandResponseParams](https://developer.apple.com/documentation/matter/mtrovencavityoperationalstateclusteroperationalcommandresponseparams)
- [MTROvenCavityOperationalStateClusterOperationalErrorEvent](https://developer.apple.com/documentation/matter/mtrovencavityoperationalstateclusteroperationalerrorevent)
- [MTROvenCavityOperationalStateClusterOperationalStateStruct](https://developer.apple.com/documentation/matter/mtrovencavityoperationalstateclusteroperationalstatestruct)
- [MTROvenCavityOperationalStateClusterStartParams](https://developer.apple.com/documentation/matter/mtrovencavityoperationalstateclusterstartparams)
- [MTROvenCavityOperationalStateClusterStopParams](https://developer.apple.com/documentation/matter/mtrovencavityoperationalstateclusterstopparams)
- [MTROvenModeClusterChangeToModeParams](https://developer.apple.com/documentation/matter/mtrovenmodeclusterchangetomodeparams)
- [MTROvenModeClusterChangeToModeResponseParams](https://developer.apple.com/documentation/matter/mtrovenmodeclusterchangetomoderesponseparams)
- [MTROvenModeClusterModeOptionStruct](https://developer.apple.com/documentation/matter/mtrovenmodeclustermodeoptionstruct)
- [MTROvenModeClusterModeTagStruct](https://developer.apple.com/documentation/matter/mtrovenmodeclustermodetagstruct)
- [MTRRVCOperationalStateClusterGoHomeParams](https://developer.apple.com/documentation/matter/mtrrvcoperationalstateclustergohomeparams)
- [MTRRefrigeratorAlarmClusterNotifyEvent](https://developer.apple.com/documentation/matter/mtrrefrigeratoralarmclusternotifyevent)
- [MTRRefrigeratorAndTemperatureControlledCabinetModeClusterChangeToModeParams](https://developer.apple.com/documentation/matter/mtrrefrigeratorandtemperaturecontrolledcabinetmodeclusterchangetomodeparams)
- [MTRRefrigeratorAndTemperatureControlledCabinetModeClusterChangeToModeResponseParams](https://developer.apple.com/documentation/matter/mtrrefrigeratorandtemperaturecontrolledcabinetmodeclusterchangetomoderesponseparams)
- [MTRRefrigeratorAndTemperatureControlledCabinetModeClusterModeOptionStruct](https://developer.apple.com/documentation/matter/mtrrefrigeratorandtemperaturecontrolledcabinetmodeclustermodeoptionstruct)
- [MTRRefrigeratorAndTemperatureControlledCabinetModeClusterModeTagStruct](https://developer.apple.com/documentation/matter/mtrrefrigeratorandtemperaturecontrolledcabinetmodeclustermodetagstruct)
- [MTRServiceAreaClusterAreaInfoStruct](https://developer.apple.com/documentation/matter/mtrserviceareaclusterareainfostruct)
- [MTRServiceAreaClusterAreaStruct](https://developer.apple.com/documentation/matter/mtrserviceareaclusterareastruct)
- [MTRServiceAreaClusterLandmarkInfoStruct](https://developer.apple.com/documentation/matter/mtrserviceareaclusterlandmarkinfostruct)
- [MTRServiceAreaClusterMapStruct](https://developer.apple.com/documentation/matter/mtrserviceareaclustermapstruct)
- [MTRServiceAreaClusterProgressStruct](https://developer.apple.com/documentation/matter/mtrserviceareaclusterprogressstruct)
- [MTRServiceAreaClusterSelectAreasParams](https://developer.apple.com/documentation/matter/mtrserviceareaclusterselectareasparams)
- [MTRServiceAreaClusterSelectAreasResponseParams](https://developer.apple.com/documentation/matter/mtrserviceareaclusterselectareasresponseparams)
- [MTRServiceAreaClusterSkipAreaParams](https://developer.apple.com/documentation/matter/mtrserviceareaclusterskipareaparams)
- [MTRServiceAreaClusterSkipAreaResponseParams](https://developer.apple.com/documentation/matter/mtrserviceareaclusterskiparearesponseparams)
- [MTRTargetNavigatorClusterTargetUpdatedEvent](https://developer.apple.com/documentation/matter/mtrtargetnavigatorclustertargetupdatedevent)
- [MTRTemperatureControlClusterSetTemperatureParams](https://developer.apple.com/documentation/matter/mtrtemperaturecontrolclustersettemperatureparams)
- [MTRThermostatClusterAtomicRequestParams](https://developer.apple.com/documentation/matter/mtrthermostatclusteratomicrequestparams)
- [MTRThermostatClusterAtomicResponseParams](https://developer.apple.com/documentation/matter/mtrthermostatclusteratomicresponseparams)
- [MTRThermostatClusterPresetStruct](https://developer.apple.com/documentation/matter/mtrthermostatclusterpresetstruct)
- [MTRThermostatClusterPresetTypeStruct](https://developer.apple.com/documentation/matter/mtrthermostatclusterpresettypestruct)
- [MTRThermostatClusterScheduleStruct](https://developer.apple.com/documentation/matter/mtrthermostatclusterschedulestruct)
- [MTRThermostatClusterScheduleTransitionStruct](https://developer.apple.com/documentation/matter/mtrthermostatclusterscheduletransitionstruct)
- [MTRThermostatClusterScheduleTypeStruct](https://developer.apple.com/documentation/matter/mtrthermostatclusterscheduletypestruct)
- [MTRThermostatClusterSetActivePresetRequestParams](https://developer.apple.com/documentation/matter/mtrthermostatclustersetactivepresetrequestparams)
- [MTRThermostatClusterSetActiveScheduleRequestParams](https://developer.apple.com/documentation/matter/mtrthermostatclustersetactiveschedulerequestparams)
- [MTRThreadBorderRouterManagementClusterDatasetResponseParams](https://developer.apple.com/documentation/matter/mtrthreadborderroutermanagementclusterdatasetresponseparams)
- [MTRThreadBorderRouterManagementClusterGetActiveDatasetRequestParams](https://developer.apple.com/documentation/matter/mtrthreadborderroutermanagementclustergetactivedatasetrequestparams)
- [MTRThreadBorderRouterManagementClusterGetPendingDatasetRequestParams](https://developer.apple.com/documentation/matter/mtrthreadborderroutermanagementclustergetpendingdatasetrequestparams)
- [MTRThreadBorderRouterManagementClusterSetActiveDatasetRequestParams](https://developer.apple.com/documentation/matter/mtrthreadborderroutermanagementclustersetactivedatasetrequestparams)
- [MTRThreadBorderRouterManagementClusterSetPendingDatasetRequestParams](https://developer.apple.com/documentation/matter/mtrthreadborderroutermanagementclustersetpendingdatasetrequestparams)
- [MTRThreadNetworkDirectoryClusterAddNetworkParams](https://developer.apple.com/documentation/matter/mtrthreadnetworkdirectoryclusteraddnetworkparams)
- [MTRThreadNetworkDirectoryClusterGetOperationalDatasetParams](https://developer.apple.com/documentation/matter/mtrthreadnetworkdirectoryclustergetoperationaldatasetparams)
- [MTRThreadNetworkDirectoryClusterOperationalDatasetResponseParams](https://developer.apple.com/documentation/matter/mtrthreadnetworkdirectoryclusteroperationaldatasetresponseparams)
- [MTRThreadNetworkDirectoryClusterRemoveNetworkParams](https://developer.apple.com/documentation/matter/mtrthreadnetworkdirectoryclusterremovenetworkparams)
- [MTRThreadNetworkDirectoryClusterThreadNetworkStruct](https://developer.apple.com/documentation/matter/mtrthreadnetworkdirectoryclusterthreadnetworkstruct)
- [MTRTimeSynchronizationClusterDSTStatusEvent](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclusterdststatusevent)
- [MTRTimeSynchronizationClusterDSTTableEmptyEvent](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclusterdsttableemptyevent)
- [MTRTimeSynchronizationClusterFabricScopedTrustedTimeSourceStruct](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclusterfabricscopedtrustedtimesourcestruct)
- [MTRTimeSynchronizationClusterMissingTrustedTimeSourceEvent](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustermissingtrustedtimesourceevent)
- [MTRTimeSynchronizationClusterSetDSTOffsetParams](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustersetdstoffsetparams)
- [MTRTimeSynchronizationClusterSetDefaultNTPParams](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustersetdefaultntpparams)
- [MTRTimeSynchronizationClusterSetTimeZoneParams](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustersettimezoneparams)
- [MTRTimeSynchronizationClusterSetTimeZoneResponseParams](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustersettimezoneresponseparams)
- [MTRTimeSynchronizationClusterSetTrustedTimeSourceParams](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustersettrustedtimesourceparams)
- [MTRTimeSynchronizationClusterTimeFailureEvent](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustertimefailureevent)
- [MTRTimeSynchronizationClusterTimeZoneStatusEvent](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustertimezonestatusevent)
- [MTRTimeSynchronizationClusterTrustedTimeSourceStruct](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustertrustedtimesourcestruct)
- [MTRWaterHeaterManagementClusterBoostEndedEvent](https://developer.apple.com/documentation/matter/mtrwaterheatermanagementclusterboostendedevent)
- [MTRWaterHeaterManagementClusterBoostParams](https://developer.apple.com/documentation/matter/mtrwaterheatermanagementclusterboostparams)
- [MTRWaterHeaterManagementClusterBoostStartedEvent](https://developer.apple.com/documentation/matter/mtrwaterheatermanagementclusterbooststartedevent)
- [MTRWaterHeaterManagementClusterCancelBoostParams](https://developer.apple.com/documentation/matter/mtrwaterheatermanagementclustercancelboostparams)
- [MTRWaterHeaterManagementClusterWaterHeaterBoostInfoStruct](https://developer.apple.com/documentation/matter/mtrwaterheatermanagementclusterwaterheaterboostinfostruct)
- [MTRWaterHeaterModeClusterChangeToModeParams](https://developer.apple.com/documentation/matter/mtrwaterheatermodeclusterchangetomodeparams)
- [MTRWaterHeaterModeClusterChangeToModeResponseParams](https://developer.apple.com/documentation/matter/mtrwaterheatermodeclusterchangetomoderesponseparams)
- [MTRWaterHeaterModeClusterModeOptionStruct](https://developer.apple.com/documentation/matter/mtrwaterheatermodeclustermodeoptionstruct)
- [MTRWaterHeaterModeClusterModeTagStruct](https://developer.apple.com/documentation/matter/mtrwaterheatermodeclustermodetagstruct)
- [MTRWiFiNetworkManagementClusterNetworkPassphraseRequestParams](https://developer.apple.com/documentation/matter/mtrwifinetworkmanagementclusternetworkpassphraserequestparams)
- [MTRWiFiNetworkManagementClusterNetworkPassphraseResponseParams](https://developer.apple.com/documentation/matter/mtrwifinetworkmanagementclusternetworkpassphraseresponseparams)
- [MTRXPCDeviceControllerParameters](https://developer.apple.com/documentation/matter/mtrxpcdevicecontrollerparameters)
:::

:::topic-grid
## Protocols
- [MTRCommissioningDelegate](https://developer.apple.com/documentation/matter/mtrcommissioningdelegate)
- [MTRXPCClientProtocol](https://developer.apple.com/documentation/matter/mtrxpcclientprotocol)
- [MTRXPCClientProtocol_MTRDevice](https://developer.apple.com/documentation/matter/mtrxpcclientprotocol_mtrdevice)
- [MTRXPCClientProtocol_MTRDeviceController](https://developer.apple.com/documentation/matter/mtrxpcclientprotocol_mtrdevicecontroller)
- [MTRXPCServerProtocol](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol)
- [MTRXPCServerProtocol_MTRDevice](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevice)
- [MTRXPCServerProtocol_MTRDeviceController](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevicecontroller)
:::

:::topic-grid
## Structures
- [MTRAccessControlFeature](https://developer.apple.com/documentation/matter/mtraccesscontrolfeature)
- [MTRBridgedDeviceBasicInformationFeature](https://developer.apple.com/documentation/matter/mtrbridgeddevicebasicinformationfeature)
- [MTRChannelRecordingFlagBitmap](https://developer.apple.com/documentation/matter/mtrchannelrecordingflagbitmap)
- [MTRColorControlColorCapabilitiesBitmap](https://developer.apple.com/documentation/matter/mtrcolorcontrolcolorcapabilitiesbitmap)
- [MTRColorControlOptionsBitmap](https://developer.apple.com/documentation/matter/mtrcolorcontroloptionsbitmap)
- [MTRColorControlUpdateFlagsBitmap](https://developer.apple.com/documentation/matter/mtrcolorcontrolupdateflagsbitmap)
- [MTRCommissionerControlSupportedDeviceCategoryBitmap](https://developer.apple.com/documentation/matter/mtrcommissionercontrolsupporteddevicecategorybitmap)
- [MTRDeviceEnergyManagementFeature](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementfeature)
- [MTRDishwasherAlarmAlarmBitmap](https://developer.apple.com/documentation/matter/mtrdishwasheralarmalarmbitmap)
- [MTRDishwasherAlarmFeature](https://developer.apple.com/documentation/matter/mtrdishwasheralarmfeature)
- [MTREnergyEVSEFeature](https://developer.apple.com/documentation/matter/mtrenergyevsefeature)
- [MTREnergyEVSETargetDayOfWeekBitmap](https://developer.apple.com/documentation/matter/mtrenergyevsetargetdayofweekbitmap)
- [MTRGeneralDiagnosticsFeature](https://developer.apple.com/documentation/matter/mtrgeneraldiagnosticsfeature)
- [MTRICDManagementFeature](https://developer.apple.com/documentation/matter/mtricdmanagementfeature)
- [MTRICDManagementUserActiveModeTriggerBitmap](https://developer.apple.com/documentation/matter/mtricdmanagementuseractivemodetriggerbitmap)
- [MTRLaundryWasherControlsFeature](https://developer.apple.com/documentation/matter/mtrlaundrywashercontrolsfeature)
- [MTRMessagesFeature](https://developer.apple.com/documentation/matter/mtrmessagesfeature)
- [MTRMessagesMessageControlBitmap](https://developer.apple.com/documentation/matter/mtrmessagesmessagecontrolbitmap)
- [MTRMicrowaveOvenControlFeature](https://developer.apple.com/documentation/matter/mtrmicrowaveovencontrolfeature)
- [MTRNetworkCommissioningThreadCapabilitiesBitmap](https://developer.apple.com/documentation/matter/mtrnetworkcommissioningthreadcapabilitiesbitmap)
- [MTROccupancySensingFeature](https://developer.apple.com/documentation/matter/mtroccupancysensingfeature)
- [MTRPowerTopologyFeature](https://developer.apple.com/documentation/matter/mtrpowertopologyfeature)
- [MTRRefrigeratorAlarmAlarmBitmap](https://developer.apple.com/documentation/matter/mtrrefrigeratoralarmalarmbitmap)
- [MTRServiceAreaFeature](https://developer.apple.com/documentation/matter/mtrserviceareafeature)
- [MTRTemperatureControlFeature](https://developer.apple.com/documentation/matter/mtrtemperaturecontrolfeature)
- [MTRThermostatACErrorCodeBitmap](https://developer.apple.com/documentation/matter/mtrthermostatacerrorcodebitmap)
- [MTRThermostatHVACSystemTypeBitmap](https://developer.apple.com/documentation/matter/mtrthermostathvacsystemtypebitmap)
- [MTRThermostatOccupancyBitmap](https://developer.apple.com/documentation/matter/mtrthermostatoccupancybitmap)
- [MTRThermostatPresetTypeFeaturesBitmap](https://developer.apple.com/documentation/matter/mtrthermostatpresettypefeaturesbitmap)
- [MTRThermostatProgrammingOperationModeBitmap](https://developer.apple.com/documentation/matter/mtrthermostatprogrammingoperationmodebitmap)
- [MTRThermostatRelayStateBitmap](https://developer.apple.com/documentation/matter/mtrthermostatrelaystatebitmap)
- [MTRThermostatRemoteSensingBitmap](https://developer.apple.com/documentation/matter/mtrthermostatremotesensingbitmap)
- [MTRThermostatScheduleTypeFeaturesBitmap](https://developer.apple.com/documentation/matter/mtrthermostatscheduletypefeaturesbitmap)
- [MTRThreadBorderRouterManagementFeature](https://developer.apple.com/documentation/matter/mtrthreadborderroutermanagementfeature)
- [MTRTimeSynchronizationFeature](https://developer.apple.com/documentation/matter/mtrtimesynchronizationfeature)
- [MTRWaterHeaterManagementFeature](https://developer.apple.com/documentation/matter/mtrwaterheatermanagementfeature)
- [MTRWaterHeaterManagementWaterHeaterHeatSourceBitmap](https://developer.apple.com/documentation/matter/mtrwaterheatermanagementwaterheaterheatsourcebitmap)
:::

:::topic-grid
## Variables
- [MTRDeviceControllerRegistrationControllerCompressedFabricIDKey](https://developer.apple.com/documentation/matter/mtrdevicecontrollerregistrationcontrollercompressedfabricidkey)
- [MTRDeviceControllerRegistrationControllerContextKey](https://developer.apple.com/documentation/matter/mtrdevicecontrollerregistrationcontrollercontextkey)
- [MTRDeviceControllerRegistrationControllerIsRunningKey](https://developer.apple.com/documentation/matter/mtrdevicecontrollerregistrationcontrollerisrunningkey)
- [MTRDeviceControllerRegistrationControllerNodeIDKey](https://developer.apple.com/documentation/matter/mtrdevicecontrollerregistrationcontrollernodeidkey)
- [MTRDeviceControllerRegistrationDeviceInternalStateKey](https://developer.apple.com/documentation/matter/mtrdevicecontrollerregistrationdeviceinternalstatekey)
- [MTRDeviceControllerRegistrationNodeIDKey](https://developer.apple.com/documentation/matter/mtrdevicecontrollerregistrationnodeidkey)
- [MTRDeviceControllerRegistrationNodeIDsKey](https://developer.apple.com/documentation/matter/mtrdevicecontrollerregistrationnodeidskey)
:::

:::topic-grid
## Functions
- [MTREventNameForID(_:_:)](https://developer.apple.com/documentation/matter/mtreventnameforid(_:_:)): Matter event ID를 설명 문자열로 해석합니다.
- [MTRRequestCommandNameForID(_:_:)](https://developer.apple.com/documentation/matter/mtrrequestcommandnameforid(_:_:)): Matter request(클라이언트에서 서버로) command ID를 설명 문자열로 해석합니다.
- [MTRResponseCommandNameForID(_:_:)](https://developer.apple.com/documentation/matter/mtrresponsecommandnameforid(_:_:)): Matter response(서버에서 클라이언트로) command ID를 설명 문자열로 해석합니다.
:::

:::topic-grid
## Enumerations
- [MTRAccessControlAccessRestrictionType](https://developer.apple.com/documentation/matter/mtraccesscontrolaccessrestrictiontype)
- [MTRChannelType](https://developer.apple.com/documentation/matter/mtrchanneltype)
- [MTRColorControlDirection](https://developer.apple.com/documentation/matter/mtrcolorcontroldirection)
- [MTRColorControlDriftCompensation](https://developer.apple.com/documentation/matter/mtrcolorcontroldriftcompensation)
- [MTRColorControlEnhancedColorMode](https://developer.apple.com/documentation/matter/mtrcolorcontrolenhancedcolormode)
- [MTRColorControlMoveMode](https://developer.apple.com/documentation/matter/mtrcolorcontrolmovemode)
- [MTRColorControlStepMode](https://developer.apple.com/documentation/matter/mtrcolorcontrolstepmode)
- [MTRContentAppObserverStatus](https://developer.apple.com/documentation/matter/mtrcontentappobserverstatus)
- [MTRDataTypeAtomicRequestTypeEnum](https://developer.apple.com/documentation/matter/mtrdatatypeatomicrequesttypeenum)
- [MTRDataTypeLandmarkTag](https://developer.apple.com/documentation/matter/mtrdatatypelandmarktag)
- [MTRDataTypePositionTag](https://developer.apple.com/documentation/matter/mtrdatatypepositiontag)
- [MTRDataTypeRelativePositionTag](https://developer.apple.com/documentation/matter/mtrdatatyperelativepositiontag)
- [MTRDeviceEnergyManagementAdjustmentCause](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementadjustmentcause)
- [MTRDeviceEnergyManagementCause](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementcause)
- [MTRDeviceEnergyManagementCostType](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementcosttype)
- [MTRDeviceEnergyManagementESAState](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementesastate)
- [MTRDeviceEnergyManagementESAType](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementesatype)
- [MTRDeviceEnergyManagementForecastUpdateReason](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementforecastupdatereason)
- [MTRDeviceEnergyManagementModeModeTag](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementmodemodetag)
- [MTRDeviceEnergyManagementOptOutState](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementoptoutstate)
- [MTRDeviceEnergyManagementPowerAdjustReason](https://developer.apple.com/documentation/matter/mtrdeviceenergymanagementpoweradjustreason)
- [MTRDeviceTypeIDType](https://developer.apple.com/documentation/matter/mtrdevicetypeidtype)
- [MTRDishwasherModeModeTag](https://developer.apple.com/documentation/matter/mtrdishwashermodemodetag)
- [MTRElectricalEnergyMeasurementMeasurementType](https://developer.apple.com/documentation/matter/mtrelectricalenergymeasurementmeasurementtype)
- [MTREnergyEVSEEnergyTransferStoppedReason](https://developer.apple.com/documentation/matter/mtrenergyevseenergytransferstoppedreason)
- [MTREnergyEVSEFaultState](https://developer.apple.com/documentation/matter/mtrenergyevsefaultstate)
- [MTREnergyEVSEModeModeTag](https://developer.apple.com/documentation/matter/mtrenergyevsemodemodetag)
- [MTREnergyEVSEState](https://developer.apple.com/documentation/matter/mtrenergyevsestate)
- [MTREnergyEVSESupplyState](https://developer.apple.com/documentation/matter/mtrenergyevsesupplystate)
- [MTRICDManagementClientType](https://developer.apple.com/documentation/matter/mtricdmanagementclienttype)
- [MTRICDManagementOperatingMode](https://developer.apple.com/documentation/matter/mtricdmanagementoperatingmode)
- [MTRLaundryDryerControlsDrynessLevel](https://developer.apple.com/documentation/matter/mtrlaundrydryercontrolsdrynesslevel)
- [MTRLaundryWasherControlsNumberOfRinses](https://developer.apple.com/documentation/matter/mtrlaundrywashercontrolsnumberofrinses)
- [MTRLaundryWasherModeModeTag](https://developer.apple.com/documentation/matter/mtrlaundrywashermodemodetag)
- [MTRMediaPlaybackCharacteristic](https://developer.apple.com/documentation/matter/mtrmediaplaybackcharacteristic)
- [MTRMessagesFutureMessagePreference](https://developer.apple.com/documentation/matter/mtrmessagesfuturemessagepreference)
- [MTRMessagesMessagePriority](https://developer.apple.com/documentation/matter/mtrmessagesmessagepriority)
- [MTRMicrowaveOvenModeModeTag](https://developer.apple.com/documentation/matter/mtrmicrowaveovenmodemodetag)
- [MTROvenCavityOperationalStateErrorState](https://developer.apple.com/documentation/matter/mtrovencavityoperationalstateerrorstate)
- [MTROvenCavityOperationalStateOperationalState](https://developer.apple.com/documentation/matter/mtrovencavityoperationalstateoperationalstate)
- [MTROvenModeModeTag](https://developer.apple.com/documentation/matter/mtrovenmodemodetag)
- [MTRRefrigeratorAndTemperatureControlledCabinetModeModeTag](https://developer.apple.com/documentation/matter/mtrrefrigeratorandtemperaturecontrolledcabinetmodemodetag)
- [MTRServiceAreaOperationalStatus](https://developer.apple.com/documentation/matter/mtrserviceareaoperationalstatus)
- [MTRServiceAreaSelectAreasStatus](https://developer.apple.com/documentation/matter/mtrserviceareaselectareasstatus)
- [MTRServiceAreaSkipAreaStatus](https://developer.apple.com/documentation/matter/mtrserviceareaskipareastatus)
- [MTRThermostatACCapacityFormat](https://developer.apple.com/documentation/matter/mtrthermostataccapacityformat)
- [MTRThermostatACCompressorType](https://developer.apple.com/documentation/matter/mtrthermostataccompressortype)
- [MTRThermostatACLouverPosition](https://developer.apple.com/documentation/matter/mtrthermostataclouverposition)
- [MTRThermostatACRefrigerantType](https://developer.apple.com/documentation/matter/mtrthermostatacrefrigeranttype)
- [MTRThermostatACType](https://developer.apple.com/documentation/matter/mtrthermostatactype)
- [MTRThermostatPresetScenario](https://developer.apple.com/documentation/matter/mtrthermostatpresetscenario)
- [MTRThermostatSetpointChangeSource](https://developer.apple.com/documentation/matter/mtrthermostatsetpointchangesource)
- [MTRThermostatStartOfWeek](https://developer.apple.com/documentation/matter/mtrthermostatstartofweek)
- [MTRThermostatTemperatureSetpointHold](https://developer.apple.com/documentation/matter/mtrthermostattemperaturesetpointhold)
- [MTRTimeSynchronizationStatusCode](https://developer.apple.com/documentation/matter/mtrtimesynchronizationstatuscode)
- [MTRTimeSynchronizationTimeZoneDatabase](https://developer.apple.com/documentation/matter/mtrtimesynchronizationtimezonedatabase)
- [MTRWaterHeaterManagementBoostState](https://developer.apple.com/documentation/matter/mtrwaterheatermanagementbooststate)
- [MTRWaterHeaterModeModeTag](https://developer.apple.com/documentation/matter/mtrwaterheatermodemodetag)
:::
