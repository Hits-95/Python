print("Enter Number Btn 1 to 30")
count = 0
while count < 3 :
  num = int(input("Enter Number : "))
  if(num == 9):
    print("Win")
    break
  elif num < 9:
    print("Guess no is small than requred.")
  else:
    print("Guess no is small than requred.")
  count += 1
else:
  print("Ooops you try to much time")
