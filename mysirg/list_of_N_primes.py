#create a list of 1st N prime numbers

#genrate next prime def...
def nextPrime(num):
    while True:
        num += 1
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            return num

#genrate list of primes
def primeProducer(n):
    num,count = 1,1
    while count <= n:
        num = nextPrime(num)
        yield num
        count += 1

#main
num = int(input("Enter N :"))
print([x for x in primeProducer(num)])
