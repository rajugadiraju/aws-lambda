#!/bin/bash

# Update the Lambda function with the new code
aws lambda update-function-code --function-name mylambda --zip-file fileb://lambda_function.zip
