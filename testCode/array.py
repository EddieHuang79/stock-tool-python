#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import copy

names = ['1', '2', '3', '4', '5', '6']
names.append('7')
names.insert(2, '8')
names.insert(3, '9')

print(names)
print(names[1:3])
print(names[-1:])
print(names[:3])


# delete methods

# 1. names.remove("Coulson")
names.remove('9')
print(names)
# 2. del names[1] = names.pop(1)
del names[1]
print(names)
# 3. names.pop(1)
names.pop(1)
print(names)

print(names.index('4'))

names.append('7')
print(names.count('7'))

names2 = copy.deepcopy(names)
names2[2] = 99
print(names)
print(names2)

# 跳著使用
print(names[::2])

