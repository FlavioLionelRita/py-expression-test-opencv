import re
from .core import Parser

if __name__ == "__main__":
    parser = Parser()

print(parser.solve('"aaa".capitalize()'))

context = {"a":1,"b":2}

op1 = parser.parse('a+1')
op2 = parser.parse('b')
op3 = op1+op2


print(op3.eval({"a":1,"b":2}))
print(op3.eval({"a":5,"b":2}))










