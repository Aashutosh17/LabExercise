# WAP which accepts marks of four subjects and display total marks,percentage and grade.
WAP1=int(input("enter the marks of first subject: "))
WAP2=int(input("enter the marks of second subject:"))
WAP3=int(input("enter the marks of third subject:"))
WAP4=int(input("enter the marks of fourth subject:"))
total_marks=(WAP2+WAP4+WAP3+WAP1)
print(f"the total marks {total_marks}")
percentage=total_marks/400*100
if percentage>=80 and percentage<=100:
    print("you have scored A+")
elif percentage>=60 and percentage<=79:
    print("you have secured A grade")
elif percentage>=40 and percentage<=59:
    print("you have secured b+ grade")
else:
    print("you have failed")