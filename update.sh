awslocal lambda update-function-code --function-name producer --region eu-west-2 --zip-file fileb://producer.zip 
awslocal lambda update-function-code --function-name consumer --region eu-west-2 --zip-file fileb://consumer.zip

# awslocal sqs send-message --message-attributes file://message-attributes.json --message-body="lets put some stuff in here" --queue-url "http://localhost:4576/queue/test_queue"
# awslocal sqs receive-message --queue-url "http://localhost:4576/queue/test_queue"
