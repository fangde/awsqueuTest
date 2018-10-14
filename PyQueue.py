import boto3

sqs=boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='TestQueue')

print queue.url

res=queue.send_message(MessageBody="What the fuck")


print res
