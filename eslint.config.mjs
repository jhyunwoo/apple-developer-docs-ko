import nextCoreWebVitals from "eslint-config-next/core-web-vitals";
import nextTypescript from "eslint-config-next/typescript";

const config = [
  ...nextCoreWebVitals,
  ...nextTypescript,
  {
    ignores: [
      ".cache/**",
      ".generated/**",
      ".next/**",
      "next-env.d.ts",
      "node_modules/**",
      "out/**",
      "public/__mirror__/**",
      "public/__search__/**"
    ]
  }
];

export default config;
