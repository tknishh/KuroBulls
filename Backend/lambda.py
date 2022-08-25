from email import policy
from email.parser import BytesParser
import json
import boto3
import io
import os, glob
import pandas as pd

s3Client = boto3.client('s3')

def email_to_dict(file_path):
    with open(file_path, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
    entities = msg.keys()
    emailData= {}
    for entity in entities:
        emailData.update({entity : msg[entity]})
    return emailData

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # print(bucket)
    # print(key)

    response = s3Client.get_object(Bucket=bucket, Key=key)

    
