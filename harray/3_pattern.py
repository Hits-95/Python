num = int(input("Enter value of n : ")) + 1
flag = bool(int(input("Enter 1 or 0 : ")))
if flag :
  for i in range(num) :
    for j in range(i) :
      print("* ", end = " ")
    print()
else :
  for i in range(num, 0, -1) :
    for j in range(i) :
      print("* ", end = " ")
    print()
