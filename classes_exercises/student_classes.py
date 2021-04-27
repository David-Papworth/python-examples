class Students:
    def __init__(self, name, age, cl):
        self.name = name 
        self.age = age 
        self.cl = cl 
    def average_test_store(self, test1, test2, test3):
        return f"{self.name} average test score is {(test1 + test2 + test3) / 3}"

tim = Students("Tim", "12", "history")
dave = Students("Dave", "13", "maths")

print(tim.name)
print(tim.age)
print(tim.cl)

print(dave.name)
print(dave.age)
print(dave.cl)

print(dave.average_test_store(10, 11, 12))