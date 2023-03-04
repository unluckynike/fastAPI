#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：22304
@Date    ：2023/3/4 9:24 
'''
from fastapi import APIRouter
from .endpoints import *

v1 = APIRouter(prefix="/v1")

v1.include_router(login)
v1.include_router(user)
v1.include_router(movie)
