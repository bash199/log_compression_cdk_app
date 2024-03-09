import json
import os
import logging
import gzip
import boto3 


logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

def handler(event, context):

   logger.info(f"Received event: {json.dumps(event, indent=2)}")
   if not event["Records"][0]["s3"]["object"]:
      logger.error(f'event Records is Falsy: {event["Records"][0]["s3"]["object"]}')
      return
   
   uploaded_object = event["Records"][0]["s3"]["object"]
   uploaded_object_key =  uploaded_object["key"]

   uncompressed_bucket_name = os.environ['uncompressed_bucket']
   compressed_bucket_name = os.environ['compressed_bucket']
   
   response = s3.get_object(
      Bucket=uncompressed_bucket_name,
      Key=uploaded_object_key,
   )

   if not response['Body']:
      logger.error(f"Error: response['Body'] is empty or None")
      return 
   
   object_content = response['Body'].read()

   decoded_content = object_content.decode('utf-8')

   print(decoded_content)

   compressed_content = gzip.compress(decoded_content.encode('utf-8'))

   s3.put_object(
      Bucket=compressed_bucket_name,
      Key=uploaded_object_key + '.gz',
      Body=compressed_content
   )
   
   logger.info(f"file_content: {decoded_content}")
   logger.info(f"Log file successfuly compressed and stored in the appropriate bucket: {compressed_content}")
