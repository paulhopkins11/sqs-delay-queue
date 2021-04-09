awslocal lambda delete-function --function-name producer --region eu-west-2
awslocal lambda delete-function --function-name consumer --region eu-west-2
awslocal sqs delete-queue --queue-url http://localhost:4566/000000000000/test_queue
