#type 1 : pass parent para using cls name...
#parent cls...
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print("Hellow ...",self.fname,self.lname)

#Child cls
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname) #here self required...


#type 2: pass parent para using super() method...
#Child cls...
class Police(Person):
    def __init__(self,fname,lname):
         super().__init__(fname,lname)   #here self NOT required...


