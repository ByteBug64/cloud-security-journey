# 01 — Secure Static Website Deployment

**Stack:** AWS S3 · CloudFront · GitHub Actions · IAM
**Status:** ✅ Complete

---

## Overview

Securely hosts a static website using a private S3 bucket behind CloudFront with Origin Access Control (OAC). Direct public access to S3 is fully blocked. Deployment is automated via GitHub Actions CI/CD.

---

## Architecture

```
GitHub Actions → S3 (private) → CloudFront (OAC) → Users (HTTPS)
```

---

## Security Design

- All public access blocked on S3
- CloudFront is the **only** allowed reader via OAC
- IAM policy scoped to: `s3:PutObject`, `s3:GetObject`, `s3:ListBucket`
- No root account usage
- HTTPS enforced by default

---

## CI/CD Workflow

**Trigger:** Push to `main` branch

**Steps:**
1. Checkout code
2. Configure AWS credentials
3. Sync files to S3
4. CloudFront cache invalidation

---

## Validation

| Test | Result |
|------|--------|
| CloudFront URL loads site | ✅ Pass |
| S3 direct URL access | ❌ 403 AccessDenied |
| HTTPS enforced | ✅ Pass |

---

## Key Learnings

- CloudFront OAC is more secure than legacy Origin Access Identity (OAI)
- CI/CD eliminates manual deployment errors
- Even simple projects can follow security best practices

---

## Screenshots

See [`screenshots/`](./screenshots/)
