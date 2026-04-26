def check_bucket_acl(bucket_name, s3_client):
    try:
        response = s3_client.get_bucket_acl(Bucket=bucket_name)
        grants = response['Grants']
        issues = []
        for grant in grants:
            grantee = grant.get('Grantee', {})
            uri = grantee.get('URI', '')
            if 'AllUsers' in uri or 'AuthenticatedUsers' in uri:
                issues.append(f'Bucket ACL grants access to {uri}.')
        if issues:
            return {"check": "Bucket has public ACLs", "status": "FAIL","issues": issues}
        return{"check": "Bucket has no public ACLs", "status":"PASS", "issues":[]}
    except:
        return {"check": "Bucket ACL check", "status": "ERROR", "issues":
                ["Unable to retrieve bucket ACL."]}  