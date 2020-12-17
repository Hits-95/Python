class Employee():
    """
    class instance & decorater
    """
    temp = 5

    @classmethod
    def change(cls, newdata):   # here diff btn self & cls . cls is parent l.e class object like Employee() & self is private object like obj()
        cls.temp = newdata


if __name__ == "__main__":
    Employee.change(10)
    hitesh = Employee()

    print(Employee.__doc__)
    print("cls change : ", Employee.temp)
    print("hitesh change : ", Employee.temp)

    # changes apply on hitesh obj also bcoz cls Employee decorater is created ...
