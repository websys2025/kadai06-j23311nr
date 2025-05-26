import requests

#ユーザID
App_ID = "dd51ee6a94ef6f8c88f630ca11e90b0909e39a1a"
#取得するデータのURL
#景気動向指数を取得
App_URL = f"http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData?appId={App_ID}&lang=J&statsDataId=0003446461&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0"

#URLからデータを取得しresponseへ代入
response = requests.get(App_URL)
#responseをjson形式を読み込みjsonに代入
json = response.json()
#データを出力
print(json)