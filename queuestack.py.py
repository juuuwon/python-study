# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:42:37 2019

@author: 김주원

"""

queue=[]
b=0
while b<10:
    queue.append(input())
    b+=1
    print(queue)
c=len(queue)
print("pop")
while c!=0:
    queue.pop(0)
    c-=1
    
    print(queue)
    

stack=[]
b=0
while b<10:
    stack.insert(0,input())
    b+=1
    print(stack)
c=len(stack)
print("pop")
while c!=0:
    stack.pop(0)
    c-=1
    print(stack)
        
    