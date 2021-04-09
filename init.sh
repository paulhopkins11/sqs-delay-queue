bash ./package.sh
awslocal sqs create-queue --queue-name test_queue --attributes "DelaySeconds=60"
awslocal lambda create-function --environment Variables="{QUEUE_URL=http://localstack:4566/000000000000/test_queue}" --function-name producer --runtime python3.8 --handler app.lambda_handler --memory-size 128 --zip-file fileb://producer.zip --role arn:aws:iam:awslocal
awslocal lambda create-function --function-name consumer --runtime python3.8 --handler app.lambda_handler --memory-size 128 --zip-file fileb://consumer.zip --role arn:aws:iam:awslocal
awslocal lambda create-event-source-mapping --function-name consumer --event-source-arn arn:aws:sqs:us-east-1:000000000000:test_queue


