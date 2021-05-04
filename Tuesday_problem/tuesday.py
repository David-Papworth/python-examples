def Fibonacci (number):
    used_number = int(number)
    if used_number < 0:
        return 'please add a number greater than 0'
    elif used_number == 0:
        return '0'
    elif used_number == 1:
        return '1'
    else:
        n1 = 0
        n2 = 1
        for x in range(used_number - 1):
            n3 = n1 + n2
            n1 = n2 
            n2 = n3
        return n3 

print(Fibonacci(9.2))