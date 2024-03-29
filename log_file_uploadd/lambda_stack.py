from aws_cdk import (
    aws_lambda as _lambda,
    Stack, 
    aws_s3 as s3,
    aws_s3_notifications as s3_notifications
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
         super().__init__(scope, id, **kwargs)

         uncompressed_log_files_bucket = s3.Bucket(self, "UncompressedLogFiles")
         compressed_log_files_bucket = s3.Bucket(self, "CompressedLogFiles")

         self.process_log_file_upload = _lambda.Function(
            self, "ProcessLogFlieUpload",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="process_file_upload.handler",
            code=_lambda.Code.from_asset("lambda"),
             environment={
                'uncompressed_bucket': uncompressed_log_files_bucket.bucket_name
            }
         )

         self.compress_log_file_stored = _lambda.Function(
            self, "CompressLogFileStored",
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler="compress_file_stored.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
               'uncompressed_bucket': uncompressed_log_files_bucket.bucket_name,
               'compressed_bucket': compressed_log_files_bucket.bucket_name
            }
         )
         
         uncompressed_log_files_bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3_notifications.LambdaDestination(self.compress_log_file_stored))
         

         uncompressed_log_files_bucket.grant_read_write(self.process_log_file_upload)
         uncompressed_log_files_bucket.grant_read(self.compress_log_file_stored)

         compressed_log_files_bucket.grant_read_write(self.compress_log_file_stored)

