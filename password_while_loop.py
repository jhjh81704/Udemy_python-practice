# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:35:09 2019

@author: user
"""

password = 'a123456'
i = 3  # 剩餘機會

while True:
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功 !')
        break # 離開 loop
        
    else:
        i -= 1
        print('密碼錯誤 !  還有', i, '次機會')
        if i == 0:
            break