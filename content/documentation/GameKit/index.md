---
route: /documentation/GameKit
source_url: https://developer.apple.com/documentation/GameKit
source_locale: en-US
section: docc
content_type: symbol
title: GameKit
original_title: GameKit
source_hash: 8f9254539dc7588c23fb38a1115c69c1567dc8bf04bcc3fe66eb1f22b7fa3501
canonical_source: manual-translation
last_crawled_at: '2026-03-13T14:17:56+00:00'
last_translated_at: '2026-03-13T23:18:11+09:00'
---

# GameKit

플레이어가 친구와 상호 작용하고, 리더보드 순위를 비교하고, 도전 과제를 획득하고, 멀티플레이어 게임에 참여할 수 있게 합니다.

## 개요

GameKit 프레임워크를 사용하면 Game Center 소셜 게임 네트워크 기능을 구현할 수 있습니다. Game Center는 모든 게임과 기기 전반에서 플레이어를 식별하는 단일 계정을 제공하는 Apple 서비스입니다. 플레이어가 기기에서 Game Center에 로그인하면 친구에 접근하고, 앱이 구현한 Game Center 기능을 사용할 수 있습니다.

![접속 지점, 도전 과제 대시보드, 리더보드 대시보드, 친구 초대 기능을 보여 주는 여러 iPhone 화면입니다.](https://developer.apple.com)

GameKit 클래스를 사용하기 전에 프로젝트에서 Game Center를 활성화하고 코드에서 로컬 플레이어를 초기화해야 합니다. 그렇지 않으면 게임은 [GKError.Code.notAuthenticated](https://developer.apple.com/documentation/gamekit/gkerror/code/notauthenticated) 오류를 받습니다.

기존 Unity 프로젝트가 있다면 [Apple Unity Plug-ins](https://github.com/Apple/UnityPlugins)을 사용해 GameKit 프레임워크에 접근할 수 있습니다.

### Game Center 기능 구현

Game Center를 활성화한 뒤에는 게임 경험을 향상시키는 다양한 기능을 구현할 수 있습니다.

리더보드를 추가하면 플레이어는 친구와 전 세계 플레이어 사이에서 자신의 순위를 확인할 수 있습니다. 주기적으로 반복되는 리더보드를 만들어 정기 경쟁을 구성하면 플레이어가 최고 점수를 얻을 기회를 더 많이 제공할 수 있습니다. 플레이어가 게임을 진행함에 따라 도전 과제를 수여해 계속 플레이하도록 독려할 수도 있습니다.

GameKit은 실시간 멀티플레이어와 턴 기반 멀티플레이어 경험을 모두 지원합니다. 플레이어는 자동 매칭을 선택하거나 친구를 초대해 게임에 참여하게 할 수 있습니다. 게임이 포그라운드에 없을 때에도 초대를 받을 수 있는 턴 기반 게임을 지원할 수도 있습니다.

GameKit은 플레이어가 게임 안에서 하이라이트를 확인하고 Game Center 데이터에 직접 접근할 수 있도록 사용자 인터페이스 구성 요소도 제공합니다. access point는 플레이어가 자신의 프로필, 리더보드, 도전 과제를 살펴보고 친구 목록을 관리할 수 있는 대시보드를 열 수 있는 방법을 제공합니다.

앱에서 Game Center 기능을 설계할 때는 [Human Interface Guidelines > Technologies > Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center)를 참고하십시오.

:::topic-grid
## 핵심
- [Initializing and configuring Game Center](https://developer.apple.com/documentation/gamekit/initializing-and-configuring-game-center): Game Center를 활성화하고 기능을 구성한 뒤 Xcode 프로젝트 안에서 로컬 테스트를 수행합니다.
- [Authenticating a player](https://developer.apple.com/documentation/gamekit/authenticating-a-player): 플레이어 자격 증명과 기기 기능을 확인하고 계정 제한 사항을 점검합니다.
- [Improving the player experience for games with large downloads](https://developer.apple.com/documentation/gamekit/improving-the-player-experience-for-games-with-large-downloads): 기본 설치에 충분한 콘텐츠를 제공하고, 이후에는 on-demand resources와 Background Assets API를 사용해 추가 콘텐츠를 처리합니다.
- [Game Center Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.game-center): 앱 사용자가 리더보드에서 도전 과제를 보고 비교하고, 친구를 초대하고, 멀티플레이어 게임을 시작할 수 있는지 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 플레이어
- [Connecting players with their friends in your game](https://developer.apple.com/documentation/gamekit/connecting-players-with-their-friends-in-your-game): 플레이어가 게임 안에서 친구와 연결되고 상호 작용할 수 있게 합니다.
- [Saving the player’s game data to an iCloud account](https://developer.apple.com/documentation/gamekit/saving-the-player-s-game-data-to-an-icloud-account): 플레이 도중 또는 게임이 끝난 뒤 게임 데이터를 플레이어의 iCloud 계정에 저장해 어느 기기에서나 접근할 수 있게 합니다.
- [Protecting the player’s privacy using scoped identifiers](https://developer.apple.com/documentation/gamekit/protecting-the-player-s-privacy-using-scoped-identifiers): GameKit이 제공하는 scoped identifier를 플레이어 ID로 사용해 플레이어 데이터를 전송하거나 저장할 때 개인정보를 보호합니다.
- [GKLocalPlayer](https://developer.apple.com/documentation/gamekit/gklocalplayer): 게임이 실행 중인 기기에서 Game Center에 로그인한 로컬 플레이어입니다.
- [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer): 로컬 플레이어가 Game Center를 통해 초대하고 통신할 수 있는 원격 플레이어입니다.
- [GKBasePlayer](https://developer.apple.com/documentation/gamekit/gkbaseplayer): 서로 다른 플레이어 객체에 공통되는 데이터와 메서드를 제공하는 클래스입니다.
- [GKLocalPlayerListener](https://developer.apple.com/documentation/gamekit/gklocalplayerlistener): Game Center 플레이어 이벤트를 처리하는 protocol입니다.
- [GKPlayerAuthenticationDidChangeNotificationName](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/GKPlayerAuthenticationDidChangeNotificationName): GameKit이 로컬 플레이어 인증을 마친 뒤 게시하는 알림입니다.
- [GKPlayerDidChangeNotificationName](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/GKPlayerDidChangeNotificationName): 플레이어 객체의 데이터가 바뀔 때 게시하는 알림입니다.
:::

:::topic-grid
## Game Center 인터페이스
- [Adding an access point to your game](https://developer.apple.com/documentation/gamekit/adding-an-access-point-to-your-game): 사용자가 Game Center 대시보드에 쉽게 접근할 수 있는 연결 지점을 제공합니다.
- [Displaying the Game Center dashboard](https://developer.apple.com/documentation/gamekit/displaying-the-game-center-dashboard): 플레이어가 게임 안에서 Game Center 데이터로 이동할 수 있는 인터페이스를 제공합니다.
- [GKAccessPoint](https://developer.apple.com/documentation/gamekit/gkaccesspoint): 플레이어가 게임 안에서 Game Center 정보를 보고 관리할 수 있게 하는 객체입니다.
- [GKDialogController](https://developer.apple.com/documentation/gamekit/gkdialogcontroller): macOS 게임에서 대시보드를 표시할 수 있게 해 주는 객체입니다.
- [GKViewController](https://developer.apple.com/documentation/gamekit/gkviewcontroller): GameKit view controller 클래스가 채택하는 추상 기반 protocol입니다.
:::

:::topic-grid
## 리더보드
- [Encourage progress and competition with leaderboards](https://developer.apple.com/documentation/gamekit/encourage-progress-and-competition-with-leaderboards): 플레이어가 자신의 진행 상황을 측정하고 친구 및 다른 사람과 실력을 비교할 수 있게 합니다.
- [Creating recurring leaderboards](https://developer.apple.com/documentation/gamekit/creating-recurring-leaderboards): 일정에 따라 플레이어 점수를 순위화하는 리더보드를 생성합니다.
- [Adding Recurring Leaderboards to Your Game](https://developer.apple.com/documentation/gamekit/adding-recurring-leaderboards-to-your-game): 기간이 있고 반복되는 리더보드를 추가해 경쟁을 촉진합니다.
- [GKLeaderboard](https://developer.apple.com/documentation/gamekit/gkleaderboard): Game Center가 저장하는 게임용 리더보드입니다.
- [GKLeaderboardSet](https://developer.apple.com/documentation/gamekit/gkleaderboardset): 리더보드를 논리적이고 일관된 그룹으로 조직합니다.
- [GKLeaderboardScore](https://developer.apple.com/documentation/gamekit/gkleaderboardscore): 리더보드에서 플레이어가 기록한 점수 정보입니다.
:::

:::topic-grid
## 도전 과제
- [Rewarding players with achievements](https://developer.apple.com/documentation/gamekit/rewarding-players-with-achievements): 도전 과제를 사용해 플레이어의 동기를 높이고 게임 참여를 늘립니다.
- [GKAchievement](https://developer.apple.com/documentation/gamekit/gkachievement): 플레이어가 게임 목표를 향해 진행하고 목표에 도달할 때 수여할 수 있는 도전 과제입니다.
- [GKAchievementDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription): 도전 과제를 플레이어에게 표시할 때 사용하는 텍스트와 아트워크를 담는 객체입니다.
:::

:::topic-grid
## 챌린지
- [Creating engaging challenges from leaderboards](https://developer.apple.com/documentation/gamekit/creating-engaging-challenges-from-leaderboards): 게임에 챌린지를 추가해 친근한 경쟁을 유도합니다.
- [Choosing a leaderboard for your challenges](https://developer.apple.com/documentation/gamekit/choosing-a-leaderboard-for-your-challenges): 챌린지를 구성할 때 어떤 게임플레이가 잘 맞는지 이해합니다.
- [GKChallengeDefinition](https://developer.apple.com/documentation/gamekit/gkchallengedefinition): 챌린지를 위해 정의한 정적 메타데이터를 나타내는 객체입니다.
- [GKShowChallengeBanners](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GKShowChallengeBanners): GameKit이 게임 안에서 챌린지 배너를 표시할 수 있는지 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 활동
- [Creating activities for your game](https://developer.apple.com/documentation/gamekit/creating-activities-for-your-game): 활동 기능으로 게임 콘텐츠를 플레이어에게 노출하고 서로 연결되도록 장려합니다.
- [GKGameActivity](https://developer.apple.com/documentation/gamekit/gkgameactivity): 현재 게임의 단일 활동 인스턴스를 나타내는 객체입니다.
- [GKGameActivityDefinition](https://developer.apple.com/documentation/gamekit/gkgameactivitydefinition): 활동을 위해 정의한 정적 메타데이터를 나타내는 객체입니다.
- [GKGameActivityListener](https://developer.apple.com/documentation/gamekit/gkgameactivitylistener): 활동 이벤트에 응답하는 객체입니다.
:::

:::topic-grid
## 실시간 게임
- [Creating real-time games](https://developer.apple.com/documentation/gamekit/creating-real-time-games): 여러 플레이어가 실시간으로 상호 작용하는 게임을 개발합니다.
- [Finding multiple players for a game](https://developer.apple.com/documentation/gamekit/finding-multiple-players-for-a-game): 실시간 게임에 참여할 다른 플레이어를 찾고 초대합니다.
- [Exchanging data between players in real-time games](https://developer.apple.com/documentation/gamekit/exchanging-data-between-players-in-real-time-games): 실시간 멀티플레이어 게임에서 플레이어 사이에 데이터를 주고받습니다.
- [Adding voice chat to multiplayer games](https://developer.apple.com/documentation/gamekit/adding-voice-chat-to-multiplayer-games): 멀티플레이어 게임에서 모든 플레이어 또는 일부 플레이어 그룹 간 음성 채팅을 활성화합니다.
- [Finding players for custom server-based games](https://developer.apple.com/documentation/gamekit/finding-players-for-custom-server-based-games): 호스팅 매치를 갖는 게임 세션을 만들어 사용자 정의 서버 기반 게임에 플레이어를 연결합니다.
- [Matchmaking rules](https://developer.apple.com/documentation/gamekit/matchmaking-rules): Game Center는 최적의 매치를 찾기 위해 사용자가 만든 여러 규칙 유형을 특정 순서로 적용합니다.
- [GKMatchRequest](https://developer.apple.com/documentation/gamekit/gkmatchrequest): 실시간 또는 턴 기반 매치를 만들기 위한 매개변수를 캡슐화하는 객체입니다.
- [GKMatchmaker](https://developer.apple.com/documentation/gamekit/gkmatchmaker): 플레이어에게 인터페이스를 보여 주지 않고 다른 플레이어와 매치를 생성하는 객체입니다.
- [GKMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller): 플레이어가 실시간 게임에 다른 플레이어를 초대하고 비어 있는 슬롯을 자동 매칭으로 채울 수 있게 해 주는 인터페이스입니다.
- [GKInviteEventListener](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener): Game Center의 초대 이벤트를 처리하는 protocol입니다.
- [GKInvite](https://developer.apple.com/documentation/gamekit/gkinvite): 다른 플레이어가 로컬 플레이어에게 보낸 매치 참여 초대입니다.
- [GKMatch](https://developer.apple.com/documentation/gamekit/gkmatch): Game Center에 로그인한 플레이어 그룹 사이의 peer-to-peer 네트워크입니다.
:::

:::topic-grid
## 턴 기반 게임
- [Creating turn-based games](https://developer.apple.com/documentation/gamekit/creating-turn-based-games): 여러 플레이어가 차례대로 플레이하고 자기 차례를 기다리면서 데이터를 주고받을 수 있는 게임을 개발합니다.
- [Starting turn-based matches and passing turns between players](https://developer.apple.com/documentation/gamekit/starting-turn-based-matches-and-passing-turns-between-players): Game Center가 턴 기반 게임의 매치 데이터를 저장하고 플레이어 사이에 전달하게 합니다.
- [Sending messages to players in turn-based games](https://developer.apple.com/documentation/gamekit/sending-messages-to-players-in-turn-based-games): 메시지와 게임 데이터를 보내 매치 이벤트를 플레이어에게 알립니다.
- [Exchanging data between players in turn-based games](https://developer.apple.com/documentation/gamekit/exchanging-data-between-players-in-turn-based-games): 플레이어가 차례를 기다리는 동안 게임 데이터를 교환하고 메시지를 보낼 수 있게 합니다.
- [GKTurnBasedMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller): 플레이어가 턴 기반 매치에 다른 플레이어를 초대하고 비어 있는 슬롯을 자동 매칭으로 채울 수 있게 하는 인터페이스입니다.
- [GKTurnBasedMatch](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch): 플레이어가 차례대로 진행하는 게임의 매치 데이터를 캡슐화하는 객체입니다.
- [GKTurnBasedParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant): 턴 기반 매치의 참가자입니다.
- [GKTurnBasedEventListener](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener): 매치 참가자 사이의 턴 기반 및 데이터 교환 이벤트를 처리하는 protocol입니다.
- [GKTurnBasedExchange](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange): 턴 기반 매치에서 참가자가 보내는 교환 요청 정보입니다.
- [GKTurnBasedExchangeReply](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply): 교환 요청에 대한 수신자의 응답 세부 정보입니다.
- [GKGameCenterBadgingDisabled](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GKGameCenterBadgingDisabled): GameKit이 턴 기반 게임 아이콘에 배지를 추가할 수 있는지 나타내는 Boolean 값입니다.
:::

:::topic-grid
## 오류
- [GKError](https://developer.apple.com/documentation/gamekit/gkerror): 이 프레임워크가 사용하는 오류 구조체입니다.
- [GKError.Code](https://developer.apple.com/documentation/gamekit/gkerror/code): GameKit 오류 도메인을 위한 오류 코드입니다.
- [GKErrorDomain](https://developer.apple.com/documentation/gamekit/gkerrordomain): 일반적인 게임 오류를 위한 오류 도메인입니다.
:::

:::topic-grid
## 지원 중단
- [Deprecated symbols](https://developer.apple.com/documentation/gamekit/deprecated-symbols): 더 이상 지원하지 않는 심볼과 그 대체 항목을 검토합니다.
:::
