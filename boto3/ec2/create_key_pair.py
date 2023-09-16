import boto3
import os

ec2 = boto3.client('ec2')

key_name ='Key from boto3'
file_name = 'key-from-boto3.pem'

response = ec2.create_key_pair(KeyName=key_name)

with open(file_name, 'w') as f:
    f.write(response["KeyMaterial"])
    
os.chmod(file_name,0o400)