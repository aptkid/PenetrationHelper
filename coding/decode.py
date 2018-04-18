# encoding: utf-8
import base64
import crypt

def base32_decode (str):
    try:
        return 'base32: ' + base64.b32decode(str)
    except TypeError:
        return 'base32: 解码失败'


def base64_decode (str):
    try:
        return 'base64: ' + base64.b64decode(str)
    except TypeError:
        return 'base64: 解码失败'


def hex_decode (str):
    try:
        return 'hex: ' + str.decode('hex')
    except TypeError:
        return 'hex:    解码失败'

def rot13_decode (str):
    try:
        count = 0;
        bottle = ''
        for temp in str:
            codeTemp = ord(temp)
            if (codeTemp >= 110 or (codeTemp <= 90 and codeTemp >= 78) ):
                bottle = bottle + chr(codeTemp - 13)
            else:
                bottle = bottle + chr(codeTemp + 13)

        return 'rot13:  ' + bottle
    except TypeError:
        return 'rot13:  解码失败'

