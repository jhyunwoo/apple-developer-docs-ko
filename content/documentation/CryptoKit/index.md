---
route: /documentation/CryptoKit
source_url: https://developer.apple.com/documentation/CryptoKit
source_locale: en-US
section: docc
content_type: symbol
title: Apple CryptoKit
original_title: Apple CryptoKit
source_hash: ac43bc0499cc9ae2f0d835ab98c95787e72d36b2eac40810347b36d681f57a03
canonical_source: manual-translation
last_crawled_at: '2026-03-13T13:26:31+00:00'
last_translated_at: '2026-03-14T00:42:00+09:00'
---

# Apple CryptoKit

암호화 작업을 안전하고 효율적으로 수행합니다.

## 개요

Apple CryptoKit을 사용하면 일반적인 암호화 작업을 수행할 수 있습니다.

- 암호학적으로 안전한 digest를 계산하고 비교합니다.
- 공개 키 암호 방식을 사용해 디지털 서명을 만들고 검증하며, 키 교환을 수행합니다. 메모리에 저장된 키뿐 아니라 Secure Enclave에 저장되고 관리되는 개인 키도 사용할 수 있습니다.
- 대칭 키를 생성하고, 이를 메시지 인증과 암호화 같은 작업에 사용합니다.

하위 수준 인터페이스보다 CryptoKit을 우선적으로 사용하십시오. CryptoKit은 앱이 raw pointer를 직접 관리하지 않도록 해 주며, 메모리 해제 시 민감한 데이터를 덮어쓰는 것처럼 앱을 더 안전하게 만드는 작업을 자동으로 처리합니다.

:::topic-grid
## 핵심 사항
- [Complying with Encryption Export Regulations](https://developer.apple.com/documentation/Security/complying-with-encryption-export-regulations): 앱 심사 과정을 간소화할 수 있도록 앱의 암호화 사용 여부를 신고합니다.
- [Performing Common Cryptographic Operations](https://developer.apple.com/documentation/cryptokit/performing-common-cryptographic-operations): 해시 계산, 키 생성, 암호화 같은 작업을 CryptoKit으로 수행합니다.
- [Storing CryptoKit Keys in the Keychain](https://developer.apple.com/documentation/cryptokit/storing-cryptokit-keys-in-the-keychain): 강한 타입의 암호 키와 기본 keychain 타입 사이를 변환합니다.
- [Enhancing your app’s privacy and security with quantum-secure workflows](https://developer.apple.com/documentation/cryptokit/enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows): 양자 공격으로부터 앱을 보호하기 위해 양자 안전 암호화를 사용합니다.
:::

:::topic-grid
## 암호학적으로 안전한 해시
- [HashFunction](https://developer.apple.com/documentation/cryptokit/hashfunction): 암호학적으로 안전한 해시를 수행하는 타입입니다.
- [SHA512](https://developer.apple.com/documentation/cryptokit/sha512): 512비트 digest를 사용하는 Secure Hashing Algorithm 2(SHA-2) 해시 구현입니다.
- [SHA384](https://developer.apple.com/documentation/cryptokit/sha384): 384비트 digest를 사용하는 Secure Hashing Algorithm 2(SHA-2) 해시 구현입니다.
- [SHA256](https://developer.apple.com/documentation/cryptokit/sha256): 256비트 digest를 사용하는 Secure Hashing Algorithm 2(SHA-2) 해시 구현입니다.
:::

:::topic-grid
## 메시지 인증 코드
- [HMAC](https://developer.apple.com/documentation/cryptokit/hmac): 해시 기반 메시지 인증 알고리즘입니다.
- [SymmetricKey](https://developer.apple.com/documentation/cryptokit/symmetrickey): 대칭 암호 키입니다.
- [SymmetricKeySize](https://developer.apple.com/documentation/cryptokit/symmetrickeysize): 대칭 암호 키가 가질 수 있는 크기입니다.
:::

:::topic-grid
## 암호
- [AES](https://developer.apple.com/documentation/cryptokit/aes): Advanced Encryption Standard(AES) 암호를 담는 컨테이너입니다.
- [ChaChaPoly](https://developer.apple.com/documentation/cryptokit/chachapoly): ChaCha20-Poly1305 암호 구현입니다.
:::

:::topic-grid
## 공개 키 암호화
- [Curve25519](https://developer.apple.com/documentation/cryptokit/curve25519): X25519 키 합의와 Ed25519 서명을 가능하게 하는 타원 곡선입니다.
- [P521](https://developer.apple.com/documentation/cryptokit/p521): NIST P-521 서명과 키 합의를 가능하게 하는 타원 곡선입니다.
- [P384](https://developer.apple.com/documentation/cryptokit/p384): NIST P-384 서명과 키 합의를 가능하게 하는 타원 곡선입니다.
- [P256](https://developer.apple.com/documentation/cryptokit/p256): NIST P-256 서명과 키 합의를 가능하게 하는 타원 곡선입니다.
- [SharedSecret](https://developer.apple.com/documentation/cryptokit/sharedsecret): 여기서 대칭 암호 키를 파생할 수 있는 키 합의 결과입니다.
- [SecureEnclave](https://developer.apple.com/documentation/cryptokit/secureenclave): 기기의 하드웨어 기반 키 관리자 표현입니다.
- [HPKE](https://developer.apple.com/documentation/cryptokit/hpke): 하이브리드 공개 키 암호화(HPKE) 작업을 담는 컨테이너입니다.
:::

:::topic-grid
## 키 파생 함수
- [HKDF](https://developer.apple.com/documentation/cryptokit/hkdf): HMAC 기반 Key Derivation Function(HKDF)의 표준 기반 구현입니다.
:::

:::topic-grid
## 키 캡슐화 메커니즘(KEM)
- [KEM](https://developer.apple.com/documentation/cryptokit/kem): 키 캡슐화 메커니즘입니다.
- [MLKEM768](https://developer.apple.com/documentation/cryptokit/mlkem768): Module-Lattice 키 캡슐화 메커니즘(KEM)입니다.
- [MLKEM1024](https://developer.apple.com/documentation/cryptokit/mlkem1024): Module-Lattice 키 캡슐화 메커니즘(KEM)입니다.
- [XWingMLKEM768X25519](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519): https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06 에 정의된 X-Wing(ML-KEM768 with X25519) 키 캡슐화 메커니즘입니다.
:::

:::topic-grid
## KEM 키
- [KEMPrivateKey](https://developer.apple.com/documentation/cryptokit/kemprivatekey): 키 캡슐화 메커니즘의 개인 키입니다.
- [KEMPublicKey](https://developer.apple.com/documentation/cryptokit/kempublickey): 키 캡슐화 메커니즘의 공개 키입니다.
:::

:::topic-grid
## 오류
- [CryptoKitError](https://developer.apple.com/documentation/cryptokit/cryptokiterror): CryptoKit이 사용하는 일반 암호화 오류입니다.
- [CryptoKitASN1Error](https://developer.apple.com/documentation/cryptokit/cryptokitasn1error): ASN.1 콘텐츠를 decode하는 동안 발생하는 오류입니다.
:::

:::topic-grid
## 레거시 알고리즘
- [Insecure](https://developer.apple.com/documentation/cryptokit/insecure): 오래되었고 암호학적으로 안전하지 않은 알고리즘을 담는 컨테이너입니다.
:::

:::topic-grid
## 프로토콜
- [DiffieHellmanKeyAgreement](https://developer.apple.com/documentation/cryptokit/diffiehellmankeyagreement): Diffie-Hellman 키 합의 키입니다.
- [HPKEDiffieHellmanPrivateKey](https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanprivatekey): Diffie-Hellman 키 교환의 개인 키를 나타내는 타입입니다.
- [HPKEDiffieHellmanPrivateKeyGeneration](https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanprivatekeygeneration): Diffie-Hellman 키 교환에서 개인 키 생성 과정을 나타내는 타입입니다.
- [HPKEDiffieHellmanPublicKey](https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanpublickey): Diffie-Hellman 키 교환의 공개 키를 나타내는 타입입니다.
- [HPKEKEMPrivateKey](https://developer.apple.com/documentation/cryptokit/hpkekemprivatekey): HPKE의 개인 키를 나타내는 타입입니다.
- [HPKEKEMPrivateKeyGeneration](https://developer.apple.com/documentation/cryptokit/hpkekemprivatekeygeneration): HPKE에서 개인 키 생성 과정을 나타내는 타입입니다.
- [HPKEKEMPublicKey](https://developer.apple.com/documentation/cryptokit/hpkekempublickey): HPKE의 공개 키를 나타내는 타입입니다.
- [HPKEPublicKeySerialization](https://developer.apple.com/documentation/cryptokit/hpkepublickeyserialization): 공개 키를 encode하는 데 사용하는 타입입니다.
:::

:::topic-grid
## 구조체
- [CorecryptoCurveType](https://developer.apple.com/documentation/cryptokit/corecryptocurvetype)
- [SHA3_256](https://developer.apple.com/documentation/cryptokit/sha3_256): 256비트 digest를 사용하는 Secure Hashing Algorithm 3(SHA-3) 해시 구현입니다.
- [SHA3_256Digest](https://developer.apple.com/documentation/cryptokit/sha3_256digest): 256비트 digest를 가진 Secure Hashing Algorithm 3(SHA-3) 해시의 출력입니다.
- [SHA3_384](https://developer.apple.com/documentation/cryptokit/sha3_384): 384비트 digest를 사용하는 Secure Hashing Algorithm 3(SHA-3) 해시 구현입니다.
- [SHA3_384Digest](https://developer.apple.com/documentation/cryptokit/sha3_384digest): 384비트 digest를 가진 Secure Hashing Algorithm 3(SHA-3) 해시의 출력입니다.
- [SHA3_512](https://developer.apple.com/documentation/cryptokit/sha3_512): 512비트 digest를 사용하는 Secure Hashing Algorithm 3(SHA-3) 해시 구현입니다.
- [SHA3_512Digest](https://developer.apple.com/documentation/cryptokit/sha3_512digest): 512비트 digest를 가진 Secure Hashing Algorithm 3(SHA-3) 해시의 출력입니다.
:::

:::topic-grid
## 타입 별칭
- [CryptoKitMetaError](https://developer.apple.com/documentation/cryptokit/cryptokitmetaerror)
- [SHA2_256](https://developer.apple.com/documentation/cryptokit/sha2_256): 256비트 digest를 사용하는 Secure Hashing Algorithm 2(SHA-2) 해시 구현입니다.
- [SHA2_384](https://developer.apple.com/documentation/cryptokit/sha2_384): 384비트 digest를 사용하는 Secure Hashing Algorithm 2(SHA-2) 해시 구현입니다.
- [SHA2_512](https://developer.apple.com/documentation/cryptokit/sha2_512): 512비트 digest를 사용하는 Secure Hashing Algorithm 2(SHA-2) 해시 구현입니다.
:::

:::topic-grid
## 열거형
- [MLDSA65](https://developer.apple.com/documentation/cryptokit/mldsa65): MLDSA65 디지털 서명 알고리즘입니다.
- [MLDSA87](https://developer.apple.com/documentation/cryptokit/mldsa87): MLDSA87 디지털 서명 알고리즘입니다.
:::
