#! /usr/bin/env python
# encoding: utf-8

import sys
import decode

if __name__ ==  "__main__":
    if len(sys.argv) == 3:
        if (sys.argv[1] == 'encode'):
            print('编码' + sys.argv[2])
        elif (sys.argv[1] == 'decode'):
            print(decode.base32_decode(sys.argv[2]))
            print(decode.base64_decode(sys.argv[2]))
            print(decode.hex_decode(sys.argv[2]))
            print(decode.rot13_decode(sys.argv[2]))
        else:
            print('参数错误，请检查输入')

    else:
        print('例子：python penetrationHelper')

