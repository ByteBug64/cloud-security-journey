def check_versioning(bucket_name, s3_client):
    try:
        response = s3_client.get_bucket_versioning(Bucket = bucket_name)
        status = response.get('Status', "")
        if status == "Enabled":
            return{"check": "Bucket Versioning", "status": "PASS", "issues": []}
        return {"check": "Bucket Versioning", "status": "FAIL", "issues": ["Bucket versioning is not enabled."]}
    except Exception as e:
        return {"check": "Bucket Versioning", "status": "ERROR", "issues": [str(e)]}