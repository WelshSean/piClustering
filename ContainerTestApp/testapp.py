"""
Test app to run inside containers and post hearbeat messages to SQS queues
Needs boto3 installed and configured to use an IAM account with write permissions to the relevant SQS Q
"""
import platform

import boto3
import platform
import datetime



def daemonLoop(queueName = 'heartbeat'):
    HostName = platform.uname()[1]
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=queueName)

    response = queue.send_message(MessageBody='Heartbeat: ' + HostName, MessageAttributes={
    'Node': {
        'StringValue': HostName,
        'DataType': 'String'
    },
    'DateTime' : { 
        'StringValue': str(datetime.datetime.now()),
        'DataType' : 'String'
    }

})

if __name__ == '__main__':
    daemonLoop()
