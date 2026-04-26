import boto3
from checks.acl import check_bucket_acl
from checks.bucket_policy import check_bucket_policy
from checks.encryption import check_encryption
from checks.logging import check_logging
from checks.public_access import check_public_access
from checks.versioning import check_versioning
from report.generator import print_terminal_report, generate_htmlreport
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description = "S3 Bucket Misconfiguration Scanner")
    parser.add_argument('--profile', help="AWS profile name", default = None) 
    parser.add_argument('--region', help = "AWS region name", default = None)
    parser.add_argument('--output', help = "Output format: terminal, html, or both", default = "both")
    parser.add_argument('--bucket', help = "Scan a specific bucket only", default = None)
    return parser.parse_args()

def get_all_buckets(s3_client):
    response = s3_client.list_buckets() 
    return [bucket["Name"] for bucket in response.get("Buckets", [])]
def scan_bucket(bucket_name, s3_client):
    findings = []
    findings.append(check_bucket_acl(bucket_name, s3_client))
    findings.append(check_bucket_policy(bucket_name, s3_client))
    findings.append(check_encryption(bucket_name, s3_client))
    findings.append(check_logging(bucket_name, s3_client))
    findings.append(check_public_access(bucket_name, s3_client))
    findings.append(check_versioning(bucket_name, s3_client))
    return findings
def run_scanner(profile = None, region = None, bucket = None):
    session = boto3.Session(region_name = region, profile_name = profile)
    s3_client = session.client('s3')
    buckets = get_all_buckets(s3_client)
    if bucket is not None:
        buckets = [bucket]
    results = []
    for bucket_name in buckets:
        results.append({"bucket": bucket_name, "findings": scan_bucket(bucket_name, s3_client)})
    return results
if __name__ == "__main__":
    args = parse_arguments()
    results = run_scanner(args.profile, args.region, args.bucket)
    if args.output == "terminal":
        print_terminal_report(results)
    elif args.output == "html":
        generate_htmlreport(results)
    else:
        print_terminal_report(results)
        generate_htmlreport(results)        
