#!/usr/bin/env python
#coding:utf-8
"""
  Author:  JasonLee --<>
  Purpose: testing
  Created: 2017/7/10
"""

import sys

def print_sys_path():
    for p in sys.path:
        print(p)

def haha():
    print('haha')

def main():
    print_sys_path()
    haha()


if __name__ == '__main__' :
    main()
    print('end')