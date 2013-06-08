#!/bin/env python 
# author: hz_linyu@2013-05-24 1th
# exercise format of python

width = input("Please enter width: ")

price_width = 5
item_width = width - price_width

header_format = '%-*s%*s'
format	      = '%-*s%*.2f'

print '=' * width

print header_format % (item_width,'Item',price_width,'Price')

print '_' * width

print format % (item_width,'Apples',price_width,0.4)
print format % (item_width,'Pears',price_width,1.11)
print format % (item_width,'Cantaloupes',price_width,2.2)
print format % (item_width,'Bananas',price_width,3.3)
print format % (item_width,'Eggs',price_width,1.1)
print format % (item_width,'Pineapple',price_width,4.2)

print '=' * width
