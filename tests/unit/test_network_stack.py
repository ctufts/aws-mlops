import pytest
from aws_cdk import App
from my_project.stacks.network_stack import NetworkStack

def test_network_stack_synth():
    app = App()
    stack = NetworkStack(app, "TestNetworkStack")
    assert stack is not None
