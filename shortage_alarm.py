# lambdaの環境変数
# WEBHOOK_URL
#
# IOT1clickのattribute
# name
# place
# goods
# icon_emoji

import os
import json
import logging
import urllib.request
import urllib.parse


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    webhook_url = os.environ.get('WEBHOOK_URL')

    logger.info('Received event: ' + json.dumps(event))

    click_type = event['deviceEvent']['buttonClicked']['clickType']

    # クリック回数によるアクション変更
    if click_type == "SINGLE":
        text = '''
        %s で %s が不足しています。補充をお願いします。
        ''' % (
            event["placementInfo"]["attributes"].get("place"),
            event["placementInfo"]["attributes"].get("goods"),
        )
    else:
        text = '''
        %s での %s 補充が完了しました。
        ''' % (
            event["placementInfo"]["attributes"].get("place"),
            event["placementInfo"]["attributes"].get("goods"),
        )

    body = {
        "link_names": 1,
        'username': event["placementInfo"]["attributes"].get("name", "AWS IoT"),
        'text': text,
        'icon_emoji': event["placementInfo"]["attributes"].get("icon_emoji", ":aws:")
    }

    encoded_post_data = urllib.parse.urlencode({"payload": body}).encode(encoding='ascii')
    urllib.request.urlopen(url=webhook_url, data=encoded_post_data)
