import logging
import json
from Packages.test import lambda_handler1
#from test import lambda_handler1
#import requests


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    logger.debug(event)
    
    city_name = event["currentIntent"]["slots"]["city"]
    #print(city_name)
    content = lambda_handler1(event, context, city_name)
    
    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": content
            }
        }
    }
