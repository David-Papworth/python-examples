name = (input('Enter name: '))
age = int(input('Enter age: '))

time_till_100 = 100 - age 
year = 2021 + time_till_100

print(year)
print(f'{name} you will turn 100 in the year {year}')

number = int(input('Enter a number: '))
solve = number % 2
solve_2 = number % 4

if solve == 0:
    print('the number is even')

else:
    print('the number is odd')

if solve_2 == 0:
    print('this number is divisible by 4')

else:
    print('this number is not divisible by 4')

num = int(input('Enter a numerator: '))
check = int(input('Enter a denominator: '))

solve_3 = num % check

if solve_3 == 0:
    print('the division is possible')

else:
    print('the division is not possible')