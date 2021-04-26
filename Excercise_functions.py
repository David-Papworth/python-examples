Homework = int(input('Enter your Homework mark: '))
Assessment = int(input('Enter your Assessment mark: '))
Final = int(input('Enter your Final exam mark: '))

def student_grade(Homework, Assessment, Final):
    Grade = ((Homework + Assessment + Final) / 175) * 100
    return  Grade 

print(f"your grade is {student_grade(Homework, Assessment, Final)}")