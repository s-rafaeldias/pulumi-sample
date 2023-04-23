import pulumi
import pulumi_aws as aws
from dataclasses import dataclass


@dataclass
class FMBucketArgs:
    name: str
    product: str
    public: bool = False


class FMBucket(pulumi.ComponentResource):
    def __init__(self, args: FMBucketArgs, opts=None):
        resource_name = f"{args.product}-{args.name}"

        super().__init__("pkg:index:FMBucket", resource_name, None, opts)

        stack = pulumi.get_stack()
        bucket_name = f"{resource_name}-{stack}"

        bucket = aws.s3.Bucket(
            args.name,
            bucket=bucket_name,
            acl="private",
            tags={
                "Environment": stack,
            },
            opts=pulumi.ResourceOptions(parent=self),
        )

        if not args.public:
            aws.s3.BucketPublicAccessBlock(
                args.name,
                bucket=bucket.id,
                block_public_acls=True,
                block_public_policy=True,
                ignore_public_acls=True,
                restrict_public_buckets=True,
                opts=pulumi.ResourceOptions(parent=self),
            )
