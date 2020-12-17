def drive():
    age = int(input("Enter ypur age : "))
    #conditions...
    if age > 7 and age <= 100:
        if age < 18:
            print("you can't  drive.")
        elif age == 18:
            print("we will think about that.")
        else :
            print("you can drive.")
    else:
        print("invalid input")
#calling....
drive()

	
	
