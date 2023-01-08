import json
import urllib.request
import os
import random

def lambda_handler(event, context):
    # TODO implement
    
    jokes = ["Why was the math book sad? it had too many problems", "My uncle named his dogs Timex and Rolex. They're his watch dogs.",
    "How do you open a banana? With a mon-key.", "I was going to tell a time traveling joke, but you guys didn't like it."]
    
    joke = random.choice(jokes)
    
    message = {
        
        "text": joke
        
    }
    
    hdr = {'Content-Type': 'application/json; charset=utf-8'}
    
    req = urllib.request.Request(os.environ["MY_WEBHOOK"], json.dumps(message).encode('utf-8'), hdr)
    response = urllib.request.urlopen(req)
    response.read()
    
    return {
        'statusCode': 200,
    }
