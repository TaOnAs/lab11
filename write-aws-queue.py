# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import requests

r = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
str = r.content.split(':',1)

queue_name = sys.argv[1]
message = sys.argv[2]



# Get the keys from a specific url and then use them to connect to AWS Service 
access_key_id = str[0]
secret_access_key = str[1]

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# delete a queue

m = Message()

m.set_body(message)

queue = conn.get_queue(queue_name)

queue.write(m)

print "Message " + message + " writen to queue " + queue_name

