def even_between (number_lower, number_upper):
    count = number_upper
    even_numbers = []
    while count >= number_lower and count <= number_upper:
        if (int(count // 1000)) % 2 == 0:
            if (int(count // 100)) % 2 == 0:
                if (int(count // 10)) % 2 == 0:
                    if count % 2 == 0:
                        even_numbers.append(count)
        count -= 1
    return even_numbers

print(even_between(10, 30))