# write a program take a input from a user, ask the user age.if  the user age is below 15
# print a message" you're a child",if the user age is greater than 15 and lesser than 40 print a
# message You are adult,if the users age is greater than 40 print a message"you are old"
num=int(input("Enter the number"))
if num<15:
    print('you are a child')
elif num<15 and num>50:
    print('you are adult')
else :
    print('you are old')
