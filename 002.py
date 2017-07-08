#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee@WeChat --<>
  Purpose: 
  Created: 2017/7/8
"""

#Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    '''
    Return the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    '''
    result = s * 3
    if exclaim:
        result += '!!!'
    return result

def main():
    print(repeat('Yay', False))
    print(repeat('Woo Hoo', True))
    
    #intentionally make error
    #name = 'guido'
    if name == 'Guido':
        #a slip of the pen
        print(repeet(name) + '!!!')
    else:
        print(repeat('name', 1))

if __name__ == '__main__':
    main()
    from sys import exit
    exit(0)