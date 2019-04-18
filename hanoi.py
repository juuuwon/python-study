# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 19:38:08 2019

@author: 김주원
"""



        
top = [[] for i in range(3)]
top[0] = [3,2,1]
for i in range(10):
    f, t = map(int ,input().split())
    if top[f]:
        if not top[t] or top[f][-1] < top[t][-1]:
            top[t].append(top[f].pop())
            print(top)