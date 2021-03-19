import random
num=random.randint(1,100)
guess=int(input("please guess the number?"))
while num !=guess:
    guess=int(input('uffs !! try agian :guess again:'))
else:
    print('Congratulation!!! U r right')