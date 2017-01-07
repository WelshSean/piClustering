"""
Test app to run inside containers and post hearbeat messages to SQS queues
Needs boto3 installed and configured to use an IAM account with write permissions to the relevant SQS Q
"""
import platform

import boto3
import platform
import datetime
import signal
import time
import sys

def SignalHandler(signum, frame):
    print "You sent an exit signal - exiting cleanly, see you next time!"
    sys.exit(0)

def daemonLoop(queueName = 'heartbeat'):
    HostName = platform.uname()[1]
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName=queueName)

    signal.signal(signal.SIGINT, SignalHandler)
    signal.signal(signal.SIGTERM, SignalHandler)
    while 1:
        time.sleep(10)
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
