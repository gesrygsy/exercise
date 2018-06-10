class Numbers:
    def __init__(self):
        self.list_n = []
        self.n = input("Input a number:")
        self.n = int(self.n)
        for i in range(self.n):
            self.list_n.append(i+1)
        print(self.list_n)

    def fizzbuzz(self):
        self.list_fb = []
        for i in range(1, self.n+1):
            if i % 3 == 0:
                i = "fizz"
            elif i % 5 == 0:
                i = "buzz"
            self.list_fb.append(i)
        print(self.list_fb)


numbers = Numbers()
numbers.fizzbuzz()
