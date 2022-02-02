'''
Created on TUES Oct 10 14:14:27
@author: eesha.kavuri
'''
import random
import datetime
birthday =[]
i = 0
while i <50:
    year = random.randint(1895,2021)
    if year%4==0 and year%100!=0 or year%400==0:
        leap = 1
    else:
        leap = 0
    month = random.randint(1,12)
    if month==2 and leap==1:
        day = random.randint(1,29)
    elif month==2 and leap==0:
        day = random.randint(1,28)
    elif month==7 or month==8:
        day = random.randint(1,31)
    elif month%2!=0 and month<7:
        day = random.randint(1,31)
    elif month%2==0 and month>7 and month<12:
        day = random.randint(1,31)
    else:
        day = random.randint(1,30)
    dd = datetime.date(year,month,day)
    day_of_year = dd.timetuple().tm_yday
    i+=1
    birthday.append(day_of_year)
    
birthday.sort()
i = 0
while i<50:
      print(birthday[i])
      i+=1

'''
%Y Year
%B Month
%d date (1-31)
%w day number of the week(0 to 6)
%W week of the year (1 to 52)
%A day (Sunday, Monday etc)
%j day of the year( 1 to 365(366))

>>> import datetime
>>> datetime.date.today()
datetime.date(2021, 10, 7)
>>> datetime.date.today().strftime('Y') #include '%'
'Y'
>>> datetime.date.today().strftime('%Y')
'2021'
>>> datetime.date.today().strftime('%M')
'00'
>>> datetime.date.today().strftime('%B')
'October'
>>> datetime.date.today().strftime('%d')
'07'
>>> datetime.date.today().strftime('%W') #week number
'40'
>>> datetime.date.today().strftime('%w') #week day of the week
'4'
>>> datetime.date.today().strftime('%j') #week day of the year
'280'
>>> datetime.date.today().strftime('%A') #week day of the year
'Thursday'
>>> datetime.datetime.now()
datetime.datetime(2021, 10, 7, 15, 4, 59, 162700)
'''
