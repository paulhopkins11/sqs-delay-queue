import json
import time

# import requests


def lambda_handler(event, context):
    epoch_time = round(time.time() * 1000.0)

    for record in event['Records']:
        print(record)
        payload = record["body"]
        print(str(payload))
        attributes = record["messageAttributes"]
        print(str(attributes))
        sent_epoc = attributes["SentTime"]['stringValue']
        print(f'Sent at {sent_epoc}, processed at {epoch_time}')
        produced = int(sent_epoc)
        consumed = epoch_time
        dif = consumed - produced
        difS = dif / 1000
        print(f'Delay is {dif}ms or {difS}s')
    # return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "hello world",
    #         # "location": ip.text.replace("\n", "")
    #     }),
    # }
