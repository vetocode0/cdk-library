#!/usr/bin/env python3
import os
import aws_cdk as cdk

from lambda_gateway.lambda_gateway_stack import LambdaGatewayStack


app = cdk.App()
LambdaGatewayStack(app, "LambdaGatewayStack", 
                   env=cdk.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"],
                                        region=os.environ["CDK_DEFAULT_REGION"]))

app.synth()
