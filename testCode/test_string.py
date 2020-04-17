#!/usr/bin/env python3
# -*- coding:utf-8 -*-

name = 'abcdeabcde';

# 首字母大寫
print(name.capitalize())

# 計算字母出現數
print(name.count('a'))

# 自動補字
print(name.center(20, "-"))

# 是否以xx結尾
print(name.endswith("de"))
print(name.endswith("ce"))

# 算長度
print(len(name))

# 找位置
print(name.find("de"))

# format
name2 = '123 {a} 345 {b}'
print(name2.format(a='d', b='e'))

# 是否為英文+數字的組合
print('123'.isalnum())
print('123＿'.isalnum())
print('123abc'.isalnum())
print('123哎'.isalnum()) # True !
print('123_'.isalnum())
print('123-'.isalnum())
print('--')
# 是否都是英文
print('123'.isalpha())
print('123＿'.isalpha())
print('123abc'.isalpha())
print('123哎'.isalpha()) # True !
print('123_'.isalpha())
print('123-'.isalpha())
print('abc'.isalpha())