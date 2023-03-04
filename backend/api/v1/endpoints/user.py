
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi 
@File    ：user.py
@IDE     ：PyCharm 
@Author  ：22304 @Date    ：2023/3/4 9:25
'''
from  fastapi import APIRouter

user=APIRouter(tags=['用户相关'])

@user.get("/user",summary="当前用户")
async def user_info():
    pass

@user.put("/user",summary="修改信息")
async def user_update():
    pass

__all__=[
    "user"
]