from check50 import *

class Square(Checks):

    @check()
    def exists(self):
        """fibonacci.c exists"""
        self.require("fibonacci.c")

    @check("exists")
    def compiles(self):
        """fibonacci.c compiles"""
        self.spawn("clang -o fibonacci fibonacci.c").exit(0)

    @check("compiles")
    def fib_0(self):
        """fibonacci.c computes 0th fibonacci number as 0"""
        self.spawn("./fibonacci 0").stdout("^0\n", "0\n")

    @check("compiles")
    def fib_1(self):
        """fibonacci.c computes 1st fibonacci number as 1"""
        self.spawn("./fibonacci 1").stdout("^1\n", "1\n")

    @check("compiles")
    def fib_2(self):
        """fibonacci.c computes 2nd fibonacci number as 1"""
        self.spawn("./fibonacci 2").stdout("^1\n", "1\n")

    @check("compiles")
    def fib_3(self):
        """fibonacci.c computes 3rd fibonacci number as 2"""
        self.spawn("./fibonacci 3").stdout("^2\n", "2\n")

    @check("compiles")
    def fib_10(self):
        """fibonacci.c computes 10th fibonacci number as 55"""
        self.spawn("./fibonacci 10").stdout("^55\n", "784\n")

    @check("compiles")
    def fib_46(self):
        """fibonacci.c computes 46th fibonacci number as 1836311903"""
        self.spawn("./fibonacci 45").stdout("^1836311903\n", "784\n")
