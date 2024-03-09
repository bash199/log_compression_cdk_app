import re
import json
import os
import logging
import uuid
import boto3 


logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def handler(event, context):

    logger.info(f"Received event: {json.dumps(event, indent=2)}")
    
    if 'body' not in event:
        return {
            'statusCode': 400,
            'body': 'Error: Request body is missing'
        }
    
    file_content = event['body']

    if not file_content:
        return {
            'statusCode': 400,
            'body': 'Error: Request body is empty'
        }
        
    if not is_log_file_content(file_content):
        print("This file does not appear to contain log-like content.")

        return {
            'statusCode': 400,
            'body': 'Error: This file does not appear to contain log-like content.'
        }

    print("This file seems to contain log-like content.")

    bucket_name = os.environ['uncompressed_bucket']

    unique_key = str(uuid.uuid4()) + '.log'
    
    s3.put_object(
        Bucket=bucket_name,
        Key=unique_key,
        Body=file_content.encode('utf-8') 
    )

    return {
        "statusCode": 200,
        "body": json.dumps(f"successfuly uploaded, key: {unique_key}")
    }


def is_log_file_content(content):
    log_patterns = [
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',  # Timestamp pattern
        r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',   # IP address pattern
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',          # Another IP address pattern
        r'\b(GET|POST|PUT|DELETE)\b',            # HTTP methods
        r'\b\d{3}\b',                             # HTTP status codes
        r'\b(INFO|ERROR|WARNING)\b'              # Log levels
    ]

    for pattern in log_patterns:
        if re.search(pattern, content):
            print(re.search(pattern, content))
            return True
    return False

