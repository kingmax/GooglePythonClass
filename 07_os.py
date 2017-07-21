#!/usr/bin/env python
#coding:utf-8
"""
  Author:  iJasonLee@WeChat --<>
  Purpose: 
  Created: 2017/7/17
"""

import os
import sys

path = r'D:\git\googlePythonClass'
filenames = os.listdir(path)
print(filenames)
fullpathfilenames = [os.path.join(path,f) for f in filenames]
print(fullpathfilenames)

for p in fullpathfilenames:
    print(os.path.abspath(p))
    
f = fullpathfilenames[-1]
print(f) #D:\git\googlePythonClass\utf8_txt.txt
print(os.path.dirname(f))
print(os.path.basename(f))
print(os.path.exists(f))

if not os.path.exists('d:\\temp_dir'):
    os.mkdir('d:\\temp_dir')
if not os.path.exists('d:\\temp1'):
    os.makedirs('d:\\temp1\\temp2\\temp3\\')

import shutil
shutil.copy('utf8_txt.txt', 'd:\\temp1\\temp2\\temp3\\txt.txt')

def printdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print(filename)
        print(os.path.join(dir, filename))
        print(os.path.abspath(os.path.join(dir, filename)))
        
print('\n')        
printdir(path)


try:
    filename = 'filename.txt'
    f = open(filename, 'rU')
    text = f.read()
    f.close()
except IOError as ex:
    print(ex.message)
    sys.stderr.write('problem reading: ' + filename)


# HTTP
url = r'http://www.baidu.com'

import urllib

ufile = urllib.urlopen(url)
text = ufile.read()
#print(text)

info = ufile.info()
print(info)

baseurl = ufile.geturl()
print(baseurl)

urllib.urlretrieve(url, 'urlretrieved')

import urlparse
print(urlparse.urljoin(url, 'music'))

def wget(url):
    '''
    Given a url, try to retrieve it,
    If it's text/html,
    print its base url and its text
    '''
    ufile = urllib.urlopen(url)
    info = ufile.info()
    if info.gettype() == 'text/html':
        print('base url:' + ufile.geturl())
        text = ufile.read()
        print(text)

print('\n\n\n')        
wget(url)        

## Version that uses try/except to print an error message 
## if the urlopen() fails
def wget2(url):
    try:
        ufile = urllib.urlopen(url)
        if ufile.info().gettype() == 'text/html':
            print(ufile.read())
    except IOError:
        print('problem reading url: ' + url)

print('-'*60)        
wget2(url)        