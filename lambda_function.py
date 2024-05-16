import json
import boto3

client = boto3.client('s3')
def lambda_handler(event, context):
	response = client.get_object (
	Bucket = 'bucket', 
	Key = 'key', 
)

	json_data = response['Body'].read()
	print(json_data)
	print(type(json_data))
