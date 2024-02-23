# Define the lambda_handler function
def lambda_handler(event, context):
    print("hello world")
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "hello world"})
    }
    return response

# Call the lambda_handler function with any input
lambda_handler({}, {})
