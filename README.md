# AmazonButton
## 概要
AWS IoT Buttonを押すとスラックに不足品についての通知が入るプログラム。  
一度押しで不足品の通知、二度押しまたは、長押しで補給の完了の通知を入れることができる。

## 使い方
- amazonLambda関数にshortage_alarm.py の中身を登録する。  
その時環境変数にwebhookURLを設定しておく。
- amazon1clickにボタンを登録し、ボタンクリック時のアクションに前述のLambda関数を登録する。  
その時属性値としてgoods, place, nameを登録する。
- ボタンを押すとスラックに設定されたメッセージが送信される。

## 注意事項
権限等の問題によりうまくボタンを登録できないこともあるので注意



## 参考資料
- コード
http://tech.studyplus.co.jp/entry/2018/05/23/100857

- クリック時のアクション差別化
https://qiita.com/hayao_k/items/0a8b3197ae7b2595ea10

- icon_emoji チートシート
https://slackmojis.com/

- webhookURLの取得手順
https://qiita.com/vmmhypervisor/items/18c99624a84df8b31008

- ボタンの動作確認方法
https://dev.classmethod.jp/cloud/aws/aws-iot-enterprise-button/

- amazon_purchase.pyの参考資料
https://foolean.net/p/1174
