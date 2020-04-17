#!/usr/bin/env python
#coding=utf-8

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:  # 整除，i 是 n 的因數，所以 n 不是質數。
            return False
    return True     # 都沒有人能整除，所以 n 是質數。

n = int(input('Input a number: '))  # 得到輸入值 n。

for i in range(2, n + 1):   # 產生 2 到 n 的數字。
    i_is_prime = is_prime(i)    # 判斷 i 是否為質數。
    if i_is_prime:              # 如果是，印出來。
        print(i)