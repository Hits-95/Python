class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


    # out-put
mycls = MyNumber()
myiter = iter(mycls)

print("type 1")
for x in range(5):
    print(next(myiter))


# Stop Iterator
class MyNumber2:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


print("\ntype 2")
mycls = MyNumber()
myiter = iter(mycls)
for x in myiter:
    print(x)
