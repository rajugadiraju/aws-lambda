#!/bin/bash

# Download the Lambda deployment package from S3
aws s3 cp s3://dafdfedfad/lambda_function.zip /tmp/lambda_function.zip

# Update the Lambda function with the new code
aws lambda update-function-code --function-name mylambda --zip-file fileb:///tmp/lambda_function.zip
