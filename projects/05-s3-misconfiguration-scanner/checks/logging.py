def check_logging(bucket_name, s3_client):
    try:
        response = s3_client.get_bucket_logging(Bucket = bucket_name)
        if response.get('LoggingEnabled'):
            return{"check": "Bucket Logging", "status": "PASS", "issues": []}
        return {"check" : "Bucket Logging", "status": "FAIL", "issues": ["Bucket logging is not enabled."]}
    except Exception as e:
        return {"check": "Bucket Logging", "status": "ERROR", "issues": [str(e)]}
        