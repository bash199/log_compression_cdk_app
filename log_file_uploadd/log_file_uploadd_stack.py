# from aws_cdk import (
#     Stack,
#     aws_lambda as _lambda,
#     aws_apigateway as apigateway
# )

# from constructs import Construct
# from aws_solutions_constructs.aws_apigateway_lambda import ApiGatewayToLambda

# class LogFileUploaddStack(Stack):

#     def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
#         super().__init__(scope, construct_id, **kwargs)
        
#         lambda_process_file_upload = _lambda.Function(self, "ProcessFileUplaod",
#                               runtime=_lambda.Runtime.PYTHON_3_12,
#                               handler="process_file_upload.handler",
#                               code=_lambda.Code.from_asset("lambda"))
        
        
#         apigateway.LambdaRestApi()
#         ApiGatewayToLambda(self, 'ApiGatewayToLambdaPattern',
#             lambda_function_props=_lambda.FunctionProps(
#                 runtime=_lambda.Runtime.PYTHON_3_9,
#                 handler='index.handler',
#                 code=_lambda.Code.from_asset('lambda')
#             ))
     
# #

from aws_cdk import (
    aws_apigateway as apigateway,
    Stack
)

from constructs import Construct
class ApiGatewayStack(Stack):

    def __init__(self, scope: Construct, id: str, lambda_function, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create API Gateway
        api = apigateway.RestApi(
            self, "UplaodFileApiGateway",
            rest_api_name="My API",
            description="This is my API Gateway"
        )

        # Create Lambda integration
        lambda_integration = apigateway.LambdaIntegration(lambda_function)

        # Create resource
        resource = api.root.add_resource("logfiles")

        # Add POST method to the resource
        resource.add_method(
            "POST",
            lambda_integration,
            api_key_required=False  # You can set it to False if you don't need API key
        )
