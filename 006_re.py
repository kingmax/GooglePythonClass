#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee@WeChat --<>
  Purpose: 
  Created: 2017/7/14
"""

import re

# match = re.search(pat, str)

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
if match:
    print('found %s'%match.group())
else:
    print('did not find')
    
#search for pattern 'iii' in string 'piiig'
#all of the pattern must match, but it may appear anywhere
#on success, match.group() is matched text
match = re.search(r'iii', 'piiig')
print(match.group())

match = re.search(r'igs', 'piiig')
if match:
    print(match.group())
else:
    print('not found')
    
# . = any char but \n    
match = re.search(r'..g', 'piiig')
print(match.group())

# \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g')
if match:
    print(match.group())

match = re.search(r'\w\w\w', '@@abcd!!!')
if match:
    print(match.group())
    
# i+ = one or more i's, as many as possible
match = re.search(r'pi+', 'piiig')
if match:
    print(match.group())
    
#find the first/leftmost solution, and within it drives the +
match = re.search(r'i+', 'piigiii')
if match:
    print(match.group()) #ii
    
# \s* = zero or more whitespace chars
pattern = r'\d\s*\d\s*\d'
match = re.search(pattern, 'xx1 2  3xx')
print(match.group())
match = re.search(pattern, 'xx12 3xx')
print(match.group())
match = re.search(pattern, 'xx123xxx')
print(match.group())

# ^ = matches the start of string
match = re.search(r'^b\w+', 'foobar')
if match:
    print(match.group())
else:
    print('Not match')

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
print(match.group())    #b@google

match = re.search(r'[\w.-]+@[\w.]+', str)
print(match.group())

match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))

print('\n')    
#find all
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w.-]+@[\w.]+', str)
for email in emails:
    print(email)
    
f = open('hello.py', 'r') 
strings = re.findall(r'print\(.+', f.read())
f.close()
for string in strings:
    print(string)

print('\r\n')    
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)
for tuple in tuples:
    print(tuple[0])
    print(tuple[1])

str = 'haha, Hello, AAA'
matches = re.findall(r'[ha]', str, flags=re.IGNORECASE)
print(matches)  #['h', 'a', 'h', 'a', 'H', 'A', 'A', 'A']

str = '<b>foo</b> and <i>so on</i>'
pt1 = r'(<.*>)'
matches = re.findall(pt1, str)
print(len(matches)) #1
print(matches)

pt2 = r'<.*?>'
matches = re.findall(pt2, str)
print(len(matches)) #4
print(matches)

matches = re.findall(r'[^</>]\s*', str)
print(matches)  #['b', 'f', 'o', 'o', 'b', ' ', 'a', 'n', 'd ', 'i', 's', 'o ', 'o', 'n', 'i']


#replace
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
#re.sub(pat, replacement, str) returns new string with all replacements
#\1 = group(1), \2 = group(2) in the replacement
new_str = re.sub(r'([\w.-]+)@([\w.]+)', r'\1@163.com', str)
print(new_str)  #purple alice@163.com, blah monkey bob@163.com blah dishwasher


