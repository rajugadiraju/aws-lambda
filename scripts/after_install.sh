#!/bin/bash

# Install dependencies
pip3 install -r requirements.txt

# Zip the Lambda function code
zip -r lambda_function.zip lambda_function.py
