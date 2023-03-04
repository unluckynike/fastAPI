#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi 
@File    ：movie.py
@IDE     ：PyCharm 
@Author  ：22304
@Date    ：2023/3/4 9:25 
'''

from fastapi import APIRouter

movie=APIRouter(tags=['电影相关'])

@movie.get("/movie",summary='列表')
async def movie_list():
    pass

@movie.post("/movie",summary='新增')
async def movie_add():
    pass

@movie.put("/movie",summary='编辑')
async def movie_edit():
    pass

@movie.delete("/movie",summary='删除')
async def movie_delete():
    pass
