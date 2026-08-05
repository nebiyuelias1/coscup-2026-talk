# Building Native Mobile Apps Using Rails 💎📱
> **COSCUP 2026 Presentation** by Neba ([@nebiyuelias1](https://github.com/nebiyuelias1))

A Slidev presentation exploring how to build iOS and Android native apps from your existing Ruby on Rails codebase using **Hotwire Native**.

---

## 🌐 Live Presentation & PDF Export

- **Live Web Presentation**: Deployed automatically via GitHub Actions to GitHub Pages.
- **Download PDF**: Available under **GitHub Actions Artifacts** as `presentation-pdf` or downloadable directly from your GitHub Pages URL at `/slides.pdf`.

---

## 🛠️ Local Development

```bash
# 1. Install dependencies
pnpm install

# 2. Start local development server
pnpm run dev

# 3. Build static presentation
pnpm run build

# 4. Export presentation to PDF
pnpm exec slidev export --output ./dist/slides.pdf
```

---

## 🚀 GitHub Actions Deployment

The automated workflow located at [`.github/workflows/deploy.yml`](./.github/workflows/deploy.yml) automatically:
1. Installs Node 20 & pnpm.
2. Installs Playwright Chromium for PDF generation.
3. Builds the interactive Slidev web presentation (`dist/`).
4. Exports the PDF slides (`dist/slides.pdf`).
5. Uploads `slides.pdf` as a downloadable GitHub Action Artifact (`presentation-pdf`).
6. Deploys the static web app to **GitHub Pages**.
