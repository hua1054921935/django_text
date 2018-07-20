#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:
# datetime:18-7-8 下午6:37
# software:
pos = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
for i in range(1,10):
    for j in range(1,10):
        for s in range(len(pos)):
            print([i,j,s])
