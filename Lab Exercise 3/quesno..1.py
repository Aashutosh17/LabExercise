# Write a python function to find the max of three numbers
def maxnumber(one,two,three):
    if one>two and one>three:
        print(f"the first number is maximum")
    elif two>one and two>three:
        print("the second number is maximum")
    else:
        print('the third number is greater')
first_number=int(input('enter the first num:'))
second_number=int(input('enter the second num:'))
third_number=int(input('enter the third number:'))
max_number=(first_number,second_number,third_number)