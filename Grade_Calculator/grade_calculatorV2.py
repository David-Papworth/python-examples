def grade():
    maths = int(input('Enter your maths mark: '))
    chemistry = int(input('Enter your chemistry mark: '))
    physics = int(input('Enter your physics mark: '))
    total_mark = maths + chemistry + physics
    average_mark = total_mark / 3
    if average_mark >= 70:
        achieve = "You achieved a grade: A"
    elif average_mark >= 60:
        achieve = "You achieved a grade: B"
    elif average_mark >= 50:
        achieve = "You achieved a grade: C"
    elif average_mark >= 40:
        achieve = "You achieved a grade: D"
    else:
        achieve = "You have failed"
    return f"{achieve}"

print(grade())