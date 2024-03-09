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

   # uncompressed_bucket = os.environ['uncompressed_bucket']
   # compressed_bucket = os.environ['compressed_bucket']

   # file_content = s3.get_object(
   #    Bucket=uncompressed_bucket,
   #    Key=unique_key,
   # )

   

   
   