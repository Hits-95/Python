class Student:
    def __init__(self):
        self.rollno = 0
        self.name = ""
        self.city = ""
        self.java = 0
        self.php = 0
        self.python = 0
        self.nodejs = 0
        self.total = 0
        self.percentage = 0.0
        self.cls = ""

    # display student..
    def get_stud(self, rollno, name, city, java, php, python, nodejs):
        self.rollno = rollno
        self.name = name
        self.city = city
        self.java = java
        self.php = php
        self.python = python
        self.nodejs = nodejs

    def display_stud(self):
        print("  --- Student", self.name, "info ---")
        print("Name       :", self.name)
        print("java       :", self.java)
        print("php        :", self.php)
        print("python     :", self.python)
        print("NodeJs     :", self.nodejs)
        print("  --- Result ---")
        print("Total      :", self.total)
        print("Percentage :", self.percentage)
        print("Class      :", self.cls)
        print("========== *** =========")

    # calculate total & percentage
    def cal_result(self):
        self.total = self.java + self.php + self.python + self.nodejs
        self.percentage = self.total / 4

    # find class
    def find_cls(self):
        if self.java < 35 or self.php < 35 or self.python < 35 or self.nodejs < 35:
            self.cls = "Fail"
        elif self.percentage >= 70:
            self.cls = "Distinction"
        elif self.percentage >= 60:
            self.cls = "1st Class"
        elif self.percentage >= 50:
            self.cls = "2nd Class"
        elif self.percentage >= 40:
            self.cls = "3rd Class"
        else:
            self.cls = "Pass Class"


# main method
if __name__ == "__main__":
    obj = Student()
    obj.get_stud(1, "hitesh", "malegaon", 54, 54, 35, 65)
    obj.cal_result()
    obj.find_cls()
    obj.display_stud()

    # objs = [Student() for i in range(3)]

    # for obj in objs:
    #     obj.get_Student()
    # for obj in objs:
    #     obj.cal_result()
    #     obj.find_cls()
    #     obj.display_stud()
