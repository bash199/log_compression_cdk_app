#!/usr/bin/env python3
import os

import aws_cdk as cdk

from log_file_uploadd.log_file_uploadd_stack import ApiGatewayStack
from log_file_uploadd.lambda_stack import LambdaStack

app = cdk.App()
lambda_stack = LambdaStack(app, "LambdaStack")
ApiGatewayStack(app, "ApiGatewayStack", lambda_function=lambda_stack.process_log_file_upload)

app.synth()
