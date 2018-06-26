# lambdaの環境変数
# LOGIN_ID
# LOGIN_PASSWORD
#
# aws IoT 1clickのattribute
# url_single
# url_double
# url_long
# limit_value_single
# limit_value_double
# limit_value_long

import os
import time
from datetime import datetime
from selenium import webdriver


def lambda_handler(event, context):
    # ログイン情報
    LOGIN_ID = os.environ['LOGIN_ID']
    LOGIN_PASSWORD = os.environ['LOGIN_PASSWORD']

    # 販売元情報
    ACCEPT_SHOP = 'Amazon'

    # 時間表示関数
    def l(str):
        print("%s : %s"%(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),str))

    # 購入処理関数
    def buy(url, LIMIT_VALUE):
        # ブラウザの起動
        try:
            b = webdriver.Chrome('./chromedriver')
            b.get(url)
        except:
            l('Failed to open browser.')
            exit()

        while True:
            # 在庫確認
            while True:
                try:
                    # 販売元確認
                    shop = b.find_element_by_id('merchant-info').text
                    shop = shop.split('が販売')[0].split('この商品は、')[1]

                    if ACCEPT_SHOP not in shop:
                        raise Exception("not Amazon.")

                    # カートに入れる
                    b.find_element_by_id('add-to-cart-button').click()
                    break
                except:
                    time.sleep(60)
                    b.refresh()

            # 購入手続き
            b.get('https://www.amazon.co.jp/gp/cart/view.html/ref=nav_cart')
            b.find_element_by_name('proceedToCheckout').click()

            # ログイン
            try:
                b.find_element_by_id('ap_email').send_keys(LOGIN_ID)
                b.find_element_by_id('ap_password').send_keys(LOGIN_PASSWORD)
                b.find_element_by_id('signInSubmit').click()
            except:
                l('LOGIN PASS.')
                pass

            # 値段の確認
            p = b.find_element_by_css_selector('td.grand-total-price').text
            if int(p.split(' ')[1].replace(',', '')) > LIMIT_VALUE:
                l('PLICE IS TOO LARGE.')
                continue

            # 注文の確定
            b.find_element_by_name('placeYourOrder1').click()
            break

        l('ALL DONE.')


    # 購入実行
    # 属性ITEM_URLには以下のようなURLを設定
    # ITEM_URL = 'https://www.amazon.co.jp/dp/B01N5QLLT3?ref=emc_b_5_i&th=1'
    # ITEM_URL = 'https://www.amazon.co.jp/dp/B01NCXFWIZ?ref=emc_b_5_i&th=1'

    click_type = event['deviceEvent']['buttonClicked']['clickType']

    if click_type == "SINGLE":
        ITEM_URL = event["placementInfo"]["attributes"].get("url_single")
        LIMIT_VALUE_SINGLE = event["placementInfo"]["attributes"].get("limit_value_single")
        buy(ITEM_URL, LIMIT_VALUE_SINGLE)
    elif click_type == "DOUBLE":
        ITEM_URL = event["placementInfo"]["attributes"].get("url_double")
        LIMIT_VALUE_DOUBLE = event["placementInfo"]["attributes"].get("limit_value_double")
        buy(ITEM_URL, LIMIT_VALUE_DOUBLE)
    elif click_type == "LONG":
        ITEM_URL = event["placementInfo"]["attributes"].get("url_long")
        LIMIT_VALUE_LONG = event["placementInfo"]["attributes"].get("limit_value_long")
        buy(ITEM_URL, LIMIT_VALUE_LONG)
