#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee@WeChat --<>
  Purpose: 
  Created: 2017/7/8
"""

import sys

def main():
    print('Hello, there %s'%sys.argv[1])
    
def usage():
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