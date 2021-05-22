class Person():
    def __init__(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name +
              " your age is " + self.age +
              " your ID num is " + self.idNum)


john = Person("Nahian", "33", "1232")

print(john.name)
print(john.age)
print(john.idNum)
print(john.output())
