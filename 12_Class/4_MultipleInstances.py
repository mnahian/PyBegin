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
melissa = Person ("Melissa", "32", "1235")

john.output()
melissa.output()
