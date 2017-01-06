"""
Test app to run inside containers and post hearbeat messages to SQS queues
Needs boto3 installed and configured to use an IAM account with write permissions to the relevant SQS Q
"""

import boto3



def daemonLoop(queueName = 'heartbeat'):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=queueName)
    response = queue.send_message(MessageBody='test from python script')
   


if __name__ == '__main__':
    daemonLoop()
