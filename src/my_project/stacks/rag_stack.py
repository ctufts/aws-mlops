import aws_cdk as cdk
from constructs import Construct

class RagStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        cdk.Tags.of(self).add("Project", "MLOps")
