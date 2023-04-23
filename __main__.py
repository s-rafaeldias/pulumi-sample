"""An AWS Python Pulumi program"""

# import pulumi
# from pulumi_aws import s3
from services.frontend import FMFrontend, FMFrontendArgs

_frontend1 = FMFrontend(FMFrontendArgs(name="myName", product="myProduct"))
