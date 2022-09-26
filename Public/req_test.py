import json
import requests
from demoLog import demo_Log


def post():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/103.0.0.0 Safari/537.36"}
    url = 'http://127.0.0.1:4523/m1/753985-0-default/login'
    params = {'password': '1222'}
    try:
        r = requests.post(url, params, headers)
        json_requests = json.loads(r.text)
        return json_requests, r.status_code
    except Exception as e:
        demo_Log().log().info('post请求出错，出错原因：', e)
        print('post请求出错，出错原因：', e)


print(post())
