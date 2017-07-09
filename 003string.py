#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee@WeChat --<>
  Purpose: 
  Created: 2017/7/9
"""

s = 'hi'
print(s[1]) #i
print(len(s))
print(s+'there')

pi = 3.14
txt = 'The value of pi is ' + str(pi)
print(txt)

raw = r'this\t\n and that'
print(raw)

multi = '''It was the best of times.
It was the worst of times.'''
print(multi)

s = ' Hello World '
print(s.lower())
print(s.upper())
print(s.strip())
print(s.isalpha())
print(s.isdigit())
print(s.isspace())
print(s.islower())
print(s.isupper())
print(s.startswith('other'))
print(s.endswith('end?'))
print(s.find('Hello'))
print(s.replace('World', 'Jason'))
print(s.split(' '))
print('---'.join(['aaa', 'bbb', 'ccc']))

s = 'Hello'
print(s[1:4])
print(s[1:])
print(s[:])
print(s[1:100])
print(s[-1])
print(s[-4])
print(s[:-3])
print(s[-3:])

# % operator
text = "%d little pigs come out or I'll %s and %s and %s"%(3, 'huff', 'puff', 'blow down')

#add parens to make the long-line work
text = ("%d little pigs come out or I'll %s and %s and %s" %
        (3, 'huff', 'puff', 'blow down'))
print(text)

ustring = u'A unicode \u018e string \Xf1'
bs = ustring.encode('utf-8')
print(bs)
t = unicode(bs, 'utf-8' )
print(t == ustring)

#if 
speed = 85
mood = ''
if speed >= 80:
    print('Licence and registration please')
    if mood == 'terrible' or speed >= 100:
        print('You have the right to remain silent')
    elif mood == 'bad' or speed >= 90:
        print("I'm going to have to write you a ticked")
        write_ticket()
    else:
        print("Let's try to keep it under 80 ok?")