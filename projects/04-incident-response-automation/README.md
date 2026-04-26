# 04 — Incident Response Automation

**Stack:** Python · Boto3 · AWS IAM · AWS EC2
**Status:** ✅ Complete

---

## Overview

When a compromised IAM user or EC2 instance is detected, this script automatically contains the threat — revoking credentials, isolating the instance from the network, and sending an alert. Built to reduce response time from minutes to seconds.

---

## What It Does

| Action | Method |
|--------|--------|
| Revoke compromised IAM credentials | Detach policies + disable access keys |
| Isolate EC2 instance | Replace security group with a deny-all group |
| Alert on containment | Console output with timestamp and resource ID |

---

## Why This Matters

Manual incident response is too slow. Every second a compromised credential stays active is a second an attacker can cause more damage. Automation is how real blue teams operate at scale.

---

## How to Use

```bash
# Install dependencies
pip install boto3

# Configure AWS credentials
aws configure

# Run against a compromised resource
python ir_automation.py --user <iam-username> --instance <instance-id>
```

---

## Key Learnings

- Containment speed is everything in incident response
- Isolating a resource (not deleting it) preserves forensic evidence
- AWS APIs make it possible to respond to threats programmatically

---

## Files

| File | Description |
|------|-------------|
| `ir_automation.py` | Main script |
| `README.md` | This file |
