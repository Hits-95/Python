class Student:
    def __init__(self):
        self.name = ""
        self.mar = ""
        self.eng = ""
        self.hin = ""
        self.total = 0
        self.percentage = 0.0
        self.cls = ""

    # get student data from user..
    def get_Student(self):
        self.name = input("Enter Name             : ")
        self.mar = int(input("Enter Marks of Marathi : "))
        self.eng = int(input("Enter Marks of English : "))
        self.hin = int(input("Enter Marks of Hindi   : "))
        print("========== Enter marks of next student =========")

    # display student..

    def display_stud(self):
        print("  --- Student", self.name, "info ---")
        print("Name       :", self.name)
        print("Marathi    :", self.mar)
        print("English    :", self.eng)
        print("Hindi      :", self.hin)
        print("  --- Result ---")
        print("Total      :", self.total)
        print("Percentage :", self.percentage)
        print("Class      :", self.cls)
        print("========== *** =========")

    # calculate total & percentage
    def cal_result(self):
        self.total = self.mar + self.eng + self.hin
        self.percentage = self.total / 3

    # find class
    def find_cls(self):
        if self.mar < 35 or self.eng < 35 or self.hin < 35:
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
    objs = [Student() for i in range(3)]

    for obj in objs:
        obj.get_Student()
    for obj in objs:
        obj.cal_result()
        obj.find_cls()
        obj.display_stud()
