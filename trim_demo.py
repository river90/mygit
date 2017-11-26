# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 10:50:07 2017

@author: Administrator
"""
def trim(s):
    i=0
    le=len(s)
    if le==0:
        return ''
    j=le-1
    for x in s:
        if x!=' ':
           
           break
        i+=1
    for y in s[::-1]:
        if y!=' ':
            break
        j-=1
    if i>j: 
        return ''
    else:
        return s[i:j+1] 
    
        
        
if trim('hello  ') != 'hello':
    print(trim('hello  '))
    print("9989")
    print('测试失败!')
elif trim('  hello') != 'hello':
    print("99349")
    print(trim('  hello'))
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('') != '':
    print("9999")
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')