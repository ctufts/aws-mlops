import pytest
from aws_cdk import App
from my_project.stacks.api_stack import ApiStack

def test_api_stack_synth():
    app = App()
    stack = ApiStack(app, "TestApiStack")
    assert stack is not None
