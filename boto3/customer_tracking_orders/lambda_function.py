# Import necessary libraries.
import json
import boto3
import datetime

# AWS Lambda entry point.
def lambda_handler(event, context):
    # Define a timezone with an offset of -5 hours (Central Time).
    cdt_timezone = datetime.timezone(datetime.timedelta(hours=-5))
    
    # Get the current time in the specified timezone.
    current_time = datetime.datetime.now(cdt_timezone)
    
    # Format the current time as a string in a specific format.
    current_time_formatted = current_time.strftime("%d-%b-%Y %H:%M:%S")
    
    # Create an SQS client using boto3.
    sqs = boto3.client('sqs')
    
    # Send a message to the specified SQS queue with the current time as the message body.
    sqs.send_message(
        QueueUrl='YOUR_QUEUE_URL',
        MessageBody=current_time_formatted
)
    
    # Return the response for the Lambda function.
    return {
        'statusCode': 200,  # HTTP status code indicating success.
        'body': json.dumps(current_time_formatted)  # Convert the formatted time to a JSON string and set it as the response body.
    }