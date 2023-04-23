import pulumi
from dataclasses import dataclass
from resources import bucket


@dataclass
class FMFrontendArgs:
    name: str
    product: str


class FMFrontend(pulumi.ComponentResource):
    def __init__(self, args: FMFrontendArgs, opts=None):
        resource_name = f"{args.product}-{args.name}"
        super().__init__("pkg:index:FMFrontend", resource_name, None, opts)

        _source = bucket.FMBucket(
            args=bucket.FMBucketArgs(name=args.name, product=args.product, public=True),
            opts=pulumi.ResourceOptions(parent=self),
        )

        _replica = bucket.FMBucket(
            args=bucket.FMBucketArgs(name=f"{args.name}-replica", product=args.product),
            opts=pulumi.ResourceOptions(parent=self),
        )
