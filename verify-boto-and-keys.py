import boto
import requests

def main():
	verify()
	keys()
def verify():

	print boto.Version 

def keys():
	r = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
	str = r.content.split(':',1)
	
	print "Access Key ID: " + str[0]
	print "Secret Access Key: " + str[1]

if __name__ == '__main__':
	main()
