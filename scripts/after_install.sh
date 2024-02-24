#!/bin/bash

# Update Lambda function code with the new deployment package
aws lambda update-function-code --function-name MyLambdaFunction --zip-file fileb://lambda_function.zip

# Optional: You can also update the Lambda function configuration here if needed
# Example: aws lambda update-function-configuration --function-name MyLambdaFunction --timeout 30 --handler lambda_function.handler

echo "After installation script executed successfully"
