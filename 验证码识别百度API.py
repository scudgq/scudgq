# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome

import requests
import base64

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=lDo19N0DR4wpQX82vnKEDWyc&client_secret=29XUO6SW2fy9sYefvGvFPrSOmw6Mqiad'
response = requests.get(host)
if response:
    # print(response.json())
    access_token = response.json()['access_token']
    print(access_token)

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('验证码003.png', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}

request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
    result = response.json()['words_result'][0]['words']
    print(result)