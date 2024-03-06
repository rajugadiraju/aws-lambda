#!/bin/bash

# Stop the Lambda function
aws lambda update-function-configuration --function-name myLambda --state "Inactive"
