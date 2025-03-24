from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy
)
from constructs import Construct

class AwsDevopsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an S3 bucket
        bucket = s3.Bucket(
            self,
            "cdk-code-catalyst",
            bucket_name="testing",  # Replace with your desired bucket name
            versioned=True,  # Enable versioning
            encryption=s3.BucketEncryption.S3_MANAGED,  # Enable encryption
            removal_policy=RemovalPolicy.DESTROY  # Optional: This will allow CDK to delete the bucket when you destroy the stack
        )
