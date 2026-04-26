from botocore.exceptions import ClientError
def check_encryption(bucket_name, s3_client):
    try:
        response = s3_client.get_bucket_encryption(Bucket = bucket_name)
        return {"check": "Bucket Encryption", "status": "PASS", "issues": []}
    except ClientError as e :   
        if e.response['Error']['Code'] == "ServerSideEncryptionConfigurationNotFoundError":
            return {"check": "Bucket Encryption", "status": "FAIL", "issues": ["Bucket is not encrypted."]}
        else:
            return {"check": "Bucket Encryption", "status": "ERROR", "issues": [str(e)]}

