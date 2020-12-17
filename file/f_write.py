#open 'online.txt' in write mode...
fp = open("online.txt","a+")
fp.write("Now Add more content in file \n")
for i in fp:
	print(i)
fp.close()

