#!/bin/env python

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

ending = ['st','nd','rd'] + 17 * ['th'] \
	+ ['st','nd','rd'] + 7 * ['th'] \
	+ ['st']


yeah	= raw_input('Yeah: ')
month	= raw_input('Month (1-12): ')
day	= raw_input('Day (1-31): ')

month_number = int(month) 
day_number   = int(day) 

month_name  = months[month_number-1]
day_name    = day + ending[day_number-1]

print  month_name + ' ' + day_name + ' ' +  yeah

