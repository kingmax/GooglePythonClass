#!/usr/bin/env python
#coding:utf-8
"""
  Author:  JasonLee --<>
  Purpose: 
  Created: 2017/7/12
"""

colors = ['red', 'green', 'blue']
print(colors[0])
print(colors[2])
print(len(colors))

b = colors
print(b[1])

c = colors + b
print(c)

squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum)

myList = ['larry', 'curly', 'moe']
if 'curly' in myList:
    print('yay')
    
#print the numbers from 0 through 99
for i in range(100):
    print(i)
    
## Access every 3rd element in a list
i = 0
while i < len(squares):
    print(squares[i])
    i += 3
    
myList.append('shemp')    
myList.insert(0, 'xxx')
myList.extend(['yyy', 'zzz'])
print(myList)
print(myList.index('curly'))

myList.remove('curly')
myList.pop(1)
print(myList)


myList = []
myList.append('a')
myList.append('b')

myList.extend(myList[::-1])
print(myList)

print(myList[1:-1])
myList[0:2] = 'z'
print(myList)