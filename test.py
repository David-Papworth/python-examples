name = (input('Enter name: '))
age = int(input('Enter age: '))

time_till_100 = 100 - age 
year = 2021 + time_till_100

print(year)
print(f'{name} you will turn 100 in the year {year}')

number = int(input('Enter a number: '))
solve = number % 2

if solve == 0:
    print('the number is even')

else:
    print('the number is odd')