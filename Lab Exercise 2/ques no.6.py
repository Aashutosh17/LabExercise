#Weight converter:
#Input the weight of a person in either kg or lbs .If the person provides his/her weight in kgs then convert it into
#lbs else convert it into kgs.

person_weight=int(input("Enter the weight"))
person_choice=input("if you want weight in kg or pound")
if person_choice=='kg':
    print(f'the weight in pound{person_weight*2.20462262 }')
elif person_choice=='pound':
    print(f'the weight in kg{person_weight*0.45359237} ')
else:
    print("it is not recognized")