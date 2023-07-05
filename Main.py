# coding: utf-8
# Your code here!

# 文
PLAIN = "YZKXZBPKQEUTIEKTCKDSPK ZWTNIKZQKBPWLDTZYKWDO"
#PLAIN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

# 鍵
#KEY = 16

# print(ord("A")) => 65
# アルファベット26文字 + 半角スペース = 27文字
for KEY in range(27):
    
    enc = ""
    for char in list(PLAIN):
        nume = 0
        ASCII = ord(char)
        if char != " ":
            num = ASCII - 65
        else:
            num = 26
        
        num = (num + KEY) % 27
        ASCII = num + 65
        if ASCII == 91:
            enc += " "
        else:
            enc += chr(ASCII)
    if 'RELATION' in enc:
        print(enc)
        print(KEY)
