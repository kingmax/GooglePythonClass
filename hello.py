#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee@WeChat --<>
  Purpose: 
  Created: 2017/7/8
"""
#import modules used here (sys is a very standard one)
import sys

#Gather our code in a main() function
def main():
    '''
    there is docstring
    about main function
    '''
    print('Hello, there %s'%sys.argv[1])
    
def usage():
    '''how to usage this module'''
    print("""
    ------- USAGE -------
     hello.py [your_name]
    """)

    
if __name__ == '__main__':
    #print(sys.version)
    if len(sys.argv) > 1:
        main()
    else:
        usage()