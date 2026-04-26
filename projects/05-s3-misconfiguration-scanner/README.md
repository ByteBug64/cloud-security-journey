# 05 — S3 Misconfiguration Scanner

**Stack:** Python · Boto3 · AWS S3
**Status:** ✅ Complete

---

## Overview

Scans all S3 buckets in an AWS account and reports any that are publicly exposed, missing encryption, or have overly permissive bucket policies. Misconfigured S3 buckets are one of the leading causes of cloud data breaches — this tool helps prevent that.

---

## What It Scans

| Check | Risk if Failed |
|-------|----------------|
| Public access block settings | Data exposed to the internet |
| Bucket ACL permissions | Unauthorized access to objects |
| Server-side encryption | Data readable if storage is compromised |
| Bucket policy scope | Overly broad access grants |

---

## How to Use

```bash
# Install dependencies
pip install boto3

# Configure AWS credentials
aws configure

# Run the scanner
python s3_scanner.py
```

## Sample Output

```
[CRITICAL] my-bucket-1 — Public access block is DISABLED
[WARNING]  my-bucket-2 — Encryption is NOT enabled
[OK]       my-bucket-3 — No issues found
```

---

## Key Learnings

- Most real-world cloud breaches trace back to misconfigurations, not sophisticated exploits
- S3 has multiple overlapping access controls — all must be checked
- Automated scanning beats manual reviews every time

---

## Files

| File | Description |
|------|-------------|
| `s3_scanner.py` | Main script |
| `README.md` | This file |
