import json
import pandas

def lambda_handler(event, context):
    name = event.get('name', 'World')
    greeting = f'Hello, {name}!'
    return {
        'statusCode': 200,
        'body': greetings Idiot
    }
