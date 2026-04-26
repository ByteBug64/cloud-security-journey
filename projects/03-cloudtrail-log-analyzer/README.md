# 03 — CloudTrail Log Analyzer

**Stack:** Python · Boto3 · AWS CloudTrail
**Status:** ✅ Complete

---

## Overview

A Python script that pulls AWS CloudTrail logs and automatically flags suspicious activity — root account logins, failed authentication attempts, and unusual API calls. Built to simulate what a real cloud security analyst does during threat detection.

---

## What It Detects

- Root account usage
- Repeated failed `ConsoleLogin` events
- Unusual or high-risk API calls (e.g. `DeleteTrail`, `StopLogging`)
- Activity from unexpected regions or IP addresses

---

## How to Use

```bash
# Install dependencies
pip install boto3

# Configure AWS credentials
aws configure

# Run the analyzer
python cloudtrail_analyzer.py
```

---

## Key Learnings

- CloudTrail is the single most important log source for AWS threat detection
- Understanding what "normal" looks like is the foundation of detecting "abnormal"
- Boto3 makes it straightforward to query and filter AWS logs programmatically

---

## Files

| File | Description |
|------|-------------|
| `cloudtrail_analyzer.py` | Main script |
| `README.md` | This file |
