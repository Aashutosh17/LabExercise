#2 2.Write a program that reads the length of the base  and the height of a right-angled  triangle and print the area.Every number is given on a seperate line.
Height=float(input('Enter the height of the triangle'))
length=float(input("Enter the length of the triangle"))
Area=(length*Height)//2
#the floor division // rounds the result down to the nearest whole number
print(f'The area of right angeled triangle is {Area}')