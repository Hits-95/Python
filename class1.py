class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("hellow ", self.name)
        print("Age : ", self.age)


if __name__ == "__main__":
    obj = Person("hitesh", 54)
    print(obj.__dict__)
