#!/usr/bin/env python3
# -*- coding:utf-8 -*-

fileName = 'test.txt'

# 新增file
# f = open(fileName, 'x')
# f.write('hello')
# f.close()

# 寫到最後
f = open(fileName, 'a')
f.write('hello')
f.close()