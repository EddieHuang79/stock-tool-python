#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from system import system
from user import user

# 開瀏覽器
system.openBrowser(system, "http://scm.docker.kkday.com/v1/zh-tw/auth/login")

# 登入
user.login(user)

# 選供應商
user.chooseSupplier(user)

# 登出
user.logout(user)

# 關瀏覽器
system.closeBrowser(system)