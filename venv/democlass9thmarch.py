# write an program to find am or pm time given by the user
hours=int(input("Enter the time in hours"))
minute=int(input("Enter the time in minutes"))
if (hours>1 and hours<12):
    print("the time is am")
elif(hour>12 and hours<24):
    print("the is is pm")