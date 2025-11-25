import boto3
import sys
from botocore.exceptions import ClientError, NoCredentialsError, NoRegionError

def validate_credentials():
    """General AWS credential check using STS."""
    try:
        sts = boto3.client("sts")
        identity = sts.get_caller_identity()
        print(f"✅ AWS credentials valid. Using identity: {identity['Arn']}")
        return True
    except NoCredentialsError:
        print("❌ No AWS credentials found. Please configure environment variables or AWS profile.")
    except NoRegionError:
        print("❌ No AWS region configured. Please set AWS_DEFAULT_REGION or configure your profile.")
    except ClientError as e:
        print(f"❌ AWS credentials invalid or missing permissions: {e}")
    sys.exit(1)
