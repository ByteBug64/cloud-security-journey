import json
from botocore.exceptions import ClientError
def check_bucket_policy(bucket_name, s3_client):
    try:
        response = s3_client.get_bucket_policy(Bucket = bucket_name)
        policy = json.loads(response['Policy'])
        statements = policy['Statement']
        issues = []
        for statement in statements:
            if statement['Effect'] == 'Allow' and statement['Principal'] == "*":
                issues.append("Bucket policy allows public access.")
        if issues:
            return {"check": "Bucket Policy", "status": "FAIL", "issues": issues}
        return {"check": "Bucket Policy", "status": "PASS", "issues": []}
    except ClientError:
        return {"check": "Bucket Policy", "status": "FAIL", "issues": ["No bucket policy found."]}
