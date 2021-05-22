class Person():
    def insert(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum

    def output(self):
        print("You name is " + self.name +
              " your age is " + self.age +
              " your ID Num is " + self.idNum)


j = Person()
j.insert("Mehedi", "34", "1345")
j.output()
