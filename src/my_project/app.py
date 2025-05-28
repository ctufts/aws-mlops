#!/usr/bin/env python3
import aws_cdk as cdk
from my_project.stacks.network_stack import NetworkStack
from my_project.stacks.api_stack import ApiStack
from my_project.stacks.inference_stack import InferenceStack
from my_project.stacks.rag_stack import RagStack
from my_project.stacks.async_stack import AsyncStack
from my_project.pipelines.pipeline_stack import PipelineStack

app = cdk.App()

NetworkStack(app, "NetworkStack")
ApiStack(app, "ApiStack")
InferenceStack(app, "InferenceStack")
RagStack(app, "RagStack")
AsyncStack(app, "AsyncStack")
PipelineStack(app, "PipelineStack")

app.synth()
