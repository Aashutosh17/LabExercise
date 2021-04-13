#Give a three digit number. find the sum of its digit.

number = int(input('enter any three digit num'))
sum_of_digits = sum(int(digit) for digit in str(number))
print(sum_of_digits)


