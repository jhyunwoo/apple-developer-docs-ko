# Security Best Practices Report

## Executive Summary

이번 Next.js 정적 문서 사이트 레이어를 기준으로 TypeScript, React, Next.js 프런트엔드 보안 관점에서 점검했습니다. 코드 수정 전에는 외부 Markdown을 MDX로 컴파일하는 경로, JSON-LD 스크립트 직렬화, 외부 문서 링크 스킴 처리에 보안상 주의가 필요한 지점이 있었고 이번 변경으로 모두 보완했습니다.

현재 코드 기준으로 남아 있는 주요 리스크는 하나입니다. 정적 export 배포 특성상 런타임 보안 헤더가 애플리케이션 코드에서 강제되지 않으므로, 실제 배포 CDN 또는 정적 호스팅 계층에서 CSP, 클릭재킹 방어, MIME sniffing 방어를 확인해야 합니다.

리포트 위치: `/Users/jhyunwoo/projects/apple-developer-docs-ko/security_best_practices_report.md`

## Medium Severity

### SEC-001

- Rule ID: NEXT / REACT baseline header posture
- Severity: Medium
- Location: [next.config.mjs](/Users/jhyunwoo/projects/apple-developer-docs-ko/next.config.mjs#L1), [app/layout.tsx](/Users/jhyunwoo/projects/apple-developer-docs-ko/app/layout.tsx#L23)
- Evidence:

```ts
const nextConfig = {
  output: "export",
  trailingSlash: true
};
```

```tsx
export const metadata: Metadata = getBaseMetadata();

export default function RootLayout(...) {
  return (
    <html lang="ko" suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: themeInitScript }} />
      </head>
      <body>{children}</body>
    </html>
  );
}
```

- Impact: 배포 CDN 또는 정적 호스트에서 별도 보안 헤더를 주지 않으면 CSP, `frame-ancestors` 또는 `X-Frame-Options`, `X-Content-Type-Options`, `Permissions-Policy` 같은 방어선이 비어 있을 수 있습니다. 그 경우 클릭재킹, MIME sniffing, XSS 방어 심화 전략이 호스팅 기본값에 의존하게 됩니다.
- Fix: 실제 배포 계층에서 최소한 다음을 설정하세요.
  - `Content-Security-Policy`
  - `X-Content-Type-Options: nosniff`
  - `Referrer-Policy: strict-origin-when-cross-origin` 또는 더 엄격한 값
  - `X-Frame-Options: DENY` 또는 CSP `frame-ancestors 'none'`
  - 필요 시 `Permissions-Policy`
- Mitigation: 현재 앱은 정적 export 구조이므로 애플리케이션 코드보다 CDN, object storage, reverse proxy, Vercel/Cloudflare/Netlify 헤더 설정이 실제 보안 경계입니다. 배포 후 `curl -I` 또는 보안 헤더 스캐너로 실측 검증이 필요합니다.
- False positive notes: 배포 플랫폼이 이미 엄격한 보안 헤더를 부여하고 있다면 실제 위험도는 낮아질 수 있습니다. 다만 이 저장소 내부만으로는 확인할 수 없습니다.

## Remediated During This Change

### FIX-001

- Rule ID: REACT-XSS-001 / MDX content execution hardening
- Severity: High before remediation
- Location: [lib/mdx.tsx](/Users/jhyunwoo/projects/apple-developer-docs-ko/lib/mdx.tsx#L30)
- Resolution: 외부 문서 Markdown을 MDX로 컴파일하기 전에 코드펜스 밖의 HTML 태그, MDX 표현식 브레이스, `import`/`export` 구문을 무력화하도록 전처리를 추가했습니다.

### FIX-002

- Rule ID: JS-XSS unsafe URL schemes
- Severity: High before remediation
- Location: [lib/mdx.tsx](/Users/jhyunwoo/projects/apple-developer-docs-ko/lib/mdx.tsx#L14), [lib/mdx.tsx](/Users/jhyunwoo/projects/apple-developer-docs-ko/lib/mdx.tsx#L111)
- Resolution: 문서 본문 링크와 이미지에서 `http:`, `https:`, `mailto:`, `tel:`, 해시, 루트 상대 경로만 허용하도록 제한했고 `javascript:` 같은 위험한 스킴은 렌더링하지 않게 했습니다.

### FIX-003

- Rule ID: REACT-XSS script serialization
- Severity: Medium before remediation
- Location: [components/structured-data.tsx](/Users/jhyunwoo/projects/apple-developer-docs-ko/components/structured-data.tsx#L1)
- Resolution: JSON-LD 직렬화 시 `<`, `>`, `&`, 유니코드 줄 구분자를 이스케이프해서 `</script>` 조기 종료 계열의 스크립트 인젝션 위험을 제거했습니다.

### FIX-004

- Rule ID: REACT navigation hardening
- Severity: Low before remediation
- Location: [lib/mdx.tsx](/Users/jhyunwoo/projects/apple-developer-docs-ko/lib/mdx.tsx#L134)
- Resolution: 외부 링크에 `noopener noreferrer`를 적용해 새 탭 오픈 시 opener 오용 위험을 줄였습니다.
