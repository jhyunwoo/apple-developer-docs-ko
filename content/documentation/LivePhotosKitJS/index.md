---
route: /documentation/LivePhotosKitJS
source_url: https://developer.apple.com/documentation/LivePhotosKitJS
source_locale: en-US
section: docc
content_type: symbol
title: LivePhotosKit JS
original_title: LivePhotosKit JS
source_hash: 96d59d7aad992fbe7a2ca46f322f2b13060322d2850fbc9d7f4edd2b3c09dd32
canonical_source: manual-translation
last_crawled_at: '2026-03-13T08:39:32+00:00'
last_translated_at: '2026-03-13T17:10:00+09:00'
---

# LivePhotosKit JS

웹에서 Live Photo를 재생합니다.

## 개요

LivePhotosKit JS 라이브러리를 사용해 웹 페이지에서 Live Photo를 재생할 수 있습니다.

JavaScript API는 플레이어를 이미지나 비디오 태그와 비슷한 DOM element 형태로 제공하며, 이 element는 사진 및 비디오 리소스와 기타 옵션으로 구성할 수 있습니다. 재생 제어는 라이브러리를 사용하는 개발자가 프로그램적으로 수행할 수도 있고, 브라우저의 최종 사용자가 미리 제공된 컨트롤을 통해 수행할 수도 있습니다.

### 시작하기 전에

1. 웹 페이지에 LivePhotosKit JS를 포함합니다.

script 태그를 사용하고 Apple이 호스팅하는 LivePhotosKit JS 버전에 대한 링크 [https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js](https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js)`.` 를 연결합니다.

```javascript
<script src="https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js"></script>
```

:::note Note
LivePhotosKit JS 버전 번호는 URL에 포함되어 있습니다. 예를 들어 `1`은 LivePhotosKit JS 1.0.0을 의미합니다.
:::

1. JavaScript strict mode를 활성화합니다.

스크립트 전체에 strict mode를 활성화하려면 다른 어떤 문장보다 먼저 `‘use strict’`를 넣으십시오.

```javascript
 'use strict';
```

:::note Note
LivePhotosKit JS는 NPM을 통해서도 사용할 수 있습니다. [https://www.npmjs.com/package/livephotoskit](https://www.npmjs.com/package/livephotoskit)을 참고하십시오.

설치 명령은 다음과 같습니다.

`npm install --save livephotoskit`
:::

### 선언형 HTML

페이지에 LivePhotosKit JS 스크립트를 포함하면, HTML에 선언형 마크업을 추가하는 것만으로 플레이어를 만들 수 있습니다. 페이지가 로드되면 LivePhotosKit JS가 페이지에 있는 플레이어 인스턴스를 판별하고 초기화합니다. 자식 노드를 지원하는 어떤 HTML 태그든 사용할 수 있습니다.

최소한 각 태그에는 `data-live-photo` 속성과 0이 아닌 height 및 width가 필요합니다. 이렇게 하면 LivePhotosKit JS가 플레이어로 초기화할 DOM element를 찾을 수 있습니다.

그런 다음 각각 `data-photo-src`, `data-video-src` 속성을 설정해 사진과 비디오 구성 요소의 위치를 지정할 수 있습니다.

선택적으로 다음 추가 data attribute를 사용할 수 있습니다.

- `data-photo-time`: 제공된 비디오 구성 요소의 시작 시점부터 정지 사진이 촬영된 시점까지의 타임스탬프입니다.
- `data-proactively-loads-video`: 사용자나 개발자가 재생을 시작하려고 시도하기 전에 Player가 `data-video-src`에 지정된 바이트를 다운로드할지 여부입니다.
- `data-shows-native-controls`: 사용자를 위한 재생 컨트롤을 활성화할지 여부입니다.

Player로 지정된 각 DOM element에는 재생 컨트롤이 장식처럼 추가됩니다.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <script src="https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js"></script>
    </head>
    <body>
        <div
            data-live-photo
            data-photo-src="https://..."
            data-video-src="https://..."
            style="width: 320px; height: 320px">            
        </div>
    </body>
</html>
```

### JavaScript API

기존 DOM element를 감싸는 방식으로 호출하거나, 인수 없이 호출해 새로운 DOM element를 생성하는 방식으로 새로운 [LivePhotosKit.Player](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/livephotoskit.player)를 만듭니다.

```javascript
// A Player built from a new DIV:
const myNewPlayer = LivePhotosKit.Player();
document.body.appendChild(myNewPlayer);
// A Player built from a pre-existing element:
LivePhotosKit.Player(document.getElementById('myExistingElement'));
```

Player를 생성한 후에는 네이티브 이미지나 비디오 element를 사용할 때처럼 프로퍼티와 메서드를 사용해 이를 설정하고 사용할 수 있습니다.

플레이어는 다음 이벤트를 발생시킵니다.

- [canplay](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player#canplay): Player가 원활한 재생에 충분한 비디오 프레임을 확보했고 그 속도도 충분할 때 발생합니다.
- [error](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player#error): Live Photo의 사진 구성 요소 또는 비디오 구성 요소 중 하나의 로드에 실패했을 때 발생합니다.
- [ended](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player#ended): Live Photo 재생이 완료되었을 때 발생합니다.
- [videoload](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player#videoload): Live Photo의 비디오 구성 요소 로드가 완료되었을 때 발생합니다.
- [photoload](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player#photoload): Live Photo의 사진 구성 요소 로드가 완료되었을 때 발생합니다.

```javascript
// Create the player using a pre-existing DOM element.
const player = LivePhotosKit.Player(document.getElementById('my-live-photo-target-element'));
player.photoSrc = 'https://...';
player.videoSrc = 'https://...';
// Listen to events the player emits.
player.addEventListener('canplay', evt => console.log('player ready', evt));
player.addEventListener('error', evt => console.log('player load error', evt));
player.addEventListener('ended', evt => console.log('player finished playing through', evt));
// Use the playback controls.
player.playbackStyle = LivePhotosKit.PlaybackStyle.HINT;
player.playbackStyle = LivePhotosKit.PlaybackStyle.FULL;
player.play();
player.pause();
player.toggle();
player.stop();
// Seek the animation to one quarter through.
player.currentTime = 0.25 * player.duration;
// Seek the animation to 0.1 seconds into the Live Photo.
player.currentTime = 0.1;
```

### 오류 처리

Player는 로드 또는 재생 시 오류가 발생하면 `error` 이벤트를 발생시킵니다. Player에 오류가 발생하면 공개 프로퍼티 [errors](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player/errors)에도 오류를 게시하여 현재 오류 상태인지, 그렇다면 어떤 오류가 발생했는지를 전달합니다.

오류 상태는 [LivePhotosKit.Errors](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.errors)에서 확인할 수 있습니다.

```javascript
player.addEventListener('error', (ev) => {
    if (typeof ev.detail.errorCode === 'number') {
        switch (ev.detail.errorCode) {
        case LivePhotosKit.Errors.IMAGE_FAILED_TO_LOAD:
            // Do something
            break;
        case LivePhotosKit.Errors.VIDEO_FAILED_TO_LOAD:
            // Do something
            break;
        }
    } else {
        // Extract error.
        console.error(ev.detail.error);
    }
})
```

### 브라우저 호환성

LivePhotosKit JS 플레이어는 다음 브라우저를 지원합니다.

| Device | Browser |
| --- | --- |
| iOS | Safari, Chrome |
| macOS | Safari, Chrome, Firefox |
| Android (performance depends on device) | Chrome (beta) |
| Windows | Chrome, Firefox, Edge, Internet Explorer 11 |

### Live Photo asset을 얻는 방법

Live Photo는 두 가지 구성 요소로 이루어집니다. 하나는 정지 사진이고, 다른 하나는 사진이 촬영되기 직전과 직후의 순간을 담은 비디오입니다. 아래 방법 중 하나를 사용하면 정지 사진을 JPG로, 비디오를 MOV 파일로 얻을 수 있습니다.

:::important Important
asset이 크면 다운로드에 오랜 시간이 걸립니다. 사진이 너무 오래 걸리면 진행 배지를 표시할 수 없습니다. 이 문제를 피하려면 플레이어로 장식될 element에 명시적으로 height와 width를 지정해야 합니다. asset 크기를 줄이면 성능이 크게 향상되고 대역폭 사용량도 줄어듭니다.
:::

샘플 프로젝트도 [available](https://developer.apple.com/library/content/samplecode/UsingPhotosFramework/Introduction/Intro.html) 합니다.

#### macOS Photos 사용

- iOS 기기를 Mac에 연결합니다.
- Photos 앱으로 사진을 가져옵니다.
- 내보내려는 Live Photo를 선택합니다.
- File > Export > Export Unmodified Original을 사용해 파일 시스템으로 내보냅니다.

#### macOS Image Capture 사용

- iOS 기기를 Mac에 연결합니다.
- 기기에서 로컬 파일 시스템으로 가져오려는 Live Photo를 선택합니다.
- 대상 폴더를 선택하고 Import를 클릭합니다.

#### Windows 10 File Explorer 사용

- Windows용 iTunes가 설치되어 있는지 확인합니다. 다음 링크에서 다운로드할 수 있습니다. [http://www.apple.com/itunes/download/](http://www.apple.com/itunes/download/)
- File Explorer를 엽니다. Windows 키와 E 키를 동시에 눌러 열 수 있습니다.
- iOS 기기를 PC에 연결합니다.
- “This PC” 폴더에 iOS 기기가 나타나야 합니다.
- 다음 폴더로 이동합니다. `(your device) > Internal Storage > DCIM` 그리고 가져오려는 Live Photo를 찾습니다.
- Live Photo는 JPG 파일과 MOV 파일 한 쌍으로 저장됩니다.
- 파일 쌍을 로컬 파일 시스템으로 드래그합니다.

:::topic-grid
## 클래스
- [LivePhotosKit](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit): LivePhotosKit 라이브러리의 네임스페이스입니다.
- [LivePhotosKit.Player](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player): Live Photo용 플레이어입니다.
:::

:::topic-grid
## 열거형
- [LivePhotosKit.Errors](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.errors): LivePhoto 재생 중 발생할 수 있는 오류입니다.
- [LivePhotosKit.PlaybackStyle](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.playbackstyle): 가능한 재생 스타일입니다.
- [LivePhotosKit.EffectType](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.effecttype)
:::
