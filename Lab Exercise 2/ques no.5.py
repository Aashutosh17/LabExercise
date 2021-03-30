#if name is less than 3 characters long- name must be at least 3 characters otherwise
#if its more than 50 character -name must be maximum 50 characters otherwise - name looks good
user_name=(input("Enter the name"))
length1=len(user_name)
if length1<3:
     print('name is not applicable')
elif length1>50:
     print('name is not applicable')
else:
    print("name is applicable")