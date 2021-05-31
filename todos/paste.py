import json
import logging
import os
import time
import uuid
import random
import boto3
dynamodb = boto3.resource('dynamodb')


BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(num, alphabet=BASE62):
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def create(event, context):
    data = json.loads(event['body'])

    hash = random.getrandbits(24)


    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps("http://tinyurl.com/"+encode(hash))
    }

    return response
