#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:
# datetime:18-7-8 下午6:37
# software:
import time
import random
import heapq
import xml.etree.ElementTree as ET


# pos = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
# for i in range(1,5):
#     pos.append([3,i])
#     pos.append(pos.index([3,i]))
# # for i in range(1,10):
# #     for j in range(1,10):
# #         for s in range(len(pos)):
# #             print([i,j,s])
# print(pos)
#
#
# [nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5)-0.5, y-4,(d * (j - 0.5) + 0.5) * pos[s][1]-0.5])+1,
# nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5)-0.5, y-4,(d * (j - 0.5) + 0.5) * pos[s][1]+0.5])+1,
# nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5)+0.5, y-4,(d * (j - 0.5) + 0.5) * pos[s][1]-0.5])+1,
# nodes_list2.index([pos[s][0] * (d * (i - 0.5) + 0.5)+0.5, y-4,(d * (j - 0.5) + 0.5) * pos[s][1]+0.5])+1]
# list1=[1,2,3,4,5,6,4,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]
# start=time.time()
# list1.append(1)
# end=time.time()
# print(end-start)
#
# list1=[]
# list2=[]
# for i in range(10000):
#     a = random.randint(1, 10000)
#     if a==666 or a==888:
#
#         list1.append('恭喜发财'+str(i))
#
#     else:
#
#         list2.append('谢谢回顾'+str(i))
# print(list1)
tree=ET.parse('aaa.xml')
root = tree.getroot()
for i in root:
    print(i)