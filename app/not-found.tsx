import Link from "next/link";

export default function NotFound() {
  return (
    <main className="not-found-page">
      <div className="not-found-card">
        <span className="landing-pill">404</span>
        <h1>문서를 찾을 수 없습니다.</h1>
        <p>아직 이 경로가 번역 큐에 들어오지 않았거나, 현재 빌드 결과에 포함되지 않았습니다.</p>
        <Link href="/" className="primary-button">
          홈으로 돌아가기
        </Link>
      </div>
    </main>
  );
}
