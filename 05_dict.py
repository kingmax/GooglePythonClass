#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee@wechat --<>
  Purpose: 
  Created: 2017/7/13
"""

d = {}
d['a'] = 'alpha'
d['g'] = 'gamma'
d['o'] = 'omega'

print(d)

print(d['a'])
d['a'] = 6

print('a' in d)

if 'z' in d:
    print(d['z'])
    
print(d.get('z'))

for k in d:
    print(k)
    
for k in d.keys():
    print(k)
    
print(d.values())    
for k in sorted(d.keys()):
    print(k, d[k])
    
print(d.items())    

for k, v in d.items():
    print(k, '>', v)
    
hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s'%hash
print(s)

var = 6
del var

list = ['a', 'b', 'c', 'd']
del list[0]
del list[-2:]
print(list)

del d['o']
print(d)

f = open('utf8_txt.txt')
for line in f:
    print(line)
f.close()

print('-'*30)
for line in open('utf8_txt.txt', 'rU'):
    print(line)

print('-'*30)
import codecs
f = codecs.open('utf8_txt.txt', 'rU', 'utf-8')
for line in f:
    print(line)
f.close()


