# A school decided to replace the desk in three classroom.Each desk sits two students.Given the number of students in each class,print the smallest possible number
#of desks thta can be purchased. The program should read three integers:the  number of student in each of the three classes
#a,b and c respectively.
#In the first test there are three groups.The first group has 20 students and thus neecd 10 desk.The second
#group has 21 students,so they can get by with no fewer than 11 desks.11 desks are also enough for third group of 22 students,
#so we need 32 desks in total
no_student_class1= int(input("Enter the number of students in first class :"))
no_students_class2=int(input("Enter the number of students i n second class :"))
no_students_class3=int(input("Enter the number of students in third class :"))
desk_class1 = (no_students_class1//2)
print(f"The required number of desk for first class is {desk_class1}")
desk_class2=(no_students_class2 // 2)
print(f"The required number of desks for secocnd class is {desk_class2}")
desk_class3=(no_students_class3//2)
print(f"The required number of desks for third is {desk_class3}"

remain_class1=(no_students_class1% 2)
print(f"Remaining desk for first class is {remain_closed1}")
remain_class2 = (no_students_class2 % 2)
print(f"Remaining desk for second class is {remain_closed2}")
remain_class3 =(no_students_class3 % 2)
print(f"remaining desk for third class is {remain_closed3}")
total_desks_in_school=desk_class3+desk_class1+desk_class2+remain_class1+remain_class2+remain_class3
print(f"Total number of desks required in school {total_desks_in_school}")
