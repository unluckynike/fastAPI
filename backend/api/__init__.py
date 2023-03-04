#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：22304
@Date    ：2023/3/4 9:23
'''
from fastapi import FastAPI
from .v1 import v1

app = FastAPI()

app.include_router(v1, prefix="/api")
