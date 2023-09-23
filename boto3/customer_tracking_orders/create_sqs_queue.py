# Import the boto3 library, which allows interaction with AWS services.
import boto3

# Create an SQS client using boto3.
sqs = boto3.client('sqs')

# Use the SQS client to create a new queue with the specified QueueName.
response = sqs.create_queue(
    QueueName='project_queue')

# Print the URL of the newly created queue.
print('QueueURL: ', response['QueueUrl'])
