#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi 
@File    ：login.py
@IDE     ：PyCharm 
@Author  ：22304
@Date    ：2023/3/4 9:24 
'''
from fastapi import APIRouter

login = APIRouter(tags=['认证相关'])


@login.post("/login", summary='登录')
async def user_login():
    pass
