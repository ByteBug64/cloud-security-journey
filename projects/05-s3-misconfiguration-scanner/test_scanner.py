import pytest
import boto3
import moto
from checks.acl import check_bucket_acl
from checks.bucket_policy import check_bucket_policy
from checks.encryption import check_encryption
from checks.logging import check_logging
from checks.public_access import check_public_access
from checks.versioning import check_versioning
from moto import mock_aws

@mock_aws
def test_public_access_block_fail():
    s3 = boto3.client('s3', region_name="us-west-2")
    s3.create_bucket(
    Bucket="test-bucket",
    CreateBucketConfiguration={"LocationConstraint": "us-west-2"}
)
    result = check_public_access("test-bucket", s3)
    assert result["status"] == "FAIL"

@mock_aws
def test_encryption_fail():
    s3 = boto3.client('s3', region_name = "us-west-2")
    s3.create_bucket(
        Bucket = "test-bucket",
        CreateBucketConfiguration = {"LocationConstraint": "us-west-2"}
    )    
    result = check_encryption("test-bucket", s3)
    assert result["status"] == "FAIL"

@mock_aws
def test_versioning_fail():
    s3 = boto3.client('s3', region_name = "us-west-2")
    s3.create_bucket(
        Bucket = "test-bucket",
        CreateBucketConfiguration = {"LocationConstraint": "us-west-2"}
    )    
    result = check_versioning("test-bucket", s3)
    assert result["status"] == "FAIL"

@mock_aws
def test_logging_fail():
    s3 = boto3.client('s3', region_name = "us-west-2")
    s3.create_bucket(
        Bucket = "test-bucket",
        CreateBucketConfiguration = {"LocationConstraint": "us-west-2"}
    )    
    result = check_logging("test-bucket", s3)
    assert result["status"] == "FAIL"

@mock_aws
def test_bucket_policy_fail():
    s3 = boto3.client('s3', region_name = "us-west-2")
    s3.create_bucket(
        Bucket = "test-bucket",
        CreateBucketConfiguration = {"LocationConstraint": "us-west-2"}
    )    
    result = check_bucket_policy("test-bucket", s3)
    assert result["status"] == "FAIL"

@mock_aws
def test_bucket_acl_fail():
    s3 = boto3.client('s3', region_name = "us-west-2")
    s3.create_bucket(
        Bucket = "test-bucket",
        CreateBucketConfiguration = {"LocationConstraint": "us-west-2"}
    )    
    result = check_bucket_acl("test-bucket", s3)
    assert result["status"] == "PASS"        