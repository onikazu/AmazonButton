import json
import os
import logging

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    webhook_url = os.environ['WEBHOOK_URL']
    user_name = os.environ['USER_NAME']

    click_type = event['deviceEvent']['buttonClicked']['clickType']
    if click_type == "SINGLE":
        msg = "１回押されました"
    elif click_type == "DOUBLE":
        msg = "２回連続で押されました"
    elif click_type == "LONG":
        msg = "長押しされました"

    slack_message = {
        'username': user_name,
        'icon_emoji': ':face_with_thermometer:',
        'text': msg
    }

    req = Request(webhook_url, json.dumps(slack_message).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted.")
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
