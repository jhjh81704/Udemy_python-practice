# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:35:09 2019

@author: user
"""

password = 'a123456'
i = 3  # 剩餘機會

while i > 0:
    i -= 1
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功 !')
        break # 離開 loop
        
    else:
        
        print('密碼錯誤 !')
        if i > 0:
            print('還有', i, '次機會')
        else:
            print('沒機會嘗試了! 要鎖帳號了')