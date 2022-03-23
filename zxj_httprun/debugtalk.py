import time

from httprunner import __version__
from until.sign import sign_body

def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def register_user():
    """生成注册用户名称"""
    user = "test" + str(int(time.time()))
    time.sleep(1)
    return user



def setup_request(request):
    """请求预处理，sign签名"""
    print("request",request)
    body=request.get("req_json")
    print('body:',body)
    sign = sign_body(body,apikey="12345678")
    print("sign:",sign)
    request["req_json"]["sign"] =sign

def goods_code():
    """随机生成商品编码goodscode"""
    # print(int(time.time()))
    time.sleep(0.1)
    goodscode = "sp_"+str(int(time.time()*100))
    return goodscode


def str_to_int(arg):
    """字符串转int类型"""
    return int(arg)