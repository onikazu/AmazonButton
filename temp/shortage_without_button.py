import json
import os
import logging

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


# webhook_url = os.environ['WEBHOOK_URL']
# # button_name = event["placementInfo"]["attributes"].get("name")
# place  = event["placementInfo"]["attributes"].get("place")
# shortage_goods  = event["placementInfo"]["attributes"].get("goods")

# click_type = event['deviceEvent']['buttonClicked']['clickType']
# if click_type == SINGLE':
#     msg = '{0}で{1}が不足しています。支給補充お願いします'.format(place, shortage_goods)
# else:
#     msg = '{0}での{1}の補給が完了しました'.format(place, shortage_goods)

webhook_url = <url>
place = 'place'
shortage_goods = 'goods'
button_name = 'not button'
msg = '{0}で{1}が不足しています。支給補充お願いします'.format(place, shortage_goods)

slack_message = {
    'username': button_name,
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
