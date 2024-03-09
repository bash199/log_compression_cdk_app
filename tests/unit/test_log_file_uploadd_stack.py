import aws_cdk as core
import aws_cdk.assertions as assertions

from log_file_uploadd.log_file_uploadd_stack import ApiGatewayStack
from log_file_uploadd.lambda_stack import LambdaStack

def test_api_gateway_stack():
    app = core.App()
    lambda_stack = LambdaStack(app, "LambdaStack")
    stack = ApiGatewayStack(app, "log-file-uploadd", lambda_function=lambda_stack.process_log_file_upload)
    template = assertions.Template.from_stack(stack)
    template.resource_count_is('AWS::ApiGateway::RestApi', 1)

def test_lambda_stack():
    app = core.App()
    lambda_stack = LambdaStack(app, "LambdaStack")
    template = assertions.Template.from_stack(lambda_stack)
    template.resource_count_is('AWS::S3::Bucket', 2)
    template.resource_count_is('AWS::Lambda::Function', 3)
