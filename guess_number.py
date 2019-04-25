# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:02:04 2019

@author: user
"""
import random
start = int(input('請決定隨機數字範圍開始值: '))
end = int(input('請決定隨機數字範圍結束值: '))

r = random.randint(start, end)
count = 0

while True:
    count += 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜中了 !')
        print('這次你猜的第', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    
    print('這次你猜的第', count, '次')