#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:
# datetime:18-7-8 下午6:37
# software:
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
x=12//7
print(x)