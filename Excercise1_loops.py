my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for x in my_list:
    if x < 5:
        print(x)

my_list_2 = [x for x in my_list if x < 5]
print(my_list_2)

number = int(input('Enter a number: '))
for x in my_list:
    if x < number:
        print(x)
my_list_3 = [x for x in my_list if x < number]
print(my_list_3)