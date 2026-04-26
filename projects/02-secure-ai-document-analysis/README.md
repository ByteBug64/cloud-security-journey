# 02 — Secure AI Document Analysis

**Stack:** Amazon Bedrock · AWS S3 · IAM · CloudTrail · CloudWatch
**Status:** ✅ Complete

---

## Overview

Demonstrates how to securely integrate AI services on AWS using Amazon Bedrock. Focuses on cloud security best practices — least-privilege IAM, logging, and full observability — applied to an AI workload.

---

## Architecture

```
S3 (encrypted docs) → IAM Role (least privilege) → Amazon Bedrock → CloudTrail + CloudWatch
```

---

## Security Implementation

### IAM Least-Privilege Role
| Permission | Scope |
|------------|-------|
| `s3:GetObject` | Read-only access to documents |
| `bedrock:InvokeModel` | AI model invocation only |
| Admin permissions | ❌ None |
| Wildcard access | ❌ None |

### Secure Storage (S3)
- Encryption enabled at rest
- Public access fully blocked
- Access restricted to IAM role only

---

## Logging & Monitoring

**CloudTrail captures:**
- Who accessed AI (IAM identity ARN)
- When access occurred (timestamp)
- Which service was called (bedrock.amazonaws.com)

**CloudWatch captures:**
- Bedrock model invocation events
- Model ID used
- Region and request metadata

---

## Key Learnings

- AI workloads need the same security discipline as any other cloud service
- Least-privilege IAM is critical even for managed AI services
- CloudTrail + CloudWatch together provide full AI security observability

---

## Screenshots

See [`screenshots/`](./screenshots/)
