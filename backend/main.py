#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：22304
@Date    ：2023/3/3 16:42 
'''
from uvicorn import run

from api import app


if __name__ == '__main__':
    run('main:app', reload=True)