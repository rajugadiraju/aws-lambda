import json

def factorial(n):
    """
    Calculates the factorial of a positive integer n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def lambda_handler(event, context):
    try:
        num = int(event["queryStringParameters"]["num"])
        if num < 0:
            response = {
                "statusCode": 400,
                "body": json.dumps("Please enter a positive integer.")
            }
        else:
            result = factorial(num)
            response = {
                "statusCode": 200,
                "body": json.dumps({"result": result})
            }
    except ValueError:
        response = {
            "statusCode": 400,
            "body": json.dumps("Invalid input. Please enter a valid positive integer.")
        }
    
    return response