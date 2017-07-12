#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee@WeChat --<>
  Purpose: 
  Created: 2017/7/12
"""

a = [5,1,4,3]
print(sorted(a))
print(a)

strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))
print(sorted(strs, reverse=True))

strs = ['CCC', 'aaaa', 'd', 'bb']
print(sorted(strs, key=len))

# "key" argument specifying str.lower function to use for sorting
print(sorted(strs, key=str.lower))

strs = ['Xc', 'zb', 'yd', 'wa']
def my_fun(s):
    return s[-1]

print(sorted(strs, key=my_fun))
print(strs)
strs.sort()
print(strs)

#######tuple
t = (1, 2, 'hi')
print(len(t))
print(t[2])
t = (1, 2, 'bye')

tuple_only_one = ('hi',)

(x, y, z) = (0, 1, 2)
print x, y, z

nums = [1, 2, 3, 4]
squares = [ n * n for n in nums]
print(squares)

strs = ['hello', 'and', 'goodbby']
shouting = [s.upper() + '!!!' for s in strs]
print(shouting)

#select values <=2
nums = [2, 8, 1, 6]
small = [n for n in nums if n<=2]
print(small)

#select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [f.upper() for f in fruits if 'a' in f]
print(afruits)