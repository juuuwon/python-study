# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:07:05 2019

@author: 김주원
"""




bubble=[3,8,0,1,4,2,9,5,7,6]
a=0
front=0
back=1
temp=0

while a<10:
    while back<10:
        if bubble[front]>bubble[back]:
          temp=bubble[back]
          bubble[back]=bubble[front]
          bubble[front]=temp
          front+=1
          back+=1
         
          
        else:
            front+=1
            back+=1
            
            

    a+=1
    front=0
    back=1
print(bubble)
print("-------------------------------------------------------------------")


list=[2,5,3,6,7,8,9,1,0,4]

a=0
i=0
temp=0
while a<10:
    while i<9:
        if list[i]>list[i+1]:
            temp=list[i+1]
            list[i+1]=list[i]
            list[i]=temp
            i+=1
        else:
            i+=1
            
    a+=1
    i=0
    
print(list)
            




