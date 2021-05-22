class Person():
    def __init__(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("Your name is " + self.name +
              " your age is " + self.age +
              " your ID num is " + self.idNum)


class Child(Person):
    pass


shifu = Child("Shifu", "7", "122")
shifu.output()
