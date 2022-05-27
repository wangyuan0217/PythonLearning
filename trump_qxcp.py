import base64
import json
import random
import sys

import requests
# from sendNotify import send

from AESCipher import AES_ENCRYPT


def printf(text):
    print(text)
    sys.stdout.flush()


def create_order(param):
    url = 'https://qx.pinbs.cn/api/go/order/create'
    headers = {
        'Cookie': 'acw_tc=0bca314e16534420182556121e0158968d7abed60c2e3955133080eb99dd70',
        'User-Agent': 'okhttp/3.12.13',
        'Accept-Encoding': 'gzip',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'oaid': '6259f5ab976a01ba',
        'device': 'Ava7LfIRTQVGceMjPaJuwZO5ZJ2F4V8UDpEUHYXxxryk',
        'channel': '1',
        'platform': 'Android',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNjk4Njc5OGI4Y2U2YWZmYWIwYmRiOTI0OTI2ZWMyM2Y1ZjI1NjUwZTk2OTQ5YjZmNWZlMzMxYmU1Y2U4ZjU2NjI4OWQyN2QyNzRkYjE3NzciLCJpYXQiOjE2NTMzODI1MjQsIm5iZiI6MTY1MzM4MjUyNCwiZXhwIjoxNjg0OTE4NTI0LCJzdWIiOiIxMjIyNjg1Iiwic2NvcGVzIjpbXX0.iMeLt1FKI0_mY-YiOrSAv5HKoRtAKlDyKfzRMIWFU3VpDKbTc0MRLV-WzReCgdf09qlsU4SgX-Uh1p3Ywh0lnTE0TCz3KXQylKnsWuFqH-AXRPI6cu2WF1-GFWQduqVPI0dqt2K4QNvFMW9IMfUZAEAOGDAyHgxozRBKEMR6PPUGoVQhqUYF7BYMj9c6ZSsbt-7c74j2r63MSMpho2IAmtYRd_q_zt_Zg_E4BVjMfkB_z5CYtdZ9FszdwOopFP4ydZyco3YP5dBW74fH50GXcqhmShe8Ve9RNejX02Bn91QI6Tm7RX-4yDy4KGPIcuSDAcCKogsmX-OzuKVesmLp_TxdOGdOcaeLdGmXc48bhD1U3CqaTOIQNA6Wc-Wtd0SF-cKM5Mklcqg9T7o3xLIBLsY8MLJM_w8uGaXHBvqyh7Ru0HQ3KLwwblM3bqSnDYap8FnnwTqyg0HcNw_FialITTtbFGSO9clsV84LTIrxudYPeszd-QnfJWyW7L232Vne9d9oMywOAOPMT45RxXnv9RLHFSfQix6vd8BrG3o9eZ7EJ0grdgqSigVr1lJur47PhOWXb2crE0Re2ykq7z3N-TPn3p951xGIgz3UiWvXS933_grxQvZMXifH6ypIWLTxzCGUEsoIgVHUYMYdo7S36ZNTrKzf4YzXOVmjm8z5hHA'
    }
    formData = {'s__': param}
    printf('trump request url ' + url)
    printf('trump request formData ' + str(formData))
    resp = requests.post(url, headers=headers, data=str(formData)).json()
    printf('trump response ' + str(resp))
    if resp['code'] == "0":
        printf('trump --> 订单创建成功')
    else:
        printf('trump --> 订单创建失败')
    # send('创建订单', str(resp))

def main():
    iv = ""
    for i in range(16):
        ran = random.randint(1, 9)
        iv += str(ran)
    paramOrigin = {"id": "190", "user_id": "1222685"}
    jsonStr = json.dumps(paramOrigin, separators=(',', ':'))

    aes = AES_ENCRYPT()
    aesResult = aes.encrypt(jsonStr, iv)
    param = {'value': aesResult, 'iv': iv}
    paramStr = json.dumps(param, separators=(',', ':'))
    paramEnd = base64.b64encode(paramStr.encode('utf-8')).decode("utf-8")

    printf('trump param iv ' + iv)
    printf('trump param jsonStr ' + jsonStr)
    printf('trump param aesResult ' + aesResult)
    printf('trump param paramStr ' + paramStr)
    printf('trump param paramEnd ' + paramEnd)
    printf('trump 开始创建订单')
    create_order(paramEnd)

import pip
if __name__ == '__main__':
    main()
    # a = pip.pep425tags.get_supported()
    # print(a)
