import json
import unittest
import requests
from ddt import ddt, data, unpack


@ddt
class req(unittest.TestCase):
    # def setUp(self):
    #     print('测试用例开始执行')
    #
    # def tearDown(self):
    #     print('测试用例执行完毕')

    def __init__(self):
        super().__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/103.0.0.0 Safari/537.36"}

    @data(("http://127.0.0.1:4523/m1/753985-0-default/user/0", {'password': '1222'}))
    def test_post(self, url, params):
        try:
            r = requests.post(url, params, headers=self.headers)
            json_requests = json.loads(r.text)
            print(r.status_code, json_requests)
            # assert r.status_code == 200
            # return json_requests, r.status_code
            assert r.status_code == 200
        except Exception as e:
            # demo_Log().log().info('post请求出错，出错原因：', e)
            print('post请求出错，出错原因：', e)

    @data("http://127.0.0.1:4523/m1/753985-0-default/user/3")
    def test_get(self, url):
        r = requests.get(url, headers=self.headers)
        r.encoding = 'UTF-8'
        json_requests = json.loads(r.text)
        print(r.status_code, json_requests)
        # assert r.status_code == 200
        # return json_requests
        assert r.status_code == 200

    def deldata(self, url, params):
        del_data = requests.delete(url, params, headers=self.headers)
        json_requests = json.loads(del_data.text)
        return json_requests

    def putdata(self, url, params):
        try:
            data = json.dump(params)
            me = requests.put(url, data)
            json_requests = json.loads(me.text)
            return json_requests
        except Exception as e:
            # demo_Log().log().info('put请求出错，出错原因：%s' % e)
            print('put请求出错，出错原因：%s' % e)


if __name__ == "__main__":
    unittest.main()
