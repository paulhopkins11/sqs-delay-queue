# sqs-delay-queue

This project was created to demonstrate the use of LocalStack in testing Lambda and SQS. This project has 2 Lambda functions, producer and consumer. It creates a 60s delay queue. 

## Running with Localstack

### Terminal 1

1. `docker-compose up` in terminal 1 to stand up localstack 

### Terminal 2

1. `bash init.sh` to create queues and lambdas
2. `awslocal lambda invoke --function-name producer outfile.txt` to initiate the producer

Now monitor Terminal 1. You will see output from the producer lambda. Then after 60s you will see the output from the consumer lambda. For example

```
localstack    | > Delay is 61317ms or 61.317s
```


## Update the lambda code 
1. `bash update.sh` once you have edited the lambda .py files

## Tear Down
1. `bash teardown.sh` to remove the lambdas and queue
2. `CTRL+C` on Terminal 1 to stop localstack
