from botocore.exceptions import ClientError
def check_public_access(bucket_name, s3_client):
    try:
        response = s3_client.get_public_access_block(Bucket=bucket_name)
        config = response['PublicAccessBlockConfiguration']
        issues = []
        if not config.get('BlockPublicAcls', False):
            issues.append("BlockPublicAcls is disabled.")
        if not config.get('IgnorePublicAcls', False):
            issues.append("IgnorePublicAcls is disabled.")
        if not config.get("BlockPublicPolicy", False):
            issues.append("BlockPublicPolicy is disabled.")
        if not config.get("RestrictPublicBuckets", False):
            issues.append("RestrictPublicBuckets is disabled.")            
        if issues:
            return {"check": "Public Access Block", "status": "FAIL", "issues": issues}
        return {"check": "Public Access Block", "status": "PASS", "issues": []}
    except ClientError:
        return {"check": "Public Access Block", "status": "FAIL", "issues": ["No Public Access Block configuration found."]}
    except Exception as e:
        return {"check": "Public Access Block", "status": "ERROR", "issues": [str(e)]}