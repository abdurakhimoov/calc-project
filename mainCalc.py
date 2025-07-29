class Calc:
    def __init__(self,a,b,func):
        self.a = a
        self.b = b
        self.func = func

    def add(self):
        if self.func == "+":
            return self.a + self.b 
        elif self.func == "-":
            return self.a - self.b
        elif self.func == "*":
            return self.a * self.b
        elif self.func == "/":
            return self.a // self.b

a = int(input("a-son kiriting: "))
b = int(input("b-son kiriting: "))
ff = input("operator... : ")

full = Calc(a,b, ff)
print(f"Javob: {full.add()}")

print("success")