from aws_cdk import (
    aws_apigateway as apigateway,
    Stack
)
from constructs import Construct

class ApiGatewayStack(Stack):

    def __init__(self, scope: Construct, id: str, lambda_function, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        api = apigateway.RestApi(
            self, "UplaodFileApiGateway",
            rest_api_name="Upload Log Files API",
            description="API endpoint for uploading and storing log files."
        )

        
        lambda_integration = apigateway.LambdaIntegration(lambda_function)

        
        resource = api.root.add_resource("logfiles")

        resource.add_method(
            "POST",
            lambda_integration,
            api_key_required=False 
        )
