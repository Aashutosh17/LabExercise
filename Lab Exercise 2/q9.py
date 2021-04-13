# check whether the given year is leap year or not if its not leap
# year print it as common year

year=int(input('Enter the year:'))
if (year % 4==0 and year % 100 !=0 or year % 400 ==0):
    print("this is a leap year!")
else:
    print("its a common year")
