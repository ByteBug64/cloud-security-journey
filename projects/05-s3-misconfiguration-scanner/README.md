# S3 Bucket Misconfiguration Scanner

## What does this tool do?

This tool is used to Scan S3 Bucket Misconfiguration and check vulnerability

## What does it check for?

This tool checks for misconfiguration in acl, bucket policy, encryption, logging, public_access and versioning

## Who is it for?

This tool is for a Cloud Security engineer who wants to make his work easier, accurate and avoid manual operation in aws console

## Installation

1. Clone or download the project
2. Create a virtual environment
3. Activate it
4. Install dependencies with `pip install -r requirements.txt`
5. Configure AWS credentials with `aws configure`

## Usage

1. `python scanner.py`
2. `python scanner.py --output html`
3. `python scanner.py --bucket my-bucket`
4. `python scanner.py --output both`
5. `python scanner.py --output terminal`

## Disclaimer

This tool is for authorized use only.
Only run it against AWS accounts you own or have permission to scan.
Thanks
