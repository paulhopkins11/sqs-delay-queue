import json
import os
import boto3
import time

# Create SQS client
# sqs = boto3.client('sqs')
hn = os.environ.get('LOCALSTACK_HOSTNAME', None)
if hn:
    hn = f'http://{hn}:4566'
print(f'LOCALSTACK_HOSTNAME = {hn}')

# sqs = boto3.client('sqs', endpoint_url=os.environ.get('ENDPOINT_URL'))
sqs = boto3.client('sqs', endpoint_url=hn)

# import requests


def lambda_handler(event, context):
    # response = sqs.get_queue_url(
    #     QueueName='sqs-delay-queue-MySqsQueue-1L38PZJQQP3XL')
    # queue_url = response['QueueUrl']
    queue_url = os.environ.get('QUEUE_URL')

    epoch_time = round(time.time() * 1000.0)
    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        # DelaySeconds=30,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'SentTime': {
                'DataType': 'String',
                'StringValue': f'{epoch_time}'
            }
        },
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )

    print(response['MessageId'])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
