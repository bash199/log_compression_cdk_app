import aws_cdk as core
import aws_cdk.assertions as assertions

from log_file_uploadd.log_file_uploadd_stack import LogFileUploaddStack

# example tests. To run these tests, uncomment this file along with the example
# resource in log_file_uploadd/log_file_uploadd_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LogFileUploaddStack(app, "log-file-uploadd")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
