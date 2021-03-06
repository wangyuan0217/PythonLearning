# -*- coding: utf-8 -*-
import base64
import json

from Crypto.Cipher import AES

AES_SECRET_KEY = '9f6f96516581acc0'  # 此处16|24|32个字符

# padding算法
BS = len(AES_SECRET_KEY)
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[0:-ord(s[-1:])]


class AES_ENCRYPT(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    # 加密函数
    def encrypt(self, text, iv):
        cryptor = AES.new(self.key.encode("utf8"), self.mode, iv.encode("utf8"))
        self.ciphertext = cryptor.encrypt(bytes(pad(text), encoding="utf8"))
        # AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题，使用base64编码
        return base64.b64encode(self.ciphertext).decode("utf-8")

    # 解密函数
    def decrypt(self, text):
        decode = base64.b64decode(text)
        cryptor = AES.new(self.key.encode("utf8"), self.mode, IV.encode("utf8"))
        plain_text = cryptor.decrypt(decode)
        return unpad(plain_text)


if __name__ == '__main__':
    aes_encrypt = AES_ENCRYPT()
    dict1 = {"phone": "13295287698", "type": "login"}
    jsonStr = json.dumps(dict1, separators=(',', ':'))
    # jsonStr = "abcd"
    print(jsonStr, type(jsonStr))

    result = aes_encrypt.encrypt(jsonStr, "JDbshISoFOrInPMc")
    print(result, type(result))

    param = {'value': result, 'iv': 'JDbshISoFOrInPMc'}
    paramStr = json.dumps(param, separators=(',', ':'))
    paramEnd = base64.b64encode(paramStr.encode('utf-8')).decode("utf-8")
    print(paramEnd, type(paramEnd))
