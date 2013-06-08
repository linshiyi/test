#!/bin/env python
#exercise of check user/passwd
#hz_linyu@20130506

database = [
    ['linyu', '1111'],
    ['zhouqiong', '2222'],
    ['arkey', 'arkey']
]

user = raw_input("User: ")
passwd = raw_input("Password: ")

if [user, passwd] in database: print 'Access granted' && exit
if uesr in database: print 'Wrong password !!' && exit
print 'Wrong User'

