#oprations method...
def oprn(str, num1, num2):
    #multiplication..
    #cond 44 * 3 = 555
    if(str == "mul"):
        if(num1 == 44 and num2 == 3 ):
            print("Result : ",555)
        else:
            print("Result : ",num1 * num2)

#calculation method...
def cal():
    str = input("1) mul\n2) div\n3) add\n4) sub \nEnter opration : ")
    num1 = int(input("Enter number1 : "))
    num2 = int(input("Enter number2 : "))
    oprn(str, num1, num2)
#calling...
cal()
    
