

# multiplication table function
def mul_table(num):
    for i in range (1,11):
        product=num*i
        print(f'{num}*{i}={product}')

num=int(input('Enter the value for multiplication'))
mul_table(num)