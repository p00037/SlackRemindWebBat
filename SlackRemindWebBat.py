import requests
import json

#POST先URL
url = "https://hooks.slack.com/services/XXXXXX/XXXXXX/XXXXXXX"

#JSON形式のデータ
json_data = {
    "channel": "#botテスト",
    "text": "pythonでメッセージを送信"
}    

#POST送信
response = requests.post(
    url,
    data = json.dumps(json_data)    #dataを指定する
    )