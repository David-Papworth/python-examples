def Uppercheck (name):
    special_characters = "!@#$%^&*()-+?_=,<>/ "
    list_upper = []
    position = 0
    for char in name:
        if any(c in special_characters for c in char):
            position +=1
        elif char == char.upper():
            n = (char, position)
            list_upper.append(n)
            position += 1
        else:
            position +=1
    return list_upper

print(Uppercheck("HeLlO wOrLd!"))


