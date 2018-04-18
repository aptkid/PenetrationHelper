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
        
    except TypeError:
        return 'rot13:  解码失败'

